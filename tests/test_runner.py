from __future__ import annotations

import os
import sys
import threading

import pytest

from src.core.runner import run_subprocess, to_operation_result
from src.core.types import OperationStatus


def _python(*args: str) -> list[str]:
    return [sys.executable, *args]


def test_success_returns_zero_and_stdout() -> None:
    sr = run_subprocess(_python("-c", "print('hello')"))

    assert sr.returncode == 0
    assert "hello" in sr.stdout
    assert sr.timed_out is False
    assert sr.cancelled is False


def test_nonzero_returncode_does_not_raise() -> None:
    sr = run_subprocess(_python("-c", "import sys; sys.exit(3)"))

    assert sr.returncode == 3
    assert sr.timed_out is False
    assert sr.cancelled is False


def test_timeout_kills_process() -> None:
    sr = run_subprocess(_python("-c", "import time; time.sleep(5)"), timeout_s=0.5)

    assert sr.timed_out is True
    assert sr.returncode is None
    assert sr.duration_ms < 2000


def test_cancel_event_kills_process() -> None:
    event = threading.Event()
    threading.Timer(0.2, event.set).start()

    sr = run_subprocess(_python("-c", "import time; time.sleep(5)"), cancel_event=event)

    assert sr.cancelled is True
    assert sr.timed_out is False
    assert sr.returncode is None
    assert sr.duration_ms < 2000


def test_text_decoding_is_utf8() -> None:
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"

    sr = run_subprocess(_python("-c", "print('éàü')"), env=env)

    assert "éàü" in sr.stdout


def test_missing_binary_raises_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        run_subprocess(["binaire-inexistant-xyz"])


def test_to_operation_result_success() -> None:
    sr = run_subprocess(_python("-c", "print('hello')"))

    result = to_operation_result(sr, success_message="Terminé")

    assert result.status is OperationStatus.SUCCESS
    assert result.message == "Terminé"
    assert result.details["returncode"] == 0


def test_to_operation_result_timeout() -> None:
    sr = run_subprocess(_python("-c", "import time; time.sleep(5)"), timeout_s=0.5)

    result = to_operation_result(sr, timeout_s=0.5)

    assert result.status is OperationStatus.FAILED
    assert "Délai dépassé" in result.message
    assert "0.5" in result.message