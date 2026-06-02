"""Lightweight output quality checks for the Streamlit research project.

Run from the repository root:
    python scripts/run_quality_check.py

The script is intentionally read-only except for writing one Markdown report
under output/. It does not import or modify the collector or app.
"""

from __future__ import annotations

import csv
from collections import Counter
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "output"
REPORT_PATH = OUTPUT_DIR / "run_quality_check_report.md"

CSV_FILES = {
    "articles": "articles.csv",
    "market_signals": "market_signals.csv",
    "development_lifecycle": "development_lifecycle.csv",
    "gp_intelligence": "gp_intelligence.csv",
    "asset_parcel_intelligence": "asset_parcel_intelligence.csv",
    "rent_demand_signals": "rent_demand_signals.csv",
}

RENT_DEMAND_TERMS = [
    "rent growth",
    "rent price",
    "rent prices",
    "asking rent",
    "effective rent",
    "absorption",
    "vacancy",
    "occupancy",
    "concession",
    "concessions",
    "leasing gains",
    "apartment supply pressure",
]

TRANSACTION_TERMS = [
    "sale",
    "sells",
    "sold",
    "disposition",
    "acquisition",
    "acquires",
    "acquired",
    "buys",
    "refinance",
    "refinancing",
    "loan",
    "financing",
    "debt",
    "recapitalization",
    "recap",
]

PROJECT_TERMS = [
    "project",
    "development",
    "community",
    "apartments",
    "apartment",
    "tower",
    "site",
    "parcel",
    "unit",
    "units",
    "construction",
    "breaks ground",
    "delivers",
    "opens",
    "redevelopment",
    "to build",
]

POLICY_APPROVAL_TERMS = [
    "policy",
    "mayor",
    "rand",
    "ula",
    "approval",
    "zoning",
    "entitlement",
    "planning commission",
    "ceqa",
    "hud review",
]

GP_PLATFORM_CORPORATE_TERMS = [
    "fund close",
    "capital raise",
    "launches platform",
    "platform launch",
    "lending platform",
    "debt platform",
    "corporate acquisition",
    "company-level acquisition",
    "merger",
    "acquires btr player",
    "acquires taylor morrison",
    "berkshire hathaway acquires",
    "portfolio-wide strategy",
    "institutional strategy",
    "capital strategy",
]


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    """Read a CSV file as dictionaries, returning [] if unavailable."""
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))
    except Exception as exc:
        return [{"__read_error__": str(exc), "__path__": str(path)}]


def clean(value: object) -> str:
    """Normalize blank-ish CSV values for checks and display."""
    if value is None:
        return ""
    text = str(value).strip()
    if text.lower() in {"nan", "none", "null"}:
        return ""
    return text


def lower_blob(row: dict[str, str]) -> str:
    fields = [
        "title",
        "summary",
        "article_text_sample",
        "market_signal",
        "section_routing_reason",
        "classification_reason",
        "primary_category_reason",
        "development_lifecycle_hint",
        "capital_event_type",
        "financing_type",
        "development_stage",
    ]
    return " ".join(clean(row.get(field)) for field in fields).lower()


def first_value(row: dict[str, str], fields: list[str], default: str = "") -> str:
    for field in fields:
        value = clean(row.get(field))
        if value:
            return value
    return default


def is_missing(row: dict[str, str], fields: list[str]) -> bool:
    return not first_value(row, fields)


def is_truthy(value: object) -> bool:
    return clean(value).lower() in {"true", "yes", "1", "y"}


