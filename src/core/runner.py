"""Exécution de sous-processus neutres (mtkclient, edl, outils tiers).

Brique imposée par docs/ARCHITECTURE.md §2 : les moteurs GPL ne sont **jamais**
importés ni liés au cœur applicatif, ils sont lancés comme des sous-processus
séparés via leur CLI officielle.

Garanties :

* 100 % bibliothèque standard, aucune dépendance ajoutée ;
* ``shell=False`` obligatoire, aucune chaîne de commande concaténée ;
* texte uniquement : ``text=True``, ``encoding="utf-8"``, ``errors="replace"``
  (un outil Windows peut émettre du CP1252, l'encodage est absorbé sans planter) ;
* aucun ``stdin`` alimenté, aucune capture binaire ;
* aucun ``print`` : journalisation optionnelle via ``logging.Logger`` ;
* aucun accès réseau, aucun import de ``mtkclient`` / ``edl`` / ``usb`` ;
* aucune exception pour les cas nominaux (timeout, annulation, code non nul).

Limitation connue (Windows) : ``Popen.kill()`` ne tue que le processus direct.
Les sous-processus enfants éventuels du processus lancé ne sont pas terminés et
peuvent conserver les pipes ouverts. À traiter plus tard si un moteur se met à
spawner des enfants (job object Windows).
"""

from __future__ import annotations

import logging
import subprocess
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from src.core.types import OperationResult, OperationStatus

__all__ = [
    "MAX_PAYLOAD_CHARS",
    "TRUNCATION_MARKER",
    "SubprocessResult",
    "run_subprocess",
    "to_operation_result",
]

MAX_PAYLOAD_CHARS = 2000
TRUNCATION_MARKER = "...[tronqué]"


@dataclass(frozen=True)
class SubprocessResult:
    """Résultat brut d'un sous-processus, indépendant de tout moteur."""

    cmd: tuple[str, ...]
    returncode: int | None
    stdout: str
    stderr: str
    duration_ms: int
    timed_out: bool
    cancelled: bool


@dataclass
class _KillState:
    """Bordereau mutable partagé entre le fil de surveillance et l'appelant."""

    timed_out: bool = False
    cancelled: bool = False


def _terminate(proc: subprocess.Popen[str]) -> None:
    try:
        proc.kill()
    except OSError:
        pass


def _start_watcher(
    proc: subprocess.Popen[str],
    timeout_s: float | None,
    cancel_event: threading.Event | None,
    state: _KillState,
) -> threading.Thread | None:
    """Surveille annulation et délai ; le premier déclenché tue le processus."""
    if timeout_s is None and cancel_event is None:
        return None

    def _watch() -> None:
        if cancel_event is not None:
            if cancel_event.wait(timeout=timeout_s):
                if proc.poll() is None:
                    state.cancelled = True
                    _terminate(proc)
                return
        elif timeout_s is not None:
            time.sleep(max(0.0, timeout_s))
        else:
            return
        if timeout_s is not None and proc.poll() is None:
            state.timed_out = True
            _terminate(proc)

    thread = threading.Thread(target=_watch, name="optima-runner-watch", daemon=True)
    thread.start()
    return thread


def run_subprocess(
    cmd: list[str],
    *,
    timeout_s: float | None = None,
    cwd: Path | None = None,
    cancel_event: threading.Event | None = None,
    env: dict[str, str] | None = None,
    logger: logging.Logger | None = None,
) -> SubprocessResult:
    """Exécute ``cmd`` sans shell et retourne sa sortie texte.

    :param cmd: argv complet ; ``cmd[0]`` est le binaire, jamais une ligne shell.
    :param timeout_s: délai maximal en secondes ; à l'expiration le processus
        est tué et ``timed_out`` vaut ``True``. Les enfants du processus ne sont
        pas tués (limitation Windows documentée en tête de module).
    :param cwd: répertoire de travail ; ``None`` pour l'hériter.
    :param cancel_event: si fourni et déclenché, le processus est tué et
        ``cancelled`` vaut ``True``. Si ``timeout_s`` et ``cancel_event`` sont
        fournis, le premier déclenché gagne.
    :param env: environnement du processus ; ``None`` pour l'hériter.
        Fournir un dict remplace l'environnement (sémantique de ``Popen``).
    :param logger: logger applicatif optionnel ; aucun journal par défaut.

    :raises FileNotFoundError: si ``cmd[0]`` est introuvable (erreur système,
        volontairement non absorbée pour que l'adaptateur la traduise).
    """
    started = time.monotonic()
    proc: subprocess.Popen[str] = subprocess.Popen(
        list(cmd),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False,
        cwd=cwd,
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    state = _KillState()
    watcher = _start_watcher(proc, timeout_s, cancel_event, state)
    stdout, stderr = proc.communicate()
    if watcher is not None:
        watcher.join(timeout=1.0)

    duration_ms = int((time.monotonic() - started) * 1000)
    result = SubprocessResult(
        cmd=tuple(cmd),
        returncode=None if state.timed_out or state.cancelled else proc.returncode,
        stdout=stdout or "",
        stderr=stderr or "",
        duration_ms=duration_ms,
        timed_out=state.timed_out,
        cancelled=state.cancelled,
    )

    if logger is not None:
        logger.info(
            "subprocess_finished",
            extra={
                "event": "subprocess_finished",
                "operator": "runner",
                "payload": {
                    "cmd": list(result.cmd),
                    "returncode": result.returncode,
                    "duration_ms": result.duration_ms,
                    "timed_out": result.timed_out,
                    "cancelled": result.cancelled,
                    "stdout_chars": len(result.stdout),
                    "stderr_chars": len(result.stderr),
                },
            },
        )
    return result


def _truncate(text: str) -> str:
    if len(text) <= MAX_PAYLOAD_CHARS:
        return text
    return text[:MAX_PAYLOAD_CHARS] + TRUNCATION_MARKER


def to_operation_result(
    sr: SubprocessResult,
    *,
    success_message: str = "OK",
    payload: dict[str, Any] | None = None,
    operation: str = "subprocess",
    timeout_s: float | None = None,
) -> OperationResult:
    """Convertit un ``SubprocessResult`` en ``OperationResult`` typé.

    Ne lève jamais ``OperationFailure`` : le statut est porté par le résultat.
    ``OperationFailure`` reste réservé aux erreurs inattendues côté adaptateur
    (mtkclient introuvable, JSON corrompu, etc.).

    :param timeout_s: délai appliqué en amont, utilisé uniquement pour rédiger
        le message d'un dépassement (``None`` → message générique).
    """
    details: dict[str, Any] = {
        "returncode": sr.returncode,
        "duration_ms": sr.duration_ms,
        "stdout": _truncate(sr.stdout),
        "stderr": _truncate(sr.stderr),
    }
    if payload:
        details.update(payload)

    if sr.cancelled:
        status = OperationStatus.CANCELLED
        message = "Opération annulée"
    elif sr.timed_out:
        status = OperationStatus.FAILED
        message = f"Délai dépassé ({timeout_s}s)" if timeout_s is not None else "Délai dépassé"
    elif sr.returncode == 0:
        status = OperationStatus.SUCCESS
        message = success_message
    else:
        status = OperationStatus.FAILED
        message = f"Code retour {sr.returncode}"

    return OperationResult(
        operation=operation,
        status=status,
        message=message,
        duration_ms=sr.duration_ms,
        details=details,
    )