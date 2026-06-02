"""Run the daily QA package workflow for the Streamlit app.

Run from the repository root:
    python scripts/run_daily_qa.py

Windows PowerShell:
    python scripts\run_daily_qa.py

The workflow is intentionally non-mutating for application logic:
1. Run news_collector.py.
2. Run scripts/run_quality_check.py.
3. Start Streamlit on localhost:8501 when it is not already running.
4. Run scripts/capture_streamlit_pages.py.
5. Write/copy QA artifacts under output/daily_qa/.

Playwright setup, if missing:
    python -m pip install playwright
    python -m playwright install chromium
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen


BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "output"
DAILY_QA_DIR = OUTPUT_DIR / "daily_qa"
APP_URL = "http://localhost:8501"


def ensure_daily_qa_dir() -> None:
    DAILY_QA_DIR.mkdir(parents=True, exist_ok=True)


def append_log(message: str) -> None:
    ensure_daily_qa_dir()
    log_path = DAILY_QA_DIR / "daily_qa_run.log"
    timestamp = datetime.now().isoformat(timespec="seconds")
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"[{timestamp}] {message}\n")


def run_step(name: str, command: list[str], timeout: int | None = None) -> None:
    print(f"[Daily QA] {name}")
    append_log(f"START {name}: {' '.join(command)}")
    completed = subprocess.run(
        command,
        cwd=BASE_DIR,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )
    append_log(f"END {name}: exit_code={completed.returncode}")
    if completed.returncode != 0:
        raise SystemExit(f"{name} failed with exit code {completed.returncode}")


def is_streamlit_ready(url: str = APP_URL) -> bool:
    try:
        with urlopen(url, timeout=5) as response:
            return 200 <= response.status < 500
    except Exception:
        return False


def wait_for_streamlit(url: str = APP_URL, timeout_seconds: int = 90) -> bool:
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        if is_streamlit_ready(url):
            return True
        time.sleep(1)
    return False


def start_streamlit_if_needed(port: int, timeout_seconds: int) -> subprocess.Popen | None:
    url = f"http://localhost:{port}"
    if is_streamlit_ready(url):
        print(f"[Daily QA] Reusing existing Streamlit server at {url}")
        append_log(f"REUSE Streamlit server at {url}")
        return None

    ensure_daily_qa_dir()
    log_path = DAILY_QA_DIR / "streamlit.log"
    log_handle = log_path.open("a", encoding="utf-8", errors="replace")
    command = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "app.py",
        "--server.port",
        str(port),
        "--server.headless",
        "true",
    ]
    print(f"[Daily QA] Starting Streamlit at {url}")
    append_log(f"START Streamlit: {' '.join(command)}")
    process = subprocess.Popen(
        command,
        cwd=BASE_DIR,
        stdout=log_handle,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    process._daily_qa_log_handle = log_handle  # type: ignore[attr-defined]
    if not wait_for_streamlit(url, timeout_seconds):
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
        log_handle.close()
        raise SystemExit(f"Streamlit did not become ready at {url}")
    return process


def stop_streamlit(process: subprocess.Popen | None) -> None:
    if process is None:
        return
    print("[Daily QA] Stopping Streamlit process started by this run")
    append_log("STOP Streamlit process")
    process.terminate()
    try:
        process.wait(timeout=15)
    except subprocess.TimeoutExpired:
        process.kill()
    log_handle = getattr(process, "_daily_qa_log_handle", None)
    if log_handle:
        log_handle.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run collector, quality check, Streamlit, and screenshots.")
    parser.add_argument("--port", type=int, default=8501, help="Streamlit port.")
    parser.add_argument("--skip-collector", action="store_true", help="Skip news_collector.py.")
    parser.add_argument("--skip-quality-check", action="store_true", help="Skip scripts/run_quality_check.py.")
    parser.add_argument("--keep-server", action="store_true", help="Leave Streamlit running after capture.")
    parser.add_argument("--streamlit-timeout", type=int, default=90)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ensure_daily_qa_dir()
    append_log("Daily QA run started")

    if not args.skip_collector:
        run_step("Run news_collector.py", [sys.executable, "news_collector.py"], timeout=600)
    if not args.skip_quality_check:
        run_step("Run quality check", [sys.executable, "scripts/run_quality_check.py"], timeout=180)

    streamlit_process = None
    try:
        streamlit_process = start_streamlit_if_needed(args.port, args.streamlit_timeout)
        run_step(
            "Capture Streamlit pages",
            [
                sys.executable,
                "scripts/capture_streamlit_pages.py",
                "--url",
                f"http://localhost:{args.port}",
                "--timeout",
                str(args.streamlit_timeout),
            ],
            timeout=240,
        )
    finally:
        if not args.keep_server:
            stop_streamlit(streamlit_process)

    append_log("Daily QA run completed")
    print(f"[Daily QA] QA package saved under: {DAILY_QA_DIR}")
    print(f"[Daily QA] Prompt: {DAILY_QA_DIR / 'qa_prompt.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
