"""Tests for pomodoro.py: negative durations and zero cycles must be rejected."""

import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pomodoro  # noqa: E402


def run_main(monkeypatch, *args):
    monkeypatch.setattr(sys, "argv", ["pomodoro.py", *args])
    # Never run the real timer in tests; validation happens before it.
    monkeypatch.setattr(pomodoro, "countdown", lambda *a, **k: None)
    return pomodoro.main()


def test_negative_work_rejected(monkeypatch, capsys):
    with pytest.raises(SystemExit) as exc:
        run_main(monkeypatch, "--work", "-5")
    assert exc.value.code == 2
    assert "Traceback" not in capsys.readouterr().err


def test_zero_cycles_rejected(monkeypatch, capsys):
    with pytest.raises(SystemExit) as exc:
        run_main(monkeypatch, "--cycles", "0")
    assert exc.value.code == 2
    assert "Traceback" not in capsys.readouterr().err


def test_short_test_run_still_works():
    script = os.path.join(os.path.dirname(__file__), "..", "pomodoro.py")
    proc = subprocess.run(
        [sys.executable, script, "--test", "--cycles", "1"],
        capture_output=True,
        text=True,
        cwd=os.path.join(os.path.dirname(__file__), ".."),
    )
    assert proc.returncode == 0
    assert "pomodoro" in (proc.stdout + proc.stderr).lower()
