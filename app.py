"""
Interactive Streamlit intelligence workstation.

This app reads existing files from output/ only. It does not call paid APIs,
does not need a database, and does not modify the collector pipeline.
"""

from datetime import datetime
from difflib import SequenceMatcher
import html
from pathlib import Path
import re

import pandas as pd
import streamlit as st


# ---------------------------------------------------------
# Paths and settings
# ---------------------------------------------------------

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"

FILES = {
    "articles": OUTPUT_DIR / "articles.csv",
    "korean_brief": OUTPUT_DIR / "executive_dashboard_brief_ko.md",
    "dashboard_summary": OUTPUT_DIR / "dashboard_summary.csv",
    "dashboard_cards": OUTPUT_DIR / "dashboard_cards.csv",
    "dashboard_watchlists": OUTPUT_DIR / "dashboard_watchlists.csv",
    "high_confidence": OUTPUT_DIR / "high_confidence_watchlist.csv",
    "opportunities": OUTPUT_DIR / "opportunity_radar.csv",
    "distress": OUTPUT_DIR / "distress_watchlist.csv",
    "la_assets": OUTPUT_DIR / "la_asset_watch.csv",
    "la_entitlement": OUTPUT_DIR / "la_entitlement_watch.csv",
    "la_lifecycle": OUTPUT_DIR / "la_development_lifecycle_watch.csv",
    "development_lifecycle": OUTPUT_DIR / "development_lifecycle.csv",
    "entitlement_intelligence": OUTPUT_DIR / "entitlement_intelligence.csv",
    "asset_parcel_intelligence": OUTPUT_DIR / "asset_parcel_intelligence.csv",
    "timing_intelligence": OUTPUT_DIR / "timing_intelligence.csv",
    "la_persistent_assets": OUTPUT_DIR / "la_persistent_asset_watch.csv",
    "gp_watchlist": OUTPUT_DIR / "gp_watchlist.csv",
    "institutional_relationships": OUTPUT_DIR / "institutional_relationships.csv",
    "relationship_graph": OUTPUT_DIR / "relationship_graph.csv",
    "historical_memory": OUTPUT_DIR / "historical_memory.csv",
    "persistent_asset_memory": OUTPUT_DIR / "persistent_asset_memory.csv",
    "lifecycle_transition": OUTPUT_DIR / "lifecycle_transition.csv",
    "relationship_persistence": OUTPUT_DIR / "relationship_persistence.csv",
    "pipeline_health": OUTPUT_DIR / "pipeline_health.csv",
    "source_coverage_report": OUTPUT_DIR / "source_coverage_report.csv",
    "market_intelligence_diagnostics": OUTPUT_DIR / "market_intelligence_diagnostics.csv",
    "regime_history": OUTPUT_DIR / "regime_history.csv",
    "regime_timeline": OUTPUT_DIR / "regime_timeline.csv",
    "run_summary": OUTPUT_DIR / "run_summary.md",
}

CLOUD_MISSING_MESSAGE = (
    "Output files are not available yet. Run `news_collector.py` locally "
    "or upload generated output files."
)

FILTER_FIELD_MAP = {
    "market": ["market", "la_submarket", "submarket", "city_or_submarket", "market_or_region"],
    "residential_sector": ["residential_sector", "residential_sector_focus"],
    "gp_or_developer": ["gp_or_developer", "canonical_gp_name", "firm_name", "local_gp_or_developer"],
    "lender": ["lender_or_debt_provider", "lender_or_capital_provider", "lender_or_capital_partner", "lender"],
    "lifecycle_stage": ["current_lifecycle_stage", "latest_lifecycle_stage", "lifecycle_stage_history", "current_stage"],
    "confidence": ["signal_quality_label", "institutional_confidence_label", "confidence_level"],
}


# ---------------------------------------------------------
# Data loading
# ---------------------------------------------------------

@st.cache_data
def read_csv_safely(path_string):
    """Read a CSV file. Missing files become empty tables for cloud safety."""
    path = Path(path_string)
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception as error:
        st.warning(f"Could not read `{path.name}`: {error}")
        return pd.DataFrame()


@st.cache_data
def read_markdown_safely(path_string):
    """Read a Markdown file. Missing files become blank text for cloud safety."""
    path = Path(path_string)
    if not path.exists():
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except Exception as error:
        return f"Could not read `{path.name}`: {error}"


def load_shared_data():
    """Load every dashboard dataset from relative output/ paths."""
    return {
        "summary": read_csv_safely(str(FILES["dashboard_summary"])),
        "cards": read_csv_safely(str(FILES["dashboard_cards"])),
        "watchlists": read_csv_safely(str(FILES["dashboard_watchlists"])),
        "high_confidence": read_csv_safely(str(FILES["high_confidence"])),
        "opportunities": read_csv_safely(str(FILES["opportunities"])),
        "distress": read_csv_safely(str(FILES["distress"])),
        "la_assets": read_csv_safely(str(FILES["la_assets"])),
        "la_entitlement": read_csv_safely(str(FILES["la_entitlement"])),
        "la_lifecycle": read_csv_safely(str(FILES["la_lifecycle"])),
        "development_lifecycle": read_csv_safely(str(FILES["development_lifecycle"])),
        "entitlement_intelligence": read_csv_safely(str(FILES["entitlement_intelligence"])),
        "asset_parcel_intelligence": read_csv_safely(str(FILES["asset_parcel_intelligence"])),
        "timing_intelligence": read_csv_safely(str(FILES["timing_intelligence"])),
        "la_persistent_assets": read_csv_safely(str(FILES["la_persistent_assets"])),
        "gp_watchlist": read_csv_safely(str(FILES["gp_watchlist"])),
        "institutional_relationships": read_csv_safely(str(FILES["institutional_relationships"])),
        "relationship_graph": read_csv_safely(str(FILES["relationship_graph"])),
        "historical_memory": read_csv_safely(str(FILES["historical_memory"])),
        "persistent_asset_memory": read_csv_safely(str(FILES["persistent_asset_memory"])),
        "lifecycle_transition": read_csv_safely(str(FILES["lifecycle_transition"])),
        "relationship_persistence": read_csv_safely(str(FILES["relationship_persistence"])),
        "health": read_csv_safely(str(FILES["pipeline_health"])),
        "source_coverage": read_csv_safely(str(FILES["source_coverage_report"])),
        "market_intelligence_diagnostics": read_csv_safely(str(FILES["market_intelligence_diagnostics"])),
        "regime_history": read_csv_safely(str(FILES["regime_history"])),
        "regime_timeline": read_csv_safely(str(FILES["regime_timeline"])),
        "articles": read_csv_safely(str(FILES["articles"])),
    }


# ---------------------------------------------------------
# Basic helpers
# ---------------------------------------------------------

def truncate_text(value, limit=120):
    """Shorten long titles and descriptions for phone screens."""
    text = str(value or "").strip()
    if not text or text.lower() == "nan":
        return ""
    return text if len(text) <= limit else text[: limit - 3].rstrip() + "..."


def file_label(path):
    """Return cloud-safe relative file labels."""
    if path is None:
        return "output/"
    return f"output/{Path(path).name}"


def missing_file_message(path=None):
    """Friendly message for local and Streamlit Cloud missing-output cases."""
    st.warning(CLOUD_MISSING_MESSAGE)
    if path:
        st.caption(f"Expected file: `{file_label(path)}`")


def source_reference(*paths):
    """Show which generated files power a section."""
    labels = ", ".join(f"`{file_label(path)}`" for path in paths if path)
    if labels:
        st.caption(f"Source: {labels}")


def as_number(value, fallback=0):
    """Safely coerce values to numbers."""
    try:
        if pd.isna(value):
            return fallback
        return float(value)
    except Exception:
        return fallback


def latest_summary(summary_df):
    """Return the latest dashboard summary row."""
    if summary_df.empty:
        return {}
    return summary_df.tail(1).iloc[0].to_dict()


def get_first(row, fields, default=""):
    """Return the first non-empty field from a row dictionary."""
    for field in fields:
        value = row.get(field, "")
        try:
            if pd.isna(value):
                continue
        except Exception:
            pass
        text = str(value).strip()
        if text and text.lower() not in {"nan", "none", "null"}:
            return value
    return default


def get_title(row):
    """Find the best title-like value across different output files."""
    return truncate_text(
        get_first(
            row,
            [
                "card_title",
                "canonical_project_name",
                "asset_or_project_name",
                "project_or_asset_name",
                "opportunity_type",
                "distress_type",
                "canonical_gp_name",
                "firm_name",
                "entity_name",
                "source_article_title",
                "title",
                "item_name",
            ],
            "Untitled signal",
        ),
        160,
    )


def get_score(row):
    """Find the most useful score across different output files."""
    return as_number(
        get_first(
            row,
            [
                "card_score",
                "overall_signal_quality_score",
                "opportunity_score",
                "distress_score",
                "la_asset_opportunity_score",
                "emerging_gp_score",
                "institutional_relationship_score",
                "relationship_strength_score",
                "persistent_asset_score",
                "persistence_score",
                "market_entry_score",
            ],
            0,
        )
    )


def get_market(row):
    """Find a market or submarket label."""
    return truncate_text(get_first(row, FILTER_FIELD_MAP["market"], "Unknown"), 90)


def get_sector(row):
    """Find a residential sector label."""
    return truncate_text(get_first(row, FILTER_FIELD_MAP["residential_sector"], "General Residential"), 90)


def get_gp(row):
    """Find GP, developer, or firm name."""
    return truncate_text(get_first(row, FILTER_FIELD_MAP["gp_or_developer"], ""), 100)


def get_lender(row):
    """Find lender or capital partner."""
    return truncate_text(get_first(row, FILTER_FIELD_MAP["lender"], ""), 100)


def get_lifecycle_stage(row):
    """Find current lifecycle stage."""
    return truncate_text(get_first(row, FILTER_FIELD_MAP["lifecycle_stage"], ""), 120)


def get_signal_type(row):
    """Find a concise signal type label."""
    return truncate_text(
        get_first(
            row,
            [
                "card_type",
                "strategic_theme",
                "opportunity_type",
                "distress_type",
                "asset_strategy_signal",
                "current_lifecycle_stage",
                "relationship_type",
                "watchlist_category",
                "signal_type",
            ],
            "Signal",
        ),
        100,
    )


def get_priority(row):
    """Find priority label from common generated columns."""
    return get_first(
        row,
        [
            "card_priority",
            "opportunity_priority_label",
            "distress_priority_label",
            "priority_label",
            "woomi_asset_watch_priority",
            "gp_tier",
        ],
        "Monitor",
    )


def get_reason(row):
    """Find a reason/summary field or generate one."""
    return get_first(row, ["why_it_matters", "summary", "supporting_evidence_summary", "evidence_signals"], executive_summary(row))


def get_url(row):
    """Find original URL if available."""
    return get_first(row, ["url", "source_url_if_available"], "")


def text_blob(row):
    """Join row values for deterministic matching."""
    return " ".join(str(value).lower() for value in row.values() if value not in ["", None])


def sort_by_score(df, score_columns=None):
    """Sort by the first score column found."""
    if df.empty:
        return df
    columns = score_columns or [
        "card_score",
        "overall_signal_quality_score",
        "opportunity_score",
        "distress_score",
        "la_asset_opportunity_score",
        "emerging_gp_score",
        "institutional_relationship_score",
        "persistence_score",
    ]
    score_column = next((column for column in columns if column in df.columns), None)
    if not score_column:
        return df
    sorted_df = df.copy()
    sorted_df["_sort_score"] = pd.to_numeric(sorted_df[score_column], errors="coerce").fillna(0)
    return sorted_df.sort_values("_sort_score", ascending=False).drop(columns=["_sort_score"])


def health_status(health_df):
    """Summarize pipeline health."""
    if health_df.empty or "status" not in health_df.columns:
        return "Unknown"
    if (health_df["status"] == "Error").any():
        return "Error"
    if (health_df["status"] == "Warning").any():
        return "Warning"
    return "OK"


# ---------------------------------------------------------
# Visual design
# ---------------------------------------------------------

def inject_css():
    """CSS polish using Streamlit markdown only."""
    st.markdown(
        """
        <style>
        .block-container { padding-top: 1rem; padding-bottom: 2rem; max-width: 1200px; }
        section[data-testid="stSidebar"] { width: 17rem !important; }
        h1 { letter-spacing: 0; }
        h2, h3 { margin-top: 1.2rem; }
        .metric-card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 0.55rem;
            padding: 0.68rem 0.75rem;
            margin-bottom: 0.55rem;
        }
        .metric-label { color: #64748b; font-size: 0.76rem; font-weight: 700; }
        .metric-value { color: #0f172a; font-size: 1.05rem; font-weight: 800; }
        .metric-help { color: #64748b; font-size: 0.74rem; }
        .hero-card, .workstation-card {
            border: 1px solid #cbd5e1;
            border-left: 7px solid #0f172a;
            border-radius: 0.75rem;
            padding: 1.15rem 1.2rem;
            background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
            margin: 0.3rem 0 1rem 0;
        }
        .brief-card {
            border: 1px solid #d8dee9;
            border-left: 5px solid #1f4e79;
            border-radius: 0.65rem;
            padding: 0.95rem 1rem;
            background: #fbfcfe;
            margin-bottom: 0.85rem;
        }
        .section-kicker {
            color: #334155;
            font-size: 0.78rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.03rem;
            margin-bottom: 0.25rem;
        }
        .signal-title { font-size: 1.05rem; font-weight: 760; margin: 0.15rem 0 0.35rem 0; }
        .muted-label { color: #64748b; font-size: 0.84rem; font-weight: 650; }
        .small-divider { border-top: 1px solid #e5e7eb; margin: 0.75rem 0; }
        @media (max-width: 760px) {
            .block-container { padding-left: 0.75rem; padding-right: 0.75rem; }
            .hero-card, .workstation-card { padding: 0.95rem; }
            .brief-card { padding: 0.85rem; }
            .signal-title { font-size: 0.98rem; }
            .metric-value { font-size: 0.98rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def badge(text, color="#334155", background="#f1f5f9", border="#cbd5e1"):
    """Return a compact HTML badge."""
    return (
        f"<span style='display:inline-block;padding:0.16rem 0.5rem;"
        f"border-radius:999px;background:{background};color:{color};"
        f"border:1px solid {border};font-size:0.76rem;font-weight:750;"
        f"margin:0.08rem 0.15rem 0.08rem 0;'>{text}</span>"
    )


def score_badge(score):
    """Colored score badge."""
    value = int(as_number(score))
    if value >= 85:
        return badge(f"Score {value}", "#7f1d1d", "#fee2e2", "#fecaca")
    if value >= 70:
        return badge(f"Score {value}", "#92400e", "#fef3c7", "#fde68a")
    if value >= 50:
        return badge(f"Score {value}", "#075985", "#e0f2fe", "#bae6fd")
    return badge(f"Score {value}")


def priority_badge(value):
    """Priority badge."""
    text = str(value or "Monitor")
    if any(term in text for term in ["Critical", "Immediate", "High", "Tier 1"]):
        return badge(text, "#7f1d1d", "#fee2e2", "#fecaca")
    if any(term in text for term in ["Strategic", "Medium", "Tier 2"]):
        return badge(text, "#92400e", "#fef3c7", "#fde68a")
    if any(term in text for term in ["Low", "Monitor", "Tier 3"]):
        return badge(text, "#166534", "#dcfce7", "#bbf7d0")
    return badge(text)


def signal_quality_badge(value):
    """Confidence badge."""
    text = str(value or "Emerging Signal")
    if "Institutional Grade" in text or "Strong Institutional" in text:
        return badge("Institutional Grade", "#075985", "#e0f2fe", "#7dd3fc")
    if "High" in text or "Strong" in text:
        return badge("High Confidence", "#166534", "#dcfce7", "#bbf7d0")
    if "Weak" in text or "Noise" in text or "Low" in text:
        return badge("Weak Signal", "#7f1d1d", "#fee2e2", "#fecaca")
    return badge("Emerging Signal", "#92400e", "#fef3c7", "#fde68a")


def risk_opportunity_badge(value):
    """Opportunity, risk, or capital-flow badge."""
    text = str(value or "Signal")
    lowered = text.lower()
    if "opportunity" in lowered or "acquisition" in lowered or "jv" in lowered:
        return badge("Opportunity", "#166534", "#dcfce7", "#bbf7d0")
    if any(term in lowered for term in ["distress", "risk", "stress", "refinancing", "stalled"]):
        return badge("Risk / Stress", "#7f1d1d", "#fee2e2", "#fecaca")
    if any(term in lowered for term in ["capital", "institutional", "flow"]):
        return badge("Capital Flow", "#075985", "#e0f2fe", "#bae6fd")
    return badge("Market Signal")


def pipeline_health_badge(status):
    """Pipeline health badge."""
    if status == "OK":
        return badge("Pipeline OK", "#166534", "#dcfce7", "#bbf7d0")
    if status == "Warning":
        return badge("Pipeline Warning", "#92400e", "#fef3c7", "#fde68a")
    if status == "Error":
        return badge("Pipeline Error", "#7f1d1d", "#fee2e2", "#fecaca")
    return badge("Pipeline Unknown")


def render_badges(badges):
    """Render HTML badges on one line."""
    st.markdown("".join(badges), unsafe_allow_html=True)


def confidence_label(row):
    """Choose an executive confidence label."""
    explicit = get_first(row, ["signal_quality_label", "institutional_confidence_label", "confidence_level"], "")
    if explicit:
        if "Institutional Grade" in explicit or "Strong Institutional" in explicit:
            return "Institutional Grade"
        if "High" in explicit or "Strong" in explicit:
            return "High Confidence"
        if "Weak" in explicit or "Noise" in explicit or "Low" in explicit:
            return "Weak Signal"
    score = get_score(row)
    if score >= 85:
        return "Institutional Grade"
    if score >= 70:
        return "High Confidence"
    if score >= 45:
        return "Emerging Signal"
    return "Weak Signal"


# ---------------------------------------------------------
# Filters
# ---------------------------------------------------------

def collect_options(dataframes, columns):
    """Collect unique values across many possible columns."""
    values = []
    for df in dataframes:
        if df.empty:
            continue
        for column in columns:
            if column in df.columns:
                values.extend(str(value) for value in df[column].dropna().unique() if str(value).strip())
    return sorted(set(values))


def set_quick_focus(value):
    """Set a sidebar quick-focus state."""
    st.session_state["quick_focus"] = value


def show_global_filters(dataframes):
    """Interactive filter experience with quick focus shortcuts."""
    if "quick_focus" not in st.session_state:
        st.session_state["quick_focus"] = "All"

    st.sidebar.markdown("### Today's Focus")
    for label in ["Top Opportunities", "Refinancing Stress", "LA Watch", "GP Watchlist", "High Confidence", "Distress Signals"]:
        st.sidebar.button(label, on_click=set_quick_focus, args=(label,), use_container_width=True)
    if st.sidebar.button("Reset filters", use_container_width=True):
        st.session_state["quick_focus"] = "All"

    filters = {"quick_focus": st.session_state["quick_focus"]}
    with st.sidebar.expander("Advanced Filters", expanded=False):
        for key, columns in FILTER_FIELD_MAP.items():
            options = collect_options(dataframes, columns)
            if options:
                selected = st.multiselect(key.replace("_", " ").title(), options)
                if selected:
                    filters[key] = selected
        filters["opportunity_risk"] = st.selectbox("Opportunity / Risk", ["All", "Opportunity", "Risk / Stress", "Capital Flow"])
        filters["california_only"] = st.checkbox("California only")
        filters["la_only"] = st.checkbox("LA only")
    return filters


def row_matches_any(row, columns, selected_values):
    """Check whether any selected value appears in matching columns."""
    selected = [str(value).lower() for value in selected_values]
    for column in columns:
        value = str(row.get(column, "")).lower()
        if any(item == value or item in value for item in selected):
            return True
    return False


def row_matches_quick_focus(row, focus):
    """Apply deterministic quick focus shortcuts."""
    if focus == "All":
        return True
    blob = text_blob(row)
    signal = get_signal_type(row).lower()
    market = get_market(row).lower()
    confidence = confidence_label(row).lower()
    if focus == "Top Opportunities":
        return "opportunity" in blob or "acquisition" in blob or "jv" in blob
    if focus == "Refinancing Stress":
        return any(term in blob for term in ["refinancing", "maturity", "loan", "debt", "recap"])
    if focus == "LA Watch":
        return "los angeles" in blob or market in ["los angeles", "california"] or "la " in blob
    if focus == "GP Watchlist":
        return "gp" in signal or "developer" in blob or "partnership" in blob
    if focus == "High Confidence":
        return "institutional" in confidence or "high" in confidence or get_score(row) >= 70
    if focus == "Distress Signals":
        return any(term in blob for term in ["distress", "default", "stalled", "foreclosure", "risk"])
    return True


def apply_filters(df, filters):
    """Apply advanced filters only where fields exist."""
    if df.empty or not filters:
        return df
    filtered = df.copy()
    for key, columns in FILTER_FIELD_MAP.items():
        selected = filters.get(key)
        if selected:
            filtered = filtered[filtered.apply(lambda row: row_matches_any(row, columns, selected), axis=1)]
    focus = filters.get("quick_focus", "All")
    if focus != "All":
        filtered = filtered[filtered.apply(lambda row: row_matches_quick_focus(row.to_dict(), focus), axis=1)]
    if filters.get("opportunity_risk") and filters["opportunity_risk"] != "All":
        selected_type = filters["opportunity_risk"].lower()
        filtered = filtered[filtered.apply(lambda row: selected_type in get_signal_type(row.to_dict()).lower() or selected_type in text_blob(row.to_dict()), axis=1)]
    if filters.get("california_only"):
        filtered = filtered[filtered.apply(lambda row: "california" in text_blob(row.to_dict()) or get_market(row.to_dict()).lower() == "california", axis=1)]
    if filters.get("la_only"):
        filtered = filtered[filtered.apply(lambda row: "los angeles" in text_blob(row.to_dict()) or "la " in text_blob(row.to_dict()) or get_market(row.to_dict()).lower() == "los angeles", axis=1)]
    return filtered


# ---------------------------------------------------------
# Rule-based summaries and actions
# ---------------------------------------------------------

def woomi_angle(row):
    """Generate a deterministic Woomi-specific interpretation."""
    blob = text_blob(row)
    market = get_market(row)
    if any(term in blob for term in ["refinancing", "loan", "debt", "fannie", "freddie", "capital flow"]):
        return "Refinancing opportunity angle: monitor debt pressure, lender behavior, and recapitalization windows."
    if any(term in blob for term in ["entitlement", "permit", "ceqa", "zoning", "planning"]):
        return "Entitlement monitoring angle: track approval precedent, permitting risk, and California execution timing."
    if any(term in blob for term in ["acquisition", "distress", "stalled", "seller"]):
        return "Acquisition angle: watch for sourcing, rescue capital, or discounted-basis opportunities."
    if any(term in blob for term in ["jv", "partnership", "gp", "developer"]):
        return "Development partnership angle: review sponsor capability and possible GP relationship relevance."
    if "california" in blob or "los angeles" in blob or market in ["Los Angeles", "California"]:
        return "LA / California strategy angle: relevant to local market monitoring and site strategy."
    return "Strategic monitoring angle: keep on the radar and look for repeat confirmation."


def executive_summary(row):
    """Create a short rule-based executive sentence."""
    title = get_title(row)
    market = get_market(row)
    gp = get_gp(row) or "the relevant sponsor"
    blob = text_blob(row)
    if "refinancing" in blob or "loan" in blob or "debt" in blob:
        return f"{gp} activity in {market} points to a financing or refinancing signal that may affect underwriting or recapitalization timing."
    if "distress" in blob or "stalled" in blob or "default" in blob:
        return f"{title} suggests a stress signal in {market}; Woomi should watch for acquisition, recapitalization, or JV gap potential."
    if "entitlement" in blob or "permit" in blob or "ceqa" in blob:
        return f"{title} is relevant to entitlement execution in {market}, especially timing, permitting precedent, and local development risk."
    if "capital" in blob or "institutional" in blob:
        return f"{gp} indicates institutional capital movement in {market}; this may help benchmark pricing and capital partner behavior."
    return f"{title} is worth monitoring because it may affect timing, GP behavior, or Woomi's target-market posture."


def recommended_action(row):
    """Find or generate an action label."""
    action = get_first(
        row,
        [
            "recommended_action",
            "recommended_executive_action",
            "recommended_next_action",
            "recommended_follow_up",
            "recommended_local_follow_up",
        ],
        "",
    )
    if action:
        return truncate_text(action, 180)
    signal = get_signal_type(row).lower()
    blob = text_blob(row)
    if "distress" in signal or "refinancing" in signal or "loan" in blob:
        return "Track financing timing and check whether a recapitalization window is emerging."
    if "entitlement" in signal or "permit" in signal:
        return "Monitor approval status and compare against LA / California entitlement precedent."
    if "gp" in signal or "partnership" in signal:
        return "Review sponsor relationship history and possible GP partnership relevance."
    return "Keep on the daily watchlist and look for repeat confirmation."


def executive_action_bullets(row):
    """Generate deterministic executive action bullets for a signal."""
    blob = text_blob(row)
    actions = ["Monitor for repeat confirmation in the next collector run."]
    if any(term in blob for term in ["refinancing", "maturity", "loan", "debt", "recap"]):
        actions.append("Track refinancing timing, lender names, and recapitalization pressure.")
        actions.append("Underwrite sensitivity to debt cost, proceeds, and exit cap rates.")
    if any(term in blob for term in ["distress", "stalled", "default", "foreclosure"]):
        actions.append("Watch for rescue capital, discounted sale, or stalled-project acquisition potential.")
    if any(term in blob for term in ["entitlement", "permit", "ceqa", "zoning", "planning"]):
        actions.append("Track entitlement status and compare with LA / California approval precedent.")
    if any(term in blob for term in ["jv", "partnership", "gp", "developer"]):
        actions.append("Investigate GP relationship history and partnership relevance.")
    if any(term in blob for term in ["construction start", "delivery", "lease-up", "stabilized"]):
        actions.append("Monitor construction start, delivery, and lease-up timing.")
    return list(dict.fromkeys(actions))[:5]


def article_preview(row):
    """Show source and original article link if available."""
    source = get_first(row, ["source", "source_report"], "")
    preview = truncate_text(get_first(row, ["article_text_sample", "summary", "why_it_matters", "evidence_signals"], ""), 420)
    url = get_url(row)
    if not source and not preview and not url:
        return
    st.markdown('<div class="small-divider"></div>', unsafe_allow_html=True)
    if source:
        st.caption(f"Source: {source}")
    if preview:
        st.markdown(f"**Source preview:** {preview}")
    if isinstance(url, str) and url.startswith("http"):
        st.markdown(f"[Read original article]({url})")


# ---------------------------------------------------------
# Relationship and history matching
# ---------------------------------------------------------

def signal_keys(row):
    """Extract deterministic keys used for related-intelligence matching."""
    return {
        "title": get_title(row),
        "project": get_first(row, ["canonical_project_name", "canonical_asset_or_project_name", "project_or_asset_name", "asset_or_project_name"], ""),
        "gp": get_gp(row),
        "market": get_market(row),
        "sector": get_sector(row),
        "lender": get_lender(row),
        "stage": get_lifecycle_stage(row),
        "signal": get_signal_type(row),
    }


def match_dataframe(df, keys, candidate_columns=None, limit=8):
    """Find related rows using market, GP, project, lender, and stage text."""
    if df.empty:
        return df
    candidates = [value for value in keys.values() if value and value not in ["Unknown", "General Residential", "Signal"]]
    candidates = [str(value).lower() for value in candidates if len(str(value)) > 2]
    if not candidates:
        return pd.DataFrame()
    columns = candidate_columns or list(df.columns)
    existing_columns = [column for column in columns if column in df.columns]
    if not existing_columns:
        existing_columns = list(df.columns)

    def score_row(row):
        blob = " ".join(str(row.get(column, "")).lower() for column in existing_columns)
        score = 0
        for value in candidates:
            if value in blob:
                score += 1
        return score

    related = df.copy()
    related["_match_score"] = related.apply(score_row, axis=1)
    related = related[related["_match_score"] > 0]
    if related.empty:
        return related.drop(columns=["_match_score"], errors="ignore")
    related = sort_by_score(related.sort_values("_match_score", ascending=False), None)
    return related.drop(columns=["_match_score"], errors="ignore").head(limit)


def render_related_table(title, df, source_path, limit=5):
    """Render compact related records."""
    if df.empty:
        st.caption(f"No related {title.lower()} found.")
        return
    st.markdown(f"**{title}**")
    for index, (_, row) in enumerate(df.head(limit).iterrows(), start=1):
        item = row.to_dict()
        st.markdown(
            f"- **{truncate_text(get_title(item), 100)}** "
            f"| {get_market(item)} | {get_gp(item) or get_lender(item) or 'No firm'} | Score {int(get_score(item))}"
        )
    source_reference(source_path)


def render_related_signals(row, shared):
    """Show related opportunity, distress, high-confidence, and dashboard signals."""
    keys = signal_keys(row)
    st.markdown("#### Related Signals")
    render_related_table(
        "Opportunity signals",
        match_dataframe(shared["opportunities"], keys, limit=4),
        FILES["opportunities"],
    )
    render_related_table(
        "Distress signals",
        match_dataframe(shared["distress"], keys, limit=4),
        FILES["distress"],
    )
    render_related_table(
        "High-confidence signals",
        match_dataframe(shared["high_confidence"], keys, limit=4),
        FILES["high_confidence"],
    )


def render_related_projects(row, shared):
    """Show related projects and lifecycle records."""
    keys = signal_keys(row)
    st.markdown("#### Related Projects")
    render_related_table(
        "Persistent assets",
        match_dataframe(shared["persistent_asset_memory"], keys, limit=5),
        FILES["persistent_asset_memory"],
    )
    render_related_table(
        "Lifecycle transitions",
        match_dataframe(shared["lifecycle_transition"], keys, limit=5),
        FILES["lifecycle_transition"],
    )


def render_related_gp_activity(row, shared):
    """Show related GP, institutional, and relationship activity."""
    keys = signal_keys(row)
    st.markdown("#### Related GP / Capital Activity")
    render_related_table(
        "GP watchlist",
        match_dataframe(shared["gp_watchlist"], keys, limit=4),
        FILES["gp_watchlist"],
    )
    render_related_table(
        "Institutional relationships",
        match_dataframe(shared["institutional_relationships"], keys, limit=4),
        FILES["institutional_relationships"],
    )
    render_related_table(
        "Relationship graph",
        match_dataframe(shared["relationship_graph"], keys, limit=4),
        FILES["relationship_graph"],
    )


def render_signal_history(row, shared):
    """Show historical context for recurring signals."""
    keys = signal_keys(row)
    st.markdown("#### Historical Context")
    history = match_dataframe(shared["historical_memory"], keys, limit=5)
    assets = match_dataframe(shared["persistent_asset_memory"], keys, limit=5)
    persistence = match_dataframe(shared["relationship_persistence"], keys, limit=5)

    if history.empty and assets.empty and persistence.empty:
        st.caption("No historical context found yet. This may be a newly detected or weakly matched signal.")
        return

    if not history.empty:
        top = history.iloc[0].to_dict()
        cols = st.columns(3)
        cols[0].metric("Observations", int(as_number(top.get("observation_count", 0))))
        cols[1].metric("Persistence", int(as_number(top.get("persistence_score", 0))))
        cols[2].metric("Momentum", top.get("momentum_direction", "Unknown"))
        st.markdown(f"**Recurring label:** {top.get('recurring_signal_label', 'Unknown')}")
        source_reference(FILES["historical_memory"])

    if not assets.empty:
        top_asset = assets.iloc[0].to_dict()
        st.markdown(
            f"**Asset memory:** {truncate_text(top_asset.get('canonical_project_name', 'Related asset'), 120)} "
            f"appears {top_asset.get('observation_count', 0)} time(s), latest stage "
            f"`{top_asset.get('latest_lifecycle_stage', 'Unknown')}`."
        )
        st.caption(
            f"Financing signals: {top_asset.get('financing_signal_count', 0)} | "
            f"Distress signals: {top_asset.get('distress_signal_count', 0)} | "
            f"Progression: {top_asset.get('progression_status', 'Unknown')}"
        )
        source_reference(FILES["persistent_asset_memory"])

    if not persistence.empty:
        render_related_table("Relationship persistence", persistence, FILES["relationship_persistence"], limit=3)


# ---------------------------------------------------------
# Drill-down components
# ---------------------------------------------------------

def render_signal_detail(row, shared):
    """Expanded drill-down view for one signal."""
    render_badges([
        score_badge(get_score(row)),
        priority_badge(get_priority(row)),
        risk_opportunity_badge(get_signal_type(row)),
        signal_quality_badge(confidence_label(row)),
    ])
    st.markdown(f"**Full summary:** {get_reason(row)}")
    st.markdown(f"**Why it matters:** {executive_summary(row)}")
    st.markdown(f"**Woomi angle:** {woomi_angle(row)}")
    st.markdown(f"**Related market:** {get_market(row)}")
    st.markdown(f"**Related GP / developer:** {get_gp(row) or 'Not specified'}")
    st.markdown(f"**Related lender / capital provider:** {get_lender(row) or 'Not specified'}")
    st.markdown(f"**Lifecycle stage:** {get_lifecycle_stage(row) or 'Not specified'}")
    st.markdown(f"**Recommended next action:** {recommended_action(row)}")

    st.markdown("#### Recommended Executive Actions")
    for action in executive_action_bullets(row):
        st.markdown(f"- {action}")

    article_preview(row)

    if not is_detail_mode():
        with st.expander("Supporting intelligence", expanded=False):
            render_related_signals(row, shared)
        return

    tabs = st.tabs(["Related Intelligence", "Projects", "GP / Capital", "History"])
    with tabs[0]:
        render_related_signals(row, shared)
    with tabs[1]:
        render_related_projects(row, shared)
    with tabs[2]:
        render_related_gp_activity(row, shared)
    with tabs[3]:
        render_signal_history(row, shared)


def render_signal_card(row, shared, rank=None, expanded=False):
    """Reusable drill-down signal card."""
    title = get_title(row)
    score = get_score(row)
    prefix = f"{rank}. " if rank else ""
    with st.expander(f"{prefix}{truncate_text(title, 92)} | Score {int(score)}", expanded=expanded):
        render_signal_detail(row, shared)


def render_mobile_card(row, shared=None, rank=None, expanded=False):
    """Backward-compatible mobile card wrapper."""
    if shared:
        render_signal_card(row, shared, rank=rank, expanded=expanded)
        return
    with st.expander(f"{rank or ''}. {truncate_text(get_title(row), 86)} | Score {int(get_score(row))}", expanded=expanded):
        render_badges([score_badge(get_score(row)), priority_badge(get_priority(row)), signal_quality_badge(confidence_label(row))])
        st.markdown(f"**Why it matters:** {get_reason(row)}")
        st.markdown(f"**Recommended action:** {recommended_action(row)}")


def render_watchlist_items(df, shared, source_path, limit=8):
    """Watchlist experience with score, recurring pattern, confidence, and details."""
    if df.empty:
        missing_file_message(source_path)
        return
    for index, (_, row) in enumerate(sort_by_score(df).head(limit).iterrows(), start=1):
        item = row.to_dict()
        with st.expander(f"{index}. {truncate_text(get_title(item), 90)} | Score {int(get_score(item))}", expanded=(index == 1)):
            render_badges([score_badge(get_score(item)), priority_badge(get_priority(item)), signal_quality_badge(confidence_label(item))])
            st.markdown(f"**Related market:** {get_market(item)}")
            st.markdown(f"**Why it matters:** {get_reason(item)}")
            st.markdown(f"**Recurring pattern:** {get_first(item, ['supporting_evidence_summary', 'lifecycle_stage_history', 'progression_status'], 'No recurring pattern available yet.')}")
            st.markdown(f"**Recent activity:** {executive_summary(item)}")
            st.markdown(f"**Recommended action:** {recommended_action(item)}")
            render_signal_detail(item, shared)
    render_expandable_table("Underlying watchlist table", df, source_path)


# ---------------------------------------------------------
# Mobile and layout helpers
# ---------------------------------------------------------

def render_compact_metric(label, value, help_text=None):
    """Render one compact metric that wraps better on mobile than wide columns."""
    st.markdown(
        f"""
        <div class="metric-card">
          <div class="metric-label">{label}</div>
          <div class="metric-value">{value}</div>
          <div class="metric-help">{help_text or ""}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_expandable_table(title, df, source_path=None, height=330):
    """Keep raw tables available, but collapsed by default."""
    with st.expander(title, expanded=False):
        if df.empty:
            missing_file_message(source_path)
            return
        st.dataframe(df, use_container_width=True, height=height)
        if source_path:
            source_reference(source_path)


def kpi_strip(shared):
    """Mobile-safe KPI strip using compact cards."""
    summary = latest_summary(shared["summary"])
    status = health_status(shared["health"])
    metrics = [
        ("Pipeline", status),
        ("Institutional", int(as_number(summary.get("institutional_grade_signals", 0)))),
        ("High Confidence", int(as_number(summary.get("high_confidence_signals", 0)))),
        ("Opportunities", int(as_number(summary.get("opportunity_count", 0)))),
        ("Distress", int(as_number(summary.get("distress_count", 0)))),
        ("LA Assets", int(as_number(summary.get("la_asset_watch_count", 0)))),
        ("GP Watch", int(as_number(summary.get("gp_watchlist_count", 0)))),
    ]
    for start in range(0, len(metrics), 4):
        cols = st.columns(min(4, len(metrics) - start))
        for col, (label, value) in zip(cols, metrics[start : start + 4]):
            with col:
                render_compact_metric(label, value)


def hero_section(cards, shared):
    """Today's top signal hero."""
    cards = sort_by_score(cards, ["card_score"])
    if cards.empty:
        missing_file_message(FILES["dashboard_cards"])
        return
    row = cards.iloc[0].to_dict()
    st.markdown(
        f"""
        <div class="hero-card">
            <div class="section-kicker">오늘의 핵심 시그널</div>
            <div class="signal-title">{get_title(row)}</div>
            {score_badge(get_score(row))}
            {risk_opportunity_badge(get_signal_type(row))}
            {signal_quality_badge(confidence_label(row))}
            <div class="small-divider"></div>
            <p><b>Why it matters</b><br>{truncate_text(get_reason(row), 420)}</p>
            <p><b>Woomi implication</b><br>{woomi_angle(row)}</p>
            <p><b>Recommended action</b><br>{recommended_action(row)}</p>
            <p class="muted-label">Market: {get_market(row)} · Sector: {get_sector(row)} · GP / Developer: {get_gp(row) or "Not specified"}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.expander("Drill down into today's top signal", expanded=False):
        render_signal_detail(row, shared)


def action_bullets(cards):
    """Action checklist for daily reading."""
    st.markdown("### 오늘 체크할 액션")
    if cards.empty:
        missing_file_message(FILES["dashboard_cards"])
        return
    actions = []
    for _, row in sort_by_score(cards, ["card_score"]).head(8).iterrows():
        for action in executive_action_bullets(row.to_dict()):
            if action and action not in actions:
                actions.append(action)
    for action in actions[:6]:
        st.markdown(f"- {action}")


def top_cards(cards, shared, title="우선 확인 Top 5", limit=5):
    """Top ranked drill-down cards."""
    st.markdown(f"### {title}")
    if cards.empty:
        missing_file_message(FILES["dashboard_cards"])
        return
    for index, (_, row) in enumerate(sort_by_score(cards, ["card_score"]).head(limit).iterrows(), start=1):
        render_signal_card(row.to_dict(), shared, rank=index, expanded=(index == 1))


def market_mood(shared):
    """Short rule-based market mood."""
    summary = latest_summary(shared["summary"])
    cards = shared["cards"]
    distress_count = int(as_number(summary.get("distress_count", 0)))
    la_count = int(as_number(summary.get("la_asset_watch_count", 0)))
    high_confidence = int(as_number(summary.get("high_confidence_signals", 0)))
    capital_rows = pd.DataFrame()
    development_rows = pd.DataFrame()
    if not cards.empty and "card_type" in cards.columns:
        capital_rows = cards[cards["card_type"].astype(str).str.contains("Capital", case=False, na=False)]
        development_rows = cards[cards["card_type"].astype(str).str.contains("Lifecycle|Asset|Opportunity", case=False, na=False)]
    st.markdown("### 시장 분위기")
    st.markdown(
        f"""
- **Capital flow:** {len(capital_rows)} capital-flow card(s) are active; watch repeated lender and capital-partner references.
- **Refinancing stress:** {distress_count} distress item(s) are visible, so maturity and refinancing pressure remain on the watchlist.
- **Development activity:** {len(development_rows)} development or opportunity card(s) suggest pipeline timing and sponsor behavior should be reviewed.
- **Entitlement trend:** Check LA / California entitlement pages when permit, CEQA, zoning, or planning signals rise.
- **LA / California signals:** {la_count} LA asset watch item(s) are available for local site strategy monitoring.
- **Confidence:** {high_confidence} high-confidence signal(s) are available after quality calibration.
"""
    )


def signal_section(title, df, shared, score_columns, source_path, limit=4):
    """Reusable signal section with drill-down cards first and tables collapsed."""
    st.markdown(f"### {title}")
    if df.empty:
        missing_file_message(source_path)
        return
    active_limit = limit if is_detail_mode() else min(limit, 3)
    for index, (_, row) in enumerate(sort_by_score(df, score_columns).head(active_limit).iterrows(), start=1):
        render_signal_card(row.to_dict(), shared, rank=index, expanded=(index == 1))
    if is_detail_mode():
        render_expandable_table("Reference table", df, source_path)


def count_chart(df, column, title):
    """Simple built-in chart."""
    if df.empty or column not in df.columns:
        return
    counts = df[column].fillna("Unknown").astype(str).value_counts().head(10)
    if not counts.empty:
        st.markdown(f"**{title}**")
        st.bar_chart(counts)


def score_chart(df, label_column, score_column, title):
    """Simple score chart."""
    if df.empty or label_column not in df.columns or score_column not in df.columns:
        return
    chart_df = df[[label_column, score_column]].copy()
    chart_df[score_column] = pd.to_numeric(chart_df[score_column], errors="coerce").fillna(0)
    chart_df = chart_df.sort_values(score_column, ascending=False).head(8)
    if not chart_df.empty:
        st.markdown(f"**{title}**")
        st.bar_chart(chart_df.set_index(label_column))


def is_detail_mode():
    """Return True when the user wants diagnostics and reference tables."""
    return st.session_state.get("view_mode", "Executive Mode") == "Detail Mode"


def section_intro(title, body):
    """Consistent executive section intro."""
    st.markdown(f"## {title}")
    st.caption(body)


def read_this_first(shared):
    """Most important today panel."""
    summary = latest_summary(shared["summary"])
    focus = summary.get("recommended_executive_focus", "Review the top-ranked institutional signal and confirm whether it repeats across related outputs.")
    st.markdown(
        f"""
        <div class="workstation-card">
            <div class="section-kicker">Read This First</div>
            <div class="signal-title">Most Important Today</div>
            <p>{focus}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def output_file_status():
    """Return a dataframe showing which expected output files are available."""
    rows = []
    for key, path in FILES.items():
        rows.append(
            {
                "output_key": key,
                "file": file_label(path),
                "available": path.exists(),
                "size_kb": round(path.stat().st_size / 1024, 1) if path.exists() else 0,
            }
        )
    return pd.DataFrame(rows)


def pipeline_warning_count(health_df):
    """Count warnings and errors in pipeline health, safely."""
    if health_df.empty or "status" not in health_df.columns:
        return 0
    return int(health_df["status"].astype(str).isin(["Warning", "Error"]).sum())


def system_status_panel(shared):
    """Operational system status panel for local and Cloud deployments."""
    summary = latest_summary(shared["summary"])
    status_df = output_file_status()
    missing = status_df[~status_df["available"]]
    total_signals = len(shared["cards"]) + len(shared["high_confidence"])
    st.markdown("### System Health / Pipeline Status")
    render_badges([pipeline_health_badge(health_status(shared["health"]))])

    metrics = [
        ("Last Run", summary.get("run_timestamp", "No run data")),
        ("Output Files", f"{int(status_df['available'].sum())}/{len(status_df)}"),
        ("Warnings", pipeline_warning_count(shared["health"])),
        ("Total Signals", total_signals),
        ("High Confidence", int(as_number(summary.get("high_confidence_signals", len(shared["high_confidence"]))))),
        ("Opportunities", int(as_number(summary.get("opportunity_count", len(shared["opportunities"]))))),
        ("Distress", int(as_number(summary.get("distress_count", len(shared["distress"]))))),
    ]
    for start in range(0, len(metrics), 3):
        cols = st.columns(min(3, len(metrics) - start))
        for col, (label, value) in zip(cols, metrics[start : start + 3]):
            with col:
                render_compact_metric(label, value)

    if missing.empty:
        st.success("All expected dashboard files are available.")
    else:
        st.warning(f"{len(missing)} expected output file(s) are missing. The app will keep running with reduced data.")
        render_expandable_table("Missing output files", missing, None, height=220)


def render_site_parcel_source_diagnostics(shared):
    """Show Site / Parcel source coverage diagnostics on the system page only."""
    coverage = shared.get("source_coverage", pd.DataFrame())
    st.markdown("### Site / Parcel Source Coverage")
    if coverage.empty:
        st.info(
            "Site / Parcel source diagnostics have not been generated yet. "
            "Run `python news_collector.py` first."
        )
        return

    status = coverage.get("status", pd.Series(dtype=str)).astype(str)
    candidate_counts = pd.to_numeric(
        coverage.get("site_parcel_candidate_count", pd.Series(dtype=float)),
        errors="coerce",
    ).fillna(0)
    inaccessible_count = int(status.isin(["blocked", "error", "skipped"]).sum())
    zero_relevant_count = int((candidate_counts == 0).sum())
    metrics = [
        ("Total sources attempted", len(coverage)),
        ("Successful sources", int(status.isin(["success", "no relevant articles"]).sum())),
        ("Blocked / inaccessible", inaccessible_count),
        ("Zero relevant Site / Parcel", zero_relevant_count),
    ]
    cols = st.columns(len(metrics))
    for col, (label, value) in zip(cols, metrics):
        with col:
            render_compact_metric(label, value)

    top_sources = coverage.assign(
        _candidate_count=candidate_counts,
    ).sort_values("_candidate_count", ascending=False)
    top_sources = top_sources[top_sources["_candidate_count"] > 0].head(5)
    st.markdown("#### Top Site / Parcel candidate sources")
    if top_sources.empty:
        st.caption("No added source produced a saved Site / Parcel candidate in the latest run.")
    else:
        for _, row in top_sources.iterrows():
            st.markdown(
                f"- **{row.get('source_name', 'Unknown source')}**: "
                f"{int(row['_candidate_count'])} candidate(s) from "
                f"{int(as_number(row.get('article_count_fetched', 0)))} fetched article(s)"
            )

    with st.expander("Source detail"):
        display_columns = [
            "source_name",
            "status",
            "article_count_fetched",
            "site_parcel_candidate_count",
            "reason_if_unavailable",
        ]
        visible_columns = [column for column in display_columns if column in coverage.columns]
        st.dataframe(coverage[visible_columns], use_container_width=True, hide_index=True)


def download_center():
    """Optional lightweight downloads for daily operations."""
    st.markdown("### Downloads")
    for label, key in [
        ("Dashboard cards CSV", "dashboard_cards"),
        ("High confidence watchlist CSV", "high_confidence"),
        ("Opportunity radar CSV", "opportunities"),
        ("Korean executive brief Markdown", "korean_brief"),
    ]:
        path = FILES[key]
        if not path.exists():
            continue
        data = path.read_bytes()
        mime = "text/csv" if path.suffix == ".csv" else "text/markdown"
        st.download_button(label, data=data, file_name=path.name, mime=mime, use_container_width=True)


# ---------------------------------------------------------
# Pages
# ---------------------------------------------------------

def page_korean_executive_brief(shared, filters):
    """Daily Korean executive reading flow."""
    st.title("한국어 경영진 브리핑")
    summary = latest_summary(shared["summary"])
    st.caption(f"Latest run: {summary.get('run_timestamp', 'No run data available')} | Interactive briefing view")
    cards = apply_filters(shared["cards"], filters)
    hero_section(cards, shared)
    action_bullets(cards)
    top_cards(cards, shared, "우선 확인 Top 5")
    signal_section("LA / California Watch", apply_filters(shared["la_assets"], filters), shared, ["la_asset_opportunity_score"], FILES["la_assets"], limit=3)
    signal_section("GP / Capital Partner Watch", apply_filters(shared["gp_watchlist"], filters), shared, ["emerging_gp_score"], FILES["gp_watchlist"], limit=3)
    market_mood(shared)
    render_expandable_table("원문 데이터 / 상세 테이블", cards, FILES["dashboard_cards"])
    with st.expander("참고 원문 한국어 보고서", expanded=False):
        markdown = read_markdown_safely(str(FILES["korean_brief"]))
        if markdown:
            st.markdown(markdown)
        else:
            missing_file_message(FILES["korean_brief"])


def page_executive_dashboard(shared, filters):
    """Narrative executive dashboard."""
    st.title("경영진 대시보드")
    summary = latest_summary(shared["summary"])
    st.caption(f"Latest run: {summary.get('run_timestamp', 'No run data available')}")
    st.markdown("### Executive Snapshot")
    render_badges([pipeline_health_badge(health_status(shared["health"])), signal_quality_badge("Institutional Grade")])
    st.markdown(f"**Recommended focus:** {summary.get('recommended_executive_focus', 'No focus available yet.')}")
    market_mood(shared)
    top_cards(apply_filters(shared["cards"], filters), shared, "Top Signals")
    count_chart(apply_filters(shared["cards"], filters), "card_type", "Signal mix")
    signal_section("Opportunity Radar", apply_filters(shared["opportunities"], filters), shared, ["opportunity_score"], FILES["opportunities"], limit=3)
    signal_section("Distress Radar", apply_filters(shared["distress"], filters), shared, ["distress_score"], FILES["distress"], limit=3)
    signal_section("LA Watch", apply_filters(shared["la_assets"], filters), shared, ["la_asset_opportunity_score"], FILES["la_assets"], limit=3)
    signal_section("GP Watchlist", apply_filters(shared["gp_watchlist"], filters), shared, ["emerging_gp_score"], FILES["gp_watchlist"], limit=3)
    render_expandable_table("Pipeline Health", shared["health"], FILES["pipeline_health"])


def page_high_confidence(shared, filters):
    """High confidence signals."""
    st.title("고신뢰 신호")
    df = apply_filters(shared["high_confidence"], filters)
    signal_section("Institutional-Grade Watchlist", df, shared, ["overall_signal_quality_score"], FILES["high_confidence"], limit=8)


def page_opportunity_distress(shared, filters):
    """Opportunity and risk radar."""
    st.title("기회 / 리스크 레이더")
    tabs = st.tabs(["Opportunities", "Distress", "High Confidence"])
    with tabs[0]:
        df = apply_filters(shared["opportunities"], filters)
        count_chart(df, "market", "Opportunity count by market")
        signal_section("Top Opportunities", df, shared, ["opportunity_score"], FILES["opportunities"], limit=6)
    with tabs[1]:
        df = apply_filters(shared["distress"], filters)
        count_chart(df, "market", "Distress count by market")
        signal_section("Top Distress Signals", df, shared, ["distress_score"], FILES["distress"], limit=6)
    with tabs[2]:
        signal_section("Related High-Confidence Signals", apply_filters(shared["high_confidence"], filters), shared, ["overall_signal_quality_score"], FILES["high_confidence"], limit=5)


def page_la_asset_watch(shared, filters):
    """LA / California asset workstation."""
    st.title("LA 자산 Watch")
    tabs = st.tabs(["Assets", "Entitlement", "Lifecycle", "Persistent Memory"])
    with tabs[0]:
        df = apply_filters(shared["la_assets"], filters)
        count_chart(df, "la_submarket", "LA asset count by submarket")
        signal_section("Top LA Asset Signals", df, shared, ["la_asset_opportunity_score"], FILES["la_assets"], limit=6)
    with tabs[1]:
        df = apply_filters(shared["la_entitlement"], filters)
        count_chart(df, "la_submarket", "Entitlement count by submarket")
        signal_section("LA Entitlement Signals", df, shared, ["local_relevance_score", "entitlement_opportunity_score"], FILES["la_entitlement"], limit=5)
    with tabs[2]:
        df = apply_filters(shared["la_lifecycle"], filters)
        count_chart(df, "current_lifecycle_stage", "Lifecycle stage count")
        signal_section("LA Lifecycle Signals", df, shared, ["lifecycle_opportunity_score"], FILES["la_lifecycle"], limit=5)
    with tabs[3]:
        df = apply_filters(shared["la_persistent_assets"], filters)
        count_chart(df, "la_submarket", "Persistent asset count by submarket")
        signal_section("Persistent LA Asset Memory", df, shared, ["opportunity_score", "risk_score"], FILES["la_persistent_assets"], limit=5)


def page_gp_watchlist(shared, filters):
    """GP and institutional relationship workstation."""
    st.title("GP Watchlist")
    tabs = st.tabs(["GP Ranking", "Institutional Relationships", "Relationship Graph"])
    with tabs[0]:
        df = apply_filters(shared["gp_watchlist"], filters)
        score_chart(df, "canonical_gp_name", "emerging_gp_score", "GP watchlist score ranking")
        render_watchlist_items(df, shared, FILES["gp_watchlist"], limit=6)
    with tabs[1]:
        df = apply_filters(shared["institutional_relationships"], filters)
        score_chart(df, "firm_name", "institutional_relationship_score", "Institutional relationship score ranking")
        render_watchlist_items(df, shared, FILES["institutional_relationships"], limit=5)
    with tabs[2]:
        df = apply_filters(shared["relationship_graph"], filters)
        count_chart(df, "relationship_type", "Relationship type count")
        signal_section("Relationship Graph Edges", df, shared, ["relationship_strength_score"], FILES["relationship_graph"], limit=5)


def page_pipeline_health(shared, filters):
    """Pipeline health and troubleshooting."""
    st.title("파이프라인 상태")
    render_badges([pipeline_health_badge(health_status(shared["health"]))])
    markdown = read_markdown_safely(str(FILES["run_summary"]))
    if markdown:
        st.markdown(markdown)
    else:
        missing_file_message(FILES["run_summary"])
    render_expandable_table("Pipeline health checks", shared["health"], FILES["pipeline_health"], height=460)


def page_how_to_use(shared, filters):
    """Usage guide."""
    st.title("How to Use This App")
    st.markdown(
        """
### Drill-down workflow

1. Open a signal card.
2. Review the summary, Woomi angle, confidence, and recommended action.
3. Use the related-intelligence tabs:
   - Related Signals
   - Projects
   - GP / Capital
   - Historical Context

### Refresh data locally

```bash
python news_collector.py
```

### Open the dashboard

```bash
python -m streamlit run app.py
```

### Streamlit Cloud note

The app reads generated files from `output/`. If those files are not committed,
uploaded, or generated in the runtime, the dashboard will show missing-file
warnings instead of failing.
"""
    )


# ---------------------------------------------------------
# Operational and deployment pages
# ---------------------------------------------------------

def page_pipeline_health(shared, filters):
    """Pipeline health and troubleshooting."""
    st.title("System Health / Pipeline Status")
    system_status_panel(shared)
    markdown = read_markdown_safely(str(FILES["run_summary"]))
    if markdown:
        with st.expander("Run summary", expanded=True):
            st.markdown(markdown)
    else:
        missing_file_message(FILES["run_summary"])
    render_expandable_table("Pipeline health checks", shared["health"], FILES["pipeline_health"], height=460)
    download_center()


def page_daily_workflow(shared, filters):
    """Daily operating workflow for recurring use."""
    st.title("Daily Workflow")
    summary = latest_summary(shared["summary"])
    st.caption(f"Latest run: {summary.get('run_timestamp', 'No run data available')}")
    st.markdown(
        """
### Daily Operating Mode

1. **Run collector**  
   Run `python news_collector.py` locally to refresh RSS feeds, scoring, outputs, and reports.

2. **Refresh outputs**  
   Confirm the `output/` folder updated, especially `dashboard_summary.csv`, `dashboard_cards.csv`, and `pipeline_health.csv`.

3. **Review executive brief**  
   Start with `한국어 경영진 브리핑` for the daily top signal, actions, LA watch, and GP / capital partner watch.

4. **Review high-confidence signals**  
   Use `고신뢰 신호` to avoid noisy one-off articles and focus on institutional-grade signals.

5. **Review LA watch**  
   Use `LA 자산 Watch` for entitlement, lifecycle, and local site-strategy monitoring.

6. **Review GP watchlist**  
   Use `GP Watchlist` to check developer, sponsor, institutional relationship, and relationship graph signals.

7. **Review distress / opportunity radar**  
   Use `기회 / 리스크 레이더` to check acquisition, refinancing, distress, and recapitalization signals.

### Recommended Executive Workflow

- **10 minutes:** Korean executive brief and Top 5 signal cards.
- **20 minutes:** High-confidence signals and LA watch.
- **30 minutes:** GP watchlist, relationship context, and opportunity / distress radar.

### What Each Section Means

- **Top signal:** Highest-priority item from the dashboard data layer.
- **High confidence:** Signals that passed quality and persistence checks.
- **LA Watch:** Project, entitlement, and lifecycle intelligence for LA / California monitoring.
- **GP Watchlist:** Developer / GP behavior, partner candidates, and institutional relationship clues.
- **Opportunity / Distress:** Potential acquisition, refinancing, recapitalization, and stalled-project signals.
"""
    )
    system_status_panel(shared)


def page_deployment_checklist(shared, filters):
    """Streamlit Cloud deployment checklist."""
    st.title("Deployment Checklist")
    status_df = output_file_status()
    checks = [
        ("requirements.txt present", (BASE_DIR / "requirements.txt").exists()),
        ("app.py present", (BASE_DIR / "app.py").exists()),
        ("output folder present", OUTPUT_DIR.exists()),
        ("dashboard_summary.csv available", FILES["dashboard_summary"].exists()),
        ("pipeline_health.csv available", FILES["pipeline_health"].exists()),
        (".streamlit/config.toml present", (BASE_DIR / ".streamlit" / "config.toml").exists()),
        ("runtime.txt present", (BASE_DIR / "runtime.txt").exists()),
        (".gitignore present", (BASE_DIR / ".gitignore").exists()),
    ]
    checklist = pd.DataFrame(
        [{"check": label, "status": "OK" if passed else "Review"} for label, passed in checks]
    )
    st.dataframe(checklist, use_container_width=True, hide_index=True)
    st.markdown(
        """
### Streamlit Cloud Setup Steps

1. Push this repository to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the repository.
5. Set **Main file path** to `app.py`.
6. Deploy.

### Mobile Usage

Open the deployed Streamlit URL from a phone browser. The app uses an expanded sidebar, compact metrics, and expandable cards for mobile review.

### Known Limitation

The Cloud app reads generated files from `output/`. If those files are missing, the app shows warnings and keeps running, but the dashboard will have less data.
"""
    )
    render_expandable_table("Expected output file availability", status_df, None, height=360)


def app_header(shared):
    """Professional app header shown above every page."""
    summary = latest_summary(shared["summary"])
    st.markdown(
        """
        <div class="workstation-card">
            <div class="section-kicker">US Residential Intelligence</div>
            <div class="signal-title">Executive strategy workstation for daily residential market monitoring</div>
            <p class="muted-label">Cloud-safe Streamlit app · CSV/Markdown powered · No paid API calls</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns(3)
    with cols[0]:
        render_compact_metric("Latest Run", summary.get("run_timestamp", "No run data"))
    with cols[1]:
        render_compact_metric("Pipeline Health", health_status(shared["health"]))
    with cols[2]:
        render_compact_metric("Output Files", f"{int(output_file_status()['available'].sum())}/{len(FILES)}")


def page_executive_briefing(shared, filters):
    """Clean executive briefing page."""
    st.title("Executive Briefing")
    st.caption("Korean-first executive view with only the highest-priority strategy points.")
    cards = apply_filters(shared["cards"], filters)
    read_this_first(shared)
    hero_section(cards, shared)
    action_bullets(cards)
    top_cards(cards, shared, "Priority Review")
    signal_section("LA / California Strategy Watch", apply_filters(shared["la_assets"], filters), shared, ["la_asset_opportunity_score"], FILES["la_assets"], limit=3)
    signal_section("Top Institutional Activity", apply_filters(shared["gp_watchlist"], filters), shared, ["emerging_gp_score"], FILES["gp_watchlist"], limit=3)
    if is_detail_mode():
        market_mood(shared)
        render_expandable_table("Core output: dashboard cards", cards, FILES["dashboard_cards"])


def page_market_intelligence(shared, filters):
    """Consolidated market intelligence page."""
    st.title("Market Intelligence")
    section_intro("Market Pulse", "Capital flow, institutional-grade items, and recurring market patterns.")
    market_mood(shared)
    signal_section("Institutional Grade Review", apply_filters(shared["high_confidence"], filters), shared, ["overall_signal_quality_score"], FILES["high_confidence"], limit=5)
    signal_section("Major Capital Flow", apply_filters(shared["cards"], filters), shared, ["card_score"], FILES["dashboard_cards"], limit=4)
    if is_detail_mode():
        count_chart(apply_filters(shared["cards"], filters), "card_type", "Signal mix")
        render_expandable_table("Watchlist reference table", apply_filters(shared["watchlists"], filters), FILES["dashboard_watchlists"])


def page_opportunity_risk(shared, filters):
    """Consolidated opportunity and risk page."""
    st.title("Opportunity & Risk")
    section_intro("Investment Opportunity And Risk Monitoring", "Prioritizes acquisition, recapitalization, refinancing pressure, and execution risk.")
    signal_section("Top Investment Opportunities", apply_filters(shared["opportunities"], filters), shared, ["opportunity_score"], FILES["opportunities"], limit=5)
    signal_section("Refinancing Pressure / Execution Risk", apply_filters(shared["distress"], filters), shared, ["distress_score"], FILES["distress"], limit=5)
    if is_detail_mode():
        signal_section("Related Institutional Grade Items", apply_filters(shared["high_confidence"], filters), shared, ["overall_signal_quality_score"], FILES["high_confidence"], limit=4)


def page_la_california_strategy(shared, filters):
    """Consolidated LA / California page."""
    st.title("LA / California Strategy")
    section_intro("Local Site Strategy Watch", "Entitlement, asset, lifecycle, and persistent project intelligence for California execution.")
    signal_section("Priority LA Asset Watch", apply_filters(shared["la_assets"], filters), shared, ["la_asset_opportunity_score"], FILES["la_assets"], limit=5)
    signal_section("Entitlement And Permitting Developments", apply_filters(shared["la_entitlement"], filters), shared, ["local_relevance_score", "entitlement_opportunity_score"], FILES["la_entitlement"], limit=4)
    if is_detail_mode():
        signal_section("Lifecycle / Execution Context", apply_filters(shared["la_lifecycle"], filters), shared, ["lifecycle_opportunity_score"], FILES["la_lifecycle"], limit=4)
        signal_section("Persistent Asset Memory", apply_filters(shared["la_persistent_assets"], filters), shared, ["opportunity_score", "risk_score"], FILES["la_persistent_assets"], limit=4)


def page_gp_capital_relationships(shared, filters):
    """Consolidated GP and capital relationship page."""
    st.title("GP & Capital Relationships")
    section_intro("Institutional Relationship Watch", "Developer, GP, lender, capital partner, and relationship graph intelligence.")
    df = apply_filters(shared["gp_watchlist"], filters)
    score_chart(df, "canonical_gp_name", "emerging_gp_score", "Top GP / Developer Ranking")
    render_watchlist_items(df, shared, FILES["gp_watchlist"], limit=5 if not is_detail_mode() else 8)
    if is_detail_mode():
        render_watchlist_items(apply_filters(shared["institutional_relationships"], filters), shared, FILES["institutional_relationships"], limit=5)
        signal_section("Relationship Graph", apply_filters(shared["relationship_graph"], filters), shared, ["relationship_strength_score"], FILES["relationship_graph"], limit=5)


def page_system_pipeline_clean(shared, filters):
    """System and pipeline page with operational sub-sections."""
    st.title("System & Pipeline")
    tabs = st.tabs(["Status", "Daily Workflow", "Deployment", "Downloads"])
    with tabs[0]:
        system_status_panel(shared)
        if is_detail_mode():
            render_expandable_table("Pipeline health checks", shared["health"], FILES["pipeline_health"], height=460)
    with tabs[1]:
        page_daily_workflow(shared, filters)
    with tabs[2]:
        page_deployment_checklist(shared, filters)
    with tabs[3]:
        download_center()


# ---------------------------------------------------------
# Main app
# ---------------------------------------------------------

def legacy_main_01():
    """Run the Streamlit dashboard."""
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("Executive strategy platform")
    st.sidebar.info("Refresh data with `python news_collector.py`.")
    st.sidebar.radio("View Mode", ["Executive Mode", "Detail Mode"], key="view_mode")

    pages = {
        "한국어 경영진 브리핑": page_korean_executive_brief,
        "경영진 대시보드": page_executive_dashboard,
        "고신뢰 신호": page_high_confidence,
        "기회 / 리스크 레이더": page_opportunity_distress,
        "LA 자산 Watch": page_la_asset_watch,
        "GP Watchlist": page_gp_watchlist,
        "System Health / Pipeline Status": page_pipeline_health,
        "Daily Workflow": page_daily_workflow,
        "Deployment Checklist": page_deployment_checklist,
        "How to Use": page_how_to_use,
    }
    page_name = st.sidebar.radio("Page", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"],
        shared["watchlists"],
        shared["high_confidence"],
        shared["opportunities"],
        shared["distress"],
        shared["la_assets"],
        shared["la_entitlement"],
        shared["la_lifecycle"],
        shared["la_persistent_assets"],
        shared["gp_watchlist"],
        shared["institutional_relationships"],
        shared["relationship_graph"],
        shared["historical_memory"],
        shared["persistent_asset_memory"],
        shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"Latest run: {summary.get('run_timestamp', 'No run data available')}")
    kpi_strip(shared)
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.markdown("### Operational Footer")
    st.caption("US Residential Intelligence MVP | Streamlit Cloud-ready | Refresh data with `python news_collector.py` | No paid APIs")


def legacy_main_02():
    """Run the clean executive strategy platform."""
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("Executive strategy platform")
    st.sidebar.info("Refresh data with `python news_collector.py`.")
    st.sidebar.radio("View Mode", ["Executive Mode", "Detail Mode"], key="view_mode")

    pages = {
        "Executive Briefing": page_executive_briefing,
        "Market Intelligence": page_market_intelligence,
        "Opportunity & Risk": page_opportunity_risk,
        "LA / California Strategy": page_la_california_strategy,
        "GP & Capital Relationships": page_gp_capital_relationships,
        "System & Pipeline": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("Navigation", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"],
        shared["watchlists"],
        shared["high_confidence"],
        shared["opportunities"],
        shared["distress"],
        shared["la_assets"],
        shared["la_entitlement"],
        shared["la_lifecycle"],
        shared["la_persistent_assets"],
        shared["gp_watchlist"],
        shared["institutional_relationships"],
        shared["relationship_graph"],
        shared["historical_memory"],
        shared["persistent_asset_memory"],
        shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"Latest run: {summary.get('run_timestamp', 'No run data available')}")
    if is_detail_mode():
        kpi_strip(shared)
    else:
        cols = st.columns(3)
        with cols[0]:
            render_compact_metric("High-Conviction Items", int(as_number(summary.get("high_confidence_signals", 0))))
        with cols[1]:
            render_compact_metric("Opportunities", int(as_number(summary.get("opportunity_count", 0))))
        with cols[2]:
            render_compact_metric("LA Watch", int(as_number(summary.get("la_asset_watch_count", 0))))
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | Executive strategy platform | Streamlit Cloud-ready | No paid APIs")


# ---------------------------------------------------------
# Korean executive localization overlay
# ---------------------------------------------------------

KO_TERMS = {
    "Executive Briefing": "경영진 브리핑",
    "Read This First": "먼저 확인할 사항",
    "Most Important Today": "오늘의 최우선 검토 사항",
    "Why it matters": "중요성",
    "Recommended action": "추천 후속 조치",
    "Woomi angle": "우미 관점",
    "Source preview": "원문 요약",
    "Historical Context": "과거 관찰 이력",
    "Top Opportunities": "주요 기회",
    "Capital Flow": "자본시장 / 금융 흐름",
    "Institutional Grade": "기관투자자급 검토",
    "High Confidence": "검토 신뢰도 높음",
    "Opportunity & Risk": "기회 및 리스크",
    "Executive Mode": "경영진 모드",
    "Detail Mode": "상세 분석 모드",
    "Refinancing": "리파이낸싱",
    "Multifamily": "멀티패밀리",
    "Distress": "부실 / 스트레스",
    "Opportunity": "기회",
    "Entitlement": "인허가",
    "Permitting": "허가",
    "Lifecycle": "개발 단계",
    "GP Watchlist": "GP 모니터링",
    "Pipeline Health": "파이프라인 상태",
    "LA Asset Watch": "LA 자산 / 프로젝트 모니터링",
    "Risk / Stress": "리스크 / 스트레스",
    "Market Signal": "시장 시그널",
    "Emerging Signal": "초기 관찰",
    "Critical": "즉시 검토",
    "High": "높음",
    "Medium": "보통",
    "Low": "낮음",
    "Monitor": "모니터링",
    "Immediate": "즉시 검토",
    "Strategic": "전략 검토",
}


def ko_label(text):
    """Translate common UI labels while preserving proper nouns."""
    value = str(text or "")
    if value in KO_TERMS:
        return KO_TERMS[value]
    translated = value
    for english, korean in sorted(KO_TERMS.items(), key=lambda item: len(item[0]), reverse=True):
        translated = translated.replace(english, korean)
    return translated


def ko_signal_type(text):
    """Translate recurring signal categories into executive Korean."""
    value = str(text or "시장 시그널")
    lowered = value.lower()
    if "capital" in lowered or "flow" in lowered or "financing" in lowered:
        return "자본시장 / 금융 흐름"
    if "refinancing" in lowered or "loan" in lowered or "debt" in lowered:
        return "리파이낸싱 / 부채 압박"
    if "distress" in lowered or "stress" in lowered or "risk" in lowered:
        return "리스크 / 스트레스"
    if "opportunity" in lowered or "acquisition" in lowered:
        return "투자 기회"
    if "entitlement" in lowered or "permit" in lowered or "planning" in lowered:
        return "인허가 / 개발 승인"
    if "lifecycle" in lowered or "construction" in lowered:
        return "개발 단계 / 실행"
    if "gp" in lowered or "relationship" in lowered or "partnership" in lowered:
        return "GP / 파트너십"
    return ko_label(value)


def ko_sentence(text):
    """Light rule-based Korean sentence cleanup for recurring English phrases."""
    value = str(text or "")
    replacements = {
        "refinancing signal": "리파이낸싱 시그널",
        "capital-flow": "자본시장 / 금융 흐름",
        "Capital-flow": "자본시장 / 금융 흐름",
        "lender behavior": "대주단 움직임",
        "recapitalization windows": "recap 기회 구간",
        "underwriting": "언더라이팅",
        "distress": "부실 / 스트레스",
        "entitlement": "인허가",
        "permitting": "허가",
        "developer": "디벨로퍼",
        "GP relationship": "GP 관계",
    }
    for english, korean in replacements.items():
        value = value.replace(english, korean)
    return value


def ko_badge(text, color="#334155", background="#f1f5f9", border="#cbd5e1"):
    """Korean-friendly badge."""
    return badge(ko_label(text), color, background, border)


def score_badge(score):
    """Korean score badge."""
    value = int(as_number(score))
    if value >= 85:
        return badge(f"점수 {value}", "#7f1d1d", "#fee2e2", "#fecaca")
    if value >= 70:
        return badge(f"점수 {value}", "#92400e", "#fef3c7", "#fde68a")
    if value >= 50:
        return badge(f"점수 {value}", "#075985", "#e0f2fe", "#bae6fd")
    return badge(f"점수 {value}")


def priority_badge(value):
    """Korean priority badge."""
    text = ko_label(value or "Monitor")
    if any(term in str(value) for term in ["Critical", "Immediate", "High", "Tier 1"]):
        return badge(text, "#7f1d1d", "#fee2e2", "#fecaca")
    if any(term in str(value) for term in ["Strategic", "Medium", "Tier 2"]):
        return badge(text, "#92400e", "#fef3c7", "#fde68a")
    if any(term in str(value) for term in ["Low", "Monitor", "Tier 3"]):
        return badge(text, "#166534", "#dcfce7", "#bbf7d0")
    return badge(text)


def signal_quality_badge(value):
    """Korean confidence badge."""
    text = str(value or "Emerging Signal")
    if "Institutional Grade" in text or "Strong Institutional" in text:
        return badge("기관급 검토", "#075985", "#e0f2fe", "#7dd3fc")
    if "High" in text or "Strong" in text:
        return badge("검토 신뢰도 높음", "#166534", "#dcfce7", "#bbf7d0")
    if "Weak" in text or "Noise" in text or "Low" in text:
        return badge("검토 신뢰도 낮음", "#7f1d1d", "#fee2e2", "#fecaca")
    return badge("초기 관찰", "#92400e", "#fef3c7", "#fde68a")


def risk_opportunity_badge(value):
    """Korean opportunity/risk badge."""
    text = str(value or "Signal")
    lowered = text.lower()
    if "opportunity" in lowered or "acquisition" in lowered or "jv" in lowered:
        return badge("투자 기회", "#166534", "#dcfce7", "#bbf7d0")
    if any(term in lowered for term in ["distress", "risk", "stress", "refinancing", "stalled"]):
        return badge("리스크 / 스트레스", "#7f1d1d", "#fee2e2", "#fecaca")
    if any(term in lowered for term in ["capital", "institutional", "flow"]):
        return badge("자본시장", "#075985", "#e0f2fe", "#bae6fd")
    return badge("시장 시그널")


def ko_executive_summary(row):
    """Generate a Korean executive summary from structured fields."""
    title = get_title(row)
    market = get_market(row)
    gp = get_gp(row)
    lender = get_lender(row)
    signal = get_signal_type(row)
    blob = text_blob(row)
    actor = " / ".join([name for name in [gp, lender] if name]) or "관련 기관"

    if any(term in blob for term in ["refinancing", "fannie", "freddie", "loan", "debt"]):
        return (
            f"{market} 멀티패밀리 자산에서 {actor} 관련 리파이낸싱 사례가 포착되었습니다. "
            "금리와 만기 부담이 지속되는 환경에서 유사 자산의 재융자 리스크와 recap 기회 여부를 함께 점검할 필요가 있습니다."
        )
    if any(term in blob for term in ["distress", "default", "stalled", "foreclosure"]):
        return (
            f"{market}에서 부실 / 스트레스 가능성이 있는 움직임이 관찰되었습니다. "
            "단순 뉴스가 아니라 매입 기회, 구조조정, JV gap 가능성으로 이어지는지 후속 확인이 필요합니다."
        )
    if any(term in blob for term in ["entitlement", "permit", "ceqa", "zoning", "planning"]):
        return (
            f"{market}에서 인허가 또는 개발 승인 관련 변화가 확인되었습니다. "
            "LA / California 사업 검토 시 승인 precedent, 허가 리스크, 착공 가능 시점을 함께 확인해야 합니다."
        )
    if any(term in blob for term in ["capital", "institutional", "partnership", "jv"]):
        return (
            f"{actor}의 자본시장 / 파트너십 관련 움직임이 관찰되었습니다. "
            "가격 발견, GP 협력 가능성, 기관투자자 자금 흐름을 판단하는 참고 시그널로 볼 수 있습니다."
        )
    if any(term in blob for term in ["construction", "delivery", "lease-up", "lifecycle"]):
        return (
            f"{market}에서 개발 단계 또는 실행 일정과 관련된 변화가 관찰되었습니다. "
            "착공, 준공, 리스업 타이밍이 언더라이팅과 시장 진입 시점에 미치는 영향을 점검해야 합니다."
        )
    return (
        f"{title} 항목은 {ko_signal_type(signal)} 관점에서 검토할 만한 시장 변화입니다. "
        "반복 관찰 여부와 관련 프로젝트 / GP 활동을 함께 확인하는 것이 좋습니다."
    )


def ko_woomi_angle(row):
    """Generate Korean Woomi implication."""
    blob = text_blob(row)
    if any(term in blob for term in ["refinancing", "loan", "debt", "fannie", "freddie"]):
        return "우미 관점에서는 재융자 압박, 대주단 태도, recap 또는 구조화 자본 투입 가능성을 함께 점검해야 합니다."
    if any(term in blob for term in ["entitlement", "permit", "ceqa", "zoning", "planning"]):
        return "우미 관점에서는 LA / California 인허가 precedent와 사업 일정 리스크를 추적하는 데 의미가 있습니다."
    if any(term in blob for term in ["distress", "stalled", "seller", "acquisition"]):
        return "우미 관점에서는 매입 기회, rescue capital, JV gap, 또는 할인된 basis 진입 가능성을 검토할 수 있습니다."
    if any(term in blob for term in ["jv", "partnership", "gp", "developer"]):
        return "우미 관점에서는 GP 역량, 파트너십 가능성, 현지 실행 파트너 후보군을 판단하는 데 참고할 수 있습니다."
    return "우미 관점에서는 반복 관찰 여부를 보면서 전략 모니터링 항목으로 관리하는 것이 적절합니다."


def ko_recommended_action(row):
    """Generate Korean recommended action."""
    blob = text_blob(row)
    if any(term in blob for term in ["refinancing", "maturity", "loan", "debt", "recap"]):
        return "재융자 일정, 대주단, 만기 구조, recap 가능성을 후속 확인하십시오."
    if any(term in blob for term in ["distress", "stalled", "default", "foreclosure"]):
        return "부실 매각, rescue capital, JV gap 가능성을 우선 모니터링하십시오."
    if any(term in blob for term in ["entitlement", "permit", "ceqa", "zoning", "planning"]):
        return "인허가 진행 단계와 LA / California 승인 precedent를 확인하십시오."
    if any(term in blob for term in ["jv", "partnership", "gp", "developer"]):
        return "관련 GP / 디벨로퍼의 파트너십 이력과 기관자본 연결성을 확인하십시오."
    return "다음 수집 결과에서 반복 포착되는지 확인하고, 필요 시 주간 전략회의 안건으로 올리십시오."


def ko_source_preview(row):
    """Korean source preview with raw English hidden unless expanded."""
    source = get_first(row, ["source", "source_report"], "")
    preview = get_first(row, ["article_text_sample", "summary", "why_it_matters", "evidence_signals"], "")
    url = get_url(row)
    with st.expander("원문 요약 / 출처", expanded=False):
        if source:
            st.caption(f"출처: {source}")
        if preview:
            st.markdown(f"**원문 식별용 텍스트:** {ko_sentence(truncate_text(preview, 520))}")
        if isinstance(url, str) and url.startswith("http"):
            st.markdown(f"[원문 기사 열기]({url})")


def ko_signal_card(row, shared, rank=None, expanded=False):
    """Korean-first signal card."""
    title = get_title(row)
    prefix = f"{rank}. " if rank else ""
    with st.expander(f"{prefix}{truncate_text(title, 92)} | 점수 {int(get_score(row))}", expanded=expanded):
        render_badges([
            score_badge(get_score(row)),
            priority_badge(get_priority(row)),
            risk_opportunity_badge(get_signal_type(row)),
            signal_quality_badge(confidence_label(row)),
        ])
        st.markdown(f"**중요성:** {ko_executive_summary(row)}")
        st.markdown(f"**우미 관점:** {ko_woomi_angle(row)}")
        st.markdown(f"**추천 후속 조치:** {ko_recommended_action(row)}")
        st.caption(
            f"시장: {get_market(row)} | 섹터: {ko_signal_type(get_sector(row))} | "
            f"GP / 디벨로퍼: {get_gp(row) or '미확인'} | 유형: {ko_signal_type(get_signal_type(row))}"
        )
        ko_source_preview(row)
        if is_detail_mode():
            with st.expander("상세 분석 / 원문 데이터", expanded=False):
                render_signal_detail(row, shared)


def ko_top_cards(cards, shared, title="오늘의 최우선 검토 사항", limit=5):
    """Korean top cards."""
    st.markdown(f"### {title}")
    if cards.empty:
        missing_file_message(FILES["dashboard_cards"])
        return
    for index, (_, row) in enumerate(sort_by_score(cards, ["card_score"]).head(limit).iterrows(), start=1):
        ko_signal_card(row.to_dict(), shared, rank=index, expanded=(index == 1))


def ko_signal_section(title, df, shared, score_columns, source_path, limit=3):
    """Korean-first signal section with raw data collapsed."""
    st.markdown(f"### {title}")
    if df.empty:
        missing_file_message(source_path)
        return
    for index, (_, row) in enumerate(sort_by_score(df, score_columns).head(limit).iterrows(), start=1):
        ko_signal_card(row.to_dict(), shared, rank=index, expanded=(index == 1))
    if is_detail_mode():
        render_expandable_table("상세 데이터", df, source_path)


def ko_read_this_first(shared):
    """Korean first-read panel."""
    summary = latest_summary(shared["summary"])
    focus = summary.get("recommended_executive_focus", "")
    if focus:
        focus_text = ko_sentence(focus)
    else:
        focus_text = "오늘은 최상위 기관급 검토 항목과 LA / California 관찰 사항을 먼저 확인하는 것이 좋습니다."
    st.markdown(
        f"""
        <div class="workstation-card">
            <div class="section-kicker">먼저 확인할 사항</div>
            <div class="signal-title">오늘의 최우선 검토 사항</div>
            <p>{focus_text}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def ko_action_bullets(cards):
    """Korean action checklist."""
    st.markdown("### 추천 후속 조치")
    if cards.empty:
        missing_file_message(FILES["dashboard_cards"])
        return
    actions = []
    for _, row in sort_by_score(cards, ["card_score"]).head(8).iterrows():
        action = ko_recommended_action(row.to_dict())
        if action and action not in actions:
            actions.append(action)
    for action in actions[:6]:
        st.markdown(f"- {action}")


def ko_hero_section(cards, shared):
    """Korean-first hero section."""
    cards = sort_by_score(cards, ["card_score"])
    if cards.empty:
        missing_file_message(FILES["dashboard_cards"])
        return
    row = cards.iloc[0].to_dict()
    st.markdown(
        f"""
        <div class="hero-card">
            <div class="section-kicker">오늘의 핵심 브리핑</div>
            <div class="signal-title">{get_title(row)}</div>
            {score_badge(get_score(row))}
            {risk_opportunity_badge(get_signal_type(row))}
            {signal_quality_badge(confidence_label(row))}
            <div class="small-divider"></div>
            <p><b>중요성</b><br>{ko_executive_summary(row)}</p>
            <p><b>우미 관점</b><br>{ko_woomi_angle(row)}</p>
            <p><b>추천 후속 조치</b><br>{ko_recommended_action(row)}</p>
            <p class="muted-label">시장: {get_market(row)} · 섹터: {ko_signal_type(get_sector(row))} · GP / 디벨로퍼: {get_gp(row) or "미확인"}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if is_detail_mode():
        with st.expander("상세 분석 보기", expanded=False):
            render_signal_detail(row, shared)


def page_executive_briefing(shared, filters):
    """Korean-first executive briefing page."""
    st.title("경영진 브리핑")
    st.caption("본 화면은 한국어 경영진 보고용으로 재구성한 요약입니다. 회사명, 시장명, 프로젝트명은 원문 식별을 위해 영어 표기를 유지합니다.")
    cards = apply_filters(shared["cards"], filters)
    st.markdown("### 먼저 확인할 사항")
    ko_read_this_first(shared)
    ko_hero_section(cards, shared)
    ko_action_bullets(cards)
    ko_top_cards(cards, shared, "오늘의 최우선 검토 사항")
    ko_signal_section("주요 기회 및 리스크", apply_filters(shared["opportunities"], filters), shared, ["opportunity_score"], FILES["opportunities"], limit=3)
    ko_signal_section("LA / California 관찰 사항", apply_filters(shared["la_assets"], filters), shared, ["la_asset_opportunity_score"], FILES["la_assets"], limit=3)
    ko_signal_section("GP 및 자본 파트너 동향", apply_filters(shared["gp_watchlist"], filters), shared, ["emerging_gp_score"], FILES["gp_watchlist"], limit=3)
    if is_detail_mode():
        market_mood(shared)
        render_expandable_table("상세 데이터", cards, FILES["dashboard_cards"])


def is_detail_mode():
    """Return True for Korean or English detail mode labels."""
    return st.session_state.get("view_mode", "경영진 모드") in ["Detail Mode", "상세 분석 모드"]


def legacy_main_03():
    """Run the Korean-localized executive strategy platform."""
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("경영진 전략 플랫폼")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드"], key="view_mode")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "Market Intelligence": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California Strategy": page_la_california_strategy,
        "GP & Capital Relationships": page_gp_capital_relationships,
        "System & Pipeline": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("Navigation", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"],
        shared["watchlists"],
        shared["high_confidence"],
        shared["opportunities"],
        shared["distress"],
        shared["la_assets"],
        shared["la_entitlement"],
        shared["la_lifecycle"],
        shared["la_persistent_assets"],
        shared["gp_watchlist"],
        shared["institutional_relationships"],
        shared["relationship_graph"],
        shared["historical_memory"],
        shared["persistent_asset_memory"],
        shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"Latest run: {summary.get('run_timestamp', 'No run data available')}")
    if is_detail_mode():
        kpi_strip(shared)
    else:
        cols = st.columns(3)
        with cols[0]:
            render_compact_metric("기관급 검토 항목", int(as_number(summary.get("high_confidence_signals", 0))))
        with cols[1]:
            render_compact_metric("주요 기회", int(as_number(summary.get("opportunity_count", 0))))
        with cols[2]:
            render_compact_metric("LA 관찰 항목", int(as_number(summary.get("la_asset_watch_count", 0))))
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | 경영진 전략 플랫폼 | Streamlit Cloud-ready | No paid APIs")


# ---------------------------------------------------------
# Investment intelligence platform overlay
# ---------------------------------------------------------

def classify_actionability(row):
    """Classify whether a signal is actionable using existing rule-based fields."""
    score = get_score(row)
    blob = text_blob(row)
    confidence = confidence_label(row)
    opportunity_score = as_number(get_first(row, ["opportunity_score", "la_asset_opportunity_score", "highest_opportunity_score"], 0))
    risk_score = as_number(get_first(row, ["risk_score", "distress_score", "highest_risk_score"], 0))
    observations = as_number(get_first(row, ["recurring_observation_count", "observation_count", "source_count"], 0))
    la_relevant = any(term in blob for term in ["los angeles", "california", "la ", "pasadena", "dtla", "koreatown"])
    stage = get_lifecycle_stage(row).lower()

    if score >= 85 and ("Institutional" in confidence or opportunity_score >= 80 or risk_score >= 60 or observations >= 5):
        return "즉시 검토"
    if la_relevant and score >= 75 and any(term in blob for term in ["entitlement", "permit", "ceqa", "zoning", "parcel", "asset"]):
        return "즉시 검토"
    if opportunity_score >= 65 or risk_score >= 55 or observations >= 3 or any(term in stage for term in ["refinancing", "construction", "entitlement"]):
        return "추가 확인 필요"
    if score >= 50 or "Emerging" in confidence:
        return "모니터링 지속"
    return "참고용"


def classify_investment_use_case(row):
    """Classify the investment use case for a signal."""
    blob = text_blob(row)
    if any(term in blob for term in ["jv", "partnership", "gp", "developer", "sponsor"]):
        return "GP 파트너십 검토"
    if any(term in blob for term in ["refinancing", "recap", "loan", "debt", "maturity", "fannie", "freddie"]):
        return "리파이낸싱 / Recap 기회"
    if any(term in blob for term in ["parcel", "asset", "site", "project", "development", "construction"]):
        return "개발 부지 / 프로젝트 검토"
    if any(term in blob for term in ["entitlement", "permit", "ceqa", "zoning", "planning"]):
        return "LA 인허가 모니터링"
    if any(term in blob for term in ["capital", "institutional", "fund", "lender", "financing"]):
        return "자본시장 동향 점검"
    if any(term in blob for term in ["distress", "stalled", "delayed", "default", "foreclosure"]):
        return "부실 / 지연 프로젝트 관찰"
    if any(term in blob for term in ["student", "senior", "btr", "sfr", "affordable", "office-to-residential"]):
        return "섹터 확장 검토"
    return "단순 모니터링"


def suggest_team_owner(row):
    """Suggest the likely Woomi team owner."""
    blob = text_blob(row)
    if any(term in blob for term in ["refinancing", "capital flow", "loan", "debt", "fannie", "freddie", "recap"]):
        return "재무 / 자금팀, 투자팀"
    if any(term in blob for term in ["los angeles", "california", "entitlement", "permit", "parcel", "ceqa", "zoning"]):
        return "미국 현지팀, 개발 / 인허가팀"
    if any(term in blob for term in ["gp", "jv", "partnership", "developer", "relationship"]):
        return "전략팀, 경영진"
    if any(term in blob for term in ["distress", "stalled", "default", "foreclosure", "acquisition"]):
        return "투자팀, 재무 / 자금팀"
    if any(term in blob for term in ["source", "pipeline", "health"]):
        return "전략팀"
    return "전략팀"


def classify_decision_status(row):
    """Display-only decision status; not persisted."""
    actionability = classify_actionability(row)
    if actionability == "즉시 검토":
        return "신규 검토"
    if actionability == "추가 확인 필요":
        return "후속 확인 중"
    if actionability == "모니터링 지속":
        return "모니터링"
    return "보류"


def actionability_badge(row):
    """Badge for investment actionability."""
    label = classify_actionability(row)
    if label == "즉시 검토":
        return badge(label, "#7f1d1d", "#fee2e2", "#fecaca")
    if label == "추가 확인 필요":
        return badge(label, "#92400e", "#fef3c7", "#fde68a")
    if label == "모니터링 지속":
        return badge(label, "#075985", "#e0f2fe", "#bae6fd")
    return badge(label, "#475569", "#f1f5f9", "#cbd5e1")


def use_case_badge(row):
    """Badge for investment use case."""
    return badge(classify_investment_use_case(row), "#334155", "#f8fafc", "#cbd5e1")


def risk_factors(row):
    """Generate concise risk factors."""
    blob = text_blob(row)
    risks = []
    if any(term in blob for term in ["refinancing", "loan", "debt", "maturity"]):
        risks.append("금리 / 만기 / 대출조건 변화")
    if any(term in blob for term in ["distress", "stalled", "default", "foreclosure"]):
        risks.append("부실화 또는 거래 구조 불확실성")
    if any(term in blob for term in ["entitlement", "permit", "ceqa", "zoning"]):
        risks.append("인허가 지연 및 규제 리스크")
    if any(term in blob for term in ["construction", "delivery", "lease-up"]):
        risks.append("착공, 준공, 리스업 실행 리스크")
    if not risks:
        risks.append("반복 관찰 부족 또는 정보 구체성 부족")
    return risks


def verification_materials(row):
    """Generate clean due-diligence follow-up items."""
    materials = ["원문 기사 및 출처 확인", "관련 프로젝트 / GP 반복 포착 여부 확인"]
    blob = text_blob(row)
    if any(term in blob for term in ["loan", "debt", "refinancing", "fannie", "freddie"]):
        materials.append("대출기관, 만기, 금액, DSCR/LTV 등 금융 조건 확인")
    if any(term in blob for term in ["entitlement", "permit", "ceqa", "zoning"]):
        materials.append("인허가 단계, 승인기관, 항소 / CEQA 리스크 확인")
    if any(term in blob for term in ["jv", "partnership", "gp", "developer"]):
        materials.append("GP / 파트너 이력과 기관자본 연결성 확인")
    if any(term in blob for term in ["asset", "parcel", "site", "project"]):
        materials.append("주소, 유닛 수, 사업 단계, 소유 / 스폰서 정보 확인")
    return list(dict.fromkeys(materials))[:5]


def investment_decision_frame(row):
    """Return structured investment decision fields."""
    return {
        "핵심 변화": ko_executive_summary(row),
        "투자적 의미": f"{classify_investment_use_case(row)} 관점에서 검토할 수 있으며, 의사결정 상태는 '{classify_decision_status(row)}'입니다.",
        "우미 관점": ko_woomi_angle(row),
        "실행 가능성": classify_actionability(row),
        "리스크 요인": ", ".join(risk_factors(row)),
        "추천 액션": ko_recommended_action(row),
        "확인 필요 자료": ", ".join(verification_materials(row)),
    }


def render_evidence_block(row):
    """Render clean evidence without dumping CSV rows."""
    st.markdown("#### 근거 자료")
    evidence = {
        "출처": get_first(row, ["source", "source_report"], "미확인"),
        "기사 / 항목명": get_first(row, ["source_article_title", "card_title", "canonical_project_name"], get_title(row)),
        "관련 프로젝트": get_first(row, ["canonical_project_name", "project_or_asset_name", "asset_or_project_name"], "미확인"),
        "관련 GP / 디벨로퍼": get_gp(row) or "미확인",
        "관련 시장": get_market(row),
        "점수": int(get_score(row)),
        "검토 신뢰도": confidence_label(row),
        "반복 관찰 수": get_first(row, ["recurring_observation_count", "observation_count", "source_count"], "미확인"),
        "개발 단계": get_lifecycle_stage(row) or "미확인",
        "출처 파일": get_first(row, ["source_report"], "dashboard / intelligence output"),
    }
    for key, value in evidence.items():
        st.markdown(f"- **{key}:** {value}")
    url = get_url(row)
    if isinstance(url, str) and url.startswith("http"):
        st.markdown(f"- **원문 URL:** [기사 열기]({url})")


def render_investment_decision_frame(row):
    """Render the investment decision framework for one signal."""
    frame = investment_decision_frame(row)
    st.markdown("#### 투자 판단 프레임")
    render_badges([
        actionability_badge(row),
        use_case_badge(row),
        badge(f"담당 제안: {suggest_team_owner(row)}", "#334155", "#f8fafc", "#cbd5e1"),
        badge(f"상태: {classify_decision_status(row)}", "#334155", "#f8fafc", "#cbd5e1"),
    ])
    for key, value in frame.items():
        st.markdown(f"**{key}:** {value}")


def render_so_what(row):
    """Render concise Korean So What block."""
    st.markdown("### So What / 우미 시사점")
    st.markdown(
        f"""
{ko_woomi_angle(row)}

**영향받는 의사결정:** {classify_investment_use_case(row)}  
**검토 담당:** {suggest_team_owner(row)}  
**다음 확인 사항:** {", ".join(verification_materials(row)[:3])}
"""
    )


def ko_signal_card(row, shared, rank=None, expanded=False):
    """Investment-focused Korean signal card."""
    title = get_title(row)
    prefix = f"{rank}. " if rank else ""
    with st.expander(f"{prefix}{truncate_text(title, 92)} | 점수 {int(get_score(row))}", expanded=expanded):
        render_badges([
            score_badge(get_score(row)),
            actionability_badge(row),
            use_case_badge(row),
            signal_quality_badge(confidence_label(row)),
        ])
        st.markdown(f"**중요성:** {ko_executive_summary(row)}")
        st.markdown(f"**우미 관점:** {ko_woomi_angle(row)}")
        st.markdown(f"**추천 후속 조치:** {ko_recommended_action(row)}")
        st.caption(
            f"시장: {get_market(row)} | 섹터: {ko_signal_type(get_sector(row))} | "
            f"GP / 디벨로퍼: {get_gp(row) or '미확인'} | 담당: {suggest_team_owner(row)}"
        )
        render_investment_decision_frame(row)
        render_evidence_block(row)
        ko_source_preview(row)
        if is_detail_mode():
            with st.expander("상세 분석 / 관련 정보", expanded=False):
                render_signal_detail(row, shared)


def render_investment_framework_for_top(cards):
    """Render framework for top signal and priority items."""
    st.markdown("### 투자 판단 프레임")
    if cards.empty:
        missing_file_message(FILES["dashboard_cards"])
        return
    top_rows = sort_by_score(cards, ["card_score"]).head(5)
    for index, (_, row) in enumerate(top_rows.iterrows(), start=1):
        item = row.to_dict()
        with st.expander(f"{index}. {truncate_text(get_title(item), 90)} | {classify_actionability(item)}", expanded=(index == 1)):
            render_investment_decision_frame(item)


def ic_memo_block(row, index):
    """Memo-style block for investment committee prep."""
    st.markdown(f"### 안건 {index}: {get_title(row)}")
    st.markdown(f"**배경:** {ko_executive_summary(row)}")
    st.markdown(f"**핵심 관찰사항:** {ko_signal_type(get_signal_type(row))} / {get_market(row)} / 점수 {int(get_score(row))}")
    st.markdown(f"**투자적 의미:** {investment_decision_frame(row)['투자적 의미']}")
    st.markdown(f"**우미 관점 검토 포인트:** {ko_woomi_angle(row)}")
    st.markdown(f"**리스크:** {', '.join(risk_factors(row))}")
    st.markdown(f"**추가 확인 필요사항:** {', '.join(verification_materials(row))}")
    st.markdown(f"**추천 액션:** {ko_recommended_action(row)}")
    st.markdown(f"**담당 제안:** {suggest_team_owner(row)}")


def page_investment_committee_prep(shared, filters):
    """Investment Committee prep view."""
    st.title("Investment Committee Prep / 투자검토 메모")
    st.caption("상위 투자 관련 항목 3개를 IC 사전검토용 메모 형식으로 정리합니다.")
    candidates = pd.concat(
        [
            apply_filters(shared["opportunities"], filters),
            apply_filters(shared["high_confidence"], filters),
            apply_filters(shared["la_assets"], filters),
        ],
        ignore_index=True,
        sort=False,
    )
    if candidates.empty:
        missing_file_message(FILES["opportunities"])
        return
    for index, (_, row) in enumerate(sort_by_score(candidates).head(3).iterrows(), start=1):
        ic_memo_block(row.to_dict(), index)
        st.divider()


def page_executive_briefing(shared, filters):
    """Investment-intelligence Korean executive briefing page."""
    st.title("경영진 브리핑")
    st.caption("본 화면은 한국어 경영진 보고용으로 재구성한 요약입니다. 회사명, 시장명, 프로젝트명은 원문 식별을 위해 영어 표기를 유지합니다.")
    cards = apply_filters(shared["cards"], filters)
    top = sort_by_score(cards, ["card_score"]).head(1)
    top_row = top.iloc[0].to_dict() if not top.empty else {}

    st.markdown("### 오늘의 최우선 검토 사항")
    ko_hero_section(cards, shared)
    if top_row:
        render_so_what(top_row)
    render_investment_framework_for_top(cards)
    ko_action_bullets(cards)

    st.markdown("### Investment Committee Prep preview")
    if not cards.empty:
        for index, (_, row) in enumerate(sort_by_score(cards, ["card_score"]).head(3).iterrows(), start=1):
            with st.expander(f"IC 메모 미리보기 {index}: {truncate_text(get_title(row.to_dict()), 80)}", expanded=(index == 1)):
                ic_memo_block(row.to_dict(), index)

    ko_signal_section("주요 기회 및 리스크", apply_filters(shared["opportunities"], filters), shared, ["opportunity_score"], FILES["opportunities"], limit=3)
    ko_signal_section("LA / California 관찰 사항", apply_filters(shared["la_assets"], filters), shared, ["la_asset_opportunity_score"], FILES["la_assets"], limit=3)
    ko_signal_section("GP 및 자본 파트너 동향", apply_filters(shared["gp_watchlist"], filters), shared, ["emerging_gp_score"], FILES["gp_watchlist"], limit=3)
    if is_detail_mode():
        render_expandable_table("상세 데이터", cards, FILES["dashboard_cards"])


def legacy_main_04():
    """Run the investment intelligence platform."""
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("투자 인텔리전스 플랫폼")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드"], key="view_mode")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "투자검토 메모": page_investment_committee_prep,
        "Market Intelligence": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California Strategy": page_la_california_strategy,
        "GP & Capital Relationships": page_gp_capital_relationships,
        "System & Pipeline": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("Navigation", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"],
        shared["watchlists"],
        shared["high_confidence"],
        shared["opportunities"],
        shared["distress"],
        shared["la_assets"],
        shared["la_entitlement"],
        shared["la_lifecycle"],
        shared["la_persistent_assets"],
        shared["gp_watchlist"],
        shared["institutional_relationships"],
        shared["relationship_graph"],
        shared["historical_memory"],
        shared["persistent_asset_memory"],
        shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"Latest run: {summary.get('run_timestamp', 'No run data available')}")
    if is_detail_mode():
        kpi_strip(shared)
    else:
        cols = st.columns(3)
        with cols[0]:
            render_compact_metric("기관급 검토 항목", int(as_number(summary.get("high_confidence_signals", 0))))
        with cols[1]:
            render_compact_metric("주요 기회", int(as_number(summary.get("opportunity_count", 0))))
        with cols[2]:
            render_compact_metric("LA 관찰 항목", int(as_number(summary.get("la_asset_watch_count", 0))))
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | Real investment intelligence platform | Streamlit Cloud-ready | No paid APIs")


# ---------------------------------------------------------------------------
# Real Investment Intelligence Platform overlay
# ---------------------------------------------------------------------------

def recurring_observation_count(row):
    """Return a lightweight recurring-observation count from any known field."""
    for field in [
        "recurring_observation_count",
        "observation_count",
        "repeat_interaction_count",
        "source_count",
        "supporting_source_count",
        "article_count",
        "duplicate_count",
    ]:
        value = as_number(get_first(row, [field], 0), 0)
        if value:
            return int(value)
    return 0


def row_has_la_california_relevance(row):
    text = text_blob(row).lower()
    return any(term in text for term in [
        "los angeles", " l.a.", " la ", "california", "southern california",
        "koreatown", "dtla", "hollywood", "pasadena", "orange county",
        "inland empire", "wilshire", "long beach",
    ])


def investment_priority_score(row):
    """Create one comparable score across mixed dashboard/watchlist rows."""
    score = get_score(row)
    text = text_blob(row).lower()
    quality = get_first(row, [
        "signal_quality_label",
        "institutional_confidence_label",
        "confidence_level",
        "card_priority",
        "priority_label",
    ]).lower()
    if "institutional" in quality or "기관" in quality:
        score += 12
    if "high" in quality or "높" in quality:
        score += 8
    if "critical" in quality or "즉시" in quality:
        score += 10
    if row_has_la_california_relevance(row):
        score += 8
    if any(term in text for term in ["refinanc", "recap", "maturity", "debt", "fannie mae", "freddie mac"]):
        score += 6
    if any(term in text for term in ["joint venture", " jv ", "partnership", "capital partner"]):
        score += 6
    if any(term in text for term in ["distress", "stalled", "foreclosure", "default", "delayed"]):
        score += 6
    if recurring_observation_count(row) >= 2:
        score += 6
    return max(0, min(100, score))


def classify_actionability(row):
    """Classify whether a signal is ready for review or should stay monitored."""
    score = investment_priority_score(row)
    text = text_blob(row).lower()
    confidence = get_first(row, [
        "signal_quality_label",
        "institutional_confidence_label",
        "confidence_level",
        "card_priority",
        "priority_label",
    ]).lower()
    stage = get_lifecycle_stage(row).lower()
    strong_quality = any(term in confidence for term in ["institutional", "high", "strong", "critical", "기관", "높", "즉시"])
    actionable_terms = ["opportunity", "distress", "refinanc", "recap", "maturity", "entitlement", "permit", "approved", "construction ready", "jv", "partnership"]
    if score >= 78 and (strong_quality or row_has_la_california_relevance(row) or recurring_observation_count(row) >= 2):
        return "즉시 검토"
    if score >= 58 or any(term in text for term in actionable_terms) or any(term in stage for term in ["approved", "permit", "construction", "stalled"]):
        return "추가 확인 필요"
    if score >= 35:
        return "모니터링 지속"
    return "참고용"


def classify_investment_use_case(row):
    """Map a row to the investment decision it most likely supports."""
    text = text_blob(row).lower()
    if any(term in text for term in ["refinanc", "recap", "maturity", "bridge loan", "fannie mae", "freddie mac", "debt"]):
        return "리파이낸싱 / Recap 기회"
    if any(term in text for term in ["jv", "joint venture", "partnership", "capital partner", "relationship"]):
        return "GP 파트너십 검토"
    if any(term in text for term in ["distress", "stalled", "foreclosure", "default", "receivership", "delayed"]):
        return "부실 / 지연 프로젝트 관찰"
    if any(term in text for term in ["entitlement", "permit", "zoning", "ceqa", "density bonus", "toc", "builder"]):
        return "LA 인허가 모니터링" if row_has_la_california_relevance(row) else "개발 부지 / 프로젝트 검토"
    if any(term in text for term in ["site", "parcel", "asset", "development", "construction", "delivery", "lease-up", "project"]):
        return "개발 부지 / 프로젝트 검토"
    if any(term in text for term in ["capital", "institutional", "blackstone", "brookfield", "kennedy wilson", "greystar"]):
        return "자본시장 동향 점검"
    if any(term in text for term in ["student housing", "senior housing", "btr", "single-family rental", "office-to-residential", "affordable"]):
        return "섹터 확장 검토"
    return "단순 모니터링"


def suggest_team_owner(row):
    """Suggest the internal owner most likely to use this signal."""
    use_case = classify_investment_use_case(row)
    text = text_blob(row).lower()
    if use_case == "리파이낸싱 / Recap 기회":
        return "재무 / 자금팀, 투자팀"
    if use_case == "LA 인허가 모니터링":
        return "미국 현지팀, 개발 / 인허가팀"
    if use_case == "GP 파트너십 검토":
        return "전략팀, 경영진"
    if use_case == "부실 / 지연 프로젝트 관찰":
        return "투자팀, 재무 / 자금팀"
    if use_case == "개발 부지 / 프로젝트 검토":
        return "투자팀, 미국 현지팀"
    if "source" in text or "pipeline" in text:
        return "전략팀"
    return "전략팀"


def classify_decision_status(row):
    actionability = classify_actionability(row)
    if actionability == "즉시 검토":
        return "신규 검토"
    if actionability == "추가 확인 필요":
        return "후속 확인 중"
    if actionability == "모니터링 지속":
        return "모니터링"
    return "보류"


def actionability_badge(row):
    label = classify_actionability(row)
    colors = {
        "즉시 검토": ("#7f1d1d", "#fee2e2", "#fecaca"),
        "추가 확인 필요": ("#92400e", "#fef3c7", "#fde68a"),
        "모니터링 지속": ("#166534", "#dcfce7", "#bbf7d0"),
        "참고용": ("#475569", "#f1f5f9", "#cbd5e1"),
    }
    color, background, border = colors.get(label, ("#334155", "#f1f5f9", "#cbd5e1"))
    return badge(label, color=color, background=background, border=border)


def investment_use_case_badge(row):
    return badge(classify_investment_use_case(row), color="#1e3a8a", background="#dbeafe", border="#bfdbfe")


def owner_badge(row):
    return badge(f"담당: {suggest_team_owner(row)}", color="#3f3f46", background="#f4f4f5", border="#d4d4d8")


def decision_status_badge(row):
    return badge(classify_decision_status(row), color="#064e3b", background="#ecfdf5", border="#a7f3d0")


def investment_meaning(row):
    use_case = classify_investment_use_case(row)
    market = get_market(row)
    gp = get_gp(row)
    if use_case == "리파이낸싱 / Recap 기회":
        return f"{market} 관련 자금조달·만기 구조가 투자 조건과 recap 가능성에 영향을 줄 수 있습니다."
    if use_case == "GP 파트너십 검토":
        return f"{gp or '관련 GP'}의 움직임은 향후 JV, 개발 파트너십, 경쟁 포지션 판단에 참고할 수 있습니다."
    if use_case == "개발 부지 / 프로젝트 검토":
        return f"{market} 프로젝트의 단계 변화는 부지, 착공, 매입 또는 개발 타이밍 판단에 연결될 수 있습니다."
    if use_case == "LA 인허가 모니터링":
        return "LA / California 인허가 신호는 현지 개발전략, density bonus, CEQA, permitting timeline의 비교사례가 될 수 있습니다."
    if use_case == "자본시장 동향 점검":
        return "기관 자본의 움직임은 가격 발견, 매입 경쟁, GP 파트너십 가능성 판단에 활용할 수 있습니다."
    if use_case == "부실 / 지연 프로젝트 관찰":
        return "부실·지연 신호는 할인 매입, rescue capital, JV gap 검토 가능성을 만들 수 있습니다."
    if use_case == "섹터 확장 검토":
        return "비멀티패밀리 주거 섹터 신호는 Woomi의 미국 주거 개발 역량 확장 후보를 보여줍니다."
    return "현재는 방향성 확인용 신호로, 반복 관찰 여부를 지켜볼 필요가 있습니다."


def risk_factors(row):
    text = text_blob(row).lower()
    risks = []
    if any(term in text for term in ["refinanc", "maturity", "floating", "debt", "loan"]):
        risks.append("금리, 만기, 대출 조건 변화")
    if any(term in text for term in ["distress", "stalled", "delayed", "default", "foreclosure"]):
        risks.append("스폰서 유동성 또는 프로젝트 지연")
    if any(term in text for term in ["ceqa", "zoning", "entitlement", "permit", "appeal"]):
        risks.append("인허가, CEQA, zoning 관련 불확실성")
    if any(term in text for term in ["supply", "lease-up", "vacancy", "concession"]):
        risks.append("공급, 리스업, 공실 및 concession 압력")
    if not risks:
        risks.append("추가 자료 부족으로 인한 해석 리스크")
    return risks


def verification_materials(row):
    materials = []
    for label, fields in [
        ("원문 기사", ["source_article_title", "article_title", "title", "card_title", "item_name"]),
        ("관련 프로젝트", ["canonical_project_name", "project_or_deal_name", "related_project_or_deal", "canonical_asset_or_project_name"]),
        ("관련 GP / 개발사", ["canonical_gp_name", "gp_or_developer", "gp_name"]),
        ("관련 시장", ["market", "top_market", "city_or_submarket", "la_submarket"]),
        ("개발 단계", ["latest_lifecycle_stage", "current_lifecycle_stage", "lifecycle_stage", "status_or_stage"]),
        ("신뢰도", ["signal_quality_label", "institutional_confidence_label", "confidence_level"]),
    ]:
        value = get_first(row, fields)
        if value:
            materials.append(f"{label}: {value}")
    url = get_first(row, ["url", "source_url_if_available"])
    if url:
        materials.append(f"링크: {url}")
    return materials[:8]


def so_what_summary(row):
    use_case = classify_investment_use_case(row)
    owner = suggest_team_owner(row)
    action = ko_recommended_action(row)
    if use_case == "리파이낸싱 / Recap 기회":
        return f"자금조달 환경 변화로 인해 JV 또는 recap 기회가 발생할 수 있습니다. {owner}이 관련 GP, 대출기관, 만기 구조, 담보 자산의 가격 민감도를 우선 확인하는 것이 좋습니다."
    if use_case == "LA 인허가 모니터링":
        return f"LA / California 인허가 신호는 현지 개발전략 수립 시 비교사례로 활용될 수 있습니다. {owner}이 승인 단계, CEQA 리스크, density bonus 적용 여부를 확인해야 합니다."
    if use_case == "GP 파트너십 검토":
        return f"GP 또는 기관 자본의 반복 움직임은 파트너십 후보와 경쟁 구도를 보여줄 수 있습니다. {owner}이 관계 이력과 최근 거래 맥락을 확인할 필요가 있습니다."
    if use_case == "부실 / 지연 프로젝트 관찰":
        return f"부실 또는 지연 신호는 rescue capital, 할인 매입, JV gap 가능성을 만들 수 있습니다. {owner}이 실제 스트레스 원인과 권리관계를 확인해야 합니다."
    return f"이 항목은 Woomi의 전략 모니터링 후보입니다. {owner}이 추가 자료를 확인하고, 현재는 '{action}' 관점으로 관리하는 것이 적절합니다."


def render_evidence_block(row):
    st.markdown("#### 근거 자료")
    bullets = verification_materials(row)
    if not bullets:
        bullets = ["구조화된 근거가 제한적입니다. 원문과 관련 CSV를 추가 확인하세요."]
    for item in bullets:
        if item.startswith("링크: http"):
            url = item.replace("링크: ", "", 1)
            st.markdown(f"- [원문 링크]({url})")
        else:
            st.markdown(f"- {item}")
    score = investment_priority_score(row)
    st.markdown(f"- 투자 판단 점수: {int(score)}")
    count = recurring_observation_count(row)
    if count:
        st.markdown(f"- 반복 관찰: {count}회")
    source_layer = get_first(row, ["_source_layer", "source_report", "source_report_file"])
    if source_layer:
        st.markdown(f"- 참조 레이어: {source_layer}")


def render_investment_decision_item(row, index=None, expanded=False):
    title = get_title(row) or "검토 항목"
    heading = f"{index}. {truncate_text(title, 88)}" if index else truncate_text(title, 88)
    with st.expander(heading, expanded=expanded):
        render_badges([
            score_badge(investment_priority_score(row)),
            actionability_badge(row),
            investment_use_case_badge(row),
            owner_badge(row),
            decision_status_badge(row),
            signal_quality_badge(confidence_label(row)),
        ])
        st.markdown("**핵심 변화**")
        st.write(ko_executive_summary(row))
        st.markdown("**투자적 의미**")
        st.write(investment_meaning(row))
        st.markdown("**우미 관점**")
        st.write(ko_woomi_angle(row))
        st.markdown("**실행 가능성**")
        st.write(classify_actionability(row))
        st.markdown("**리스크 요인**")
        for risk in risk_factors(row):
            st.markdown(f"- {risk}")
        st.markdown("**추천 액션**")
        st.write(ko_recommended_action(row))
        st.markdown("**확인 필요 자료**")
        for item in verification_materials(row)[:5]:
            if item.startswith("링크: http"):
                continue
            st.markdown(f"- {item}")
        render_evidence_block(row)
        if is_detail_mode():
            render_signal_detail(row, current_shared_data())


def candidate_priority_rows(shared, filters=None, limit=8):
    """Collect mixed rows into one investment-priority queue."""
    filters = filters or {}
    candidates = []
    for key, source_name in [
        ("cards", "dashboard_cards.csv"),
        ("high_confidence", "high_confidence_watchlist.csv"),
        ("opportunities", "opportunity_radar.csv"),
        ("distress", "distress_watchlist.csv"),
        ("la_assets", "la_asset_watch.csv"),
        ("gp_watchlist", "gp_watchlist.csv"),
    ]:
        df = apply_filters(shared.get(key, pd.DataFrame()), filters)
        if df.empty:
            continue
        temp = df.copy()
        temp["_source_layer"] = source_name
        candidates.append(temp)
    if not candidates:
        return pd.DataFrame()
    combined = pd.concat(candidates, ignore_index=True, sort=False)
    combined["_platform_priority_score"] = combined.apply(lambda row: investment_priority_score(row.to_dict()), axis=1)
    return combined.sort_values("_platform_priority_score", ascending=False).head(limit)


def render_so_what_block(row):
    st.markdown("### So What / 우미 시사점")
    st.markdown(
        f"""
        <div class="soft-card">
          <div class="muted">투자 판단 관점</div>
          <div style="font-size:1.02rem; line-height:1.65; margin-top:.35rem;">{so_what_summary(row)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_investment_decision_framework(rows, shared=None, title="투자 판단 프레임"):
    st.markdown(f"### {title}")
    if rows is None or rows.empty:
        st.info("현재 투자 판단 프레임에 넣을 우선순위 항목이 없습니다.")
        return
    for index, (_, row) in enumerate(rows.head(5).iterrows(), start=1):
        render_investment_decision_item(row.to_dict(), index=index, expanded=(index == 1))


def render_ic_memo_item(row, index):
    title = get_title(row) or f"투자검토 안건 {index}"
    st.markdown(f"#### 안건 {index}: {truncate_text(title, 90)}")
    render_badges([
        score_badge(investment_priority_score(row)),
        actionability_badge(row),
        investment_use_case_badge(row),
        owner_badge(row),
        decision_status_badge(row),
    ])
    fields = [
        ("배경", ko_executive_summary(row)),
        ("핵심 관찰사항", f"{get_market(row)} / {get_gp(row) or '관련 GP 미확인'} / {classify_investment_use_case(row)}"),
        ("투자적 의미", investment_meaning(row)),
        ("우미 관점 검토 포인트", ko_woomi_angle(row)),
        ("리스크", "; ".join(risk_factors(row))),
        ("추가 확인 필요사항", "; ".join(item for item in verification_materials(row)[:4] if not item.startswith("링크:")) or "원문 및 관련 출력 파일 확인"),
        ("추천 액션", ko_recommended_action(row)),
    ]
    for label, value in fields:
        st.markdown(f"**{label}**")
        st.write(value)
    st.divider()


def ko_signal_card(row, shared, rank=None, expanded=False):
    """Korean-first expandable signal card with investment context."""
    title = get_title(row) or "검토 항목"
    summary = ko_executive_summary(row)
    market = get_market(row)
    sector = get_sector(row)
    gp = get_gp(row)
    score = investment_priority_score(row)
    header = f"{rank}. {truncate_text(title, 88)}" if rank else truncate_text(title, 88)
    with st.expander(header, expanded=expanded):
        render_badges([
            score_badge(score),
            actionability_badge(row),
            investment_use_case_badge(row),
            risk_opportunity_badge(get_signal_type(row)),
            signal_quality_badge(confidence_label(row)),
            owner_badge(row),
            decision_status_badge(row),
        ])
        st.markdown(f"**시장 / 섹터:** {market or '미확인'} · {sector or '미확인'}")
        if gp:
            st.markdown(f"**GP / 개발사:** {gp}")
        st.markdown("**핵심 변화**")
        st.write(summary)
        st.markdown("**중요성**")
        st.write(investment_meaning(row))
        st.markdown("**우미 관점**")
        st.write(ko_woomi_angle(row))
        st.markdown("**추천 후속 조치**")
        st.write(ko_recommended_action(row))
        render_evidence_block(row)
        if is_detail_mode():
            st.markdown("#### 과거 관찰 이력")
            render_signal_history(row, shared)
            st.markdown("#### 관련 시그널")
            render_related_signals(row, shared)
            render_related_projects(row, shared)
            render_related_gp_activity(row, shared)
            with st.expander("원문 요약 / 상세 필드", expanded=False):
                render_signal_detail(row, shared)


def ko_hero_section(cards, shared):
    st.markdown("### 오늘의 최우선 검토 사항")
    if cards.empty:
        missing_file_message(FILES["dashboard_cards"])
        return None
    row = sort_by_score(cards, ["card_score"]).iloc[0].to_dict()
    st.markdown(
        f"""
        <div class="hero-card">
          <div class="muted">오늘의 핵심 시그널</div>
          <h2>{truncate_text(get_title(row), 110)}</h2>
          <p>{ko_executive_summary(row)}</p>
          <div style="margin-top:.8rem;">{score_badge(investment_priority_score(row))} {actionability_badge(row)} {investment_use_case_badge(row)}</div>
          <p><strong>시장:</strong> {get_market(row) or '미확인'} · <strong>GP / 개발사:</strong> {get_gp(row) or '미확인'}</p>
          <p><strong>추천 액션:</strong> {ko_recommended_action(row)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_so_what_block(row)
    return row


def render_ic_prep_preview(priority_rows):
    st.markdown("### Investment Committee Prep preview / 투자검토 메모 미리보기")
    if priority_rows.empty:
        st.info("투자검토 메모 후보가 없습니다.")
        return
    for index, (_, row) in enumerate(priority_rows.head(3).iterrows(), start=1):
        with st.expander(f"투자검토 메모 {index}: {truncate_text(get_title(row.to_dict()), 80)}", expanded=(index == 1)):
            render_ic_memo_item(row.to_dict(), index)


def page_investment_committee_prep(shared, filters):
    st.subheader("Investment Committee Prep / 투자검토 메모")
    st.caption("상위 투자 관련 항목을 투자위원회 사전 검토 형식으로 정리합니다.")
    priority_rows = candidate_priority_rows(shared, filters, limit=5)
    if priority_rows.empty:
        st.info("현재 투자검토 메모를 만들 우선순위 항목이 없습니다.")
        return
    for index, (_, row) in enumerate(priority_rows.head(3).iterrows(), start=1):
        render_ic_memo_item(row.to_dict(), index)
    if is_detail_mode():
        render_expandable_table("상세 후보 데이터", priority_rows, FILES["dashboard_cards"])


def page_executive_briefing(shared, filters):
    """Korean-first executive briefing with investment decision framing."""
    st.subheader("경영진 브리핑")
    st.caption("본 화면은 한국어 경영진 보고용으로 재구성한 요약입니다. 회사명, 시장명, 프로젝트명은 원문 식별을 위해 영어 표기를 유지합니다.")

    cards = apply_filters(shared["cards"], filters)
    priority_rows = candidate_priority_rows(shared, filters, limit=8)

    top_row = ko_hero_section(cards, shared)

    st.markdown("### 투자 판단 프레임")
    if priority_rows.empty and top_row:
        priority_rows = pd.DataFrame([top_row])
    render_investment_decision_framework(priority_rows, shared)

    st.markdown("### 오늘 체크할 액션")
    action_source = priority_rows if not priority_rows.empty else cards
    ko_action_bullets(action_source)

    render_ic_prep_preview(priority_rows)

    st.markdown("### 주요 기회 및 리스크")
    ko_signal_section("투자 기회", apply_filters(shared["opportunities"], filters), shared, ["opportunity_score"], FILES["opportunities"], limit=3)
    ko_signal_section("리스크 모니터링", apply_filters(shared["distress"], filters), shared, ["distress_score"], FILES["distress"], limit=3)

    st.markdown("### LA / California 관찰 사항")
    ko_signal_section("LA 자산 / 프로젝트 모니터링", apply_filters(shared["la_assets"], filters), shared, ["la_asset_opportunity_score"], FILES["la_assets"], limit=3)

    st.markdown("### GP 및 자본 파트너 동향")
    ko_signal_section("GP 모니터링", apply_filters(shared["gp_watchlist"], filters), shared, ["emerging_gp_score"], FILES["gp_watchlist"], limit=3)

    if is_detail_mode():
        render_expandable_table("상세 데이터", priority_rows if not priority_rows.empty else cards, FILES["dashboard_cards"])


def legacy_main_05():
    """Run the final investment intelligence platform experience."""
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("투자 인텔리전스 플랫폼")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드"], key="view_mode")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "투자검토 메모": page_investment_committee_prep,
        "Market Intelligence": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California Strategy": page_la_california_strategy,
        "GP & Capital Relationships": page_gp_capital_relationships,
        "System & Pipeline": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("Navigation", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"],
        shared["watchlists"],
        shared["high_confidence"],
        shared["opportunities"],
        shared["distress"],
        shared["la_assets"],
        shared["la_entitlement"],
        shared["la_lifecycle"],
        shared["la_persistent_assets"],
        shared["gp_watchlist"],
        shared["institutional_relationships"],
        shared["relationship_graph"],
        shared["historical_memory"],
        shared["persistent_asset_memory"],
        shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"Latest run: {summary.get('run_timestamp', 'No run data available')}")
    if is_detail_mode():
        kpi_strip(shared)
    else:
        cols = st.columns(3)
        with cols[0]:
            render_compact_metric("기관급 검토 항목", int(as_number(summary.get("high_confidence_signals", 0))))
        with cols[1]:
            render_compact_metric("주요 기회", int(as_number(summary.get("opportunity_count", 0))))
        with cols[2]:
            render_compact_metric("LA 관찰 항목", int(as_number(summary.get("la_asset_watch_count", 0))))
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | Real investment intelligence platform | Streamlit Cloud-ready | No paid APIs")


def show_global_filters(dataframes):
    """Korean-first sidebar filters with English internal focus keys."""
    if "quick_focus" not in st.session_state:
        st.session_state["quick_focus"] = "All"

    st.sidebar.markdown("### 오늘의 집중 검토")
    focus_buttons = [
        ("주요 투자 기회", "Top Opportunities"),
        ("리파이낸싱 압박", "Refinancing Stress"),
        ("LA Watch", "LA Watch"),
        ("GP 모니터링", "GP Watchlist"),
        ("기관급 검토", "High Confidence"),
        ("리스크 신호", "Distress Signals"),
    ]
    for label, focus_key in focus_buttons:
        st.sidebar.button(label, on_click=set_quick_focus, args=(focus_key,), use_container_width=True)
    if st.sidebar.button("필터 초기화", use_container_width=True):
        st.session_state["quick_focus"] = "All"

    filters = {"quick_focus": st.session_state["quick_focus"]}
    filter_labels = {
        "market": "시장",
        "residential_sector": "주거 섹터",
        "gp_or_developer": "GP / 개발사",
        "lender": "대주 / 금융기관",
        "lifecycle_stage": "개발 단계",
        "confidence": "신뢰도",
        "signal_quality": "시그널 품질",
        "priority": "우선순위",
    }
    with st.sidebar.expander("상세 필터", expanded=False):
        for key, columns in FILTER_FIELD_MAP.items():
            options = collect_options(dataframes, columns)
            if options:
                selected = st.multiselect(filter_labels.get(key, key.replace("_", " ")), options)
                if selected:
                    filters[key] = selected
        filters["opportunity_risk"] = st.selectbox("기회 / 리스크", ["All", "Opportunity", "Risk / Stress", "Capital Flow"])
        filters["california_only"] = st.checkbox("California만 보기")
        filters["la_only"] = st.checkbox("LA만 보기")
    return filters


def app_header(shared):
    """Korean-first professional app header."""
    summary = latest_summary(shared["summary"])
    st.markdown(
        """
        <div class="workstation-card">
            <div class="section-kicker">US Residential Intelligence</div>
            <div class="signal-title">미국 주거 투자 인텔리전스 워크스테이션</div>
            <p class="muted-label">CSV / Markdown 기반 · 로컬 및 Streamlit Cloud 지원 · 유료 API 없음</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns(3)
    with cols[0]:
        render_compact_metric("최근 실행", summary.get("run_timestamp", "실행 데이터 없음"))
    with cols[1]:
        render_compact_metric("파이프라인 상태", health_status(shared["health"]))
    with cols[2]:
        render_compact_metric("출력 파일", f"{int(output_file_status()['available'].sum())}/{len(FILES)}")


def legacy_main_06():
    """Run the Korean-first investment intelligence platform experience."""
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("투자 인텔리전스 플랫폼")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드"], key="view_mode")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "투자검토 메모": page_investment_committee_prep,
        "시장 인텔리전스": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California 전략": page_la_california_strategy,
        "GP / 자본 관계": page_gp_capital_relationships,
        "시스템 / 파이프라인": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"],
        shared["watchlists"],
        shared["high_confidence"],
        shared["opportunities"],
        shared["distress"],
        shared["la_assets"],
        shared["la_entitlement"],
        shared["la_lifecycle"],
        shared["la_persistent_assets"],
        shared["gp_watchlist"],
        shared["institutional_relationships"],
        shared["relationship_graph"],
        shared["historical_memory"],
        shared["persistent_asset_memory"],
        shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"최근 실행: {summary.get('run_timestamp', '실행 데이터 없음')}")
    if is_detail_mode():
        kpi_strip(shared)
    else:
        cols = st.columns(3)
        with cols[0]:
            render_compact_metric("기관급 검토 항목", int(as_number(summary.get("high_confidence_signals", 0))))
        with cols[1]:
            render_compact_metric("주요 기회", int(as_number(summary.get("opportunity_count", 0))))
        with cols[2]:
            render_compact_metric("LA 관찰 항목", int(as_number(summary.get("la_asset_watch_count", 0))))
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | 투자 인텔리전스 플랫폼 | Streamlit Cloud-ready | No paid APIs")


# ---------------------------------------------------------------------------
# Regime Intelligence and Cross-Signal Reasoning overlay
# ---------------------------------------------------------------------------

def current_shared_data():
    """Return the loaded shared data for expandable detail views."""
    return st.session_state.get("shared_data", load_shared_data())


def source_frames_for_reasoning(shared, filters=None):
    """Collect the most useful intelligence tables into one lightweight list."""
    filters = filters or {}
    frames = []
    for key, label in [
        ("cards", "dashboard_cards.csv"),
        ("high_confidence", "high_confidence_watchlist.csv"),
        ("opportunities", "opportunity_radar.csv"),
        ("distress", "distress_watchlist.csv"),
        ("la_assets", "la_asset_watch.csv"),
        ("la_entitlement", "la_entitlement_watch.csv"),
        ("la_lifecycle", "la_development_lifecycle_watch.csv"),
        ("la_persistent_assets", "la_persistent_asset_watch.csv"),
        ("gp_watchlist", "gp_watchlist.csv"),
        ("institutional_relationships", "institutional_relationships.csv"),
        ("relationship_graph", "relationship_graph.csv"),
        ("historical_memory", "historical_memory.csv"),
        ("persistent_asset_memory", "persistent_asset_memory.csv"),
        ("lifecycle_transition", "lifecycle_transition.csv"),
        ("relationship_persistence", "relationship_persistence.csv"),
    ]:
        df = apply_filters(shared.get(key, pd.DataFrame()), filters)
        if df.empty:
            continue
        temp = df.copy()
        temp["_source_layer"] = label
        frames.append(temp)
    return frames


def combined_reasoning_rows(shared, filters=None):
    frames = source_frames_for_reasoning(shared, filters)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True, sort=False)


def rows_matching_keywords(df, keywords):
    if df is None or df.empty:
        return df if df is not None else pd.DataFrame()
    keywords = [word.lower() for word in keywords]
    mask = df.apply(lambda row: any(word in text_blob(row.to_dict()).lower() for word in keywords), axis=1)
    return df[mask].copy()


def collect_unique_values(df, fields, limit=5):
    values = []
    if df is None or df.empty:
        return []
    for _, row in df.iterrows():
        item = get_first(row.to_dict(), fields)
        if item and item not in values:
            values.append(item)
        if len(values) >= limit:
            break
    return values


REGIME_THEME_RULES = [
    {
        "title": "리파이낸싱 스트레스 확대",
        "keywords": ["refinancing", "refinance", "maturity", "loan maturity", "bridge loan", "floating-rate", "debt service", "recap"],
        "why": "만기와 금리 부담이 커지면 construction loan sizing, refinancing, recap, JV gap 기회가 동시에 나타날 수 있습니다.",
        "woomi": "재무 / 자금팀과 투자팀은 반복되는 대주, 만기, sponsor stress를 함께 추적해야 합니다.",
        "focus": "refinancing maturity, bridge lender activity, agency debt, recap 가능성",
    },
    {
        "title": "공사 및 개발 속도 둔화",
        "keywords": ["stalled", "delayed", "paused", "construction delay", "construction financing gap", "construction loan", "started construction"],
        "why": "착공 지연과 공사금융 갭은 개발 pipeline의 실행 리스크와 구조화 자본 수요를 동시에 보여줍니다.",
        "woomi": "개발 / 인허가팀은 공사준비 단계와 stalled project를 구분해 site 또는 JV 타이밍을 검토해야 합니다.",
        "focus": "construction-ready assets, financing gap, stalled project watch",
    },
    {
        "title": "LA 인허가 병목 및 정책 민감도",
        "keywords": ["los angeles", "california", "entitlement", "permit", "zoning", "ceqa", "density bonus", "toc", "builder"],
        "why": "LA / California의 인허가 신호는 개발 가능 용적, 일정, 소송·환경 리스크를 직접 좌우합니다.",
        "woomi": "미국 현지팀은 entitlement precedent, density bonus, CEQA, local sponsor 움직임을 반복 관찰해야 합니다.",
        "focus": "LA entitlement docket, density bonus, CEQA, permit issuance",
    },
    {
        "title": "기관 자본 집중 및 관계 맵 강화",
        "keywords": ["blackstone", "brookfield", "kennedy wilson", "greystar", "institutional", "capital partner", "relationship", "jv", "partnership"],
        "why": "기관 자본과 GP의 반복 연결은 가격 발견, 경쟁 강도, 잠재 파트너십 방향을 보여줍니다.",
        "woomi": "전략팀은 반복 등장하는 GP, 대주, capital partner를 관계 구축 후보로 분류해야 합니다.",
        "focus": "repeat GP-capital relationships, institutional partner concentration",
    },
    {
        "title": "Affordable / Workforce Housing 모멘텀",
        "keywords": ["affordable", "workforce", "lihtc", "tax credit", "mixed-income", "income-restricted", "density bonus"],
        "why": "affordable component는 인허가 속도, public incentive, capital stack 구성에 영향을 줍니다.",
        "woomi": "LA 전략에서는 affordable overlay와 density incentive를 site strategy의 비교사례로 활용할 수 있습니다.",
        "focus": "affordable overlay, LIHTC, mixed-income approvals",
    },
    {
        "title": "Adaptive Reuse / Office Conversion 관심",
        "keywords": ["office-to-residential", "office conversion", "adaptive reuse", "conversion to apartments", "downtown conversion"],
        "why": "office conversion은 도시형 주거 공급, 비용 가정, entitlement path가 결합된 개발전략 신호입니다.",
        "woomi": "DTLA 등 도시형 submarket에서 conversion feasibility와 local approval precedent를 추적해야 합니다.",
        "focus": "DTLA conversion, adaptive reuse ordinance, feasibility signals",
    },
    {
        "title": "Sun Belt 공급 정상화 관찰",
        "keywords": ["sun belt", "texas", "dallas", "austin", "phoenix", "florida", "supply", "lease-up", "concession", "vacancy"],
        "why": "공급 정상화 또는 lease-up 압력은 rent growth와 development timing에 영향을 줍니다.",
        "woomi": "투자팀은 Sun Belt 시장의 공급 부담과 매입 가격 조정 가능성을 함께 검토해야 합니다.",
        "focus": "lease-up, concessions, new supply, market entry timing",
    },
]


def strategic_conviction_score(rows, base_count=0):
    """Score conviction from frequency, recurrence, source variety, and specificity."""
    if rows is None or rows.empty:
        return 0
    count = len(rows)
    source_count = len(set(collect_unique_values(rows, ["_source_layer"], limit=50)))
    recurring_total = 0
    specificity_hits = 0
    institutional_hits = 0
    for _, row in rows.iterrows():
        item = row.to_dict()
        recurring_total += recurring_observation_count(item)
        if any(get_first(item, fields) for fields in [
            ["canonical_project_name", "project_or_deal_name", "canonical_asset_or_project_name"],
            ["url", "source_url_if_available"],
            ["gp_or_developer", "canonical_gp_name", "firm_name"],
            ["lender_or_debt_provider", "lender_or_capital_provider"],
        ]):
            specificity_hits += 1
        if any(term in text_blob(item).lower() for term in ["institutional", "blackstone", "brookfield", "fannie mae", "freddie mac", "jll", "cbre", "berkadia"]):
            institutional_hits += 1
    score = min(100, (count * 7) + (source_count * 9) + min(20, recurring_total * 3) + min(20, specificity_hits * 3) + min(16, institutional_hits * 4) + base_count)
    return int(score)


def conviction_label(score):
    if score >= 80:
        return "High Conviction"
    if score >= 60:
        return "Strong"
    if score >= 40:
        return "Developing"
    return "Emerging"


def conviction_badge(score):
    label = conviction_label(score)
    colors = {
        "High Conviction": ("#7f1d1d", "#fee2e2", "#fecaca"),
        "Strong": ("#92400e", "#fef3c7", "#fde68a"),
        "Developing": ("#1e40af", "#dbeafe", "#bfdbfe"),
        "Emerging": ("#475569", "#f1f5f9", "#cbd5e1"),
    }
    color, background, border = colors[label]
    return badge(label, color=color, background=background, border=border)


def build_market_regime_observations(shared, filters=None, limit=5):
    combined = combined_reasoning_rows(shared, filters)
    observations = []
    for rule in REGIME_THEME_RULES:
        matched = rows_matching_keywords(combined, rule["keywords"])
        if matched.empty:
            continue
        score = strategic_conviction_score(matched)
        observations.append({
            "title": rule["title"],
            "supporting_count": len(matched),
            "score": score,
            "why": rule["why"],
            "woomi": rule["woomi"],
            "focus": rule["focus"],
            "markets": collect_unique_values(matched, ["market", "la_submarket", "submarket", "city_or_submarket"], limit=4),
            "sectors": collect_unique_values(matched, ["residential_sector", "residential_sector_focus"], limit=4),
            "gps": collect_unique_values(matched, ["gp_or_developer", "canonical_gp_name", "firm_name"], limit=4),
            "rows": matched.head(8),
        })
    observations.sort(key=lambda item: (item["score"], item["supporting_count"]), reverse=True)
    return observations[:limit]


def pattern_count(shared, filters, keywords):
    return len(rows_matching_keywords(combined_reasoning_rows(shared, filters), keywords))


def generate_cross_signal_reasoning(shared, filters=None):
    combined = combined_reasoning_rows(shared, filters)
    if combined.empty:
        return []
    rules = [
        {
            "title": "리파이낸싱 압박 + 지연 프로젝트 + bridge lending",
            "groups": [
                ["refinancing", "maturity", "recap"],
                ["stalled", "delayed", "paused", "distress"],
                ["bridge loan", "lender", "construction loan", "debt"],
            ],
            "interpretation": "자금 만기 압박과 개발 지연이 함께 관찰되면 recap 또는 JV gap 가능성을 점검할 필요가 있습니다.",
            "implication": "Woomi는 sponsor stress, 대주 관계, 담보 프로젝트의 실제 단계 확인을 우선순위로 둘 수 있습니다.",
        },
        {
            "title": "LA 인허가 신호 + affordable / density momentum",
            "groups": [
                ["los angeles", "california", "koreatown", "dtla", "hollywood"],
                ["entitlement", "permit", "zoning", "ceqa"],
                ["affordable", "density bonus", "toc", "mixed-income", "lihtc"],
            ],
            "interpretation": "LA 인허가와 affordable incentive가 같이 나타나면 현지 개발 timing과 site strategy 비교사례가 생깁니다.",
            "implication": "미국 현지팀은 approval precedent, affordability requirement, density bonus 적용 사례를 반복 추적해야 합니다.",
        },
        {
            "title": "반복 lender 활동 + GP 관계 집중",
            "groups": [
                ["lender", "fannie mae", "freddie mac", "berkadia", "greystone", "jll", "cbre"],
                ["relationship", "partnership", "capital partner", "institutional"],
                ["recurring", "repeat", "persistence", "observation"],
            ],
            "interpretation": "대주와 GP가 반복적으로 연결되면 capital relationship map의 신뢰도가 높아집니다.",
            "implication": "전략팀은 반복 등장하는 lender-GP 조합을 partnership 또는 pricing benchmark 후보로 관리할 수 있습니다.",
        },
        {
            "title": "construction financing gap + lifecycle stall",
            "groups": [
                ["construction financing", "construction loan", "financing gap"],
                ["lifecycle", "stalled", "same stage", "delayed", "possible stall"],
                ["project", "asset", "development"],
            ],
            "interpretation": "공사금융 갭과 lifecycle 정체가 함께 나타나면 실행 리스크와 rescue capital 수요를 동시에 시사합니다.",
            "implication": "투자팀은 construction-ready asset과 stalled asset을 구분해 진입 타이밍을 검토해야 합니다.",
        },
    ]
    results = []
    for rule in rules:
        linked_counts = [len(rows_matching_keywords(combined, group)) for group in rule["groups"]]
        if sum(1 for count in linked_counts if count > 0) < 2:
            continue
        matched = rows_matching_keywords(combined, [word for group in rule["groups"] for word in group])
        score = strategic_conviction_score(matched, base_count=sum(linked_counts))
        results.append({
            "title": rule["title"],
            "linked_signals": linked_counts,
            "count": len(matched),
            "interpretation": rule["interpretation"],
            "implication": rule["implication"],
            "confidence": conviction_label(score),
            "score": score,
            "rows": matched.head(6),
        })
    return sorted(results, key=lambda item: item["score"], reverse=True)


def build_strategic_watch_themes(shared, filters=None, limit=6):
    observations = build_market_regime_observations(shared, filters, limit=8)
    themes = []
    for obs in observations:
        rows = obs["rows"]
        top_projects = collect_unique_values(rows, ["canonical_project_name", "project_or_deal_name", "canonical_asset_or_project_name", "asset_or_project_name"], limit=3)
        themes.append({
            "theme": obs["title"],
            "score": obs["score"],
            "related_signals": obs["supporting_count"],
            "markets": obs["markets"],
            "gps": obs["gps"],
            "projects": top_projects,
            "evidence": f"{obs['supporting_count']}개 관련 신호 · {', '.join(obs['markets'] or ['시장 미확인'])}",
            "monitoring": obs["focus"],
        })
    return themes[:limit]


def build_relationship_intelligence(shared, filters=None, limit=5):
    frames = []
    for key in ["relationship_persistence", "relationship_graph", "institutional_relationships", "historical_memory", "gp_watchlist"]:
        df = apply_filters(shared.get(key, pd.DataFrame()), filters or {})
        if not df.empty:
            temp = df.copy()
            temp["_source_layer"] = key
            frames.append(temp)
    if not frames:
        return []
    combined = pd.concat(frames, ignore_index=True, sort=False)
    rows = []
    for _, row in combined.iterrows():
        item = row.to_dict()
        text = text_blob(item).lower()
        if not any(term in text for term in ["relationship", "lender", "capital", "partner", "gp", "developer", "repeat", "persistent"]):
            continue
        score = investment_priority_score(item) + min(20, recurring_observation_count(item) * 4)
        rows.append((score, item))
    rows.sort(key=lambda pair: pair[0], reverse=True)
    results = []
    for score, item in rows[:limit]:
        results.append({
            "title": get_title(item) or get_gp(item) or get_first(item, ["source_entity", "firm_name"], "관계 신호"),
            "score": min(100, int(score)),
            "market": get_market(item),
            "gp": get_gp(item) or get_first(item, ["source_entity", "target_entity", "firm_name"]),
            "pattern": get_first(item, ["relationship_type", "strategic_relationship_label", "relationship_signal", "recurring_signal_label"], "반복 관계 관찰"),
            "action": "반복 등장하는 GP / lender / capital partner를 관계 구축 후보로 분류하고 원문 근거를 확인하십시오.",
            "row": item,
        })
    return results


def why_today_matters(shared, filters=None):
    observations = build_market_regime_observations(shared, filters, limit=3)
    reasoning = generate_cross_signal_reasoning(shared, filters)
    if not observations:
        return ["오늘은 강한 시장 체제 변화보다 기존 watchlist를 유지하며 반복 관찰 여부를 확인하는 흐름입니다."]
    lines = []
    top = observations[0]
    lines.append(f"{top['title']} 관련 신호가 가장 강합니다. 관련 근거는 {top['supporting_count']}개이며, {', '.join(top['markets'] or ['복수 시장'])}에서 관찰됩니다.")
    if len(observations) > 1:
        second = observations[1]
        lines.append(f"보조적으로 {second['title']} 흐름이 나타나며, 이는 단일 뉴스보다 여러 레이어의 반복 관찰로 해석하는 것이 적절합니다.")
    if reasoning:
        lines.append(f"가장 중요한 cross-signal 조합은 '{reasoning[0]['title']}'입니다. {reasoning[0]['interpretation']}")
    return lines


def build_womi_monitoring_items(shared, filters=None):
    observations = build_market_regime_observations(shared, filters, limit=5)
    relationship_items = build_relationship_intelligence(shared, filters, limit=3)
    items = []
    for obs in observations[:4]:
        items.append(f"{obs['title']}: {obs['focus']}")
    for rel in relationship_items[:2]:
        items.append(f"관계 흐름: {rel['gp'] or rel['title']} 반복 활동과 capital relationship 확인")
    if not items:
        items.append("고신뢰 watchlist와 LA / California 프로젝트 업데이트를 반복 확인")
    return items[:6]


def build_market_timeline(shared, filters=None):
    observations = build_market_regime_observations(shared, filters, limit=4)
    reasoning = generate_cross_signal_reasoning(shared, filters)
    timeline = []
    if observations:
        timeline.append(("현재", f"{observations[0]['title']} 흐름이 가장 강하게 관찰됩니다."))
    if reasoning:
        timeline.append(("단기", f"{reasoning[0]['title']} 조합을 통해 실행 가능한 recap, JV, entitlement watch 후보를 좁혀야 합니다."))
    timeline.append(("반복 관찰", "향후 실행 판단은 동일 GP, 동일 lender, 동일 프로젝트의 재등장 여부에 따라 conviction을 높이는 방식이 적절합니다."))
    timeline.append(("다음 검토", "새 run 이후 lifecycle progression, refinancing signal, LA entitlement update가 강화되는지 확인하십시오."))
    return timeline


def render_regime_observations(shared, filters=None, limit=3):
    st.markdown("### 시장 체제 변화 (Market Regime Intelligence)")
    observations = build_market_regime_observations(shared, filters, limit=limit)
    if not observations:
        st.info("현재 강한 시장 체제 변화가 감지되지 않았습니다.")
        return
    for obs in observations:
        with st.container():
            render_badges([
                conviction_badge(obs["score"]),
                badge(f"근거 {obs['supporting_count']}개", color="#1e3a8a", background="#dbeafe", border="#bfdbfe"),
            ])
            st.markdown(f"**{obs['title']}**")
            st.write(obs["why"])
            meta = []
            if obs["markets"]:
                meta.append(f"영향 시장: {', '.join(obs['markets'])}")
            if obs["sectors"]:
                meta.append(f"영향 섹터: {', '.join(obs['sectors'])}")
            if obs["gps"]:
                meta.append(f"관련 GP: {', '.join(obs['gps'])}")
            if meta:
                st.caption(" · ".join(meta))
            st.markdown(f"**우미 시사점:** {obs['woomi']}")
            st.markdown(f"**모니터링 포커스:** {obs['focus']}")
            if is_detail_mode():
                render_expandable_table(f"{obs['title']} 근거 데이터", obs["rows"], None)
            st.divider()


def render_cross_signal_reasoning(shared, filters=None, limit=3):
    st.markdown("### Cross-Signal Reasoning / 교차 시그널 해석")
    items = generate_cross_signal_reasoning(shared, filters)[:limit]
    if not items:
        st.info("현재 교차 확인된 강한 패턴은 제한적입니다.")
        return
    for item in items:
        render_badges([
            conviction_badge(item["score"]),
            badge(f"연결 신호 {item['count']}개", color="#3f3f46", background="#f4f4f5", border="#d4d4d8"),
        ])
        st.markdown(f"**{item['title']}**")
        st.write(item["interpretation"])
        st.markdown(f"**전략적 의미:** {item['implication']}")
        st.caption(f"신뢰도: {item['confidence']} · linked signals: {', '.join(str(v) for v in item['linked_signals'])}")
        if is_detail_mode():
            render_expandable_table(f"{item['title']} 관련 근거", item["rows"], None)
        st.divider()


def render_why_today_matters(shared, filters=None):
    st.markdown("### 오늘 시장에서 중요한 변화")
    for line in why_today_matters(shared, filters):
        st.markdown(f"- {line}")


def render_strategic_watch_themes(shared, filters=None, limit=4):
    st.markdown("### 전략 모니터링 테마")
    themes = build_strategic_watch_themes(shared, filters, limit=limit)
    if not themes:
        st.info("현재 전략 테마를 만들 충분한 근거가 없습니다.")
        return
    for theme in themes:
        render_badges([
            conviction_badge(theme["score"]),
            badge(f"{theme['related_signals']}개 신호", color="#065f46", background="#d1fae5", border="#a7f3d0"),
        ])
        st.markdown(f"**{theme['theme']}**")
        st.caption(theme["evidence"])
        if theme["gps"]:
            st.write(f"관련 GP / 개발사: {', '.join(theme['gps'])}")
        if theme["projects"]:
            st.write(f"상위 프로젝트: {', '.join(theme['projects'])}")
        st.write(f"모니터링 포커스: {theme['monitoring']}")
        st.divider()


def render_relationship_intelligence(shared, filters=None, limit=4):
    st.markdown("### 관계 흐름 분석")
    items = build_relationship_intelligence(shared, filters, limit=limit)
    if not items:
        st.info("반복 관계 또는 capital relationship 근거가 제한적입니다.")
        return
    for item in items:
        render_badges([conviction_badge(item["score"]), badge(item["pattern"], color="#1e3a8a", background="#dbeafe", border="#bfdbfe")])
        st.markdown(f"**{item['title']}**")
        st.write(f"시장: {item['market'] or '미확인'} · 관계 대상: {item['gp'] or '미확인'}")
        st.write(item["action"])
        if is_detail_mode():
            render_evidence_block(item["row"])
        st.divider()


def render_womi_monitoring_block(shared, filters=None):
    st.markdown("### 우미 중점 모니터링")
    for item in build_womi_monitoring_items(shared, filters):
        st.markdown(f"- {item}")


def render_market_timeline(shared, filters=None):
    st.markdown("### 시장 흐름 타임라인")
    for label, text in build_market_timeline(shared, filters):
        st.markdown(f"**{label}** · {text}")


def safe_render_section(section_name, render_function, *args, **kwargs):
    """Render one reasoning section without letting a data edge case stop the page."""
    try:
        render_function(*args, **kwargs)
    except Exception as error:
        st.warning(f"{section_name} 섹션을 표시하는 중 일부 데이터 형식 문제가 있었습니다: {error}")


# Fast overrides for regime reasoning. These keep the executive page responsive
# by scanning only dashboard-relevant fields and a capped number of rows.
REASONING_TEXT_FIELDS = [
    "card_title", "summary", "why_it_matters", "recommended_action",
    "source_article_title", "title", "item_name", "market", "la_submarket",
    "submarket", "residential_sector", "gp_or_developer", "canonical_gp_name",
    "firm_name", "relationship_type", "relationship_signal", "capital_flow_signal",
    "opportunity_type", "distress_type", "current_lifecycle_stage",
    "latest_lifecycle_stage", "evidence_signals", "key_evidence",
]


def compact_text_blob(row):
    parts = []
    for field in REASONING_TEXT_FIELDS:
        value = row.get(field, "")
        if pd.isna(value):
            continue
        text = str(value).strip()
        if text and text.lower() != "nan":
            parts.append(text[:350])
    if not parts:
        return text_blob(row)[:1200]
    return " ".join(parts).lower()


def source_frames_for_reasoning(shared, filters=None):
    """Collect a capped, text-indexed set of rows for fast reasoning."""
    filters = filters or {}
    frames = []
    for key, label, cap in [
        ("cards", "dashboard_cards.csv", 40),
        ("high_confidence", "high_confidence_watchlist.csv", 35),
        ("opportunities", "opportunity_radar.csv", 40),
        ("distress", "distress_watchlist.csv", 25),
        ("la_assets", "la_asset_watch.csv", 35),
        ("la_entitlement", "la_entitlement_watch.csv", 35),
        ("la_lifecycle", "la_development_lifecycle_watch.csv", 35),
        ("la_persistent_assets", "la_persistent_asset_watch.csv", 35),
        ("gp_watchlist", "gp_watchlist.csv", 35),
        ("institutional_relationships", "institutional_relationships.csv", 35),
        ("relationship_graph", "relationship_graph.csv", 35),
        ("historical_memory", "historical_memory.csv", 45),
        ("persistent_asset_memory", "persistent_asset_memory.csv", 45),
        ("lifecycle_transition", "lifecycle_transition.csv", 35),
        ("relationship_persistence", "relationship_persistence.csv", 35),
    ]:
        df = apply_filters(shared.get(key, pd.DataFrame()), filters)
        if df.empty:
            continue
        temp = df.head(cap).copy()
        temp["_source_layer"] = label
        temp["_reasoning_text"] = temp.apply(lambda row: compact_text_blob(row.to_dict()), axis=1)
        frames.append(temp)
    return frames


def rows_matching_keywords(df, keywords):
    if df is None or df.empty:
        return df if df is not None else pd.DataFrame()
    keywords = [word.lower() for word in keywords]
    if "_reasoning_text" not in df.columns:
        df = df.copy()
        df["_reasoning_text"] = df.apply(lambda row: compact_text_blob(row.to_dict()), axis=1)
    pattern = "|".join([word.replace("|", " ") for word in keywords])
    if not pattern:
        return df.head(0)
    return df[df["_reasoning_text"].str.contains(pattern, case=False, na=False, regex=True)].copy()


def page_regime_reasoning(shared, filters):
    st.subheader("시장 체제 / 교차 시그널 분석")
    st.caption("여러 출력 파일의 신호를 묶어 시장 체제, 반복 관계, 전략 테마를 해석합니다.")
    safe_render_section("오늘 시장에서 중요한 변화", render_why_today_matters, shared, filters)
    safe_render_section("시장 체제 변화", render_regime_observations, shared, filters, limit=5 if is_detail_mode() else 3)
    safe_render_section("교차 시그널 해석", render_cross_signal_reasoning, shared, filters, limit=5 if is_detail_mode() else 3)
    safe_render_section("전략 모니터링 테마", render_strategic_watch_themes, shared, filters, limit=6 if is_detail_mode() else 4)
    safe_render_section("관계 흐름 분석", render_relationship_intelligence, shared, filters, limit=6 if is_detail_mode() else 4)
    safe_render_section("우미 중점 모니터링", render_womi_monitoring_block, shared, filters)
    safe_render_section("시장 흐름 타임라인", render_market_timeline, shared, filters)


def page_executive_briefing(shared, filters):
    """Korean-first executive briefing with regime reasoning before action."""
    st.subheader("경영진 브리핑")
    st.caption("본 화면은 한국어 경영진 보고용으로 재구성한 요약입니다. 회사명, 시장명, 프로젝트명은 원문 식별을 위해 영어 표기를 유지합니다.")

    cards = apply_filters(shared["cards"], filters)
    priority_rows = candidate_priority_rows(shared, filters, limit=8)

    top_row = ko_hero_section(cards, shared)
    safe_render_section("오늘 시장에서 중요한 변화", render_why_today_matters, shared, filters)
    safe_render_section("시장 체제 변화", render_regime_observations, shared, filters, limit=3)
    safe_render_section("교차 시그널 해석", render_cross_signal_reasoning, shared, filters, limit=2)
    safe_render_section("전략 모니터링 테마", render_strategic_watch_themes, shared, filters, limit=3)
    safe_render_section("관계 흐름 분석", render_relationship_intelligence, shared, filters, limit=3)
    safe_render_section("우미 중점 모니터링", render_womi_monitoring_block, shared, filters)
    safe_render_section("시장 흐름 타임라인", render_market_timeline, shared, filters)

    st.markdown("### 투자 판단 프레임")
    if priority_rows.empty and top_row:
        priority_rows = pd.DataFrame([top_row])
    render_investment_decision_framework(priority_rows, shared)

    st.markdown("### 오늘 체크할 액션")
    action_source = priority_rows if not priority_rows.empty else cards
    ko_action_bullets(action_source)

    render_ic_prep_preview(priority_rows)

    st.markdown("### 주요 기회 및 리스크")
    ko_signal_section("투자 기회", apply_filters(shared["opportunities"], filters), shared, ["opportunity_score"], FILES["opportunities"], limit=3)
    ko_signal_section("리스크 모니터링", apply_filters(shared["distress"], filters), shared, ["distress_score"], FILES["distress"], limit=3)

    st.markdown("### LA / California 관찰 사항")
    ko_signal_section("LA 자산 / 프로젝트 모니터링", apply_filters(shared["la_assets"], filters), shared, ["la_asset_opportunity_score"], FILES["la_assets"], limit=3)

    st.markdown("### GP 및 자본 파트너 동향")
    ko_signal_section("GP 모니터링", apply_filters(shared["gp_watchlist"], filters), shared, ["emerging_gp_score"], FILES["gp_watchlist"], limit=3)

    if is_detail_mode():
        render_expandable_table("상세 데이터", priority_rows if not priority_rows.empty else cards, FILES["dashboard_cards"])


def legacy_main_07():
    """Run the Korean-first regime and investment intelligence platform."""
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("투자 인텔리전스 플랫폼")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드"], key="view_mode")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "체제 / 교차 시그널": page_regime_reasoning,
        "투자검토 메모": page_investment_committee_prep,
        "시장 인텔리전스": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California 전략": page_la_california_strategy,
        "GP / 자본 관계": page_gp_capital_relationships,
        "시스템 / 파이프라인": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"],
        shared["watchlists"],
        shared["high_confidence"],
        shared["opportunities"],
        shared["distress"],
        shared["la_assets"],
        shared["la_entitlement"],
        shared["la_lifecycle"],
        shared["la_persistent_assets"],
        shared["gp_watchlist"],
        shared["institutional_relationships"],
        shared["relationship_graph"],
        shared["historical_memory"],
        shared["persistent_asset_memory"],
        shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"최근 실행: {summary.get('run_timestamp', '실행 데이터 없음')}")
    if is_detail_mode():
        kpi_strip(shared)
    else:
        cols = st.columns(3)
        with cols[0]:
            render_compact_metric("기관급 검토 항목", int(as_number(summary.get("high_confidence_signals", 0))))
        with cols[1]:
            render_compact_metric("주요 기회", int(as_number(summary.get("opportunity_count", 0))))
        with cols[2]:
            render_compact_metric("LA 관찰 항목", int(as_number(summary.get("la_asset_watch_count", 0))))
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | 체제 변화 및 투자 인텔리전스 플랫폼 | Streamlit Cloud-ready | No paid APIs")


# ---------------------------------------------------------------------------
# Strategic Narrative and Investment Committee Intelligence overlay
# ---------------------------------------------------------------------------

def strategic_momentum_label(score, count=0):
    """Translate conviction and evidence count into an executive momentum label."""
    if score >= 80 and count >= 20:
        return "전략 중요도 높음"
    if score >= 65 and count >= 10:
        return "구조적 변화 가능성"
    if score >= 50:
        return "시장 확산 가능성"
    if count >= 3:
        return "반복 관찰 증가"
    return "초기 포착"


def render_insight_block(title, body, badges=None):
    """Consistent narrative block for executive memo-style sections."""
    badge_html = " ".join(badges or [])
    st.markdown(
        f"""
        <div class="soft-card">
          <div class="muted">{badge_html}</div>
          <div style="font-weight:700; font-size:1.02rem; margin:.35rem 0;">{title}</div>
          <div style="line-height:1.65;">{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def daily_strategic_narrative(shared, filters=None):
    observations = build_market_regime_observations(shared, filters, limit=4)
    reasoning = generate_cross_signal_reasoning(shared, filters)
    relationships = build_relationship_intelligence(shared, filters, limit=3)
    top = observations[0] if observations else None
    second = observations[1] if len(observations) > 1 else None
    capital = next((obs for obs in observations if "자본" in obs["title"] or "리파이낸싱" in obs["title"]), top)
    entitlement = next((obs for obs in observations if "인허가" in obs["title"] or "Affordable" in obs["title"]), second or top)
    gp_move = relationships[0] if relationships else None
    return {
        "시장 핵심 변화": (
            f"{top['title']} 흐름이 가장 강하게 관찰됩니다. 근거 {top['supporting_count']}개가 여러 출력 레이어에서 반복 확인되어 단일 기사보다 시장 분위기 변화로 해석할 여지가 있습니다."
            if top else "오늘은 뚜렷한 체제 변화보다 기존 watchlist를 유지하며 반복 관찰을 축적하는 국면입니다."
        ),
        "자본시장 흐름": (
            f"{capital['title']}은 Woomi가 refinancing, recap, preferred equity, JV gap 가능성을 함께 점검해야 함을 시사합니다."
            if capital else "자본시장 신호는 아직 강하지 않으므로 기관 자본과 대주 움직임을 추가 관찰해야 합니다."
        ),
        "개발 / 인허가 흐름": (
            f"{entitlement['title']} 관련 관찰은 개발 timing, entitlement precedent, construction readiness 판단에 직접 연결됩니다."
            if entitlement else "개발 / 인허가 흐름은 현재 선별적이며, LA / California 프로젝트 업데이트 중심의 모니터링이 적절합니다."
        ),
        "GP / 기관투자자 움직임": (
            f"{gp_move['title']} 관련 반복 관계가 관찰됩니다. 이는 관계 구축 후보, 가격 벤치마크, capital partner mapping에 활용할 수 있습니다."
            if gp_move else "GP / 기관투자자 움직임은 아직 분산되어 있어 반복 등장하는 sponsor와 lender 조합을 먼저 확인해야 합니다."
        ),
        "우미 전략 시사점": (
            "향후 6~18개월은 단일 매입 판단보다 recap 가능성, LA entitlement precedent, 반복 GP/lender 관계, construction-ready pipeline을 동시에 추적하는 준비 국면으로 보는 것이 적절합니다."
        ),
    }


def render_daily_strategic_narrative(shared, filters=None):
    st.markdown("### 오늘의 전략 해석")
    narrative = daily_strategic_narrative(shared, filters)
    for title, body in narrative.items():
        render_insight_block(title, body)


def market_timing_phase(shared, filters=None):
    observations = build_market_regime_observations(shared, filters, limit=5)
    if not observations:
        return "초기 관찰 국면", "강한 방향성보다 반복 관찰 축적이 필요한 단계입니다.", 25
    top = observations[0]
    title = top["title"]
    score = top["score"]
    if "리파이낸싱" in title:
        return "financing stress phase / 리파이낸싱 압박 국면", "만기와 자금조달 부담이 투자 조건과 recap 기회 판단의 중심 변수가 될 수 있습니다.", score
    if "공사" in title or "개발" in title:
        return "construction slowdown phase / 개발 실행 둔화 국면", "공사금융, 착공, 지연 프로젝트의 실제 실행 가능성을 선별해야 합니다.", score
    if "인허가" in title or "Affordable" in title:
        return "entitlement accumulation phase / 인허가 축적 국면", "승인 사례와 정책 인센티브가 향후 site strategy의 비교 근거가 될 수 있습니다.", score
    if "기관" in title or "자본" in title:
        return "institutional re-entry phase / 기관 자본 재정렬 국면", "기관 자본의 반복 등장 여부가 가격 발견과 GP 관계 구축의 선행 신호가 될 수 있습니다.", score
    return "mixed monitoring phase / 복합 모니터링 국면", "여러 신호가 혼재되어 있어 단일 narrative보다 theme별 모니터링이 중요합니다.", score


def render_market_timing_interpretation(shared, filters=None):
    st.markdown("### 시장 Timing 해석")
    phase, explanation, score = market_timing_phase(shared, filters)
    render_insight_block(
        phase,
        explanation,
        badges=[conviction_badge(score), badge(strategic_momentum_label(score, 5), color="#1e3a8a", background="#dbeafe", border="#bfdbfe")],
    )


def forward_looking_outlook(shared, filters=None):
    observations = build_market_regime_observations(shared, filters, limit=5)
    themes = build_strategic_watch_themes(shared, filters, limit=5)
    outlook = []
    for obs in observations[:3]:
        if "리파이낸싱" in obs["title"]:
            outlook.append("리파이낸싱 만기와 debt service 부담이 반복되면 JV recap, preferred equity, rescue capital 수요가 증가할 수 있습니다.")
        elif "인허가" in obs["title"]:
            outlook.append("LA / California 인허가 precedent가 축적되면 density bonus, affordable overlay, CEQA 리스크를 반영한 site screening이 중요해질 수 있습니다.")
        elif "기관" in obs["title"]:
            outlook.append("기관 자본과 GP 관계가 반복되면 Woomi의 partner mapping과 pricing benchmark 체계가 더 중요해질 수 있습니다.")
        elif "Affordable" in obs["title"]:
            outlook.append("Affordable / workforce housing momentum은 공공 인센티브, entitlement path, capital stack 구성에서 전략 기회를 만들 수 있습니다.")
        elif "Sun Belt" in obs["title"]:
            outlook.append("Sun Belt 공급 정상화가 이어지면 가격 조정과 lease-up 리스크를 동시에 반영한 선별적 진입 검토가 필요합니다.")
    if themes:
        outlook.append(f"현재 반복 모니터링해야 할 상위 테마는 {themes[0]['theme']}입니다.")
    while len(outlook) < 4:
        outlook.append("다음 run에서 동일 시장, 동일 GP, 동일 lender가 반복 등장하는지 확인하면 conviction을 높일 수 있습니다.")
    return outlook[:5]


def render_forward_outlook(shared, filters=None):
    st.markdown("### 향후 관찰 포인트 (6–18개월)")
    for item in forward_looking_outlook(shared, filters):
        st.markdown(f"- {item}")


def what_could_matter_next(shared, filters=None):
    combined = combined_reasoning_rows(shared, filters)
    if combined.empty:
        return ["초기 테마를 포착하려면 다음 run 이후 반복 등장하는 낮은 빈도 신호를 확인해야 합니다."]
    early_rules = [
        ("adaptive reuse / office conversion", ["adaptive reuse", "office conversion", "office-to-residential"]),
        ("bridge lender expansion", ["bridge loan", "bridge lender"]),
        ("GP recap activity", ["recapitalization", "recap", "preferred equity"]),
        ("affordable housing incentives", ["affordable", "lihtc", "density bonus", "toc"]),
        ("BTR / SFR platform growth", ["btr", "single-family rental", "sfr", "build-to-rent"]),
    ]
    items = []
    for title, keywords in early_rules:
        matched = rows_matching_keywords(combined, keywords)
        count = len(matched)
        if 0 < count <= 25:
            items.append(f"{title}: 아직 빈도는 제한적이지만 {count}개 근거가 있어 early drift로 추적할 가치가 있습니다.")
    if not items:
        items.append("현재 low-frequency emerging theme은 제한적이며, 상위 체제 변화 신호의 반복성을 우선 확인하는 것이 적절합니다.")
    return items[:5]


def render_what_could_matter_next(shared, filters=None):
    st.markdown("### 다음 단계에서 중요해질 가능성")
    for item in what_could_matter_next(shared, filters):
        st.markdown(f"- {item}")


def relationship_priority_targets(shared, filters=None, limit=5):
    items = build_relationship_intelligence(shared, filters, limit=limit + 3)
    targets = []
    for item in items[:limit]:
        row = item["row"]
        count = recurring_observation_count(row) or len(rows_matching_keywords(combined_reasoning_rows(shared, filters), [str(item["gp"] or item["title"]).lower()]))
        targets.append({
            "name": item["gp"] or item["title"],
            "score": item["score"],
            "market": item["market"] or "시장 미확인",
            "why": item["pattern"],
            "count": count,
            "angle": "반복 등장하는 GP / lender / institutional capital 관계를 파트너십, 가격 벤치마크, capital market read-through 후보로 관리",
        })
    return targets


def render_relationship_priority_targets(shared, filters=None):
    st.markdown("### 우선 관계 구축 대상")
    targets = relationship_priority_targets(shared, filters)
    if not targets:
        st.info("현재 우선 관계 구축 대상으로 분류할 반복 관계 신호가 제한적입니다.")
        return
    for target in targets:
        render_badges([
            conviction_badge(target["score"]),
            badge(f"반복 근거 {target['count']}개", color="#065f46", background="#d1fae5", border="#a7f3d0"),
        ])
        st.markdown(f"**{target['name']}**")
        st.write(f"관련 시장: {target['market']}")
        st.write(f"관계 중요성: {target['why']}")
        st.write(f"Woomi angle: {target['angle']}")
        st.divider()


def investment_heatmap_summary(shared, filters=None):
    combined = combined_reasoning_rows(shared, filters)
    if combined.empty:
        return []
    categories = [
        ("strongest opportunity markets", ["opportunity", "acquisition", "jv", "recap"], "기회 시장"),
        ("strongest stress markets", ["distress", "stalled", "default", "maturity", "refinancing"], "스트레스 시장"),
        ("strongest GP activity regions", ["gp", "developer", "partnership"], "GP 활동 지역"),
        ("strongest lender activity regions", ["lender", "fannie mae", "freddie mac", "berkadia", "greystone"], "대주 활동 지역"),
        ("strongest entitlement activity", ["entitlement", "permit", "zoning", "ceqa", "density bonus"], "인허가 활동"),
        ("strongest recurring capital flow", ["capital", "recurring", "relationship", "institutional"], "반복 자본 흐름"),
    ]
    blocks = []
    for _, keywords, label in categories:
        rows = rows_matching_keywords(combined, keywords)
        if rows.empty:
            continue
        markets = collect_unique_values(rows, ["market", "la_submarket", "submarket", "city_or_submarket"], limit=3)
        score = strategic_conviction_score(rows)
        blocks.append((score, label, markets, len(rows)))
    blocks.sort(reverse=True, key=lambda item: item[0])
    return blocks[:6]


def render_investment_heatmap_summary(shared, filters=None):
    st.markdown("### 투자 Heatmap 요약")
    blocks = investment_heatmap_summary(shared, filters)
    if not blocks:
        st.info("Heatmap 요약을 만들 충분한 데이터가 없습니다.")
        return
    for score, label, markets, count in blocks:
        render_badges([conviction_badge(score), badge(f"{count}개 근거", color="#334155", background="#f1f5f9", border="#cbd5e1")])
        st.markdown(f"**{label}**: {', '.join(markets or ['시장 미확인'])}")
        st.divider()


def ic_pro_argument(row):
    use_case = classify_investment_use_case(row)
    if use_case == "리파이낸싱 / Recap 기회":
        return "자금 만기와 refinancing 부담이 실제라면 recap, preferred equity, JV 구조 검토 여지가 생길 수 있습니다."
    if use_case == "LA 인허가 모니터링":
        return "인허가 precedent가 확인되면 LA site strategy와 entitlement timeline benchmark로 활용할 수 있습니다."
    if use_case == "GP 파트너십 검토":
        return "반복 등장하는 GP 또는 capital partner는 관계 구축 후보와 시장 가격 발견의 기준점이 될 수 있습니다."
    return "반복 관찰과 고신뢰 근거가 축적되면 전략 watchlist에서 투자 검토 후보로 전환될 수 있습니다."


def ic_con_argument(row):
    risks = risk_factors(row)
    return f"핵심 반대 논리는 {', '.join(risks[:2])}입니다. 원문 근거가 약하거나 프로젝트 특정성이 낮으면 실행 판단을 보류해야 합니다."


def ic_dd_items(row):
    items = verification_materials(row)[:3]
    items.append("동일 프로젝트 / GP / lender의 반복 관찰 여부")
    items.append("가격, 만기, 인허가 단계, sponsor 상황의 원문 확인")
    return items[:5]


def render_ic_memo_item(row, index):
    """Investment committee memo with pro/con and timing reasoning."""
    title = get_title(row) or f"투자검토 안건 {index}"
    phase, timing_text, timing_score = market_timing_phase(current_shared_data(), {})
    st.markdown(f"#### 안건 {index}: {truncate_text(title, 90)}")
    render_badges([
        score_badge(investment_priority_score(row)),
        actionability_badge(row),
        investment_use_case_badge(row),
        owner_badge(row),
        decision_status_badge(row),
        conviction_badge(timing_score),
    ])
    fields = [
        ("배경", ko_executive_summary(row)),
        ("핵심 관찰사항", f"{get_market(row)} / {get_gp(row) or '관련 GP 미확인'} / {classify_investment_use_case(row)}"),
        ("투자 찬성 논리", ic_pro_argument(row)),
        ("투자 반대 논리", ic_con_argument(row)),
        ("추가 DD 필요사항", "; ".join(ic_dd_items(row))),
        ("유사 사례 비교 포인트", "동일 시장의 financing terms, entitlement stage, unit count, sponsor 반복성, lender 관계를 비교하십시오."),
        ("예상 리스크", "; ".join(risk_factors(row))),
        ("실행 가능성", classify_actionability(row)),
        ("시장 timing 관점", f"{phase}: {timing_text}"),
        ("추천 액션", ko_recommended_action(row)),
    ]
    for label, value in fields:
        st.markdown(f"**{label}**")
        st.write(value)
    if is_detail_mode():
        render_evidence_block(row)
    st.divider()


def page_investment_committee_prep(shared, filters):
    st.subheader("Investment Committee Prep / 투자검토 메모")
    st.caption("상위 투자 관련 항목을 찬성 / 반대 논리와 DD 포인트 중심으로 정리합니다.")
    priority_rows = candidate_priority_rows(shared, filters, limit=6)
    if priority_rows.empty:
        st.info("현재 투자검토 메모를 만들 우선순위 항목이 없습니다.")
        return
    safe_render_section("시장 Timing 해석", render_market_timing_interpretation, shared, filters)
    for index, (_, row) in enumerate(priority_rows.head(3).iterrows(), start=1):
        render_ic_memo_item(row.to_dict(), index)
    if is_detail_mode():
        render_expandable_table("상세 후보 데이터", priority_rows, FILES["dashboard_cards"])


def page_executive_briefing(shared, filters):
    """Executive strategic narrative flow."""
    st.subheader("경영진 브리핑")
    st.caption("본 화면은 한국어 경영진 보고용으로 재구성한 요약입니다. 회사명, 시장명, 프로젝트명은 원문 식별을 위해 영어 표기를 유지합니다.")

    cards = apply_filters(shared["cards"], filters)
    priority_rows = candidate_priority_rows(shared, filters, limit=8)

    safe_render_section("오늘의 전략 해석", render_daily_strategic_narrative, shared, filters)
    safe_render_section("오늘 시장에서 중요한 변화", render_why_today_matters, shared, filters)
    safe_render_section("시장 체제 변화", render_regime_observations, shared, filters, limit=3)
    safe_render_section("시장 Timing 해석", render_market_timing_interpretation, shared, filters)

    top_row = ko_hero_section(cards, shared)

    st.markdown("### 투자 판단 프레임")
    if priority_rows.empty and top_row:
        priority_rows = pd.DataFrame([top_row])
    render_investment_decision_framework(priority_rows, shared)

    safe_render_section("우미 시사점", render_womi_monitoring_block, shared, filters)
    safe_render_section("우선 관계 구축 대상", render_relationship_priority_targets, shared, filters)
    safe_render_section("향후 관찰 포인트", render_forward_outlook, shared, filters)
    safe_render_section("다음 단계에서 중요해질 가능성", render_what_could_matter_next, shared, filters)
    safe_render_section("투자 Heatmap 요약", render_investment_heatmap_summary, shared, filters)

    st.markdown("### 주요 기회 및 리스크")
    ko_signal_section("투자 기회", apply_filters(shared["opportunities"], filters), shared, ["opportunity_score"], FILES["opportunities"], limit=3)
    ko_signal_section("리스크 모니터링", apply_filters(shared["distress"], filters), shared, ["distress_score"], FILES["distress"], limit=3)

    render_ic_prep_preview(priority_rows)

    if is_detail_mode():
        safe_render_section("교차 시그널 해석", render_cross_signal_reasoning, shared, filters, limit=4)
        safe_render_section("전략 모니터링 테마", render_strategic_watch_themes, shared, filters, limit=5)
        render_expandable_table("상세 데이터", priority_rows if not priority_rows.empty else cards, FILES["dashboard_cards"])


def page_strategic_narrative(shared, filters):
    st.subheader("전략 Narrative / 시장 Outlook")
    st.caption("시장 체제, timing, 관계 우선순위, 향후 6–18개월 관찰 포인트를 한 화면에서 봅니다.")
    render_daily_strategic_narrative(shared, filters)
    render_market_timing_interpretation(shared, filters)
    render_forward_outlook(shared, filters)
    render_relationship_priority_targets(shared, filters)
    render_what_could_matter_next(shared, filters)
    render_investment_heatmap_summary(shared, filters)
    if is_detail_mode():
        render_regime_observations(shared, filters, limit=5)
        render_cross_signal_reasoning(shared, filters, limit=5)


def legacy_main_08():
    """Run the strategic narrative and IC intelligence platform."""
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("전략 / 투자 인텔리전스 플랫폼")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드"], key="view_mode")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "전략 Narrative": page_strategic_narrative,
        "체제 / 교차 시그널": page_regime_reasoning,
        "투자검토 메모": page_investment_committee_prep,
        "시장 인텔리전스": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California 전략": page_la_california_strategy,
        "GP / 자본 관계": page_gp_capital_relationships,
        "시스템 / 파이프라인": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"],
        shared["watchlists"],
        shared["high_confidence"],
        shared["opportunities"],
        shared["distress"],
        shared["la_assets"],
        shared["la_entitlement"],
        shared["la_lifecycle"],
        shared["la_persistent_assets"],
        shared["gp_watchlist"],
        shared["institutional_relationships"],
        shared["relationship_graph"],
        shared["historical_memory"],
        shared["persistent_asset_memory"],
        shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"최근 실행: {summary.get('run_timestamp', '실행 데이터 없음')}")
    if is_detail_mode():
        kpi_strip(shared)
    else:
        cols = st.columns(3)
        with cols[0]:
            render_compact_metric("기관급 검토 항목", int(as_number(summary.get("high_confidence_signals", 0))))
        with cols[1]:
            render_compact_metric("주요 기회", int(as_number(summary.get("opportunity_count", 0))))
        with cols[2]:
            render_compact_metric("LA 관찰 항목", int(as_number(summary.get("la_asset_watch_count", 0))))
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | 전략 Narrative 및 투자검토 인텔리전스 | Streamlit Cloud-ready | No paid APIs")


# ---------------------------------------------------------------------------
# Operating Intelligence Workflow overlay
# ---------------------------------------------------------------------------

def operating_actionability_label(row):
    """More operational action labels for daily team usage."""
    score = investment_priority_score(row)
    text = compact_text_blob(row).lower()
    recurrence = recurring_observation_count(row)
    use_case = classify_investment_use_case(row)
    confidence = confidence_label(row).lower()
    has_relationship = any(term in text for term in ["relationship", "partnership", "jv", "capital partner", "lender", "gp"])
    has_underwriting = any(term in text for term in ["refinanc", "recap", "maturity", "loan", "debt", "cap rate", "construction financing"])
    has_ic = score >= 85 and ("high" in confidence or "institutional" in confidence or recurrence >= 2)
    if has_ic:
        return "투자위 검토 가능"
    if score >= 82 and use_case in ["리파이낸싱 / Recap 기회", "부실 / 지연 프로젝트 관찰", "개발 부지 / 프로젝트 검토"]:
        return "실행 가능성 높음"
    if score >= 75:
        return "즉시 검토"
    if has_relationship and score >= 58:
        return "관계 구축 권장"
    if has_underwriting and score >= 55:
        return "underwriting 준비"
    if score >= 50:
        return "우선 검토"
    if score >= 30:
        return "검토 필요"
    return "단순 모니터링"


def operating_action_badge(row):
    label = operating_actionability_label(row)
    palette = {
        "투자위 검토 가능": ("#7f1d1d", "#fee2e2", "#fecaca"),
        "실행 가능성 높음": ("#991b1b", "#fee2e2", "#fecaca"),
        "즉시 검토": ("#92400e", "#fef3c7", "#fde68a"),
        "관계 구축 권장": ("#1e3a8a", "#dbeafe", "#bfdbfe"),
        "underwriting 준비": ("#065f46", "#d1fae5", "#a7f3d0"),
        "우선 검토": ("#4338ca", "#e0e7ff", "#c7d2fe"),
        "검토 필요": ("#475569", "#f1f5f9", "#cbd5e1"),
        "단순 모니터링": ("#52525b", "#f4f4f5", "#d4d4d8"),
    }
    color, background, border = palette.get(label, ("#334155", "#f1f5f9", "#cbd5e1"))
    return badge(label, color=color, background=background, border=border)


def suggested_owner_type(row):
    owners = suggest_team_owner(row)
    if "재무" in owners:
        return "capital markets"
    if "개발" in owners or "인허가" in owners or "현지" in owners:
        return "development"
    if "투자" in owners:
        return "investment"
    if "경영진" in owners:
        return "executive review"
    return "strategy"


def operating_why_now(row):
    label = operating_actionability_label(row)
    use_case = classify_investment_use_case(row)
    recurrence = recurring_observation_count(row)
    if label in ["투자위 검토 가능", "실행 가능성 높음", "즉시 검토"]:
        return "점수와 신뢰도, 반복 관찰 또는 전략 적합성이 높아 오늘 우선순위에 올릴 만합니다."
    if label == "관계 구축 권장":
        return "GP / lender / capital partner 반복 신호가 있어 관계 구축 후보로 분류할 필요가 있습니다."
    if label == "underwriting 준비":
        return "자금조달, 만기, cap rate, construction financing 관련 입력값 점검이 필요합니다."
    if recurrence >= 2:
        return "동일 또는 유사 신호가 반복되어 단발성 뉴스보다 추세 가능성이 있습니다."
    return f"{use_case} 관점에서 다음 run까지 방향성을 확인해야 합니다."


def operating_strategic_impact(row):
    use_case = classify_investment_use_case(row)
    if use_case == "리파이낸싱 / Recap 기회":
        return "recap / preferred equity / JV 구조 검토와 debt sensitivity에 영향을 줄 수 있습니다."
    if use_case == "GP 파트너십 검토":
        return "Woomi의 GP partnership map과 관계 구축 우선순위에 영향을 줄 수 있습니다."
    if use_case == "LA 인허가 모니터링":
        return "LA site strategy, entitlement precedent, density incentive 판단에 영향을 줄 수 있습니다."
    if use_case == "부실 / 지연 프로젝트 관찰":
        return "distressed acquisition, rescue capital, stalled project sourcing 가능성에 영향을 줄 수 있습니다."
    if use_case == "개발 부지 / 프로젝트 검토":
        return "project timing, site control, construction readiness 판단에 영향을 줄 수 있습니다."
    return "전략 watchlist의 conviction 축적과 시장 방향성 판단에 영향을 줄 수 있습니다."


def top_operating_items(shared, filters=None, limit=8):
    rows = candidate_priority_rows(shared, filters or {}, limit=limit * 2)
    if rows.empty:
        return rows
    rows = rows.copy()
    rows["_operating_score"] = rows.apply(lambda r: investment_priority_score(r.to_dict()) + min(10, recurring_observation_count(r.to_dict()) * 2), axis=1)
    rows["_operating_label"] = rows.apply(lambda r: operating_actionability_label(r.to_dict()), axis=1)
    priority_order = {
        "투자위 검토 가능": 8,
        "실행 가능성 높음": 7,
        "즉시 검토": 6,
        "관계 구축 권장": 5,
        "underwriting 준비": 4,
        "우선 검토": 3,
        "검토 필요": 2,
        "단순 모니터링": 1,
    }
    rows["_label_rank"] = rows["_operating_label"].map(priority_order).fillna(0)
    return rows.sort_values(["_label_rank", "_operating_score"], ascending=False).head(limit)


def render_daily_operating_priorities(shared, filters=None):
    st.markdown("### 오늘 팀 우선 실행 사항")
    rows = top_operating_items(shared, filters, limit=4 if not is_detail_mode() else 6)
    if rows.empty:
        st.info("오늘 우선 실행 항목을 만들 충분한 데이터가 없습니다.")
        return
    for index, (_, row) in enumerate(rows.iterrows(), start=1):
        item = row.to_dict()
        render_badges([
            operating_action_badge(item),
            score_badge(investment_priority_score(item)),
            owner_badge(item),
        ])
        st.markdown(f"**{index}. {truncate_text(get_title(item), 92)}**")
        st.write(f"**왜 지금:** {operating_why_now(item)}")
        st.write(f"**전략적 영향:** {operating_strategic_impact(item)}")
        st.write(f"**추천 owner type:** {suggested_owner_type(item)}")
        st.write(f"**다음 조치:** {ko_recommended_action(item)}")
        st.divider()


def change_detection_items(shared, filters=None):
    observations = build_market_regime_observations(shared, filters, limit=6)
    relationships = build_relationship_intelligence(shared, filters, limit=5)
    combined = combined_reasoning_rows(shared, filters)
    items = []
    for obs in observations[:4]:
        momentum = strategic_momentum_label(obs["score"], obs["supporting_count"])
        if obs["score"] >= 70:
            direction = "강화"
        elif obs["supporting_count"] <= 5:
            direction = "초기 포착"
        else:
            direction = "관찰 지속"
        items.append({
            "title": obs["title"],
            "direction": direction,
            "momentum": momentum,
            "summary": f"{obs['supporting_count']}개 근거로 {obs['focus']} 관련 관찰이 이어지고 있습니다.",
        })
    for rel in relationships[:2]:
        items.append({
            "title": rel["title"],
            "direction": "관계 반복",
            "momentum": strategic_momentum_label(rel["score"], 3),
            "summary": f"{rel['pattern']} 흐름이 있어 relationship map 업데이트가 필요합니다.",
        })
    early = what_could_matter_next(shared, filters)
    if early:
        items.append({
            "title": "emerging theme",
            "direction": "신규 / 저빈도",
            "momentum": "초기 포착",
            "summary": early[0],
        })
    return items[:7]


def render_change_detection(shared, filters=None):
    st.markdown("### 최근 변화 감지")
    items = change_detection_items(shared, filters)
    if not is_detail_mode():
        items = items[:4]
    if not items:
        st.info("최근 변화 감지에 사용할 반복 관찰이 아직 제한적입니다.")
        return
    for item in items:
        render_badges([
            badge(item["direction"], color="#1e3a8a", background="#dbeafe", border="#bfdbfe"),
            badge(item["momentum"], color="#065f46", background="#d1fae5", border="#a7f3d0"),
        ])
        st.markdown(f"**{item['title']}**")
        st.write(item["summary"])
        st.divider()


def weekly_change_summary(shared, filters=None):
    observations = build_market_regime_observations(shared, filters, limit=5)
    top_items = top_operating_items(shared, filters, limit=5)
    rel = build_relationship_intelligence(shared, filters, limit=3)
    biggest_dev = observations[0]["title"] if observations else "반복 관찰 축적"
    biggest_opp = "확인 필요"
    biggest_risk = "확인 필요"
    if not top_items.empty:
        opp_rows = rows_matching_keywords(top_items, ["opportunity", "jv", "recap", "acquisition", "development"])
        risk_rows = rows_matching_keywords(top_items, ["risk", "distress", "stalled", "refinancing", "maturity", "default"])
        if not opp_rows.empty:
            biggest_opp = get_title(opp_rows.iloc[0].to_dict())
        if not risk_rows.empty:
            biggest_risk = get_title(risk_rows.iloc[0].to_dict())
    return [
        ("가장 큰 신규 변화", biggest_dev),
        ("가장 큰 기회 후보", truncate_text(biggest_opp, 120)),
        ("가장 큰 리스크 후보", truncate_text(biggest_risk, 120)),
        ("시장 행동 변화", observations[1]["title"] if len(observations) > 1 else "추가 run 필요"),
        ("자본 흐름 변화", next((obs["title"] for obs in observations if "자본" in obs["title"] or "리파이낸싱" in obs["title"]), "대주 / GP 반복 관찰 필요")),
        ("관계 트렌드", rel[0]["title"] if rel else "관계 반복 신호 추가 확인 필요"),
    ]


def render_weekly_change_summary(shared, filters=None):
    st.markdown("### 이번 주 변화 요약")
    for label, value in weekly_change_summary(shared, filters):
        st.markdown(f"**{label}** · {value}")


def pipeline_stage(row):
    label = operating_actionability_label(row)
    text = compact_text_blob(row).lower()
    if label in ["투자위 검토 가능"]:
        return "potential IC discussion"
    if label in ["실행 가능성 높음", "즉시 검토"]:
        return "serious review"
    if "underwriting" in label or any(term in text for term in ["cap rate", "loan", "debt", "unit", "dollar", "financing"]):
        return "preliminary underwriting"
    if label == "관계 구축 권장":
        return "relationship forming"
    if label in ["우선 검토", "검토 필요"]:
        return "active monitoring"
    if any(term in text for term in ["execution", "construction", "delivery", "permit issued", "approved"]):
        return "execution watch"
    return "early observation"


def watchlist_tier(row):
    score = investment_priority_score(row)
    recurrence = recurring_observation_count(row)
    label = operating_actionability_label(row)
    if score >= 78 or label in ["투자위 검토 가능", "실행 가능성 높음", "즉시 검토"]:
        return "Tier 1 Immediate Focus"
    if score >= 55 or recurrence >= 2 or label in ["관계 구축 권장", "underwriting 준비", "우선 검토"]:
        return "Tier 2 Active Monitoring"
    return "Tier 3 Long-Term Observation"


def render_investment_pipeline_status(shared, filters=None):
    st.markdown("### 투자 Pipeline 상태")
    rows = top_operating_items(shared, filters, limit=6 if not is_detail_mode() else 10)
    if rows.empty:
        st.info("투자 Pipeline 상태를 만들 후보가 없습니다.")
        return
    grouped = {}
    for _, row in rows.iterrows():
        item = row.to_dict()
        grouped.setdefault(pipeline_stage(item), []).append(item)
    for stage, items in grouped.items():
        st.markdown(f"**{stage}**")
        for item in items[:3]:
            st.markdown(f"- {truncate_text(get_title(item), 90)} · {get_market(item) or '시장 미확인'} · {operating_actionability_label(item)}")
        st.divider()


def render_watchlist_tiers(shared, filters=None):
    st.markdown("### 전략 Watchlist Tier")
    rows = top_operating_items(shared, filters, limit=6 if not is_detail_mode() else 12)
    if rows.empty:
        st.info("Watchlist tier 후보가 없습니다.")
        return
    tiers = {
        "Tier 1 Immediate Focus": [],
        "Tier 2 Active Monitoring": [],
        "Tier 3 Long-Term Observation": [],
    }
    for _, row in rows.iterrows():
        item = row.to_dict()
        tiers[watchlist_tier(item)].append(item)
    for tier, items in tiers.items():
        if not items:
            continue
        st.markdown(f"**{tier}**")
        for item in items[:4]:
            st.markdown(f"- {truncate_text(get_title(item), 90)} · {operating_actionability_label(item)} · {suggested_owner_type(item)}")
        st.divider()


def escalation_items(shared, filters=None):
    rows = top_operating_items(shared, filters, limit=8)
    if rows.empty:
        return []
    escalation = []
    for _, row in rows.iterrows():
        item = row.to_dict()
        text = compact_text_blob(item).lower()
        score = investment_priority_score(item)
        if score >= 82 and any(term in text for term in [
            "refinanc", "maturity", "distress", "stalled", "default", "recap",
            "entitlement", "ceqa", "lender", "capital", "construction financing",
        ]):
            escalation.append(item)
    return escalation[:5]


def render_escalation_logic(shared, filters=None):
    st.markdown("### 경영진 Escalation 필요")
    items = escalation_items(shared, filters)
    if not items:
        st.info("현재 경영진 escalation이 필요한 강한 항목은 제한적입니다.")
        return
    for item in items[:3 if not is_detail_mode() else 5]:
        render_badges([operating_action_badge(item), score_badge(investment_priority_score(item)), owner_badge(item)])
        st.markdown(f"**{truncate_text(get_title(item), 100)}**")
        st.write(f"Escalation 이유: {operating_why_now(item)}")
        st.write(f"관리 포인트: {operating_strategic_impact(item)}")
        st.divider()


def render_team_workflow(shared, filters=None):
    st.markdown("### 팀 Workflow")
    rows = top_operating_items(shared, filters, limit=8 if not is_detail_mode() else 12)
    if rows.empty:
        st.info("팀 workflow를 만들 우선 항목이 없습니다.")
        return
    groups = {"투자팀": [], "전략팀": [], "자본시장팀": [], "개발관리": [], "경영진": []}
    for _, row in rows.iterrows():
        item = row.to_dict()
        owner = suggested_owner_type(item)
        if owner == "investment":
            groups["투자팀"].append(item)
        elif owner == "capital markets":
            groups["자본시장팀"].append(item)
        elif owner == "development":
            groups["개발관리"].append(item)
        elif owner == "executive review":
            groups["경영진"].append(item)
        else:
            groups["전략팀"].append(item)
    for team, items in groups.items():
        if not items:
            continue
        st.markdown(f"**{team}**")
        for item in items[:3]:
            st.markdown(f"- {truncate_text(get_title(item), 92)}")
            st.caption(f"{operating_why_now(item)} · 다음 조치: {ko_recommended_action(item)}")
        st.divider()


def render_relationship_development_tracking(shared, filters=None):
    st.markdown("### 관계 구축 진행 상황")
    targets = relationship_priority_targets(shared, filters, limit=3 if not is_detail_mode() else 5)
    if not targets:
        st.info("관계 구축 진행 상황을 만들 반복 관계 신호가 제한적입니다.")
        return
    for target in targets:
        timing = "이번 주 접촉 후보" if target["score"] >= 75 else "다음 전략회의 전 업데이트"
        render_badges([conviction_badge(target["score"]), badge(timing, color="#1e3a8a", background="#dbeafe", border="#bfdbfe")])
        st.markdown(f"**{target['name']}**")
        st.write(f"전략 가치: {target['angle']}")
        st.write(f"관련 시장: {target['market']} · 반복 근거: {target['count']}개")
        st.write(f"추천 outreach timing: {timing}")
        st.divider()


def page_operating_workflow(shared, filters):
    st.subheader("Operating Workflow / 팀 실행 관리")
    st.caption("오늘 실행할 일, escalation, pipeline, 팀별 workflow를 한 화면에서 봅니다.")
    render_daily_operating_priorities(shared, filters)
    render_change_detection(shared, filters)
    render_weekly_change_summary(shared, filters)
    render_team_workflow(shared, filters)
    render_escalation_logic(shared, filters)
    render_investment_pipeline_status(shared, filters)
    render_watchlist_tiers(shared, filters)
    render_relationship_development_tracking(shared, filters)
    if is_detail_mode():
        render_cross_signal_reasoning(shared, filters, limit=5)
        render_expandable_table("운영 우선순위 원천 데이터", top_operating_items(shared, filters, limit=20), FILES["dashboard_cards"])


def page_executive_briefing(shared, filters):
    """Operating-first executive workflow."""
    st.subheader("경영진 브리핑")
    st.caption("오늘 실행할 항목과 전략 해석을 먼저 보여주는 운영형 브리핑입니다.")

    cards = apply_filters(shared["cards"], filters)
    priority_rows = candidate_priority_rows(shared, filters, limit=8)

    safe_render_section("오늘 팀 우선 실행 사항", render_daily_operating_priorities, shared, filters)
    safe_render_section("오늘의 전략 해석", render_daily_strategic_narrative, shared, filters)
    safe_render_section("최근 변화 감지", render_change_detection, shared, filters)
    safe_render_section("이번 주 변화 요약", render_weekly_change_summary, shared, filters)
    safe_render_section("시장 체제 변화", render_regime_observations, shared, filters, limit=3)
    safe_render_section("시장 Timing 해석", render_market_timing_interpretation, shared, filters)
    safe_render_section("경영진 Escalation 필요", render_escalation_logic, shared, filters)

    st.markdown("### 투자 판단 프레임")
    top_row = None
    if cards.empty is False:
        top_row = sort_by_score(cards, ["card_score"]).iloc[0].to_dict()
    if priority_rows.empty and top_row:
        priority_rows = pd.DataFrame([top_row])
    render_investment_decision_framework(priority_rows, shared)

    safe_render_section("우선 관계 구축 대상", render_relationship_priority_targets, shared, filters)
    safe_render_section("투자 Pipeline 상태", render_investment_pipeline_status, shared, filters)
    safe_render_section("전략 Watchlist Tier", render_watchlist_tiers, shared, filters)
    safe_render_section("향후 관찰 포인트", render_forward_outlook, shared, filters)

    st.markdown("### 주요 기회 및 리스크")
    ko_signal_section("투자 기회", apply_filters(shared["opportunities"], filters), shared, ["opportunity_score"], FILES["opportunities"], limit=3)
    ko_signal_section("리스크 모니터링", apply_filters(shared["distress"], filters), shared, ["distress_score"], FILES["distress"], limit=3)

    render_ic_prep_preview(priority_rows)

    if is_detail_mode():
        safe_render_section("팀 Workflow", render_team_workflow, shared, filters)
        safe_render_section("관계 구축 진행 상황", render_relationship_development_tracking, shared, filters)
        safe_render_section("다음 단계에서 중요해질 가능성", render_what_could_matter_next, shared, filters)
        render_expandable_table("상세 데이터", priority_rows if not priority_rows.empty else cards, FILES["dashboard_cards"])


def legacy_main_09():
    """Run the operating intelligence workflow platform."""
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("투자팀 운영 인텔리전스 플랫폼")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드"], key="view_mode")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "팀 Workflow": page_operating_workflow,
        "전략 Narrative": page_strategic_narrative,
        "체제 / 교차 시그널": page_regime_reasoning,
        "투자검토 메모": page_investment_committee_prep,
        "시장 인텔리전스": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California 전략": page_la_california_strategy,
        "GP / 자본 관계": page_gp_capital_relationships,
        "시스템 / 파이프라인": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"],
        shared["watchlists"],
        shared["high_confidence"],
        shared["opportunities"],
        shared["distress"],
        shared["la_assets"],
        shared["la_entitlement"],
        shared["la_lifecycle"],
        shared["la_persistent_assets"],
        shared["gp_watchlist"],
        shared["institutional_relationships"],
        shared["relationship_graph"],
        shared["historical_memory"],
        shared["persistent_asset_memory"],
        shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"최근 실행: {summary.get('run_timestamp', '실행 데이터 없음')}")
    if is_detail_mode():
        kpi_strip(shared)
    else:
        cols = st.columns(3)
        with cols[0]:
            render_compact_metric("기관급 검토 항목", int(as_number(summary.get("high_confidence_signals", 0))))
        with cols[1]:
            render_compact_metric("주요 기회", int(as_number(summary.get("opportunity_count", 0))))
        with cols[2]:
            render_compact_metric("LA 관찰 항목", int(as_number(summary.get("la_asset_watch_count", 0))))
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | 운영 Workflow 및 투자 인텔리전스 | Streamlit Cloud-ready | No paid APIs")


# ---------------------------------------------------------------------------
# Relationship Intelligence and Partner Targeting overlay
# ---------------------------------------------------------------------------

def normalize_firm_name(value):
    text = str(value or "").strip()
    if not text or text.lower() == "nan":
        return ""
    return text.replace("→", "->").strip()


def firm_type_from_row(row, firm_name=""):
    text = compact_text_blob(row).lower() + " " + firm_name.lower()
    if any(term in text for term in ["fannie mae", "freddie mac", "lender", "loan", "debt", "berkadia", "greystone", "walker", "jll", "cbre"]):
        return "lender / debt provider"
    if any(term in text for term in ["blackstone", "brookfield", "capital", "institutional", "fund", "reit", "equity"]):
        return "capital partner"
    if any(term in text for term in ["broker", "advisor", "capital markets"]):
        return "broker / advisor"
    if any(term in text for term in ["entitlement", "local", "planning", "permit", "los angeles", "california"]):
        return "local sponsor / developer"
    return "GP / developer"


def relationship_score_components(row, firm_name=""):
    text = compact_text_blob(row).lower() + " " + firm_name.lower()
    base = investment_priority_score(row)
    repeat = min(100, recurring_observation_count(row) * 18)
    capital = 80 if any(term in text for term in ["capital", "lender", "loan", "debt", "fannie mae", "freddie mac", "recap", "refinanc"]) else 35
    development = 80 if any(term in text for term in ["developer", "gp", "project", "asset", "construction", "entitlement", "permit"]) else 35
    la = 90 if row_has_la_california_relevance(row) else 30
    opportunity = 85 if any(term in text for term in ["opportunity", "jv", "partnership", "acquisition", "distress", "recap"]) else 35
    strategic_fit = min(100, int((base * 0.45) + (repeat * 0.2) + (capital * 0.15) + (development * 0.1) + (la * 0.1)))
    priority_score = min(100, int((strategic_fit * 0.35) + (capital * 0.18) + (development * 0.15) + (la * 0.14) + (repeat * 0.1) + (opportunity * 0.08)))
    return {
        "strategic_fit": strategic_fit,
        "capital_relevance": capital,
        "development_relevance": development,
        "la_california_relevance": la,
        "repeat_appearance": repeat,
        "opportunity_linkage": opportunity,
        "relationship_priority_score": priority_score,
    }


def relationship_priority_label(score):
    if score >= 78:
        return "Tier 1 관계 구축 후보"
    if score >= 58:
        return "Tier 2 지속 모니터링"
    if score >= 38:
        return "Tier 3 참고 관찰"
    return "Low Priority"


def outreach_angle(row, firm_name=""):
    text = compact_text_blob(row).lower() + " " + firm_name.lower()
    if any(term in text for term in ["refinanc", "recap", "maturity", "loan", "debt"]):
        return "refinancing / recap opportunity monitoring"
    if any(term in text for term in ["entitlement", "permit", "zoning", "ceqa", "density bonus", "los angeles", "california"]):
        return "LA entitlement precedent discussion"
    if any(term in text for term in ["jv", "joint venture", "partnership"]):
        return "JV / partnership discussion"
    if any(term in text for term in ["btr", "single-family rental", "sfr"]):
        return "BTR / SFR platform discussion"
    if any(term in text for term in ["affordable", "lihtc", "workforce", "mixed-income"]):
        return "affordable housing pipeline discussion"
    if any(term in text for term in ["capital", "institutional", "blackstone", "brookfield"]):
        return "capital markets relationship mapping"
    return "local sponsor intelligence gathering"


def extract_relationship_firm(row):
    candidates = [
        "firm_name", "canonical_gp_name", "gp_or_developer", "gp_name",
        "lender_or_debt_provider", "lender_or_capital_provider", "capital_partner",
        "source_entity", "target_entity", "institutional_partner", "item_name",
    ]
    for field in candidates:
        value = normalize_firm_name(row.get(field, ""))
        if value and value.lower() not in ["unknown", "other / unknown", "national / other", "general residential"]:
            if value.lower() in ["untitled signal", "general project signal", "los angeles", "california", "new york", "sun belt"]:
                continue
            return value
    title = normalize_firm_name(get_title(row))
    known_firms = [
        "Berkadia", "CBRE", "JLL", "Greystone", "Fannie Mae", "Freddie Mac",
        "Blackstone", "Brookfield", "Kennedy Wilson", "Greystar", "Related",
        "Hines", "Wood Partners", "AvalonBay", "Essex", "Crescent Communities",
        "Walker & Dunlop", "Northmarq", "Newmark", "Toll Brothers",
    ]
    title_lower = title.lower()
    for firm in known_firms:
        if firm.lower() in title_lower:
            return firm
    return ""


def build_partner_targets(shared, filters=None, limit=8):
    frames = []
    for key, label in [
        ("relationship_persistence", "relationship_persistence.csv"),
        ("relationship_graph", "relationship_graph.csv"),
        ("institutional_relationships", "institutional_relationships.csv"),
        ("gp_watchlist", "gp_watchlist.csv"),
        ("opportunities", "opportunity_radar.csv"),
        ("distress", "distress_watchlist.csv"),
        ("la_assets", "la_asset_watch.csv"),
        ("la_entitlement", "la_entitlement_watch.csv"),
        ("cards", "dashboard_cards.csv"),
    ]:
        df = apply_filters(shared.get(key, pd.DataFrame()), filters or {})
        if df.empty:
            continue
        temp = df.head(50).copy()
        temp["_source_layer"] = label
        frames.append(temp)
    if not frames:
        return []
    combined = pd.concat(frames, ignore_index=True, sort=False)
    target_map = {}
    for _, row in combined.iterrows():
        item = row.to_dict()
        firm = extract_relationship_firm(item)
        if not firm or len(firm) < 2:
            continue
        components = relationship_score_components(item, firm)
        score = components["relationship_priority_score"]
        existing = target_map.get(firm)
        if not existing or score > existing["score"]:
            target_map[firm] = {
                "firm": firm,
                "firm_type": firm_type_from_row(item, firm),
                "market": get_market(item) or "시장 미확인",
                "sector": get_sector(item) or "섹터 미확인",
                "score": score,
                "components": components,
                "row": item,
                "evidence_count": max(1, recurring_observation_count(item)),
                "source_layers": {item.get("_source_layer", "")},
            }
        else:
            existing["evidence_count"] += max(1, recurring_observation_count(item) or 1)
            existing["source_layers"].add(item.get("_source_layer", ""))
            existing["score"] = min(100, existing["score"] + 2)
    targets = list(target_map.values())
    for target in targets:
        target["priority_label"] = relationship_priority_label(target["score"])
        target["outreach_angle"] = outreach_angle(target["row"], target["firm"])
        target["why"] = relationship_why_matters(target)
        target["woomi_angle"] = relationship_woomi_angle(target)
    targets.sort(key=lambda item: (item["score"], item["evidence_count"]), reverse=True)
    return targets[:limit]


def relationship_why_matters(target):
    firm_type = target["firm_type"]
    if "lender" in firm_type:
        return "대주 / debt provider 반복 신호는 refinancing, construction loan, recap 가능성 판단에 중요합니다."
    if "capital" in firm_type:
        return "기관 자본 또는 capital partner 움직임은 가격 발견과 GP 관계 구축 우선순위를 보여줍니다."
    if "local" in firm_type:
        return "현지 sponsor / developer 신호는 LA entitlement precedent와 site strategy에 직접 연결됩니다."
    return "GP / developer 반복 등장은 partnership 후보, 경쟁 구도, 개발 실행력 판단에 유용합니다."


def relationship_woomi_angle(target):
    if target["components"]["la_california_relevance"] >= 70:
        return "LA / California 개발전략과 현지 sponsor map에 우선 반영"
    if target["components"]["capital_relevance"] >= 70:
        return "자본시장 관계 맵과 refinancing / recap opportunity watch에 반영"
    if target["components"]["opportunity_linkage"] >= 70:
        return "opportunity-linked relationship review 및 JV 가능성 검토"
    return "전략 watchlist에 등록하고 반복 등장 여부 확인"


def render_relationship_scorecard(target):
    c = target["components"]
    render_badges([
        badge(target["priority_label"], color="#7f1d1d" if target["score"] >= 78 else "#1e3a8a", background="#fee2e2" if target["score"] >= 78 else "#dbeafe", border="#fecaca" if target["score"] >= 78 else "#bfdbfe"),
        conviction_badge(target["score"]),
        badge(target["firm_type"], color="#334155", background="#f1f5f9", border="#cbd5e1"),
    ])
    st.markdown(f"**{target['firm']}**")
    st.write(f"시장 / 섹터: {target['market']} · {target['sector']}")
    st.write(f"반복 관찰: {target['evidence_count']}개 · Outreach angle: {target['outreach_angle']}")
    st.write(f"왜 중요한가: {target['why']}")
    st.write(f"Woomi angle: {target['woomi_angle']}")
    st.write("관계 Scorecard")
    st.caption(
        f"전략 적합도 {c['strategic_fit']} · 자본시장 연결성 {c['capital_relevance']} · "
        f"개발 파트너 적합도 {c['development_relevance']} · LA 전략 관련성 {c['la_california_relevance']} · "
        f"반복 관찰 {c['repeat_appearance']} · 기회 연결성 {c['opportunity_linkage']}"
    )


def render_partner_targeting(shared, filters=None, limit=5):
    st.markdown("### 우선 파트너 / 관계 구축 대상")
    targets = build_partner_targets(shared, filters, limit=limit)
    if not targets:
        st.info("우선 파트너 후보를 만들 관계 신호가 제한적입니다.")
        return
    for target in targets:
        render_relationship_scorecard(target)
        if is_detail_mode():
            render_relationship_history_for_target(shared, target)
        st.divider()


def render_who_should_we_meet(shared, filters=None):
    st.markdown("### 이번 주 관계 구축 후보")
    targets = build_partner_targets(shared, filters, limit=5)
    if not targets:
        st.info("이번 주 우선 접촉 후보가 없습니다.")
        return
    for target in targets[:5]:
        owner = "자본시장팀" if "lender" in target["firm_type"] or "capital" in target["firm_type"] else "전략팀"
        if target["components"]["la_california_relevance"] >= 70:
            owner = "미국 현지팀 / 개발관리"
        st.markdown(f"- **{target['firm']}** · {target['priority_label']} · {owner}")
        st.caption(f"왜 지금: {target['why']} / 다음 조치: {target['outreach_angle']}")


def render_la_relationship_focus(shared, filters=None):
    st.markdown("### LA / California 관계 타깃")
    targets = [t for t in build_partner_targets(shared, filters, limit=12) if t["components"]["la_california_relevance"] >= 60 or "california" in t["market"].lower() or "los angeles" in t["market"].lower()]
    if not targets:
        st.info("LA / California 관련 관계 타깃이 제한적입니다.")
        return
    for target in targets[:4 if not is_detail_mode() else 8]:
        render_badges([badge("LA 전략 관련성", color="#1e3a8a", background="#dbeafe", border="#bfdbfe"), conviction_badge(target["score"])])
        st.markdown(f"**{target['firm']}** · {target['firm_type']}")
        st.write(f"{target['woomi_angle']} · {target['outreach_angle']}")
        st.divider()


def relationship_map_rows(shared, filters=None, limit=20):
    rows = []
    for key in ["relationship_graph", "relationship_persistence"]:
        df = apply_filters(shared.get(key, pd.DataFrame()), filters or {})
        if df.empty:
            continue
        for _, row in df.head(80).iterrows():
            item = row.to_dict()
            source = get_first(item, ["canonical_source_entity", "source_entity", "gp_or_developer", "canonical_gp_name"], "")
            target = get_first(item, ["canonical_target_entity", "target_entity", "lender_or_debt_provider", "capital_partner"], "")
            if not source and not target:
                continue
            relation = get_first(item, ["relationship_type", "strategic_relationship_label", "capital_alignment_label"], "General Association")
            market = get_market(item)
            sector = get_sector(item)
            score = int(as_number(get_first(item, ["relationship_strength_score", "relationship_persistence_score", "institutional_relationship_score"], get_score(item)), 0))
            rows.append({
                "관계": f"{source or 'Unknown'} → {target or market or sector or 'Unknown'}",
                "유형": relation,
                "시장": market,
                "섹터": sector,
                "점수": score,
                "소스": key,
            })
    rows = sorted(rows, key=lambda item: item["점수"], reverse=True)
    return pd.DataFrame(rows[:limit])


def render_relationship_map_view(shared, filters=None):
    st.markdown("### Relationship Map View")
    df = relationship_map_rows(shared, filters, limit=10 if not is_detail_mode() else 30)
    if df.empty:
        st.info("관계 맵을 만들 relationship edge가 제한적입니다.")
        return
    st.dataframe(df, use_container_width=True, hide_index=True)


def related_rows_for_firm(shared, firm):
    firm_lower = firm.lower()
    sections = []
    for key, label in [
        ("opportunities", "관련 기회"),
        ("distress", "관련 리스크"),
        ("la_assets", "LA 자산"),
        ("la_entitlement", "LA 인허가"),
        ("la_lifecycle", "개발 단계"),
        ("relationship_graph", "관계 그래프"),
        ("relationship_persistence", "관계 지속성"),
        ("historical_memory", "과거 관찰"),
        ("gp_watchlist", "GP watchlist"),
    ]:
        df = current_shared_data().get(key, pd.DataFrame())
        if df.empty:
            continue
        matched = df[df.apply(lambda row: firm_lower in compact_text_blob(row.to_dict()).lower(), axis=1)].head(5)
        if not matched.empty:
            sections.append((label, matched))
    return sections


def render_relationship_history_for_target(shared, target):
    st.markdown("#### 관계 이력 / 관련 근거")
    sections = related_rows_for_firm(shared, target["firm"])
    if not sections:
        st.caption("관련 history row가 제한적입니다.")
        return
    for label, df in sections[:5]:
        render_expandable_table(label, df, None)


def page_partner_targeting(shared, filters):
    st.subheader("Relationship Intelligence / Partner Targeting")
    st.caption("GP, lender, capital partner, local sponsor 관계를 우선순위화합니다.")
    render_who_should_we_meet(shared, filters)
    render_partner_targeting(shared, filters, limit=5 if not is_detail_mode() else 10)
    render_la_relationship_focus(shared, filters)
    if is_detail_mode():
        render_relationship_map_view(shared, filters)


def render_team_workflow(shared, filters=None):
    st.markdown("### 팀 Workflow")
    rows = top_operating_items(shared, filters, limit=8 if not is_detail_mode() else 12)
    targets = build_partner_targets(shared, filters, limit=6)
    if rows.empty and not targets:
        st.info("팀 workflow를 만들 우선 항목이 없습니다.")
        return
    groups = {"투자팀": [], "전략팀": [], "자본시장팀": [], "개발관리": [], "경영진": []}
    for _, row in rows.iterrows():
        item = row.to_dict()
        owner = suggested_owner_type(item)
        if owner == "investment":
            groups["투자팀"].append((truncate_text(get_title(item), 92), operating_why_now(item), ko_recommended_action(item)))
        elif owner == "capital markets":
            groups["자본시장팀"].append((truncate_text(get_title(item), 92), operating_why_now(item), ko_recommended_action(item)))
        elif owner == "development":
            groups["개발관리"].append((truncate_text(get_title(item), 92), operating_why_now(item), ko_recommended_action(item)))
        elif owner == "executive review":
            groups["경영진"].append((truncate_text(get_title(item), 92), operating_why_now(item), ko_recommended_action(item)))
        else:
            groups["전략팀"].append((truncate_text(get_title(item), 92), operating_why_now(item), ko_recommended_action(item)))
    for target in targets[:5]:
        task = (target["firm"], target["why"], target["outreach_angle"])
        if "lender" in target["firm_type"] or "capital" in target["firm_type"]:
            groups["자본시장팀"].append(task)
        elif target["components"]["la_california_relevance"] >= 70:
            groups["개발관리"].append(task)
        elif target["priority_label"].startswith("Tier 1"):
            groups["경영진"].append(task)
        else:
            groups["전략팀"].append(task)
    if targets:
        groups["전략팀"].insert(0, ("GP / capital partner mapping", "반복 관계와 opportunity linkage가 있는 firms를 relationship map에 반영", "우선 관계 구축 후보 업데이트"))
        groups["투자팀"].insert(0, ("opportunity-linked relationship review", "투자 기회와 연결된 GP / lender를 underwriting context와 함께 검토", "상위 기회 후보별 sponsor / lender 확인"))
        groups["자본시장팀"].insert(0, ("lender / debt provider mapping", "반복 lender 활동과 refinancing stress를 함께 추적", "대주별 market exposure 정리"))
        groups["개발관리"].insert(0, ("local sponsor / entitlement consultant monitoring", "LA entitlement-heavy sponsor와 local approval precedent를 확인", "LA 관계 타깃 후속 확인"))
        groups["경영진"].insert(0, ("Tier 1 relationship candidates", "전략 중요도가 높은 관계 구축 후보를 선별", "다음 경영진 미팅 안건화"))
    for team, items in groups.items():
        if not items:
            continue
        st.markdown(f"**{team}**")
        for title, why, action in items[:4]:
            st.markdown(f"- {title}")
            st.caption(f"{why} · 다음 조치: {action}")
        st.divider()


def page_operating_workflow(shared, filters):
    st.subheader("Operating Workflow / 팀 실행 관리")
    st.caption("오늘 실행할 일, escalation, pipeline, 팀별 workflow, 관계 구축 후보를 한 화면에서 봅니다.")
    render_daily_operating_priorities(shared, filters)
    render_who_should_we_meet(shared, filters)
    render_team_workflow(shared, filters)
    render_change_detection(shared, filters)
    render_weekly_change_summary(shared, filters)
    render_escalation_logic(shared, filters)
    render_investment_pipeline_status(shared, filters)
    render_watchlist_tiers(shared, filters)
    render_relationship_development_tracking(shared, filters)
    if is_detail_mode():
        render_relationship_map_view(shared, filters)
        render_cross_signal_reasoning(shared, filters, limit=5)
        render_expandable_table("운영 우선순위 원천 데이터", top_operating_items(shared, filters, limit=20), FILES["dashboard_cards"])


def page_executive_briefing(shared, filters):
    """Executive briefing with partner targeting embedded."""
    st.subheader("경영진 브리핑")
    st.caption("오늘 실행할 항목, 전략 해석, 관계 구축 후보를 먼저 보여주는 운영형 브리핑입니다.")

    cards = apply_filters(shared["cards"], filters)
    priority_rows = candidate_priority_rows(shared, filters, limit=8)

    safe_render_section("오늘 팀 우선 실행 사항", render_daily_operating_priorities, shared, filters)
    safe_render_section("이번 주 관계 구축 후보", render_who_should_we_meet, shared, filters)
    safe_render_section("우선 파트너 / 관계 구축 대상", render_partner_targeting, shared, filters, limit=3)
    safe_render_section("LA / California 관계 타깃", render_la_relationship_focus, shared, filters)
    safe_render_section("오늘의 전략 해석", render_daily_strategic_narrative, shared, filters)
    safe_render_section("최근 변화 감지", render_change_detection, shared, filters)
    safe_render_section("이번 주 변화 요약", render_weekly_change_summary, shared, filters)
    safe_render_section("시장 체제 변화", render_regime_observations, shared, filters, limit=3)
    safe_render_section("시장 Timing 해석", render_market_timing_interpretation, shared, filters)
    safe_render_section("경영진 Escalation 필요", render_escalation_logic, shared, filters)

    st.markdown("### 투자 판단 프레임")
    top_row = None
    if cards.empty is False:
        top_row = sort_by_score(cards, ["card_score"]).iloc[0].to_dict()
    if priority_rows.empty and top_row:
        priority_rows = pd.DataFrame([top_row])
    render_investment_decision_framework(priority_rows, shared)

    safe_render_section("투자 Pipeline 상태", render_investment_pipeline_status, shared, filters)
    safe_render_section("전략 Watchlist Tier", render_watchlist_tiers, shared, filters)
    safe_render_section("향후 관찰 포인트", render_forward_outlook, shared, filters)

    st.markdown("### 주요 기회 및 리스크")
    ko_signal_section("투자 기회", apply_filters(shared["opportunities"], filters), shared, ["opportunity_score"], FILES["opportunities"], limit=3)
    ko_signal_section("리스크 모니터링", apply_filters(shared["distress"], filters), shared, ["distress_score"], FILES["distress"], limit=3)

    render_ic_prep_preview(priority_rows)

    if is_detail_mode():
        render_relationship_map_view(shared, filters)
        safe_render_section("팀 Workflow", render_team_workflow, shared, filters)
        safe_render_section("관계 구축 진행 상황", render_relationship_development_tracking, shared, filters)
        render_expandable_table("상세 데이터", priority_rows if not priority_rows.empty else cards, FILES["dashboard_cards"])


def legacy_main_10():
    """Run the relationship intelligence and operating workflow platform."""
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("관계 / 투자 운영 인텔리전스 플랫폼")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드"], key="view_mode")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "파트너 Targeting": page_partner_targeting,
        "팀 Workflow": page_operating_workflow,
        "전략 Narrative": page_strategic_narrative,
        "체제 / 교차 시그널": page_regime_reasoning,
        "투자검토 메모": page_investment_committee_prep,
        "시장 인텔리전스": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California 전략": page_la_california_strategy,
        "GP / 자본 관계": page_gp_capital_relationships,
        "시스템 / 파이프라인": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"],
        shared["watchlists"],
        shared["high_confidence"],
        shared["opportunities"],
        shared["distress"],
        shared["la_assets"],
        shared["la_entitlement"],
        shared["la_lifecycle"],
        shared["la_persistent_assets"],
        shared["gp_watchlist"],
        shared["institutional_relationships"],
        shared["relationship_graph"],
        shared["historical_memory"],
        shared["persistent_asset_memory"],
        shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"최근 실행: {summary.get('run_timestamp', '실행 데이터 없음')}")
    if is_detail_mode():
        kpi_strip(shared)
    else:
        cols = st.columns(3)
        with cols[0]:
            render_compact_metric("기관급 검토 항목", int(as_number(summary.get("high_confidence_signals", 0))))
        with cols[1]:
            render_compact_metric("주요 기회", int(as_number(summary.get("opportunity_count", 0))))
        with cols[2]:
            render_compact_metric("LA 관찰 항목", int(as_number(summary.get("la_asset_watch_count", 0))))
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | 관계 구축 및 투자 운영 인텔리전스 | Streamlit Cloud-ready | No paid APIs")


# ---------------------------------------------------------------------------
# Strategic Timing Intelligence and Conviction Memory overlay
# ---------------------------------------------------------------------------

def temporal_signal_count(row):
    """A compact recurrence proxy from whichever history fields are available."""
    return max(
        recurring_observation_count(row),
        int(as_number(get_first(row, ["observation_count", "repeat_interaction_count", "source_count"], 0), 0)),
    )


def conviction_memory_label(score, recurrence=0, momentum_text=""):
    text = str(momentum_text or "").lower()
    if any(term in text for term in ["accelerating", "rising", "strengthening", "improving", "progressing"]):
        return "conviction rising"
    if any(term in text for term in ["weakening", "fading", "dormant", "decreasing"]):
        return "conviction weakening"
    if score >= 80 and recurrence >= 3:
        return "structurally strengthening"
    if recurrence == 0 and score < 45:
        return "newly emerging"
    if score >= 45 and recurrence >= 1:
        return "conviction stable"
    return "fading observation" if score < 30 else "newly emerging"


def conviction_memory_badge(label):
    palette = {
        "structurally strengthening": ("#7f1d1d", "#fee2e2", "#fecaca"),
        "conviction rising": ("#92400e", "#fef3c7", "#fde68a"),
        "conviction stable": ("#166534", "#dcfce7", "#bbf7d0"),
        "newly emerging": ("#1e40af", "#dbeafe", "#bfdbfe"),
        "conviction weakening": ("#52525b", "#f4f4f5", "#d4d4d8"),
        "fading observation": ("#475569", "#f1f5f9", "#cbd5e1"),
    }
    color, background, border = palette.get(label, ("#334155", "#f1f5f9", "#cbd5e1"))
    return badge(label, color=color, background=background, border=border)


def execution_readiness(row):
    """Classify whether a signal is only being watched or nearing execution."""
    score = investment_priority_score(row)
    recurrence = temporal_signal_count(row)
    text = compact_text_blob(row).lower()
    relationship = any(term in text for term in ["relationship", "partnership", "jv", "capital partner", "lender"])
    timing = any(term in text for term in ["maturity", "delivery", "permit", "approved", "construction", "recap", "distress", "stalled"])
    if score >= 88 and timing:
        return "active execution watch"
    if score >= 78:
        return "execution preparation"
    if score >= 65 and any(term in text for term in ["loan", "debt", "cap rate", "refinanc", "unit", "$"]):
        return "preliminary underwriting"
    if relationship or recurrence >= 2:
        return "relationship preparation"
    if score >= 45:
        return "strategic monitoring"
    return "observation only"


def execution_readiness_badge(label):
    palette = {
        "active execution watch": ("#7f1d1d", "#fee2e2", "#fecaca"),
        "execution preparation": ("#92400e", "#fef3c7", "#fde68a"),
        "preliminary underwriting": ("#065f46", "#d1fae5", "#a7f3d0"),
        "relationship preparation": ("#1e3a8a", "#dbeafe", "#bfdbfe"),
        "strategic monitoring": ("#475569", "#f1f5f9", "#cbd5e1"),
        "observation only": ("#52525b", "#f4f4f5", "#d4d4d8"),
    }
    color, background, border = palette.get(label, ("#334155", "#f1f5f9", "#cbd5e1"))
    return badge(label, color=color, background=background, border=border)


def relationship_maturity(target):
    score = target.get("score", 0)
    count = target.get("evidence_count", 0)
    priority = target.get("priority_label", "")
    if score >= 85 and count >= 4:
        return "long-term strategic importance"
    if "Tier 1" in priority:
        return "execution-relevant"
    if score >= 65:
        return "high-priority target"
    if count >= 3:
        return "strategically relevant"
    if count >= 1:
        return "recurring awareness"
    return "early observation"


def timing_window_label(row_or_theme):
    text = compact_text_blob(row_or_theme).lower() if isinstance(row_or_theme, dict) else str(row_or_theme).lower()
    if any(term in text for term in ["recap", "recapitalization", "refinanc", "maturity", "bridge loan"]):
        return "recapitalization window"
    if any(term in text for term in ["distress", "stalled", "default", "foreclosure", "delayed"]):
        return "distress accumulation phase"
    if any(term in text for term in ["relationship", "partnership", "jv", "capital partner"]):
        return "relationship-building phase"
    if any(term in text for term in ["underwriting", "cap rate", "loan", "unit", "construction financing"]):
        return "underwriting preparation phase"
    if any(term in text for term in ["permit", "entitlement", "approved", "ceqa", "density bonus"]):
        return "entitlement accumulation phase"
    if any(term in text for term in ["blackstone", "brookfield", "institutional", "capital re-entry"]):
        return "institutional re-entry phase"
    if any(term in text for term in ["construction", "delivery", "lease-up", "opening"]):
        return "execution watch phase"
    return "early observation phase"


def timing_window_explanation(label):
    explanations = {
        "early observation phase": "아직 consensus가 형성되기 전의 초기 관찰 단계입니다. 반복 등장 여부를 확인해야 합니다.",
        "relationship-building phase": "관계 구축을 먼저 시작하면 기회가 명확해지기 전에 GP / lender map을 선점할 수 있습니다.",
        "underwriting preparation phase": "가격, debt terms, cap rate, unit economics를 사전에 준비해야 기회가 구체화될 때 빠르게 검토할 수 있습니다.",
        "execution watch phase": "프로젝트가 승인, 착공, delivery, lease-up 등 실행 단계로 이동할 가능성을 추적해야 합니다.",
        "recapitalization window": "만기와 refinancing 압박이 recap, preferred equity, JV gap 기회로 연결될 수 있습니다.",
        "distress accumulation phase": "지연, 부실, 대출 압박이 누적되면 discounted basis 또는 rescue capital 검토 가능성이 생깁니다.",
        "institutional re-entry phase": "기관 자본의 반복 움직임은 pricing discovery와 partner activity의 선행 신호일 수 있습니다.",
        "entitlement accumulation phase": "인허가 precedent가 축적되는 구간으로, LA / California site strategy에 활용할 비교사례가 생깁니다.",
    }
    return explanations.get(label, explanations["early observation phase"])


def conviction_memory_items(shared, filters=None, limit=6):
    items = []
    observations = build_market_regime_observations(shared, filters, limit=6)
    for obs in observations:
        label = conviction_memory_label(obs["score"], obs["supporting_count"], obs["title"])
        items.append({
            "title": obs["title"],
            "score": obs["score"],
            "count": obs["supporting_count"],
            "label": label,
            "why": f"{obs['supporting_count']}개 근거가 {obs['focus']} 관련 conviction을 형성하고 있습니다.",
        })
    for target in build_partner_targets(shared, filters, limit=4):
        label = conviction_memory_label(target["score"], target["evidence_count"], target["priority_label"])
        items.append({
            "title": target["firm"],
            "score": target["score"],
            "count": target["evidence_count"],
            "label": label,
            "why": f"{target['firm_type']} 관계가 {target['market']}에서 반복 관찰됩니다.",
        })
    items.sort(key=lambda item: (item["score"], item["count"]), reverse=True)
    return items[:limit]


def render_conviction_memory(shared, filters=None):
    st.markdown("### Conviction Memory / 신뢰도 추세")
    items = conviction_memory_items(shared, filters, limit=4 if not is_detail_mode() else 8)
    if not items:
        st.info("신뢰도 추세를 만들 반복 관찰이 제한적입니다.")
        return
    for item in items:
        render_badges([conviction_memory_badge(item["label"]), conviction_badge(item["score"]), badge(f"반복 {item['count']}개", color="#334155", background="#f1f5f9", border="#cbd5e1")])
        st.markdown(f"**{item['title']}**")
        st.write(item["why"])
        st.divider()


def timing_window_items(shared, filters=None):
    rows = top_operating_items(shared, filters, limit=6)
    items = []
    for _, row in rows.iterrows():
        data = row.to_dict()
        label = timing_window_label(data)
        items.append({
            "title": get_title(data),
            "label": label,
            "score": investment_priority_score(data),
            "prep": timing_window_explanation(label),
            "next": "다음 run에서 동일 firm / market / project가 반복되는지 확인하고, 관련 owner에게 follow-up 항목을 배정하십시오.",
            "row": data,
        })
    return items


def render_timing_windows(shared, filters=None):
    st.markdown("### 전략 Timing Window")
    items = timing_window_items(shared, filters)
    if not items:
        st.info("전략 timing window를 만들 우선 항목이 없습니다.")
        return
    for item in items[:3 if not is_detail_mode() else 6]:
        render_badges([badge(item["label"], color="#1e3a8a", background="#dbeafe", border="#bfdbfe"), conviction_badge(item["score"])])
        st.markdown(f"**{truncate_text(item['title'], 95)}**")
        st.write(f"왜 지금 중요한가: {item['prep']}")
        st.write(f"다음에 일어날 수 있는 일: {item['next']}")
        st.write(f"Woomi 준비: {operating_strategic_impact(item['row'])}")
        st.divider()


def render_market_cycle_interpretation(shared, filters=None):
    st.markdown("### 시장 Cycle 해석")
    phase, explanation, score = market_timing_phase(shared, filters)
    observations = build_market_regime_observations(shared, filters, limit=4)
    cycle_lines = [
        ("financing cycle", "리파이낸싱, maturity, lender activity가 cycle 판단의 핵심입니다."),
        ("development cycle", "착공, delivery, lease-up, stalled project가 개발 cycle을 보여줍니다."),
        ("capital cycle", "기관 자본과 GP 관계의 반복성이 capital cycle의 재정렬 여부를 보여줍니다."),
        ("entitlement cycle", "LA / California 승인, CEQA, density bonus 신호가 entitlement cycle을 보여줍니다."),
    ]
    render_insight_block(phase, explanation, badges=[conviction_badge(score)])
    for label, body in cycle_lines:
        related = [obs["title"] for obs in observations if any(term in obs["title"].lower() for term in label.split())]
        st.markdown(f"**{label}** · {body}")
        if related:
            st.caption(f"관련 테마: {', '.join(related[:2])}")


def render_execution_readiness(shared, filters=None):
    st.markdown("### 실행 준비도")
    rows = top_operating_items(shared, filters, limit=5 if not is_detail_mode() else 10)
    if rows.empty:
        st.info("실행 준비도 평가 후보가 없습니다.")
        return
    for _, row in rows.iterrows():
        data = row.to_dict()
        label = execution_readiness(data)
        render_badges([execution_readiness_badge(label), score_badge(investment_priority_score(data))])
        st.markdown(f"**{truncate_text(get_title(data), 95)}**")
        st.write(f"판단: {operating_why_now(data)}")
        st.divider()


def render_relationship_maturity(shared, filters=None):
    st.markdown("### 관계 성숙도")
    targets = build_partner_targets(shared, filters, limit=4 if not is_detail_mode() else 8)
    if not targets:
        st.info("관계 성숙도를 평가할 partner target이 제한적입니다.")
        return
    for target in targets:
        maturity = relationship_maturity(target)
        render_badges([badge(maturity, color="#1e3a8a", background="#dbeafe", border="#bfdbfe"), conviction_badge(target["score"])])
        st.markdown(f"**{target['firm']}** · {target['firm_type']}")
        st.write(f"전략 가치: {target['woomi_angle']} · Outreach: {target['outreach_angle']}")
        st.divider()


def momentum_theme_lists(shared, filters=None):
    observations = build_market_regime_observations(shared, filters, limit=8)
    gaining, fading = [], []
    for obs in observations:
        label = conviction_memory_label(obs["score"], obs["supporting_count"], obs["title"])
        entry = {
            "title": obs["title"],
            "score": obs["score"],
            "count": obs["supporting_count"],
            "label": label,
            "why": f"{obs['focus']} 관련 근거가 {obs['supporting_count']}개 축적되어 있습니다.",
            "implication": obs["woomi"],
        }
        if label in ["structurally strengthening", "conviction rising", "conviction stable"] and obs["score"] >= 55:
            gaining.append(entry)
        elif label in ["conviction weakening", "fading observation"] or obs["supporting_count"] <= 2:
            fading.append(entry)
    early = what_could_matter_next(shared, filters)
    for item in early[:2]:
        gaining.append({"title": item.split(":")[0], "score": 42, "count": 1, "label": "newly emerging", "why": item, "implication": "consensus 이전에 반복 여부를 추적할 후보입니다."})
    return gaining[:5], fading[:4]


def render_momentum_gaining(shared, filters=None):
    st.markdown("### Momentum 상승 테마")
    gaining, _ = momentum_theme_lists(shared, filters)
    if not gaining:
        st.info("상승 momentum으로 볼 테마가 제한적입니다.")
        return
    for item in gaining[:3 if not is_detail_mode() else 5]:
        render_badges([conviction_memory_badge(item["label"]), conviction_badge(item["score"])])
        st.markdown(f"**{item['title']}**")
        st.write(f"왜 중요한가: {item['why']}")
        st.write(f"전략적 시사점: {item['implication']}")
        st.divider()


def render_momentum_fading(shared, filters=None):
    st.markdown("### Momentum 약화 테마")
    _, fading = momentum_theme_lists(shared, filters)
    if not fading:
        st.caption("현재 명확한 momentum 약화 테마는 제한적입니다. 이는 강한 신호 위주로 해석하는 것이 적절하다는 뜻입니다.")
        return
    for item in fading[:3 if not is_detail_mode() else 4]:
        render_badges([conviction_memory_badge(item["label"]), conviction_badge(item["score"])])
        st.markdown(f"**{item['title']}**")
        st.write(item["why"])
        st.divider()


def render_womi_preparation(shared, filters=None):
    st.markdown("### 우미 준비 필요 사항")
    observations = build_market_regime_observations(shared, filters, limit=5)
    prep = []
    titles = " ".join(obs["title"] for obs in observations)
    if "리파이낸싱" in titles or "자본" in titles:
        prep.append(("recapitalization structuring capability", "리파이낸싱 압박과 recap 기회가 구체화되기 전에 capital stack, preferred equity, JV 구조 검토 역량을 준비해야 합니다."))
        prep.append(("lender mapping", "반복 lender와 agency financing 관계를 정리해 debt market read-through를 빠르게 확인해야 합니다."))
    if "인허가" in titles or "Affordable" in titles:
        prep.append(("entitlement expertise", "LA entitlement, CEQA, density bonus, affordable overlay 사례를 비교할 내부 기준이 필요합니다."))
        prep.append(("California policy tracking", "California 정책 변화와 local approval precedent를 site strategy에 연결해야 합니다."))
    prep.append(("relationship building", "기회가 명확해지기 전 반복 등장 GP / lender / local sponsor와 관계를 형성해야 합니다."))
    prep.append(("underwriting capability", "stress, concession, debt cost, delivery timing을 반영한 preliminary underwriting template를 준비해야 합니다."))
    seen = set()
    for title, body in prep:
        if title in seen:
            continue
        seen.add(title)
        st.markdown(f"- **{title}**: {body}")


def render_before_consensus(shared, filters=None):
    st.markdown("### Consensus 이전 관찰")
    items = what_could_matter_next(shared, filters)
    if not items:
        st.info("consensus 이전 관찰 후보가 제한적입니다.")
        return
    for item in items[:4 if not is_detail_mode() else 6]:
        st.markdown(f"- {item}")
    st.caption("목표는 빈도가 낮지만 전략적으로 중요한 패턴을 consensus 형성 전에 추적하는 것입니다.")


def render_temporal_comparison(shared, filters=None):
    st.markdown("### 최근 대비 변화")
    observations = build_market_regime_observations(shared, filters, limit=4)
    if not observations:
        st.info("최근 대비 변화를 판단할 관찰값이 제한적입니다.")
        return
    for obs in observations:
        label = conviction_memory_label(obs["score"], obs["supporting_count"], obs["title"])
        if obs["supporting_count"] >= 50:
            direction = "broadening"
        elif obs["score"] >= 70:
            direction = "accelerating"
        elif obs["supporting_count"] >= 10:
            direction = "stable"
        else:
            direction = "becoming concentrated"
        render_badges([badge(direction, color="#1e3a8a", background="#dbeafe", border="#bfdbfe"), conviction_memory_badge(label)])
        st.markdown(f"**{obs['title']}**")
        st.write(f"{obs['focus']} 관련 관찰이 {direction} 상태로 보입니다.")
        st.divider()


def page_timing_memory(shared, filters):
    st.subheader("Timing Intelligence / Conviction Memory")
    st.caption("시장 cycle, timing window, conviction 추세, 실행 준비도를 한 화면에서 봅니다.")
    render_temporal_comparison(shared, filters)
    render_timing_windows(shared, filters)
    render_market_cycle_interpretation(shared, filters)
    render_momentum_gaining(shared, filters)
    render_momentum_fading(shared, filters)
    render_conviction_memory(shared, filters)
    render_execution_readiness(shared, filters)
    render_relationship_maturity(shared, filters)
    render_before_consensus(shared, filters)
    render_womi_preparation(shared, filters)


def page_executive_briefing(shared, filters):
    """Timing-oriented executive operating briefing."""
    st.subheader("경영진 브리핑")
    st.caption("오늘 실행할 항목과 시간 기반 conviction 변화를 함께 보여주는 운영형 브리핑입니다.")

    cards = apply_filters(shared["cards"], filters)
    priority_rows = candidate_priority_rows(shared, filters, limit=8)

    safe_render_section("오늘 팀 우선 실행 사항", render_daily_operating_priorities, shared, filters)
    safe_render_section("오늘의 전략 해석", render_daily_strategic_narrative, shared, filters)
    safe_render_section("최근 대비 변화", render_temporal_comparison, shared, filters)
    safe_render_section("전략 Timing Window", render_timing_windows, shared, filters)
    safe_render_section("시장 Cycle 해석", render_market_cycle_interpretation, shared, filters)
    safe_render_section("Momentum 상승 테마", render_momentum_gaining, shared, filters)
    safe_render_section("Momentum 약화 테마", render_momentum_fading, shared, filters)
    safe_render_section("Conviction Memory", render_conviction_memory, shared, filters)
    safe_render_section("Consensus 이전 관찰", render_before_consensus, shared, filters)
    safe_render_section("우미 준비 필요 사항", render_womi_preparation, shared, filters)
    safe_render_section("관계 구축 우선순위", render_who_should_we_meet, shared, filters)

    st.markdown("### 투자 판단 프레임")
    top_row = None
    if cards.empty is False:
        top_row = sort_by_score(cards, ["card_score"]).iloc[0].to_dict()
    if priority_rows.empty and top_row:
        priority_rows = pd.DataFrame([top_row])
    render_investment_decision_framework(priority_rows, shared)

    safe_render_section("투자 Pipeline 상태", render_investment_pipeline_status, shared, filters)

    st.markdown("### 주요 기회 및 리스크")
    ko_signal_section("투자 기회", apply_filters(shared["opportunities"], filters), shared, ["opportunity_score"], FILES["opportunities"], limit=3)
    ko_signal_section("리스크 모니터링", apply_filters(shared["distress"], filters), shared, ["distress_score"], FILES["distress"], limit=3)

    render_ic_prep_preview(priority_rows)

    if is_detail_mode():
        safe_render_section("실행 준비도", render_execution_readiness, shared, filters)
        safe_render_section("관계 성숙도", render_relationship_maturity, shared, filters)
        render_relationship_map_view(shared, filters)
        render_expandable_table("상세 데이터", priority_rows if not priority_rows.empty else cards, FILES["dashboard_cards"])


def legacy_main_11():
    """Run the timing intelligence and conviction memory platform."""
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("Timing / Conviction 운영 인텔리전스")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드"], key="view_mode")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "Timing / Conviction": page_timing_memory,
        "파트너 Targeting": page_partner_targeting,
        "팀 Workflow": page_operating_workflow,
        "전략 Narrative": page_strategic_narrative,
        "체제 / 교차 시그널": page_regime_reasoning,
        "투자검토 메모": page_investment_committee_prep,
        "시장 인텔리전스": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California 전략": page_la_california_strategy,
        "GP / 자본 관계": page_gp_capital_relationships,
        "시스템 / 파이프라인": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"],
        shared["watchlists"],
        shared["high_confidence"],
        shared["opportunities"],
        shared["distress"],
        shared["la_assets"],
        shared["la_entitlement"],
        shared["la_lifecycle"],
        shared["la_persistent_assets"],
        shared["gp_watchlist"],
        shared["institutional_relationships"],
        shared["relationship_graph"],
        shared["historical_memory"],
        shared["persistent_asset_memory"],
        shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"최근 실행: {summary.get('run_timestamp', '실행 데이터 없음')}")
    if is_detail_mode():
        kpi_strip(shared)
    else:
        cols = st.columns(3)
        with cols[0]:
            render_compact_metric("기관급 검토 항목", int(as_number(summary.get("high_confidence_signals", 0))))
        with cols[1]:
            render_compact_metric("주요 기회", int(as_number(summary.get("opportunity_count", 0))))
        with cols[2]:
            render_compact_metric("LA 관찰 항목", int(as_number(summary.get("la_asset_watch_count", 0))))
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | Timing Intelligence & Conviction Memory | Streamlit Cloud-ready | No paid APIs")


# ---------------------------------------------------------------------------
# Decision Compression and Executive Signal Ranking overlay
# ---------------------------------------------------------------------------

def decision_identity_key(row):
    """Build a simple duplicate-suppression key for executive mode."""
    project = get_first(row, ["canonical_project_name", "project_or_deal_name", "related_project_or_deal", "canonical_asset_or_project_name"])
    firm = extract_relationship_firm(row) or get_gp(row) or get_lender(row)
    market = get_market(row)
    signal = classify_investment_use_case(row)
    if project:
        return f"project::{project}".lower()[:120]
    if firm and market:
        return f"firm-market::{firm}-{market}-{signal}".lower()[:120]
    title = get_title(row)
    return f"title::{title[:80]}".lower()


def executive_priority_score(row):
    """Compressed executive ranking score across mixed signal types."""
    base = investment_priority_score(row)
    score = base * 0.35
    label = operating_actionability_label(row)
    readiness = execution_readiness(row)
    recurrence = temporal_signal_count(row)
    text = compact_text_blob(row).lower()
    if label in ["투자위 검토 가능", "실행 가능성 높음"]:
        score += 18
    elif label in ["즉시 검토", "관계 구축 권장", "underwriting 준비"]:
        score += 12
    elif label == "우선 검토":
        score += 7
    if readiness in ["active execution watch", "execution preparation"]:
        score += 14
    elif readiness in ["preliminary underwriting", "relationship preparation"]:
        score += 9
    if row_has_la_california_relevance(row):
        score += 8
    if recurrence:
        score += min(12, recurrence * 3)
    if any(term in text for term in ["refinanc", "maturity", "distress", "recap", "construction financing", "entitlement", "ceqa"]):
        score += 8
    if any(term in text for term in ["blackstone", "brookfield", "fannie mae", "freddie mac", "cbre", "jll", "berkadia", "greystone"]):
        score += 5
    if "unknown" in text and base < 55:
        score -= 8
    return int(max(0, min(100, score)))


def executive_priority_label(score):
    if score >= 82:
        return "Top Executive Priority"
    if score >= 66:
        return "Priority Review"
    if score >= 48:
        return "Active Monitoring"
    if score >= 30:
        return "Background Monitoring"
    return "Deprioritized"


def executive_priority_badge(score):
    label = executive_priority_label(score)
    palette = {
        "Top Executive Priority": ("#7f1d1d", "#fee2e2", "#fecaca"),
        "Priority Review": ("#92400e", "#fef3c7", "#fde68a"),
        "Active Monitoring": ("#1e40af", "#dbeafe", "#bfdbfe"),
        "Background Monitoring": ("#475569", "#f1f5f9", "#cbd5e1"),
        "Deprioritized": ("#52525b", "#f4f4f5", "#d4d4d8"),
    }
    color, background, border = palette[label]
    return badge(label, color=color, background=background, border=border)


def executive_candidate_rows(shared, filters=None, detail=False, limit=40):
    frames = []
    for key, source in [
        ("cards", "dashboard_cards.csv"),
        ("high_confidence", "high_confidence_watchlist.csv"),
        ("opportunities", "opportunity_radar.csv"),
        ("distress", "distress_watchlist.csv"),
        ("la_assets", "la_asset_watch.csv"),
        ("la_entitlement", "la_entitlement_watch.csv"),
        ("gp_watchlist", "gp_watchlist.csv"),
        ("institutional_relationships", "institutional_relationships.csv"),
        ("relationship_graph", "relationship_graph.csv"),
    ]:
        df = apply_filters(shared.get(key, pd.DataFrame()), filters or {})
        if df.empty:
            continue
        temp = df.head(60).copy()
        temp["_source_layer"] = source
        frames.append(temp)
    if not frames:
        return pd.DataFrame()
    combined = pd.concat(frames, ignore_index=True, sort=False)
    combined["_executive_score"] = combined.apply(lambda r: executive_priority_score(r.to_dict()), axis=1)
    combined["_executive_label"] = combined["_executive_score"].apply(executive_priority_label)
    combined["_identity_key"] = combined.apply(lambda r: decision_identity_key(r.to_dict()), axis=1)
    combined = combined.sort_values("_executive_score", ascending=False)
    if not detail:
        combined = combined.drop_duplicates("_identity_key", keep="first")
        combined = combined[combined["_executive_label"].isin(["Top Executive Priority", "Priority Review", "Active Monitoring"])]
    return combined.head(limit)


def escalation_reasons(row):
    reasons = []
    score = executive_priority_score(row)
    text = compact_text_blob(row).lower()
    if score >= 82:
        reasons.append("high conviction")
    if temporal_signal_count(row) >= 2:
        reasons.append("strong recurrence")
    if any(term in text for term in ["capital", "lender", "loan", "debt", "institutional"]):
        reasons.append("large capital flow relevance")
    if any(term in text for term in ["refinanc", "maturity", "recap"]):
        reasons.append("refinancing pressure")
    if row_has_la_california_relevance(row):
        reasons.append("LA strategic relevance")
    if any(term in text for term in ["opportunity", "acquisition", "jv", "distress", "stalled"]):
        reasons.append("actionable opportunity")
    if classify_investment_use_case(row) == "GP 파트너십 검토" or "relationship" in text:
        reasons.append("relationship priority")
    window = timing_window_label(row)
    if window not in ["early observation phase"]:
        reasons.append(window)
    return reasons[:5] or ["decision relevance under monitoring"]


def render_only_three_today(shared, filters=None):
    st.markdown("### 오늘 반드시 볼 3가지")
    rows = executive_candidate_rows(shared, filters, detail=False, limit=3)
    if rows.empty:
        st.info("오늘 반드시 볼 상위 3개 항목이 없습니다.")
        return
    for index, (_, row) in enumerate(rows.iterrows(), start=1):
        item = row.to_dict()
        score = int(item.get("_executive_score", executive_priority_score(item)))
        render_badges([
            executive_priority_badge(score),
            operating_action_badge(item),
            execution_readiness_badge(execution_readiness(item)),
            signal_quality_badge(confidence_label(item)),
        ])
        st.markdown(f"**{index}. {truncate_text(get_title(item), 96)}**")
        st.write(f"**핵심 이유:** {operating_why_now(item)}")
        st.write(f"**우미 관점:** {ko_woomi_angle(item)}")
        st.write(f"**오늘 할 일:** {ko_recommended_action(item)}")
        st.caption(f"Owner: {suggested_owner_type(item)} · urgency: {operating_actionability_label(item)} · conviction score: {score}")
        st.divider()


def render_read_this_first(shared, filters=None):
    rows = executive_candidate_rows(shared, filters, detail=False, limit=1)
    if rows.empty:
        return
    item = rows.iloc[0].to_dict()
    st.markdown("### 먼저 확인할 사항")
    render_insight_block(
        "오늘 최우선 검토",
        f"{truncate_text(get_title(item), 100)}\n\n핵심 이유: {operating_why_now(item)}\n\n우미 관점: {ko_woomi_angle(item)}\n\n오늘 할 일: {ko_recommended_action(item)}",
        badges=[executive_priority_badge(executive_priority_score(item)), owner_badge(item)],
    )


def render_escalation_criteria(shared, filters=None):
    st.markdown("### 경영진 보고 기준")
    rows = executive_candidate_rows(shared, filters, detail=False, limit=8)
    rows = rows[rows["_executive_label"].isin(["Top Executive Priority", "Priority Review"])] if not rows.empty else rows
    if rows.empty:
        st.info("현재 경영진 보고 기준을 충족하는 항목은 제한적입니다.")
        return
    for _, row in rows.head(4 if not is_detail_mode() else 8).iterrows():
        item = row.to_dict()
        st.markdown(f"**{truncate_text(get_title(item), 92)}**")
        st.write("Escalation 기준: " + ", ".join(escalation_reasons(item)))
        st.divider()


def render_monitoring_bucket(shared, filters=None):
    st.markdown("### 모니터링 유지 항목")
    rows = executive_candidate_rows(shared, filters, detail=True, limit=30)
    if rows.empty:
        st.info("모니터링 유지 항목이 없습니다.")
        return
    monitoring = rows[rows["_executive_label"].isin(["Active Monitoring", "Background Monitoring"])]
    if monitoring.empty:
        st.caption("상위 항목이 대부분 우선 검토 또는 경영진 검토 대상으로 분류되었습니다.")
        return
    for _, row in monitoring.head(5 if not is_detail_mode() else 12).iterrows():
        item = row.to_dict()
        st.markdown(f"- {truncate_text(get_title(item), 95)} · {item['_executive_label']} · {classify_investment_use_case(item)}")


def render_low_conviction_bucket(shared, filters=None):
    if not is_detail_mode():
        return
    st.markdown("### 낮은 우선순위 / 참고 항목")
    rows = executive_candidate_rows(shared, filters, detail=True, limit=60)
    if rows.empty:
        st.info("참고 항목이 없습니다.")
        return
    low = rows[rows["_executive_label"].isin(["Background Monitoring", "Deprioritized"])]
    if low.empty:
        st.caption("현재 낮은 우선순위 항목이 제한적입니다.")
        return
    render_expandable_table("낮은 우선순위 후보", low.head(25), FILES["dashboard_cards"])


def render_priority_review_items(shared, filters=None):
    st.markdown("### 우선 검토 항목")
    rows = executive_candidate_rows(shared, filters, detail=False, limit=12)
    priority = rows[rows["_executive_label"].isin(["Top Executive Priority", "Priority Review"])] if not rows.empty else rows
    if priority.empty:
        st.info("우선 검토 항목이 없습니다.")
        return
    for _, row in priority.head(5 if not is_detail_mode() else 10).iterrows():
        item = row.to_dict()
        render_badges([executive_priority_badge(int(item["_executive_score"])), operating_action_badge(item)])
        st.markdown(f"**{truncate_text(get_title(item), 95)}**")
        st.write(f"{operating_why_now(item)} · {ko_recommended_action(item)}")
        st.divider()


def render_ic_ready_items(shared, filters=None):
    st.markdown("### 투자위 검토 가능 항목")
    rows = executive_candidate_rows(shared, filters, detail=False, limit=15)
    if rows.empty:
        st.info("투자위 검토 가능 항목이 없습니다.")
        return
    ic_rows = [row.to_dict() for _, row in rows.iterrows() if operating_actionability_label(row.to_dict()) == "투자위 검토 가능" or executive_priority_score(row.to_dict()) >= 86]
    if not ic_rows:
        st.caption("현재 투자위 검토 가능 수준까지 압축된 항목은 제한적입니다.")
        return
    for item in ic_rows[:4 if not is_detail_mode() else 8]:
        st.markdown(f"- **{truncate_text(get_title(item), 95)}** · {suggested_owner_type(item)} · {', '.join(escalation_reasons(item)[:3])}")


def render_decision_relationship_candidates(shared, filters=None):
    st.markdown("### 관계 구축 후보")
    targets = build_partner_targets(shared, filters, limit=3 if not is_detail_mode() else 8)
    if not targets:
        st.info("관계 구축 후보가 없습니다.")
        return
    for target in targets:
        st.markdown(f"- **{target['firm']}** · {target['priority_label']} · {target['outreach_angle']}")
        st.caption(target["woomi_angle"])


def render_decision_la_items(shared, filters=None):
    st.markdown("### LA 전략 항목")
    rows = executive_candidate_rows(shared, filters, detail=False, limit=20)
    if rows.empty:
        st.info("LA 전략 항목이 없습니다.")
        return
    la_rows = [row.to_dict() for _, row in rows.iterrows() if row_has_la_california_relevance(row.to_dict())]
    if not la_rows:
        st.caption("현재 상위 의사결정 항목 중 LA / California 항목은 제한적입니다.")
        return
    for item in la_rows[:3 if not is_detail_mode() else 8]:
        st.markdown(f"- **{truncate_text(get_title(item), 95)}** · {executive_priority_label(executive_priority_score(item))}")
        st.caption(ko_woomi_angle(item))


def page_decision_board(shared, filters):
    st.subheader("Decision Board / 의사결정 보드")
    st.caption("경영진과 투자팀이 오늘 볼 항목만 압축해 보여줍니다.")
    render_only_three_today(shared, filters)
    render_escalation_criteria(shared, filters)
    render_priority_review_items(shared, filters)
    render_monitoring_bucket(shared, filters)
    render_ic_ready_items(shared, filters)
    render_decision_relationship_candidates(shared, filters)
    render_decision_la_items(shared, filters)
    render_low_conviction_bucket(shared, filters)


def page_executive_briefing(shared, filters):
    """Compressed executive briefing."""
    st.subheader("경영진 브리핑")
    st.caption("오늘 의사결정에 필요한 항목만 먼저 보여주는 압축 브리핑입니다.")
    render_only_three_today(shared, filters)
    render_read_this_first(shared, filters)
    safe_render_section("경영진 보고 기준", render_escalation_criteria, shared, filters)
    safe_render_section("오늘 팀 우선 실행 사항", render_daily_operating_priorities, shared, filters)
    safe_render_section("최근 대비 변화", render_temporal_comparison, shared, filters)
    safe_render_section("전략 Timing Window", render_timing_windows, shared, filters)
    safe_render_section("Momentum 상승 테마", render_momentum_gaining, shared, filters)
    safe_render_section("Conviction Memory", render_conviction_memory, shared, filters)
    safe_render_section("관계 구축 우선순위", render_who_should_we_meet, shared, filters)
    safe_render_section("투자 Pipeline 상태", render_investment_pipeline_status, shared, filters)

    st.markdown("### 주요 기회 및 리스크")
    ko_signal_section("투자 기회", apply_filters(shared["opportunities"], filters), shared, ["opportunity_score"], FILES["opportunities"], limit=3)
    ko_signal_section("리스크 모니터링", apply_filters(shared["distress"], filters), shared, ["distress_score"], FILES["distress"], limit=3)

    priority_rows = executive_candidate_rows(shared, filters, detail=is_detail_mode(), limit=8)
    render_ic_prep_preview(priority_rows)
    render_monitoring_bucket(shared, filters)
    render_low_conviction_bucket(shared, filters)


def legacy_main_12():
    """Run the decision-compressed executive intelligence platform."""
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("Decision Board / 투자 운영 인텔리전스")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드"], key="view_mode")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "Decision Board": page_decision_board,
        "Timing / Conviction": page_timing_memory,
        "파트너 Targeting": page_partner_targeting,
        "팀 Workflow": page_operating_workflow,
        "전략 Narrative": page_strategic_narrative,
        "체제 / 교차 시그널": page_regime_reasoning,
        "투자검토 메모": page_investment_committee_prep,
        "시장 인텔리전스": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California 전략": page_la_california_strategy,
        "GP / 자본 관계": page_gp_capital_relationships,
        "시스템 / 파이프라인": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"],
        shared["watchlists"],
        shared["high_confidence"],
        shared["opportunities"],
        shared["distress"],
        shared["la_assets"],
        shared["la_entitlement"],
        shared["la_lifecycle"],
        shared["la_persistent_assets"],
        shared["gp_watchlist"],
        shared["institutional_relationships"],
        shared["relationship_graph"],
        shared["historical_memory"],
        shared["persistent_asset_memory"],
        shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"최근 실행: {summary.get('run_timestamp', '실행 데이터 없음')}")
    if is_detail_mode():
        kpi_strip(shared)
    else:
        cols = st.columns(3)
        with cols[0]:
            render_compact_metric("기관급 검토 항목", int(as_number(summary.get("high_confidence_signals", 0))))
        with cols[1]:
            render_compact_metric("주요 기회", int(as_number(summary.get("opportunity_count", 0))))
        with cols[2]:
            render_compact_metric("LA 관찰 항목", int(as_number(summary.get("la_asset_watch_count", 0))))
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | Decision Compression & Executive Signal Ranking | Streamlit Cloud-ready | No paid APIs")


# ---------------------------------------------------------------------------
# Investment Decision Engine overlay
# ---------------------------------------------------------------------------

def strategic_fit_label(row):
    text = compact_text_blob(row).lower()
    score = 0
    if row_has_la_california_relevance(row):
        score += 28
    if any(term in text for term in ["multifamily", "apartment", "affordable", "workforce"]):
        score += 18
    if any(term in text for term in ["btr", "single-family rental", "sfr", "office-to-residential", "adaptive reuse"]):
        score += 12
    if any(term in text for term in ["recap", "refinanc", "maturity", "construction loan", "debt"]):
        score += 16
    if any(term in text for term in ["jv", "joint venture", "partnership", "capital partner"]):
        score += 14
    if any(term in text for term in ["blackstone", "brookfield", "kennedy wilson", "greystar", "related", "hines", "cbre", "jll", "fannie mae", "freddie mac"]):
        score += 12
    if score >= 58:
        return "Core Strategic Fit"
    if score >= 38:
        return "Adjacent Strategic Fit"
    if score >= 22:
        return "Opportunistic"
    return "Low Strategic Fit"


def underwriting_readiness(row):
    text = compact_text_blob(row).lower()
    points = 0
    if get_market(row) and get_market(row).lower() not in ["unknown", "other / unknown", "market unknown"]:
        points += 18
    if get_gp(row) or extract_relationship_firm(row):
        points += 16
    if classify_investment_use_case(row) != "단순 모니터링":
        points += 12
    if any(term in text for term in ["loan", "debt", "$", "million", "financing", "refinanc", "cap rate"]):
        points += 18
    if any(term in text for term in ["entitlement", "permit", "approved", "ceqa", "zoning"]):
        points += 12
    if temporal_signal_count(row) >= 2:
        points += 12
    if any(term in text for term in ["unit", "units", "apartments", "homes", "square feet", "acres"]):
        points += 12
    if points >= 62:
        return "Ready for Preliminary UW"
    if points >= 38:
        return "Needs More Information"
    if points >= 20:
        return "Too Early"
    return "Monitoring Only"


def execution_blockers(row):
    text = compact_text_blob(row).lower()
    blockers = []
    def add(name, severity, reduce_by, monitor):
        blockers.append({"blocker": name, "severity": severity, "reduce_by": reduce_by, "monitor": monitor})
    if any(term in text for term in ["ceqa", "entitlement", "zoning", "permit", "appeal"]) and "approved" not in text:
        add("entitlement uncertainty", "High" if row_has_la_california_relevance(row) else "Medium", "확정 approval stage와 appeal risk 확인", "planning commission / permit update")
    if not (get_gp(row) or extract_relationship_firm(row)):
        add("unclear sponsor", "Medium", "sponsor / GP / owner 식별", "원문 기사와 project record")
    if any(term in text for term in ["refinanc", "maturity", "distress", "bridge loan", "floating"]):
        add("refinancing stress", "Medium", "loan maturity, debt basis, lender stance 확인", "maturity / recap news")
    if any(term in text for term in ["capital stack", "preferred equity", "rescue capital"]) or ("loan" not in text and "debt" in text):
        add("unclear capital stack", "Medium", "senior debt, pref equity, sponsor equity 구조 확인", "financing disclosure")
    if timing_window_label(row) == "early observation phase":
        add("timing mismatch", "Low", "반복 관찰과 trigger event 확인", "next run recurrence")
    if executive_priority_score(row) < 45:
        add("insufficient conviction", "Medium", "multi-source confirmation 확보", "source count / recurring evidence")
    if temporal_signal_count(row) == 0:
        add("weak recurring evidence", "Low", "동일 firm / project / market 재등장 확인", "historical memory")
    if any(term in text for term in ["construction", "conversion", "adaptive reuse", "urban infill"]):
        add("execution complexity", "Medium", "cost, schedule, permit, lease-up assumptions 점검", "lifecycle transition")
    if classify_investment_use_case(row) in ["GP 파트너십 검토", "리파이낸싱 / Recap 기회"] and not extract_relationship_firm(row):
        add("relationship gap", "Medium", "접촉 가능한 GP / lender / advisor 식별", "relationship graph")
    return blockers[:5]


def ic_readiness_score(row):
    score = executive_priority_score(row) * 0.28
    text = compact_text_blob(row).lower()
    score += min(14, temporal_signal_count(row) * 4)
    if execution_readiness(row) in ["active execution watch", "execution preparation"]:
        score += 14
    elif execution_readiness(row) in ["preliminary underwriting", "relationship preparation"]:
        score += 8
    if get_market(row) and "unknown" not in get_market(row).lower():
        score += 8
    if get_gp(row) or extract_relationship_firm(row):
        score += 8
    if any(term in text for term in ["loan", "debt", "financing", "refinanc", "$", "million"]):
        score += 8
    if timing_window_label(row) != "early observation phase":
        score += 8
    if strategic_fit_label(row) == "Core Strategic Fit":
        score += 8
    elif strategic_fit_label(row) == "Adjacent Strategic Fit":
        score += 4
    if any(term in text for term in ["institutional", "blackstone", "brookfield", "fannie mae", "freddie mac", "cbre", "jll"]):
        score += 6
    return int(max(0, min(100, score)))


def ic_readiness_label(score):
    if score >= 76:
        return "IC Discussion Ready"
    if score >= 55:
        return "Preliminary Screening"
    if score >= 32:
        return "Early Observation"
    return "Not IC Ready"


def investment_decision_label(row):
    ic_score = ic_readiness_score(row)
    uw = underwriting_readiness(row)
    fit = strategic_fit_label(row)
    readiness = execution_readiness(row)
    high_blocker = any(item["severity"] == "High" for item in execution_blockers(row))
    if ic_score >= 78 and uw == "Ready for Preliminary UW" and not high_blocker:
        return "Strong Candidate"
    if fit in ["Core Strategic Fit", "Adjacent Strategic Fit"] and readiness in ["relationship preparation", "preliminary underwriting"]:
        return "Early Strategic Interest"
    if timing_window_label(row) in ["early observation phase", "entitlement accumulation phase"] and ic_score >= 40:
        return "Monitor for Timing"
    if classify_investment_use_case(row) == "GP 파트너십 검토" or "relationship" in compact_text_blob(row).lower():
        return "Relationship First"
    if high_blocker:
        return "High Risk / Limited Visibility"
    return "Not Actionable Yet"


def decision_label_badge(label):
    palette = {
        "Strong Candidate": ("#7f1d1d", "#fee2e2", "#fecaca"),
        "Early Strategic Interest": ("#92400e", "#fef3c7", "#fde68a"),
        "Monitor for Timing": ("#1e40af", "#dbeafe", "#bfdbfe"),
        "Relationship First": ("#065f46", "#d1fae5", "#a7f3d0"),
        "High Risk / Limited Visibility": ("#991b1b", "#fee2e2", "#fecaca"),
        "Not Actionable Yet": ("#52525b", "#f4f4f5", "#d4d4d8"),
    }
    color, background, border = palette.get(label, ("#334155", "#f1f5f9", "#cbd5e1"))
    return badge(label, color=color, background=background, border=border)


def required_dd_items(row):
    items = [blocker["reduce_by"] for blocker in execution_blockers(row)[:3]]
    if underwriting_readiness(row) != "Ready for Preliminary UW":
        items.append("location, sponsor, financing terms, unit economics 보강")
    if strategic_fit_label(row) in ["Core Strategic Fit", "Adjacent Strategic Fit"]:
        items.append("Woomi strategy fit와 owner team 확인")
    if not items:
        items.append("원문, sponsor, debt terms, timing trigger 최종 확인")
    return items[:5]


def team_action_ownership(row):
    owner_type = suggested_owner_type(row)
    mapping = {
        "investment": "투자팀",
        "strategy": "전략팀",
        "capital markets": "자본시장팀",
        "development": "개발관리",
        "executive review": "경영진",
    }
    team = mapping.get(owner_type, "전략팀")
    urgency = operating_actionability_label(row)
    timeline = "오늘 / 이번 주" if urgency in ["투자위 검토 가능", "실행 가능성 높음", "즉시 검토"] else "다음 전략회의 전"
    return team, ko_recommended_action(row), urgency, timeline


def investment_pipeline_stage(row):
    label = investment_decision_label(row)
    ic_label = ic_readiness_label(ic_readiness_score(row))
    readiness = execution_readiness(row)
    if label == "Not Actionable Yet":
        return "Observation"
    if label == "Monitor for Timing":
        return "Strategic Monitoring"
    if label == "Relationship First":
        return "Relationship Building"
    if underwriting_readiness(row) == "Ready for Preliminary UW":
        return "Preliminary Underwriting"
    if label == "Strong Candidate" and ic_label != "IC Discussion Ready":
        return "Active Review"
    if ic_label == "IC Discussion Ready":
        return "IC Prep"
    if readiness == "active execution watch":
        return "Execution Watch"
    return "Strategic Monitoring"


def investment_decision_rows(shared, filters=None, detail=False, limit=20):
    rows = executive_candidate_rows(shared, filters, detail=detail, limit=60)
    if rows.empty:
        return rows
    rows = rows.copy()
    rows["_ic_readiness_score"] = rows.apply(lambda r: ic_readiness_score(r.to_dict()), axis=1)
    rows["_ic_readiness_label"] = rows["_ic_readiness_score"].apply(ic_readiness_label)
    rows["_underwriting_readiness"] = rows.apply(lambda r: underwriting_readiness(r.to_dict()), axis=1)
    rows["_investment_decision_label"] = rows.apply(lambda r: investment_decision_label(r.to_dict()), axis=1)
    rows["_strategic_fit"] = rows.apply(lambda r: strategic_fit_label(r.to_dict()), axis=1)
    rows["_pipeline_stage"] = rows.apply(lambda r: investment_pipeline_stage(r.to_dict()), axis=1)
    rows["_blocker_count"] = rows.apply(lambda r: len(execution_blockers(r.to_dict())), axis=1)
    rank_order = {
        "Strong Candidate": 6,
        "Early Strategic Interest": 5,
        "Relationship First": 4,
        "Monitor for Timing": 3,
        "High Risk / Limited Visibility": 2,
        "Not Actionable Yet": 1,
    }
    rows["_decision_rank"] = rows["_investment_decision_label"].map(rank_order).fillna(0)
    rows = rows.sort_values(["_decision_rank", "_ic_readiness_score", "_executive_score"], ascending=False)
    if not detail:
        rows = rows[~rows["_investment_decision_label"].isin(["Not Actionable Yet"])]
    return rows.head(limit)


def render_investment_decision_frame(row, expanded=False):
    item = row.to_dict() if hasattr(row, "to_dict") else row
    label = investment_decision_label(item)
    ic_score = ic_readiness_score(item)
    team, action, urgency, timeline = team_action_ownership(item)
    with st.expander(truncate_text(get_title(item), 95), expanded=expanded):
        render_badges([
            decision_label_badge(label),
            badge(ic_readiness_label(ic_score), color="#1e3a8a", background="#dbeafe", border="#bfdbfe"),
            execution_readiness_badge(execution_readiness(item)),
            badge(strategic_fit_label(item), color="#065f46", background="#d1fae5", border="#a7f3d0"),
        ])
        fields = [
            ("투자 적합성", label),
            ("실행 가능성", execution_readiness(item)),
            ("전략 적합성", strategic_fit_label(item)),
            ("자본시장 적합성", "높음" if any(term in compact_text_blob(item).lower() for term in ["loan", "debt", "capital", "refinanc", "recap"]) else "추가 확인 필요"),
            ("관계 가치", "관계 구축 선행 필요" if "relationship" in compact_text_blob(item).lower() or extract_relationship_firm(item) else "관련 firm 식별 필요"),
            ("시장 timing", f"{timing_window_label(item)} · {timing_window_explanation(timing_window_label(item))}"),
        ]
        for title, value in fields:
            st.markdown(f"**{title}**")
            st.write(value)
        st.markdown("**예상 리스크 / blocker**")
        blockers = execution_blockers(item)
        if blockers:
            for blocker in blockers:
                st.markdown(f"- {blocker['blocker']} ({blocker['severity']}): {blocker['reduce_by']} / monitor: {blocker['monitor']}")
        else:
            st.markdown("- 현재 구조화된 blocker는 제한적입니다.")
        st.markdown("**DD 필요사항**")
        for dd in required_dd_items(item):
            st.markdown(f"- {dd}")
        st.markdown("**우미 relevance / 실행 우선순위**")
        st.write(f"{ko_woomi_angle(item)} · owner: {team} · urgency: {urgency} · timeline: {timeline}")
        if is_detail_mode():
            render_evidence_block(item)


def render_ic_readiness(shared, filters=None):
    st.markdown("### IC 검토 가능 항목")
    rows = investment_decision_rows(shared, filters, detail=is_detail_mode(), limit=12)
    ready = rows[rows["_ic_readiness_label"].isin(["IC Discussion Ready", "Preliminary Screening"])] if not rows.empty else rows
    if ready.empty:
        st.info("현재 IC 검토 가능 수준의 항목은 제한적입니다.")
        return
    for _, row in ready.head(4 if not is_detail_mode() else 10).iterrows():
        item = row.to_dict()
        render_badges([badge(item["_ic_readiness_label"], color="#1e3a8a", background="#dbeafe", border="#bfdbfe"), score_badge(item["_ic_readiness_score"])])
        st.markdown(f"**{truncate_text(get_title(item), 95)}**")
        st.write(f"IC readiness: {item['_ic_readiness_score']} · stage: {item['_pipeline_stage']}")
        st.divider()


def render_underwriting_readiness(shared, filters=None):
    st.markdown("### Underwriting Readiness / 검토 준비도")
    rows = investment_decision_rows(shared, filters, detail=is_detail_mode(), limit=12)
    if rows.empty:
        st.info("검토 준비도 평가 후보가 없습니다.")
        return
    for _, row in rows.head(5 if not is_detail_mode() else 10).iterrows():
        item = row.to_dict()
        st.markdown(f"- **{truncate_text(get_title(item), 92)}** · {item['_underwriting_readiness']} · {item['_pipeline_stage']}")


def render_execution_blocker_analysis(shared, filters=None):
    st.markdown("### 실행 blocker 분석")
    rows = investment_decision_rows(shared, filters, detail=is_detail_mode(), limit=10)
    if rows.empty:
        st.info("blocker 분석 후보가 없습니다.")
        return
    for _, row in rows.head(4 if not is_detail_mode() else 8).iterrows():
        item = row.to_dict()
        st.markdown(f"**{truncate_text(get_title(item), 95)}**")
        blockers = execution_blockers(item)
        if not blockers:
            st.caption("주요 blocker 제한적")
        for blocker in blockers[:3]:
            st.markdown(f"- {blocker['blocker']} · {blocker['severity']} · reduce by: {blocker['reduce_by']}")
        st.divider()


def render_investment_memo_preview(shared, filters=None):
    st.markdown("### 투자 메모 초안")
    rows = investment_decision_rows(shared, filters, detail=False, limit=3)
    if rows.empty:
        st.info("투자 메모 초안을 만들 후보가 없습니다.")
        return
    for index, (_, row) in enumerate(rows.iterrows(), start=1):
        item = row.to_dict()
        with st.expander(f"Memo {index}: {truncate_text(get_title(item), 80)}", expanded=(index == 1)):
            memo_fields = [
                ("Opportunity summary", ko_executive_summary(item)),
                ("Why now", operating_why_now(item)),
                ("Strategic rationale", ko_woomi_angle(item)),
                ("Relationship angle", outreach_angle(item, extract_relationship_firm(item))),
                ("Capital markets angle", "refinancing / recap / debt sensitivity 확인" if any(term in compact_text_blob(item).lower() for term in ["loan", "debt", "refinanc", "recap"]) else "capital stack 추가 확인"),
                ("Execution path", investment_pipeline_stage(item)),
                ("Risks", "; ".join(risk_factors(item))),
                ("Required diligence", "; ".join(required_dd_items(item))),
                ("Recommended next step", ko_recommended_action(item)),
            ]
            for title, value in memo_fields:
                st.markdown(f"**{title}**")
                st.write(value)


def render_investment_pipeline_staging(shared, filters=None):
    st.markdown("### 투자 Pipeline Staging")
    rows = investment_decision_rows(shared, filters, detail=is_detail_mode(), limit=16)
    if rows.empty:
        st.info("pipeline staging 후보가 없습니다.")
        return
    for stage in ["Observation", "Strategic Monitoring", "Relationship Building", "Preliminary Underwriting", "Active Review", "IC Prep", "Execution Watch", "Archived"]:
        stage_rows = rows[rows["_pipeline_stage"] == stage]
        if stage_rows.empty:
            continue
        st.markdown(f"**{stage}**")
        for _, row in stage_rows.head(3).iterrows():
            item = row.to_dict()
            st.markdown(f"- {truncate_text(get_title(item), 90)} · {item['_investment_decision_label']} · {item['_ic_readiness_label']}")
        st.divider()


def page_investment_decision_center(shared, filters):
    st.subheader("Investment Decision Center / 투자 판단 센터")
    st.caption("투자 가능성, IC readiness, underwriting readiness, blocker, memo 초안을 한 화면에서 봅니다.")
    st.markdown("### 투자 검토 우선순위")
    rows = investment_decision_rows(shared, filters, detail=is_detail_mode(), limit=8)
    if rows.empty:
        st.info("투자 검토 우선순위 후보가 없습니다.")
    else:
        for index, (_, row) in enumerate(rows.head(5 if not is_detail_mode() else 8).iterrows(), start=1):
            render_investment_decision_frame(row.to_dict(), expanded=(index == 1))
    render_ic_readiness(shared, filters)
    render_underwriting_readiness(shared, filters)
    st.markdown("### 관계 구축 선행 항목")
    render_decision_relationship_candidates(shared, filters)
    st.markdown("### Timing 대기 항목")
    render_timing_windows(shared, filters)
    st.markdown("### High Risk 항목")
    render_execution_blocker_analysis(shared, filters)
    render_investment_memo_preview(shared, filters)
    render_investment_pipeline_staging(shared, filters)


def page_executive_briefing(shared, filters):
    st.subheader("경영진 브리핑")
    st.caption("투자 판단 가능성, IC readiness, blocker를 우선 보여주는 압축 브리핑입니다.")
    render_only_three_today(shared, filters)
    st.markdown("### 투자 판단 프레임")
    rows = investment_decision_rows(shared, filters, detail=False, limit=5)
    if rows.empty:
        st.info("투자 판단 후보가 없습니다.")
    else:
        for index, (_, row) in enumerate(rows.head(3).iterrows(), start=1):
            render_investment_decision_frame(row.to_dict(), expanded=(index == 1))
    safe_render_section("IC 검토 가능 항목", render_ic_readiness, shared, filters)
    safe_render_section("Underwriting Readiness", render_underwriting_readiness, shared, filters)
    safe_render_section("실행 blocker 분석", render_execution_blocker_analysis, shared, filters)
    safe_render_section("투자 Pipeline Staging", render_investment_pipeline_staging, shared, filters)
    safe_render_section("투자 메모 초안", render_investment_memo_preview, shared, filters)
    safe_render_section("관계 구축 우선순위", render_who_should_we_meet, shared, filters)
    safe_render_section("전략 Timing Window", render_timing_windows, shared, filters)
    st.markdown("### 주요 기회 및 리스크")
    ko_signal_section("투자 기회", apply_filters(shared["opportunities"], filters), shared, ["opportunity_score"], FILES["opportunities"], limit=3)
    ko_signal_section("리스크 모니터링", apply_filters(shared["distress"], filters), shared, ["distress_score"], FILES["distress"], limit=3)
    if is_detail_mode():
        render_low_conviction_bucket(shared, filters)


def legacy_main_13():
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("Investment Decision Engine")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드"], key="view_mode")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "투자 판단 센터": page_investment_decision_center,
        "Decision Board": page_decision_board,
        "Timing / Conviction": page_timing_memory,
        "파트너 Targeting": page_partner_targeting,
        "팀 Workflow": page_operating_workflow,
        "전략 Narrative": page_strategic_narrative,
        "체제 / 교차 시그널": page_regime_reasoning,
        "투자검토 메모": page_investment_committee_prep,
        "시장 인텔리전스": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California 전략": page_la_california_strategy,
        "GP / 자본 관계": page_gp_capital_relationships,
        "시스템 / 파이프라인": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"], shared["watchlists"], shared["high_confidence"],
        shared["opportunities"], shared["distress"], shared["la_assets"],
        shared["la_entitlement"], shared["la_lifecycle"], shared["la_persistent_assets"],
        shared["gp_watchlist"], shared["institutional_relationships"], shared["relationship_graph"],
        shared["historical_memory"], shared["persistent_asset_memory"], shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"최근 실행: {summary.get('run_timestamp', '실행 데이터 없음')}")
    if is_detail_mode():
        kpi_strip(shared)
    else:
        cols = st.columns(3)
        with cols[0]:
            render_compact_metric("기관급 검토 항목", int(as_number(summary.get("high_confidence_signals", 0))))
        with cols[1]:
            render_compact_metric("주요 기회", int(as_number(summary.get("opportunity_count", 0))))
        with cols[2]:
            render_compact_metric("LA 관찰 항목", int(as_number(summary.get("la_asset_watch_count", 0))))
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | Investment Decision Engine | Streamlit Cloud-ready | No paid APIs")


# ---------------------------------------------------------------------------
# Institutional Quality Refinement overlay
# ---------------------------------------------------------------------------

INSTITUTIONAL_LABELS = {
    "High Confidence": "Institutional Validation",
    "Institutional Grade": "기관투자자급 검토",
    "Signal": "시장 관찰",
    "Actionable": "검토 가능",
    "Momentum": "관심 확대",
    "Execution Watch": "실행 모니터링",
    "Strong Candidate": "우선 검토 가능",
    "Early Strategic Interest": "전략적 관심",
    "Monitor for Timing": "Timing 관찰",
    "Relationship First": "관계 구축 선행",
    "High Risk / Limited Visibility": "고위험 / 가시성 제한",
    "Not Actionable Yet": "추가 관찰 필요",
    "IC Discussion Ready": "투자위 논의 가능",
    "Preliminary Screening": "예비 검토",
    "Early Observation": "초기 관찰",
    "Not IC Ready": "투자위 전 단계",
    "Ready for Preliminary UW": "예비 UW 가능",
    "Needs More Information": "추가 정보 필요",
    "Too Early": "시기상조",
    "Monitoring Only": "모니터링",
    "Top Executive Priority": "경영진 최우선",
    "Priority Review": "우선 검토",
    "Active Monitoring": "집중 모니터링",
    "Background Monitoring": "배경 모니터링",
    "Deprioritized": "우선순위 낮음",
    "active execution watch": "실행 모니터링",
    "execution preparation": "실행 준비",
    "preliminary underwriting": "예비 UW",
    "relationship preparation": "관계 구축 준비",
    "strategic monitoring": "전략 모니터링",
    "observation only": "단순 관찰",
}


def institutional_label(value):
    text = str(value or "").strip()
    return INSTITUTIONAL_LABELS.get(text, text)


def quiet_badge(text, tone="neutral"):
    colors = {
        "high": ("#7f1d1d", "#fef2f2", "#fecaca"),
        "medium": ("#1e3a8a", "#eff6ff", "#bfdbfe"),
        "green": ("#14532d", "#f0fdf4", "#bbf7d0"),
        "neutral": ("#334155", "#f8fafc", "#cbd5e1"),
    }
    color, background, border = colors.get(tone, colors["neutral"])
    return badge(institutional_label(text), color=color, background=background, border=border)


def decision_label_badge(label):
    if label in ["Strong Candidate", "High Risk / Limited Visibility"]:
        return quiet_badge(label, "high")
    if label in ["Early Strategic Interest", "Relationship First"]:
        return quiet_badge(label, "medium")
    if label == "Monitor for Timing":
        return quiet_badge(label, "green")
    return quiet_badge(label, "neutral")


def executive_priority_badge(score):
    label = executive_priority_label(score)
    if label == "Top Executive Priority":
        return quiet_badge(label, "high")
    if label == "Priority Review":
        return quiet_badge(label, "medium")
    if label == "Active Monitoring":
        return quiet_badge(label, "green")
    return quiet_badge(label, "neutral")


def execution_readiness_badge(label):
    if label in ["active execution watch", "execution preparation"]:
        return quiet_badge(label, "high")
    if label in ["preliminary underwriting", "relationship preparation"]:
        return quiet_badge(label, "medium")
    if label == "strategic monitoring":
        return quiet_badge(label, "green")
    return quiet_badge(label, "neutral")


def decision_maturity_label(row):
    score = executive_priority_score(row)
    recurrence = temporal_signal_count(row)
    readiness = execution_readiness(row)
    fit = strategic_fit_label(row)
    if readiness in ["active execution watch", "execution preparation"] and score >= 78:
        return "Execution Candidate"
    if score >= 80 or fit == "Core Strategic Fit":
        return "Strategic Priority"
    if any(term in compact_text_blob(row).lower() for term in ["institutional", "blackstone", "brookfield", "fannie mae", "freddie mac", "cbre", "jll"]) and score >= 55:
        return "Institutional Attention"
    if recurrence >= 2 or score >= 45:
        return "Developing Theme"
    return "Emerging Observation"


def maturity_badge(row):
    label = decision_maturity_label(row)
    tone = "high" if label in ["Execution Candidate", "Strategic Priority"] else "medium" if label == "Institutional Attention" else "green" if label == "Developing Theme" else "neutral"
    return quiet_badge(label, tone)


def compressed_title(row):
    use_case = classify_investment_use_case(row)
    market = get_market(row)
    firm = extract_relationship_firm(row) or get_gp(row) or get_lender(row)
    if use_case == "리파이낸싱 / Recap 기회":
        return f"{market or '핵심 시장'} refinancing / recap 검토"
    if use_case == "LA 인허가 모니터링":
        return "LA / California entitlement 관찰"
    if use_case == "GP 파트너십 검토":
        return f"{firm or '주요 GP'} 관계 구축 검토"
    if use_case == "부실 / 지연 프로젝트 관찰":
        return f"{market or '핵심 시장'} distress / delay 관찰"
    if use_case == "개발 부지 / 프로젝트 검토":
        return f"{market or '핵심 시장'} 개발 프로젝트 검토"
    return f"{market or firm or '시장'} 전략 관찰"


def compressed_reason(row):
    label = investment_decision_label(row)
    window = timing_window_label(row)
    if label == "Strong Candidate":
        return "투자 판단에 필요한 전략 적합성, timing, 실행 준비도가 동시에 높아졌습니다."
    if label == "Early Strategic Interest":
        return "아직 즉시 투자안은 아니지만 Woomi 전략과 연결되는 초기 방향성이 확인됩니다."
    if label == "Relationship First":
        return "거래보다 관계 선점이 먼저 필요한 국면입니다."
    if "recapitalization" in window:
        return "자금 만기와 refinancing 압박이 검토 timing을 앞당기고 있습니다."
    if "entitlement" in window:
        return "인허가 precedent가 쌓이며 LA 개발전략의 비교 기준이 형성되고 있습니다."
    return "반복 관찰 여부에 따라 우선순위가 달라질 수 있는 항목입니다."


def short_woomi_implication(row):
    fit = strategic_fit_label(row)
    use_case = classify_investment_use_case(row)
    if fit == "Core Strategic Fit":
        return "Woomi의 미국 주거 전략과 직접 연결됩니다."
    if use_case == "리파이낸싱 / Recap 기회":
        return "recap 구조, debt sensitivity, GP 접점 검토가 필요합니다."
    if use_case == "LA 인허가 모니터링":
        return "LA site strategy와 entitlement 역량 축적에 중요합니다."
    if use_case == "GP 파트너십 검토":
        return "관계 맵에 올리고 반복 접점을 확인해야 합니다."
    return "전략 watchlist에서 timing과 반복성을 확인해야 합니다."


def compressed_executive_rows(shared, filters=None, limit=8):
    rows = investment_decision_rows(shared, filters, detail=is_detail_mode(), limit=30)
    if rows.empty:
        return rows
    rows = rows.copy()
    rows["_compressed_key"] = rows.apply(lambda r: f"{extract_relationship_firm(r.to_dict()) or get_market(r.to_dict())}-{classify_investment_use_case(r.to_dict())}", axis=1)
    if not is_detail_mode():
        rows = rows.drop_duplicates("_compressed_key", keep="first")
        rows = rows[~rows["_investment_decision_label"].isin(["Not Actionable Yet"])]
    return rows.head(limit)


def render_what_matters_today(shared, filters=None):
    st.markdown("### 오늘 실제 중요한 것")
    rows = compressed_executive_rows(shared, filters, limit=5)
    if rows.empty:
        st.info("오늘 압축해서 볼 핵심 항목이 없습니다.")
        return
    seen_markets = set()
    seen_firms = set()
    count = 0
    for _, row in rows.iterrows():
        item = row.to_dict()
        market = get_market(item)
        firm = extract_relationship_firm(item)
        if not is_detail_mode() and ((market and market in seen_markets) or (firm and firm in seen_firms)):
            continue
        seen_markets.add(market)
        seen_firms.add(firm)
        st.markdown(f"- **{compressed_title(item)}**: {compressed_reason(item)} {short_woomi_implication(item)}")
        count += 1
        if count >= 5:
            break


def render_investment_conviction_narrative(shared, filters=None):
    st.markdown("### 왜 중요도가 높아졌는가")
    rows = compressed_executive_rows(shared, filters, limit=3)
    if rows.empty:
        st.caption("중요도 상승을 설명할 충분한 항목이 없습니다.")
        return
    for _, row in rows.iterrows():
        item = row.to_dict()
        st.markdown(f"**{compressed_title(item)}**")
        st.write(
            f"{compressed_reason(item)} "
            f"현재 {institutional_label(investment_decision_label(item))} 단계이며, "
            f"{institutional_label(execution_readiness(item))} 관점에서 {short_woomi_implication(item)}"
        )


def render_market_regime_summary(shared, filters=None):
    st.markdown("### 시장 국면 요약")
    observations = build_market_regime_observations(shared, filters, limit=4)
    joined = " ".join(obs["title"] for obs in observations)
    financing = "refinancing 부담이 주요 변수입니다." if "리파이낸싱" in joined or "자본" in joined else "자금조달 환경은 추가 관찰이 필요합니다."
    appetite = "기관 자본은 선별적으로 움직이며 관계 맵 중요도가 커졌습니다." if "기관" in joined else "기관 risk appetite는 아직 명확히 확산되지 않았습니다."
    development = "개발 / 인허가 국면은 LA 및 affordable precedent 중심으로 축적되고 있습니다." if "인허가" in joined or "Affordable" in joined else "개발 cycle은 watchlist 중심으로 관리하는 단계입니다."
    st.write(f"**Financing environment:** {financing}")
    st.write(f"**Institutional risk appetite:** {appetite}")
    st.write(f"**Development / entitlement environment:** {development}")


def render_clean_investment_card(row, expanded=False):
    item = row.to_dict() if hasattr(row, "to_dict") else row
    with st.expander(compressed_title(item), expanded=expanded):
        render_badges([
            decision_label_badge(investment_decision_label(item)),
            maturity_badge(item),
            execution_readiness_badge(execution_readiness(item)),
        ])
        st.write(f"**핵심 판단:** {compressed_reason(item)}")
        st.write(f"**우미 관점:** {short_woomi_implication(item)}")
        st.write(f"**다음 조치:** {ko_recommended_action(item)}")
        blockers = execution_blockers(item)
        if blockers:
            st.write(f"**주요 blocker:** {blockers[0]['blocker']} · {blockers[0]['reduce_by']}")
        if is_detail_mode():
            render_investment_decision_frame(item, expanded=False)


def render_clean_team_workflow(shared, filters=None):
    st.markdown("### 팀별 실행 포인트")
    rows = compressed_executive_rows(shared, filters, limit=8)
    if rows.empty:
        return
    buckets = {"투자팀": [], "전략팀": [], "자본시장팀": [], "개발관리": [], "경영진": []}
    for _, row in rows.iterrows():
        item = row.to_dict()
        team, _, _, _ = team_action_ownership(item)
        buckets.setdefault(team, []).append(item)
    for team, items in buckets.items():
        if not items:
            continue
        st.markdown(f"**{team}**")
        for item in items[:2]:
            if team == "투자팀":
                action = "예비 투자 검토와 blocker 확인"
            elif team == "전략팀":
                action = "반복 테마와 관계 우선순위 업데이트"
            elif team == "자본시장팀":
                action = "refinancing / lender exposure 확인"
            elif team == "개발관리":
                action = "인허가 단계와 local sponsor 확인"
            else:
                action = "경영진 보고 필요성 판단"
            st.markdown(f"- {compressed_title(item)}: {action}")


def page_executive_briefing(shared, filters):
    st.subheader("오늘의 브리핑")
    st.caption("경영진이 3분 안에 읽을 수 있도록 의사결정 관련 항목만 압축했습니다.")
    render_what_matters_today(shared, filters)
    render_market_regime_summary(shared, filters)
    render_investment_conviction_narrative(shared, filters)

    st.markdown("### 오늘 우선 검토 사항")
    rows = compressed_executive_rows(shared, filters, limit=4)
    if rows.empty:
        st.info("우선 검토 항목이 없습니다.")
    else:
        for index, (_, row) in enumerate(rows.head(3).iterrows(), start=1):
            render_clean_investment_card(row.to_dict(), expanded=(index == 1))

    st.markdown("### 관계 구축 / 시장 timing")
    safe_render_section("관계 구축 / 시장 timing", render_who_should_we_meet, shared, filters)
    st.markdown("### 리스크 및 관찰 사항")
    safe_render_section("리스크 및 관찰 사항", render_execution_blocker_analysis, shared, filters)
    st.markdown("### 실행 준비 상태")
    safe_render_section("실행 준비 상태", render_underwriting_readiness, shared, filters)
    render_clean_team_workflow(shared, filters)

    if is_detail_mode():
        st.markdown("### 상세 분석")
        render_ic_readiness(shared, filters)
        render_investment_pipeline_staging(shared, filters)
        render_investment_memo_preview(shared, filters)
        render_low_conviction_bucket(shared, filters)


def page_investment_decision_center(shared, filters):
    st.subheader("Investment Decision Center / 투자 판단 센터")
    st.caption("투자 판단, IC readiness, UW readiness, blocker를 정리한 실무 검토 화면입니다.")
    render_what_matters_today(shared, filters)
    st.markdown("### 투자 검토 우선순위")
    rows = compressed_executive_rows(shared, filters, limit=8 if is_detail_mode() else 5)
    if rows.empty:
        st.info("투자 검토 우선순위 후보가 없습니다.")
    else:
        for index, (_, row) in enumerate(rows.iterrows(), start=1):
            render_clean_investment_card(row.to_dict(), expanded=(index == 1))
    render_ic_readiness(shared, filters)
    render_underwriting_readiness(shared, filters)
    render_execution_blocker_analysis(shared, filters)
    render_investment_memo_preview(shared, filters)
    if is_detail_mode():
        render_investment_pipeline_staging(shared, filters)


def app_header(shared):
    summary = latest_summary(shared["summary"])
    st.markdown(
        """
        <div class="workstation-card">
            <div class="section-kicker">US Residential Intelligence</div>
            <div class="signal-title">Institutional Investment Operating System</div>
            <p class="muted-label">Decision-first briefing · Relationship intelligence · Local CSV/Markdown pipeline</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns(3)
    with cols[0]:
        render_compact_metric("최근 실행", summary.get("run_timestamp", "실행 데이터 없음"))
    with cols[1]:
        render_compact_metric("상태", health_status(shared["health"]))
    with cols[2]:
        render_compact_metric("검토 후보", len(executive_candidate_rows(shared, {}, detail=False, limit=20)))


def legacy_main_14():
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("Institutional Investment OS")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드"], key="view_mode")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "투자 판단 센터": page_investment_decision_center,
        "Decision Board": page_decision_board,
        "Timing / Conviction": page_timing_memory,
        "파트너 Targeting": page_partner_targeting,
        "팀 Workflow": page_operating_workflow,
        "전략 Narrative": page_strategic_narrative,
        "체제 / 교차 시그널": page_regime_reasoning,
        "투자검토 메모": page_investment_committee_prep,
        "시장 인텔리전스": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California 전략": page_la_california_strategy,
        "GP / 자본 관계": page_gp_capital_relationships,
        "시스템 / 파이프라인": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"], shared["watchlists"], shared["high_confidence"],
        shared["opportunities"], shared["distress"], shared["la_assets"],
        shared["la_entitlement"], shared["la_lifecycle"], shared["la_persistent_assets"],
        shared["gp_watchlist"], shared["institutional_relationships"], shared["relationship_graph"],
        shared["historical_memory"], shared["persistent_asset_memory"], shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"최근 실행: {summary.get('run_timestamp', '실행 데이터 없음')}")
    if is_detail_mode():
        kpi_strip(shared)
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | Institutional Investment OS | Streamlit Cloud-ready")


# ---------------------------------------------------------------------------
# Daily Institutional Operating System refinement overlay
# ---------------------------------------------------------------------------

def concise_item_key(row):
    firm = extract_relationship_firm(row)
    market = get_market(row)
    use_case = classify_investment_use_case(row)
    return f"{firm or market}-{use_case}".lower()


def daily_brief_rows(shared, filters=None, limit=6):
    rows = compressed_executive_rows(shared, filters, limit=20)
    if rows.empty:
        return rows
    rows = rows.copy()
    rows["_daily_key"] = rows.apply(lambda r: concise_item_key(r.to_dict()), axis=1)
    rows = rows.drop_duplicates("_daily_key", keep="first")
    return rows.head(limit)


def market_temperature(shared, filters=None):
    rows = investment_decision_rows(shared, filters, detail=False, limit=12)
    if rows.empty:
        return "Defensive", "신호가 제한적이므로 방어적 모니터링이 적절합니다."
    avg_score = rows["_ic_readiness_score"].mean() if "_ic_readiness_score" in rows else 35
    capital_count = len(rows_matching_keywords(rows, ["capital", "lender", "loan", "refinanc", "recap", "fannie mae", "freddie mac"]))
    execution_count = len(rows[rows.apply(lambda r: execution_readiness(r.to_dict()) in ["execution preparation", "active execution watch"], axis=1)])
    relationship_count = len(rows_matching_keywords(rows, ["relationship", "partnership", "jv", "capital partner"]))
    heat = avg_score + capital_count * 3 + execution_count * 5 + relationship_count * 2
    if heat >= 85:
        return "Active Opportunity Environment", "자본시장 신호와 실행 준비도가 동시에 높아져 선별적 기회 검토가 가능한 환경입니다."
    if heat >= 65:
        return "Selective Expansion", "모든 시장이 열린 것은 아니지만 특정 관계와 시장에서 확장 검토 여지가 있습니다."
    if heat >= 45:
        return "Cautious Opportunity", "기회는 보이지만 underwriting, 관계, timing 확인이 선행되어야 합니다."
    return "Defensive", "리스크 확인과 watchlist 관리가 우선인 방어적 환경입니다."


def render_market_temperature(shared, filters=None):
    label, explanation = market_temperature(shared, filters)
    tone = "high" if label == "Active Opportunity Environment" else "medium" if label == "Selective Expansion" else "green" if label == "Cautious Opportunity" else "neutral"
    render_badges([quiet_badge(label, tone)])
    st.write(explanation)


def render_today_market_change(shared, filters=None):
    st.markdown("### 오늘 시장에서 실제 중요한 변화")
    render_market_temperature(shared, filters)
    rows = daily_brief_rows(shared, filters, limit=5)
    if rows.empty:
        st.info("오늘 압축해서 볼 시장 변화가 없습니다.")
        return
    for _, row in rows.head(4).iterrows():
        item = row.to_dict()
        st.markdown(f"- **{compressed_title(item)}**: {compressed_reason(item)}")


def render_woomi_core_interpretation(shared, filters=None):
    st.markdown("### 우미 관점 핵심 해석")
    rows = daily_brief_rows(shared, filters, limit=4)
    if rows.empty:
        st.caption("우미 관점 해석을 만들 후보가 제한적입니다.")
        return
    implications = []
    for _, row in rows.iterrows():
        item = row.to_dict()
        use_case = classify_investment_use_case(item)
        if use_case == "리파이낸싱 / Recap 기회":
            implications.append("capital markets positioning: refinancing pressure는 recap 구조와 lender relationship 구축 준비로 연결됩니다.")
        elif use_case == "LA 인허가 모니터링":
            implications.append("LA execution capability: entitlement precedent와 local sponsor map을 축적해야 합니다.")
        elif use_case == "GP 파트너십 검토":
            implications.append("institutional relationship-building: 반복 등장 GP / capital partner를 접촉 후보로 관리해야 합니다.")
        elif use_case == "개발 부지 / 프로젝트 검토":
            implications.append("future developer capability: site control, permit, construction readiness를 비교할 내부 기준이 필요합니다.")
    if not implications:
        implications.append("strategic market entry timing: 반복 신호가 확인될 때까지 선별적 모니터링이 적절합니다.")
    for item in list(dict.fromkeys(implications))[:4]:
        st.markdown(f"- {item}")


def daily_task_for_team(item, team):
    title = compressed_title(item)
    if team == "투자팀":
        action = "예비 투자 검토: 가격 / sponsor / debt terms 확인"
    elif team == "전략팀":
        action = "전략 테마 업데이트: 반복 시장과 GP 관계를 watchlist에 반영"
    elif team == "자본시장팀":
        action = "자본시장 확인: refinancing, lender, maturity 노출 점검"
    elif team == "개발관리":
        action = "개발 실행 확인: entitlement, permit, local sponsor 단계 점검"
    else:
        action = "경영진 판단: escalation 여부와 owner 지정"
    return {
        "title": title,
        "action": action,
        "why": compressed_reason(item),
        "urgency": institutional_label(investment_decision_label(item)),
        "follow_up": ko_recommended_action(item),
        "context": f"{get_market(item) or '시장 미확인'} / {extract_relationship_firm(item) or get_gp(item) or 'firm 미확인'}",
    }


def daily_operating_tasks(shared, filters=None):
    rows = daily_brief_rows(shared, filters, limit=8)
    teams = {"투자팀": [], "전략팀": [], "자본시장팀": [], "개발관리": [], "경영진": []}
    for _, row in rows.iterrows():
        item = row.to_dict()
        team, _, _, _ = team_action_ownership(item)
        teams.setdefault(team, []).append(daily_task_for_team(item, team))
        if classify_investment_use_case(item) == "리파이낸싱 / Recap 기회":
            teams["자본시장팀"].append(daily_task_for_team(item, "자본시장팀"))
        if row_has_la_california_relevance(item):
            teams["개발관리"].append(daily_task_for_team(item, "개발관리"))
        if executive_priority_score(item) >= 82:
            teams["경영진"].append(daily_task_for_team(item, "경영진"))
    return teams


def render_daily_operating_tasks(shared, filters=None):
    st.markdown("### 오늘 팀 우선 실행 사항")
    teams = daily_operating_tasks(shared, filters)
    for team, tasks in teams.items():
        if not tasks:
            continue
        st.markdown(f"**{team}**")
        seen = set()
        for task in tasks:
            key = task["title"] + task["action"]
            if key in seen:
                continue
            seen.add(key)
            st.markdown(f"- {task['action']} · {task['context']}")
            st.caption(f"{task['why']} / urgency: {task['urgency']} / follow-up: {task['follow_up']}")
            if len(seen) >= (2 if not is_detail_mode() else 4):
                break


def weekly_strategic_shifts(shared, filters=None):
    observations = build_market_regime_observations(shared, filters, limit=6)
    shifts = []
    for obs in observations:
        title = obs["title"]
        count = obs["supporting_count"]
        if "리파이낸싱" in title or "자본" in title:
            shifts.append(("capital flow / refinancing", f"{title} 관찰이 {count}개로 누적되어 자본시장 대응 필요성이 커졌습니다."))
        elif "인허가" in title or "Affordable" in title:
            shifts.append(("LA / entitlement relevance", f"{title} 흐름이 강화되어 LA 실행 역량과 policy tracking이 중요해졌습니다."))
        elif "Sun Belt" in title:
            shifts.append(("market behavior", f"{title} 관련 관찰이 늘어 supply / lease-up 가정을 점검해야 합니다."))
    relationship_targets = build_partner_targets(shared, filters, limit=3)
    if relationship_targets:
        shifts.append(("relationship trend", f"{relationship_targets[0]['firm']} 등 반복 관계 후보가 나타나 relationship map 업데이트가 필요합니다."))
    return list(dict.fromkeys(shifts))[:5]


def render_weekly_strategic_shifts(shared, filters=None):
    st.markdown("### 이번 주 전략 변화")
    shifts = weekly_strategic_shifts(shared, filters)
    if not shifts:
        st.caption("이번 주 의미 있는 전략 변화는 제한적입니다.")
        return
    for title, body in shifts:
        st.markdown(f"- **{title}**: {body}")


def market_concentration_summary(shared, filters=None):
    observations = build_market_regime_observations(shared, filters, limit=5)
    lines = []
    for obs in observations[:4]:
        markets = ", ".join(obs["markets"][:3]) if obs["markets"] else "복수 시장"
        lines.append(f"{obs['title']} · {markets} · {obs['supporting_count']}개 근거")
    if not lines:
        lines.append("기관 자금 집중 영역은 아직 명확하지 않습니다.")
    return lines


def render_market_concentration(shared, filters=None):
    st.markdown("### 현재 기관 자금이 집중되는 영역")
    for line in market_concentration_summary(shared, filters):
        st.markdown(f"- {line}")
    st.caption("집중 영역은 향후 가격 발견, lender appetite, GP partnership 우선순위 판단에 영향을 줍니다.")


def early_but_important_themes(shared, filters=None):
    items = []
    for text in what_could_matter_next(shared, filters):
        if "1개" not in text:
            items.append(text)
    targets = build_partner_targets(shared, filters, limit=5)
    for target in targets:
        if target["evidence_count"] >= 2 and target["score"] < 78:
            items.append(f"{target['firm']}: 아직 Tier 1은 아니지만 반복 관계 신호가 있어 consensus 이전에 관리할 후보입니다.")
    return items[:5]


def render_early_theme_detection(shared, filters=None):
    st.markdown("### 초기 관찰 단계이나 중요해질 가능성")
    items = early_but_important_themes(shared, filters)
    if not items:
        st.caption("초기 중요 테마는 제한적입니다.")
        return
    for item in items[:4 if not is_detail_mode() else 6]:
        st.markdown(f"- {item}")


def contradiction_items(shared, filters=None):
    combined = combined_reasoning_rows(shared, filters)
    items = []
    if combined.empty:
        return items
    capital = len(rows_matching_keywords(combined, ["capital", "institutional", "lender", "loan"]))
    stalled = len(rows_matching_keywords(combined, ["stalled", "delayed", "construction delay", "distress"]))
    entitlement = len(rows_matching_keywords(combined, ["entitlement", "permit", "approved", "density bonus"]))
    demand_risk = len(rows_matching_keywords(combined, ["vacancy", "concession", "lease-up", "supply pressure"]))
    relationship = len(rows_matching_keywords(combined, ["relationship", "partnership", "jv"]))
    execution = len(rows_matching_keywords(combined, ["construction started", "delivery", "opened", "stabilized"]))
    if capital > 10 and stalled > 2:
        items.append("자본 흐름은 보이지만 실행 지연 신호도 있어, capital appetite와 project execution을 분리해서 판단해야 합니다.")
    if capital > 10 and len(rows_matching_keywords(combined, ["refinanc", "maturity", "recap"])) > 8:
        items.append("기관 자본 활동이 있음에도 refinancing 압박이 반복되어, 매입 기회와 stress risk가 동시에 존재합니다.")
    if entitlement > 20 and demand_risk > 3:
        items.append("인허가 precedent는 쌓이지만 lease-up / supply 부담이 있어 개발 timing 판단이 단순하지 않습니다.")
    if relationship > 10 and execution < 4:
        items.append("관계 활동은 늘지만 실행 이벤트가 제한적이어서, relationship mapping을 선행하되 투자 판단은 보류해야 합니다.")
    return items[:4]


def render_strategic_contradictions(shared, filters=None):
    st.markdown("### 엇갈리는 시장 신호")
    items = contradiction_items(shared, filters)
    if not items:
        st.caption("현재 뚜렷한 contradiction은 제한적입니다.")
        return
    for item in items:
        st.markdown(f"- {item}")


def render_long_horizon_watches(shared, filters=None):
    st.markdown("### 6~18개월 관찰 테마")
    themes = [
        "recapitalization wave: refinancing maturity와 lender appetite 변화를 함께 추적",
        "distressed refinancing: bridge loan stress와 sponsor liquidity watch",
        "institutional GP expansion: 반복 등장 GP와 capital partner 관계 mapping",
        "LA entitlement pipeline: affordable / density bonus / CEQA precedent 축적",
        "affordable housing incentives: public incentive와 capital stack feasibility",
        "development slowdown/recovery: construction start, delivery, lease-up 전환점 확인",
    ]
    for theme in themes[:4 if not is_detail_mode() else 6]:
        st.markdown(f"- {theme}")


def page_daily_operating_brief(shared, filters):
    st.subheader("Daily Operating Brief / 일일 운영 브리핑")
    st.caption("전략팀, 투자팀, 자본시장팀, 개발관리, 경영진이 함께 보는 일일 운영 브리핑입니다.")
    st.markdown("### 오늘 시장 변화")
    render_today_market_change(shared, filters)
    render_daily_operating_tasks(shared, filters)
    render_weekly_strategic_shifts(shared, filters)
    render_who_should_we_meet(shared, filters)
    st.markdown("### Timing / Cycle")
    render_market_temperature(shared, filters)
    render_market_cycle_interpretation(shared, filters)
    st.markdown("### 초기 중요 테마")
    render_early_theme_detection(shared, filters)
    render_strategic_contradictions(shared, filters)
    st.markdown("### 6~18개월 관찰 테마")
    render_long_horizon_watches(shared, filters)
    if is_detail_mode():
        render_market_concentration(shared, filters)
        render_execution_blocker_analysis(shared, filters)


def page_executive_briefing(shared, filters):
    st.subheader("Morning Investment Brief")
    st.caption("실제 의사결정에 필요한 변화, 실행 항목, timing만 압축했습니다.")
    render_today_market_change(shared, filters)
    render_woomi_core_interpretation(shared, filters)
    render_daily_operating_tasks(shared, filters)
    render_who_should_we_meet(shared, filters)
    st.markdown("### 시장 timing / cycle 변화")
    render_market_temperature(shared, filters)
    render_market_cycle_interpretation(shared, filters)
    render_strategic_contradictions(shared, filters)
    render_underwriting_readiness(shared, filters)
    if is_detail_mode():
        render_weekly_strategic_shifts(shared, filters)
        render_market_concentration(shared, filters)
        render_early_theme_detection(shared, filters)
        render_long_horizon_watches(shared, filters)
        render_investment_memo_preview(shared, filters)


def legacy_main_15():
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)

    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("Daily Institutional Operating System")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드"], key="view_mode")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "일일 운영 브리핑": page_daily_operating_brief,
        "투자 판단 센터": page_investment_decision_center,
        "Decision Board": page_decision_board,
        "Timing / Conviction": page_timing_memory,
        "파트너 Targeting": page_partner_targeting,
        "팀 Workflow": page_operating_workflow,
        "전략 Narrative": page_strategic_narrative,
        "체제 / 교차 시그널": page_regime_reasoning,
        "투자검토 메모": page_investment_committee_prep,
        "시장 인텔리전스": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California 전략": page_la_california_strategy,
        "GP / 자본 관계": page_gp_capital_relationships,
        "시스템 / 파이프라인": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)

    filters = show_global_filters([
        shared["cards"], shared["watchlists"], shared["high_confidence"],
        shared["opportunities"], shared["distress"], shared["la_assets"],
        shared["la_entitlement"], shared["la_lifecycle"], shared["la_persistent_assets"],
        shared["gp_watchlist"], shared["institutional_relationships"], shared["relationship_graph"],
        shared["historical_memory"], shared["persistent_asset_memory"], shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])

    app_header(shared)
    st.caption(f"최근 실행: {summary.get('run_timestamp', '실행 데이터 없음')}")
    if is_detail_mode():
        kpi_strip(shared)
    st.divider()

    pages[page_name](shared, filters)

    st.divider()
    st.caption("US Residential Intelligence | Daily Institutional Operating System | Streamlit Cloud-ready")


# ---------------------------------------------------------------------------
# Visual Review and Refinement overlay
# ---------------------------------------------------------------------------

REVIEW_TAGS = [
    "too long", "unclear", "repetitive", "weak importance", "too generic",
    "too analytical", "not actionable", "wording awkward", "excessive detail",
    "unclear recommendation",
]


def is_review_mode():
    return st.session_state.get("view_mode", "경영진 모드") == "리뷰 모드"


def review_settings():
    return {
        "hide_badges": st.session_state.get("review_hide_badges", False),
        "hide_metrics": st.session_state.get("review_hide_metrics", False),
        "narrative_only": st.session_state.get("review_narrative_only", False),
        "compressed_cards_only": st.session_state.get("review_compressed_cards_only", False),
        "ultra_clean": st.session_state.get("review_ultra_clean", False),
    }


def review_surface_allows(section_kind):
    """Return whether a review section should render under the active simplification settings."""
    settings = review_settings()
    if not is_review_mode():
        return True
    if settings["ultra_clean"]:
        return section_kind in {"narrative", "core"}
    if settings["narrative_only"]:
        return section_kind in {"narrative", "core", "analysis"}
    if settings["compressed_cards_only"]:
        return section_kind in {"cards", "core"}
    return True


def render_badges(badges):
    if review_settings()["hide_badges"]:
        return
    st.markdown(" ".join([item for item in badges if item]), unsafe_allow_html=True)


def section_review_rows(shared, filters=None):
    return {
        "오늘 시장 변화": daily_brief_rows(shared, filters, limit=6),
        "오늘 팀 실행": compressed_executive_rows(shared, filters, limit=8),
        "관계 구축 우선순위": pd.DataFrame(build_partner_targets(shared, filters, limit=6)),
        "시장 timing / cycle": investment_decision_rows(shared, filters, detail=False, limit=8),
        "리스크 및 관찰": investment_decision_rows(shared, filters, detail=True, limit=12),
        "실행 준비 상태": investment_decision_rows(shared, filters, detail=False, limit=8),
    }


def section_texts_from_df(df):
    if df is None or df.empty:
        return []
    texts = []
    for _, row in df.iterrows():
        item = row.to_dict()
        texts.append(" ".join([
            get_title(item), compressed_title(item), ko_recommended_action(item),
            get_market(item), extract_relationship_firm(item), get_gp(item),
        ]))
    return texts


def density_stats(name, df):
    texts = section_texts_from_df(df)
    words = sum(len(text.split()) for text in texts)
    entities = [extract_relationship_firm(row.to_dict()) for _, row in df.iterrows()] if df is not None and not df.empty else []
    markets = [get_market(row.to_dict()) for _, row in df.iterrows()] if df is not None and not df.empty else []
    gps = [get_gp(row.to_dict()) for _, row in df.iterrows()] if df is not None and not df.empty else []
    recommendations = [ko_recommended_action(row.to_dict()) for _, row in df.iterrows()] if df is not None and not df.empty else []
    return {
        "section": name,
        "reading_words": words,
        "reading_seconds": int(words / 3.3) if words else 0,
        "cards": 0 if df is None else len(df),
        "repeated_entities": max(0, len([v for v in entities if v]) - len(set([v for v in entities if v]))),
        "repeated_markets": max(0, len([v for v in markets if v]) - len(set([v for v in markets if v]))),
        "repeated_gps": max(0, len([v for v in gps if v]) - len(set([v for v in gps if v]))),
        "repeated_narratives": max(0, len([v for v in recommendations if v]) - len(set([v for v in recommendations if v]))),
    }


def all_density_stats(shared, filters=None):
    return [density_stats(name, df) for name, df in section_review_rows(shared, filters).items()]


def deterministic_review_tags(stats):
    tags = []
    if stats["reading_words"] > 220:
        tags += ["too long", "excessive detail"]
    if stats["cards"] > 5:
        tags.append("too analytical")
    if stats["repeated_entities"] or stats["repeated_markets"] or stats["repeated_narratives"]:
        tags.append("repetitive")
    if stats["cards"] and stats["reading_words"] < 25:
        tags.append("weak importance")
    if stats["repeated_narratives"] >= 2:
        tags.append("too generic")
    return list(dict.fromkeys(tags))


def render_review_guides(section_name, order):
    if not is_review_mode():
        return
    st.markdown(
        f"""
        <div style="border:1px dashed #94a3b8; padding:.55rem .7rem; margin:.7rem 0 1rem 0; background:#f8fafc;">
          <strong>Review #{order}</strong> · {section_name}<br>
          <span style="color:#64748b;">section boundary · reading order · card grouping · spacing checkpoint</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_content_density_panel(shared, filters=None):
    st.markdown("### Content Density Analysis")
    stats = all_density_stats(shared, filters)
    df = pd.DataFrame(stats)
    st.dataframe(df, use_container_width=True, hide_index=True)
    for stat in stats:
        tags = deterministic_review_tags(stat)
        if tags:
            st.caption(f"{stat['section']}: {', '.join(tags)}")


def render_mobile_review_panel(shared, filters=None):
    st.markdown("### 모바일 미리보기 체크")
    rows = compressed_executive_rows(shared, filters, limit=12)
    if rows.empty:
        st.caption("모바일 검토 후보가 없습니다.")
        return
    title_lengths = [(len(get_title(row.to_dict())), compressed_title(row.to_dict())) for _, row in rows.iterrows()]
    longest = sorted(title_lengths, reverse=True)[:3]
    stats = all_density_stats(shared, filters)
    overflow = [s["section"] for s in stats if s["reading_words"] > 220 or s["cards"] > 5]
    badge_density = len(rows) * 3
    fatigue = [s["section"] for s in stats if s["reading_seconds"] > 60]
    st.write("**Longest cards**")
    for length, title in longest:
        st.markdown(f"- {title} · {length} chars")
    st.write(f"**Overflow-prone sections:** {', '.join(overflow) if overflow else '제한적'}")
    st.write(f"**Excessive badge density:** {'검토 필요' if badge_density > 24 else '양호'}")
    st.write(f"**Likely mobile fatigue areas:** {', '.join(fatigue) if fatigue else '제한적'}")


def render_executive_compression_check(shared, filters=None):
    st.markdown("### Executive Compression Check")
    stats = all_density_stats(shared, filters)
    total_cards = sum(s["cards"] for s in stats)
    total_blocks = len([s for s in stats if s["cards"] or s["reading_words"]])
    total_words = sum(s["reading_words"] for s in stats)
    rows = compressed_executive_rows(shared, filters, limit=15)
    recommendations = [ko_recommended_action(row.to_dict()) for _, row in rows.iterrows()] if not rows.empty else []
    markets = [get_market(row.to_dict()) for _, row in rows.iterrows()] if not rows.empty else []
    repeated_recommendations = max(0, len([v for v in recommendations if v]) - len(set([v for v in recommendations if v])))
    repeated_markets = max(0, len([v for v in markets if v]) - len(set([v for v in markets if v])))
    st.write(f"Visible executive cards: **{total_cards}**")
    st.write(f"Visible reading blocks: **{total_blocks}**")
    st.write(f"Estimated reading time: **{int(total_words / 220 * 60)} sec**")
    st.write(f"Repeated recommendations: **{repeated_recommendations}**")
    st.write(f"Repeated markets: **{repeated_markets}**")
    if total_words > 660 or total_cards > 18:
        st.warning("Executive surface is likely too dense for a 3-minute read.")
    else:
        st.success("Executive surface is within a reasonable 3-minute review range.")


def render_what_feels_wrong_panel(shared, filters=None):
    st.markdown("### What feels wrong?")
    stats = all_density_stats(shared, filters)
    for stat in stats:
        tags = deterministic_review_tags(stat)
        selected = st.multiselect(
            f"{stat['section']} review tags",
            REVIEW_TAGS,
            default=tags,
            key=f"review_tags_{stat['section']}",
        )
        if selected:
            st.caption(f"현재 태그: {', '.join(selected)}")
    st.text_area("Reviewer notes", key="reviewer_notes", placeholder="압축 필요, 문구 수정, 제거 후보, 재설계 아이디어를 적습니다.")


def build_review_snapshot(shared, filters=None):
    stats = all_density_stats(shared, filters)
    lines = [
        "# Review Snapshot",
        "",
        "## Compression Check",
    ]
    total_words = sum(s["reading_words"] for s in stats)
    lines += [
        f"- Total sections: {len(stats)}",
        f"- Total estimated words: {total_words}",
        f"- Estimated reading time: {int(total_words / 220 * 60)} sec",
        "",
        "## Noisy Sections",
    ]
    for stat in stats:
        tags = st.session_state.get(f"review_tags_{stat['section']}", deterministic_review_tags(stat))
        if tags:
            lines.append(f"- {stat['section']}: {', '.join(tags)}")
    lines += ["", "## Density", ""]
    for stat in stats:
        lines.append(
            f"- {stat['section']}: {stat['cards']} cards, {stat['reading_words']} words, "
            f"{stat['repeated_markets']} repeated markets, {stat['repeated_narratives']} repeated narratives"
        )
    notes = st.session_state.get("reviewer_notes", "").strip()
    lines += ["", "## Reviewer Notes", "", notes or "- None"]
    return "\n".join(lines)


def render_review_snapshot_export(shared, filters=None):
    st.markdown("### Review Snapshot Export")
    snapshot = build_review_snapshot(shared, filters)
    if st.button("Export review snapshot", use_container_width=True):
        path = OUTPUT_DIR / "review_snapshot.md"
        path.write_text(snapshot, encoding="utf-8")
        st.success(f"Saved `{file_label(path)}`")
    st.download_button(
        "Download current review snapshot",
        snapshot,
        file_name="review_snapshot.md",
        mime="text/markdown",
        use_container_width=True,
    )


def review_section_options():
    return [
        "전체 보기",
        "오늘 시장 변화",
        "우미 관점 핵심 해석",
        "오늘 팀 우선 실행 사항",
        "관계 구축 우선순위",
        "시장 timing / cycle 변화",
        "리스크 및 관찰 사항",
        "실행 준비 상태",
    ]


def render_selected_review_section(shared, filters, section_name):
    renderers = {
        "오늘 시장 변화": lambda: render_today_market_change(shared, filters),
        "우미 관점 핵심 해석": lambda: render_woomi_core_interpretation(shared, filters),
        "오늘 팀 우선 실행 사항": lambda: render_daily_operating_tasks(shared, filters),
        "관계 구축 우선순위": lambda: render_who_should_we_meet(shared, filters),
        "시장 timing / cycle 변화": lambda: (render_market_temperature(shared, filters), render_market_cycle_interpretation(shared, filters)),
        "리스크 및 관찰 사항": lambda: render_strategic_contradictions(shared, filters),
        "실행 준비 상태": lambda: render_underwriting_readiness(shared, filters),
    }
    if section_name == "전체 보기":
        page_executive_briefing(shared, filters)
    else:
        render_review_guides(section_name, review_section_options().index(section_name))
        renderers[section_name]()


def render_review_flow_section(order, section_name, section_kind, renderer):
    """Render one reviewable section with visible hierarchy and active simplification logic."""
    if not review_surface_allows(section_kind):
        return
    render_review_guides(section_name, order)
    st.caption(f"Hierarchy: {section_kind} · Flow position {order}")
    renderer()


def page_review_mode(shared, filters):
    st.subheader("Review Mode / 리뷰 모드")
    st.caption("정보 구조, 압축 품질, 모바일 가독성, 반복 서사를 검토하는 임시 작업 화면입니다.")
    section_name = st.selectbox("Section Isolation Mode", review_section_options(), key="review_isolated_section")
    render_selected_review_section(shared, filters, section_name)
    st.divider()
    render_content_density_panel(shared, filters)
    render_mobile_review_panel(shared, filters)
    render_executive_compression_check(shared, filters)
    render_what_feels_wrong_panel(shared, filters)
    render_review_snapshot_export(shared, filters)


def page_executive_briefing(shared, filters):
    if is_review_mode():
        st.subheader("Morning Investment Brief / Review")
        for order, (name, kind, renderer) in enumerate([
            ("오늘 시장 변화", "narrative", lambda: render_today_market_change(shared, filters)),
            ("우미 관점 핵심 해석", "core", lambda: render_woomi_core_interpretation(shared, filters)),
            ("오늘 팀 우선 실행 사항", "cards", lambda: render_daily_operating_tasks(shared, filters)),
            ("관계 구축 우선순위", "cards", lambda: render_who_should_we_meet(shared, filters)),
            ("시장 timing / cycle 변화", "analysis", lambda: (
                render_market_temperature(shared, filters),
                render_market_cycle_interpretation(shared, filters),
            )),
            ("리스크 및 관찰 사항", "analysis", lambda: render_strategic_contradictions(shared, filters)),
            ("실행 준비 상태", "analysis", lambda: render_underwriting_readiness(shared, filters)),
        ], start=1):
            render_review_flow_section(order, name, kind, renderer)
        return
    st.subheader("Morning Investment Brief")
    st.caption("실제 의사결정에 필요한 변화, 실행 항목, timing만 압축했습니다.")
    render_today_market_change(shared, filters)
    render_woomi_core_interpretation(shared, filters)
    render_daily_operating_tasks(shared, filters)
    render_who_should_we_meet(shared, filters)
    st.markdown("### 시장 timing / cycle 변화")
    render_market_temperature(shared, filters)
    render_market_cycle_interpretation(shared, filters)
    render_strategic_contradictions(shared, filters)
    render_underwriting_readiness(shared, filters)
    if is_detail_mode():
        render_weekly_strategic_shifts(shared, filters)
        render_market_concentration(shared, filters)
        render_early_theme_detection(shared, filters)
        render_long_horizon_watches(shared, filters)
        render_investment_memo_preview(shared, filters)


def legacy_main_16():
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()
    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)
    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("Daily Institutional Operating System")
    st.sidebar.info("데이터 갱신: `python news_collector.py`")
    st.sidebar.radio("보기 모드", ["경영진 모드", "상세 분석 모드", "리뷰 모드"], key="view_mode")
    if is_review_mode():
        st.sidebar.markdown("### Visual Simplification")
        st.sidebar.checkbox("Hide badges", key="review_hide_badges")
        st.sidebar.checkbox("Hide metrics", key="review_hide_metrics")
        st.sidebar.checkbox("Narrative-only mode", key="review_narrative_only")
        st.sidebar.checkbox("Compressed cards only", key="review_compressed_cards_only")
        st.sidebar.checkbox("Ultra-clean executive mode", key="review_ultra_clean")

    pages = {
        "경영진 브리핑": page_executive_briefing,
        "리뷰 모드": page_review_mode,
        "일일 운영 브리핑": page_daily_operating_brief,
        "투자 판단 센터": page_investment_decision_center,
        "Decision Board": page_decision_board,
        "Timing / Conviction": page_timing_memory,
        "파트너 Targeting": page_partner_targeting,
        "팀 Workflow": page_operating_workflow,
        "전략 Narrative": page_strategic_narrative,
        "체제 / 교차 시그널": page_regime_reasoning,
        "투자검토 메모": page_investment_committee_prep,
        "시장 인텔리전스": page_market_intelligence,
        "기회 및 리스크": page_opportunity_risk,
        "LA / California 전략": page_la_california_strategy,
        "GP / 자본 관계": page_gp_capital_relationships,
        "시스템 / 파이프라인": page_system_pipeline_clean,
    }
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)
    filters = show_global_filters([
        shared["cards"], shared["watchlists"], shared["high_confidence"],
        shared["opportunities"], shared["distress"], shared["la_assets"],
        shared["la_entitlement"], shared["la_lifecycle"], shared["la_persistent_assets"],
        shared["gp_watchlist"], shared["institutional_relationships"], shared["relationship_graph"],
        shared["historical_memory"], shared["persistent_asset_memory"], shared["lifecycle_transition"],
        shared["relationship_persistence"],
    ])
    app_header(shared)
    st.caption(f"최근 실행: {summary.get('run_timestamp', '실행 데이터 없음')}")
    if is_detail_mode() and not review_settings()["hide_metrics"]:
        kpi_strip(shared)
    st.divider()
    pages[page_name](shared, filters)
    st.divider()
    st.caption("US Residential Intelligence | Review-ready Institutional Operating System")


# ---------------------------------------------------------------------------
# Institutional morning brief homepage refinement
# ---------------------------------------------------------------------------

def homepage_ranked_cards(shared, filters=None, limit=3):
    cards = apply_filters(shared["cards"], filters)
    if cards.empty:
        return cards
    score_col = "card_score" if "card_score" in cards.columns else None
    if score_col:
        cards = cards.copy()
        cards["_homepage_score"] = cards[score_col].apply(as_number)
        cards = cards.sort_values("_homepage_score", ascending=False)
    return cards.head(limit)


def render_homepage_top_articles(shared, filters=None):
    st.markdown("### 오늘의 Top 기사")
    rows = homepage_ranked_cards(shared, filters, limit=3)
    if rows.empty:
        st.caption("오늘 우선 검토할 기사형 관찰이 아직 충분하지 않습니다.")
        return
    for _, row in rows.iterrows():
        item = row.to_dict()
        title = item.get("card_title") or get_title(item)
        market = item.get("market") or "시장 미확인"
        sector = item.get("residential_sector") or "섹터 미확인"
        implication = item.get("why_it_matters") or compressed_reason(item)
        with st.container(border=True):
            st.markdown(f"**{title}**")
            st.caption(f"{market} · {sector}")
            st.write(implication)


def render_homepage_hot_market(shared, filters=None):
    st.markdown("### 오늘의 Hot Market")
    frames = [
        apply_filters(shared["cards"], filters),
        apply_filters(shared["opportunities"], filters),
        apply_filters(shared["high_confidence"], filters),
    ]
    markets = []
    for frame in frames:
        if frame is not None and not frame.empty and "market" in frame.columns:
            markets.extend([value for value in frame["market"].dropna().tolist() if str(value).strip()])
    if not markets:
        st.caption("시장 집중도를 판단할 데이터가 아직 충분하지 않습니다.")
        return
    counts = pd.Series(markets).value_counts()
    top_market = counts.index[0]
    support = int(counts.iloc[0])
    related_cards = apply_filters(shared["cards"], filters)
    related_cards = related_cards[related_cards.get("market", pd.Series(dtype=str)) == top_market] if not related_cards.empty and "market" in related_cards.columns else pd.DataFrame()
    theme = "기관 검토와 기회 관찰이 함께 쌓이고 있습니다."
    if not related_cards.empty and "card_type" in related_cards.columns:
        top_type = related_cards["card_type"].mode().iloc[0]
        theme = f"{top_type} 관련 관찰이 가장 많이 집중되고 있습니다."
    st.markdown(f"**{top_market}**")
    st.write(f"{support}건의 관련 관찰이 포착되며, {theme} 단일 기사보다 반복 출현 여부를 중심으로 해석할 필요가 있습니다.")


def render_homepage_development_status(shared, filters=None):
    st.markdown("### 개발 현황")
    lifecycle = apply_filters(shared["development_lifecycle"], filters)
    if lifecycle.empty or "current_lifecycle_stage" not in lifecycle.columns:
        st.caption("개발 단계 해석에 필요한 데이터가 아직 충분하지 않습니다.")
        return
    counts = lifecycle["current_lifecycle_stage"].fillna("Unknown Stage").value_counts()
    leading = counts.head(3)
    sentence = ", ".join([f"{stage} {int(count)}건" for stage, count in leading.items()])
    later_stage_terms = {"Construction Ready", "Construction Started", "Vertical Construction", "Delivery / Opening", "Lease-Up", "Stabilized / Operating"}
    later_count = int(lifecycle["current_lifecycle_stage"].isin(later_stage_terms).sum())
    stalled_count = int((lifecycle["current_lifecycle_stage"] == "Distressed / Stalled").sum())
    st.write(f"현재 가장 많이 관찰되는 개발 단계는 {sentence}입니다.")
    if later_count:
        st.write(f"후기 개발 단계 신호는 {later_count}건으로, 일부 프로젝트는 실행 국면에 진입해 있습니다.")
    if stalled_count:
        st.write(f"다만 지연 또는 정체 신호도 {stalled_count}건 확인되어, 실행 리스크와 자본조달 조건을 함께 봐야 합니다.")


def render_homepage_institutional_gp_trends(shared, filters=None):
    st.markdown("### 기관 및 GP 동향")
    gp_rows = apply_filters(shared["gp_watchlist"], filters)
    inst_rows = apply_filters(shared["institutional_relationships"], filters)
    points = []
    if not gp_rows.empty:
        ranked = gp_rows.copy()
        if "emerging_gp_score" in ranked.columns:
            ranked["_score"] = ranked["emerging_gp_score"].apply(as_number)
            ranked = ranked.sort_values("_score", ascending=False)
        top_gp = ranked.iloc[0].to_dict()
        gp_name = top_gp.get("canonical_gp_name") or top_gp.get("gp_name") or "상위 GP"
        market = top_gp.get("primary_market") or "주요 시장"
        points.append(f"{gp_name}가 {market}에서 가장 두드러진 GP 관찰 대상으로 나타납니다.")
    if not inst_rows.empty:
        ranked = inst_rows.copy()
        if "institutional_relationship_score" in ranked.columns:
            ranked["_score"] = ranked["institutional_relationship_score"].apply(as_number)
            ranked = ranked.sort_values("_score", ascending=False)
        top_inst = ranked.iloc[0].to_dict()
        firm = top_inst.get("firm_name") or "상위 기관"
        relation = top_inst.get("capital_flow_signal") or top_inst.get("relationship_signal") or "관계 신호"
        points.append(f"{firm} 관련 {relation}이 반복적으로 포착되어 자본시장 연결성 점검이 필요합니다.")
    if not points:
        st.caption("기관 및 GP 동향을 요약할 데이터가 아직 충분하지 않습니다.")
        return
    for point in points[:3]:
        st.markdown(f"- {point}")


def page_executive_briefing(shared, filters):
    if is_review_mode():
        st.subheader("Morning Investment Brief / Review")
        review_sections = [
            ("오늘 시장에서 실제 중요한 변화", "narrative", lambda: render_today_market_change(shared, filters)),
            ("오늘의 Top 기사", "cards", lambda: render_homepage_top_articles(shared, filters)),
            ("오늘의 Hot Market", "analysis", lambda: render_homepage_hot_market(shared, filters)),
            ("개발 현황", "analysis", lambda: render_homepage_development_status(shared, filters)),
            ("기관 및 GP 동향", "analysis", lambda: render_homepage_institutional_gp_trends(shared, filters)),
        ]
        for order, (name, kind, renderer) in enumerate(review_sections, start=1):
            render_review_flow_section(order, name, kind, renderer)
        return

    st.subheader("Morning Investment Brief")
    st.caption("오늘의 시장 변화와 투자적 함의를 압축해 보여주는 기관투자자형 아침 브리프입니다.")
    render_today_market_change(shared, filters)
    render_homepage_top_articles(shared, filters)
    render_homepage_hot_market(shared, filters)
    render_homepage_development_status(shared, filters)
    render_homepage_institutional_gp_trends(shared, filters)


def page_market_intelligence_product(shared, filters):
    st.title("시장 인텔리전스")
    render_homepage_hot_market(shared, filters)
    render_market_regime_summary(shared, filters)
    render_market_timing_interpretation(shared, filters)
    with st.expander("상세 보기"):
        render_conviction_memory(shared, filters)
        render_daily_strategic_narrative(shared, filters)
        signal_section("투자 기회", apply_filters(shared["opportunities"], filters), shared, ["opportunity_score"], FILES["opportunities"], limit=4)
        signal_section("리스크 모니터링", apply_filters(shared["distress"], filters), shared, ["distress_score"], FILES["distress"], limit=4)


def page_development_status_product(shared, filters):
    st.title("개발 현황")
    render_homepage_development_status(shared, filters)
    signal_section("개발 단계", apply_filters(shared["development_lifecycle"], filters), shared, ["lifecycle_opportunity_score"], FILES["development_lifecycle"], limit=4)
    with st.expander("상세 보기"):
        signal_section("인허가 동향", apply_filters(shared["la_entitlement"], filters), shared, ["local_relevance_score", "entitlement_opportunity_score"], FILES["la_entitlement"], limit=4)
        signal_section("LA / California 개발 Watch", apply_filters(shared["la_lifecycle"], filters), shared, ["lifecycle_opportunity_score"], FILES["la_lifecycle"], limit=4)
        signal_section("자산 / Parcel Watch", apply_filters(shared["la_assets"], filters), shared, ["la_asset_opportunity_score"], FILES["la_assets"], limit=4)


def page_gp_capital_product(shared, filters):
    st.title("GP / 자본 동향")
    render_homepage_institutional_gp_trends(shared, filters)
    gp_rows = apply_filters(shared["gp_watchlist"], filters)
    render_watchlist_items(gp_rows, shared, FILES["gp_watchlist"], limit=5)
    with st.expander("상세 보기"):
        render_watchlist_items(apply_filters(shared["institutional_relationships"], filters), shared, FILES["institutional_relationships"], limit=5)
        render_relationship_priority_targets(shared, filters)
        render_relationship_map_view(shared, filters)
        render_relationship_development_tracking(shared, filters)


CAPITAL_ACTIVITY_TERMS = {
    "Acquisition": ["acquisition", "acquire", "acquires", "acquired", "purchase"],
    "Disposition / Exit": ["disposition", "sale", "seeks buyers", "exit"],
    "JV / Partnership": ["joint venture", " jv ", "partnership"],
    "Construction Financing": ["construction financing", "construction loan"],
    "Refinancing / Recapitalization": ["refinancing", "refinanced", "recapitalization", "recap"],
    "Preferred Equity / Mezzanine": ["preferred equity", "mezzanine"],
    "Fundraising / Fund Close": ["fund close", "fundraising", "closes fund", "capital raise"],
    "Platform Investment": ["platform investment"],
    "Portfolio Transaction": ["portfolio transaction", "portfolio sale", "portfolio acquisition"],
    "Development Partnership": ["development partnership"],
    "Lender / Agency Financing": ["fannie mae", "freddie mac", "agency financing", "agency lending"],
}


def capital_activity_type(text):
    """Classify observed capital activity without promoting weak mentions."""
    blob = str(text or "").lower()
    for label, terms in CAPITAL_ACTIVITY_TERMS.items():
        if any(term in blob for term in terms):
            return label
    if any(term in blob for term in ["commentary", "outlook", "research", "mentioned"]):
        return "Commentary"
    return "Entity Mention Only"


def is_strong_capital_activity(label):
    return label not in {
        "Entity Mention Only",
        "Commentary",
        "Macro mention",
        "Relationship reference without transaction",
        "Unknown",
    }


def capital_entity_articles(shared, entity_name):
    """Return deduped article rows that explicitly mention one entity."""
    source = shared.get("articles", pd.DataFrame())
    if source.empty:
        return source
    entity_lower = str(entity_name).lower()
    rows = source[source.apply(
        lambda row: entity_lower in compact_text_blob(row.to_dict()).lower(),
        axis=1,
    )].copy()
    if rows.empty:
        return rows
    rows["_entity_title"] = rows.apply(lambda row: get_title(row.to_dict()), axis=1)
    rows["_entity_title_key"] = rows["_entity_title"].apply(normalized_headline)
    rows["_activity_type"] = rows.apply(
        lambda row: capital_activity_type(compact_text_blob(row.to_dict())),
        axis=1,
    )
    return rows.drop_duplicates("_entity_title_key", keep="first")


def build_capital_entity_rows(shared):
    """Aggregate one display row per GP / sponsor / capital entity."""
    inst = shared.get("institutional_relationships", pd.DataFrame())
    gp = shared.get("gp_watchlist", pd.DataFrame())
    names = []
    if not inst.empty and "firm_name" in inst.columns:
        names.extend(inst["firm_name"].dropna().astype(str).tolist())
    if not gp.empty and "canonical_gp_name" in gp.columns:
        names.extend(gp["canonical_gp_name"].dropna().astype(str).tolist())
    rows = []
    for name in list(dict.fromkeys([item for item in names if item and item != "Unknown"])):
        articles = capital_entity_articles(shared, name)
        inst_match = inst[inst.get("firm_name", pd.Series(dtype=str)).astype(str) == name]
        gp_match = gp[gp.get("canonical_gp_name", pd.Series(dtype=str)).astype(str) == name]
        metadata = {}
        if not inst_match.empty:
            metadata.update(inst_match.iloc[0].to_dict())
        if not gp_match.empty:
            metadata.update(gp_match.iloc[0].to_dict())
        activity_counts = articles["_activity_type"].value_counts() if not articles.empty else pd.Series(dtype=int)
        activity = activity_counts.index[0] if not activity_counts.empty else capital_activity_type(
            metadata.get("detected_activity_types", "")
        )
        source_titles = articles["_entity_title"].head(3).tolist() if not articles.empty else []
        rows.append({
            "entity_name": name,
            "related_markets": metadata.get("detected_markets") or metadata.get("primary_market") or "",
            "residential_sector": metadata.get("residential_sector") or metadata.get("residential_sector_focus") or "",
            "observed_activity": activity,
            "article_count": len(articles),
            "representative_titles": source_titles,
            "signal_quality": metadata.get("confidence_level") or "",
            "score": max(
                as_number(metadata.get("institutional_relationship_score", 0)),
                as_number(metadata.get("gp_activity_score", 0)),
            ),
            "latest_date": articles.get("published", pd.Series(dtype=str)).max() if not articles.empty else "",
            "articles": articles,
        })
    return sorted(
        rows,
        key=lambda row: (
            not is_strong_capital_activity(row["observed_activity"]),
            -row["article_count"],
            -row["score"],
            str(row["latest_date"]),
        ),
    )


def render_capital_entity_cards(shared, filters=None):
    """Render one concise card per capital entity."""
    rows = build_capital_entity_rows(shared)
    if not rows:
        st.caption("현재 자본 흐름을 요약할 엔티티 데이터가 충분하지 않습니다.")
        return
    for row in rows:
        strength = "강한 활동" if is_strong_capital_activity(row["observed_activity"]) else "Weak Mention"
        headline = f"{row['entity_name']} | {row['observed_activity']} | {row['article_count']}건"
        with st.expander(headline, expanded=False):
            if row["related_markets"]:
                st.write(f"**관련 시장:** {row['related_markets']}")
            st.write(f"**관찰된 활동:** {row['observed_activity']} ({strength})")
            st.write(f"**왜 중요한가:** 실제 거래, financing, recap, partnership 여부를 구분해 자본 이동의 강도를 판단하기 위한 관찰입니다.")
            if row["representative_titles"]:
                st.write("**관련 기사:**")
                for title in row["representative_titles"]:
                    st.markdown(f"- {title}")
            if row["signal_quality"]:
                st.write(f"**Signal quality:** {row['signal_quality']}")
            articles = row["articles"]
            if not articles.empty:
                st.markdown("#### 최근 관련 기사")
                for _, article in articles.head(5).iterrows():
                    item = article.to_dict()
                    title = item.get("_entity_title") or get_title(item)
                    source = get_first(item, ["source"], "")
                    date = get_first(item, ["published"], "")
                    market = get_first(item, ["market_focus", "market"], "")
                    activity = item.get("_activity_type") or capital_activity_type(compact_text_blob(item))
                    st.markdown(f"- **{title}**  \n  {source} | {date} | {market} | {activity}")
                    url = get_url(item)
                    if isinstance(url, str) and url.startswith("http"):
                        st.markdown(f"  [원문 기사 보기]({url})")


def render_capital_network_map(shared, filters=None):
    """Render event-clustered capital relationships instead of raw graph edges."""
    st.markdown("### Capital Network Map")
    events = build_capital_events(shared)
    if not events:
        st.caption("현재 표시할 자본 이벤트가 충분하지 않습니다.")
        return
    display_rows = []
    for event in events[:12]:
        relationship_parts = [event["lead_sponsor"]]
        if event["capital_provider"]:
            relationship_parts.append(event["capital_provider"])
        elif event["lender"]:
            relationship_parts.append(event["lender"])
        canonical_title = normalized_capital_event_title(event["event_title"])
        display_rows.append({
            "관계": " → ".join([part for part in relationship_parts if part]),
            "활동 유형": event["activity_type"],
            "시장": event["market"],
            "관련 기사 수": event["article_count"],
            "주요 source": event["source"],
            "_event_key": "|".join([
                (event["lead_sponsor"] or "").lower(),
                event["activity_type"].lower(),
                canonical_title,
            ]),
        })
    display = pd.DataFrame(display_rows).drop_duplicates("_event_key")
    st.dataframe(
        display[["관계", "활동 유형", "시장", "관련 기사 수", "주요 source"]],
        use_container_width=True,
        hide_index=True,
    )


CAPITAL_EVENT_ACTIVITY_MAP = {
    "acquisition": "Acquisition",
    "disposition / exit": "Disposition / Exit",
    "jv / partnership": "JV / Partnership",
    "construction financing": "Construction Financing",
    "refinancing / recapitalization": "Refinancing",
    "preferred equity / mezzanine": "Preferred Equity / Mezzanine",
    "fundraising / fund close": "Fundraising / Fund Close",
    "platform investment": "Platform Investment",
    "portfolio transaction": "Portfolio Transaction",
    "development partnership": "Development Partnership",
}
CAPITAL_EVENT_ALLOWED_TYPES = {
    "Acquisition",
    "Disposition / Exit",
    "JV / Partnership",
    "Construction Financing",
    "Refinancing",
    "Preferred Equity / Mezzanine",
    "Fundraising / Fund Close",
    "Platform Investment",
    "Portfolio Transaction",
    "Development Partnership",
    "Lender / Agency Financing",
}


def normalized_capital_event_title(value):
    return normalized_headline(str(value or "").replace("...", " "))


def event_activity_from_row(row):
    """Prefer explicit deal type, then fall back to headline text."""
    deal_type = str(row.get("deal_type", "") or "").strip().lower()
    if deal_type:
        if deal_type == "jv / partnership":
            return "JV / Partnership"
        return CAPITAL_EVENT_ACTIVITY_MAP.get(deal_type, row.get("deal_type", "Unknown"))
    return capital_activity_type(compact_text_blob(row))


def clean_capital_entity(value):
    text = str(value or "").strip()
    return "" if text in {"", "Unknown", "None detected", "nan"} else text


def infer_lead_sponsor_from_title(title):
    """Infer a lead sponsor only when the headline itself clearly starts with one."""
    clean_title = str(title or "").strip()
    match = re.match(
        r"^([A-Z][A-Za-z&.,' -]+?)\s+(?:acquires|acquire|closes|forms|launches|partners|seeks|secures|gets|opens|to develop)\b",
        clean_title,
        flags=re.IGNORECASE,
    )
    return match.group(1).strip(" ,") if match else ""


def event_participant_role(row, lead_sponsor):
    """Prepare a future-ready participant hierarchy for one capital event."""
    lender = clean_capital_entity(row.get("lender_or_debt_provider", ""))
    capital_provider = clean_capital_entity(row.get("capital_partner", "")) or clean_capital_entity(
        row.get("institutional_partner", "")
    )
    activity = event_activity_from_row(row)
    jv_partner = capital_provider if activity == "JV / Partnership" else ""
    return {
        "lead_sponsor": lead_sponsor,
        "capital_provider": capital_provider,
        "lender": lender,
        "jv_partner": jv_partner,
    }


def build_capital_events(shared):
    """Cluster capital behavior by URL, canonical title, or sponsor + activity + market."""
    deals = read_csv_safely(str(OUTPUT_DIR / "deal_pipeline.csv"))
    if deals.empty:
        return []
    events = []
    seen_urls = set()
    seen_titles = set()
    seen_triplets = set()
    for _, row in deals.iterrows():
        item = row.to_dict()
        title = get_first(item, ["source_article_title", "project_or_deal_name"], "")
        activity = event_activity_from_row(item)
        if activity not in CAPITAL_EVENT_ALLOWED_TYPES:
            continue
        lead_sponsor = clean_capital_entity(item.get("gp_or_developer", "")) or infer_lead_sponsor_from_title(title)
        market = clean_capital_entity(item.get("market", "")) or "Market not specified"
        url = str(item.get("url", "") or "").strip().lower()
        title_key = normalized_capital_event_title(title)
        triplet = (lead_sponsor.lower(), activity.lower(), market.lower())
        if (url and url in seen_urls) or title_key in seen_titles or triplet in seen_triplets:
            continue
        if url:
            seen_urls.add(url)
        seen_titles.add(title_key)
        seen_triplets.add(triplet)
        roles = event_participant_role(item, lead_sponsor)
        events.append({
            "event_title": title,
            "activity_type": activity,
            "market": market,
            "source": clean_capital_entity(item.get("source", "")),
            "url": str(item.get("url", "") or ""),
            "article_count": 1,
            **roles,
        })
    return events


def capital_event_tag(activity):
    if activity == "JV / Partnership":
        return "JV / Partnership"
    if activity in {"Construction Financing", "Lender / Agency Financing"}:
        return "Financing"
    if activity == "Refinancing":
        return "Refinancing"
    if activity in {"Acquisition", "Disposition / Exit", "Portfolio Transaction"}:
        return "Capital Flow"
    if activity in {"Fundraising / Fund Close", "Platform Investment", "Development Partnership"}:
        return "Strategic Expansion"
    return activity or "Weak Mention"


def render_capital_event_cards(shared, filters=None):
    """Render one compact card per deduped capital event."""
    events = build_capital_events(shared)
    if not events:
        st.caption("현재 명확한 capital event가 충분히 포착되지 않았습니다.")
        return
    for event in events:
        entity = event["lead_sponsor"] or event["capital_provider"] or event["lender"] or "Entity not specified"
        headline = f"{entity} | {event['activity_type']} | {event['market']}"
        with st.expander(headline, expanded=False):
            st.write(f"**관찰된 활동:** {capital_event_tag(event['activity_type'])}")
            if event["lead_sponsor"]:
                st.write(f"**Lead Sponsor:** {event['lead_sponsor']}")
            if event["capital_provider"]:
                st.write(f"**Capital Provider:** {event['capital_provider']}")
            if event["lender"]:
                st.write(f"**Lender:** {event['lender']}")
            if event["jv_partner"]:
                st.write(f"**JV Partner:** {event['jv_partner']}")
            st.write(f"**관련 시장:** {event['market']}")
            st.write(f"**관련 기사:** {event['event_title']}")
            if event["source"]:
                if event["url"]:
                    st.markdown(f"**Source:** [{event['source']}]({event['url']})")
                else:
                    st.write(f"**Source:** {event['source']}")
            if event["url"]:
                st.markdown(f"[원문 기사 보기]({event['url']})")


def page_gp_capital_product(shared, filters):
    """Entity-first capital flow intelligence page."""
    st.title("GP / 자본 동향")
    st.markdown("### 기관 및 GP 자본 흐름")
    st.caption("미국 주거시장에서 관찰되는 GP, sponsor, lender, institutional capital 움직임을 정리합니다.")
    render_capital_event_cards(shared, filters)
    render_capital_network_map(shared, filters)


def page_system_settings_product(shared, filters):
    st.title("시스템 / 설정")
    system_status_panel(shared)
    render_site_parcel_source_diagnostics(shared)
    tabs = st.tabs(["리뷰 도구", "배포 체크", "원문 데이터"])
    with tabs[0]:
        st.subheader("리뷰 도구")
        render_content_density_panel(shared, filters)
        render_mobile_review_panel(shared, filters)
        render_executive_compression_check(shared, filters)
        render_what_feels_wrong_panel(shared, filters)
        render_review_snapshot_export(shared, filters)
    with tabs[1]:
        page_deployment_checklist(shared, filters)
    with tabs[2]:
        render_expandable_table("Pipeline health checks", shared["health"], FILES["pipeline_health"], height=460)
        download_center()


def app_header(shared):
    """Restrained product header for the simplified five-page app."""
    st.markdown(
        """
        <div class="workstation-card">
            <div class="section-kicker">US Residential Intelligence</div>
            <div class="signal-title">우미글로벌 미국 주거시장 전략 브리핑</div>
            <p class="muted-label">시장 변화, 개발 현황, GP 및 자본 흐름을 압축한 기관투자자형 모닝 브리프</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def is_detail_mode():
    """Top-level pages are executive-first; deeper material lives inside expanders."""
    return False


def is_review_mode():
    """Review tooling now lives only inside the system page."""
    return False


def legacy_main_17():
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()
    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)
    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("우미글로벌 미국 주거시장 전략 브리핑")

    pages = {
        "오늘의 브리핑": page_executive_briefing,
        "시장 인텔리전스": page_market_intelligence_product,
        "최근 개발 Activity": page_development_status_product,
        "GP / 자본 동향": page_gp_capital_product,
        "기사 모음": page_article_feed,
        "시스템 / 설정": page_system_settings_product,
    }
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)
    filters = {}
    app_header(shared)
    st.caption(f"최근 실행: {summary.get('run_timestamp', '실행 데이터 없음')}")
    st.divider()
    pages[page_name](shared, filters)
    st.divider()
    st.caption("US Residential Intelligence | Institutional Morning Brief")


def render_homepage_hot_market(shared, filters=None):
    """Describe observed market concentration without overstating article frequency."""
    st.markdown("### 오늘의 Hot Market / 시장 집중도")
    frames = [
        apply_filters(shared["cards"], filters),
        apply_filters(shared["opportunities"], filters),
        apply_filters(shared["high_confidence"], filters),
    ]
    markets = []
    transaction_markets = []
    for frame in frames:
        if frame is None or frame.empty or "market" not in frame.columns:
            continue
        for _, row in frame.iterrows():
            market = str(row.get("market", "")).strip()
            if not market:
                continue
            markets.append(market)
            blob = text_blob(row.to_dict())
            if any(term in blob for term in ["acquisition", "refinanc", "recap", "joint venture", "jv", "capital flow", "loan"]):
                transaction_markets.append(market)
    usable_markets = [market for market in transaction_markets if market.lower() not in {"other / unknown", "unknown", "other"}]
    if not usable_markets:
        st.markdown("**시장 집중도 분산**")
        st.write("현재 기사 관찰은 인허가 및 entitlement 공개 데이터 중심으로 많이 포착되고 있습니다. 이는 실제 개발 급증보다는 공개 인허가 데이터의 기사화 빈도가 높은 영향이 포함되어 있습니다.")
        st.write("현재 기사 기준으로 특정 시장에 거래 및 자본 흐름이 뚜렷하게 집중된다고 보기는 어렵습니다.")
        return
    counts = pd.Series(usable_markets).value_counts()
    top_market = counts.index[0]
    support = int(counts.iloc[0])
    if support < 2:
        st.markdown("**시장 집중도 분산**")
        st.write("현재 기사 기준으로 특정 시장에 거래 및 자본 흐름이 뚜렷하게 집중된다고 보기는 어렵습니다.")
        return
    st.markdown(f"**{top_market}**")
    st.write(f"최근 기사에서 거래, financing, recap 관련 사례가 {support}건 포착되었습니다. 다만 기사 관찰 밀도만으로 시장 과열을 단정하기보다는 후속 거래와 자본 흐름 확인이 필요합니다.")


def render_market_regime_summary(shared, filters=None):
    """Cautious market-regime summary based on observed news patterns."""
    st.markdown("### 시장 국면 요약")
    st.write("**자금조달 환경:** refinancing 부담이 주요 변수로 관찰됩니다.")
    st.write("**기관 activity:** 신규 acquisition보다 기존 포지션 관리와 selective recapitalization 중심으로 나타나고 있습니다.")
    st.write("**개발 / 인허가 흐름:** LA 개발 흐름은 affordable housing 인센티브를 활용한 entitlement 사례 중심으로 기사화되고 있습니다.")


def render_recent_market_signals(shared, filters=None):
    st.markdown("### 최근 시장 시그널")
    items = [
        (
            "LA entitlement / affordable approvals 반복 관찰",
            [
                "최근 기사에서 density bonus, affordable overlay, mixed-income approval 사례가 반복적으로 포착됩니다.",
                "이는 실제 공급 급증이라기보다, 인허가 precedent와 정책 인센티브 활용 사례가 기사화되고 있는 흐름으로 해석하는 것이 적절합니다.",
                "우미 입장에서는 LA site strategy와 entitlement precedent 검토 시 참고 가능한 관찰입니다.",
            ],
        ),
        (
            "기관 자본 recap / refinancing 사례 반복",
            [
                "기관 activity는 신규 acquisition보다 기존 포지션 관리와 selective recapitalization 중심으로 나타나고 있습니다.",
                "이는 refinancing 부담, lender relationship, recap opportunity를 함께 관찰해야 함을 시사합니다.",
                "아직 직접 투자기회라기보다는 자본시장 흐름을 읽기 위한 참고 신호로 보는 것이 적절합니다.",
            ],
        ),
        (
            "Sun Belt 공급 부담 지속 관찰",
            [
                "Sun Belt 관련 기사에서는 lease-up, concessions, new supply, absorption 관련 표현이 반복적으로 포착됩니다.",
                "이는 공급 정상화라기보다 최근 몇 년간 누적된 공급 물량을 시장이 얼마나 소화하고 있는지 확인해야 하는 국면으로 해석하는 것이 적절합니다.",
                "시장별 편차가 클 수 있으므로 단일 결론보다 지역별 후속 관찰이 필요합니다.",
            ],
        ),
    ]
    for title, bullets in items:
        st.markdown(f"**{title}**")
        for bullet in bullets:
            st.markdown(f"- {bullet}")


def render_woomi_market_checkpoints(shared, filters=None):
    st.markdown("### 우미 관점 체크포인트")
    st.markdown("- 현재 기사 기준으로는 refinancing 부담과 selective recap 사례를 함께 참고할 필요가 있습니다.")
    st.markdown("- LA entitlement 관찰은 site strategy와 인허가 precedent 검토에 유용하지만, 아직 시장 전반의 공급 가속으로 결론 내리기는 어렵습니다.")
    st.markdown("- Sun Belt 관련 표현은 반복 포착되고 있으나 시장별 편차가 크므로 후속 관찰이 필요합니다.")
    st.markdown("- 직접 투자기회라기보다 시장 흐름을 읽기 위한 참고 신호가 많으며, 데이터가 누적되면 판단 강도를 높일 수 있습니다.")


def explicit_risk_row(row):
    blob = text_blob(row)
    return any(term in blob for term in [
        "distress", "default", "maturity pressure", "refinancing gap", "stalled project",
        "construction delay", "lease-up stress", "concessions", "vacancy pressure", "entitlement delay",
    ])


def render_market_case_section(title, intro, df, score_columns, source_path, shared, limit=4):
    """Concise market-example cards with evidence hidden by default."""
    st.markdown(f"### {title}")
    st.write(intro)
    if df.empty:
        missing_file_message(source_path)
        return
    for _, row in sort_by_score(df, score_columns).head(limit).iterrows():
        item = row.to_dict()
        with st.container(border=True):
            st.markdown(f"**{get_title(item)}**")
            metadata = " · ".join([value for value in [get_market(item), get_gp(item), get_lender(item)] if value])
            if metadata:
                st.caption(metadata)
            st.write(get_reason(item))
            source = get_first(item, ["source", "source_report"], "")
            if source:
                st.caption(f"Source: {source}")
            with st.expander("상세 근거 보기", expanded=False):
                st.write(f"**관련 시장:** {get_market(item)}")
                st.write(f"**관련 GP / lender:** {get_gp(item) or '미확인'} / {get_lender(item) or '미확인'}")
                article_preview(item)


def page_market_intelligence_product(shared, filters):
    st.title("시장 인텔리전스")
    render_market_regime_summary(shared, filters)
    render_market_case_section(
        "최근 거래 사례",
        "최근 기사에서 포착된 거래 및 financing 사례입니다. 직접 투자기회라기보다는 현재 시장에서 어떤 유형의 딜이 실제로 진행되고 있는지 참고하기 위한 사례로 보는 것이 적절합니다.",
        apply_filters(shared["opportunities"], filters),
        ["opportunity_score"],
        FILES["opportunities"],
        shared,
        limit=4,
    )
    render_homepage_hot_market(shared, filters)
    render_recent_market_signals(shared, filters)
    render_woomi_market_checkpoints(shared, filters)
    distress = apply_filters(shared["distress"], filters)
    monitoring = distress if distress.empty else distress[distress.apply(lambda row: explicit_risk_row(row.to_dict()), axis=1)]
    if monitoring.empty:
        monitoring = distress
    render_market_case_section(
        "추가 모니터링 사례",
        "아래 항목은 즉각적인 리스크라기보다 후속 관찰이 필요한 시장 사례입니다. refinancing, bridge loan, construction financing 등은 상황에 따라 기회 또는 리스크로 해석될 수 있으므로 추가 확인이 필요합니다.",
        monitoring,
        ["distress_score"],
        FILES["distress"],
        shared,
        limit=4,
    )


DEVELOPMENT_CATEGORY_TERMS = {
    "approval": [
        "permit", "permitting", "entitlement", "zoning", "rezoning", "ceqa",
        "hud review", "density bonus", "approval", "planning commission",
        "environmental review", "affordable overlay", "conditional approval",
    ],
    "construction": [
        "wood framing", "framing takes shape", "vertical construction",
        "construction started", "starts construction", "construction start",
        "broke ground", "breaks ground", "under construction", "topping out",
        "topped out", "delivery", "delivered", "opening", "opened",
        "completion", "completed", "lease-up", "lease up", "occupancy",
        "move-ins", "absorption",
    ],
    "site": [
        "acquisition", "site acquisition", "parcel", "assemblage", "redevelopment",
        "land trade", "sponsor entry", "development site", "site control",
        "land purchase", "land acquisition", "site assemblage", "parcel disposition",
    ],
}

DEVELOPMENT_EXCLUSION_TERMS = {
    "refinancing": ["refinancing", "refinanced", "recap", "recapitalization", "loan maturity"],
    "construction_financing": ["construction financing", "construction loan", "bridge loan"],
    "non_site_acquisition": ["lease-up", "lease up", "completion", "delivered", "delivery"],
}

PRIMARY_DEVELOPMENT_CATEGORY_MAP = {
    "approval_watch": "approval",
    "construction_delivery_watch": "construction",
    "site_parcel_activity": "site",
    "excluded": "",
}


def development_monitor_universe(shared):
    """Combine existing development outputs into one read-only monitor universe."""
    frames = [
        shared["development_lifecycle"],
        shared["entitlement_intelligence"],
        shared["la_entitlement"],
        shared["asset_parcel_intelligence"],
        shared["la_assets"],
        shared["timing_intelligence"],
    ]
    available = [frame.copy() for frame in frames if frame is not None and not frame.empty]
    if not available:
        return pd.DataFrame()
    combined = pd.concat(available, ignore_index=True, sort=False)
    combined["_dev_blob"] = combined.apply(lambda row: text_blob(row.to_dict()), axis=1)
    combined["_dev_title"] = combined.apply(lambda row: development_article_title(row.to_dict()), axis=1)
    combined["_normalized_dev_title"] = combined["_dev_title"].apply(normalize_development_title)
    combined["_dev_key"] = combined.apply(
        lambda row: str(get_url(row.to_dict()) or row["_dev_title"]).strip().lower(),
        axis=1,
    )
    combined = combined.drop_duplicates("_dev_key", keep="first")
    combined["_primary_development_category"] = combined.apply(
        lambda row: classify_primary_development_category(row.to_dict()),
        axis=1,
    )
    category_priority = {"construction": 0, "approval": 1, "site": 2, "": 3}
    combined["_category_priority"] = combined["_primary_development_category"].map(category_priority).fillna(3)
    write_development_routing_diagnostics(combined)
    combined = combined.sort_values("_category_priority")
    combined = combined.drop_duplicates("_normalized_dev_title", keep="first")
    return combined


def has_any_term(blob, terms):
    return any(term in blob for term in terms)


def development_article_title(row):
    """Prefer the original article title when routing development activity."""
    return truncate_text(
        get_first(
            row,
            ["source_article_title", "evidence_article_title", "title"],
            get_title(row),
        )
    )


def normalize_development_title(value):
    """Normalize one headline for cross-section dedupe."""
    text = str(value or "")
    if text.count(" - ") >= 2:
        text = text.split(" - ", 2)[-1]
    text = text.lower().replace("...", " ")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def development_address_key(value):
    """Extract a lightweight address-like key for duplicate development stories."""
    normalized = normalize_development_title(value)
    match = re.search(
        r"\b\d{2,6}\s+(?:[nesw]\s+)?[a-z0-9 ]+?\s+(?:rd|road|st|street|ave|avenue|blvd|boulevard|dr|drive)\b",
        normalized,
    )
    return match.group(0) if match else ""


def development_identity_key(row):
    """Build the strongest available identity key for one displayed development row."""
    normalized_url = str(get_url(row) or "").strip().lower()
    if normalized_url:
        return f"url:{normalized_url}"
    address_key = development_address_key(text_blob(row))
    if address_key:
        return f"address:{address_key}"
    return f"title:{normalize_development_title(development_article_title(row))}"


def write_development_routing_diagnostics(universe):
    """Write a quiet diagnostic file for duplicate or misrouted development rows."""
    if universe.empty:
        return
    diagnostics = []
    visible = universe[universe["_primary_development_category"].isin(["construction", "approval", "site"])]
    for normalized_title, rows in visible.groupby("_normalized_dev_title"):
        categories = sorted(set(rows["_primary_development_category"]))
        if len(categories) > 1:
            diagnostics.append({
                "normalized_title": normalized_title,
                "issue": "duplicate_visible_categories",
                "categories": "; ".join(categories),
                "article_count": len(rows),
            })
    mission_rows = visible[
        visible["_normalized_dev_title"].str.contains("1321 n mission rd", na=False)
    ]
    if not mission_rows.empty:
        categories = sorted(set(mission_rows["_primary_development_category"]))
        if categories != ["construction"]:
            diagnostics.append({
                "normalized_title": "1321 n mission rd",
                "issue": "mission_rd_wrong_category",
                "categories": "; ".join(categories),
                "article_count": len(mission_rows),
            })
    diagnostic_path = OUTPUT_DIR / "development_routing_diagnostics.csv"
    if diagnostics:
        pd.DataFrame(diagnostics).to_csv(diagnostic_path, index=False, encoding="utf-8")
    else:
        pd.DataFrame(
            columns=["normalized_title", "issue", "categories", "article_count"]
        ).to_csv(diagnostic_path, index=False, encoding="utf-8")


def classify_primary_development_category(row):
    """Assign exactly one development category, or exclude the article from this page."""
    upstream_category = str(row.get("primary_development_category", "") or "").strip()
    if upstream_category in PRIMARY_DEVELOPMENT_CATEGORY_MAP:
        return PRIMARY_DEVELOPMENT_CATEGORY_MAP[upstream_category]
    blob = text_blob(row)
    if has_any_term(blob, DEVELOPMENT_EXCLUSION_TERMS["refinancing"]):
        return ""
    has_execution = has_any_term(blob, DEVELOPMENT_CATEGORY_TERMS["construction"])
    has_approval = has_any_term(blob, DEVELOPMENT_CATEGORY_TERMS["approval"])
    has_site = has_any_term(blob, DEVELOPMENT_CATEGORY_TERMS["site"])
    financing_only = has_any_term(blob, DEVELOPMENT_EXCLUSION_TERMS["construction_financing"]) and not has_execution
    if financing_only:
        return ""
    # Priority routing: execution milestone > approval precedent > site entry.
    if has_execution:
        return "construction"
    if has_approval:
        return "approval"
    if has_site and not has_any_term(blob, DEVELOPMENT_EXCLUSION_TERMS["non_site_acquisition"]):
        return "site"
    return ""


def development_watch_rows(shared, category):
    universe = development_monitor_universe(shared)
    if universe.empty:
        return universe
    matched = universe[universe["_primary_development_category"] == category]
    score_columns = [
        "entitlement_opportunity_score", "local_relevance_score", "lifecycle_opportunity_score",
        "asset_opportunity_score", "la_asset_opportunity_score", "timing_urgency_score",
    ]
    ranked = sort_by_score(matched, score_columns)
    return diversify_development_rows(ranked, limit=10)


def dedupe_development_sections(section_rows):
    """Apply one final cross-section headline dedupe before rendering."""
    seen_identity_keys = set()
    cleaned = {}
    for category, rows in section_rows:
        if rows.empty:
            cleaned[category] = rows
            continue
        keep_indices = []
        for index, row in rows.iterrows():
            item = row.to_dict()
            identity_key = development_identity_key(item)
            if identity_key in seen_identity_keys:
                continue
            seen_identity_keys.add(identity_key)
            keep_indices.append(index)
        cleaned[category] = rows.loc[keep_indices]
    return cleaned


def normalized_headline(value):
    text = str(value or "").lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def headline_similarity(left, right):
    return SequenceMatcher(None, normalized_headline(left), normalized_headline(right)).ratio()


def development_metro(row):
    metro = get_first(row, ["city_or_submarket", "la_submarket", "city", "market"], "Unknown")
    metro = str(metro).strip()
    if metro in {"", "Unknown", "Other / Unknown"}:
        return "Unknown"
    return metro


def development_region(row):
    blob = text_blob(row)
    if any(term in blob for term in ["los angeles", "california", "seattle", "portland", "san francisco", "bay area"]):
        return "West Coast"
    if any(term in blob for term in ["sun belt", "texas", "florida", "phoenix", "atlanta", "nashville", "charlotte", "raleigh"]):
        return "Sun Belt"
    if any(term in blob for term in ["new york", "new jersey", "boston", "washington", "virginia", "philadelphia"]):
        return "East Coast"
    return "Midwest / Other"


def article_freshness_bonus(row):
    blob = " ".join(str(row.get(field, "")) for field in ["url", "timing_reference", "delivery_or_timing_reference", "source_article_title"])
    years = [int(year) for year in re.findall(r"\b20\d{2}\b", blob)]
    if not years:
        return 0
    newest = max(years)
    current_year = datetime.now().year
    if newest >= current_year:
        return 12
    if newest == current_year - 1:
        return 4
    return -8


def development_display_score(row):
    return get_score(row) + article_freshness_bonus(row)


def diversify_development_rows(df, limit=10):
    """Apply dedupe, metro/source caps, and soft regional balancing before display."""
    if df.empty:
        return df
    working = df.copy()
    working["_display_score"] = working.apply(lambda row: development_display_score(row.to_dict()), axis=1)
    working["_metro"] = working.apply(lambda row: development_metro(row.to_dict()), axis=1)
    working["_source"] = working.apply(lambda row: development_source_label(row.to_dict()), axis=1)
    working["_region"] = working.apply(lambda row: development_region(row.to_dict()), axis=1)
    working = working.sort_values("_display_score", ascending=False)
    region_targets = {"West Coast": 0.35, "Sun Belt": 0.35, "East Coast": 0.20, "Midwest / Other": 0.10}
    metro_counts = {}
    source_counts = {}
    region_counts = {}
    selected = []
    selected_titles = []
    for _, row in working.iterrows():
        item = row.to_dict()
        title = get_title(item)
        if any(headline_similarity(title, seen) >= 0.85 for seen in selected_titles):
            continue
        metro = item["_metro"]
        source = item["_source"]
        region = item["_region"]
        if metro != "Unknown" and metro_counts.get(metro, 0) >= 3:
            continue
        if source != "Source 미확인" and source_counts.get(source, 0) >= 2:
            continue
        target_count = max(1, round(limit * region_targets.get(region, 0.10)))
        if region_counts.get(region, 0) >= target_count and len(selected) < max(4, limit // 2):
            continue
        selected.append(row)
        selected_titles.append(title)
        metro_counts[metro] = metro_counts.get(metro, 0) + 1
        source_counts[source] = source_counts.get(source, 0) + 1
        region_counts[region] = region_counts.get(region, 0) + 1
        if len(selected) >= limit:
            break
    if len(selected) < min(limit, len(working)):
        for _, row in working.iterrows():
            if len(selected) >= limit:
                break
            item = row.to_dict()
            title = get_title(item)
            if any(headline_similarity(title, seen) >= 0.85 for seen in selected_titles):
                continue
            metro = item["_metro"]
            source = item["_source"]
            if metro != "Unknown" and metro_counts.get(metro, 0) >= 3:
                continue
            if source != "Source 미확인" and source_counts.get(source, 0) >= 2:
                continue
            selected.append(row)
            selected_titles.append(title)
            metro_counts[metro] = metro_counts.get(metro, 0) + 1
            source_counts[source] = source_counts.get(source, 0) + 1
    return pd.DataFrame(selected)


def development_market_label(row):
    market = get_market(row)
    if market and market != "Unknown":
        return market
    return truncate_text(
        get_first(
            row,
            ["related_market", "city_or_submarket", "la_submarket", "neighborhood_or_submarket", "city"],
            "Market not specified",
        ),
        90,
    )


def development_source_label(row):
    return get_first(row, ["source", "source_report"], "Source not specified")


def development_woomi_angle(row, category):
    if category == "approval":
        return "인허가 precedent, density incentive 활용, local approval path를 비교 검토할 참고 사례입니다."
    if category == "construction":
        return "실제 execution 속도와 delivery / lease-up timing을 판단할 비교 사례입니다."
    return "site control과 sponsor entry 흐름을 읽기 위한 sourcing 참고 사례입니다."


def render_development_pipeline_card(row, category):
    item = row.to_dict() if hasattr(row, "to_dict") else row
    title = get_title(item)
    sponsor = get_gp(item) or get_first(item, ["owner_or_sponsor"], "Sponsor 미확인")
    stage = get_lifecycle_stage(item) or get_first(item, ["entitlement_stage", "execution_stage", "construction_status"], "단계 미확인")
    category_reason = get_first(item, ["primary_category_reason"], "")
    headline = f"{title} | {development_market_label(item)} · {development_source_label(item)} · {stage}"
    with st.expander(headline, expanded=False):
        st.caption(f"GP / sponsor: {sponsor}")
        st.write(f"**Why it matters:** {get_reason(item)}")
        st.write(f"**Woomi angle:** {development_woomi_angle(item, category)}")
        st.write(f"**Lifecycle stage:** {stage}")
        if category_reason:
            st.write(f"**Category reason:** {category_reason}")
        url = get_url(item)
        if isinstance(url, str) and url.startswith("http"):
            st.markdown(f"[Read original article]({url})")


def render_development_watch_section(title, intro, rows, category, limit=8):
    st.markdown(f"### {title}")
    st.write(intro)
    if rows.empty:
        st.caption("현재 기사 기준으로 해당 흐름은 충분히 포착되지 않았습니다.")
        return
    for _, row in rows.head(limit).iterrows():
        render_development_pipeline_card(row, category)


def render_development_activity_summary(shared):
    st.markdown("### 최근 개발 Activity 요약")
    approval = development_watch_rows(shared, "approval")
    construction = development_watch_rows(shared, "construction")
    site = development_watch_rows(shared, "site")
    approval_la = approval["_dev_blob"].str.contains("los angeles|california|la |koreatown|dtla", regex=True).sum() if not approval.empty else 0
    construction_sunbelt = construction["_dev_blob"].str.contains("sun belt|texas|florida|phoenix|atlanta|nashville|charlotte|raleigh", regex=True).sum() if not construction.empty else 0
    execution_count = len(construction)
    refinancing_count = 0
    universe = development_monitor_universe(shared)
    if not universe.empty:
        refinancing_count = int(universe["_dev_blob"].str.contains("refinanc|recap|loan maturity", regex=True).sum())
    bullets = []
    if approval_la:
        bullets.append("LA / California affordable entitlement 사례가 반복적으로 관찰됩니다.")
    if construction_sunbelt:
        bullets.append("Sun Belt에서 delivery 및 lease-up activity 관련 기사가 이어지고 있습니다.")
    if execution_count > refinancing_count:
        bullets.append("최근 개발 기사에서는 refinancing보다 실제 development execution 관련 사례가 더 많이 포착됩니다.")
    if site.empty:
        bullets.append("site / parcel activity는 아직 제한적으로 포착되어 후속 관찰이 필요합니다.")
    for bullet in bullets[:3] or ["현재 기사 기준으로 approval, construction, site-control 흐름을 함께 추적할 필요가 있습니다."]:
        st.markdown(f"- {bullet}")


def render_homepage_development_status(shared, filters=None):
    """Summarize development activity without exposing internal taxonomy buckets."""
    render_development_activity_summary(shared)


def page_development_status_product(shared, filters):
    st.title("최근 개발 Activity")
    render_development_activity_summary(shared)
    render_development_watch_section(
        "인허가 / Approval Watch",
        "entitlement, zoning, density bonus, permit issuance, affordable overlay, CEQA, HUD review 관련 기사 흐름입니다.",
        development_watch_rows(shared, "approval"),
        "approval",
        limit=8,
    )
    render_development_watch_section(
        "Construction / Delivery Watch",
        "construction start, lease-up, delivery, opening, absorption 등 실제 실행 흐름을 보여주는 기사입니다.",
        development_watch_rows(shared, "construction"),
        "construction",
        limit=8,
    )
    render_development_watch_section(
        "Site / Parcel Activity",
        "site acquisition, land assemblage, parcel trade, redevelopment, sponsor entry 관련 부지 선행 신호입니다.",
        development_watch_rows(shared, "site"),
        "site",
        limit=8,
    )


def page_development_status_product(shared, filters):
    """Render one deduped Recent Development Activity surface."""
    st.title("최근 개발 Activity")
    render_development_activity_summary(shared)
    section_rows = dedupe_development_sections([
        ("construction", development_watch_rows(shared, "construction")),
        ("approval", development_watch_rows(shared, "approval")),
        ("site", development_watch_rows(shared, "site")),
    ])
    render_development_watch_section(
        "Construction / Delivery Watch",
        "construction start, lease-up, delivery, opening, absorption 등 실제 실행 흐름을 보여주는 기사입니다.",
        section_rows["construction"],
        "construction",
        limit=8,
    )
    render_development_watch_section(
        "인허가 / Approval Watch",
        "entitlement, zoning, density bonus, permit issuance, affordable overlay, CEQA, HUD review 관련 기사 흐름입니다.",
        section_rows["approval"],
        "approval",
        limit=8,
    )
    render_development_watch_section(
        "Site / Parcel Activity",
        "site acquisition, land assemblage, parcel trade, redevelopment, sponsor entry 관련 부지 진입 신호입니다.",
        section_rows["site"],
        "site",
        limit=8,
    )


ARTICLE_CATEGORY_TERMS = {
    "market": [
        "oversupply", "absorption", "vacancy", "rent growth", "concession",
        "concessions", "construction cost", "labor cost", "insurance cost",
        "developer sentiment", "construction data", "housing starts",
        "starts data", "permits data", "permits and starts", "fed", "interest rate", "rates", "treasury",
        "treasury yield", "sofr", "bank lending", "lending environment",
        "mansion tax", "rent control", "housing policy", "zoning reform",
        "affordable housing policy", "california regulation", "macro",
        "market outlook", "sentiment", "policy", "bill", "legislation",
        "mandate", "house", "senate", "white house", "regulation", "tax",
        "developers pull back", "pull back on new builds", "cautious builders",
        "permits weaken", "new builds", "supply pressure", "economy",
        "inflation", "cap rate",
    ],
    "development": [
        "entitlement", "permit", "permitting", "zoning", "approval",
        "proposed development", "planned project", "development plan",
        "site acquisition", "land purchase", "parcel", "groundbreaking",
        "breaks ground", "broke ground", "construction start",
        "construction starts", "construction started", "construction begins",
        "work begins", "site prep", "site preparation", "under construction",
        "vertical construction", "delivery", "completion", "completed",
        "opens", "opened", "tops out", "filed plans", "application filed",
        "permit filed", "entitlement filed", "proposed apartments",
        "proposed housing", "development proposed", "project proposed",
        "grand opening", "opening celebration", "advances toward construction",
        "advance toward construction", "toward construction",
        "project paused", "shelved", "cancelled",
    ],
    "gp_capital": [
        "platform acquisition", "company acquisition", "stake acquisition",
        "portfolio acquisition", "portfolio sale", "large acquisition",
        "disposition", "large disposition", "joint venture", "jv",
        "recapitalization", "recap", "preferred equity", "rescue capital",
        "construction loan", "bridge loan", "refinancing", "inventory loan",
        "debt financing", "equity financing", "equity syndication", "loan closing",
        "capital partner", "institutional investor", "blackstone",
        "brookfield", "berkshire hathaway", "greystar", "related",
        "kennedy wilson", "harrison street", "pccp", "jll", "cbre",
        "walker & dunlop", "berkadia",
    ],
}

ARTICLE_DEVELOPMENT_EXECUTION_TERMS = [
    "entitlement",
    "permit",
    "permitting",
    "zoning",
    "approval",
    "proposed development",
    "planned project",
    "development plan",
    "site acquisition",
    "land purchase",
    "land assemblage",
    "redevelopment site",
    "parcel acquisition",
    "broke ground",
    "breaks ground",
    "groundbreaking",
    "construction start",
    "construction starts",
    "construction started",
    "construction begins",
    "work begins",
    "site prep",
    "site preparation",
    "under construction",
    "vertical construction",
    "filed plans",
    "application filed",
    "permit filed",
    "entitlement filed",
    "proposed apartments",
    "proposed housing",
    "development proposed",
    "project proposed",
    "tops out",
    "grand opening",
    "opening celebration",
    "advances toward construction",
    "advance toward construction",
    "toward construction",
    "opened",
    "opens",
    "completed",
    "completion",
    "delivered",
    "delivery",
    "project paused",
    "shelved",
    "cancelled",
]

ARTICLE_MARKET_FINANCE_TERMS = [
    "refinancing", "recapitalization", "recap", "loan", "loan closing",
    "mortgage", "debt", "bridge loan", "construction loan",
    "inventory loan", "debt financing", "equity financing", "equity syndication",
    "preferred equity", "rescue capital", "capital partner",
]

ARTICLE_GP_CAPITAL_TRANSACTION_TERMS = [
    "platform acquisition", "company acquisition", "stake acquisition",
    "portfolio acquisition", "portfolio sale", "acquisition", "acquires",
    "acquired", "sale", "sells", "sold", "disposition", "joint venture",
    "jv", "recapitalization", "recap", "preferred equity", "rescue capital",
    "construction loan", "bridge loan", "refinancing", "inventory loan",
    "debt financing", "equity financing", "equity syndication", "loan closing",
]

ARTICLE_MARKET_DATA_TERMS = [
    "construction data", "housing starts", "permits and starts",
    "starts data", "permits data", "market data", "market outlook",
    "construction time", "apartment construction time", "development time",
    "oversupply", "absorption", "vacancy", "rent growth", "concessions",
    "construction cost", "labor cost", "insurance cost",
    "developer sentiment", "developer confidence", "sentiment", "fed", "interest rate",
    "treasury yield", "sofr", "lending environment", "bank lending",
    "mansion tax", "rent control", "housing policy", "zoning reform",
    "affordable housing policy", "california regulation", "macro",
    "developers pull back", "pull back on new builds", "cautious builders",
    "permits weaken", "new builds", "supply pressure",
]

ARTICLE_MARKET_POLICY_TERMS = [
    "policy", "bill", "legislation", "mandate", "house", "senate",
    "white house", "regulation", "tax", "mansion tax", "rent control",
    "housing bill", "road to housing bill", "zoning reform",
    "affordable housing policy", "california regulation",
]

ARTICLE_GP_CAPITAL_ACTOR_TERMS = [
    "jll", "cbre", "walker & dunlop", "berkadia", "blackstone",
    "brookfield", "berkshire hathaway",
]

ARTICLE_GP_CAPITAL_ACTION_TERMS = [
    "arranged", "arranges", "secured", "secures", "provided", "provides",
    "launches", "launched", "launch",
]

ARTICLE_GP_CAPITAL_DEBT_PLATFORM_TERMS = [
    "loan", "refinancing", "financing", "debt", "lending platform",
    "mortgage division", "debt strategies", "financing platform",
]

ARTICLE_GP_CAPITAL_SALE_SCALE_TERMS = [
    "seeks buyers", "seeking buyers", "sale mandate", "portfolio",
    "portfolio sale", "apartment portfolio", "apartments",
]

ARTICLE_PROJECT_SPECIFIC_TERMS = [
    "specific project", "project would", "project will", "planned project",
    "proposed development", "development plan", "site acquisition",
    "land purchase", "parcel acquisition", "land assemblage",
    "breaks ground", "broke ground", "groundbreaking", "construction start",
    "construction starts", "construction begins", "site prep",
    "site preparation", "work begins", "under construction", "filed plans",
    "application filed", "permit filed", "entitlement filed",
    "proposed apartments", "proposed housing", "development proposed",
    "project proposed", "grand opening", "opening celebration",
    "advances toward construction", "advance toward construction",
    "toward construction", "tops out", "delivery", "completion", "opens",
    "project paused", "shelved", "cancelled",
]

ARTICLE_SITE_TERMS = ["site", "land", "parcel"]
ARTICLE_SITE_ACTION_TERMS = [
    "acquisition", "purchase", "assemblage", "bought", "buys", "acquired",
    "development site", "redevelopment site", "prep", "preparation",
    "underway", "work begins",
]

ARTICLE_ACCESS_LIMITED_SOURCE_TERMS = [
    "urbanize", "urbanize la", "urbanize atlanta", "urbanize chicago",
    "urbanize new york", "sf yimby",
]

ARTICLE_ACCESS_LIMITED_URL_TERMS = [
    "urbanize.city", "sfyimby.com",
]

ARTICLE_ACCESS_LIMITED_WARNING_TERMS = [
    "subscribe", "subscription", "sign in", "log in",
    "free articles remaining", "paywall", "advertisement",
    "skip to main content advertisement",
]


def article_feed_source(shared):
    """Prefer articles.csv, then fall back to existing intelligence outputs."""
    articles = shared.get("articles", pd.DataFrame())
    if articles is not None and not articles.empty:
        return articles.copy()
    fallback_frames = [
        shared["cards"],
        shared["opportunities"],
        read_csv_safely(str(OUTPUT_DIR / "deal_pipeline.csv")),
        shared["gp_watchlist"],
        shared["asset_parcel_intelligence"],
    ]
    available = [frame.copy() for frame in fallback_frames if frame is not None and not frame.empty]
    return pd.concat(available, ignore_index=True, sort=False) if available else pd.DataFrame()


def is_access_limited_article(row):
    source_blob = " ".join(
        str(row.get(field, "") or "").lower()
        for field in ["source", "source_report", "platform_type"]
    )
    url = str(row.get("url", "") or row.get("source_url_if_available", "") or "").lower()
    return (
        any(source in source_blob for source in ARTICLE_ACCESS_LIMITED_SOURCE_TERMS)
        or any(term in url for term in ARTICLE_ACCESS_LIMITED_URL_TERMS)
    )


def article_feed_text_parts(row):
    title = str(row.get("title", "") or row.get("card_title", "") or row.get("source_article_title", "") or "")
    source = str(row.get("source", "") or row.get("source_report", "") or row.get("platform_type", "") or "")
    summary = " ".join(
        str(row.get(field, "") or "")
        for field in [
            "summary",
            "article_text_sample",
            "why_it_matters",
            "strategic_implication",
            "reason_for_inclusion",
            "market_signal",
        ]
    )
    url = str(row.get("url", "") or row.get("source_url_if_available", "") or "")
    return {
        "title": title.lower(),
        "source": source.lower(),
        "summary": summary.lower(),
        "url": url.lower(),
        "display": " ".join([title, source, summary, url]).lower(),
    }


def article_feed_has_term(term, text):
    if not term:
        return False
    if re.search(r"[a-z0-9]$", term):
        return re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", text) is not None
    return term in text


def article_feed_matching_terms(terms, text, limit=4):
    return [term for term in terms if article_feed_has_term(term, text)][:limit]


def article_feed_term_score(terms, parts, strong=False):
    title_matches = article_feed_matching_terms(terms, parts["title"])
    source_matches = article_feed_matching_terms(terms, parts["source"])
    summary_matches = article_feed_matching_terms(terms, parts["summary"])
    url_matches = article_feed_matching_terms(terms, parts["url"])
    base = 4 if strong else 2
    score = 0
    score += len(title_matches) * (base + 2)
    score += len(source_matches) * (base + 1)
    score += len(summary_matches) * base
    score += len(url_matches)
    matches = []
    for term in [*title_matches, *source_matches, *summary_matches, *url_matches]:
        if term not in matches:
            matches.append(term)
    return score, matches[:5]


def has_accessible_article_body(row):
    parts = article_feed_text_parts(row)
    body = " ".join([parts["summary"], parts["display"]])
    sample = str(row.get("article_text_sample", "") or row.get("summary", "") or "")
    has_long_sample = len(sample.strip()) >= 500
    has_paywall_text = any(term in body for term in ARTICLE_ACCESS_LIMITED_WARNING_TERMS)
    return has_long_sample and not has_paywall_text


def article_feed_confidence(top_score, second_score, reason_count, access_limited=False, override=False):
    if override or (top_score >= 8 and top_score - second_score >= 3):
        return "medium" if access_limited else "high"
    if top_score >= 4:
        return "medium"
    if top_score >= 3 and reason_count:
        return "medium"
    return "low"


def classify_article_feed_row(row):
    primary_section = str(row.get("primary_display_section", "") or "").strip().lower()
    parts = article_feed_text_parts(row)
    display = parts["display"]
    title_summary = " ".join(
        str(row.get(field, "") or "").lower()
        for field in ["title", "summary", "article_text_sample"]
    )
    limited_source = is_access_limited_article(row)

    market_score, market_matches = article_feed_term_score(ARTICLE_MARKET_DATA_TERMS, parts, strong=True)
    market_policy_score, market_policy_matches = article_feed_term_score(ARTICLE_MARKET_POLICY_TERMS, parts, strong=True)
    development_score, development_matches = article_feed_term_score(ARTICLE_DEVELOPMENT_EXECUTION_TERMS, parts, strong=True)
    capital_score, capital_matches = article_feed_term_score(ARTICLE_GP_CAPITAL_TRANSACTION_TERMS, parts, strong=True)
    capital_name_score, capital_name_matches = article_feed_term_score(ARTICLE_CATEGORY_TERMS["gp_capital"], parts)
    finance_score, finance_matches = article_feed_term_score(ARTICLE_MARKET_FINANCE_TERMS, parts, strong=True)
    capital_score += capital_name_score + finance_score
    capital_matches = [*capital_matches, *capital_name_matches, *finance_matches][:5]

    has_policy_override = bool(article_feed_matching_terms(ARTICLE_MARKET_POLICY_TERMS, title_summary))
    has_market_data_title = bool(article_feed_matching_terms(ARTICLE_MARKET_DATA_TERMS, title_summary))
    gp_actor_matches = article_feed_matching_terms(ARTICLE_GP_CAPITAL_ACTOR_TERMS, title_summary)
    gp_action_matches = article_feed_matching_terms(ARTICLE_GP_CAPITAL_ACTION_TERMS, title_summary)
    gp_debt_platform_matches = article_feed_matching_terms(ARTICLE_GP_CAPITAL_DEBT_PLATFORM_TERMS, title_summary)
    gp_sale_scale_matches = article_feed_matching_terms(ARTICLE_GP_CAPITAL_SALE_SCALE_TERMS, title_summary)
    has_gp_debt_arranger = bool(gp_actor_matches and gp_action_matches and gp_debt_platform_matches)
    has_gp_debt_platform = bool(gp_actor_matches and gp_debt_platform_matches)
    has_gp_sale_scale = bool(gp_sale_scale_matches and re.search(r"\b\d{3,}[\d,]*\b", title_summary))
    has_lender_side_capability = bool(
        article_feed_matching_terms(["mortgage division", "lending platform", "financing platform", "debt strategies"], title_summary)
    )
    has_site_action = (
        bool(article_feed_matching_terms(ARTICLE_SITE_TERMS, title_summary))
        and bool(article_feed_matching_terms(ARTICLE_SITE_ACTION_TERMS, title_summary))
    )
    if has_site_action:
        development_score += 5
        if "site/land/parcel action" not in development_matches:
            development_matches.append("site/land/parcel action")

    if limited_source and not has_accessible_article_body(row):
        return {
            "category": "access_limited",
            "confidence": "low",
            "reason": "source is access-limited and article body/snippet is not reliable enough",
        }

    # Priority exceptions prevent keyword drift: policy/data beats transaction
    # words, while true site-prep/groundbreaking/filing milestones beat generic
    # market language.
    if has_policy_override:
        market_score += 8
        category = "market"
        reason = "policy/bill/regulation signal: " + ", ".join(market_policy_matches)
        confidence = article_feed_confidence(market_score, max(development_score, capital_score), len(market_policy_matches), limited_source, override=True)
    elif has_market_data_title:
        market_score += 6
        category = "market"
        reason = "market data signal: " + ", ".join(market_matches or article_feed_matching_terms(ARTICLE_MARKET_DATA_TERMS, title_summary))
        confidence = article_feed_confidence(market_score, max(development_score, capital_score), len(market_matches), limited_source, override=True)
    elif has_gp_debt_arranger or has_gp_debt_platform or has_gp_sale_scale or has_lender_side_capability:
        capital_score += 8
        category = "gp_capital"
        capital_override_matches = [
            *gp_actor_matches,
            *gp_action_matches,
            *gp_debt_platform_matches,
            *gp_sale_scale_matches,
        ]
        reason_terms = []
        for term in capital_override_matches:
            if term not in reason_terms:
                reason_terms.append(term)
        reason = "gp_capital transaction/platform signal: " + ", ".join(reason_terms or ["lender-side capability"])
        confidence = article_feed_confidence(capital_score, max(market_score, development_score), len(reason_terms), limited_source, override=True)
    else:
        scores = {
            "market": market_score,
            "development": development_score,
            "gp_capital": capital_score,
        }
        sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        category, top_score = sorted_scores[0]
        second_score = sorted_scores[1][1]
        match_map = {
            "market": market_matches,
            "development": development_matches,
            "gp_capital": capital_matches,
        }
        if top_score < 3:
            return {
                "category": "review",
                "confidence": "low",
                "reason": "not enough article evidence for market/development/gp_capital",
            }
        confidence = article_feed_confidence(top_score, second_score, len(match_map[category]), limited_source)
        if confidence == "low":
            return {
                "category": "review",
                "confidence": "low",
                "reason": "weak or conflicting category signals",
            }
        reason = f"{category} signal: " + ", ".join(match_map[category] or ["collector context"])

    if primary_section == "market intelligence" and category == "review":
        category, confidence, reason = "market", "medium", "collector routed this article to market intelligence"
    if primary_section == "development activity" and category == "review":
        category, confidence, reason = "development", "medium", "collector routed this article to development activity"
    if primary_section == "gp / capital activity" and category == "review":
        category, confidence, reason = "gp_capital", "medium", "collector routed this article to gp/capital activity"

    if not display.strip():
        return {
            "category": "review",
            "confidence": "low",
            "reason": "missing title/source/summary/url evidence",
        }
    return {
        "category": category,
        "confidence": confidence,
        "reason": reason,
    }


def article_feed_category(row):
    return classify_article_feed_row(row)["category"]


def article_feed_rows(shared):
    df = article_feed_source(shared)
    if df.empty:
        return df
    rows = df.copy()
    rows["_article_title"] = rows.apply(lambda row: get_title(row.to_dict()), axis=1)
    rows["_original_order"] = range(len(rows))
    rows["_published_dt"] = pd.to_datetime(rows.get("published"), errors="coerce", utc=True)
    rows["_collected_dt"] = pd.to_datetime(rows.get("collected_at"), errors="coerce", utc=True)
    rows["_title_sort"] = rows["_article_title"].fillna("").astype(str)
    rows = rows.sort_values(
        ["_published_dt", "_collected_dt", "_title_sort", "_original_order"],
        ascending=[False, False, True, True],
        na_position="last",
    )
    rows["_article_key"] = rows.apply(
        lambda row: normalized_headline(row["_article_title"]) or str(get_url(row.to_dict())).strip().lower(),
        axis=1,
    )
    rows = rows.drop_duplicates("_article_key", keep="first")
    return rows.sort_values(
        ["_published_dt", "_collected_dt", "_title_sort", "_original_order"],
        ascending=[False, False, True, True],
        na_position="last",
    )


def article_feed_date(row):
    return get_first(row, ["published", "collected_at"], "날짜 미확인")


def legacy_render_article_feed_card_item_01(row):
    item = row.to_dict() if hasattr(row, "to_dict") else row
    category_label = {
        "market": "시장 기사",
        "development": "개발 기사",
        "gp_capital": "GP / 자본 기사",
        "review": "Review",
        "access_limited": "Access-limited",
    }.get(item.get("_article_category"), "시장 기사")
    title = item.get("_article_title") or get_title(item)
    source = get_first(item, ["source", "source_report"], "Source 미확인")
    market = get_first(item, ["market_focus", "market", "primary_market"], "시장 미확인")
    published = article_feed_date(item)
    with st.expander(f"{title} | {source} · {market} · {published}", expanded=False):
        st.write(f"**Source:** {source}")
        st.write(f"**Published:** {published}")
        st.write(f"**Category:** {category_label}")
        confidence = get_first(item, ["_article_confidence"], "")
        reason = get_first(item, ["_article_category_reason"], "")
        if confidence:
            st.write(f"**Classification confidence:** {confidence}")
        if reason:
            st.caption(f"Classification reason: {reason}")
        snippet = get_first(item, ["article_text_sample", "summary", "why_it_matters", "strategic_implication"], "")
        if snippet:
            st.write(f"**Summary / snippet:** {truncate_text(snippet, 420)}")
        st.write(f"**Related market:** {market}")
        gp = get_first(item, ["gp_or_developer", "canonical_gp_name", "firm_name"], "")
        if gp:
            st.write(f"**Related GP / developer:** {gp}")
        why = get_first(item, ["strategic_implication", "why_it_matters", "reason_for_inclusion"], "")
        if why:
            st.write(f"**Why it may matter:** {why}")
        url = get_url(item)
        if isinstance(url, str) and url.startswith("http"):
            st.markdown(f"[원문 기사 보기]({url})")


def render_article_feed_section(title, rows, limit=12):
    st.markdown(f"### {title}")
    if rows.empty:
        st.caption("표시할 기사가 아직 없습니다.")
        return
    for _, row in rows.head(limit).iterrows():
        render_article_feed_item(row)


def render_article_feed_collapsed_section(title, rows, limit=20):
    if rows.empty:
        return
    with st.expander(title, expanded=False):
        for _, row in rows.head(limit).iterrows():
            render_article_feed_item(row)


def legacy_page_article_feed_01(shared, filters):
    st.title("기사 모음 / Article Feed")
    st.caption("수집된 주요 기사들을 카테고리별로 확인하는 페이지입니다.")
    rows = article_feed_rows(shared)
    if rows.empty:
        missing_file_message(FILES["articles"])
        return
    counts = rows["_article_category"].value_counts()
    review_count = int(counts.get("review", 0))
    access_limited_count = int(counts.get("access_limited", 0))
    total_count = max(len(rows), 1)
    review_ratio = review_count / total_count
    access_limited_ratio = access_limited_count / total_count
    if review_ratio > 0.25:
        st.warning("Review 기사 비율이 25%를 넘었습니다. Article Feed 분류 기준 점검이 필요합니다.")
    cols = st.columns(3)
    metrics = [
        ("시장 기사 수", int(counts.get("market", 0))),
        ("개발 기사 수", int(counts.get("development", 0))),
        ("GP / 자본 기사 수", int(counts.get("gp_capital", 0))),
    ]
    for col, (label, value) in zip(cols, metrics):
        with col:
            render_compact_metric(label, value)
    st.caption(
        "시장 기사: financing / macro / capital markets 중심 | "
        "개발 기사: entitlement / construction / delivery / site 중심 | "
        "GP / 자본 기사: sponsor / lender / JV / capital partner 중심"
    )
    st.caption(f"Review ratio: {review_ratio:.1%} | Access-limited ratio: {access_limited_ratio:.1%}")
    normal_confidence = rows["_article_confidence"].isin(["high", "medium"])
    render_article_feed_section("시장 기사", rows[(rows["_article_category"] == "market") & normal_confidence])
    render_article_feed_section("개발 기사", rows[(rows["_article_category"] == "development") & normal_confidence])
    render_article_feed_section("GP / 자본 기사", rows[(rows["_article_category"] == "gp_capital") & normal_confidence])
    render_article_feed_collapsed_section("Review / classification tuning samples", rows[rows["_article_category"] == "review"])
    render_article_feed_collapsed_section("Access-limited sources", rows[rows["_article_category"] == "access_limited"])


def article_feed_date(row):
    value = get_first(row, ["published", "collected_at"], "")
    if not value:
        return "날짜 미확인"
    parsed = pd.to_datetime(value, errors="coerce", utc=True)
    if not pd.isna(parsed):
        return parsed.strftime("%Y-%m-%d")
    return truncate_text(str(value), 24)


def article_feed_split_tags(value):
    tags = []
    for tag in str(value or "").split(";"):
        clean_tag = tag.strip()
        if clean_tag and clean_tag not in tags:
            tags.append(clean_tag)
    return tags


def article_feed_unique_values(rows, column):
    if rows.empty or column not in rows.columns:
        return []
    values = []
    for value in rows[column].dropna().astype(str):
        clean_value = value.strip()
        if clean_value and clean_value not in values:
            values.append(clean_value)
    return sorted(values)


def article_feed_unique_tags(rows):
    tags = []
    if rows.empty or "event_tags" not in rows.columns:
        return tags
    for value in rows["event_tags"].dropna().astype(str):
        for tag in article_feed_split_tags(value):
            if tag not in tags:
                tags.append(tag)
    return sorted(tags)


ARTICLE_FEED_DISPLAY_CATEGORIES = [
    "시장 데이터",
    "개발/인허가",
    "거래/투자",
    "운영/임대",
    "기타",
]
ARTICLE_FEED_EXCLUDED_FINANCE_CATEGORY = "제외/금융"


ARTICLE_FEED_CORE_15_MARKETS = [
    "Los Angeles / Southern California",
    "New York / Northern New Jersey",
    "Dallas-Fort Worth",
    "Houston",
    "Atlanta",
    "Phoenix",
    "Miami / South Florida",
    "Washington DC / Northern Virginia",
    "Seattle",
    "Denver",
    "Austin",
    "Charlotte",
    "Raleigh-Durham",
    "Nashville",
    "Tampa / St. Petersburg",
]

ARTICLE_FEED_WATCHLIST_8_MARKETS = [
    "Orlando",
    "San Antonio",
    "Las Vegas",
    "Salt Lake City",
    "Jacksonville",
    "Columbus",
    "Minneapolis",
    "San Diego",
]

ARTICLE_FEED_OTHER_MARKETS = ["San Francisco / Bay Area", "National / Macro", "Non-Core Local", "Unknown"]
ARTICLE_FEED_BROAD_MARKET_VALUES = {
    "",
    "California",
    "Sun Belt",
    "Southeast",
    "Texas",
    "Florida",
    "Arizona",
    "National",
    "Other / Unknown",
}

ARTICLE_FEED_MACRO_MARKET_TERMS = [
    "absorption",
    "vacancy",
    "rent growth",
    "housing starts",
    "construction data",
    "construction spending",
    "developer confidence",
    "market data",
    "national",
    "u.s.",
    "nationwide",
    "overall",
    "survey",
    "index",
]

ARTICLE_FEED_NON_CORE_LOCAL_TERMS = [
    "nokomis",
    "sarasota",
    "baltimore",
    "baltimore county",
    "connecticut",
    "southern connecticut",
    "hilton head",
    "south carolina",
    "kenosha",
    "wisconsin",
    "ohio",
    "cleveland",
    "cincinnati",
]

ARTICLE_FEED_BAY_AREA_TERMS = [
    "san francisco",
    "bay area",
    "palo alto",
    "alameda county",
    "newark california",
    "newark, california",
    "oakland",
    "san jose",
    "berkeley",
    "fremont",
]


def article_feed_market_text(row):
    return " ".join(
        str(row.get(field, "") or "").lower()
        for field in [
            "title",
            "canonical_market",
            "market_focus",
            "source",
            "topics",
            "event_tags",
            "category_tags",
            "article_text_sample",
            "url",
        ]
    )


def article_feed_text_has_any(text, terms):
    padded = f" {text.lower()} "
    return any(term in padded for term in terms)


def article_feed_display_category(row):
    category = article_feed_clean_value(row.get("display_category", ""))
    if category == ARTICLE_FEED_EXCLUDED_FINANCE_CATEGORY:
        return category
    if category in ARTICLE_FEED_DISPLAY_CATEGORIES:
        return category
    tags = article_feed_category_tags(row)
    if tags:
        return tags[0]
    return "기타"


def article_feed_category_tags(row):
    raw_tags = article_feed_clean_value(row.get("category_tags", ""))
    if raw_tags:
        tags = []
        for tag in article_feed_split_tags(raw_tags):
            clean_tag = article_feed_clean_value(tag)
            if clean_tag == ARTICLE_FEED_EXCLUDED_FINANCE_CATEGORY:
                return [ARTICLE_FEED_EXCLUDED_FINANCE_CATEGORY]
            if clean_tag in ARTICLE_FEED_DISPLAY_CATEGORIES and clean_tag not in tags:
                tags.append(clean_tag)
        if tags:
            return [category for category in ARTICLE_FEED_DISPLAY_CATEGORIES if category in tags]

    text = article_feed_market_text(row)
    title = str(row.get("title", "") or row.get("_article_title", "") or "").lower()
    development_terms = [
        "develop", "development", "developer", "project", "proposed", "proposal",
        "planning", "plan", "site plan", "permit", "entitlement", "entitled",
        "approval", "approved", "zoning", "rezoning", "construction",
        "construction start", "starts work", "breaks ground", "groundbreak",
        "under construction", "delivery", "completion", "completed", "opens",
        "unveiled", "redevelopment", "mixed-use", "mixed use", "apartment tower",
        "housing community", "affordable housing development", "student housing project",
        "senior housing project", "btr development", "build-to-rent development",
        "build to rent development", "to build", "to develop",
    ]
    transaction_terms = [
        "acquisition", "acquire", "acquires", "acquired", "buyer", "buys",
        "purchase", "sale", "sells", "sold", "disposition", "portfolio sale",
        "portfolio acquisition", "transaction", "jv", "joint venture",
        "recapitalization", "recap", "stake", "investment", "invests",
        "investor", "merger", "platform acquisition",
    ]
    finance_terms = [
        "capital stack", "capital raise", "structured finance",
    ]
    operations_terms = [
        "rent", "rents", "rent growth", "rent prices", "lease", "leasing",
        "preleasing", "pre-leasing", "occupancy", "vacancy", "absorption",
        "concession", "concessions", "tenant", "tenants", "stabilized",
        "operations", "property management", "noi", "covenant",
        "operating performance", "btr", "build-to-rent", "build to rent",
    ]
    market_data_terms = [
        "market data", "supply", "demand", "absorption rate", "vacancy rate",
        "absorption", "rent growth", "rent prices", "housing starts",
        "construction data", "construction spending",
        "permits data", "starts data", "index", "survey", "forecast", "outlook",
        "report", "quarter", "first quarter", "quarterly report", "monthly report",
        "confidence index", "national", "nationwide", "u.s.", "macro",
    ]
    hits = {
        "개발/인허가": article_feed_text_has_any(title, development_terms) or article_feed_text_has_any(text, development_terms),
        "거래/투자": article_feed_text_has_any(title, transaction_terms) or article_feed_text_has_any(text, transaction_terms),
        "운영/임대": article_feed_text_has_any(title, operations_terms) or article_feed_text_has_any(text, operations_terms),
        "시장 데이터": article_feed_text_has_any(title, market_data_terms) or article_feed_text_has_any(text, market_data_terms),
    }
    tags = [category for category in ARTICLE_FEED_DISPLAY_CATEGORIES if hits.get(category)]
    return tags or ["기타"]


def article_feed_is_excluded_finance(row):
    item = row.to_dict() if hasattr(row, "to_dict") else row
    if article_feed_clean_value(item.get("exclude_from_feed", "")).lower() == "yes":
        return True
    if article_feed_clean_value(item.get("display_category", "")) == ARTICLE_FEED_EXCLUDED_FINANCE_CATEGORY:
        return True
    if ARTICLE_FEED_EXCLUDED_FINANCE_CATEGORY in article_feed_category_tags(item):
        return True

    title = str(item.get("title", "") or item.get("_article_title", "") or "").lower()
    summary = " ".join(
        str(item.get(field, "") or "").lower()
        for field in ["summary", "article_text_sample", "reason_for_inclusion"]
    )
    finance_core_terms = [
        "construction loan", "bridge loan", "refinancing", "refinance",
        "agency loan", "fha loan", "mortgage", "acquisition loan",
        "debt financing", "loan arranged", "arranges loan", "arranged loan",
        "loan provided", "provides loan", "provided loan", "financing provided",
        "provides financing", "debt package", "credit facility", "lender",
        "loan for", "lands loan", "secures loan", "closes loan",
    ]
    non_finance_title_terms = [
        "sale", "sells", "sold", "acquisition", "acquires", "buys", "purchase",
        "portfolio sale", "joint venture", "jv", "stake", "platform investment",
        "breaks ground", "groundbreaking", "starts work", "construction start",
        "opens", "delivers", "development plan", "proposed", "approved",
        "entitlement", "permit", "zoning", "planning", "site acquisition",
        "land acquisition", "development site", "project launch",
    ]
    if article_feed_text_has_any(title, finance_core_terms):
        return True
    return article_feed_text_has_any(summary, finance_core_terms) and not article_feed_text_has_any(title, non_finance_title_terms)


def article_feed_has_specific_market_hint(row):
    text = article_feed_market_text(row)
    market_alias_terms = [
        *(market.lower() for market in ARTICLE_FEED_CORE_15_MARKETS),
        *(market.lower() for market in ARTICLE_FEED_WATCHLIST_8_MARKETS),
        "los angeles",
        "southern california",
        "new york",
        "northern new jersey",
        "dallas",
        "fort worth",
        "houston",
        "atlanta",
        "phoenix",
        "miami",
        "south florida",
        "washington dc",
        "northern virginia",
        "seattle",
        "denver",
        "austin",
        "charlotte",
        "raleigh",
        "durham",
        "nashville",
        "tampa",
        "st. petersburg",
        "orlando",
        "san antonio",
        "las vegas",
        "salt lake city",
        "jacksonville",
        "columbus",
        "minneapolis",
        "san diego",
        *ARTICLE_FEED_NON_CORE_LOCAL_TERMS,
        *ARTICLE_FEED_BAY_AREA_TERMS,
    ]
    return article_feed_text_has_any(text, market_alias_terms)


def article_feed_display_market(row):
    market = str(row.get("canonical_market", "") or "").strip()
    text = article_feed_market_text(row)
    if market in ARTICLE_FEED_CORE_15_MARKETS or market in ARTICLE_FEED_WATCHLIST_8_MARKETS:
        return market
    if (
        market == "San Francisco / Bay Area"
        or "san francisco" in market.lower()
        or "bay area" in market.lower()
        or article_feed_text_has_any(text, ARTICLE_FEED_BAY_AREA_TERMS)
    ):
        return "San Francisco / Bay Area"
    if (
        market == "National"
        or str(row.get("market_focus", "") or "").strip() == "National"
        or (article_feed_text_has_any(text, ARTICLE_FEED_MACRO_MARKET_TERMS) and not article_feed_has_specific_market_hint(row))
    ):
        return "National / Macro"
    if market and market not in ARTICLE_FEED_BROAD_MARKET_VALUES:
        return "Non-Core Local"
    if article_feed_text_has_any(text, ARTICLE_FEED_NON_CORE_LOCAL_TERMS):
        return "Non-Core Local"
    if market in {"California", "Texas", "Florida", "Arizona"}:
        return "Non-Core Local"
    return "Unknown"


def article_feed_market_options(rows, market_group):
    if market_group == "Core 15":
        return ["All", *ARTICLE_FEED_CORE_15_MARKETS]
    if market_group == "Watchlist 8":
        return ["All", *ARTICLE_FEED_WATCHLIST_8_MARKETS]
    if market_group == "Other":
        options = []
        if not rows.empty:
            for _, row in rows.iterrows():
                market = article_feed_display_market(row.to_dict())
                if market not in ARTICLE_FEED_CORE_15_MARKETS and market not in ARTICLE_FEED_WATCHLIST_8_MARKETS and market not in options:
                    options.append(market)
        ordered = [market for market in ARTICLE_FEED_OTHER_MARKETS if market in options or market == "Other / Unknown"]
        ordered.extend(sorted(market for market in options if market not in ordered))
        return ["All", *ordered]
    return [
        "All",
        *ARTICLE_FEED_CORE_15_MARKETS,
        *ARTICLE_FEED_WATCHLIST_8_MARKETS,
        *ARTICLE_FEED_OTHER_MARKETS,
    ]


def article_feed_market_group(row):
    market = article_feed_display_market(row)
    tier = str(row.get("market_tier", "") or "").strip().lower()
    if tier == "core_15" or market in ARTICLE_FEED_CORE_15_MARKETS or str(row.get("is_core_market", "")).strip().lower() == "yes":
        return "Core 15"
    if tier == "watchlist_8" or market in ARTICLE_FEED_WATCHLIST_8_MARKETS or str(row.get("is_watchlist_market", "")).strip().lower() == "yes":
        return "Watchlist 8"
    return "Other"


def article_feed_is_access_limited(row):
    return str(row.get("access_status", "") or "").strip().lower() == "access_limited"


def filter_article_feed_rows(rows, market_group, market, sector, display_category, include_access_limited, event_tag="All"):
    if rows.empty:
        return rows
    filtered = rows.copy()
    if not include_access_limited:
        filtered = filtered[~filtered.apply(lambda row: article_feed_is_access_limited(row.to_dict()), axis=1)]
    if market_group != "All":
        filtered = filtered[filtered.apply(lambda row: article_feed_market_group(row.to_dict()) == market_group, axis=1)]
    if market != "All":
        filtered = filtered[filtered.apply(lambda row: article_feed_display_market(row.to_dict()) == market, axis=1)]
    if sector != "All" and "normalized_sector" in filtered.columns:
        filtered = filtered[filtered["normalized_sector"].fillna("").astype(str) == sector]
    if display_category != "All":
        filtered = filtered[filtered.apply(lambda row: display_category in article_feed_category_tags(row.to_dict()), axis=1)]
    if event_tag != "All":
        filtered = filtered[filtered.apply(
            lambda row: event_tag in article_feed_split_tags(str(row.to_dict().get("event_tags", ""))), axis=1
        )]
    return filtered


def render_article_feed_item(row):
    item = row.to_dict() if hasattr(row, "to_dict") else row
    title = item.get("_article_title") or get_title(item)
    source = get_first(item, ["source", "source_report"], "Source 미확인")
    market = get_first(item, ["canonical_market", "market_focus", "market", "primary_market"], "시장 미확인")
    sector = get_first(item, ["normalized_sector", "residential_sector", "residential_sector_focus"], "섹터 미확인")
    published = article_feed_date(item)
    tags = article_feed_split_tags(item.get("event_tags", ""))[:2]
    url = get_url(item)
    with st.container():
        st.markdown(f"**{title}**")
        st.caption(f"{source} · {published}")
        st.write(f"{market} · {sector}")
        if tags:
            st.caption(" · ".join(tags))
        if article_feed_is_access_limited(item):
            st.caption("접근 제한 가능")
        if isinstance(url, str) and url.startswith("http"):
            st.markdown(f"[원문 보기]({url})")


def legacy_page_article_feed_02(shared, filters):
    st.title("기사 모음 / Article Feed")
    st.caption("수집된 주요 주거시장 뉴스를 시장, 섹터, 이벤트 태그별로 확인합니다.")
    rows = article_feed_rows(shared)
    if rows.empty:
        missing_file_message(FILES["articles"])
        return

    total_articles = len(rows)
    core_count = int(rows.apply(lambda row: article_feed_market_group(row.to_dict()) == "Core 15", axis=1).sum())
    watchlist_count = int(rows.apply(lambda row: article_feed_market_group(row.to_dict()) == "Watchlist 8", axis=1).sum())
    access_limited_count = int(rows.apply(lambda row: article_feed_is_access_limited(row.to_dict()), axis=1).sum())
    cols = st.columns(4)
    metrics = [
        ("전체 기사 수", total_articles),
        ("Core 15 기사 수", core_count),
        ("Watchlist 8 기사 수", watchlist_count),
        ("Access-limited 기사 수", access_limited_count),
    ]
    for col, (label, value) in zip(cols, metrics):
        with col:
            render_compact_metric(label, value)
    other_counts = rows.apply(lambda row: article_feed_display_market(row.to_dict()), axis=1).value_counts()
    st.caption(
        "National / Macro: "
        f"{int(other_counts.get('National / Macro', 0))} · "
        "Non-Core Local: "
        f"{int(other_counts.get('Non-Core Local', 0))} · "
        "Unknown: "
        f"{int(other_counts.get('Unknown', 0))}"
    )

    filter_cols = st.columns([1, 1.3, 1.2, 1.4, 1])
    with filter_cols[0]:
        market_group = st.selectbox("시장 그룹", ["All", "Core 15", "Watchlist 8", "Other"], key="article_feed_market_group")
    with filter_cols[1]:
        market = st.selectbox("시장", ["All", *article_feed_unique_values(rows, "canonical_market")], key="article_feed_market")
    with filter_cols[2]:
        sector = st.selectbox("섹터", ["All", *article_feed_unique_values(rows, "normalized_sector")], key="article_feed_sector")
    with filter_cols[3]:
        event_tag = st.selectbox("이벤트 태그", ["All", *article_feed_unique_tags(rows)], key="article_feed_event_tag")
    with filter_cols[4]:
        include_access_limited = st.checkbox("접근 제한 기사 포함", value=False, key="article_feed_include_access_limited")

    filtered_rows = filter_article_feed_rows(
        rows,
        market_group,
        market,
        sector,
        event_tag,
        include_access_limited,
    )
    st.caption(f"표시 기사 수: {len(filtered_rows)}")
    if filtered_rows.empty:
        st.caption("조건에 맞는 기사가 없습니다.")
        return
    for _, row in filtered_rows.iterrows():
        render_article_feed_item(row)


def article_feed_card_css():
    return """
    <style>
    .article-feed-card {
        border: 1px solid rgba(49, 51, 63, 0.14);
        background: rgba(248, 250, 252, 0.78);
        border-radius: 8px;
        box-sizing: border-box;
        width: 100%;
        padding: 10px 12px;
        margin-bottom: 10px;
    }
    .article-feed-title {
        font-weight: 650;
        font-size: 0.92rem;
        line-height: 1.3;
        color: rgb(31, 41, 55);
        margin-bottom: 5px;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    .article-feed-meta {
        color: rgb(90, 99, 112);
        font-size: 0.79rem;
        line-height: 1.3;
        margin: 0 0 2px 0;
    }
    .article-feed-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 4px;
        margin: 5px 0 6px 0;
        line-height: 1.25;
    }
    .article-feed-tag {
        border: 1px solid rgba(49, 51, 63, 0.12);
        background: rgba(255, 255, 255, 0.75);
        border-radius: 999px;
        padding: 1px 6px;
        color: rgb(75, 85, 99);
        font-size: 0.74rem;
        line-height: 1.25;
    }
    .article-feed-access {
        display: inline-block;
        border: 1px solid rgba(180, 83, 9, 0.22);
        background: rgba(255, 247, 237, 0.92);
        color: rgb(146, 64, 14);
        border-radius: 999px;
        padding: 1px 6px;
        font-size: 0.72rem;
        line-height: 1.25;
        margin-top: 5px;
        white-space: nowrap;
    }
    .article-feed-freshness {
        display: inline-block;
        border: 1px solid rgba(100, 116, 139, 0.22);
        background: rgba(241, 245, 249, 0.9);
        color: rgb(71, 85, 105);
        border-radius: 999px;
        padding: 1px 6px;
        font-size: 0.72rem;
        line-height: 1.25;
        margin: 5px 5px 0 0;
        white-space: nowrap;
    }
    .article-feed-link {
        font-size: 0.8rem;
        line-height: 1.25;
        margin-top: 2px;
    }
    </style>
    """


def article_feed_clean_value(value, fallback=""):
    if value is None:
        return fallback
    try:
        if pd.isna(value):
            return fallback
    except (TypeError, ValueError):
        pass
    clean_value = str(value).strip()
    if clean_value.lower() in {"", "nan", "none", "null"}:
        return fallback
    return clean_value


def article_feed_clean_tags(value, limit=3):
    tags = []
    for tag in article_feed_split_tags(value):
        clean_tag = article_feed_clean_value(tag)
        if clean_tag and clean_tag not in tags:
            tags.append(clean_tag)
        if len(tags) >= limit:
            break
    return tags


def article_feed_card_meta_line(*values):
    clean_values = [article_feed_clean_value(value) for value in values]
    clean_values = [value for value in clean_values if value]
    if not clean_values:
        return ""
    return f"<div class=\"article-feed-meta\">{html.escape(' · '.join(clean_values))}</div>"


def article_feed_valid_url(value):
    url = article_feed_clean_value(value)
    return url if url.startswith(("http://", "https://")) else ""


def article_feed_freshness_status(row):
    item = row.to_dict() if hasattr(row, "to_dict") else row
    status = article_feed_clean_value(item.get("freshness_status", "")).lower()
    legacy_status_map = {
        "current": "fresh",
        "usable_recent": "fresh",
        "stale_penalized": "recent",
        "historical_only": "old",
        "unknown_date_review": "unknown_date",
    }
    status = legacy_status_map.get(status, status)
    if status in {"fresh", "recent", "old", "archive", "unknown_date"}:
        return status

    parsed = pd.to_datetime(item.get("published"), errors="coerce", utc=True)
    if pd.isna(parsed):
        return "unknown_date"
    today = pd.Timestamp.now(tz="UTC").normalize()
    age_days = max(0, int((today - parsed.normalize()).days))
    if age_days <= 7:
        return "fresh"
    if age_days <= 14:
        return "recent"
    if age_days <= 60:
        return "old"
    return "archive"


def filter_article_feed_by_freshness(rows, freshness_filter):
    if rows.empty:
        return rows
    allowed = {
        "Fresh only": {"fresh"},
        "Recent 14 days": {"fresh", "recent"},
        "Include old": {"fresh", "recent", "old"},
        "Include archive": {"fresh", "recent", "old", "archive", "unknown_date"},
    }.get(freshness_filter, {"fresh"})
    return rows[rows.apply(lambda row: article_feed_freshness_status(row.to_dict()) in allowed, axis=1)]


def article_feed_category_tag_counts(rows):
    counts = {category: 0 for category in ARTICLE_FEED_DISPLAY_CATEGORIES}
    if rows.empty:
        return counts
    for _, row in rows.iterrows():
        for category in article_feed_category_tags(row.to_dict()):
            counts[category] = counts.get(category, 0) + 1
    return counts


def render_article_feed_card_item(row):
    item = row.to_dict() if hasattr(row, "to_dict") else row
    title = article_feed_clean_value(item.get("_article_title") or get_title(item), "Untitled article")
    source = article_feed_clean_value(get_first(item, ["source", "source_report"], ""))
    market = article_feed_clean_value(article_feed_display_market(item))
    sector = article_feed_clean_value(get_first(item, ["normalized_sector", "residential_sector", "residential_sector_focus"], ""))
    display_category = article_feed_clean_value(article_feed_display_category(item))
    published = article_feed_clean_value(article_feed_date(item))
    url = article_feed_valid_url(get_url(item))
    category_html = (
        f"<div class='article-feed-tags'><span class='article-feed-tag'>{html.escape(display_category)}</span></div>"
        if display_category
        else ""
    )
    access_status = article_feed_clean_value(item.get("access_status", ""))
    access_badge = "<span class='article-feed-access'>접근 제한 가능</span>" if access_status == "access_limited" else ""
    freshness_status = article_feed_freshness_status(item)
    freshness_badge = (
        f"<span class='article-feed-freshness'>{html.escape(freshness_status)}</span>"
        if freshness_status in {"old", "archive"}
        else ""
    )
    if url:
        link_html = f"<a href=\"{html.escape(url, quote=True)}\" target=\"_blank\" rel=\"noopener noreferrer\">원문 보기</a>"
    else:
        link_html = "<span>원문 링크 없음</span>"
    source_date_html = article_feed_card_meta_line(source, published)
    market_sector_html = article_feed_card_meta_line(market, sector)
    card_html = (
        "<div class=\"article-feed-card\">"
        f"<div class=\"article-feed-title\">{html.escape(str(title or '제목 미확인'))}</div>"
        f"{source_date_html}"
        f"{market_sector_html}"
        f"{category_html}"
        f"<div class=\"article-feed-link\">{link_html}</div>"
        f"{freshness_badge}"
        f"{access_badge}"
        "</div>"
    )
    st.markdown(card_html, unsafe_allow_html=True)


def render_article_feed_item(row):
    item = row.to_dict() if hasattr(row, "to_dict") else row
    title = item.get("_article_title") or get_title(item)
    source = get_first(item, ["source", "source_report"], "Source 미확인")
    market = article_feed_display_market(item)
    sector = get_first(item, ["normalized_sector", "residential_sector", "residential_sector_focus"], "섹터 미확인")
    published = article_feed_date(item)
    tags = article_feed_split_tags(item.get("event_tags", ""))[:2]
    url = get_url(item)
    with st.container():
        st.markdown(f"**{title}**")
        st.caption(f"{source} · {published}")
        st.write(f"{market} · {sector}")
        if tags:
            st.caption(" · ".join(tags))
        if article_feed_is_access_limited(item):
            st.caption("접근 제한 가능")
        if isinstance(url, str) and url.startswith("http"):
            st.markdown(f"[원문 보기]({url})")


def render_article_feed_cards(rows):
    if rows.empty:
        return
    st.markdown(article_feed_card_css(), unsafe_allow_html=True)
    row_items = list(rows.iterrows())
    for start in range(0, len(row_items), 2):
        cols = st.columns(2)
        for offset, (_, row) in enumerate(row_items[start:start + 2]):
            with cols[offset]:
                render_article_feed_card_item(row)


def article_feed_rerun():
    rerun = getattr(st, "rerun", None) or getattr(st, "experimental_rerun", None)
    if rerun:
        rerun()


def apply_pending_article_feed_category():
    pending_category = st.session_state.pop("article_feed_pending_category", None)
    if pending_category in ARTICLE_FEED_DISPLAY_CATEGORIES:
        st.session_state["article_feed_display_category"] = pending_category
        st.session_state["article_feed_current_page"] = 1


def page_article_feed(shared, filters):
    st.markdown("<div id='article-feed-top'></div>", unsafe_allow_html=True)
    st.title("기사 모음 / Article Feed")
    rows = article_feed_rows(shared)
    if rows.empty:
        missing_file_message(FILES["articles"])
        return

    total_articles = len(rows)
    excluded_finance_count = int(rows.apply(lambda row: article_feed_is_excluded_finance(row.to_dict()), axis=1).sum())
    rows = rows[~rows.apply(lambda row: article_feed_is_excluded_finance(row.to_dict()), axis=1)].copy()
    core_count = int(rows.apply(lambda row: article_feed_market_group(row.to_dict()) == "Core 15", axis=1).sum())
    watchlist_count = int(rows.apply(lambda row: article_feed_market_group(row.to_dict()) == "Watchlist 8", axis=1).sum())
    access_limited_count = int(rows.apply(lambda row: article_feed_is_access_limited(row.to_dict()), axis=1).sum())

    freshness_counts = rows.apply(lambda row: article_feed_freshness_status(row.to_dict()), axis=1).value_counts()
    fresh_count = int(freshness_counts.get("fresh", 0))
    recent_14d_count = int(fresh_count + freshness_counts.get("recent", 0))
    old_count = int(freshness_counts.get("old", 0))
    archive_count = int(freshness_counts.get("archive", 0))
    unknown_date_count = int(freshness_counts.get("unknown_date", 0))

    apply_pending_article_feed_category()

    filter_cols = st.columns([0.9, 1.15, 0.95, 1.55, 1, 1, 1.2])
    with filter_cols[0]:
        market_group = st.selectbox("지역", ["All", "Core 15", "Watchlist 8", "Other"], key="article_feed_market_group")
    with filter_cols[1]:
        market = st.selectbox("Market", article_feed_market_options(rows, market_group), key="article_feed_market")
    with filter_cols[2]:
        sector = st.selectbox("섹터", ["All", *article_feed_unique_values(rows, "normalized_sector")], key="article_feed_sector")
    with filter_cols[3]:
        display_category = st.selectbox("분류", ["All", *ARTICLE_FEED_DISPLAY_CATEGORIES], key="article_feed_display_category")
    with filter_cols[4]:
        freshness_filter = st.selectbox(
            "Freshness",
            ["Fresh only", "Recent 14 days", "Include old", "Include archive"],
            index=0,
            key="article_feed_freshness_filter",
        )
    with filter_cols[5]:
        display_limit_label = st.selectbox(
            "페이지당 표시",
            ["20개", "40개", "전체 보기"],
            index=0,
            key="article_feed_display_limit",
        )
    with filter_cols[6]:
        event_tag = st.selectbox(
            "Event Tag",
            ["All", *article_feed_unique_tags(rows)],
            key="article_feed_event_tag",
        )

    filtered_rows = filter_article_feed_rows(
        rows,
        market_group,
        market,
        sector,
        display_category,
        False,
        event_tag,
    )
    filtered_rows = filter_article_feed_by_freshness(filtered_rows, freshness_filter)
    matching_count = len(filtered_rows)
    if display_limit_label == "전체 보기":
        display_rows = filtered_rows
        page_start = 1 if matching_count else 0
        page_end = matching_count
        page_range_label = f"{page_start}~{page_end}" if matching_count else "0"
        total_pages = 1
        current_page = 1
    else:
        page_size = int(display_limit_label.replace("개", ""))
        total_pages = max(1, (matching_count + page_size - 1) // page_size)
        page_options = [f"{page}페이지" for page in range(1, total_pages + 1)]
        current_page = int(st.session_state.get("article_feed_current_page", 1) or 1)
        current_page = max(1, min(current_page, total_pages))
        st.session_state["article_feed_current_page"] = current_page
        page_start = ((current_page - 1) * page_size) + 1 if matching_count else 0
        page_end = min(current_page * page_size, matching_count)
        display_rows = filtered_rows.iloc[page_start - 1:page_end] if matching_count else filtered_rows.head(0)
        page_range_label = f"{page_start}~{page_end}" if matching_count else "0"

    result_text = f"조건 일치 기사 {matching_count}개"
    if matching_count:
        result_text += f" · 현재 {page_range_label} 표시"
    st.caption(result_text)

    with st.expander("수집 현황 보기", expanded=False):
        cols = st.columns(3)
        metrics = [
            ("전체 수집", total_articles),
            ("Fresh", fresh_count),
            ("Recent 14d", recent_14d_count),
            ("Old", old_count),
            ("Archive", archive_count),
            ("Unknown date", unknown_date_count),
            ("Core 15", core_count),
            ("Watchlist 8", watchlist_count),
            ("Access-limited", access_limited_count),
            ("제외 금융/대출", excluded_finance_count),
        ]
        for index, (label, value) in enumerate(metrics):
            with cols[index % len(cols)]:
                render_compact_metric(label, value)
        category_counts = article_feed_category_tag_counts(rows)
        st.caption("분류별 태그 수는 복수 태그 기준이므로 전체 기사 수와 합계가 다를 수 있습니다.")
        st.markdown("**분류별 태그 수**")
        for category in ARTICLE_FEED_DISPLAY_CATEGORIES:
            st.markdown(f"- {category}: {int(category_counts.get(category, 0))}")

    if filtered_rows.empty:
        st.caption("조건에 맞는 기사가 없습니다.")
        st.markdown("[맨 위로 이동](#article-feed-top)")
        return
    render_article_feed_cards(display_rows)
    if display_limit_label != "전체 보기" and total_pages > 1:
        page_options = [f"{page}페이지" for page in range(1, total_pages + 1)]
        nav_cols = st.columns([1.3, 4])
        with nav_cols[0]:
            selected_page = st.selectbox(
                "페이지",
                page_options,
                index=current_page - 1,
                key="article_feed_page",
            )
            selected_page_number = page_options.index(selected_page) + 1
            if selected_page_number != current_page:
                st.session_state["article_feed_current_page"] = selected_page_number
                article_feed_rerun()
        st.caption(f"현재 {page_range_label} / {matching_count}개")
    elif matching_count:
        st.caption(f"현재 {page_range_label} / {matching_count}개")

    access_limited_rows = rows[
        rows.apply(lambda row: article_feed_is_access_limited(row.to_dict()), axis=1)
    ]
    if not access_limited_rows.empty:
        st.divider()
        with st.expander(f"접근 제한 기사 보관 ({len(access_limited_rows)}건)", expanded=False):
            st.caption("페이월 등 접근 제한으로 본문 확인이 어려운 기사입니다. 제목과 원문 링크만 보존합니다.")
            render_article_feed_cards(access_limited_rows)

    st.markdown("[맨 위로 이동](#article-feed-top)")


def market_dashboard_rows(shared):
    rows = article_feed_rows(shared)
    if rows.empty:
        return rows
    return rows[~rows.apply(lambda row: article_feed_is_excluded_finance(row.to_dict()), axis=1)].copy()


def article_market_order():
    return [
        *ARTICLE_FEED_CORE_15_MARKETS,
        *ARTICLE_FEED_WATCHLIST_8_MARKETS,
        "San Francisco / Bay Area",
        "National / Macro",
        "Non-Core Local",
        "Unknown",
    ]


def market_dashboard_market_counts(rows):
    if rows.empty:
        return pd.Series(dtype=int)
    values = rows.apply(lambda row: article_feed_display_market(row.to_dict()), axis=1)
    counts = values.value_counts()
    ordered = [market for market in article_market_order() if counts.get(market, 0) > 0]
    return counts.reindex(ordered).fillna(0).astype(int)


def market_dashboard_sector_counts(rows, limit=10):
    if rows.empty or "normalized_sector" not in rows.columns:
        return pd.Series(dtype=int)
    values = rows["normalized_sector"].fillna("").astype(str).str.strip()
    values = values.replace({"": "Other", "nan": "Other", "None": "Other"})
    return values.value_counts().head(limit)


def market_dashboard_event_tag_counts(rows, limit=10):
    if rows.empty or "event_tags" not in rows.columns:
        return pd.Series(dtype=int)
    tags = []
    for value in rows["event_tags"].dropna().astype(str):
        tags.extend(article_feed_split_tags(value))
    if not tags:
        return pd.Series(dtype=int)
    return pd.Series(tags).value_counts().head(limit)


def market_dashboard_recent_rows(rows, limit=5):
    if rows.empty:
        return rows
    recent = rows.copy()
    if "_published_sort" not in recent.columns:
        recent["_published_sort"] = pd.to_datetime(recent.get("published"), errors="coerce", utc=True)
    if "_run_sort" not in recent.columns:
        recent["_run_sort"] = pd.to_datetime(recent.get("collected_at"), errors="coerce", utc=True)
    return recent.sort_values(["_published_sort", "_run_sort"], ascending=[False, False], na_position="last").head(limit)


def render_market_dashboard_chart(title, series):
    st.markdown(f"### {title}")
    if series is None or series.empty:
        st.caption("표시할 기사 데이터가 없습니다.")
        return
    st.bar_chart(series)


def page_market_dashboard(shared, filters):
    st.title("Market Dashboard")
    st.caption("수집된 미국 주거시장 뉴스를 시장, 섹터, 이벤트 기준으로 확인합니다.")
    rows = market_dashboard_rows(shared)
    if rows.empty:
        missing_file_message(FILES["articles"])
        return

    total_articles = len(rows)
    core_count = int(rows.apply(lambda row: article_feed_market_group(row.to_dict()) == "Core 15", axis=1).sum())
    watchlist_count = int(rows.apply(lambda row: article_feed_market_group(row.to_dict()) == "Watchlist 8", axis=1).sum())
    access_limited_count = int(rows.apply(lambda row: article_feed_is_access_limited(row.to_dict()), axis=1).sum())
    cols = st.columns(4)
    metrics = [
        ("전체 기사 수", total_articles),
        ("Core 15 기사 수", core_count),
        ("Watchlist 8 기사 수", watchlist_count),
        ("Access-limited 기사 수", access_limited_count),
    ]
    for col, (label, value) in zip(cols, metrics):
        with col:
            render_compact_metric(label, value)

    chart_cols = st.columns(2)
    with chart_cols[0]:
        render_market_dashboard_chart("시장별 기사 수", market_dashboard_market_counts(rows))
    with chart_cols[1]:
        render_market_dashboard_chart("섹터별 기사 수", market_dashboard_sector_counts(rows))

    render_market_dashboard_chart("이벤트 태그별 기사 수", market_dashboard_event_tag_counts(rows))

    st.markdown("### Top Markets")
    top_markets = market_dashboard_market_counts(rows).head(8)
    if top_markets.empty:
        st.caption("표시할 시장 데이터가 없습니다.")
    else:
        st.table(pd.DataFrame({
            "시장 / 분류": top_markets.index,
            "기사 수": top_markets.values,
        }))

    st.markdown("### 최근 기사")
    recent_rows = market_dashboard_recent_rows(rows, limit=5)
    if recent_rows.empty:
        st.caption("표시할 최근 기사가 없습니다.")
    else:
        for _, row in recent_rows.iterrows():
            render_article_feed_item(row)

    st.caption("지도형 시장 대시보드는 다음 단계에서 추가 예정입니다.")


def market_dashboard_chip_text(series, limit=8):
    if series is None or series.empty:
        return "표시할 기사 데이터가 없습니다."
    items = []
    for label, value in series.head(limit).items():
        items.append(f"**{label}** {int(value)}")
    return " · ".join(items)


def market_dashboard_count_table(series, label_column, count_column, limit):
    if series is None or series.empty:
        return pd.DataFrame(columns=[label_column, count_column])
    trimmed = series.head(limit)
    return pd.DataFrame({
        label_column: trimmed.index,
        count_column: trimmed.astype(int).values,
    })


def render_market_dashboard_capture_cards(market_counts):
    st.markdown("### 오늘의 시장 포착")
    non_macro_counts = market_counts.drop(
        labels=["National / Macro", "Non-Core Local", "Unknown"],
        errors="ignore",
    )
    non_macro_counts = non_macro_counts[non_macro_counts > 0]
    if non_macro_counts.empty:
        top_market = "No tracked market"
        top_count = 0
    else:
        top_market = str(non_macro_counts.idxmax())
        top_count = int(non_macro_counts.max())

    macro_count = int(market_counts.get("National / Macro", 0))
    non_core_count = int(market_counts.get("Non-Core Local", 0))
    cards = [
        ("최다 포착 시장", top_market, top_count),
        ("전국/매크로 흐름", "National / Macro", macro_count),
        ("비추적 지역 신호", "Non-Core Local", non_core_count),
    ]
    cols = st.columns(3)
    for col, (label, value, count) in zip(cols, cards):
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value" style="font-size:1.1rem;line-height:1.3;">{value}</div>
                    <div class="metric-footnote">{count} articles</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_market_dashboard_ranking(market_counts, limit=10):
    st.markdown("### 기사 분포 랭킹")
    ranking = market_counts[market_counts > 0].sort_values(ascending=False).head(limit)
    if ranking.empty:
        st.caption("표시할 시장 데이터가 없습니다.")
        return
    max_count = max(int(ranking.max()), 1)
    for market, count in ranking.items():
        count = int(count)
        label_col, count_col = st.columns([4, 1])
        with label_col:
            st.markdown(f"**{market}**")
        with count_col:
            st.markdown(f"{count} articles")
        st.progress(min(count / max_count, 1.0))


MARKET_DASHBOARD_CATEGORY_CARDS = [
    (
        "개발/인허가",
        "개발계획, 착공, 준공, 인허가, 토지/부지 관련 기사",
        True,
    ),
    (
        "거래/투자",
        "자산 매각, 인수, JV, GP/운용사 투자, BTR 지분거래",
        False,
    ),
    (
        "시장 데이터",
        "임대료, 흡수율, 공실률, 공급, 정책, 매크로 시장 흐름",
        False,
    ),
]


def market_dashboard_category_count(rows, category):
    if rows.empty:
        return 0
    return int(rows.apply(
        lambda row: article_feed_display_category(row.to_dict()) == category,
        axis=1,
    ).sum())


def open_article_feed_with_category(category):
    st.session_state["article_feed_pending_category"] = category
    st.session_state["article_feed_display_category"] = category
    st.session_state["article_feed_current_page"] = 1
    st.session_state["app_page"] = "Article Feed"
    st.session_state["article_feed_applied_query_category"] = category
    try:
        st.query_params["page"] = "Article Feed"
        st.query_params["category"] = category
    except Exception:
        pass


def render_market_dashboard_category_cards(rows):
    st.markdown("### 기사 성격별 분류")
    st.caption("Article Feed와 같은 분류 기준으로 현재 수집 기사를 빠르게 엽니다. 수치는 전체 기간 기준이며 Freshness 필터 미적용입니다.")
    st.markdown(
        """
        <style>
        .dashboard-category-card {
            border: 1px solid #d8dee9;
            border-radius: 8px;
            padding: 1rem;
            min-height: 168px;
            background: #ffffff;
            box-shadow: 0 1px 2px rgba(15, 23, 42, 0.05);
        }
        .dashboard-category-card.primary {
            min-height: 204px;
            border-color: #9bb7d4;
            background: #f7fbff;
        }
        .dashboard-category-title {
            font-size: 1.05rem;
            font-weight: 700;
            margin-bottom: 0.45rem;
        }
        .dashboard-category-card.primary .dashboard-category-title {
            font-size: 1.22rem;
        }
        .dashboard-category-count {
            font-size: 2rem;
            font-weight: 750;
            line-height: 1.05;
            margin: 0.25rem 0 0.55rem;
        }
        .dashboard-category-card.primary .dashboard-category-count {
            font-size: 2.55rem;
        }
        .dashboard-category-description {
            color: #475569;
            font-size: 0.92rem;
            line-height: 1.45;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    primary = MARKET_DASHBOARD_CATEGORY_CARDS[0]
    secondary_cards = MARKET_DASHBOARD_CATEGORY_CARDS[1:]

    primary_col, secondary_col = st.columns([1.25, 2])
    with primary_col:
        category, description, emphasized = primary
        count = market_dashboard_category_count(rows, category)
        card_class = "dashboard-category-card primary" if emphasized else "dashboard-category-card"
        st.markdown(
            f"""
            <div class="{card_class}">
                <div class="dashboard-category-title">{html.escape(category)}</div>
                <div class="dashboard-category-count">{count}</div>
                <div class="dashboard-category-description">{html.escape(description)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button("기사 보기", key=f"dashboard_category_{category}", on_click=open_article_feed_with_category, args=(category,))

    with secondary_col:
        cols = st.columns(2)
        for col, (category, description, emphasized) in zip(cols, secondary_cards):
            with col:
                count = market_dashboard_category_count(rows, category)
                card_class = "dashboard-category-card primary" if emphasized else "dashboard-category-card"
                st.markdown(
                    f"""
                    <div class="{card_class}">
                        <div class="dashboard-category-title">{html.escape(category)}</div>
                        <div class="dashboard-category-count">{count}</div>
                        <div class="dashboard-category-description">{html.escape(description)}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.button("기사 보기", key=f"dashboard_category_{category}", on_click=open_article_feed_with_category, args=(category,))


def page_market_dashboard(shared, filters):
    st.title("Market Dashboard")
    st.caption("수집된 미국 주거시장 뉴스를 기사 성격별 분류 중심으로 확인합니다.")
    rows = market_dashboard_rows(shared)
    if rows.empty:
        missing_file_message(FILES["articles"])
        return

    total_articles = len(rows)
    core_count = int(rows.apply(lambda row: article_feed_market_group(row.to_dict()) == "Core 15", axis=1).sum())
    watchlist_count = int(rows.apply(lambda row: article_feed_market_group(row.to_dict()) == "Watchlist 8", axis=1).sum())
    access_limited_count = int(rows.apply(lambda row: article_feed_is_access_limited(row.to_dict()), axis=1).sum())

    cols = st.columns(4)
    metrics = [
        ("전체 기사 수", total_articles),
        ("Core 15 기사 수", core_count),
        ("Watchlist 8 기사 수", watchlist_count),
        ("Access-limited 기사 수", access_limited_count),
    ]
    for col, (label, value) in zip(cols, metrics):
        with col:
            render_compact_metric(label, value)

    render_market_dashboard_category_cards(rows)

    market_counts = market_dashboard_market_counts(rows)
    sector_counts = market_dashboard_sector_counts(rows, limit=5)
    event_tag_counts = market_dashboard_event_tag_counts(rows, limit=8)

    with st.expander("최근 수집 기사", expanded=False):
        recent_rows = market_dashboard_recent_rows(rows, limit=3)
        if recent_rows.empty:
            st.caption("표시할 최근 기사가 없습니다.")
        else:
            for _, row in recent_rows.iterrows():
                render_article_feed_item(row)

    with st.expander("주요 섹터 / 이벤트 태그", expanded=False):
        summary_cols = st.columns(2)
        with summary_cols[0]:
            st.markdown("### 주요 섹터")
            st.table(market_dashboard_count_table(sector_counts, "섹터", "기사 수", limit=5))
        with summary_cols[1]:
            st.markdown("### 주요 이벤트 태그")
            st.table(market_dashboard_count_table(event_tag_counts, "이벤트 태그", "기사 수", limit=8))

    st.caption("지도형 시장 대시보드는 다음 단계에서 추가 예정입니다.")


MARKET_SIGNAL_RULES = [
    ("Refinancing pressure unresolved", ["refinancing", "bridge loan", "recapitalization", "recap", "loan maturity"], "capital markets remain selective rather than expansionary"),
    ("Construction financing still selective", ["construction financing", "construction loan", "bridge financing"], "development capital remains available, but only for selective execution"),
    ("LA entitlement precedent accumulation", ["entitlement", "density bonus", "affordable overlay", "planning commission", "permit", "zoning"], "public approval activity is clustering more visibly than private transaction flow"),
    ("Sun Belt lease-up pressure watch", ["lease-up", "concessions", "absorption", "vacancy", "new supply"], "supply digestion remains a live underwriting question"),
    ("JV / partnership activity observed", ["joint venture", " jv ", "partnership"], "institutional behavior is visible through partnership formation rather than broad buying"),
]


def market_signal_clusters(shared):
    """Build recurring market-pattern clusters from the current article set."""
    articles = shared.get("articles", pd.DataFrame())
    if articles.empty:
        return []
    clusters = []
    for title, terms, interpretation in MARKET_SIGNAL_RULES:
        matched = articles[articles.apply(
            lambda row: any(term in text_blob(row.to_dict()) for term in terms),
            axis=1,
        )]
        if matched.empty:
            continue
        cluster_blob = " ".join(text_blob(row.to_dict()) for _, row in matched.iterrows())
        observed = [term for term in terms if term in cluster_blob]
        clusters.append({
            "title": title,
            "evidence": observed[:4],
            "frequency": len(matched),
            "interpretation": interpretation,
        })
    return sorted(clusters, key=lambda item: item["frequency"], reverse=True)


def render_market_regime_summary(shared, filters=None):
    """Dynamic regime snapshot from article-cluster frequency."""
    st.markdown("### Regime Snapshot")
    clusters = market_signal_clusters(shared)
    if not clusters:
        st.caption("이번 run에서는 뚜렷한 regime cluster가 충분히 포착되지 않았습니다.")
        return
    buckets = {
        "Capital Markets": [],
        "Development": [],
        "Supply Conditions": [],
        "Institutional Behavior": [],
    }
    for cluster in clusters:
        title = cluster["title"].lower()
        if title.startswith(("refinancing", "construction financing")):
            buckets["Capital Markets"].append(cluster)
        elif "entitlement" in title:
            buckets["Development"].append(cluster)
        elif "lease-up" in title:
            buckets["Supply Conditions"].append(cluster)
        else:
            buckets["Institutional Behavior"].append(cluster)
    for heading, items in buckets.items():
        if items:
            top = items[0]
            st.markdown(f"**{heading}**")
            st.markdown(f"- {top['title'].lower()} ({top['frequency']} related articles)")


def render_signal_clusters(shared, filters=None):
    """Render recurring market patterns rather than article summaries."""
    st.markdown("### Signal Cluster")
    clusters = market_signal_clusters(shared)
    if not clusters:
        st.caption("이번 run에서는 반복 signal cluster가 충분히 포착되지 않았습니다.")
        return
    for cluster in clusters[:5]:
        with st.container(border=True):
            st.markdown(f"**{cluster['title']}**")
            st.markdown("**Observed evidence**")
            for evidence in cluster["evidence"]:
                st.markdown(f"- {evidence}")
            st.markdown(f"**Observed frequency**  \n{cluster['frequency']} related articles this run")
            st.markdown(f"**Interpretation**  \n{cluster['interpretation']}")


def render_woomi_market_checkpoints(shared, filters=None):
    """Concise strategy-note bullets tied to detected clusters."""
    st.markdown("### 우미 관점 체크포인트")
    titles = {cluster["title"] for cluster in market_signal_clusters(shared)}
    if "LA entitlement precedent accumulation" in titles:
        st.markdown("- LA entitlement precedent accumulation continues → useful for future affordable multifamily positioning")
    if "Refinancing pressure unresolved" in titles or "Construction financing still selective" in titles:
        st.markdown("- bridge / refinancing activity remains elevated → monitor recap and rescue-capital conditions")
    if "Sun Belt lease-up pressure watch" in titles:
        st.markdown("- Sun Belt lease-up commentary remains visible → monitor absorption durability before land entry")
    if not titles:
        st.markdown("- 이번 run에서는 conviction을 높일 만큼 반복된 market cluster가 제한적입니다.")


def page_market_intelligence_product(shared, filters):
    """Market regime interpretation page rather than article re-display."""
    st.title("시장 인텔리전스")
    render_market_regime_summary(shared, filters)
    render_homepage_hot_market(shared, filters)
    render_signal_clusters(shared, filters)
    render_woomi_market_checkpoints(shared, filters)


MARKET_SIGNAL_RULES_V2 = [
    {
        "title": "Refinancing pressure unresolved",
        "ko_title": "refinancing 부담 지속 관찰",
        "terms": ["refinancing", "bridge loan", "recapitalization", "recap", "loan maturity"],
        "interpretation": "자본시장은 확장보다 만기 대응과 선택적 구조조정 중심으로 관찰됩니다.",
        "regime": "자본시장",
    },
    {
        "title": "Construction financing still selective",
        "ko_title": "construction financing 선별성 지속",
        "terms": ["construction financing", "construction loan", "bridge financing"],
        "interpretation": "개발 자금은 열려 있지만 실행력과 구조가 분명한 건에 더 집중되는 흐름입니다.",
        "regime": "자본시장",
    },
    {
        "title": "LA entitlement precedent accumulation",
        "ko_title": "LA 인허가 precedent 누적 관찰",
        "terms": ["entitlement", "density bonus", "affordable overlay", "planning commission", "permit", "zoning"],
        "interpretation": "민간 거래보다 공개 인허가 precedent가 더 뚜렷하게 기사화되고 있습니다.",
        "regime": "개발 흐름",
    },
    {
        "title": "Sun Belt lease-up pressure watch",
        "ko_title": "Sun Belt lease-up 부담 관찰",
        "terms": ["lease-up", "concessions", "absorption", "vacancy", "new supply"],
        "interpretation": "공급 소화와 임대 흡수력 검증이 여전히 underwriting의 핵심 변수입니다.",
        "regime": "공급 / 임대시장",
    },
    {
        "title": "JV / partnership activity observed",
        "ko_title": "JV / partnership activity 증가 관찰",
        "terms": ["joint venture", " jv ", "partnership"],
        "interpretation": "기관 참여는 공격적 매입보다 파트너십 형성으로 먼저 드러나는 양상입니다.",
        "regime": "기관 행동 흐름",
    },
]


def market_signal_clusters(shared):
    """Build recurring market-pattern clusters from the current article set."""
    articles = shared.get("articles", pd.DataFrame())
    if articles.empty:
        return []
    clusters = []
    for rule in MARKET_SIGNAL_RULES_V2:
        terms = rule["terms"]
        matched = articles[articles.apply(
            lambda row: any(term in text_blob(row.to_dict()) for term in terms),
            axis=1,
        )]
        if matched.empty:
            continue
        cluster_blob = " ".join(text_blob(row.to_dict()) for _, row in matched.iterrows())
        observed = [term for term in terms if term in cluster_blob]
        clusters.append({
            "title": rule["title"],
            "ko_title": rule["ko_title"],
            "evidence": observed[:4],
            "dominant_signal": " / ".join(observed[:3]),
            "frequency": len(matched),
            "interpretation": rule["interpretation"],
            "regime": rule["regime"],
        })
    return sorted(clusters, key=lambda item: item["frequency"], reverse=True)


def render_market_regime_summary(shared, filters=None):
    """Dynamic regime snapshot from article-cluster frequency."""
    st.markdown("### Regime Snapshot")
    clusters = market_signal_clusters(shared)
    if not clusters:
        st.caption("이번 run에서는 충분히 반복된 regime cluster가 포착되지 않았습니다.")
        return
    buckets = {"자본시장": [], "개발 흐름": [], "공급 / 임대시장": [], "기관 행동 흐름": []}
    for cluster in clusters:
        buckets[cluster["regime"]].append(cluster)
    for heading, items in buckets.items():
        if items:
            top = items[0]
            st.markdown(f"**{heading}**")
            st.markdown(f"- {top['ko_title']} ({top['frequency']}건)")


def render_signal_clusters(shared, filters=None):
    """Render recurring market patterns in a compact scan-friendly layout."""
    st.markdown("### Signal Cluster")
    clusters = market_signal_clusters(shared)
    if not clusters:
        st.caption("이번 run에서는 반복 signal cluster가 충분히 포착되지 않았습니다.")
        return
    for cluster in clusters[:5]:
        label = f"{cluster['ko_title']} · {cluster['frequency']}건 · {cluster['dominant_signal'] or '관찰 신호'}"
        with st.expander(label, expanded=False):
            st.markdown("**Observed evidence**")
            for evidence in cluster["evidence"]:
                st.markdown(f"- {evidence}")
            st.markdown(f"**Observed frequency**  \n{cluster['frequency']} related articles this run")
            st.markdown(f"**Interpretation**  \n{cluster['interpretation']}")


def render_woomi_market_checkpoints(shared, filters=None):
    """Concise Korean strategy-note bullets tied to detected clusters."""
    st.markdown("### 우미 관점 체크포인트")
    titles = {cluster["title"] for cluster in market_signal_clusters(shared)}
    if "LA entitlement precedent accumulation" in titles:
        st.markdown("- LA affordable entitlement precedent가 지속 누적되고 있어 향후 multifamily positioning 참고가 필요합니다.")
    if "Refinancing pressure unresolved" in titles or "Construction financing still selective" in titles:
        st.markdown("- bridge financing / refinancing activity가 반복되어 recap 및 rescue-capital 환경을 계속 관찰할 필요가 있습니다.")
    if "Sun Belt lease-up pressure watch" in titles:
        st.markdown("- Sun Belt lease-up commentary가 반복되어 land entry 전 absorption durability 추가 확인이 필요합니다.")
    if not titles:
        st.markdown("- 이번 run에서는 반복성이 충분한 market cluster가 제한적입니다. 추가 데이터 누적 후 판단 강도를 높이는 편이 적절합니다.")


def render_homepage_hot_market(shared, filters=None):
    """Weighted market activity view rather than raw article-volume ranking."""
    st.markdown("### 오늘의 Hot Market / 시장 집중도")
    frames = [
        apply_filters(shared["cards"], filters),
        apply_filters(shared["opportunities"], filters),
        apply_filters(shared["high_confidence"], filters),
    ]
    score_by_market = {}
    source_counts = {}
    entity_sets = {}
    signal_sets = {}
    for frame in frames:
        if frame is None or frame.empty:
            continue
        for _, row in frame.iterrows():
            item = row.to_dict()
            market = str(item.get("market", "")).strip()
            if not market or market.lower() in {"other / unknown", "unknown", "other", "national"}:
                continue
            blob = text_blob(item)
            score = 1
            if any(term in blob for term in ["acquisition", "joint venture", " jv ", "construction financing", "recapitalization", "refinancing"]):
                score += 3
            if any(term in blob for term in ["lease-up", "concessions", "absorption"]):
                score += 1
            source = str(item.get("source", item.get("source_report", ""))).strip()
            source_key = (market, source)
            source_counts[source_key] = source_counts.get(source_key, 0) + 1
            if source_counts[source_key] > 1:
                score -= 1
            gp = str(item.get("gp_or_developer", item.get("canonical_gp_name", ""))).strip()
            lender = str(item.get("lender_or_capital_partner", item.get("firm_name", ""))).strip()
            entity_sets.setdefault(market, set()).update(value for value in [gp, lender] if value)
            signal_sets.setdefault(market, set()).update(
                label for label, terms in [
                    ("elevated JV activity", ["joint venture", " jv ", "partnership"]),
                    ("construction financing", ["construction financing", "construction loan"]),
                    ("recurring lease-up commentary", ["lease-up", "concessions", "absorption"]),
                    ("refinancing / recap", ["refinancing", "recapitalization", "recap"]),
                ]
                if any(term in blob for term in terms)
            )
            score_by_market[market] = score_by_market.get(market, 0) + max(score, 0)
    for market, entities in entity_sets.items():
        score_by_market[market] = score_by_market.get(market, 0) + min(len(entities), 3)
    if not score_by_market:
        st.markdown("**시장 집중도 분산**")
        st.write("현재 기사 기준으로 특정 시장에 거래 및 자본 흐름이 뚜렷하게 집중된다고 보기는 어렵습니다.")
        return
    top_market, top_score = sorted(score_by_market.items(), key=lambda item: item[1], reverse=True)[0]
    if top_score < 4:
        st.markdown("**시장 집중도 분산**")
        st.write("현재 기사 기준으로 특정 시장에 거래 및 자본 흐름이 뚜렷하게 집중된다고 보기는 어렵습니다.")
        return
    st.markdown(f"**{top_market}**")
    reasons = sorted(signal_sets.get(top_market, set()))
    if reasons:
        st.write("선정 근거: " + ", ".join(reasons))
    st.caption("단순 기사 수가 아니라 transaction relevance, unique GP/lender, source 반복 패널티를 함께 반영한 관찰입니다.")


def market_diagnostics_map(shared):
    diagnostics = shared.get("market_intelligence_diagnostics", pd.DataFrame())
    if diagnostics.empty:
        return {}
    return {
        str(row.get("generated_signal_cluster", "")): row.to_dict()
        for _, row in diagnostics.iterrows()
    }


def dynamic_market_interpretation(cluster, diagnostic):
    """Produce concise desk-note interpretations from cluster context."""
    market = str(diagnostic.get("dominant_market", "") or "")
    financing = str(diagnostic.get("dominant_financing_patterns", "") or "")
    lifecycle = str(diagnostic.get("dominant_lifecycle_tags", "") or "")
    keywords = str(diagnostic.get("dominant_keywords", "") or "")
    delta = int(as_number(diagnostic.get("prior_run_delta", 0)))
    article_count = int(as_number(diagnostic.get("supporting_article_count", cluster["frequency"])))
    source_diversity = int(as_number(diagnostic.get("source_diversity_score", 0)))
    lender_diversity = int(as_number(diagnostic.get("lender_diversity_score", 0)))
    title = cluster["title"]

    if title == "Refinancing pressure unresolved":
        if "bridge loan" in financing and delta > 0:
            return "bridge-heavy refinancing visibility is rising; liquidity pressure may be building beneath the surface."
        if lender_diversity >= 2:
            return "refinancing remains functional, but lender participation is selective rather than broad-based."
        return "refinancing visibility remains muted, suggesting stress is not yet broadening in the current article set."
    if title == "Construction financing still selective":
        if market == "Los Angeles" and article_count >= 3:
            return "construction capital is still available in Los Angeles, but deployment remains concentrated and selective."
        if source_diversity >= 3:
            return "construction financing is appearing across several sources, pointing to selective reopening rather than a broad thaw."
        return "lender caution persists; construction capital is visible but not yet broadly distributed."
    if title == "LA entitlement precedent accumulation":
        if "density bonus" in keywords and "zoning" in keywords:
            return "policy-enabled entitlement activity is becoming more visible, especially where density incentives support feasibility."
        if delta > 0:
            return "approval visibility is expanding, but the signal still reflects public precedent more than private capital movement."
        return "LA entitlement precedent remains visible and steady, with affordable incentives continuing to shape the observed pipeline."
    if title == "Sun Belt lease-up pressure watch":
        if "concessions" in keywords and "absorption" in keywords:
            return "concession and absorption references are co-occurring, indicating widening divergence in supply digestion."
        if delta > 0:
            return "lease-up commentary is broadening, keeping absorption durability near the center of underwriting."
        return "Sun Belt supply digestion remains an active watch item rather than a resolved normalization story."
    if title == "JV / partnership activity observed":
        if delta > 0 or source_diversity >= 2:
            return "institutional deployment may be reopening selectively through partnership structures before direct acquisitions."
        return "capital deployment remains disciplined, with partnership activity visible but still narrow in breadth."
    return cluster["interpretation"]


def market_signal_clusters(shared):
    """Build recurring market-pattern clusters and enrich them with diagnostics."""
    articles = shared.get("articles", pd.DataFrame())
    if articles.empty:
        return []
    diagnostics = market_diagnostics_map(shared)
    clusters = []
    for rule in MARKET_SIGNAL_RULES_V2:
        terms = rule["terms"]
        matched = articles[articles.apply(
            lambda row: any(term in text_blob(row.to_dict()) for term in terms),
            axis=1,
        )]
        if matched.empty:
            continue
        cluster_blob = " ".join(text_blob(row.to_dict()) for _, row in matched.iterrows())
        observed = [term for term in terms if term in cluster_blob]
        diagnostic = diagnostics.get(rule["title"], {})
        status = str(diagnostic.get("cluster_status", "") or "")
        if not status:
            status = "newly emerging" if len(matched) else "inactive"
        cluster = {
            "title": rule["title"],
            "ko_title": rule["ko_title"],
            "evidence": observed[:4],
            "dominant_signal": " / ".join(observed[:3]),
            "frequency": len(matched),
            "regime": rule["regime"],
            "status": status,
            "diagnostic": diagnostic,
        }
        cluster["interpretation"] = dynamic_market_interpretation(cluster, diagnostic)
        clusters.append(cluster)
    return sorted(clusters, key=lambda item: item["frequency"], reverse=True)


def cluster_status_label(status):
    return {
        "expanding": "expanding",
        "stable": "stable",
        "fading": "fading",
        "newly emerging": "newly emerging",
        "inactive": "inactive",
    }.get(status, status or "stable")


def render_signal_clusters(shared, filters=None):
    """Render recurring market patterns with state-aware detail."""
    st.markdown("### Signal Cluster")
    clusters = market_signal_clusters(shared)
    if not clusters:
        st.caption("이번 run에서는 반복 signal cluster가 충분히 포착되지 않았습니다.")
        return
    for cluster in clusters[:5]:
        diagnostic = cluster["diagnostic"]
        label = (
            f"{cluster['ko_title']} · {cluster['frequency']}건 · "
            f"{cluster['dominant_signal'] or '관찰 신호'} · Status: {cluster_status_label(cluster['status'])}"
        )
        with st.expander(label, expanded=False):
            st.markdown("**Observed evidence**")
            for evidence in cluster["evidence"]:
                st.markdown(f"- {evidence}")
            st.markdown(f"**Interpretation**  \n{cluster['interpretation']}")
            market = diagnostic.get("dominant_market", "")
            financing = diagnostic.get("dominant_financing_patterns", "")
            if market:
                st.markdown(f"**Dominant market**  \n{market}")
            if financing:
                st.markdown(f"**Financing pattern**  \n{financing}")
            st.markdown(
                f"**Status explanation**  \n"
                f"{diagnostic.get('regime_shift_signal', 'steady visibility')} "
                f"(prior-run delta {int(as_number(diagnostic.get('prior_run_delta', 0)))})"
            )


def render_woomi_market_checkpoints(shared, filters=None):
    """Generate status-aware Woomi checkpoints from detected clusters."""
    st.markdown("### 우미 관점 체크포인트")
    clusters = {cluster["title"]: cluster for cluster in market_signal_clusters(shared)}
    la_cluster = clusters.get("LA entitlement precedent accumulation")
    if la_cluster:
        st.markdown(
            f"- LA affordable entitlement precedent가 {cluster_status_label(la_cluster['status'])} 상태로 관찰되어 "
            "향후 multifamily positioning 참고가 필요합니다."
        )
    financing_cluster = clusters.get("Refinancing pressure unresolved") or clusters.get("Construction financing still selective")
    if financing_cluster:
        st.markdown(
            f"- bridge financing / refinancing activity가 {cluster_status_label(financing_cluster['status'])}하게 반복되어 "
            "recap 및 rescue-capital 환경을 계속 관찰할 필요가 있습니다."
        )
    supply_cluster = clusters.get("Sun Belt lease-up pressure watch")
    if supply_cluster:
        st.markdown(
            f"- Sun Belt lease-up commentary가 {cluster_status_label(supply_cluster['status'])} 상태로 유지되어 "
            "land entry 전 absorption durability 추가 확인이 필요합니다."
        )
    if not clusters:
        st.markdown("- 이번 run에서는 반복성이 충분한 market cluster가 제한적입니다. 추가 데이터 누적 후 판단 강도를 높이는 편이 적절합니다.")


def page_market_intelligence_product(shared, filters):
    """Market regime interpretation page rather than article re-display."""
    st.title("시장 인텔리전스")
    render_woomi_market_checkpoints(shared, filters)
    render_market_regime_summary(shared, filters)
    render_homepage_hot_market(shared, filters)
    render_signal_clusters(shared, filters)


def dynamic_market_interpretation(cluster, diagnostic):
    """Produce source-aware desk-note interpretations from cluster context."""
    market = str(diagnostic.get("dominant_market", "") or "")
    financing = str(diagnostic.get("dominant_financing_patterns", "") or "")
    keywords = str(diagnostic.get("dominant_keywords", "") or "")
    delta = int(as_number(diagnostic.get("prior_run_delta", 0)))
    article_count = int(as_number(diagnostic.get("supporting_article_count", cluster["frequency"])))
    source_diversity = int(as_number(diagnostic.get("source_diversity_score", 0)))
    lender_diversity = int(as_number(diagnostic.get("lender_diversity_score", 0)))
    confidence = str(diagnostic.get("signal_confidence_label", "") or "")
    title = cluster["title"]
    if confidence == "Source-Concentrated":
        if title == "LA entitlement precedent accumulation":
            return "LA entitlement coverage remains highly visible, but signal strength is source-concentrated."
        return "signal visibility is elevated, but confirmation remains source-concentrated rather than broad-based."
    if confidence == "Broadly Confirmed":
        if title == "Refinancing pressure unresolved":
            return "refinancing pressure is broadly confirmed across multiple sources and markets."
        if title == "Sun Belt lease-up pressure watch":
            return "supply digestion concerns are broadly confirmed across several sources."
    if title == "Refinancing pressure unresolved":
        if "bridge loan" in financing and delta > 0:
            return "bridge-heavy refinancing visibility is rising; liquidity pressure may be building beneath the surface."
        if lender_diversity >= 2:
            return "refinancing remains functional, but lender participation is selective rather than broad-based."
        return "refinancing visibility remains muted, suggesting stress is not yet broadening in the current article set."
    if title == "Construction financing still selective":
        if market == "Los Angeles" and article_count >= 3:
            return "construction capital is still available in Los Angeles, but deployment remains concentrated and selective."
        if source_diversity >= 3:
            return "construction financing is appearing across several sources, pointing to selective reopening rather than a broad thaw."
        return "lender caution persists; construction capital is visible but not yet broadly distributed."
    if title == "LA entitlement precedent accumulation":
        if "density bonus" in keywords and "zoning" in keywords:
            return "policy-enabled entitlement activity is becoming more visible, especially where density incentives support feasibility."
        if delta > 0:
            return "approval visibility is expanding, but the signal still reflects public precedent more than private capital movement."
        return "LA entitlement precedent remains visible and steady, with affordable incentives continuing to shape the observed pipeline."
    if title == "Sun Belt lease-up pressure watch":
        if "concessions" in keywords and "absorption" in keywords:
            return "concession and absorption references are co-occurring, indicating widening divergence in supply digestion."
        if delta > 0:
            return "lease-up commentary is broadening, keeping absorption durability near the center of underwriting."
        return "Sun Belt supply digestion remains an active watch item rather than a resolved normalization story."
    if title == "JV / partnership activity observed":
        if delta > 0 or source_diversity >= 2:
            return "institutional deployment may be reopening selectively through partnership structures before direct acquisitions."
        return "capital deployment remains disciplined, with partnership activity visible but still narrow in breadth."
    return cluster.get("interpretation", "")


def market_signal_clusters(shared):
    """Build recurring market-pattern clusters using retained diagnostics counts."""
    articles = shared.get("articles", pd.DataFrame())
    if articles.empty:
        return []
    diagnostics = market_diagnostics_map(shared)
    clusters = []
    for rule in MARKET_SIGNAL_RULES_V2:
        terms = rule["terms"]
        matched = articles[articles.apply(lambda row: any(term in text_blob(row.to_dict()) for term in terms), axis=1)]
        if matched.empty:
            continue
        cluster_blob = " ".join(text_blob(row.to_dict()) for _, row in matched.iterrows())
        observed = [term for term in terms if term in cluster_blob]
        diagnostic = diagnostics.get(rule["title"], {})
        retained_count = int(as_number(diagnostic.get("supporting_article_count", len(matched))))
        cluster = {
            "title": rule["title"],
            "ko_title": rule["ko_title"],
            "evidence": observed[:4],
            "dominant_signal": " / ".join(observed[:3]),
            "frequency": retained_count,
            "regime": rule["regime"],
            "status": str(diagnostic.get("cluster_status", "") or "newly emerging"),
            "diagnostic": diagnostic,
        }
        cluster["interpretation"] = dynamic_market_interpretation(cluster, diagnostic)
        clusters.append(cluster)
    return sorted(clusters, key=lambda item: item["frequency"], reverse=True)


def render_signal_clusters(shared, filters=None):
    """Render state- and confidence-aware cluster cards."""
    st.markdown("### Signal Cluster")
    clusters = market_signal_clusters(shared)
    if not clusters:
        st.caption("이번 run에서는 반복 signal cluster가 충분히 포착되지 않았습니다.")
        return
    for cluster in clusters[:5]:
        diagnostic = cluster["diagnostic"]
        label = (
            f"{cluster['ko_title']} · {cluster['frequency']}건 · "
            f"{cluster['dominant_signal'] or '관찰 신호'} · Status: {cluster_status_label(cluster['status'])} · "
            f"Confidence: {diagnostic.get('signal_confidence_label', 'Early Signal')}"
        )
        with st.expander(label, expanded=False):
            st.markdown("**Observed evidence**")
            for evidence in cluster["evidence"]:
                st.markdown(f"- {evidence}")
            st.markdown(f"**Interpretation**  \n{cluster['interpretation']}")
            if diagnostic.get("dominant_market", ""):
                st.markdown(f"**Dominant market**  \n{diagnostic.get('dominant_market')}")
            if diagnostic.get("dominant_financing_patterns", ""):
                st.markdown(f"**Financing pattern**  \n{diagnostic.get('dominant_financing_patterns')}")
            st.markdown(
                f"**Status explanation**  \n{diagnostic.get('regime_shift_signal', 'steady visibility')} "
                f"(prior-run delta {int(as_number(diagnostic.get('prior_run_delta', 0)))})"
            )
            st.markdown(
                f"**Confidence explanation**  \n{diagnostic.get('confidence_explanation', 'evidence base still developing')}"
            )


def regime_timeline_map(shared):
    timeline = shared.get("regime_timeline", pd.DataFrame())
    if timeline.empty:
        return {}
    return {
        str(row.get("cluster_title", "")): row.to_dict()
        for _, row in timeline.iterrows()
    }


def market_synthesis_bullets(shared):
    """Return time-aware cross-cluster synthesis bullets."""
    timeline = regime_timeline_map(shared)
    diagnostics = shared.get("market_intelligence_diagnostics", pd.DataFrame())
    if diagnostics.empty:
        return []
    rows = {str(row.get("generated_signal_cluster", "")): row.to_dict() for _, row in diagnostics.iterrows()}
    bullets = []
    financing = timeline.get("Refinancing pressure unresolved", {})
    construction = timeline.get("Construction financing still selective", {})
    entitlement = timeline.get("LA entitlement precedent accumulation", {})
    supply = timeline.get("Sun Belt lease-up pressure watch", {})
    jv = timeline.get("JV / partnership activity observed", {})
    if construction or financing:
        if financing.get("persistence_label") == "Persistent":
            bullets.append("refinancing 부담은 최근 run 전반에서 지속적으로 관찰되며, 자본시장은 선별적으로 작동하고 있습니다.")
        else:
            bullets.append("자본시장은 완전히 닫힌 상태라기보다, 선별적 refinancing과 construction financing 중심으로 작동하고 있습니다.")
    if entitlement:
        if entitlement.get("trend_direction") == "weakening":
            bullets.append("LA entitlement visibility는 유지되지만 최근 momentum은 다소 약화됐습니다.")
        elif rows.get("LA entitlement precedent accumulation", {}).get("signal_confidence_label") == "Source-Concentrated":
            bullets.append("LA 인허가 관련 보도는 계속 관찰되지만, source 집중도가 높아 시장 전반으로 일반화하기는 어렵습니다.")
        else:
            bullets.append("LA 인허가 precedent는 꾸준히 누적되고 있으며, affordable incentive 기반 개발 흐름이 계속 기사화되고 있습니다.")
    if supply:
        if supply.get("persistence_label") == "Building":
            bullets.append("Sun Belt lease-up commentary는 최근 보고에서 계속 축적되고 있어 absorption durability 확인이 필요합니다.")
        else:
            bullets.append("Sun Belt는 신규 공급 소화와 lease-up 속도 확인이 필요한 시장으로 계속 관찰됩니다.")
    if jv and jv.get("trend_direction") == "re-emerging":
        bullets.append("기관 partnership activity는 조용한 구간 이후 다시 관찰되기 시작했습니다.")
    return bullets[:3]


def render_today_market_interpretation(shared, filters=None):
    """Render cross-cluster, time-aware regime synthesis."""
    st.markdown("### 오늘의 시장 해석")
    bullets = market_synthesis_bullets(shared)
    if not bullets:
        st.caption("이번 run에서는 여러 cluster를 묶어 해석할 만큼 충분한 교차 신호가 포착되지 않았습니다.")
        return
    for bullet in bullets:
        st.markdown(f"- {bullet}")


def render_today_regime_changes(shared):
    """Render only meaningful time-series shifts."""
    st.markdown("### 오늘의 변화 감지")
    timeline = shared.get("regime_timeline", pd.DataFrame())
    if timeline.empty:
        st.caption("아직 누적된 regime history가 충분하지 않습니다.")
        return
    meaningful = timeline[
        timeline["trend_direction"].isin(["accelerating", "weakening", "re-emerging"])
        | timeline["persistence_label"].isin(["Peaking"])
    ]
    if meaningful.empty:
        st.caption("오늘은 의미 있는 regime shift가 새로 포착되지 않았습니다.")
        return
    for _, row in meaningful.head(4).iterrows():
        st.markdown(f"- {row.get('regime_shift_signal')}")


def render_woomi_market_checkpoints(shared, filters=None):
    """Generate persistence-aware Woomi checkpoints."""
    st.markdown("### 우미 관점 체크포인트")
    timeline = regime_timeline_map(shared)
    if not timeline:
        st.markdown("- 추가 데이터 누적 후 시장 방향성 판단 강도를 높이는 편이 적절합니다.")
        return
    financing = timeline.get("Refinancing pressure unresolved", {})
    construction = timeline.get("Construction financing still selective", {})
    entitlement = timeline.get("LA entitlement precedent accumulation", {})
    supply = timeline.get("Sun Belt lease-up pressure watch", {})
    jv = timeline.get("JV / partnership activity observed", {})
    if financing.get("persistence_label") == "Persistent" or construction:
        st.markdown("- debt stress / recap 후보군은 단기 현상보다 구조적 pressure 가능성까지 함께 고려할 필요가 있습니다.")
    if supply:
        if supply.get("persistence_label") == "Building":
            st.markdown("- Sun Belt는 absorption durability와 concession 추세를 지속 모니터링할 필요가 있습니다.")
        else:
            st.markdown("- Sun Belt는 absorption durability 확인이 우선이며, land entry 판단은 lease-up 지속성 검증 이후가 적절합니다.")
    if entitlement:
        if entitlement.get("trend_direction") == "weakening":
            st.markdown("- entitlement precedent 흐름은 유지되나 최근 visibility는 다소 약화되어 추가 확인이 필요합니다.")
        else:
            st.markdown("- LA entitlement precedent는 참고 가치가 있으나, planning docket과 별도 source로 계속 검증하는 편이 적절합니다.")
    if jv and jv.get("trend_direction") == "re-emerging":
        st.markdown("- JV relationship tracking을 다시 강화할 필요가 있습니다.")


def market_signal_clusters(shared):
    """Build recurring market-pattern clusters with time-series context."""
    articles = shared.get("articles", pd.DataFrame())
    if articles.empty:
        return []
    diagnostics = market_diagnostics_map(shared)
    timeline = regime_timeline_map(shared)
    clusters = []
    for rule in MARKET_SIGNAL_RULES_V2:
        terms = rule["terms"]
        matched = articles[articles.apply(lambda row: any(term in text_blob(row.to_dict()) for term in terms), axis=1)]
        if matched.empty:
            continue
        cluster_blob = " ".join(text_blob(row.to_dict()) for _, row in matched.iterrows())
        observed = [term for term in terms if term in cluster_blob]
        diagnostic = diagnostics.get(rule["title"], {})
        timeline_row = timeline.get(rule["title"], {})
        retained_count = int(as_number(diagnostic.get("supporting_article_count", len(matched))))
        cluster = {
            "title": rule["title"],
            "ko_title": rule["ko_title"],
            "evidence": observed[:4],
            "dominant_signal": " / ".join(observed[:3]),
            "frequency": retained_count,
            "regime": rule["regime"],
            "status": str(diagnostic.get("cluster_status", "") or "newly emerging"),
            "diagnostic": diagnostic,
            "timeline": timeline_row,
        }
        cluster["interpretation"] = dynamic_market_interpretation(cluster, diagnostic)
        clusters.append(cluster)
    return sorted(clusters, key=lambda item: item["frequency"], reverse=True)


def render_signal_clusters(shared, filters=None):
    """Render state-, persistence-, and confidence-aware cluster cards."""
    st.markdown("### Signal Cluster")
    clusters = market_signal_clusters(shared)
    if not clusters:
        st.caption("이번 run에서는 반복 signal cluster가 충분히 포착되지 않았습니다.")
        return
    for cluster in clusters[:5]:
        diagnostic = cluster["diagnostic"]
        timeline = cluster["timeline"]
        label = (
            f"{cluster['ko_title']} · {cluster['frequency']}건 · "
            f"{timeline.get('persistence_label', 'Newly Emerging')} · "
            f"{timeline.get('trend_direction', 'stable')} · "
            f"{diagnostic.get('signal_confidence_label', 'Early Signal')}"
        )
        with st.expander(label, expanded=False):
            st.markdown("**Observed evidence**")
            for evidence in cluster["evidence"]:
                st.markdown(f"- {evidence}")
            st.markdown(f"**Interpretation**  \n{cluster['interpretation']}")
            st.markdown(
                f"**Persistence explanation**  \n"
                f"{timeline.get('persistence_label', 'Newly Emerging')} across "
                f"{timeline.get('consecutive_run_count', 0)} consecutive run(s); "
                f"{timeline.get('30d_presence', 0)} active day(s) in the last 30 days."
            )
            if diagnostic.get("dominant_market", ""):
                st.markdown(f"**Dominant market**  \n{diagnostic.get('dominant_market')}")
            if diagnostic.get("dominant_financing_patterns", ""):
                st.markdown(f"**Financing pattern**  \n{diagnostic.get('dominant_financing_patterns')}")
            st.markdown(f"**Regime shift explanation**  \n{timeline.get('regime_shift_signal', 'steady visibility')}")


def page_market_intelligence_product(shared, filters):
    """Market regime interpretation page with rolling memory."""
    st.title("시장 인텔리전스")
    render_woomi_market_checkpoints(shared, filters)
    render_today_market_interpretation(shared, filters)
    render_today_regime_changes(shared)
    render_market_regime_summary(shared, filters)
    render_homepage_hot_market(shared, filters)
    render_signal_clusters(shared, filters)


def market_synthesis_bullets(shared):
    """Return collector-generated cross-cluster regime synthesis bullets."""
    diagnostics = shared.get("market_intelligence_diagnostics", pd.DataFrame())
    if diagnostics.empty or "regime_synthesis_text" not in diagnostics.columns:
        return []
    text = str(diagnostics.iloc[0].get("regime_synthesis_text", "") or "")
    return [item.strip() for item in text.split("|") if item.strip()]


def render_today_market_interpretation(shared, filters=None):
    """Render cross-cluster market regime synthesis."""
    st.markdown("### 오늘의 시장 해석")
    bullets = market_synthesis_bullets(shared)
    if not bullets:
        st.caption("이번 run에서는 여러 cluster를 묶어 해석할 만큼 충분한 교차 신호가 포착되지 않았습니다.")
        return
    for bullet in bullets[:3]:
        st.markdown(f"- {bullet}")


def render_woomi_market_checkpoints(shared, filters=None):
    """Generate synthesis-aware Woomi checkpoints."""
    st.markdown("### 우미 관점 체크포인트")
    diagnostics = shared.get("market_intelligence_diagnostics", pd.DataFrame())
    if diagnostics.empty:
        st.markdown("- 이번 run에서는 반복성이 충분한 market cluster가 제한적입니다. 추가 데이터 누적 후 판단 강도를 높이는 편이 적절합니다.")
        return
    first = diagnostics.iloc[0].to_dict()
    drivers = str(first.get("woomi_watchpoint_driver", "") or "")
    caution_flags = str(first.get("caution_flags", "") or "")
    if "debt stress / recap" in drivers:
        st.markdown("- debt stress / recap 후보는 계속 관찰하되, 실제 투자 검토 전 lender와 sponsor 상황 확인이 필요합니다.")
    if "LA entitlement verification" in drivers:
        if "LA entitlement source concentration" in caution_flags:
            st.markdown("- LA entitlement precedent는 참고하되, source 편중 가능성을 감안해 planning docket 또는 별도 source로 추가 검증이 필요합니다.")
        else:
            st.markdown("- LA entitlement precedent 누적은 향후 affordable multifamily positioning 참고 자료로 활용할 수 있습니다.")
    if "absorption durability" in drivers:
        st.markdown("- Sun Belt는 absorption durability 확인이 우선이며, land entry 판단은 lease-up 지속성 검증 이후가 적절합니다.")
    if "partner mapping" in drivers:
        st.markdown("- JV / partnership 신호는 아직 초기 단계이므로, 즉시 투자안보다 관계 map 업데이트부터 진행하는 편이 적절합니다.")


def page_market_intelligence_product(shared, filters):
    """Market regime interpretation page rather than article re-display."""
    st.title("시장 인텔리전스")
    render_woomi_market_checkpoints(shared, filters)
    render_today_market_interpretation(shared, filters)
    render_market_regime_summary(shared, filters)
    render_homepage_hot_market(shared, filters)
    render_signal_clusters(shared, filters)


def render_woomi_market_checkpoints(shared, filters=None):
    """Generate persistence-aware Woomi checkpoints."""
    st.markdown("### 우미 관점 체크포인트")
    timeline = regime_timeline_map(shared)
    if not timeline:
        st.markdown("- 추가 데이터 누적 후 시장 방향성 판단 강도를 높이는 편이 적절합니다.")
        return
    financing = timeline.get("Refinancing pressure unresolved", {})
    construction = timeline.get("Construction financing still selective", {})
    entitlement = timeline.get("LA entitlement precedent accumulation", {})
    supply = timeline.get("Sun Belt lease-up pressure watch", {})
    jv = timeline.get("JV / partnership activity observed", {})
    if financing.get("persistence_label") == "Persistent" or construction:
        st.markdown("- debt stress / recap 후보군은 단기 현상보다 구조적 pressure 가능성까지 함께 고려할 필요가 있습니다.")
    if supply:
        if supply.get("persistence_label") == "Building":
            st.markdown("- Sun Belt는 absorption durability와 concession 추세를 지속 모니터링할 필요가 있습니다.")
        else:
            st.markdown("- Sun Belt는 absorption durability 확인이 우선이며, land entry 판단은 lease-up 지속성 검증 이후가 적절합니다.")
    if entitlement:
        if entitlement.get("trend_direction") == "weakening":
            st.markdown("- entitlement precedent 흐름은 유지되나 최근 visibility는 다소 약화되어 추가 확인이 필요합니다.")
        else:
            st.markdown("- LA entitlement precedent는 참고 가치가 있으나, planning docket과 별도 source로 계속 검증하는 편이 적절합니다.")
    if jv and jv.get("trend_direction") == "re-emerging":
        st.markdown("- JV relationship tracking을 다시 강화할 필요가 있습니다.")


def page_market_intelligence_product(shared, filters):
    """Market regime interpretation page with rolling memory."""
    st.title("시장 인텔리전스")
    render_woomi_market_checkpoints(shared, filters)
    render_today_market_interpretation(shared, filters)
    render_today_regime_changes(shared)
    render_market_regime_summary(shared, filters)
    render_homepage_hot_market(shared, filters)
    render_signal_clusters(shared, filters)


# ---------------------------------------------------------
# Pilot UX polish overrides
# ---------------------------------------------------------

def inject_css():
    """Lightweight institutional UI polish for pilot review."""
    st.markdown(
        """
        <style>
        :root {
            --ink: #111827;
            --muted: #64748b;
            --line: #d7dde6;
            --panel: #ffffff;
        }
        .block-container { padding-top: 1.1rem; padding-bottom: 2.2rem; max-width: 1140px; }
        section[data-testid="stSidebar"] { width: 16.5rem !important; border-right: 1px solid #e2e8f0; }
        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { font-size: 0.86rem; line-height: 1.35; }
        h1 { font-size: 1.7rem !important; letter-spacing: 0; margin: 0.25rem 0 0.65rem 0 !important; color: var(--ink); }
        h2, h3 { letter-spacing: 0; color: var(--ink); }
        h3 {
            font-size: 1.08rem !important;
            margin-top: 1.3rem !important;
            margin-bottom: 0.55rem !important;
            padding-top: 0.15rem;
        }
        div[data-testid="stExpander"] {
            border: 1px solid #dbe2ea;
            border-radius: 7px;
            background: #ffffff;
            margin-bottom: 0.55rem;
        }
        div[data-testid="stExpander"] details summary { font-weight: 650; color: #1f2937; }
        .stDataFrame { border: 1px solid #e5e7eb; border-radius: 6px; overflow: hidden; }
        .workstation-card, .pilot-panel, .pilot-card {
            border: 1px solid var(--line);
            border-radius: 7px;
            background: var(--panel);
            margin: 0.6rem 0 0.9rem 0;
            box-shadow: 0 1px 0 rgba(15, 23, 42, 0.03);
        }
        .workstation-card, .pilot-panel { padding: 0.95rem 1rem; }
        .pilot-card { padding: 0.72rem 0.85rem; }
        .pilot-section {
            border-top: 1px solid #dfe5ec;
            padding-top: 0.95rem;
            margin-top: 1.15rem;
        }
        .section-kicker {
            color: #475569;
            font-size: 0.73rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.04rem;
            margin-bottom: 0.15rem;
        }
        .signal-title {
            color: var(--ink);
            font-size: 1.02rem;
            font-weight: 760;
            line-height: 1.34;
            margin: 0.08rem 0 0.28rem 0;
            overflow-wrap: anywhere;
        }
        .muted-label, .pilot-muted { color: var(--muted); font-size: 0.83rem; line-height: 1.42; }
        .pilot-row { display: flex; gap: 0.45rem; flex-wrap: wrap; align-items: center; margin: 0.35rem 0 0.2rem 0; }
        .pilot-chip {
            display: inline-block;
            border: 1px solid #cbd5e1;
            border-radius: 999px;
            padding: 0.12rem 0.45rem;
            margin: 0.06rem 0.14rem 0.06rem 0;
            background: #f8fafc;
            color: #334155;
            font-size: 0.74rem;
            font-weight: 720;
            line-height: 1.3;
            white-space: nowrap;
        }
        .chip-expanding { color: #7c5517; background: #fbf3df; border-color: #ead7aa; }
        .chip-weakening { color: #315b76; background: #e8f1f7; border-color: #c8dae7; }
        .chip-persistent { color: #374151; background: #f3f4f6; border-color: #d1d5db; }
        .chip-peaking { color: #7b3131; background: #f7e8e8; border-color: #e2bebe; }
        .chip-confirmed { color: #1f4f37; background: #e8f3ed; border-color: #bdd8c8; font-weight: 800; }
        .chip-early { color: #6b5a2e; background: #f6f0df; border-color: #ded0a8; }
        .sidebar-version {
            border-top: 1px solid #e2e8f0;
            margin-top: 1rem;
            padding-top: 0.75rem;
            color: #64748b;
            font-size: 0.78rem;
            line-height: 1.45;
        }
        @media (max-width: 760px) {
            .block-container { padding-left: 0.72rem; padding-right: 0.72rem; padding-top: 0.65rem; }
            h1 { font-size: 1.36rem !important; }
            h3 { font-size: 1rem !important; margin-top: 1rem !important; }
            .workstation-card, .pilot-panel { padding: 0.78rem 0.82rem; }
            .pilot-card { padding: 0.65rem 0.72rem; }
            .signal-title { font-size: 0.95rem; }
            .pilot-chip { white-space: normal; }
            div[data-testid="stExpander"] details summary { line-height: 1.35; overflow-wrap: anywhere; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def pilot_chip(text, kind="neutral"):
    safe = str(text or "").strip()
    if not safe:
        return ""
    class_name = {
        "expanding": "chip-expanding",
        "building": "chip-expanding",
        "accelerating": "chip-expanding",
        "weakening": "chip-weakening",
        "fading": "chip-weakening",
        "persistent": "chip-persistent",
        "stable": "chip-persistent",
        "peaking": "chip-peaking",
        "confirmed": "chip-confirmed",
        "broadly confirmed": "chip-confirmed",
        "early": "chip-early",
        "newly emerging": "chip-early",
        "source-concentrated": "chip-early",
    }.get(str(kind or "").lower(), "")
    return f"<span class='pilot-chip {class_name}'>{safe}</span>"


def render_pilot_chips(items):
    chips = [pilot_chip(text, kind) for text, kind in items if pilot_chip(text, kind)]
    if chips:
        st.markdown("<div class='pilot-row'>" + "".join(chips) + "</div>", unsafe_allow_html=True)


def render_section_header(title, subtitle=None):
    st.markdown("<div class='pilot-section'>", unsafe_allow_html=True)
    st.markdown(f"### {title}")
    if subtitle:
        st.markdown(f"<div class='pilot-muted'>{subtitle}</div>", unsafe_allow_html=True)


def close_section():
    st.markdown("</div>", unsafe_allow_html=True)


def clean_cluster_title(title):
    return {
        "Refinancing pressure unresolved": "refinancing 부담 지속 관찰",
        "Construction financing still selective": "construction financing 선별성 관찰",
        "LA entitlement precedent accumulation": "LA 인허가 precedent 누적 관찰",
        "Sun Belt lease-up pressure watch": "Sun Belt lease-up 부담 관찰",
        "JV / partnership activity observed": "JV / partnership activity 관찰",
    }.get(str(title or ""), str(title or "시장 시그널"))


def ko_regime_label(label):
    text = str(label or "")
    lowered = text.lower()
    if "capital" in lowered or "자본" in text:
        return "자본시장"
    if "development" in lowered or "개발" in text:
        return "개발 흐름"
    if "supply" in lowered or "공급" in text or "lease" in lowered:
        return "공급 / 임대시장"
    if "institutional" in lowered or "기관" in text or "jv" in lowered:
        return "기관 행동 흐름"
    return text or "시장 관찰"


def status_kind(value):
    text = str(value or "").lower()
    if text in {"expanding", "building", "accelerating"}:
        return "expanding"
    if text in {"weakening", "fading"}:
        return "weakening"
    if text == "peaking":
        return "peaking"
    if text in {"newly emerging", "early signal", "early"}:
        return "early"
    return "persistent"


def confidence_kind(value):
    text = str(value or "").lower()
    if "broadly" in text or "confirmed" in text:
        return "confirmed"
    if "source" in text or "early" in text:
        return "early"
    if "low" in text:
        return "weakening"
    return "persistent"


def render_woomi_market_checkpoints(shared, filters=None):
    render_section_header("우미 관점 체크포인트", "기사 관찰을 바로 투자 판단으로 연결하지 않고, 검증해야 할 시장 포인트만 압축합니다.")
    timeline = regime_timeline_map(shared)
    diagnostics = market_diagnostics_map(shared)
    bullets = []
    financing = timeline.get("Refinancing pressure unresolved", {})
    construction = timeline.get("Construction financing still selective", {})
    entitlement = timeline.get("LA entitlement precedent accumulation", {})
    supply = timeline.get("Sun Belt lease-up pressure watch", {})
    jv = timeline.get("JV / partnership activity observed", {})
    if financing or construction:
        label = financing.get("persistence_label", "관찰 지속")
        bullets.append(f"debt stress / recap 후보군은 단기 뉴스보다 구조적 pressure 가능성까지 열어두고 lender, sponsor, maturity profile 확인이 필요합니다. ({label})")
    if entitlement:
        confidence = diagnostics.get("LA entitlement precedent accumulation", {}).get("signal_confidence_label", "")
        if confidence == "Source-Concentrated":
            bullets.append("LA entitlement precedent는 참고 가치가 있으나 source 편중 가능성이 있어 planning docket 또는 별도 local source 검증이 필요합니다.")
        else:
            bullets.append("LA affordable entitlement precedent는 multifamily positioning과 인허가 비교사례 검토에 활용할 수 있습니다.")
    if supply:
        trend = supply.get("trend_direction", "stable")
        bullets.append(f"Sun Belt lease-up commentary는 {trend} 흐름으로 관찰됩니다. land entry 판단 전 absorption durability와 concession 추세 확인이 우선입니다.")
    if jv:
        bullets.append("JV / partnership 관찰은 관계 map 업데이트 관점에서 관리하되, 반복 확인 전까지 직접 투자기회로 보기는 이릅니다.")
    if not bullets:
        bullets.append("이번 run에서는 투자 판단 강도를 높일 만큼 반복 확인된 시장 cluster가 제한적입니다. 데이터 누적 후 판단 강도를 높이는 편이 적절합니다.")
    for bullet in bullets[:4]:
        st.markdown(f"- {bullet}")
    close_section()


def render_today_market_interpretation(shared, filters=None):
    render_section_header("오늘의 시장 해석", "개별 기사보다 여러 cluster가 함께 말하는 시장 국면을 요약합니다.")
    bullets = market_synthesis_bullets(shared)
    if not bullets:
        st.caption("이번 run에서는 여러 cluster를 묶어 해석할 만큼 충분한 교차 신호가 제한적입니다.")
    for bullet in bullets[:3]:
        st.markdown(f"- {bullet}")
    close_section()


def render_today_regime_changes(shared):
    timeline = shared.get("regime_timeline", pd.DataFrame())
    if timeline.empty:
        return
    trend_col = timeline["trend_direction"] if "trend_direction" in timeline.columns else pd.Series(dtype=str)
    persistence_col = timeline["persistence_label"] if "persistence_label" in timeline.columns else pd.Series(dtype=str)
    meaningful = timeline[trend_col.isin(["accelerating", "weakening", "re-emerging"]) | persistence_col.isin(["Peaking"])]
    if meaningful.empty:
        return
    render_section_header("오늘의 변화 감지")
    for _, row in meaningful.head(3).iterrows():
        st.markdown(f"- {row.get('regime_shift_signal', '의미 있는 변화가 관찰되었습니다.')}")
    close_section()


def render_market_regime_summary(shared, filters=None):
    render_section_header("Regime Snapshot", "이번 run에서 관찰된 cluster를 자본시장, 개발, 공급, 기관 행동 흐름으로 압축합니다.")
    clusters = market_signal_clusters(shared)
    if not clusters:
        st.caption("이번 run에서 충분한 반복 regime cluster가 포착되지 않았습니다.")
        close_section()
        return
    buckets = {}
    for cluster in clusters:
        buckets.setdefault(ko_regime_label(cluster.get("regime")), []).append(cluster)
    for heading in ["자본시장", "개발 흐름", "공급 / 임대시장", "기관 행동 흐름"]:
        items = buckets.get(heading, [])
        if not items:
            continue
        top = items[0]
        diagnostic = top.get("diagnostic", {})
        confidence = diagnostic.get("signal_confidence_label", "Early Signal")
        st.markdown(
            f"""
            <div class="pilot-card">
                <div class="section-kicker">{heading}</div>
                <div class="signal-title">{clean_cluster_title(top.get("title"))}</div>
                <div class="pilot-muted">{top.get("frequency", 0)}건 관찰 · {top.get("dominant_signal", "반복 관찰")}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        render_pilot_chips([
            (confidence, confidence_kind(confidence)),
            (top.get("status", "stable"), status_kind(top.get("status", "stable"))),
        ])
    close_section()


def render_homepage_hot_market(shared, filters=None):
    render_section_header("오늘의 Hot Market / 시장 집중도", "단순 기사 수가 아니라 거래성, GP/lender 다양성, source 반복 penalty를 함께 본 관찰입니다.")
    frames = [
        apply_filters(shared["cards"], filters),
        apply_filters(shared["opportunities"], filters),
        apply_filters(shared["high_confidence"], filters),
    ]
    score_by_market = {}
    signal_sets = {}
    source_counts = {}
    entity_sets = {}
    for frame in frames:
        if frame is None or frame.empty:
            continue
        for _, row in frame.iterrows():
            item = row.to_dict()
            market = str(item.get("market", "")).strip()
            if not market or market.lower() in {"other / unknown", "unknown", "other", "national"}:
                continue
            blob = text_blob(item)
            score = 1
            if any(term in blob for term in ["acquisition", "joint venture", " jv ", "construction financing", "recapitalization", "refinancing"]):
                score += 3
            if any(term in blob for term in ["lease-up", "concessions", "absorption"]):
                score += 1
            source = str(item.get("source", item.get("source_report", ""))).strip()
            source_key = (market, source)
            source_counts[source_key] = source_counts.get(source_key, 0) + 1
            if source_counts[source_key] > 1:
                score -= 1
            gp = str(item.get("gp_or_developer", item.get("canonical_gp_name", ""))).strip()
            lender = str(item.get("lender_or_capital_partner", item.get("firm_name", ""))).strip()
            entity_sets.setdefault(market, set()).update(value for value in [gp, lender] if value)
            signal_sets.setdefault(market, set()).update(
                label for label, terms in [
                    ("JV activity", ["joint venture", " jv ", "partnership"]),
                    ("construction financing", ["construction financing", "construction loan"]),
                    ("lease-up commentary", ["lease-up", "concessions", "absorption"]),
                    ("refinancing / recap", ["refinancing", "recapitalization", "recap"]),
                ]
                if any(term in blob for term in terms)
            )
            score_by_market[market] = score_by_market.get(market, 0) + max(score, 0)
    for market, entities in entity_sets.items():
        score_by_market[market] = score_by_market.get(market, 0) + min(len(entities), 3)
    if not score_by_market or max(score_by_market.values()) < 4:
        st.markdown("**시장 집중도 분산**")
        st.write("현재 기사 기준으로 특정 시장에 거래 및 자본 흐름이 뚜렷하게 집중된다고 보기는 어렵습니다.")
        st.caption("공개 인허가 데이터와 source별 기사 빈도 bias가 포함될 수 있어 후속 관찰이 필요합니다.")
        close_section()
        return
    top_market, _ = sorted(score_by_market.items(), key=lambda item: item[1], reverse=True)[0]
    st.markdown(f"**{top_market}**")
    reasons = sorted(signal_sets.get(top_market, set()))
    if reasons:
        st.write("선정 근거: " + ", ".join(reasons))
    st.caption("시장 집중도는 거래성, unique GP/lender, source 반복 penalty를 함께 반영한 관찰 지표입니다.")
    close_section()


def render_signal_clusters(shared, filters=None):
    render_section_header("Signal Cluster", "반복 기사 패턴을 confidence와 persistence 기준으로 압축해 보여줍니다.")
    clusters = market_signal_clusters(shared)
    if not clusters:
        st.caption("이번 run에서 반복 signal cluster가 충분히 포착되지 않았습니다.")
        close_section()
        return
    for cluster in clusters[:5]:
        diagnostic = cluster.get("diagnostic", {})
        timeline = cluster.get("timeline", regime_timeline_map(shared).get(cluster.get("title"), {}))
        confidence = diagnostic.get("signal_confidence_label", "Early Signal")
        persistence = timeline.get("persistence_label", "Newly Emerging")
        trend = timeline.get("trend_direction", cluster.get("status", "stable"))
        label = f"{clean_cluster_title(cluster.get('title'))} | {cluster.get('frequency', 0)}건 | {persistence} | {trend} | {confidence}"
        with st.expander(label, expanded=False):
            render_pilot_chips([
                (persistence, status_kind(persistence)),
                (trend, status_kind(trend)),
                (confidence, confidence_kind(confidence)),
            ])
            st.markdown("**Observed evidence**")
            for evidence in cluster.get("evidence", [])[:4]:
                st.markdown(f"- {evidence}")
            interpretation = cluster.get("interpretation", "")
            if interpretation:
                st.markdown(f"**Interpretation**  \n{interpretation}")
            market = diagnostic.get("dominant_market", "")
            financing = diagnostic.get("dominant_financing_patterns", "")
            if market:
                st.markdown(f"**Dominant market**  \n{market}")
            if financing:
                st.markdown(f"**Financing pattern**  \n{financing}")
            explanation = timeline.get("regime_shift_signal") or diagnostic.get("confidence_explanation") or "steady visibility"
            st.markdown(f"**Regime explanation**  \n{explanation}")
    close_section()


def render_development_pipeline_card(row, category):
    item = row.to_dict() if hasattr(row, "to_dict") else row
    title = get_title(item)
    sponsor = get_gp(item) or get_first(item, ["owner_or_sponsor"], "Sponsor not specified")
    stage = get_lifecycle_stage(item) or get_first(item, ["entitlement_stage", "execution_stage", "construction_status"], "Stage not specified")
    category_reason = get_first(item, ["primary_category_reason"], "")
    freshness = get_first(item, ["freshness_bucket", "freshness_status"], "")
    if str(freshness).strip().lower() in {"unknown_date", "nan", "none", "null"}:
        freshness = ""
    meta_parts = [development_market_label(item), development_source_label(item), stage]
    if freshness:
        meta_parts.append(str(freshness))
    headline = f"{title} | {' · '.join(meta_parts)}"
    with st.expander(headline, expanded=False):
        if sponsor:
            st.caption(f"GP / sponsor: {sponsor}")
        st.write(f"**Why it matters:** {get_reason(item)}")
        st.write(f"**Woomi angle:** {development_woomi_angle(item, category)}")
        st.write(f"**Lifecycle stage:** {stage}")
        if category_reason:
            st.write(f"**Category reason:** {category_reason}")
        url = get_url(item)
        if isinstance(url, str) and url.startswith("http"):
            st.markdown(f"[Read original article]({url})")


def page_development_status_product(shared, filters):
    st.title("최근 개발 Activity")
    render_development_activity_summary(shared)
    section_rows = dedupe_development_sections([
        ("construction", development_watch_rows(shared, "construction")),
        ("approval", development_watch_rows(shared, "approval")),
        ("site", development_watch_rows(shared, "site")),
    ])
    render_development_watch_section(
        "Construction / Delivery Watch",
        "construction start, lease-up, delivery, opening, absorption 등 실제 execution 흐름을 봅니다.",
        section_rows["construction"],
        "construction",
        limit=8,
    )
    render_development_watch_section(
        "인허가 / Approval Watch",
        "entitlement, zoning, density bonus, permit issuance, affordable overlay, CEQA, HUD review 관련 관찰입니다.",
        section_rows["approval"],
        "approval",
        limit=8,
    )
    render_development_watch_section(
        "Site / Parcel Activity",
        "site acquisition, land assemblage, parcel trade, redevelopment, sponsor entry 등 부지 진입 신호입니다.",
        section_rows["site"],
        "site",
        limit=8,
    )


def render_capital_event_cards(shared, filters=None):
    events = build_capital_events(shared)
    if not events:
        st.caption("현재 명확한 capital event가 충분히 포착되지 않았습니다.")
        return
    for event in events:
        entity = event["lead_sponsor"] or event["capital_provider"] or event["lender"] or "Entity not specified"
        headline = f"{entity} | {event['activity_type']} | {event['market']}"
        with st.expander(headline, expanded=False):
            render_pilot_chips([(capital_event_tag(event["activity_type"]), "confirmed")])
            if event["lead_sponsor"]:
                st.write(f"**Lead Sponsor:** {event['lead_sponsor']}")
            if event["capital_provider"]:
                st.write(f"**Capital Provider:** {event['capital_provider']}")
            if event["lender"]:
                st.write(f"**Lender:** {event['lender']}")
            if event["jv_partner"]:
                st.write(f"**JV Partner:** {event['jv_partner']}")
            st.write(f"**Related Market:** {event['market']}")
            st.write(f"**Related Article:** {event['event_title']}")
            if event["source"]:
                if event["url"]:
                    st.markdown(f"**Source:** [{event['source']}]({event['url']})")
                else:
                    st.write(f"**Source:** {event['source']}")
            if event["url"]:
                st.markdown(f"[원문 기사 보기]({event['url']})")


def page_gp_capital_product(shared, filters):
    st.title("GP / 자본 동향")
    st.markdown("### 기관 및 GP 자본 흐름")
    st.caption("미국 주거시장에서 관찰되는 sponsor, lender, institutional capital event를 압축해 보여줍니다.")
    render_capital_event_cards(shared, filters)
    with st.expander("Capital Network Map", expanded=False):
        render_capital_network_map(shared, filters)


def app_header(shared):
    st.markdown(
        """
        <div class="workstation-card">
            <div class="section-kicker">US Residential Intelligence</div>
            <div class="signal-title">우미글로벌 미국 주거시장 전략 브리핑</div>
            <div class="pilot-muted">시장 변화, 개발 Activity, GP 및 자본 흐름을 압축한 기관투자자형 모닝 브리프</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def legacy_main_18():
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()
    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)
    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])
    latest_run = summary.get("run_timestamp", "run timestamp unavailable")

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("우미글로벌 미국 주거시장 전략 브리핑")
    pages = {
        "오늘의 브리핑": page_executive_briefing,
        "시장 인텔리전스": page_market_intelligence_product,
        "최근 개발 Activity": page_development_status_product,
        "GP / 자본 동향": page_gp_capital_product,
        "기사 모음": page_article_feed,
        "시스템 / 설정": page_system_settings_product,
    }
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)
    st.sidebar.markdown(
        f"""
        <div class="sidebar-version">
            <strong>Pilot Version</strong><br>
            v0.1<br><br>
            최근 실행 시간<br>
            {latest_run}
        </div>
        """,
        unsafe_allow_html=True,
    )

    filters = {}
    app_header(shared)
    st.caption(f"최근 실행: {latest_run}")
    pages[page_name](shared, filters)
    st.divider()
    st.caption("US Residential Intelligence | Institutional Morning Brief | Pilot v0.1")


# ---------------------------------------------------------------------------
# Institutional morning desk homepage refinement
# ---------------------------------------------------------------------------

def inject_css():
    """Lightweight institutional UI polish for pilot review."""
    st.markdown(
        """
        <style>
        :root {
            --ink: #111827;
            --muted: #64748b;
            --line: #d7dde6;
            --panel: #ffffff;
        }
        .block-container { padding-top: 1.1rem; padding-bottom: 2.2rem; max-width: 1140px; }
        section[data-testid="stSidebar"] { width: 16.5rem !important; border-right: 1px solid #e2e8f0; }
        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { font-size: 0.86rem; line-height: 1.35; }
        h1 { font-size: 1.7rem !important; letter-spacing: 0; margin: 0.25rem 0 0.65rem 0 !important; color: var(--ink); }
        h2, h3 { letter-spacing: 0; color: var(--ink); }
        h3 { font-size: 1.08rem !important; margin-top: 1.3rem !important; margin-bottom: 0.55rem !important; }
        div[data-testid="stExpander"] {
            border: 1px solid #dbe2ea;
            border-radius: 7px;
            background: #ffffff;
            margin-bottom: 0.55rem;
        }
        div[data-testid="stExpander"] details summary { font-weight: 650; color: #1f2937; }
        .stDataFrame { border: 1px solid #e5e7eb; border-radius: 6px; overflow: hidden; }
        .workstation-card, .pilot-panel, .pilot-card, .desk-hero, .hot-market-card {
            border: 1px solid var(--line);
            border-radius: 7px;
            background: var(--panel);
            box-shadow: 0 1px 0 rgba(15, 23, 42, 0.03);
        }
        .workstation-card, .pilot-panel { padding: 0.95rem 1rem; margin: 1rem 0 0.9rem 0; }
        .workstation-card:first-of-type { margin-top: 1rem; padding: 1rem 1.05rem; }
        .pilot-card { padding: 0.72rem 0.85rem; margin: 0.55rem 0 0.75rem 0; }
        .pilot-section { border-top: 1px solid #dfe5ec; padding-top: 0.95rem; margin-top: 1.15rem; }
        .section-kicker {
            color: #475569;
            font-size: 0.73rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.04rem;
            margin-bottom: 0.15rem;
        }
        .signal-title {
            color: var(--ink);
            font-size: 1.02rem;
            font-weight: 760;
            line-height: 1.34;
            margin: 0.08rem 0 0.28rem 0;
            overflow-wrap: anywhere;
        }
        .muted-label, .pilot-muted { color: var(--muted); font-size: 0.83rem; line-height: 1.42; }
        .desk-hero {
            padding: 1.2rem 1.25rem;
            margin: 0.35rem 0 1.05rem 0;
            background: linear-gradient(180deg, #ffffff 0%, #f7f8fb 100%);
            border-left: 6px solid #172033;
        }
        .desk-hero-title {
            color: #0f172a;
            font-size: 1.82rem;
            font-weight: 820;
            line-height: 1.18;
            letter-spacing: 0;
            margin: 0.25rem 0 0.55rem 0;
        }
        .desk-hero-sub {
            color: #475569;
            font-size: 0.94rem;
            line-height: 1.45;
            margin-top: 0.3rem;
        }
        .hot-market-card {
            padding: 0.95rem 1rem;
            margin: 0.55rem 0 0.85rem 0;
            background: #fbfcfe;
        }
        .hot-market-name {
            font-size: 1.55rem;
            font-weight: 820;
            color: #111827;
            line-height: 1.18;
            margin: 0.15rem 0 0.3rem 0;
        }
        .pilot-row { display: flex; gap: 0.45rem; flex-wrap: wrap; align-items: center; margin: 0.35rem 0 0.2rem 0; }
        .pilot-chip {
            display: inline-block;
            border: 1px solid #cbd5e1;
            border-radius: 999px;
            padding: 0.12rem 0.45rem;
            margin: 0.06rem 0.14rem 0.06rem 0;
            background: #f8fafc;
            color: #334155;
            font-size: 0.74rem;
            font-weight: 720;
            line-height: 1.3;
            white-space: nowrap;
        }
        .chip-expanding { color: #7c5517; background: #fbf3df; border-color: #ead7aa; }
        .chip-weakening { color: #315b76; background: #e8f1f7; border-color: #c8dae7; }
        .chip-persistent { color: #374151; background: #f3f4f6; border-color: #d1d5db; }
        .chip-peaking { color: #7b3131; background: #f7e8e8; border-color: #e2bebe; }
        .chip-confirmed { color: #1f4f37; background: #e8f3ed; border-color: #bdd8c8; font-weight: 800; }
        .chip-early { color: #6b5a2e; background: #f6f0df; border-color: #ded0a8; }
        .sidebar-version {
            border-top: 1px solid #e2e8f0;
            margin-top: 1rem;
            padding-top: 0.75rem;
            color: #64748b;
            font-size: 0.78rem;
            line-height: 1.45;
        }
        @media (max-width: 760px) {
            .block-container { padding-left: 0.72rem; padding-right: 0.72rem; padding-top: 1.2rem; }
            h1 { font-size: 1.32rem !important; }
            h3 { font-size: 1rem !important; margin-top: 1rem !important; }
            .workstation-card, .pilot-panel, .desk-hero, .hot-market-card { padding: 0.86rem 0.88rem; }
            .workstation-card:first-of-type { margin-top: 1.75rem; padding: 0.95rem 0.9rem; }
            .pilot-card { padding: 0.65rem 0.72rem; }
            .signal-title { font-size: 0.95rem; }
            .desk-hero-title { font-size: 1.28rem; line-height: 1.23; }
            .hot-market-name { font-size: 1.18rem; }
            .pilot-chip { white-space: normal; }
            div[data-testid="stExpander"] details summary { line-height: 1.35; overflow-wrap: anywhere; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def get_primary_regime_phrase(shared):
    clusters = market_signal_clusters(shared)
    titles = {cluster.get("title") for cluster in clusters}
    if {"Refinancing pressure unresolved", "Construction financing still selective"} & titles:
        if "JV / partnership activity observed" in titles:
            return "선별적 자본 재개 + refinancing 압박 지속"
        return "refinancing 부담 지속 + construction capital 선별성"
    if "LA entitlement precedent accumulation" in titles:
        return "LA entitlement visibility 지속 + 정책 기반 개발 관찰"
    if "Sun Belt lease-up pressure watch" in titles:
        return "Sun Belt absorption 확인 필요"
    if clusters:
        return clean_cluster_title(clusters[0].get("title"))
    return "시장 집중도 분산 + 추가 관찰 필요"


def get_hero_support_lines(shared):
    clusters = market_signal_clusters(shared)
    parts = []
    for cluster in clusters[:4]:
        title = cluster.get("title")
        if title == "LA entitlement precedent accumulation":
            parts.append("LA entitlement 지속")
        elif title == "Sun Belt lease-up pressure watch":
            parts.append("Sun Belt absorption 확인 필요")
        elif title == "JV / partnership activity observed":
            parts.append("JV activity 제한적 증가")
        elif title == "Refinancing pressure unresolved":
            parts.append("refinancing 부담 관찰")
        elif title == "Construction financing still selective":
            parts.append("construction financing 선별성")
    return parts[:3] or ["반복 cluster 제한적", "source bias 검증 필요", "추가 run 확인 필요"]


def render_hero_market_view(shared):
    phrase = get_primary_regime_phrase(shared)
    support = " / ".join(get_hero_support_lines(shared))
    synthesis = market_synthesis_bullets(shared)
    synthesis_line = synthesis[0] if synthesis else "이번 run에서는 특정 시장 국면을 강하게 단정하기보다 반복 관찰과 source bias를 함께 확인하는 접근이 적절합니다."
    st.markdown(
        f"""
        <div class="desk-hero">
            <div class="section-kicker">Hero Market View</div>
            <div class="desk-hero-title">오늘 시장은<br>“{phrase}”<br>구간으로 해석됩니다.</div>
            <div class="desk-hero-sub">{support}</div>
            <div class="small-divider"></div>
            <div class="pilot-muted">{synthesis_line}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def compute_homepage_hot_market(shared, filters=None):
    frames = [
        apply_filters(shared["cards"], filters),
        apply_filters(shared["opportunities"], filters),
        apply_filters(shared["high_confidence"], filters),
    ]
    score_by_market = {}
    signal_sets = {}
    source_counts = {}
    entity_sets = {}
    for frame in frames:
        if frame is None or frame.empty:
            continue
        for _, row in frame.iterrows():
            item = row.to_dict()
            market = str(item.get("market", "")).strip()
            if not market or market.lower() in {"other / unknown", "unknown", "other", "national"}:
                continue
            blob = text_blob(item)
            score = 1
            if any(term in blob for term in ["acquisition", "joint venture", " jv ", "construction financing", "recapitalization", "refinancing"]):
                score += 3
            if any(term in blob for term in ["lease-up", "concessions", "absorption"]):
                score += 1
            source = str(item.get("source", item.get("source_report", ""))).strip()
            source_key = (market, source)
            source_counts[source_key] = source_counts.get(source_key, 0) + 1
            if source_counts[source_key] > 1:
                score -= 1
            gp = str(item.get("gp_or_developer", item.get("canonical_gp_name", ""))).strip()
            lender = str(item.get("lender_or_capital_partner", item.get("firm_name", ""))).strip()
            entity_sets.setdefault(market, set()).update(value for value in [gp, lender] if value)
            signal_sets.setdefault(market, set()).update(
                label for label, terms in [
                    ("JV activity", ["joint venture", " jv ", "partnership"]),
                    ("construction financing", ["construction financing", "construction loan"]),
                    ("lease-up commentary", ["lease-up", "concessions", "absorption"]),
                    ("refinancing / recap", ["refinancing", "recapitalization", "recap"]),
                ]
                if any(term in blob for term in terms)
            )
            score_by_market[market] = score_by_market.get(market, 0) + max(score, 0)
    for market, entities in entity_sets.items():
        score_by_market[market] = score_by_market.get(market, 0) + min(len(entities), 3)
    if not score_by_market or max(score_by_market.values()) < 4:
        return {
            "market": "시장 집중도 분산",
            "signals": ["거래 및 자본 흐름 집중도 제한적", "source / public-data bias 확인 필요"],
            "support": "현재 기사 기준으로 특정 시장에 거래 및 자본 흐름이 뚜렷하게 집중된다고 보기는 어렵습니다.",
        }
    market, _ = sorted(score_by_market.items(), key=lambda item: item[1], reverse=True)[0]
    signals = sorted(signal_sets.get(market, set())) or ["반복 관찰"]
    return {
        "market": market,
        "signals": signals,
        "support": "거래성, unique GP/lender, source 반복 penalty를 함께 반영한 관찰입니다.",
    }


def render_homepage_hot_market_card(shared, filters=None):
    render_section_header("TODAY'S HOT MARKET", "오늘 왜 이 시장이 중요했는지 먼저 보여줍니다.")
    hot = compute_homepage_hot_market(shared, filters)
    st.markdown(
        f"""
        <div class="hot-market-card">
            <div class="section-kicker">Market Focus</div>
            <div class="hot-market-name">{hot['market']}</div>
            <div class="pilot-muted">{' / '.join(hot['signals'][:4])}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption(hot["support"])
    close_section()


def render_homepage_key_market_signals(shared, filters=None):
    render_section_header("KEY MARKET SIGNALS", "브리핑에서는 핵심 3개 cluster만 먼저 노출합니다.")
    clusters = market_signal_clusters(shared)[:3]
    if not clusters:
        st.caption("이번 run에서 우선 노출할 market signal cluster가 제한적입니다.")
        close_section()
        return
    for index, cluster in enumerate(clusters, start=1):
        diagnostic = cluster.get("diagnostic", {})
        timeline = cluster.get("timeline", regime_timeline_map(shared).get(cluster.get("title"), {}))
        confidence = diagnostic.get("signal_confidence_label", "Early Signal")
        persistence = timeline.get("persistence_label", "Newly Emerging")
        trend = timeline.get("trend_direction", cluster.get("status", "stable"))
        title = clean_cluster_title(cluster.get("title"))
        with st.expander(f"[{index}] {title} | {cluster.get('frequency', 0)}건 | {persistence} | {confidence}", expanded=False):
            render_pilot_chips([
                (persistence, status_kind(persistence)),
                (trend, status_kind(trend)),
                (confidence, confidence_kind(confidence)),
            ])
            if cluster.get("dominant_signal"):
                st.write(f"**Dominant signals:** {cluster.get('dominant_signal')}")
            if cluster.get("interpretation"):
                st.write(cluster.get("interpretation"))
            market = diagnostic.get("dominant_market", "")
            if market:
                st.caption(f"Dominant market: {market}")
    with st.expander("전체 Signal Cluster 보기", expanded=False):
        render_signal_clusters(shared, filters)
    close_section()


def render_homepage_development_watch(shared, filters=None):
    render_section_header("DEVELOPMENT WATCH", "뉴스 목록이 아니라 pipeline 상태를 approval, delivery, site-control 관점에서 압축합니다.")
    approval = development_watch_rows(shared, "approval")
    construction = development_watch_rows(shared, "construction")
    site = development_watch_rows(shared, "site")
    approval_la = approval["_dev_blob"].str.contains("los angeles|california|density bonus|affordable", regex=True).sum() if not approval.empty else 0
    construction_sunbelt = construction["_dev_blob"].str.contains("sun belt|texas|florida|phoenix|atlanta|nashville|charlotte|lease-up|delivery|opening", regex=True).sum() if not construction.empty else 0
    site_count = len(site)
    cards = [
        ("ENTITLEMENT WATCH", f"LA / California affordable entitlement 사례가 {int(approval_la)}건 수준으로 관찰됩니다. 실제 공급 급증보다 approval precedent 축적 여부를 확인하는 용도입니다."),
        ("DELIVERY / LEASE-UP WATCH", f"Construction / delivery 관련 관찰은 {len(construction)}건입니다. Sun Belt lease-up 또는 absorption 문맥은 underwriting check로 연결됩니다."),
        ("SITE / PARCEL ACTIVITY", f"Site / parcel 관찰은 {site_count}건입니다. land entry, assemblage, sponsor entry가 반복되는지 후속 run에서 확인이 필요합니다."),
    ]
    for title, body in cards:
        st.markdown(
            f"""
            <div class="pilot-card">
                <div class="section-kicker">{title}</div>
                <div class="pilot-muted">{body}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    close_section()


def render_homepage_capital_flow_watch(shared, filters=None):
    render_section_header("Institutional Capital Watch", "기사보다 capital behavior를 먼저 읽기 위한 요약입니다.")
    events = build_capital_events(shared)
    activity_counts = {}
    sponsor_counts = {}
    lender_counts = {}
    for event in events:
        activity = event.get("activity_type", "Unknown")
        activity_counts[activity] = activity_counts.get(activity, 0) + 1
        sponsor = event.get("lead_sponsor") or event.get("capital_provider")
        lender = event.get("lender")
        if sponsor:
            sponsor_counts[sponsor] = sponsor_counts.get(sponsor, 0) + 1
        if lender:
            lender_counts[lender] = lender_counts.get(lender, 0) + 1
    top_activity = sorted(activity_counts.items(), key=lambda item: item[1], reverse=True)[:3]
    if top_activity:
        render_pilot_chips([(f"{name}: {count}", "confirmed") for name, count in top_activity])
    bullets = []
    if activity_counts.get("Refinancing", 0):
        bullets.append(f"Refinancing / recap 관련 capital event가 {activity_counts.get('Refinancing', 0)}건 관찰되어 debt market selectivity 확인이 필요합니다.")
    if activity_counts.get("JV / Partnership", 0):
        bullets.append(f"JV / partnership event가 {activity_counts.get('JV / Partnership', 0)}건 관찰됩니다. 관계 후보로 관리하되 반복 확인이 우선입니다.")
    if activity_counts.get("Construction Financing", 0):
        bullets.append(f"Construction financing event가 {activity_counts.get('Construction Financing', 0)}건 관찰되어 lender appetite의 선별성을 확인할 필요가 있습니다.")
    if sponsor_counts:
        sponsor = sorted(sponsor_counts.items(), key=lambda item: item[1], reverse=True)[0][0]
        bullets.append(f"반복 sponsor 관찰: {sponsor}")
    if lender_counts:
        lender = sorted(lender_counts.items(), key=lambda item: item[1], reverse=True)[0][0]
        bullets.append(f"반복 lender 관찰: {lender}")
    if not bullets:
        bullets.append("이번 run에서는 강한 capital behavior cluster보다 약한 entity mention이 더 많아 보수적으로 관찰하는 편이 적절합니다.")
    for bullet in bullets[:5]:
        st.markdown(f"- {bullet}")
    close_section()


def page_executive_briefing(shared, filters):
    st.title("오늘의 브리핑")
    render_hero_market_view(shared)
    render_homepage_hot_market_card(shared, filters)
    render_homepage_key_market_signals(shared, filters)
    render_homepage_development_watch(shared, filters)
    render_homepage_capital_flow_watch(shared, filters)
    with st.expander("시장 해석 상세", expanded=False):
        render_woomi_market_checkpoints(shared, filters)
        render_today_market_interpretation(shared, filters)
        render_market_regime_summary(shared, filters)


def is_admin_mode():
    """Hidden admin utility gate. Can later be replaced with password logic."""
    try:
        return bool(st.secrets.get("admin_mode", False))
    except Exception:
        return False


def inject_css():
    """Lightweight institutional UI polish for pilot review."""
    st.markdown(
        """
        <style>
        :root {
            --ink: #111827;
            --muted: #64748b;
            --line: #d7dde6;
            --panel: #ffffff;
        }
        .block-container { padding-top: 1.1rem; padding-bottom: 2.2rem; max-width: 1140px; }
        section[data-testid="stSidebar"] { width: 16.5rem !important; border-right: 1px solid #e2e8f0; }
        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { font-size: 0.86rem; line-height: 1.35; }
        h1 { font-size: 1.7rem !important; letter-spacing: 0; margin: 0.25rem 0 0.65rem 0 !important; color: var(--ink); }
        h2, h3 { letter-spacing: 0; color: var(--ink); }
        h3 { font-size: 1.08rem !important; margin-top: 1.3rem !important; margin-bottom: 0.55rem !important; }
        div[data-testid="stExpander"] {
            border: 1px solid #dbe2ea;
            border-radius: 7px;
            background: #ffffff;
            margin-bottom: 0.55rem;
        }
        div[data-testid="stExpander"] details summary { font-weight: 650; color: #1f2937; }
        .stDataFrame { border: 1px solid #e5e7eb; border-radius: 6px; overflow: hidden; }
        .workstation-card, .pilot-panel, .pilot-card, .desk-hero, .hot-market-card {
            border: 1px solid var(--line);
            border-radius: 7px;
            background: var(--panel);
            box-shadow: 0 1px 0 rgba(15, 23, 42, 0.03);
        }
        .workstation-card, .pilot-panel { padding: 0.95rem 1rem; margin: 1rem 0 0.9rem 0; }
        .workstation-card:first-of-type { margin-top: 1rem; padding: 1rem 1.05rem; }
        .pilot-card { padding: 0.72rem 0.85rem; margin: 0.55rem 0 0.75rem 0; }
        .pilot-section { border-top: 1px solid #dfe5ec; padding-top: 0.95rem; margin-top: 1.15rem; }
        .section-kicker {
            color: #475569;
            font-size: 0.73rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.04rem;
            margin-bottom: 0.15rem;
        }
        .signal-title {
            color: var(--ink);
            font-size: 1.02rem;
            font-weight: 760;
            line-height: 1.34;
            margin: 0.08rem 0 0.28rem 0;
            overflow-wrap: anywhere;
        }
        .muted-label, .pilot-muted { color: var(--muted); font-size: 0.83rem; line-height: 1.42; }
        .header-title-line {
            display: block;
            color: var(--ink);
            font-size: 1.02rem;
            font-weight: 760;
            line-height: 1.28;
            margin: 0.04rem 0;
        }
        .desk-hero {
            padding: 1.2rem 1.25rem;
            margin: 0.35rem 0 1.05rem 0;
            background: linear-gradient(180deg, #ffffff 0%, #f7f8fb 100%);
            border-left: 6px solid #172033;
        }
        .desk-hero-title {
            color: #0f172a;
            font-size: 1.74rem;
            font-weight: 820;
            line-height: 1.22;
            letter-spacing: 0;
            margin: 0.25rem 0 0.55rem 0;
        }
        .desk-hero-sub {
            color: #475569;
            font-size: 0.95rem;
            line-height: 1.48;
            margin-top: 0.3rem;
            max-width: 820px;
        }
        .hot-market-card {
            padding: 0.95rem 1rem;
            margin: 0.55rem 0 0.85rem 0;
            background: #fbfcfe;
        }
        .hot-market-name {
            font-size: 1.55rem;
            font-weight: 820;
            color: #111827;
            line-height: 1.18;
            margin: 0.15rem 0 0.3rem 0;
        }
        .pilot-row { display: flex; gap: 0.45rem; flex-wrap: wrap; align-items: center; margin: 0.35rem 0 0.2rem 0; }
        .pilot-chip {
            display: inline-block;
            border: 1px solid #cbd5e1;
            border-radius: 999px;
            padding: 0.12rem 0.45rem;
            margin: 0.06rem 0.14rem 0.06rem 0;
            background: #f8fafc;
            color: #334155;
            font-size: 0.74rem;
            font-weight: 720;
            line-height: 1.3;
            white-space: nowrap;
        }
        .chip-expanding { color: #7c5517; background: #fbf3df; border-color: #ead7aa; }
        .chip-weakening { color: #315b76; background: #e8f1f7; border-color: #c8dae7; }
        .chip-persistent { color: #374151; background: #f3f4f6; border-color: #d1d5db; }
        .chip-peaking { color: #7b3131; background: #f7e8e8; border-color: #e2bebe; }
        .chip-confirmed { color: #1f4f37; background: #e8f3ed; border-color: #bdd8c8; font-weight: 800; }
        .chip-early { color: #6b5a2e; background: #f6f0df; border-color: #ded0a8; }
        .sidebar-version {
            border-top: 1px solid #e2e8f0;
            margin-top: 1rem;
            padding-top: 0.75rem;
            color: #64748b;
            font-size: 0.78rem;
            line-height: 1.45;
        }
        @media (max-width: 760px) {
            .block-container { padding-left: 0.72rem; padding-right: 0.72rem; padding-top: 1.2rem; }
            h1 { font-size: 1.32rem !important; }
            h3 { font-size: 1rem !important; margin-top: 1rem !important; }
            .workstation-card, .pilot-panel, .desk-hero, .hot-market-card { padding: 0.86rem 0.88rem; }
            .workstation-card:first-of-type { margin-top: 1.75rem; padding: 0.95rem 0.9rem; }
            .pilot-card { padding: 0.65rem 0.72rem; }
            .signal-title, .header-title-line { font-size: 0.96rem; }
            .desk-hero-title { font-size: 1.22rem; line-height: 1.26; }
            .desk-hero-sub { font-size: 0.88rem; }
            .hot-market-name { font-size: 1.18rem; }
            .pilot-chip { white-space: normal; }
            div[data-testid="stExpander"] details summary { line-height: 1.35; overflow-wrap: anywhere; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def app_header(shared):
    st.markdown(
        """
        <div class="workstation-card">
            <div class="section-kicker">US Residential Intelligence</div>
            <span class="header-title-line">우미글로벌</span>
            <span class="header-title-line">미국 주거시장 전략 브리핑</span>
            <div class="pilot-muted">시장 국면, 개발 Activity, GP 및 자본 흐름을 압축한 기관투자자형 모닝 브리프</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def get_primary_regime_phrase(shared):
    clusters = market_signal_clusters(shared)
    titles = {cluster.get("title") for cluster in clusters}
    if {"Refinancing pressure unresolved", "Construction financing still selective"} & titles:
        if "JV / partnership activity observed" in titles:
            return "선별적 투자 재개와 refinancing 부담 공존 국면"
        return "자금 집행은 선별적으로 재개되지만 debt 부담은 여전한 국면"
    if "LA entitlement precedent accumulation" in titles:
        return "LA 인허가 precedent가 누적되는 정책 기반 개발 관찰 국면"
    if "Sun Belt lease-up pressure watch" in titles:
        return "Sun Belt 공급 소화와 absorption 확인이 필요한 국면"
    if clusters:
        return cluster_institutional_sentence(clusters[0])
    return "시장 집중도는 분산되어 있고 추가 관찰이 필요한 국면"


def get_hero_support_sentence(shared):
    clusters = market_signal_clusters(shared)
    titles = {cluster.get("title") for cluster in clusters}
    sentences = []
    if "LA entitlement precedent accumulation" in titles:
        sentences.append("LA entitlement activity는 지속 관찰됩니다")
    if "JV / partnership activity observed" in titles:
        sentences.append("JV 논의는 일부 재개 조짐을 보입니다")
    if "Refinancing pressure unresolved" in titles or "Construction financing still selective" in titles:
        sentences.append("refinancing 부담은 여전히 주요 변수로 남아 있습니다")
    if "Sun Belt lease-up pressure watch" in titles:
        sentences.append("Sun Belt는 absorption durability 확인이 필요합니다")
    if not sentences:
        return "이번 run에서는 특정 market regime을 강하게 단정하기보다 반복 관찰과 source bias를 함께 확인하는 접근이 적절합니다."
    return ". ".join(sentences[:3]) + "."


def cluster_institutional_sentence(cluster):
    title = cluster.get("title") if isinstance(cluster, dict) else str(cluster or "")
    diagnostic = cluster.get("diagnostic", {}) if isinstance(cluster, dict) else {}
    confidence = diagnostic.get("signal_confidence_label", "")
    if title == "Refinancing pressure unresolved":
        if confidence == "Broadly Confirmed":
            return "차환 및 recap 수요가 여러 source에서 반복 관찰되며 debt 부담이 완화되지 않고 있습니다."
        return "refinancing 관련 관찰은 이어지지만 broad market stress로 단정하기 전 추가 확인이 필요합니다."
    if title == "Construction financing still selective":
        return "자금은 일부 공급되지만 lender underwriting은 여전히 선별적으로 작동하고 있습니다."
    if title == "LA entitlement precedent accumulation":
        if confidence == "Source-Concentrated":
            return "LA 인허가 보도는 계속 관찰되지만 source 집중도가 높아 실제 시장 가속으로 일반화하기는 어렵습니다."
        return "LA affordable entitlement precedent가 누적되며 향후 multifamily positioning 참고사례가 늘고 있습니다."
    if title == "Sun Belt lease-up pressure watch":
        return "Sun Belt는 신규 공급 소화와 lease-up 속도 확인이 underwriting의 핵심 변수로 남아 있습니다."
    if title == "JV / partnership activity observed":
        return "JV 및 partnership 신호는 일부 재개되고 있으나 반복 확인 전까지는 관계 mapping 관점에서 관리하는 것이 적절합니다."
    return clean_cluster_title(title)


def render_hero_market_view(shared):
    phrase = get_primary_regime_phrase(shared)
    support = get_hero_support_sentence(shared)
    synthesis = market_synthesis_bullets(shared)
    synthesis_line = synthesis[0] if synthesis else "현재는 단일 기사보다 반복 cluster와 source breadth를 함께 확인해야 하는 관찰 국면입니다."
    st.markdown(
        f"""
        <div class="desk-hero">
            <div class="section-kicker">Hero Market View</div>
            <div class="desk-hero-title">오늘 시장은<br>“{phrase}”<br>으로 해석됩니다.</div>
            <div class="desk-hero-sub">{support}</div>
            <div class="small-divider"></div>
            <div class="pilot-muted">{synthesis_line}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_homepage_key_market_signals(shared, filters=None):
    render_section_header("KEY MARKET SIGNALS", "브리핑에서는 핵심 3개 cluster만 먼저 노출합니다.")
    clusters = market_signal_clusters(shared)[:3]
    if not clusters:
        st.caption("이번 run에서 우선 노출할 market signal cluster가 제한적입니다.")
        close_section()
        return
    for index, cluster in enumerate(clusters, start=1):
        diagnostic = cluster.get("diagnostic", {})
        timeline = cluster.get("timeline", regime_timeline_map(shared).get(cluster.get("title"), {}))
        confidence = diagnostic.get("signal_confidence_label", "Early Signal")
        persistence = timeline.get("persistence_label", "Newly Emerging")
        trend = timeline.get("trend_direction", cluster.get("status", "stable"))
        title = clean_cluster_title(cluster.get("title"))
        with st.expander(f"[{index}] {title} | {cluster.get('frequency', 0)}건 | {persistence} | {confidence}", expanded=False):
            render_pilot_chips([
                (persistence, status_kind(persistence)),
                (trend, status_kind(trend)),
                (confidence, confidence_kind(confidence)),
            ])
            st.write(cluster_institutional_sentence(cluster))
            if cluster.get("dominant_signal"):
                st.caption(f"Dominant signals: {cluster.get('dominant_signal')}")
            market = diagnostic.get("dominant_market", "")
            if market:
                st.caption(f"Dominant market: {market}")
    with st.expander("전체 Signal Cluster 보기", expanded=False):
        render_signal_clusters(shared, filters)
    close_section()


def legacy_main_19():
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()
    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)
    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])
    latest_run = summary.get("run_timestamp", "run timestamp unavailable")

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("우미글로벌 미국 주거시장 전략 브리핑")
    pages = {
        "오늘의 브리핑": page_executive_briefing,
        "시장 인텔리전스": page_market_intelligence_product,
        "최근 개발 Activity": page_development_status_product,
        "GP / 자본 동향": page_gp_capital_product,
        "기사 모음": page_article_feed,
    }
    if is_admin_mode():
        pages["시스템 / 설정"] = page_system_settings_product
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)
    st.sidebar.markdown(
        f"""
        <div class="sidebar-version">
            <strong>Pilot Version</strong><br>
            v0.1<br><br>
            최근 실행 시간<br>
            {latest_run}
        </div>
        """,
        unsafe_allow_html=True,
    )

    filters = {}
    app_header(shared)
    st.caption(f"최근 실행: {latest_run}")
    pages[page_name](shared, filters)
    st.divider()
    st.caption("US Residential Intelligence | Institutional Morning Brief | Pilot v0.1")


def render_sidebar_subtitle():
    """Keep the Korean sidebar subtitle on two intentional lines."""
    st.sidebar.markdown(
        """
        <div style="line-height:1.35; color:#64748b; font-size:0.86rem; margin-top:-0.35rem; margin-bottom:0.75rem;">
            <div>우미글로벌</div>
            <div>미국 주거시장 전략 브리핑</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def legacy_main_20():
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()
    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)
    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])
    latest_run = summary.get("run_timestamp", "run timestamp unavailable")

    st.sidebar.title("US Residential Intelligence")
    render_sidebar_subtitle()
    pages = {
        "오늘의 브리핑": page_executive_briefing,
        "시장 인텔리전스": page_market_intelligence_product,
        "최근 개발 Activity": page_development_status_product,
        "GP / 자본 동향": page_gp_capital_product,
        "기사 모음": page_article_feed,
    }
    if is_admin_mode():
        pages["시스템 / 설정"] = page_system_settings_product
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)
    st.sidebar.markdown(
        f"""
        <div class="sidebar-version">
            <strong>Pilot Version</strong><br>
            v0.1<br><br>
            최근 실행 시간<br>
            {latest_run}
        </div>
        """,
        unsafe_allow_html=True,
    )

    filters = {}
    app_header(shared)
    st.caption(f"최근 실행: {latest_run}")
    pages[page_name](shared, filters)
    st.divider()
    st.caption("US Residential Intelligence | Institutional Morning Brief | Pilot v0.1")


def render_sidebar_subtitle():
    """Keep the Korean sidebar subtitle on two intentional lines."""
    st.sidebar.markdown(
        """
        <div style="line-height:1.35; color:#64748b; font-size:0.86rem; margin-top:-0.35rem; margin-bottom:0.75rem;">
            <div>우미글로벌</div>
            <div>미국 주거시장 전략 브리핑</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_executive_briefing(shared, filters):
    st.title("오늘의 브리핑")
    render_hero_market_view(shared)
    render_homepage_hot_market_card(shared, filters)
    render_homepage_key_market_signals(shared, filters)
    render_homepage_development_watch(shared, filters)
    render_homepage_capital_flow_watch(shared, filters)
    with st.expander("시장 해석 상세", expanded=False):
        render_woomi_market_checkpoints(shared, filters)
        render_today_market_interpretation(shared, filters)
        render_market_regime_summary(shared, filters)


# ACTIVE MAIN - 실제 실행 진입점
#
# Page routing used by the active Streamlit entry point:
# - 오늘의 브리핑 -> page_executive_briefing
# - 시장 인텔리전스 -> page_market_intelligence_product
# - 최근 개발 Activity -> page_development_status_product
# - GP / 자본 동향 -> page_gp_capital_product
# - 기사 모음 -> page_article_feed
#
# Earlier main variants are intentionally preserved as legacy_main_XX so that
# historical page/render logic remains available while this final entry point
# stays unambiguous.
def legacy_main_21():
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()
    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)
    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])
    latest_run = summary.get("run_timestamp", "run timestamp unavailable")

    st.sidebar.title("US Residential Intelligence")
    render_sidebar_subtitle()
    pages = {
        "오늘의 브리핑": page_executive_briefing,
        "시장 인텔리전스": page_market_intelligence_product,
        "최근 개발 Activity": page_development_status_product,
        "GP / 자본 동향": page_gp_capital_product,
        "기사 모음": page_article_feed,
    }
    if is_admin_mode():
        pages["시스템 / 설정"] = page_system_settings_product
    page_name = st.sidebar.radio("페이지", list(pages.keys()), index=0)
    st.sidebar.markdown(
        f"""
        <div class="sidebar-version">
            <strong>Pilot Version</strong><br>
            v0.1<br><br>
            최근 실행 시간<br>
            {latest_run}
        </div>
        """,
        unsafe_allow_html=True,
    )

    filters = {}
    app_header(shared)
    st.caption(f"최근 실행: {latest_run}")
    pages[page_name](shared, filters)
    st.divider()
    st.caption("US Residential Intelligence | Institutional Morning Brief | Pilot v0.1")


# ACTIVE MAIN - Article Feed phase navigation
def main():
    st.set_page_config(
        page_title="US Residential Intelligence",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()
    if not OUTPUT_DIR.exists():
        st.warning(CLOUD_MISSING_MESSAGE)
    shared = load_shared_data()
    st.session_state["shared_data"] = shared
    summary = latest_summary(shared["summary"])
    latest_run = summary.get("run_timestamp", "run timestamp unavailable")

    st.sidebar.title("US Residential Intelligence")
    st.sidebar.caption("US residential news archive")
    pages = {
        "Market Dashboard": page_market_dashboard,
        "Article Feed": page_article_feed,
    }
    try:
        query_page = st.query_params.get("page")
        query_category = st.query_params.get("category")
    except Exception:
        query_page = None
        query_category = None
    if query_page in pages and "app_page" not in st.session_state:
        st.session_state["app_page"] = query_page
    if (
        query_category in ARTICLE_FEED_DISPLAY_CATEGORIES
        and st.session_state.get("article_feed_applied_query_category") != query_category
    ):
        st.session_state["article_feed_pending_category"] = query_category
        st.session_state["article_feed_applied_query_category"] = query_category
    page_name = st.sidebar.radio("Page", list(pages.keys()), index=0, key="app_page")
    st.sidebar.markdown(
        f"""
        <div class="sidebar-version">
            <strong>Pilot Version</strong><br>
            v0.1<br><br>
            Latest run<br>
            {latest_run}
        </div>
        """,
        unsafe_allow_html=True,
    )

    filters = {}
    app_header(shared)
    st.caption(f"Latest run: {latest_run}")
    pages[page_name](shared, filters)
    st.divider()
    st.caption("US Residential Intelligence | News Archive Dashboard | Pilot v0.1")


if __name__ == "__main__":
    main()
