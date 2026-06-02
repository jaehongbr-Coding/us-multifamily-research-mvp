"""Capture key Streamlit pages for daily visual QA.

Run from the repository root after Streamlit is available:
    python scripts/capture_streamlit_pages.py

Windows PowerShell example:
    python -m streamlit run app.py --server.port 8501
    python scripts/capture_streamlit_pages.py

Playwright setup, if missing:
    python -m pip install playwright
    python -m playwright install chromium

This script only reads app output and writes files under output/daily_qa/.
It does not modify application routing or rendering logic.
"""

from __future__ import annotations

import argparse
import shutil
import time
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen


BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "output"
DAILY_QA_DIR = OUTPUT_DIR / "daily_qa"
QUALITY_REPORT = OUTPUT_DIR / "run_quality_check_report.md"
QA_PROMPT = DAILY_QA_DIR / "qa_prompt.md"
CAPTURE_MANIFEST = DAILY_QA_DIR / "capture_manifest.md"

APP_URL = "http://localhost:8501"

PAGES = [
    {
        "name": "오늘의 브리핑",
        "slug": "01_today_briefing",
        "radio_index": 0,
        "label_candidates": ["오늘의 브리핑", "Today", "Briefing"],
    },
    {
        "name": "시장 인텔리전스",
        "slug": "02_market_intelligence",
        "radio_index": 1,
        "label_candidates": ["시장 인텔리전스", "Market Intelligence"],
    },
    {
        "name": "최근 개발 Activity",
        "slug": "03_development_activity",
        "radio_index": 2,
        "label_candidates": ["최근 개발 Activity", "Development Activity"],
    },
    {
        "name": "GP / 자본 동향",
        "slug": "04_gp_capital",
        "radio_index": 3,
        "label_candidates": ["GP / 자본 동향", "GP / Capital"],
    },
    {
        "name": "Rent Comp Lab",
        "slug": "05_rent_comp_lab",
        "radio_index": None,
        "label_candidates": ["Rent Comp Lab", "Rent Comp"],
    },
    {
        "name": "기사 모음",
        "slug": "06_article_feed",
        "radio_index": 4,
        "label_candidates": ["기사 모음", "Article Feed"],
    },
    {
        "name": "Internal Lab",
        "slug": "07_internal_lab",
        "radio_index": 5,
        "label_candidates": ["Internal Lab", "Internal"],
    },
]


def ensure_daily_qa_dir() -> None:
    DAILY_QA_DIR.mkdir(parents=True, exist_ok=True)


def wait_for_streamlit(url: str, timeout_seconds: int = 60) -> bool:
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        try:
            with urlopen(url, timeout=5) as response:
                if 200 <= response.status < 500:
                    return True
        except Exception:
            time.sleep(1)
    return False


def copy_quality_report() -> Path | None:
    if not QUALITY_REPORT.exists():
        return None
    target = DAILY_QA_DIR / "run_quality_check_report.md"
    shutil.copy2(QUALITY_REPORT, target)
    return target


def summarize_quality_report(max_lines: int = 36) -> list[str]:
    report_path = DAILY_QA_DIR / "run_quality_check_report.md"
    if not report_path.exists():
        return ["- run_quality_check_report.md was not found."]
    lines = report_path.read_text(encoding="utf-8", errors="replace").splitlines()
    summary: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if (
            stripped.startswith("#")
            or stripped.startswith("- Total")
            or stripped.startswith("- Article")
            or stripped.startswith("- Market")
            or stripped.startswith("- Development")
            or stripped.startswith("- GP")
            or stripped.startswith("- Missing")
            or stripped.startswith("- Participant")
            or stripped.startswith("- Other")
            or "Possible routing regressions" in stripped
        ):
            summary.append(stripped)
        if len(summary) >= max_lines:
            break
    return summary or ["- No summary lines were extracted from run_quality_check_report.md."]


def locator_count(locator) -> int:
    try:
        return locator.count()
    except Exception:
        return 0


