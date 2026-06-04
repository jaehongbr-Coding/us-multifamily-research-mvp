"""
Streamlit dashboard for the US Residential Intelligence App.

The app only reads existing files from output/. It does not run the collector,
call APIs, or write generated files.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"

FILES = {
    "articles": OUTPUT_DIR / "articles.csv",
    "dashboard_summary": OUTPUT_DIR / "dashboard_summary.csv",
    "dashboard_cards": OUTPUT_DIR / "dashboard_cards.csv",
    "dashboard_watchlists": OUTPUT_DIR / "dashboard_watchlists.csv",
    "market_diagnostics": OUTPUT_DIR / "market_intelligence_diagnostics.csv",
    "development_lifecycle": OUTPUT_DIR / "development_lifecycle.csv",
    "gp_watchlist": OUTPUT_DIR / "gp_watchlist.csv",
    "institutional_relationships": OUTPUT_DIR / "institutional_relationships.csv",
    "executive_brief_ko": OUTPUT_DIR / "executive_dashboard_brief_ko.md",
    "run_summary": OUTPUT_DIR / "run_summary.md",
}

PAGE_NAMES = [
    "오늘의 브리핑",
    "시장 인텔리전스",
    "개발현황",
    "GP Action",
    "기사 모음",
]


@st.cache_data(show_spinner=False)
def read_csv_safely(path_string: str) -> pd.DataFrame:
    """Read a CSV file; return an empty table when it is missing or invalid."""
    path = Path(path_string)
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception as error:
        st.warning(f"`{path.name}` 파일을 읽지 못했습니다: {error}")
        return pd.DataFrame()


@st.cache_data(show_spinner=False)
def read_markdown_safely(path_string: str) -> str:
    """Read a Markdown file; return blank text when it is missing or invalid."""
    path = Path(path_string)
    if not path.exists():
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except Exception as error:
        return f"`{path.name}` 파일을 읽지 못했습니다: {error}"


def load_data() -> dict[str, pd.DataFrame | str]:
    """Load every app-facing output file in one predictable place."""
    return {
        "articles": read_csv_safely(str(FILES["articles"])),
        "summary": read_csv_safely(str(FILES["dashboard_summary"])),
        "cards": read_csv_safely(str(FILES["dashboard_cards"])),
        "watchlists": read_csv_safely(str(FILES["dashboard_watchlists"])),
        "market_diagnostics": read_csv_safely(str(FILES["market_diagnostics"])),
        "development": read_csv_safely(str(FILES["development_lifecycle"])),
        "gp_watchlist": read_csv_safely(str(FILES["gp_watchlist"])),
        "relationships": read_csv_safely(str(FILES["institutional_relationships"])),
        "executive_brief_ko": read_markdown_safely(str(FILES["executive_brief_ko"])),
        "run_summary": read_markdown_safely(str(FILES["run_summary"])),
    }


def get_table(data: dict[str, pd.DataFrame | str], key: str) -> pd.DataFrame:
    value = data.get(key)
    if isinstance(value, pd.DataFrame):
        return value
    return pd.DataFrame()


def get_text(data: dict[str, pd.DataFrame | str], key: str) -> str:
    value = data.get(key)
    return value if isinstance(value, str) else ""


def clean(value: object, default: str = "") -> str:
    if value is None:
        return default
    text = str(value).strip()
    if not text or text.lower() in {"nan", "none", "null"}:
        return default
    return text


def first_value(row: pd.Series | dict, fields: Iterable[str], default: str = "") -> str:
    for field in fields:
        if field in row:
            value = clean(row.get(field))
            if value:
                return value
    return default


def numeric(value: object, default: float = 0) -> float:
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def truncate(value: object, limit: int = 120) -> str:
    text = clean(value)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def latest_summary(summary: pd.DataFrame) -> dict:
    if summary.empty:
        return {}
    return summary.iloc[-1].fillna("").to_dict()


def sorted_by_score(df: pd.DataFrame, score_fields: Iterable[str]) -> pd.DataFrame:
    if df.empty:
        return df
    table = df.copy()
    for field in score_fields:
        if field in table.columns:
            table["_sort_score"] = pd.to_numeric(table[field], errors="coerce").fillna(0)
            return table.sort_values("_sort_score", ascending=False).drop(columns=["_sort_score"])
    return table


def rows_for_card_type(cards: pd.DataFrame, card_type_terms: Iterable[str], limit: int = 5) -> pd.DataFrame:
    if cards.empty or "card_type" not in cards.columns:
        return pd.DataFrame()
    terms = [term.lower() for term in card_type_terms]
    mask = cards["card_type"].fillna("").astype(str).str.lower().apply(
        lambda value: any(term in value for term in terms)
    )
    return sorted_by_score(cards[mask], ["card_score", "score"]).head(limit)


def inject_css() -> None:
    st.markdown(
        """
        <style>
        .block-container { max-width: 1120px; padding-top: 1rem; padding-bottom: 2rem; }
        h1 { font-size: 1.75rem !important; letter-spacing: 0; }
        h2, h3 { letter-spacing: 0; }
        .brief-card {
            border: 1px solid #dbe2ea;
            border-radius: 7px;
            padding: 0.85rem 0.95rem;
            margin: 0.55rem 0 0.7rem 0;
            background: #ffffff;
        }
        .brief-hero {
            border-left: 6px solid #172033;
            background: #fbfcfe;
            padding: 1rem 1.1rem;
            margin: 0.45rem 0 1rem 0;
            border-radius: 7px;
            border-top: 1px solid #dbe2ea;
            border-right: 1px solid #dbe2ea;
            border-bottom: 1px solid #dbe2ea;
        }
        .kicker {
            color: #64748b;
            font-size: 0.74rem;
            font-weight: 800;
            text-transform: uppercase;
            margin-bottom: 0.25rem;
        }
        .card-title {
            color: #111827;
            font-size: 1rem;
            line-height: 1.35;
            font-weight: 750;
            margin-bottom: 0.25rem;
        }
        .muted {
            color: #64748b;
            font-size: 0.86rem;
            line-height: 1.45;
        }
        .badge {
            display: inline-block;
            border: 1px solid #cbd5e1;
            border-radius: 999px;
            padding: 0.12rem 0.45rem;
            margin: 0.1rem 0.15rem 0.1rem 0;
            background: #f8fafc;
            color: #334155;
            font-size: 0.74rem;
            font-weight: 700;
        }
        @media (max-width: 760px) {
            .block-container { padding-left: 0.72rem; padding-right: 0.72rem; }
            h1 { font-size: 1.35rem !important; }
            .brief-card, .brief-hero { padding: 0.75rem 0.8rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_badges(items: Iterable[str]) -> None:
    badges = [clean(item) for item in items if clean(item)]
    if not badges:
        return
    html = " ".join(f'<span class="badge">{item}</span>' for item in badges[:5])
    st.markdown(html, unsafe_allow_html=True)


def render_section_header(title: str, body: str | None = None) -> None:
    st.markdown("---")
    st.subheader(title)
    if body:
        st.caption(body)


def render_empty_state(message: str) -> None:
    st.info(message)


def render_metric_row(summary: dict) -> None:
    columns = st.columns(4)
    metrics = [
        ("전체 기사", summary.get("total_articles", "0")),
        ("고신뢰 신호", summary.get("high_confidence_signals", "0")),
        ("기회 신호", summary.get("opportunity_count", "0")),
        ("GP Watch", summary.get("gp_watchlist_count", "0")),
    ]
    for column, (label, value) in zip(columns, metrics):
        column.metric(label, clean(value, "0"))


def render_output_warning() -> None:
    if OUTPUT_DIR.exists():
        return
    st.warning(
        "`output/` 폴더가 없습니다. 먼저 `python news_collector.py`를 실행하거나 "
        "GitHub Actions가 생성한 output 파일을 준비해야 합니다."
    )


def render_header(summary: dict) -> None:
    st.title("US Residential Intelligence")
    st.caption("우미글로벌 미국 주거시장 전략 브리핑")
    latest_run = clean(summary.get("run_timestamp"), "실행 기록 없음")
    focus = clean(summary.get("recommended_executive_focus"))
    st.markdown(
        f"""
        <div class="brief-hero">
            <div class="kicker">Today&apos;s Highlight</div>
            <div class="card-title">{focus or "오늘 확인할 핵심 시장 신호를 요약합니다."}</div>
            <div class="muted">최근 실행: {latest_run}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_card(row: pd.Series | dict, title_fields: Iterable[str], body_fields: Iterable[str]) -> None:
    title = first_value(row, title_fields, "제목 없음")
    body = first_value(row, body_fields)
    score = first_value(row, ["card_score", "score", "relevance_score", "gp_activity_score"])
    url = first_value(row, ["source_url_if_available", "url"])
    badges = [
        first_value(row, ["market", "dominant_market", "primary_market"]),
        first_value(row, ["residential_sector", "residential_sector_focus"]),
        first_value(row, ["gp_or_developer", "canonical_gp_name", "gp_name", "firm_name"]),
        first_value(row, ["priority_label", "card_priority", "priority"]),
    ]

    st.markdown('<div class="brief-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="card-title">{truncate(title, 140)}</div>', unsafe_allow_html=True)
    if body:
        st.markdown(f'<div class="muted">{truncate(body, 280)}</div>', unsafe_allow_html=True)
    render_badges([*badges, f"Score {score}" if score else ""])
    if url:
        st.link_button("원문 열기", url)
    st.markdown("</div>", unsafe_allow_html=True)


def render_today_highlight(data: dict[str, pd.DataFrame | str], summary: dict) -> None:
    render_section_header(
        "오늘의 Highlight",
        "오늘 아침 가장 먼저 읽어야 할 시장 구도와 실행 포인트입니다.",
    )
    render_metric_row(summary)
    highlights = rows_for_card_type(get_table(data, "cards"), ["priority", "executive", "highlight"], limit=3)
    if highlights.empty:
        focus = clean(summary.get("recommended_executive_focus"))
        if focus:
            st.markdown(f"- {focus}")
        else:
            render_empty_state("대시보드 요약 파일에 오늘의 Highlight 데이터가 없습니다.")
        return
    for _, row in highlights.iterrows():
        render_card(
            row,
            ["card_title", "item_name", "title"],
            ["summary", "why_it_matters", "recommended_action"],
        )


def render_top_articles(data: dict[str, pd.DataFrame | str]) -> None:
    render_section_header(
        "오늘의 Top 기사",
        "관련성과 활용도가 높은 기사입니다. 제목만 보지 말고 포함 이유와 실행 포인트를 같이 확인합니다.",
    )
    articles = sorted_by_score(get_table(data, "articles"), ["relevance_score"]).head(5)
    if articles.empty:
        render_empty_state("articles.csv가 없거나 비어 있습니다.")
        return
    for _, row in articles.iterrows():
        render_card(
            row,
            ["title"],
            ["reason_for_inclusion", "strategic_implication", "article_text_sample", "summary"],
        )


def render_hot_market(data: dict[str, pd.DataFrame | str], summary: dict) -> None:
    render_section_header(
        "오늘의 Hot Market",
        "기사 수만이 아니라 반복 신호, source breadth, capital/development activity를 함께 봅니다.",
    )
    top_market = clean(summary.get("top_market"))
    diagnostics = sorted_by_score(
        get_table(data, "market_diagnostics"),
        ["supporting_article_count", "source_diversity_score"],
    ).head(5)
    if top_market:
        st.markdown(f"**오늘 우선 확인 시장:** {top_market}")
    if diagnostics.empty:
        render_empty_state("market_intelligence_diagnostics.csv가 없거나 비어 있습니다.")
        return
    for _, row in diagnostics.iterrows():
        render_card(
            row,
            ["generated_signal_cluster", "dominant_market"],
            ["regime_synthesis_text", "confidence_explanation", "woomi_watchpoint_driver"],
        )


def render_development_status(data: dict[str, pd.DataFrame | str]) -> None:
    render_section_header(
        "개발현황",
        "신규 개발, 인허가, 착공, lifecycle 변화와 실행 리스크를 봅니다.",
    )
    development = sorted_by_score(
        get_table(data, "development"),
        ["lifecycle_opportunity_score", "lifecycle_risk_score"],
    ).head(6)
    if development.empty:
        render_empty_state("development_lifecycle.csv가 없거나 비어 있습니다.")
        return
    for _, row in development.iterrows():
        render_card(
            row,
            ["canonical_asset_or_project_name", "canonical_project_name", "source_article_title"],
            ["primary_category_reason", "evidence_signals", "recommended_lifecycle_follow_up"],
        )


def render_gp_action(data: dict[str, pd.DataFrame | str]) -> None:
    render_section_header(
        "오늘의 GP Action",
        "Developer, GP, institutional capital의 움직임과 우미 관점의 후속 검토 포인트입니다.",
    )
    gp_rows = sorted_by_score(get_table(data, "gp_watchlist"), ["emerging_gp_score", "gp_activity_score"]).head(5)
    relationship_rows = sorted_by_score(
        get_table(data, "relationships"),
        ["institutional_relationship_score", "highest_relevance_score"],
    ).head(3)
    if gp_rows.empty and relationship_rows.empty:
        render_empty_state("gp_watchlist.csv 또는 institutional_relationships.csv 데이터가 없습니다.")
        return
    for _, row in gp_rows.iterrows():
        render_card(
            row,
            ["canonical_gp_name", "gp_name"],
            ["potential_woomi_use_case", "recommended_follow_up", "likely_growth_direction"],
        )
    if not relationship_rows.empty:
        with st.expander("기관 / 자본 관계 신호 더 보기", expanded=False):
            for _, row in relationship_rows.iterrows():
                render_card(
                    row,
                    ["firm_name"],
                    ["capital_flow_signal", "relationship_signal", "recommended_follow_up"],
                )


def render_article_feed(data: dict[str, pd.DataFrame | str], limit: int = 20) -> None:
    render_section_header(
        "기사 모음",
        "전체 기사 목록입니다. 상세 검토가 필요할 때 원문과 분류 정보를 확인합니다.",
    )
    articles = sorted_by_score(get_table(data, "articles"), ["relevance_score"]).head(limit)
    if articles.empty:
        render_empty_state("articles.csv가 없거나 비어 있습니다.")
        return
    visible_columns = [
        column
        for column in [
            "relevance_score",
            "priority",
            "source",
            "published",
            "market_focus",
            "residential_sector",
            "title",
            "url",
        ]
        if column in articles.columns
    ]
    st.dataframe(articles[visible_columns], use_container_width=True, hide_index=True)


def render_today_briefing(data: dict[str, pd.DataFrame | str]) -> None:
    summary = latest_summary(get_table(data, "summary"))
    render_header(summary)
    render_today_highlight(data, summary)
    render_top_articles(data)
    render_hot_market(data, summary)
    render_development_status(data)
    render_gp_action(data)
    render_article_feed(data, limit=10)


def render_market_page(data: dict[str, pd.DataFrame | str]) -> None:
    st.title("시장 인텔리전스")
    summary = latest_summary(get_table(data, "summary"))
    render_hot_market(data, summary)
    brief = get_text(data, "executive_brief_ko")
    if brief:
        with st.expander("한국어 브리핑 원문", expanded=False):
            st.markdown(brief)


def render_development_page(data: dict[str, pd.DataFrame | str]) -> None:
    st.title("개발현황")
    render_development_status(data)


def render_gp_page(data: dict[str, pd.DataFrame | str]) -> None:
    st.title("GP Action")
    render_gp_action(data)


def render_articles_page(data: dict[str, pd.DataFrame | str]) -> None:
    st.title("기사 모음")
    render_article_feed(data, limit=50)


def render_sidebar(summary: dict) -> str:
    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("우미글로벌 미국 주거시장 전략 브리핑")
    st.sidebar.info("데이터 갱신은 `python news_collector.py` 또는 GitHub Actions에서 수행합니다.")
    page_name = st.sidebar.radio("페이지", PAGE_NAMES, index=0)
    latest_run = clean(summary.get("run_timestamp"), "실행 기록 없음")
    st.sidebar.markdown("---")
    st.sidebar.caption(f"최근 실행: {latest_run}")
    return page_name


def main() -> None:
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏘️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()
    render_output_warning()
    data = load_data()
    summary = latest_summary(get_table(data, "summary"))
    page_name = render_sidebar(summary)

    if page_name == "오늘의 브리핑":
        render_today_briefing(data)
    elif page_name == "시장 인텔리전스":
        render_market_page(data)
    elif page_name == "개발현황":
        render_development_page(data)
    elif page_name == "GP Action":
        render_gp_page(data)
    elif page_name == "기사 모음":
        render_articles_page(data)

    st.markdown("---")
    st.caption("US Residential Intelligence | Pilot dashboard")


if __name__ == "__main__":
    main()
