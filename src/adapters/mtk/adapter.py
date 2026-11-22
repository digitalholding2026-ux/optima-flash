"""Adaptateur MediaTek : détection passive et lecture non destructive.

Frontière avec le moteur GPL (docs/ARCHITECTURE.md §2) : ``mtkclient`` n'est
**jamais** importé. Il est lancé en sous-processus via
:func:`src.core.runner.run_subprocess`, avec une commande issue de la
configuration (``binaries.mtkclient_cmd``, cf. ``config.yaml.example``).

La détection n'appelle pas mtkclient : ``mtk devices`` liste les appareils
*pris en charge par le loader*, pas ceux qui sont branchés. La détection
repose donc sur l'énumération USB passive (:mod:`src.adapters.usb.detector`).
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any, Protocol

from src.adapters.usb.detector import detect_devices
from src.core.config import AppConfig
from src.core.runner import run_subprocess
from src.core.types import (
    ChipsetType,
    DeviceInfo,
    OperationError,
    OperationFailure,
    OperationResult,
)

__all__ = ["MediaTekAdapter", "MediaTekAdapterProtocol", "MediaTekAdapterStub"]

_MAX_RAW_CHARS = 4000
_TRUNCATION_MARKER = "...[tronqué]"

_PRINTGPT_TIMEOUT_S = 60.0
_TARGETCONFIG_TIMEOUT_S = 30.0

_CMD_MISSING = "MTKCLIENT_CMD_MISSING"
_NOT_FOUND = "MTKCLIENT_NOT_FOUND"
_TIMEOUT = "MTKCLIENT_TIMEOUT"

# Sortie texte de « mtk printgpt » (mtkclient/Library/Partitions/__init__.py) :
#   "preloader:          Offset 0x0000000000000000, Length 0x0000000000040000, Flags 0x0"
_PARTITION_RE = re.compile(
    r"^(?P<name>.+?):\s+Offset 0x(?P<offset>[0-9a-fA-F]+),"
    r"\s+Length 0x(?P<length>[0-9a-fA-F]+),\s+Flags 0x(?P<flags>[0-9a-fA-F]+)",
    re.MULTILINE,
)
# Sortie de « mtk gettargetconfig » (mtkclient/Library/mtk_preloader.py) :
#   "... - \tCPU:\t\t\tmt6765(Helio P35)"
#   "... - HW code:\t\t\t0x1234"
#   "... - \tHW Ver:\t\t\t0x0" / "... - \tSW Ver:\t\t\t0x1"
_CPU_RE = re.compile(r"CPU:\s*(?P<cpu>[^\s(]+)", re.IGNORECASE)
_HW_CODE_RE = re.compile(r"HW code:\s*(?P<hw>0x[0-9a-fA-F]+)", re.IGNORECASE)
_HW_VER_RE = re.compile(r"HW Ver(?:sion)?:\s*(?P<hw>0x[0-9a-fA-F]+)", re.IGNORECASE)
_SW_VER_RE = re.compile(r"SW Ver(?:sion)?:\s*(?P<sw>0x[0-9a-fA-F]+)", re.IGNORECASE)


def _truncate(text: str, limit: int = _MAX_RAW_CHARS) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + _TRUNCATION_MARKER


def _search(pattern: re.Pattern[str], text: str) -> str | None:
    match = pattern.search(text)
    if match is None:
        return None
    return match.group(1).strip() or None


def _parse_partitions(stdout: str) -> list[str]:
    names: list[str] = []
    for match in _PARTITION_RE.finditer(stdout):
        name = match.group("name").strip()
        if name and name not in names:
            names.append(name)
    return names


class MediaTekAdapterProtocol(Protocol):
    """Contrat d'un adaptateur MediaTek (détection, lecture, flash, FRP)."""

    def detect(self) -> list[DeviceInfo]:
        """Détecte les appareils MediaTek branchés."""
        ...

    def read_info(self, device: DeviceInfo) -> dict[str, Any]:
        """Lit les informations non destructives de l'appareil."""
        ...

    def flash_partition(
        self, device: DeviceInfo, partition: str, image_path: Path
    ) -> OperationResult:
        """Écrit une image sur une partition."""
        ...

    def erase_frp(self, device: DeviceInfo, proof_hash: str) -> OperationResult:
        """Efface le FRP après preuve écrite."""
        ...