def expand_sidebar_if_needed(page) -> str:
    """Best-effort expansion for Streamlit sidebars that start collapsed."""
    selectors = [
        '[data-testid="collapsedControl"]',
        '[data-testid="stSidebarCollapsedControl"]',
        'button[aria-label*="Open sidebar"]',
        'button[aria-label*="open sidebar"]',
        'button[aria-label*="Expand sidebar"]',
        'button[title*="sidebar"]',
    ]
    for selector in selectors:
        control = page.locator(selector)
        if locator_count(control) > 0:
            try:
                control.first.click(timeout=3000)
                page.wait_for_timeout(1000)
                return f"expanded sidebar via {selector}"
            except Exception:
                continue
    sidebar = page.locator('[data-testid="stSidebar"]')
    if locator_count(sidebar) > 0:
        try:
            if sidebar.first.is_visible(timeout=1000):
                return "sidebar already visible"
        except Exception:
            pass
    return "sidebar expansion control not found"


def click_by_label(page, target: dict) -> tuple[bool, str]:
    sidebar = page.locator('[data-testid="stSidebar"]')
    for label in target["label_candidates"]:
        candidates = [
            sidebar.get_by_text(label, exact=True),
            sidebar.get_by_text(label, exact=False),
            page.get_by_role("radio", name=label, exact=False),
            page.get_by_text(label, exact=True),
            page.get_by_text(label, exact=False),
        ]
        for candidate in candidates:
            if locator_count(candidate) > 0:
                try:
                    candidate.first.click(timeout=6000, force=True)
                    return True, f"clicked label candidate: {label}"
                except Exception:
                    continue
    return False, "page label was not found in the sidebar"


def click_radio_by_index(page, target: dict) -> tuple[bool, str]:
    """Click the requested page radio by index, independent of label text."""
    index = target.get("radio_index")
    if index is None:
        return False, "no radio_index configured for this page"

    sidebar = page.locator('[data-testid="stSidebar"]')
    if locator_count(sidebar) == 0:
        return False, "sidebar locator not found"

    errors: list[str] = []
    radiogroups = sidebar.locator('[role="radiogroup"]')
    group_count = locator_count(radiogroups)
    for group_idx in range(group_count - 1, -1, -1):
        group = radiogroups.nth(group_idx)
        for selector in ['[role="radio"]', 'label', 'div[role="radio"]']:
            options = group.locator(selector)
            if locator_count(options) > index:
                try:
                    options.nth(index).click(timeout=6000, force=True)
                    return True, f"clicked radiogroup {group_idx} option index {index}"
                except Exception as exc:
                    errors.append(f"radiogroup {group_idx} {selector}: {exc}")

    for selector in [
        '[data-testid="stSidebar"] [role="radio"]',
        '[data-testid="stSidebar"] label',
    ]:
        options = page.locator(selector)
        if locator_count(options) > index:
            try:
                options.nth(index).click(timeout=6000, force=True)
                return True, f"clicked {selector} index {index}"
            except Exception as exc:
                errors.append(f"{selector}: {exc}")

    reason = "; ".join(errors[-3:]) if errors else f"no sidebar radio option found at index {index}"
    return False, reason


def click_page(page, target: dict) -> tuple[bool, str, str]:
    label_clicked, label_reason = click_by_label(page, target)
    if label_clicked:
        return True, "label", label_reason

    index_clicked, index_reason = click_radio_by_index(page, target)
    if index_clicked:
        return True, "radio_index", index_reason

    return False, "missing", f"{label_reason}; radio_index fallback failed: {index_reason}"


def capture_pages(url: str, timeout_seconds: int, viewport_width: int, viewport_height: int) -> list[dict]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise SystemExit(
            "Playwright is not installed.\n"
            "Install it with:\n"
            "  python -m pip install playwright\n"
            "  python -m playwright install chromium"
        ) from exc

    if not wait_for_streamlit(url, timeout_seconds):
        raise SystemExit(f"Streamlit did not respond at {url} within {timeout_seconds} seconds.")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results: list[dict] = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": viewport_width, "height": viewport_height})
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=timeout_seconds * 1000)
        page.wait_for_timeout(3000)
        sidebar_note = expand_sidebar_if_needed(page)

        for target in PAGES:
            clicked, click_method, note = click_page(page, target)
            if clicked:
                page.wait_for_timeout(3500)
                screenshot_path = DAILY_QA_DIR / f"{target['slug']}_{timestamp}.png"
                page.screenshot(path=str(screenshot_path), full_page=True)
                status = "captured"
                failure_reason = ""
            else:
                page.wait_for_timeout(1000)
                screenshot_path = DAILY_QA_DIR / f"missing_{target['slug']}_{timestamp}.png"
                page.screenshot(path=str(screenshot_path), full_page=True)
                status = "diagnostic"
                failure_reason = note
            results.append({
                "name": target["name"],
                "slug": target["slug"],
                "status": status,
                "path": str(screenshot_path),
                "click_method": click_method,
                "note": note,
                "failure_reason": failure_reason,
                "sidebar_note": sidebar_note,
            })

        context.close()
        browser.close()

    return results