def has_any(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def truncate(text: str, limit: int = 130) -> str:
    text = " ".join(clean(text).split())
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def markdown_escape(text: str) -> str:
    return clean(text).replace("|", "\\|").replace("\n", " ")


def suspect_row(
    row: dict[str, str],
    issue: str,
    severity: int,
    source_file: str,
) -> dict[str, str | int]:
    return {
        "issue": issue,
        "severity": severity,
        "source_file": source_file,
        "title": first_value(row, ["title", "source_article_title", "canonical_asset_or_project_name"], "Untitled"),
        "source": first_value(row, ["source", "source_report"], "Source not specified"),
        "market": first_value(row, ["market_focus", "market", "related_market", "state_or_region"], "Market not specified"),
        "primary_display_section": first_value(row, ["primary_display_section"], "Section not specified"),
        "stage": first_value(
            row,
            [
                "development_lifecycle_hint",
                "current_lifecycle_stage",
                "lifecycle_stage",
                "development_stage",
                "primary_development_category",
                "current_stage",
            ],
            "Stage not specified",
        ),
        "reason": first_value(
            row,
            [
                "section_routing_reason",
                "primary_category_reason",
                "classification_reason",
                "project_anchor_reason",
                "rent_demand_reason",
            ],
            "No reason provided",
        ),
    }


def collect_possible_regressions(data: dict[str, list[dict[str, str]]]) -> list[dict[str, str | int]]:
    suspects: list[dict[str, str | int]] = []
    articles = data.get("articles", [])

    for row in articles:
        section = clean(row.get("primary_display_section"))
        blob = lower_blob(row)
        has_project_anchor = is_truthy(row.get("has_project_anchor"))

        if section == "Development Activity" and has_any(blob, RENT_DEMAND_TERMS):
            suspects.append(suspect_row(row, "rent/demand signal inside Development Activity", 80, "articles.csv"))

        if section == "Development Activity" and has_any(blob, TRANSACTION_TERMS) and not has_project_anchor:
            suspects.append(suspect_row(row, "transaction/capital event in Development without project anchor", 95, "articles.csv"))

        if (
            section == "GP / Capital Activity"
            and (has_project_anchor or has_any(blob, PROJECT_TERMS))
            and not has_any(blob, GP_PLATFORM_CORPORATE_TERMS)
        ):
            suspects.append(suspect_row(row, "project/development article routed to GP/Capital", 90, "articles.csv"))

    for row in data.get("asset_parcel_intelligence", []):
        section = clean(row.get("primary_display_section"))
        category = clean(row.get("primary_development_category")).lower()
        blob = lower_blob(row)
        site_like = "site_parcel" in category or "site / parcel" in category or "parcel" in category
        if site_like and has_any(blob, POLICY_APPROVAL_TERMS) and not has_any(blob, ["acquired land", "purchased land", "site control", "parcel acquired", "development site acquired"]):
            suspects.append(suspect_row(row, "policy/approval article routed to Site / Parcel", 75, "asset_parcel_intelligence.csv"))
        elif section == "Development Activity" and site_like and has_any(blob, POLICY_APPROVAL_TERMS):
            suspects.append(suspect_row(row, "policy/approval article routed to Site / Parcel", 70, "asset_parcel_intelligence.csv"))

    suspects.sort(key=lambda item: (-int(item["severity"]), clean(item["title"]).lower()))
    return suspects


def count_gp_participant_not_identified(rows: list[dict[str, str]]) -> int:
    count = 0
    for row in rows:
        values = [
            row.get("lead_entity"),
            row.get("gp_name"),
            row.get("canonical_gp_name"),
            row.get("gp_or_developer"),
        ]
        if any(clean(value).lower() == "participant not identified" for value in values):
            count += 1
    return count


def count_gp_unknown_market(rows: list[dict[str, str]]) -> int:
    count = 0
    for row in rows:
        market = first_value(row, ["market_focus", "market", "related_market"])
        if market in {"Other / Unknown", "Unknown", "Market not specified"}:
            count += 1
    return count


def build_report(data: dict[str, list[dict[str, str]]], missing_files: list[str]) -> str:
    articles = data.get("articles", [])
    gp_rows = data.get("gp_intelligence", [])
    suspects = collect_possible_regressions(data)

    section_counts = Counter(first_value(row, ["primary_display_section"], "Section not specified") for row in articles)
    missing_source = sum(1 for row in articles if is_missing(row, ["source", "source_report"]))
    missing_market = sum(1 for row in articles if is_missing(row, ["market_focus", "market", "related_market", "primary_market"]))
    missing_published = sum(1 for row in articles if is_missing(row, ["published", "published_date_normalized"]))
    missing_stage = sum(1 for row in articles if is_missing(row, ["development_lifecycle_hint", "lifecycle_stage", "development_stage", "current_lifecycle_stage"]))
    participant_not_identified = count_gp_participant_not_identified(gp_rows)
    gp_unknown_market = count_gp_unknown_market(gp_rows)

    issue_counts = Counter(clean(item["issue"]) for item in suspects)

    lines: list[str] = [
        "# Run Quality Check Report",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Files Checked",
        "",
    ]
    for key, filename in CSV_FILES.items():
        status = f"{len(data.get(key, []))} row(s)" if filename not in missing_files else "missing"
        lines.append(f"- `{filename}`: {status}")

    lines.extend([
        "",
        "## Headline Counts",
        "",
        f"- Total articles: {len(articles)}",
        f"- Missing source: {missing_source}",
        f"- Missing market: {missing_market}",
        f"- Missing published date: {missing_published}",
        f"- Missing lifecycle/stage: {missing_stage}",
        f"- GP/Capital Participant not identified: {participant_not_identified}",
        f"- GP/Capital Other / Unknown market: {gp_unknown_market}",
        "",
        "## Articles By Primary Display Section",
        "",
    ])
    if section_counts:
        for section, count in sorted(section_counts.items()):
            lines.append(f"- {section}: {count}")
    else:
        lines.append("- No article rows found.")

    lines.extend([
        "",
        "## Possible Routing Regressions",
        "",
        f"- Total suspect rows: {len(suspects)}",
    ])
    if issue_counts:
        for issue, count in sorted(issue_counts.items()):
            lines.append(f"- {issue}: {count}")
    else:
        lines.append("- None detected by current heuristic checks.")

    lines.extend([
        "",
        "## Top 20 Suspect Rows",
        "",
        "| # | Issue | Title | Source | Market | Section | Stage | Reason |",
        "|---:|---|---|---|---|---|---|---|",
    ])
    for index, row in enumerate(suspects[:20], start=1):
        lines.append(
            "| "
            + " | ".join(
                [
                    str(index),
                    markdown_escape(str(row["issue"])),
                    markdown_escape(truncate(str(row["title"]))),
                    markdown_escape(str(row["source"])),
                    markdown_escape(str(row["market"])),
                    markdown_escape(str(row["primary_display_section"])),
                    markdown_escape(str(row["stage"])),
                    markdown_escape(truncate(str(row["reason"]), 180)),
                ]
            )
            + " |"
        )
    if not suspects:
        lines.append("| - | None | - | - | - | - | - | - |")

    lines.extend([
        "",
        "## Notes",
        "",
        "- This script is diagnostic only. It does not modify routing, classification, or app rendering logic.",
        "- Optional CSV files may be missing; missing files are reported but do not fail the run.",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data: dict[str, list[dict[str, str]]] = {}
    missing_files: list[str] = []

    for key, filename in CSV_FILES.items():
        path = OUTPUT_DIR / filename
        rows = read_csv_rows(path)
        data[key] = rows
        if not path.exists():
            missing_files.append(filename)

    report = build_report(data, missing_files)
    REPORT_PATH.write_text(report, encoding="utf-8")

    articles = data.get("articles", [])
    section_counts = Counter(first_value(row, ["primary_display_section"], "Section not specified") for row in articles)
    suspects = collect_possible_regressions(data)

    print(f"Saved quality report: {REPORT_PATH}")
    print(f"Total articles: {len(articles)}")
    for section, count in sorted(section_counts.items()):
        print(f"{section}: {count}")
    print(f"Possible routing regressions: {len(suspects)}")


if __name__ == "__main__":
    main()
