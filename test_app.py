import subprocess
import sys
from pathlib import Path

from app import main


PROJECT_ROOT = Path(__file__).parent


def test_main_prints_greeting(capsys):
    main()

    assert capsys.readouterr().out == "Hello, Jenkins!\n"


def test_running_app_script_prints_greeting():
    result = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "app.py")],
        capture_output=True,
        text=True,
        check=True,
    )

    assert result.stdout == "Hello, Jenkins!\n"