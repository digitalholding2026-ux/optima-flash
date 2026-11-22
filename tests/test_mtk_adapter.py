from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import pytest

from src.adapters.mtk.adapter import MediaTekAdapter
from src.core.config import AppConfig
from src.core.runner import SubprocessResult
from src.core.types import (
    ChipsetType,
    ConnectionMode,
    DeviceInfo,
    OperationFailure,
)

GPT_STDOUT = """
GPT Table:
-------------
preloader:          Offset 0x0000000000000000, Length 0x0000000000040000, Flags 0x0
boot:               Offset 0x0000000000040000, Length 0x0000000001000000, Flags 0x0
"""
TARGET_STDOUT = """
mtkclient.Library.mtk_preloader - 	CPU:			mt6765(Helio P35)
mtkclient.Library.mtk_preloader - HW code:			0x1234
mtkclient.Library.mtk_preloader - 	HW Ver:			0x0
mtkclient.Library.mtk_preloader - 	SW Ver:			0x1
"""


def _config() -> AppConfig:
    return AppConfig(
        mtkclient_path=Path("bin/mtkclient"),
        edl_path=Path("bin/edl"),
        logs_dir=Path("logs"),
        raw_dir=Path("logs/raw"),
        db_path=Path("data/optima.db"),
        theme="dark",
        mtkclient_cmd=(".venv-mtk/Scripts/mtk.exe",),
    )


def _device() -> DeviceInfo:
    return DeviceInfo(
        chipset=ChipsetType.MTK,
        connection_mode=ConnectionMode.PRELOADER,
        vid=0x0E8D,
        pid=0x2000,
        bus=1,
        address=2,
    )


def _result(
    returncode: int | None,
    stdout: str = "",
    stderr: str = "",
    *,
    timed_out: bool = False,
) -> SubprocessResult:
    return SubprocessResult(
        cmd=("mtk",),
        returncode=None if timed_out else returncode,
        stdout=stdout,
        stderr=stderr,
        duration_ms=12,
        timed_out=timed_out,
        cancelled=False,
    )


def _install_runner(
    monkeypatch: pytest.MonkeyPatch,
    *,
    gpt: SubprocessResult,
    target: SubprocessResult,
) -> list[list[str]]:
    calls: list[list[str]] = []

    def fake(
        cmd: list[str],
        *,
        timeout_s: float | None = None,
        cwd: Path | None = None,
        cancel_event: Any = None,
        env: dict[str, str] | None = None,
        logger: logging.Logger | None = None,
    ) -> SubprocessResult:
        calls.append(list(cmd))
        return gpt if "printgpt" in cmd else target

    monkeypatch.setattr("src.adapters.mtk.adapter.run_subprocess", fake)
    return calls


def test_detect_keeps_only_mtk_devices(monkeypatch: pytest.MonkeyPatch) -> None:
    mtk = _device()
    qualcomm = DeviceInfo(
        chipset=ChipsetType.QUALCOMM,
        connection_mode=ConnectionMode.EDL_9008,
        vid=0x05C6,
        pid=0x9008,
        bus=1,
        address=3,
    )
    monkeypatch.setattr(
        "src.adapters.mtk.adapter.detect_devices", lambda: [mtk, qualcomm]
    )

    adapter = MediaTekAdapter(_config(), logging.getLogger("test"))

    assert adapter.detect() == [mtk]


def test_read_info_parses_partitions(monkeypatch: pytest.MonkeyPatch) -> None:
    _install_runner(
        monkeypatch,
        gpt=_result(0, GPT_STDOUT),
        target=_result(0, TARGET_STDOUT),
    )

    info = MediaTekAdapter(_config(), logging.getLogger("test")).read_info(_device())

    assert info["partitions"] == ["preloader", "boot"]


def test_read_info_parses_target_config(monkeypatch: pytest.MonkeyPatch) -> None:
    _install_runner(
        monkeypatch,
        gpt=_result(0, GPT_STDOUT),
        target=_result(0, TARGET_STDOUT),
    )

    info = MediaTekAdapter(_config(), logging.getLogger("test")).read_info(_device())

    assert info["hw_code"] == "0x1234"
    assert info["hw_ver"] == "0x0"
    assert info["sw_ver"] == "0x1"
    assert info["cpu"] == "mt6765"


def test_read_info_nonzero_returncode_is_not_an_exception(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _install_runner(
        monkeypatch,
        gpt=_result(1, stderr="Error: no device"),
        target=_result(1, stderr="Error: no device"),
    )

    info = MediaTekAdapter(_config(), logging.getLogger("test")).read_info(_device())

    assert info["hw_code"] is None
    assert info["sw_ver"] is None
    assert info["partitions"] == []
    assert "no device" in info["raw_stderr"]


def test_read_info_missing_binary_raises_operation_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake(cmd: list[str], **kwargs: Any) -> SubprocessResult:
        raise FileNotFoundError("mtk.exe introuvable")

    monkeypatch.setattr("src.adapters.mtk.adapter.run_subprocess", fake)

    adapter = MediaTekAdapter(_config(), logging.getLogger("test"))

    with pytest.raises(OperationFailure):
        adapter.read_info(_device())


def _probe_mtk_device() -> bool:
    try:
        return bool(MediaTekAdapter(_config(), logging.getLogger("probe")).detect())
    except (OperationFailure, OSError):
        return False


HAS_DEVICE = _probe_mtk_device()


@pytest.mark.skipif(not HAS_DEVICE, reason="Aucun appareil MediaTek branché")
def test_hardware_read_info_returns_hw_code() -> None:
    adapter = MediaTekAdapter(_config(), logging.getLogger("test"))
    device = adapter.detect()[0]

    info = adapter.read_info(device)

    assert info["hw_code"] is not None