class MediaTekAdapter(MediaTekAdapterProtocol):
    """Adaptateur MediaTek réel, sans import de mtkclient.

    :param config: configuration applicative ; ``binaries.mtkclient_cmd`` fournit
        la commande du moteur (ex. ``[".venv-mtk/Scripts/mtk.exe"]``).
    :param logger: logger applicatif ; les sorties brutes restent dans
        :class:`~src.core.runner.SubprocessResult`, pas dans les journaux.
    """

    def __init__(self, config: AppConfig, logger: logging.Logger) -> None:
        self._config = config
        self._logger = logger

    def _mtkclient_cmd(self) -> list[str]:
        if not self._config.mtkclient_cmd:
            raise OperationFailure(
                OperationError(
                    "Commande mtkclient non configurée : renseignez binaries.mtkclient_cmd.",
                    code=_CMD_MISSING,
                )
            )
        return list(self._config.mtkclient_cmd)

    def detect(self) -> list[DeviceInfo]:
        """Retourne les appareils MediaTek branchés.

        ``mtk devices`` ne convient pas : il énumère les appareils supportés par
        le loader, indépendamment du matériel connecté. La détection s'appuie sur
        l'énumération USB passive, qui ne réalise aucun transfert.
        """
        devices = detect_devices()
        return [device for device in devices if device.chipset is ChipsetType.MTK]

    def read_info(self, device: DeviceInfo) -> dict[str, Any]:
        """Lit GPT et configuration cible via deux sous-processus mtkclient.

        Aucun appel réseau, aucune écriture. Un code retour non nul n'est pas une
        erreur d'exécution : les champs concernés valent ``None`` et la sortie
        brute reste consultable.

        :raises OperationFailure: si le binaire est introuvable
            (``FileNotFoundError``) ou si les deux commandes dépassent leur délai.
        """
        cmd = self._mtkclient_cmd()
        self._logger.debug(
            "mtk_read_info",
            extra={
                "event": "mtk_read_info",
                "operator": "mtk_adapter",
                "payload": {"device_key": device.key},
            },
        )

        try:
            gpt = run_subprocess(
                cmd=[*cmd, "printgpt"], timeout_s=_PRINTGPT_TIMEOUT_S, logger=self._logger
            )
            target = run_subprocess(
                cmd=[*cmd, "gettargetconfig"],
                timeout_s=_TARGETCONFIG_TIMEOUT_S,
                logger=self._logger,
            )
        except FileNotFoundError as exc:
            raise OperationFailure(
                OperationError(
                    "mtkclient est introuvable. Vérifiez binaries.mtkclient_cmd.",
                    code=_NOT_FOUND,
                    detail=str(exc),
                )
            ) from exc

        if gpt.timed_out and target.timed_out:
            raise OperationFailure(
                OperationError(
                    "mtkclient n'a répondu à aucune commande (délai dépassé).",
                    code=_TIMEOUT,
                    details={
                        "printgpt_timeout_s": _PRINTGPT_TIMEOUT_S,
                        "gettargetconfig_timeout_s": _TARGETCONFIG_TIMEOUT_S,
                    },
                )
            )

        return {
            "cpu": _search(_CPU_RE, target.stdout),
            "hw_code": _search(_HW_CODE_RE, target.stdout),
            "hw_ver": _search(_HW_VER_RE, target.stdout),
            "sw_ver": _search(_SW_VER_RE, target.stdout),
            "partitions": _parse_partitions(gpt.stdout),
            "printgpt_returncode": gpt.returncode,
            "gettargetconfig_returncode": target.returncode,
            "raw_stdout": _truncate(gpt.stdout + "\n" + target.stdout),
            "raw_stderr": _truncate(gpt.stderr + "\n" + target.stderr),
        }

    def flash_partition(
        self, device: DeviceInfo, partition: str, image_path: Path
    ) -> OperationResult:
        raise NotImplementedError("Flash MediaTek — implémentation prévue au Prompt 3.4.")

    def erase_frp(self, device: DeviceInfo, proof_hash: str) -> OperationResult:
        raise NotImplementedError("Effacement FRP MediaTek — implémentation prévue au Prompt 3.4.")


class MediaTekAdapterStub(MediaTekAdapterProtocol):
    """Bouchon historique : contrat uniquement, aucune logique métier."""

    def detect(self) -> list[DeviceInfo]:
        raise NotImplementedError("Module MediaTek — implémentation prévue au Prompt 3.")

    def read_info(self, device: DeviceInfo) -> dict[str, Any]:
        raise NotImplementedError("Module MediaTek — implémentation prévue au Prompt 3.")

    def flash_partition(
        self, device: DeviceInfo, partition: str, image_path: Path
    ) -> OperationResult:
        raise NotImplementedError("Module MediaTek — implémentation prévue au Prompt 3.")

    def erase_frp(self, device: DeviceInfo, proof_hash: str) -> OperationResult:
        raise NotImplementedError("Module MediaTek — implémentation prévue au Prompt 3.")