def write_capture_manifest(capture_results: list[dict]) -> None:
    lines = [
        "# Streamlit Capture Manifest",
        "",
        f"- Generated at: {datetime.now().isoformat(timespec='seconds')}",
        f"- Output folder: {DAILY_QA_DIR}",
        "",
        "| Page | Status | Screenshot | Click method | Failure reason |",
        "| --- | --- | --- | --- | --- |",
    ]
    for result in capture_results:
        screenshot = Path(result["path"]).name if result.get("path") else ""
        lines.append(
            "| "
            f"{result.get('name', '')} | "
            f"{result.get('status', '')} | "
            f"{screenshot} | "
            f"{result.get('click_method', '')} | "
            f"{result.get('failure_reason', '') or result.get('note', '')} |"
        )
    CAPTURE_MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_qa_prompt(capture_results: list[dict]) -> None:
    quality_copy = copy_quality_report()
    report_summary = summarize_quality_report()
    write_capture_manifest(capture_results)
    lines = [
        "# Daily QA Review Prompt",
        "",
        f"- Generated at: {datetime.now().isoformat(timespec='seconds')}",
        f"- Streamlit URL: {APP_URL}",
        f"- Quality report copy: {quality_copy.name if quality_copy else 'missing'}",
        f"- Capture manifest: {CAPTURE_MANIFEST.name}",
        "",
        "## Screenshot Files",
    ]
    for result in capture_results:
        screenshot_name = Path(result["path"]).name if result.get("path") else "no screenshot"
        lines.append(
            f"- {result['name']}: {result['status']} | `{screenshot_name}` | "
            f"method={result.get('click_method', '')} | "
            f"reason={result.get('failure_reason', '')}"
        )

    lines.extend([
        "",
        "## run_quality_check_report.md Summary",
        *report_summary,
        "",
        "## Human Review Checklist",
        "1. Article Feed section routing errors",
        "2. Transaction or market articles mixed into Development Activity",
        "3. Project development articles routed too heavily into GP/Capital",
        "4. Source/Market/Stage missing values",
        "5. Repeated copy or low-value briefing text",
        "6. Missing Site/Parcel candidates",
        "",
        "아래 캡쳐와 리포트를 보고 수정 제안만 작성하고, 코드 수정은 승인 전까지 하지 말 것",
    ])
    QA_PROMPT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Capture Streamlit pages for daily QA.")
    parser.add_argument("--url", default=APP_URL, help="Streamlit URL to capture.")
    parser.add_argument("--timeout", type=int, default=90, help="Seconds to wait for Streamlit.")
    parser.add_argument("--viewport-width", type=int, default=1440)
    parser.add_argument("--viewport-height", type=int, default=1200)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ensure_daily_qa_dir()
    results = capture_pages(args.url, args.timeout, args.viewport_width, args.viewport_height)
    write_qa_prompt(results)
    captured = sum(1 for result in results if result["status"] == "captured")
    diagnostic = sum(1 for result in results if result["status"] == "diagnostic")
    missing = len(results) - captured - diagnostic
    print(f"Saved daily QA files under: {DAILY_QA_DIR}")
    print(f"Captured pages: {captured}")
    print(f"Diagnostic screenshots: {diagnostic}")
    print(f"Missing pages without screenshot: {missing}")
    print(f"Capture manifest: {CAPTURE_MANIFEST}")
    print(f"QA prompt: {QA_PROMPT}")
    return 0 if captured or diagnostic else 1


if __name__ == "__main__":
    raise SystemExit(main())
