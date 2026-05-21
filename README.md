# US Multifamily Research MVP

This is an early-stage strategic research tool for US multifamily housing development.

The current MVP collects RSS articles, filters for multifamily relevance, scores each article, and exports a CSV file.

## What To Open First

For normal executive review, start here:

1. `output/executive_dashboard_brief.md`
2. `output/run_summary.md`
3. `output/high_confidence_watchlist_report.md`
4. `output/opportunity_radar_report.md`
5. `output/pipeline_health_report.md`

For maintenance or troubleshooting, start here:

1. `output/pipeline_health_report.md`
2. `output/pipeline_manifest.md`
3. `output/error_log.csv`
4. `output/source_health_report.md`

## Current Features

- RSS news collection
- Multifamily-focused filtering
- Article relevance scoring from 0 to 100
- Minimum relevance threshold
- Priority labels
- Daily briefing action levels
- Market focus detection
- Strategic angle labels
- Decision-use labels
- Plain-English inclusion reasons
- Basic article page fetching
- Numeric market signal extraction
- Market signal CSV export
- Rule-based strategic implications
- Woomi relevance labels
- Recommended next steps
- Strategy briefing CSV export
- Human-readable daily Markdown briefing
- Weekly strategy memo in Markdown
- LLM-ready prompt generation without API calls
- LLM prompt quality scoring
- Optional OpenAI GPT analysis mode
- Dated output folders
- Run log history
- Trend detection and change monitoring
- Thematic trend intelligence
- Narrative regime detection
- Regime transition tracking across multiple runs
- Regime heatmap scoring
- Regime score calibration and momentum detection
- Narrative severity and conviction scoring
- Materiality and business impact assessment
- Executive prioritization engine
- Base / Bull / Bear scenario planning
- Regional and city intelligence
- Developer / GP intelligence
- Institutional relationship and capital-flow intelligence
- Institutional source expansion and source health reporting
- Deal and project pipeline extraction
- Developer network and relationship graph intelligence
- Entity resolution and canonicalization
- Residential sector coverage
- Strategic topic classification
- Executive dashboard data files for a future web app
- Korean executive reports using rule-based localization
- Pipeline manifest and health checks
- Error logging and beginner-friendly run summary
- Full, high-priority, market-signal, and strategy briefing CSV export

## Current Folder Structure

```text
us_resi_research_mvp/
  news_collector.py
  app.py
  DEPLOYMENT.md
  requirements.txt
  README.md
  output/
    articles.csv
    executive_dashboard_brief.md
    run_summary.md
    pipeline_manifest.csv
    pipeline_manifest.md
    pipeline_health.csv
    pipeline_health_report.md
    error_log.csv
    runs/
      YYYY-MM-DD/
        archived copies of the latest output files
```

The files directly under `output/` are the latest run. The files under `output/runs/YYYY-MM-DD/` are archived copies for historical comparison.

## Streamlit Cloud Pilot Deployment

The pilot deployment uses Streamlit Cloud for the app and GitHub Actions for the daily data refresh.

The Streamlit app does **not** run `news_collector.py` on every user page load. Instead:

1. GitHub Actions runs `python news_collector.py` once every morning.
2. Updated files under `output/` are committed back to GitHub.
3. Streamlit Cloud reads the latest committed output files.
4. Team members open the Streamlit URL to review the latest daily briefing.

Workflow file:

```text
.github/workflows/daily_news_collector.yml
```

Schedule:

- 8:00 AM Korea time
- 23:00 UTC on the previous day

Local run:

```bash
python news_collector.py
python -m streamlit run app.py
```

Streamlit Cloud setup:

1. Push the repository to GitHub.
2. Go to Streamlit Community Cloud.
3. Create a new app from the GitHub repository.
4. Set **Main file path** to `app.py`.
5. Deploy.
6. Share the Streamlit app URL with the team.

Manual refresh:

1. Go to GitHub Actions.
2. Select `Daily News Collector`.
3. Click `Run workflow`.

Output management:

- Latest app-facing files stay in `output/`.
- Dated snapshots are saved in `output/runs/YYYY-MM-DD/`.
- Each dated run folder includes `run_manifest.json`.
- Major CSVs include `run_id` and `run_date`.
- `regime_history.csv` and `regime_timeline.csv` append run-level memory over time.

Pilot navigation:

1. `오늘의 브리핑`
2. `시장 인텔리전스`
3. `최근 개발 Activity`
4. `GP / 자본 동향`
5. `기사 모음`

The hidden `시스템 / 설정` page appears only when `admin_mode = true` is set in Streamlit secrets.

## Web App Dashboard

This project now includes a Streamlit web app:

```bash
python -m streamlit run app.py
```

The app is designed as a mobile-friendly executive intelligence briefing, not just a CSV viewer.

Recommended app reading order:

1. `한국어 경영진 브리핑`
2. `경영진 대시보드`
3. `고신뢰 신호`
4. `기회 / 리스크 레이더`
5. `LA 자산 Watch`
6. `GP Watchlist`
7. `파이프라인 상태`

## Refresh Data

The Streamlit app only reads files from `output/`. It does not collect news by itself.

To refresh the dashboard data:

```bash
python news_collector.py
```

Then reopen or refresh the Streamlit app.

## Streamlit Cloud Deployment

See `DEPLOYMENT.md` for beginner-friendly deployment steps.

Short version:

1. Push the repository to GitHub.
2. Open Streamlit Community Cloud.
3. Connect GitHub.
4. Select this repository.
5. Set the main file path to `app.py`.
6. Deploy.

## Mobile Usage

The Streamlit app uses compact metrics, narrative cards, collapsed tables, and expandable details so it is easier to review on a phone.

Open the deployed app URL in a mobile browser. You can add the app to your phone home screen for faster access.

## Web App Limitations

- The app reads generated files from `output/`.
- If `output/` files are missing on Streamlit Cloud, the app shows missing-file warnings instead of failing.
- For now, refresh data locally with `python news_collector.py`.
- If you want Streamlit Cloud to show the latest data, commit or upload the refreshed `output/` files.
- The app does not use paid APIs, authentication, or a database.

## Daily Operational Web App

The Streamlit app is now designed for daily operational usage.

Main pages:

- `한국어 경영진 브리핑`: daily Korean executive briefing and top signal drill-down
- `경영진 대시보드`: executive snapshot, market pulse, opportunity, distress, LA, and GP views
- `고신뢰 신호`: quality-filtered institutional signals
- `기회 / 리스크 레이더`: opportunity, refinancing, distress, and recapitalization signals
- `LA 자산 Watch`: LA / California asset, entitlement, lifecycle, and persistent memory watch
- `GP Watchlist`: developer / GP, institutional relationship, and relationship graph intelligence
- `System Health / Pipeline Status`: output availability, warnings, latest run status, and downloads
- `Daily Workflow`: recommended daily operating sequence
- `Deployment Checklist`: Streamlit Cloud deployment readiness checks

## Streamlit Cloud Readiness

Deployment support files:

- `requirements.txt`: Python packages for Streamlit Cloud
- `runtime.txt`: Python runtime hint
- `.streamlit/config.toml`: Streamlit theme and server settings
- `.gitignore`: ignores caches and local secrets while keeping current `output/*.csv` and `output/*.md`
- `DEPLOYMENT.md`: full deployment and troubleshooting guide

The app uses only relative paths such as `output/dashboard_cards.csv`, so it can run locally and on Streamlit Cloud.

## Cloud Update Workflow

Streamlit Cloud does not automatically refresh RSS data in this MVP.

Recommended workflow:

1. Run `python news_collector.py` locally.
2. Review the local Streamlit app with `python -m streamlit run app.py`.
3. Commit and push updated `output/*.csv` and `output/*.md` files.
4. Streamlit Cloud will show the updated intelligence files after redeploy or refresh.

## Mobile Access

The app uses compact KPI cards, expanded sidebar navigation, collapsed raw tables, and expandable signal drill-downs to support phone usage.

Open the deployed Streamlit URL on a phone browser. Add it to the home screen if it becomes part of the daily workflow.

## Troubleshooting the Web App

- Missing files: run `python news_collector.py` and confirm `output/` files exist.
- Empty dashboard: confirm `output/dashboard_summary.csv` and `output/dashboard_cards.csv` exist.
- Cloud app lacks current data: commit and push updated `output/*.csv` and `output/*.md`.
- Dependency failure: confirm `requirements.txt` includes `streamlit` and `pandas`.
- Korean text issues: keep files encoded as UTF-8.

## Install Packages

This project uses:

- `streamlit`
- `pandas`
- `feedparser`
- `requests`
- `beautifulsoup4`

Install them with:

```bash
pip install -r requirements.txt
```

The `openai` package is only needed if GPT mode is enabled:

```bash
pip install openai
```

## Why Filtering Was Improved

The first version used broad keyword matching. That allowed too many general policy articles into the CSV, especially articles that mentioned housing but were not useful for multifamily development strategy.

The updated version is stricter. An article now needs one of these signals:

- Direct multifamily or apartment relevance
- Development, supply, rent, capital markets, or transaction relevance
- Named multifamily market players
- Policy relevance that also connects to development, finance, supply, or multifamily operations

## Relevance Score

The script adds a `relevance_score` column to the CSV.

Higher scores usually mean the article is more useful for multifamily strategic research.

Only articles with a score of `50` or higher are saved to the final CSV.

The score gives extra weight to:

- Multifamily and apartment terms
- Development pipeline, permits, construction, lease-up, and adaptive reuse
- Rent growth, vacancy, occupancy, concessions, absorption, and market reports
- Financing, cap rates, refinancing, acquisitions, sales, and joint ventures
- Major owners, developers, REITs, lenders, and brokers
- High-value multifamily trade sources

The score reduces weak matches when an article is mostly about broad policy, homelessness, public housing, single-family housing, homebuyers, or mortgages without a clear multifamily connection.

The CSV is sorted by `relevance_score` in descending order, so the strongest articles appear first.

Numeric market signals can also add a scoring bonus:

- Any extracted number: `+5`
- Cap rate, financing cost, or supply / starts signal: additional `+5`

Market focus can also add a small scoring bonus:

- Los Angeles: `+15`
- California: `+10`
- Sun Belt: `+8`
- Texas: `+6`
- Seattle: `+5`
- New York: `+5`

## Priority

The script adds a `priority` column to make the CSV easier to scan.

Priority rules:

- `High`: `relevance_score >= 80`
- `Medium`: `relevance_score >= 60`
- `Low`: `relevance_score >= 50`

Because articles below `50` are excluded, the CSV should only contain High, Medium, or Low priority articles that passed the minimum research-quality threshold.

## Action Level

The script adds an `action_level` column for daily briefing workflow.

Action level rules:

- `Must Read`: `relevance_score >= 85`
- `Review`: `relevance_score >= 70`
- `Monitor`: `relevance_score >= 50`

`Must Read` and `Review` articles are also saved to `output/high_priority_articles.csv`.

## Market Focus

The script adds a `market_focus` column by detecting geography in the article title and summary.

Possible labels:

- `National`
- `California`
- `Los Angeles`
- `New York`
- `Seattle`
- `Texas`
- `Sun Belt`
- `Southeast`
- `Florida`
- `Arizona`
- `Other / Unknown`

More specific markets are checked before broader markets. For example, Los Angeles is detected before California.

## Strategic Angle

The script adds a `strategic_angle` column with simple rule-based labels.

These labels help identify why an article may matter for US multifamily or residential developer strategy.

Possible labels:

- `Financing Risk`: rates, debt, refinancing, lending, credit, or capital market pressure
- `Supply Pressure`: new supply, deliveries, starts, lease-up, vacancy, or pipeline issues
- `Rent Growth / Demand`: rents, occupancy, absorption, concessions, migration, or demand
- `Regulation Risk`: rent control, zoning, permitting, entitlement, LIHTC, or tenant rules
- `Cost Control`: construction costs, labor, materials, modular construction, or value engineering
- `Institutional Flow`: acquisitions, dispositions, portfolio deals, cap rates, or major capital flows
- `Developer Strategy`: development, adaptive reuse, build-to-rent, conversions, site acquisition, or groundbreakings

An article can receive more than one strategic angle.

## Decision Use

The script adds a `decision_use` column to show how a strategy team might use the article.

Possible labels:

- `Track Financing Conditions`
- `Track Supply Pipeline`
- `Track Rent / Vacancy Trend`
- `Track Regulation Risk`
- `Track Construction Cost`
- `Track Institutional Capital Flow`
- `Track Developer Strategy`
- `General Monitoring`

## Reason For Inclusion

The script adds a `reason_for_inclusion` column.

This is a short plain-English explanation based on matched keywords, relevance score, strategic angle, and market focus.

Example:

```text
Included because it scored 82 and mentions multifamily, rent growth, California, with a Rent Growth / Demand angle for California.
```

## Article Text Sample

The script adds an `article_text_sample` column.

When `FETCH_ARTICLE_TEXT = True`, the script tries to visit each likely article page using `requests` and `BeautifulSoup`.

Only the first 500 characters of cleaned article text are stored. The full article body is not saved yet.

If article fetching fails, the script keeps running and leaves the sample blank.

Set `FETCH_ARTICLE_TEXT = False` in `news_collector.py` if you want the script to run faster or avoid article page fetching.

## Extracted Numbers

The script adds an `extracted_numbers` column.

It looks for simple numeric market signals in the title, RSS summary, and article text sample.

Examples include:

- Percentages like `5.2%`
- Basis points like `100 bps` or `35 basis points`
- Dollar amounts like `$250 million` or `$1.2B`
- Unit counts like `350 units` or `1,200 apartments`
- Rent values like `$2,500 rent`
- Relevant years when tied to starts, deliveries, pipeline, forecast, or outlook

## Market Signal

The script adds a `market_signal` column.

Possible labels:

- `Rent Growth Signal`
- `Vacancy Signal`
- `Cap Rate Signal`
- `Financing Cost Signal`
- `Supply / Starts Signal`
- `Construction Cost Signal`
- `Concession Signal`
- `Deal Size Signal`
- `No Clear Numeric Signal`

## Strategic Implication

The script adds a `strategic_implication` column.

This is a short rule-based plain-English sentence that explains what the article may mean for US residential developer strategy.

It uses existing fields such as:

- `relevance_score`
- `priority`
- `action_level`
- `strategic_angle`
- `market_focus`
- `decision_use`
- `market_signal`
- `extracted_numbers`
- `matched_keywords`

Example:

```text
Monitor financing conditions because the article includes SOFR / rate signals that may affect construction loans and exit cap rates.
```

## Woomi Relevance

The script adds a `woomi_relevance` column.

Possible labels:

- `High relevance to US residential developer strategy`
- `Medium relevance to market monitoring`
- `Low relevance / background information`

This is a simple MVP label for quickly identifying articles that may matter most for a Korean residential developer studying US multifamily market entry and strategy.

## Recommended Next Step

The script adds a `recommended_next_step` column.

Possible labels:

- `Read full article`
- `Track source for follow-up`
- `Add to weekly strategy memo`
- `Monitor only`
- `Ignore unless repeated`

## LLM Analysis Prompt

The script adds an `llm_analysis_prompt` column.

This field is filled for strategy-briefing articles. It creates a structured prompt that can later be sent to an LLM.

The prompt includes:

- Article title
- Source
- URL
- Market focus
- Strategic angle
- Market signal
- Extracted numbers
- Strategic implication
- Woomi relevance

The prompt asks the LLM to answer:

- Why does this article matter for a US multifamily developer?
- What is the implication for Woomi / Woomi Global?
- What risk or opportunity does this indicate?
- What follow-up question should the strategy team ask?

Important: this MVP does not call an LLM API yet. It only prepares prompt text for a future GPT-based analysis layer.

## LLM Prompt Quality

The script adds three prompt QA columns:

- `llm_prompt_quality_score`
- `llm_prompt_quality_label`
- `missing_prompt_context`

The score is rule-based from `0` to `100`.

It checks whether the prompt includes:

- Title
- Source
- URL
- Market focus
- Strategic angle
- Market signal
- Extracted numbers
- Strategic implication
- Woomi relevance
- Follow-up questions

Quality labels:

- `Excellent`: score `>= 85`
- `Good`: score `>= 70`
- `Needs Improvement`: score `>= 50`
- `Poor`: score `< 50`

`missing_prompt_context` lists weak or missing fields, such as missing market focus, missing market signal, missing extracted numbers, missing Woomi relevance, or missing strategic implication.

This is useful before paid LLM API integration because it helps catch weak prompts before spending money on automated analysis.

## Optional GPT Analysis

GPT analysis is optional and turned off by default.

Settings near the top of `news_collector.py`:

```python
USE_OPENAI_ANALYSIS = False
OPENAI_MODEL = "gpt-4o-mini"
MAX_GPT_ARTICLES = 5
```

When `USE_OPENAI_ANALYSIS = False`, the script still runs normally without an OpenAI API key. The `gpt_strategic_analysis` CSV column is filled with:

```text
GPT analysis not enabled
```

When `USE_OPENAI_ANALYSIS = True`, the script:

- Reads the API key from the `OPENAI_API_KEY` environment variable
- Uses `OPENAI_MODEL`
- Sends only the top `MAX_GPT_ARTICLES` strategy-briefing articles
- Uses each article's existing `llm_analysis_prompt`
- Writes concise GPT output to `gpt_strategic_analysis`

Do not hardcode an API key in the script.

Example setup:

```bash
set OPENAI_API_KEY=your_api_key_here
```

Then change:

```python
USE_OPENAI_ANALYSIS = True
```

This mode is designed for later use. Keep it off while testing the free rule-based pipeline.

## RSS Sources

Current feeds include:

- Multifamily Dive
- Multifamily Executive
- Yield PRO
- Multi-Housing News
- NAHB Eye on Housing - Multifamily
- Construction Dive
- HousingWire
- Federal Reserve Press Releases

The first five are the highest-value sources because they are closer to multifamily owners, developers, managers, investors, and apartment market data.

Construction Dive, HousingWire, and Federal Reserve feeds are still useful, but the scoring rules are stricter for them because they produce more general construction, housing, mortgage, and macroeconomic news.

## Output

The script writes two kinds of outputs:

- Latest output files in `output/`
- Dated archive files in `output/runs/YYYY-MM-DD/`

The latest files are convenient because they always show the newest run. The dated archive folders are useful when you want to compare prior runs or keep a history of past daily briefings.

For daily reading, start here:

```text
output/daily_strategy_briefing.md
```

This Markdown report is the most human-readable output. Open it first when you want a quick daily strategy briefing instead of scanning CSV rows.

For weekly strategy review, read this next:

```text
output/weekly_strategy_memo.md
```

Recommended reading order:

1. `output/daily_strategy_briefing.md`
2. `output/weekly_strategy_memo.md`
3. `output/llm_prompt_pack.md`
4. `output/narrative_regime.md`
5. `output/regime_transition_report.md`
6. `output/regime_heatmap_report.md`
7. `output/regime_momentum_report.md`
8. `output/narrative_severity_report.md`
9. `output/materiality_impact_report.md`
10. `output/executive_priority_brief.md`
11. `output/strategy_scenario_report.md`
12. `output/regional_intelligence_report.md`
13. `output/gp_intelligence_report.md`
14. `output/institutional_relationship_report.md`
15. `output/source_health_report.md`
16. `output/source_activation_report.md`
17. `output/historical_memory_report.md`
18. `output/capital_flow_report.md`
19. `output/relationship_persistence_report.md`
20. `output/opportunity_radar_report.md`
21. `output/distress_watchlist_report.md`
22. `output/gp_source_coverage_report.md`
23. `output/deal_pipeline_report.md`
24. `output/relationship_graph_report.md`
25. `output/entity_resolution_report.md`
26. `output/residential_sector_report.md`
27. `output/gp_watchlist_report.md`
28. `output/strategy_briefing.csv`
29. `output/market_signals.csv`
30. `output/articles.csv`

The main CSV is saved here:

```text
output/articles.csv
```

The shorter daily briefing CSV is saved here:

```text
output/high_priority_articles.csv
```

`high_priority_articles.csv` only includes articles with `action_level` equal to `Must Read` or `Review`.

The market-signal CSV is saved here:

```text
output/market_signals.csv
```

`market_signals.csv` only includes articles where `market_signal` is not `No Clear Numeric Signal`.

The strategy briefing CSV is saved here:

```text
output/strategy_briefing.csv
```

`strategy_briefing.csv` includes articles where:

- `action_level` is `Must Read` or `Review`, or
- `woomi_relevance` is `High relevance to US residential developer strategy`

It is sorted by `action_level` first, then by `relevance_score` descending.

The LLM prompt pack is saved here:

```text
output/llm_prompt_pack.md
```

`llm_prompt_pack.md` contains one LLM-ready prompt per strategy-briefing article. It is designed for future GPT-based analysis, but the current script does not call any paid API.

The LLM prompt quality report is saved here:

```text
output/llm_prompt_quality_report.md
```

It summarizes prompt quality before any paid LLM API integration.

The GPT analysis preview is saved here:

```text
output/gpt_analysis_preview.md
```

It shows whether GPT mode was enabled, the model name, number of GPT-analyzed articles, and GPT analysis results if enabled.

The trend alerts report is saved here:

```text
output/trend_alerts.md
```

It compares the latest run against the previous run in `output/run_log.csv`.

The thematic trends report is saved here:

```text
output/thematic_trends.md
```

It compares the themes in the latest strategy briefing and market-signal CSVs against the most recent archived run.

## Dated Archive Folders

When this setting is enabled in `news_collector.py`:

```python
SAVE_DATED_OUTPUT = True
```

the script also saves a dated copy of each output file here:

```text
output/runs/YYYY-MM-DD/
```

Example:

```text
output/runs/2026-05-13/articles.csv
```

This lets you keep the normal latest files in `output/` while also archiving each day's generated files.

## Run Log

The script appends one row to:

```text
output/run_log.csv
```

Each run log row includes:

- `run_timestamp`
- `total_articles`
- `high_priority_articles`
- `market_signal_articles`
- `strategy_briefing_articles`
- `llm_prompts_generated`
- `gpt_analyzed_articles`
- `gpt_enabled`
- `output_folder`

Use `run_log.csv` to see how many articles and signals were generated each time the script ran.

## Trend Alerts

The script also creates:

```text
output/trend_alerts.md
```

When `SAVE_DATED_OUTPUT = True`, the report is also archived here:

```text
output/runs/YYYY-MM-DD/trend_alerts.md
```

The trend report uses `output/run_log.csv` to compare the latest run against the previous run.

It tracks:

- Total article volume
- High-priority article volume
- Market-signal article volume
- Strategy-briefing article volume

Alert labels:

- `Sharp Increase`: increase `>= 50%`
- `Moderate Increase`: increase `>= 20%`
- `Stable`: change between `-20%` and `+20%`
- `Moderate Decrease`: decrease `<= -20%`
- `Sharp Decrease`: decrease `<= -50%`

Trend detection is useful because it shows whether market-relevant news flow, numeric market signals, or strategy-review workload is accelerating, stable, or slowing down.

## Thematic Trends

The script also creates:

```text
output/thematic_trends.md
```

When `SAVE_DATED_OUTPUT = True`, the report is also archived here:

```text
output/runs/YYYY-MM-DD/thematic_trends.md
```

`thematic_trends.md` uses the latest:

- `strategy_briefing.csv`
- `market_signals.csv`

It compares them against the most recent previous archived run, using files such as:

```text
output/runs/YYYY-MM-DD/strategy_briefing.csv
output/runs/YYYY-MM-DD/market_signals.csv
```

It tracks counts by:

- `strategic_angle`
- `market_focus`
- `market_signal`
- `decision_use`
- `action_level`
- `woomi_relevance`

Alert labels:

- `New Theme`: previous count is `0` and latest count is greater than `0`
- `Sharp Increase`: increase `>= 50%`
- `Moderate Increase`: increase `>= 20%`
- `Stable`: change between `-20%` and `+20%`
- `Moderate Decrease`: decrease `<= -20%`
- `Sharp Decrease`: decrease `<= -50%`

Difference from `trend_alerts.md`:

- `trend_alerts.md` tracks total volume changes.
- `thematic_trends.md` tracks what the news is about.

Thematic trends are useful for strategic monitoring because they show whether financing risk, supply pressure, California / Los Angeles focus, institutional flow, regulation risk, or market-signal activity is becoming more important over time.

## Narrative Regime Detection

The script also creates:

```text
output/narrative_regime.md
```

When `SAVE_DATED_OUTPUT = True`, the report is also archived here:

```text
output/runs/YYYY-MM-DD/narrative_regime.md
```

Narrative regime detection is a simple rule-based synthesis layer. It looks at the latest strategy briefing and market-signal articles, then labels the current market narrative.

Possible regime labels include:

- `Financing Stress`
- `Supply Pressure`
- `Selective Capital Re-entry`
- `Policy / Entitlement Watch`
- `Construction Cost Pressure`
- `Developer Strategy Shift`
- `Stable Monitoring Environment`

The regime logic uses:

- Strategic angle counts
- Market signal counts
- Decision-use counts
- Market focus counts
- Institutional player keyword mentions
- Extracted-number presence
- Action-level mix

Difference from the other monitoring reports:

- `trend_alerts.md` tracks whether total article volume is rising or falling.
- `thematic_trends.md` tracks which themes, markets, signals, and decision-use labels are changing.
- `narrative_regime.md` interprets those signals as a plain-English market regime for strategy discussion.

This helps strategic interpretation because it turns many article-level signals into a single briefing view, including a primary regime, optional secondary regime, confidence level, implications for Woomi / Woomi Global, and recommended strategy-team questions.

## Regime Transition Tracking

The script also appends one row per run to:

```text
output/regime_log.csv
```

Each row records:

- `run_timestamp`
- `primary_regime`
- `secondary_regime`
- `confidence_level`
- `total_articles`
- `high_priority_articles`
- `market_signal_articles`
- `strategy_briefing_articles`
- `top_strategic_angle`
- `top_market_focus`
- `top_market_signal`

The transition report is saved here:

```text
output/regime_transition_report.md
```

When `SAVE_DATED_OUTPUT = True`, the report is also archived here:

```text
output/runs/YYYY-MM-DD/regime_transition_report.md
```

`regime_transition_report.md` uses the latest 3 to 5 rows from `regime_log.csv` to show:

- Current primary regime
- Previous primary regime
- Whether the regime changed
- How many consecutive runs the current regime has persisted
- Whether confidence is strengthening, weakening, or stable
- Whether market signals are increasing, decreasing, or stable

Transition labels:

- `Persistent Regime`
- `Possible Regime Shift`
- `Strengthening Regime`
- `Weakening Regime`
- `Insufficient History`

Difference from `narrative_regime.md`:

- `narrative_regime.md` explains the current run.
- `regime_transition_report.md` checks whether the current regime is persisting or changing across multiple runs.

Multi-run regime tracking matters because one run can be noisy. Repeated regime patterns are more useful for strategy decisions, underwriting posture, capital-flow monitoring, and weekly team discussion.

## Regime Heatmap

The script also creates a weighted regime score CSV:

```text
output/regime_heatmap.csv
```

and a human-readable report:

```text
output/regime_heatmap_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/regime_heatmap.csv
output/runs/YYYY-MM-DD/regime_heatmap_report.md
```

`regime_heatmap.csv` scores each possible regime from `0` to `100`:

- `Financing Stress`
- `Supply Pressure`
- `Selective Capital Re-entry`
- `Policy / Entitlement Watch`
- `Construction Cost Pressure`
- `Developer Strategy Shift`
- `Stable Monitoring Environment`

The CSV columns are:

- `run_timestamp`
- `regime`
- `raw_score`
- `normalized_score`
- `final_score`
- `strength_label`
- `supporting_signals`
- `interpretation`

`raw_score` is the first weighted score from the rule-based components.

`normalized_score` converts the raw score onto a `0` to `100` scale.

`final_score` is the calibrated score used for ranking and strength labels. It is designed to avoid too many regimes reaching `100` unless the supporting signals are very strong.

Strength labels:

- `Very Strong`: score `>= 80`
- `Strong`: score `>= 60`
- `Moderate`: score `>= 40`
- `Weak`: score `>= 20`
- `Not Detected`: score `< 20`

The heatmap uses simple rule-based scoring from:

- Strategic angle counts
- Market signal counts
- Decision-use counts
- Market focus counts
- Action-level mix
- Extracted-number presence
- Institutional player keywords
- Matched keywords

Difference from the regime reports:

- `narrative_regime.md` chooses and explains the current primary and secondary regime.
- `regime_transition_report.md` checks whether regimes are changing across multiple runs.
- `regime_heatmap_report.md` scores every regime side by side, even if it is not the top regime.

Weighted regime scoring is useful because more than one market narrative can be active at the same time. The heatmap helps Woomi compare financing stress, supply pressure, institutional capital flow, policy risk, construction cost pressure, and developer strategy shifts in one view.

## Regime Momentum

The script also creates:

```text
output/regime_momentum.csv
```

and:

```text
output/regime_momentum_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/regime_momentum.csv
output/runs/YYYY-MM-DD/regime_momentum_report.md
```

`regime_momentum.csv` compares the latest `regime_heatmap.csv` against the most recent previous archived heatmap.

The CSV columns are:

- `run_timestamp`
- `regime`
- `previous_score`
- `latest_score`
- `score_change`
- `momentum_label`

Momentum labels:

- `Accelerating`: score change `>= 15`
- `Improving`: score change `>= 5`
- `Stable`: score change between `-5` and `+5`
- `Weakening`: score change `<= -5`
- `Fading`: score change `<= -15`
- `New / Insufficient History`: no previous score exists

Calibration and momentum detection are useful because they make the regime layer less jumpy. Calibration reduces score saturation, while momentum shows whether each regime is strengthening, weakening, or staying stable across runs.

## Narrative Severity

The script also creates:

```text
output/narrative_severity.csv
```

and:

```text
output/narrative_severity_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/narrative_severity.csv
output/runs/YYYY-MM-DD/narrative_severity_report.md
```

`narrative_severity.csv` evaluates each major regime:

- `Financing Stress`
- `Supply Pressure`
- `Selective Capital Re-entry`
- `Policy / Entitlement Watch`
- `Construction Cost Pressure`
- `Developer Strategy Shift`

The CSV columns are:

- `run_timestamp`
- `regime`
- `severity_score`
- `conviction_score`
- `urgency_label`
- `opportunity_or_risk_label`
- `key_evidence`

`severity_score` shows how urgent or important the signal appears. It uses heatmap final score, momentum, action-level mix, market-signal count, extracted numbers, high-priority article count, and supporting signals.

`conviction_score` shows how well-supported the signal appears. It uses supporting article count, consistency across strategic angle / market signal / decision use, whether the regime appears in `narrative_regime.md`, and momentum direction.

Urgency labels:

- `Immediate Attention`: severity score `>= 80` and conviction score `>= 70`
- `Review This Week`: severity score `>= 60`
- `Monitor`: severity score `>= 40`
- `Background`: severity score `< 40`

Risk / opportunity labels:

- `Financing Stress`: `Risk`
- `Supply Pressure`: `Risk`
- `Construction Cost Pressure`: `Risk`
- `Policy / Entitlement Watch`: `Risk / Opportunity`
- `Selective Capital Re-entry`: `Opportunity / Pricing Signal`
- `Developer Strategy Shift`: `Opportunity / Capability Signal`

Difference from the regime reports:

- `regime_heatmap_report.md` compares each regime's calibrated intensity.
- `regime_momentum_report.md` shows whether each regime is strengthening or weakening versus the previous heatmap.
- `narrative_severity_report.md` combines intensity, momentum, evidence, and conviction into management attention levels.

Narrative severity is useful because a regime can be high-scoring but low-conviction, or moderate-scoring but backed by consistent evidence. This report helps decide what should be escalated, reviewed this week, monitored, or treated as background.

## Materiality / Impact Assessment

The script also creates:

```text
output/materiality_impact.csv
```

and:

```text
output/materiality_impact_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/materiality_impact.csv
output/runs/YYYY-MM-DD/materiality_impact_report.md
```

`materiality_impact.csv` translates narrative signals into business relevance for Woomi / Woomi Global.

The CSV columns are:

- `run_timestamp`
- `regime`
- `materiality_score`
- `impact_score`
- `business_area_impact`
- `impact_label`
- `key_business_risk_or_opportunity`
- `recommended_management_action`

`materiality_score` estimates how important a regime is for management attention. It uses severity, conviction, urgency, high-priority article count, market-signal count, Woomi relevance, market focus, and extracted-number evidence.

`impact_score` estimates how much a regime may affect business areas such as:

- Underwriting
- Financing
- Land / Pipeline
- GP Partnership
- Capital Markets
- LA / California Strategy
- Cost Management
- Leasing / Operations
- Strategic Monitoring

Impact labels:

- `Critical Business Impact`: impact score `>= 80`
- `High Business Impact`: impact score `>= 60`
- `Moderate Business Impact`: impact score `>= 40`
- `Low Business Impact`: impact score `< 40`

Difference from severity and conviction:

- `severity_score` asks how urgent or intense the regime signal is.
- `conviction_score` asks how well-supported the signal is.
- `materiality_score` asks whether the signal matters to management.
- `impact_score` asks which parts of the business may be affected.

This is useful because a research signal becomes more actionable when it is tied to underwriting, financing, pipeline strategy, GP partnerships, capital markets, LA / California strategy, cost management, or leasing assumptions.

## Executive Prioritization

The script also creates:

```text
output/executive_priorities.csv
```

and:

```text
output/executive_priority_brief.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/executive_priorities.csv
output/runs/YYYY-MM-DD/executive_priority_brief.md
```

`executive_priorities.csv` combines the prior management layers into one forced-ranked executive view.

The CSV columns are:

- `run_timestamp`
- `regime`
- `executive_priority_score`
- `executive_priority_rank`
- `executive_attention_tier`
- `management_message`
- `recommended_owner`
- `recommended_action_timing`

`executive_priority_score` uses:

- `materiality_score`
- `impact_score`
- `severity_score`
- `conviction_score`
- heatmap `final_score`
- `momentum_label`
- `business_area_impact`
- `urgency_label`

Executive attention tiers:

- `Tier 1 Executive Attention`: rank 1 to 2
- `Tier 2 Strategic Review`: rank 3 to 4
- `Tier 3 Monitoring`: rank 5 to 6
- `Background`: low score or not detected

Recommended owners can include:

- `Investment Team`
- `Development Team`
- `Finance / Treasury`
- `Strategy Team`
- `US Local Team`
- `Executive Committee`

Recommended action timing can be:

- `This Week`
- `Next IC / Strategy Meeting`
- `Monthly Monitoring`
- `Background Tracking`

Forced ranking is useful because management attention is limited. Even when several regimes look important, the executive brief keeps only the top two in Tier 1, the next two in Tier 2, and pushes the rest into monitoring or background tracking.

## Strategy Scenarios

The script also creates:

```text
output/strategy_scenarios.csv
```

and:

```text
output/strategy_scenario_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/strategy_scenarios.csv
output/runs/YYYY-MM-DD/strategy_scenario_report.md
```

The scenario engine creates three planning cases:

- `Base Case`
- `Bull Case`
- `Bear Case`

`strategy_scenarios.csv` includes:

- `scenario_probability_label`
- `key_assumptions`
- `expected_market_environment`
- `implication_for_woomi`
- `recommended_strategy_response`
- `key_risks_to_monitor`
- `trigger_events_to_watch`

Scenario logic:

- `Base Case` reflects the current dominant regime and executive priorities.
- `Bull Case` assumes financing stress eases, institutional capital re-entry strengthens, and supply pressure becomes manageable.
- `Bear Case` assumes financing stress persists, supply pressure worsens, and capital re-entry weakens.

Probability labels:

- `Most Likely`
- `Plausible Upside`
- `Plausible Downside`

Scenario planning is useful for US residential developer strategy because it prevents the team from making decisions from only one current narrative. It helps Woomi compare underwriting posture, capital partner monitoring, LA / California strategy, GP / developer partnership strategy, development timing, and cost discipline across upside and downside market paths.

## Regional Intelligence

The script also creates:

```text
output/regional_intelligence.csv
```

and:

```text
output/regional_intelligence_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/regional_intelligence.csv
output/runs/YYYY-MM-DD/regional_intelligence_report.md
```

The regional engine tracks:

- `Los Angeles`
- `California`
- `Seattle`
- `New York`
- `Texas`
- `Dallas`
- `Austin`
- `Phoenix`
- `Arizona`
- `Florida`
- `Southeast`
- `Sun Belt`
- `National / Other`

`regional_intelligence.csv` includes:

- `market_article_count`
- `high_priority_count`
- `market_signal_count`
- `average_relevance_score`
- `dominant_strategic_angle`
- `dominant_market_signal`
- `regional_risk_or_opportunity`
- `woomi_market_relevance`
- `recommended_market_action`

`woomi_market_relevance` labels:

- `Core Watch Market`
- `Strategic Watch Market`
- `General Monitoring`
- `Low Priority`

Suggested interpretation:

- Los Angeles and California are always `Core Watch Market`.
- Seattle is a `Strategic Watch Market` when signals appear.
- Texas, Dallas, Austin, Phoenix, Arizona, Florida, Southeast, and Sun Belt are `Strategic Watch Market` when article or market-signal activity is strong.
- National / Other is usually `General Monitoring`.

Regional monitoring matters for US multifamily development strategy because development feasibility is local. Financing, supply pressure, entitlement, rent growth, concessions, and GP partnership opportunities can differ sharply by city and state.

## Developer / GP Intelligence

The script also creates:

```text
output/gp_intelligence.csv
```

and:

```text
output/gp_intelligence_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/gp_intelligence.csv
output/runs/YYYY-MM-DD/gp_intelligence_report.md
```

The GP intelligence engine tracks major US multifamily developers, operators, REITs, and institutional GP platforms such as Greystar, Lincoln Property Company, AvalonBay, Related Companies, Trammell Crow Residential, Mill Creek Residential, Hines, Blackstone, Brookfield, Kennedy Wilson, Mavrek, Quarterra, Carmel Partners, BGO, Waterton, CIM Group, RXR, Related California, and others.

`gp_intelligence.csv` includes:

- `gp_name`
- `activity_type`
- `market_focus`
- `article_count`
- `average_relevance_score`
- `institutional_signal_strength`
- `growth_or_defensive_signal`
- `likely_strategy`
- `potential_implication_for_woomi`
- `recommended_follow_up`
- `strategic_priority_label`

Activity types include acquisition, disposition / exit, refinancing, recapitalization, development start, entitlement, modular construction, BTR expansion, office-to-residential conversion, JV / partnership, capital raise, market expansion, distressed opportunity, and operational technology / AI adoption.

`institutional_signal_strength` is a 0 to 100 score based on article frequency, relevance score, activity type, California / LA exposure, institutional capital involvement, and innovation signals.

Strategic priority labels:

- `Immediate Watch`
- `Strategic Watch`
- `General Monitoring`
- `Low Priority`

GP behavior matters for US residential developer strategy because major platforms can reveal pricing discovery, capital availability, development trends, distressed opportunities, construction innovation, market expansion, and potential JV or GP partnership signals.

## Institutional Relationship & Capital Flow Intelligence

The script also creates:

```text
output/institutional_relationships.csv
```

and:

```text
output/institutional_relationship_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/institutional_relationships.csv
output/runs/YYYY-MM-DD/institutional_relationship_report.md
```

This layer builds on the GP intelligence engine and adds firm-tier weighting, capital-flow inference, relationship signals, and Woomi-specific follow-up logic.

`institutional_relationships.csv` includes:

- `firm_name`
- `strategic_tier`
- `strategic_weight`
- `detected_markets`
- `detected_activity_types`
- `article_count`
- `highest_relevance_score`
- `average_relevance_score`
- `capital_flow_signal`
- `relationship_signal`
- `partnership_relevance_to_woomi`
- `california_la_relevance`
- `institutional_relationship_score`
- `recommended_follow_up`

Strategic tiers give more baseline weight to firms that are especially important for US multifamily strategy:

- Tier 1 / Immediate Strategic Importance = `100`
- Tier 2 / Strategic Watch = `75`
- Tier 3 / Growth and Market Signal Watch = `50`

The score is intentionally balanced. Strategic tier matters, but article relevance, activity type, capital-flow signal, relationship signal, California / LA relevance, and high-priority article status also affect the final `institutional_relationship_score`. This means a Tier 3 firm with strong current activity can outrank a Tier 1 firm with only weak background mentions.

`capital_flow_signal` uses simple rule-based labels such as:

- `Capital Inflow`
- `Capital Outflow / Exit`
- `Refinancing / Recapitalization`
- `Development Capital Deployment`
- `Distressed Opportunity Positioning`
- `Operational / Platform Investment`
- `No Clear Capital Flow Signal`

`relationship_signal` uses labels such as:

- `Potential JV / Partnership Signal`
- `Competitive Benchmark Signal`
- `Capital Partner Tracking Signal`
- `GP Capability Benchmark Signal`
- `Pricing Discovery Signal`
- `No Clear Relationship Signal`

Relationship and capital-flow intelligence matters because Woomi can use it to track possible GP partners, competitive benchmarks, institutional capital movement, pricing discovery, California / LA relevance, and developer capability signals before committing to deeper research or paid LLM analysis.

## Institutional Source Expansion

The script now uses source categories so articles can be scored and reviewed with better institutional context:

- `Core Multifamily News`
- `Institutional Real Estate / Capital Markets`
- `Developer / GP Newsrooms`
- `Brokerage / Debt / Research`
- `Public Agency / Housing Data`
- `Regional / California / LA Sources`

Each article row includes:

- `source_category`

Source-category bonuses are intentionally modest:

- Institutional Real Estate / Capital Markets: `+8`
- Developer / GP Newsrooms: `+10`
- Developer / GP Source Expansion: `+10`
- Regional / California / LA Sources: `+10`
- Core Multifamily News: `+5`
- Brokerage / Debt / Research: `+7`
- Public Agency / Housing Data: `+4`

These bonuses help better sources rise in the ranking, but they do not override weak article relevance. A poor article from a strong source can still be filtered out, while a strong article from a smaller source can still be saved.

The script also creates:

```text
output/source_health.csv
```

and:

```text
output/source_health_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/source_health.csv
output/runs/YYYY-MM-DD/source_health_report.md
```

`source_health.csv` includes:

- `source_name`
- `source_category`
- `platform_type`
- `source_url`
- `fetch_status`
- `entries_found`
- `articles_saved`
- `error_message`
- `source_quality_label`

`source_quality_label` uses simple rules:

- `High Value`: 3 or more saved articles
- `Useful`: at least 1 saved article
- `Watch`: feed worked and had entries, but no articles passed filtering
- `Failing`: confirmed feed URL failed or returned no usable feed
- `Placeholder / Needs Review`: source URL is not confirmed yet

Institutional source quality matters because GP intelligence, relationship scoring, capital-flow inference, and transaction monitoring are only as good as the source universe feeding them. The source health report helps identify which RSS feeds are producing useful signals and which developer, GP, brokerage, public-agency, or regional sources need manual URL review.

## Source Activation & Feed Validation

The script also creates:

```text
output/source_activation.csv
```

and:

```text
output/source_activation_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/source_activation.csv
output/runs/YYYY-MM-DD/source_activation_report.md
```

`source_activation.csv` evaluates every source in `SOURCE_REGISTRY` and adds lightweight validation fields:

- `source_status`: `Working`, `Placeholder`, `Failed`, or `Manual Review`
- `activation_type`: `RSS`, `Newsroom`, `HTML Parsing`, or `Manual`
- `feed_url`
- `last_successful_fetch`
- `fetch_attempts`
- `fetch_success_rate`
- `signal_density_score`
- GP, deal, capital markets, residential sector, California, LA, and institutional signal counts
- `source_quality_score`
- `source_priority_label`

The validation layer uses the current run's feed results. It checks whether a URL exists, whether the feed returned successfully, whether parsed entries were available, and whether saved articles created useful strategy signals. It does not aggressively scrape, does not require a paid API, and does not require a database.

Source priority tiers:

- `Tier 1`: major multifamily GPs, institutional investors, debt providers, agency lenders, and capital markets firms
- `Tier 2`: regional developers, BTR operators, student housing operators, and senior housing operators
- `Tier 3`: niche, local, newsroom, or general monitoring sources

`source_quality_score` is a weighted score using reliability, signal density, institutional importance, California / LA relevance, GP/developer usefulness, and deal extraction usefulness. This helps separate production-ready sources from placeholders and failed critical feeds.

## Historical Persistence & Capital Flow Memory

The script now creates three CSV-backed memory layers:

```text
output/historical_memory.csv
output/capital_flow_memory.csv
output/relationship_persistence.csv
```

and three Markdown reports:

```text
output/historical_memory_report.md
output/capital_flow_report.md
output/relationship_persistence_report.md
```

When `SAVE_DATED_OUTPUT = True`, all six files are also archived here:

```text
output/runs/YYYY-MM-DD/
```

`historical_memory.csv` tracks recurring observations across runs for GPs/developers, lenders, institutional capital partners, markets, residential sectors, deal/project signals, relationship edges, regimes, and capital-flow patterns.

Important fields include:

- `first_seen_date`
- `last_seen_date`
- `observation_count`
- `persistence_score`
- `momentum_direction`
- `signal_acceleration`
- `recurring_signal_label`
- `historical_importance_score`
- `longitudinal_conviction_score`
- `institutional_persistence_score`
- `capital_flow_strength_score`

Recurring signal labels are:

- `Emerging`
- `Persistent`
- `Accelerating`
- `Fading`
- `Dormant`
- `Reappearing`

`capital_flow_memory.csv` tracks repeated refinancing, construction financing, recurring lenders, recurring capital partners, market-level capital concentration, and debt-market stress patterns.

`relationship_persistence.csv` tracks repeated GP/lender/capital/market relationships over time, including recurring JV partnerships, repeated lender support, repeat market-entry patterns, and durable California / LA relationship signals.

This memory layer stays beginner-friendly by using CSV files only. It does not require an external database, paid API, or new infrastructure.

## Acquisition & Distress Opportunity Radar

The script now creates:

```text
output/opportunity_radar.csv
output/opportunity_radar_report.md
output/distress_watchlist.csv
output/distress_watchlist_report.md
```

When `SAVE_DATED_OUTPUT = True`, all four files are also archived here:

```text
output/runs/YYYY-MM-DD/
```

`opportunity_radar.csv` detects possible acquisition, recapitalization, refinancing gap, construction financing gap, preferred equity / rescue capital, stalled development, land / pipeline, office-to-residential conversion, JV / partnership, GP capability, BTR / SFR, affordable / workforce, and LA / California entitlement opportunities.

Important fields include:

- `opportunity_score`
- `opportunity_priority_label`
- `evidence_signals`
- `why_it_matters`
- `potential_woomi_angle`
- `recommended_next_action`
- `confidence_level`

`distress_watchlist.csv` focuses on stress signals such as refinancing stress, maturity walls, lender pressure, floating-rate debt, bridge loan stress, construction loan gaps, stalled projects, recapitalization needs, distressed sales, foreclosures, receivership, loan modification, covenant issues, preferred equity, rescue capital, and sponsor liquidity pressure.

Important fields include:

- `distress_score`
- `distress_priority_label`
- `evidence_signals`
- `potential_woomi_angle`
- `recommended_next_action`
- `confidence_level`

Opportunity and distress detection matters for Woomi's US residential developer strategy because it helps turn market monitoring into a practical radar for potential acquisition basis, recapitalization openings, rescue-capital needs, GP partnership gaps, entitlement opportunities, and capital-market stress patterns.

## Deal & Project Pipeline Extraction

The script also creates:

```text
output/deal_pipeline.csv
```

and:

```text
output/deal_pipeline_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/deal_pipeline.csv
output/runs/YYYY-MM-DD/deal_pipeline_report.md
```

This layer uses simple regex and rule-based parsing to extract transaction, financing, development, JV, entitlement, BTR, modular, and project pipeline signals from saved articles.

`deal_pipeline.csv` includes fields such as:

- `project_or_deal_name`
- `deal_type`
- `asset_type`
- `market`
- `city_or_submarket`
- `state_or_region`
- `gp_or_developer`
- `institutional_partner`
- `lender_or_debt_provider`
- `capital_partner`
- `unit_count`
- `dollar_amount`
- `loan_amount`
- `acquisition_price`
- `development_cost`
- `cap_rate`
- `rent_growth`
- `vacancy_rate`
- `concession_signal`
- `construction_start_or_delivery_timing`
- `entitlement_or_permitting_stage`
- `deal_signal_score`
- `deal_priority_label`
- `potential_woomi_use`

`deal_signal_score` is a 0 to 100 score based on article relevance, GP/developer detection, market detection, dollar amount, unit count, deal type importance, California / LA relevance, and institutional partner or lender presence.

`deal_priority_label` uses:

- `High Deal Intelligence`: score 80 or higher
- `Useful Deal Signal`: score 60 or higher
- `Monitor`: score 40 or higher
- `Low Detail Signal`: below 40

`potential_woomi_use` translates each row into a practical use case:

- `Pricing benchmark`
- `Underwriting benchmark`
- `GP partnership reference`
- `Capital market signal`
- `Pipeline / supply signal`
- `Entitlement / zoning watch`
- `Construction strategy reference`
- `Monitor only`

Deal and project extraction matters for US multifamily developer strategy because it turns article flow into a basic pipeline of transactions, construction starts, refinancing events, JV activity, entitlement signals, and supply benchmarks that can support underwriting, GP relationship mapping, and market-entry review.

## Developer Network & Relationship Graph

The script also creates:

```text
output/relationship_graph.csv
```

and:

```text
output/relationship_graph_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/relationship_graph.csv
output/runs/YYYY-MM-DD/relationship_graph_report.md
```

This layer converts deal and project rows into simple relationship edges. It helps show which developers, GP firms, lenders, capital partners, projects, and markets are connected through financing, JV activity, acquisitions, development activity, and market expansion.

`relationship_graph.csv` includes:

- `source_entity`
- `source_entity_type`
- `target_entity`
- `target_entity_type`
- `relationship_type`
- `market`
- `deal_type`
- `evidence_article_title`
- `url`
- `relationship_strength_score`
- `woomi_strategic_relevance`
- `recommended_follow_up`

Entity types include:

- `Developer / GP`
- `Institutional Capital`
- `Lender / Debt Provider`
- `Broker / Advisor`
- `Market / Region`
- `Project / Deal`
- `Public Agency / Policy`
- `Unknown`

Relationship types include:

- `JV / Partnership`
- `Financing Relationship`
- `Acquisition / Buyer`
- `Disposition / Seller`
- `Development Activity`
- `Entitlement / Permitting`
- `Market Expansion`
- `Capital Flow`
- `Pricing / Valuation Signal`
- `Innovation / Construction Strategy`
- `General Association`

`relationship_strength_score` is a 0 to 100 score based on deal signal score, article relevance, institutional relationship score, strategic firm tier, relationship type, California / LA relevance, and lender or capital partner presence.

`woomi_strategic_relevance` uses labels such as:

- `High relevance to Woomi partnership strategy`
- `Relevant to capital markets monitoring`
- `Relevant to LA / California strategy`
- `Relevant to underwriting benchmarks`
- `General market intelligence`
- `Low relevance`

Relationship graph intelligence matters for US residential developer strategy because it moves beyond individual articles. It helps Woomi see repeated connections among sponsors, lenders, capital partners, markets, and projects, which is useful for GP relationship mapping, underwriting benchmarks, capital-market monitoring, and LA / California strategy.

## Entity Resolution & Canonicalization

The script also creates:

```text
output/entity_resolution.csv
```

and:

```text
output/entity_resolution_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/entity_resolution.csv
output/runs/YYYY-MM-DD/entity_resolution_report.md
```

Entity resolution normalizes raw firm, lender, capital partner, and market names into canonical entities. For example, `Blackstone Real Estate`, `BREIT`, and `Blackstone Real Estate Income Trust` can resolve to `Blackstone`; `Fannie`, `FNMA`, and `Fannie Mae` can resolve to `Fannie Mae`.

`entity_resolution.csv` includes:

- `raw_entity`
- `canonical_entity`
- `entity_type`
- `alias_matched`
- `confidence_score`
- `source_file`
- `occurrence_count`
- `notes`

Confidence scores use simple rules:

- `100`: exact canonical match
- `90`: known alias match
- `75`: case-insensitive or punctuation-normalized match
- `60`: partial match
- `40`: weak match / needs review

The canonicalization layer also adds:

- `canonical_source_entity`, `canonical_target_entity`, and `entity_resolution_confidence` to `relationship_graph.csv`
- `canonical_gp_or_developer`, `canonical_lender_or_debt_provider`, `canonical_capital_partner`, and `canonical_market` to `deal_pipeline.csv`
- `canonical_gp_name` to `gp_intelligence.csv`

Entity resolution matters for institutional relationship intelligence because the same organization or market can appear under several names. Canonical names make network counts, lender tracking, GP relationship mapping, capital-flow analysis, and LA / California monitoring more reliable across runs.

## Residential Sector Coverage

The script now adds a `residential_sector` field to major CSV outputs, including:

- `articles.csv`
- `strategy_briefing.csv`
- `market_signals.csv`
- `deal_pipeline.csv`
- `gp_intelligence.csv`
- `institutional_relationships.csv`
- `regional_intelligence.csv`
- `executive_priorities.csv`

The sector labels are:

- `Multifamily`
- `Apartment`
- `Student Housing`
- `Senior Housing`
- `BTR / Single-Family Rental`
- `Affordable Housing`
- `Mixed-Use Residential`
- `Office-to-Residential Conversion`
- `Workforce Housing`
- `Manufactured Housing`
- `General Residential`

The script also creates:

```text
output/residential_sector_intelligence.csv
```

and:

```text
output/residential_sector_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/residential_sector_intelligence.csv
output/runs/YYYY-MM-DD/residential_sector_report.md
```

`residential_sector_intelligence.csv` summarizes article count, high-priority count, market-signal count, deal-signal count, average relevance, dominant market, dominant strategic angle, dominant GP/developer, sector risk or opportunity, Woomi sector relevance, and recommended sector action.

Broader residential coverage matters for US developer capability building because Woomi may need to monitor adjacent residential strategies beyond conventional multifamily, including BTR/SFR, student housing, senior housing, affordable/workforce housing, mixed-use residential, manufactured housing, and office-to-residential conversion.

## Emerging GP Ranking & Watchlist

The script now creates:

```text
output/gp_watchlist.csv
```

and:

```text
output/gp_watchlist_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/gp_watchlist.csv
output/runs/YYYY-MM-DD/gp_watchlist_report.md
```

`gp_watchlist.csv` ranks rising residential developers and GP platforms using these rule-based component scores:

- `gp_activity_score`
- `institutional_relationship_score`
- `capital_flow_score`
- `regional_relevance_score`
- `residential_sector_score`
- `partnership_signal_score`
- `innovation_signal_score`
- `california_la_relevance_score`
- `execution_signal_score`
- `momentum_signal_score`
- `emerging_gp_score`

`emerging_gp_score` is a weighted composite that emphasizes institutional relationships, capital-flow signals, partnership signals, residential sector fit, regional relevance, California / LA relevance, innovation, execution, and current momentum. The score is designed to help identify developers or GPs that may become important strategic partners, competitors, acquisition targets, or institutional capital magnets.

The GP tier labels are:

- `Tier 1 Strategic GP`
- `Tier 2 High Potential GP`
- `Tier 3 Monitoring GP`
- `Emerging Watchlist`
- `Low Signal`

The watchlist also detects partnership signals when a GP appears near major capital, lender, brokerage, or developer names such as Blackstone, Brookfield, Starwood, Greystar, Kennedy Wilson, Related, Hines, JLL, CBRE, Fannie Mae, and Freddie Mac.

`gp_watchlist_report.md` summarizes top emerging GPs, Tier 1 and Tier 2 names, California / LA watch names, BTR / SFR activity, affordable housing activity, student housing activity, innovation-oriented platforms, institutional capital magnets, and potential Woomi partnership candidates.

GP ranking matters for developer capability expansion because Woomi can use it to prioritize relationship mapping, partnership research, competitive benchmarking, capital-flow monitoring, and market-entry learning.

## Developer / GP Source Coverage

The script now adds a dedicated source expansion category:

```text
Developer / GP Source Expansion
```

It also creates:

```text
output/gp_source_coverage.csv
```

and:

```text
output/gp_source_coverage_report.md
```

When `SAVE_DATED_OUTPUT = True`, both files are also archived here:

```text
output/runs/YYYY-MM-DD/gp_source_coverage.csv
output/runs/YYYY-MM-DD/gp_source_coverage_report.md
```

`gp_source_coverage.csv` tracks developer, GP, capital platform, BTR / SFR, student housing, senior housing, lender, and brokerage source coverage.

Important fields include:

- `platform_type`: identifies whether the source is a multifamily developer/operator, institutional capital platform, BTR / SFR platform, student housing platform, senior housing platform, lender/debt platform, brokerage/advisor, public/agency source, or other source.
- `source_priority`: labels each source as `Critical Source`, `High Priority Source`, `Useful Source`, `Watch Source`, or `Placeholder / Needs Review`.
- `needs_manual_review`: marks placeholder or failing sources that need a confirmed public newsroom, RSS, press release, or insights URL.

Many developer and GP websites do not publish obvious RSS feeds. When a public feed is not confirmed, the script keeps the source as `Placeholder / Needs Review` instead of scraping paywalled or login-only pages.

GP-specific source coverage improves the GP watchlist, relationship graph, and institutional capital intelligence because better source inputs create better firm detection, deal signals, capital-flow signals, and partnership clues.

## Daily Markdown Briefing

The script also creates:

```text
output/daily_strategy_briefing.md
```

Use this file as the first-read daily report.

It includes:

- Report title
- Generated timestamp
- Total saved articles
- High-priority article count
- Market-signal article count
- Strategy-briefing article count
- Executive Summary
- Must Read Articles
- Key Market Signals
- Financing / Capital Markets
- Supply / Demand
- Policy / Regulation
- Institutional Flow / Deals
- Developer Strategy / Innovation
- Recommended Follow-up Items

The Executive Summary is rule-based. It highlights the most common strategic angle, most common market focus, number of Must Read articles, number of Review articles, and whether market signals were detected.

The Recommended Follow-up Items section pulls articles where `recommended_next_step` is:

- `Read full article`
- `Add to weekly strategy memo`
- `Track source for follow-up`

## Weekly Strategy Memo

The script also creates:

```text
output/weekly_strategy_memo.md
```

Use this file for a more thematic weekly review. It is generated from the same data used for `strategy_briefing.csv` and `market_signals.csv`.

Difference between the two Markdown reports:

- `daily_strategy_briefing.md` is article-focused and useful for quick daily scanning.
- `weekly_strategy_memo.md` is theme-focused and better for strategy discussion, weekly review, and memo writing.

The weekly memo includes:

- Executive Takeaways
- Trend Alert Summary
- Thematic Trend Summary
- Narrative Regime Summary
- Regime Transition Summary
- Regime Heatmap Summary
- Regime Momentum Summary
- Narrative Severity Summary
- Materiality / Impact Summary
- Executive Priority Summary
- Scenario Summary
- Regional Intelligence Summary
- GP / Developer Intelligence Summary
- Institutional Relationship Summary
- Deal / Project Pipeline Summary
- Relationship Graph Summary
- Residential Sector Coverage Summary
- Emerging GP Watchlist Summary
- GP Source Coverage Summary
- Source Activation Summary
- Historical Persistence Summary
- Capital Flow Memory Summary
- Recurring Relationship Summary
- Opportunity / Distress Radar Summary
- Source Health Summary
- Key Themes This Week
- Financing & Capital Markets
- Supply / Demand Signals
- Policy & Regulation Watch
- Institutional Flow / Deals
- Developer Strategy / Innovation
- Implications for Woomi / US Residential Developer Strategy
- Recommended Follow-up Actions

The weekly memo uses rule-based logic to highlight repeated themes, common markets, common market signals, Must Read article count, high Woomi relevance count, repeated decision-use labels, volume trend alerts, and thematic trend alerts.

## LLM Prompt Pack

The script also creates:

```text
output/llm_prompt_pack.md
```

Use this file when you want to manually test GPT-style strategic analysis without changing the code.

For now, the workflow is:

1. Run `python news_collector.py`.
2. Open `output/llm_prompt_pack.md`.
3. Copy one prompt into an LLM.
4. Review the LLM response before adding any conclusions to a strategy memo.

This prepares the project for a future automated GPT-based layer while keeping the current MVP free of paid API calls.

## LLM Prompt Quality Report

The script also creates:

```text
output/llm_prompt_quality_report.md
```

The report includes:

- Total prompts reviewed
- Average prompt quality score
- Number of Excellent / Good / Needs Improvement / Poor prompts
- Top 5 strongest prompts
- Top 5 weakest prompts
- Common missing context issues

Use this report before connecting any paid API. The goal is to improve prompt quality first, then automate later.

## GPT Analysis Preview

The script also creates:

```text
output/gpt_analysis_preview.md
```

When GPT mode is off, this file clearly says GPT analysis was not enabled.

When GPT mode is on, this file shows the GPT analysis results for the top `MAX_GPT_ARTICLES` strategy-briefing articles.

This lets you preview the future paid-analysis workflow without making GPT mandatory for the MVP.

## Deal Fingerprinting & Opportunity Deduplication

The script also creates:

```text
output/deal_fingerprints.csv
output/deal_fingerprint_report.md
output/opportunity_deduplication.csv
output/opportunity_deduplication_report.md
```

Deal fingerprinting creates a canonical event ID for each project, deal, refinancing, recapitalization, JV, construction financing, or distress-related situation. It uses lightweight matching based on normalized GP/developer names, lender names, markets, residential sectors, deal types, project names, unit counts, dollar amounts, loan amounts, and title keywords.

Important fields:

- `deal_fingerprint_id`: stable ID for a canonical deal or event.
- `fingerprint_confidence`: how confident the script is that the event is structured enough to track.
- `canonical_project_name`: cleaned project or development name.
- `canonical_deal_name`: cleaned deal-level name.
- `canonical_event_name`: readable event label such as refinancing, JV, or construction financing.
- `duplicate_cluster_id`: grouping ID for repeated coverage of the same event.
- `duplicate_count`: number of related rows mapped to the same canonical event.

Opportunity deduplication checks opportunity and distress rows against those fingerprints. This helps prevent article-count inflation, where repeated or syndicated articles make one opportunity look like many separate opportunities.

Deduplication fields:

- `deduplicated_opportunity_score`: strongest opportunity score for one canonical event.
- `deduplicated_distress_score`: strongest distress score for one canonical event.
- `opportunities_removed_via_deduplication`: repeated opportunity rows that should not inflate counts.
- `distress_inflation_prevented`: repeated distress rows that should not inflate distress tracking.
- `multi_source_confirmation`: shows when repeated coverage may strengthen confidence instead of simply creating noise.

Why this matters:

- It improves persistence accuracy by tracking unique canonical events instead of raw article volume.
- It strengthens relationship graph quality by counting repeat GP, lender, and capital partner relationships around the same event.
- It improves historical memory reliability by reducing duplicate rows from repeated news coverage.
- It helps Woomi distinguish true recurring market signals from repeated coverage of the same deal.

## Timing Intelligence & Market Entry Windows

The script also creates:

```text
output/timing_intelligence.csv
output/timing_intelligence_report.md
output/market_entry_window.csv
output/market_entry_window_report.md
```

`timing_intelligence.csv` looks for when Woomi should pay attention, not just what happened. It tracks refinancing maturity windows, construction starts, delivery timing, lease-up, entitlement and permitting cycles, acquisition windows, capital re-entry, recapitalization timing, distress sale timing, BTR/SFR expansion timing, office conversion timing, and supply wave timing.

Important fields:

- `timing_signal_type`: the type of timing signal, such as `Refinancing / Maturity Window`, `Construction Start`, `Entitlement / Permitting`, or `Acquisition Window`.
- `timing_reference`: the plain text timing clue found in the article or deal row, such as a year, quarter, or timing phrase.
- `estimated_timing_bucket`: rough timing label: `Immediate / 0-3 Months`, `Near-Term / 3-6 Months`, `Medium-Term / 6-12 Months`, `Long-Term / 12+ Months`, or `Unknown Timing`.
- `timing_urgency_score`: 0 to 100 score combining timing type, timing bucket, market relevance, and deal/opportunity/distress strength.
- `timing_confidence`: `High`, `Medium`, or `Low`.
- `recommended_monitoring_frequency`: `Weekly`, `Biweekly`, `Monthly`, `Quarterly`, or `Monitor Only`.

`market_entry_window.csv` converts timing and strategy signals into a market-level entry view for:

- Los Angeles
- California
- Sun Belt
- Texas
- Florida
- New York
- Seattle
- National / Other

Important fields:

- `market_entry_score`: 0 to 100 score for current market-entry attention.
- `market_entry_window_label`: `Active Watch Window`, `Selective Entry Window`, `Early Signal / Prepare`, `Monitor Only`, or `Not Attractive Now`.
- `recommended_entry_posture`: suggested Woomi posture, such as `Actively source opportunities`, `Prepare GP conversations`, `Monitor refinancing and distress pipeline`, `Track entitlement / permitting pipeline`, `Wait for better pricing evidence`, or `Monitor only`.
- `key_entry_risks`: main risks behind the market score.
- `key_entry_opportunities`: main opportunity signals behind the market score.

Why this matters:

- Timing intelligence helps the team separate immediate watch items from long-cycle background monitoring.
- Market entry windows help connect refinancing, distress, entitlement, construction, capital-flow, and GP signals into a practical action cadence.
- For US residential developer strategy, timing can matter as much as signal strength because financing gaps, entitlement milestones, and acquisition windows can close quickly.

## Permit / Entitlement Intelligence

The script also creates:

```text
output/entitlement_intelligence.csv
output/entitlement_intelligence_report.md
output/la_entitlement_watch.csv
output/la_entitlement_watch_report.md
```

`entitlement_intelligence.csv` detects zoning, permitting, planning approval, CEQA, density bonus, affordable overlay, office conversion, SB 35, Builder's Remedy, Housing Element, RHNA, and other entitlement-related signals.

Important fields:

- `entitlement_signal_type`: label such as `Zoning / Rezoning`, `Planning Approval`, `Building Permit / Construction Permit`, `CEQA / Environmental Review`, `Density Bonus / TOC`, `Office-to-Residential Conversion`, or `Builder's Remedy / SB 35`.
- `entitlement_stage`: rough stage such as `Early Planning`, `Under Review`, `Approved / Entitled`, `Permitted`, `Construction Ready`, `Delayed / Appealed`, or `Unknown Stage`.
- `approval_body`: likely decision body, such as Planning Commission, City Council, City Planning Department, California HCD, or Local Housing Authority.
- `regulatory_theme`: plain-English regulatory theme, such as density incentive, CEQA risk, zoning reform, permit acceleration, or entitlement delay risk.
- `entitlement_risk_score`: 0 to 100 score for entitlement, CEQA, delay, policy, and approval risk.
- `entitlement_opportunity_score`: 0 to 100 score for approval, permit, density bonus, by-right, office conversion, and LA / California opportunity.

`la_entitlement_watch.csv` filters those signals into a focused Los Angeles / California development watchlist. It tracks submarkets such as Koreatown, DTLA, Hollywood, Wilshire, Lincoln Heights, Watts, Pasadena, Glendale, Culver City, Santa Monica, Long Beach, Orange County, Inland Empire, Southern California, and California.

LA watch fields:

- `local_relevance_score`: score for local LA / California site-strategy relevance.
- `woomi_site_strategy_relevance`: `High relevance to LA site strategy`, `Relevant to California entitlement monitoring`, `General LA / California monitoring`, or `Low relevance`.
- `potential_site_strategy_angle`: simple action lens, such as track entitlement precedent, monitor density bonus use, watch affordable housing requirement, track office-to-residential feasibility, or benchmark permitting timeline.
- `recommended_local_follow_up`: suggested local next step.

Why this matters:

- Entitlement intelligence helps Woomi build US residential developer capability beyond capital-market monitoring.
- LA / California development strategy depends heavily on zoning, CEQA, affordability requirements, density incentives, and local approval timing.
- Tracking permit and entitlement precedent can improve site screening, underwriting assumptions, GP partner evaluation, and construction-ready pipeline monitoring.

## Submarket & Parcel Intelligence

The script also creates:

```text
output/submarket_intelligence.csv
output/submarket_intelligence_report.md
output/la_submarket_watch.csv
output/la_submarket_watch_report.md
```

`submarket_intelligence.csv` aggregates signals below the regional level. It looks for LA / Southern California submarkets such as Koreatown, Wilshire, DTLA, Hollywood, Lincoln Heights, Watts, Pasadena, Long Beach, Orange County, and Inland Empire, plus strategic US submarkets such as Brooklyn, Queens, Seattle, Austin, Dallas, Nashville, Atlanta, Phoenix, Tampa, Miami, Charlotte, and Raleigh.

Important fields:

- `submarket_opportunity_score`: 0 to 100 score based on opportunity count, deal count, entitlement opportunity score, timing signals, residential sector fit, LA / California relevance, GP activity, and site strategy themes.
- `submarket_risk_score`: 0 to 100 score based on CEQA / environmental risk, entitlement delay, distress, refinancing stress, supply pressure, construction delay, and local execution complexity.
- `execution_complexity_score`: 0 to 100 score based on entitlement uncertainty, CEQA / appeal risk, permitting delay, affordability requirements, urban infill complexity, and office conversion complexity.
- `site_strategy_theme`: local theme such as transit-oriented development, downtown infill, office conversion corridor, density bonus corridor, mixed-use corridor, waterfront redevelopment, arts district, or suburban growth corridor.
- `woomi_site_strategy_relevance`: `High relevance to Woomi site strategy`, `Strategic watch submarket`, `General monitoring`, or `Low relevance`.
- `recommended_submarket_action`: suggested action such as track local planning docket, monitor entitlement precedent, review acquisition pipeline, monitor refinancing / distress pipeline, track local GP / sponsor activity, watch office-to-residential feasibility, or monitor only.

`la_submarket_watch.csv` focuses on LA / Southern California site strategy and includes:

- `la_submarket`
- `la_opportunity_score`
- `la_execution_risk_score`
- `entitlement_precedent_signal`
- `potential_woomi_site_strategy`
- `recommended_local_follow_up`

Why this matters:

- Developer capability depends on local site knowledge, not just national or metro-level signals.
- LA / California strategy requires monitoring corridors, entitlement precedent, parcel feasibility, affordable housing rules, and execution risk.
- Submarket intelligence helps Woomi compare where to track sites, where to map local sponsors, and where permitting or CEQA complexity may affect development timing.

## Real Asset & Parcel Intelligence

The script also creates:

```text
output/asset_parcel_intelligence.csv
output/asset_parcel_intelligence_report.md
output/la_asset_watch.csv
output/la_asset_watch_report.md
```

`asset_parcel_intelligence.csv` extracts project/site-level clues from article and deal text. This is not GIS or parcel-database work yet; it is a lightweight rule-based layer that looks for addresses, intersections, neighborhood clues, project names, developers, sponsors, lenders, site size, unit counts, dollar amounts, entitlement status, permit status, construction status, delivery timing, acquisition/sale/refinancing language, office conversion language, and affordable/density bonus language.

Important fields:

- `canonical_asset_or_project_name`: best readable name for the project, property, or site signal.
- `address_or_location_clue`: address, neighborhood, submarket, or market clue found in the text.
- `intersection_or_corridor`: intersection clue or corridor/site strategy theme.
- `asset_strategy_signal`: `Acquisition / Site Control`, `Entitlement Play`, `Construction-Ready Pipeline`, `Development Start`, `Lease-Up / Delivery`, `Refinancing / Recapitalization`, `Office-to-Residential Conversion`, `Affordable / Density Bonus Strategy`, `Distressed / Stalled Asset`, or `General Asset Signal`.
- `site_control_signal`: `Site acquired`, `Land / parcel referenced`, `Project under entitlement`, `Permitted / construction ready`, `Existing asset refinance`, `Existing asset sale`, or `Unknown site control`.
- `execution_stage`: `Site Search / Early Signal`, `Site Controlled`, `Entitlement / Planning`, `Permitted`, `Under Construction`, `Delivered / Lease-Up`, `Stabilized / Operating`, `Distressed / Stalled`, or `Unknown`.
- `asset_opportunity_score`: 0 to 100 score for asset/site opportunity relevance.
- `asset_risk_score`: 0 to 100 score for site-level risk, including entitlement, delay, financing stress, distress, and complexity.

`la_asset_watch.csv` filters asset/site rows for LA / Southern California relevance and adds:

- `la_asset_opportunity_score`
- `la_asset_risk_score`
- `woomi_site_relevance`
- `potential_woomi_strategy_angle`
- `recommended_local_follow_up`

Why this matters:

- US residential developer strategy eventually has to connect market signals to real sites, assets, sponsors, and execution stages.
- Asset / parcel intelligence helps Woomi screen potential acquisition, JV, entitlement, financing, office conversion, and construction-ready pipeline opportunities.
- This layer prepares the MVP for future geocoding, parcel database matching, ownership research, and site underwriting workflows without requiring any external GIS API today.

## Entitlement Workflow & Development Lifecycle

The script also creates:

```text
output/development_lifecycle.csv
output/development_lifecycle_report.md
output/la_development_lifecycle_watch.csv
output/la_development_lifecycle_watch_report.md
```

`development_lifecycle.csv` turns asset and parcel signals into a simple project pipeline. It classifies each asset or project into lifecycle stages such as:

- `Early Site Signal`
- `Site Acquisition / Site Control`
- `Planning Filed`
- `Community Review`
- `Environmental Review / CEQA`
- `Entitlement Under Review`
- `Entitled / Approved`
- `Building Permit / Construction Permit`
- `Construction Ready`
- `Construction Started`
- `Vertical Construction`
- `Topped Out`
- `Delivery / Opening`
- `Lease-Up`
- `Stabilized / Operating`
- `Refinancing / Recapitalization`
- `Distressed / Stalled`
- `Unknown Stage`

Important fields:

- `current_lifecycle_stage`: the rule-based estimate of where the project sits in the development process.
- `previous_lifecycle_stage_if_known`: previous stage from the latest lifecycle file, when the same project is found again.
- `lifecycle_progression_signal`: `Progressing`, `Stalled`, `Reappearing`, `Newly Detected`, `Mature / Operating`, or `Unknown`.
- `lifecycle_opportunity_score`: 0 to 100 score for development timing opportunity.
- `lifecycle_risk_score`: 0 to 100 score for entitlement, financing, construction, lease-up, or distress risk.
- `timing_bucket`: estimated timing from the timing-intelligence layer when available.
- `entitlement_complexity_flag`, `financing_dependency_flag`, `construction_execution_flag`, and `lease_up_risk_flag`: simple High / Medium / Low / Unknown flags.
- `woomi_lifecycle_relevance`: explains whether the item is relevant to development timing, entitlement monitoring, acquisition / JV timing, underwriting benchmarks, or general monitoring.

`la_development_lifecycle_watch.csv` filters lifecycle rows for LA / Southern California and highlights local site-strategy questions such as permit issuance, construction-ready pipeline, stalled project opportunity, delivery / lease-up benchmarking, and refinancing or recapitalization windows.

Why this matters:

- Developer capability depends on knowing whether a project is early, entitled, permitted, under construction, delivering, leasing, stabilized, refinancing, or stalled.
- LA / California strategy needs a local view of entitlement status, CEQA risk, permit timing, construction readiness, and sponsor execution.
- Lifecycle intelligence helps Woomi decide when to watch, underwrite, contact a GP, track a lender, or prepare for a possible JV / acquisition conversation.

## Lifecycle Progression & State Transitions

The script also creates:

```text
output/lifecycle_transition.csv
output/lifecycle_transition_report.md
output/la_lifecycle_transition_watch.csv
output/la_lifecycle_transition_watch_report.md
```

`lifecycle_transition.csv` compares the latest `development_lifecycle.csv` with the previous archived lifecycle file under `output/runs/YYYY-MM-DD/`. This turns lifecycle classification from a single-run snapshot into a simple longitudinal tracker.

Important fields:

- `previous_stage` and `current_stage`: the prior and latest lifecycle stages for the same project or asset when a match is found.
- `previous_stage_rank` and `current_stage_rank`: numeric stage order used to detect movement through the pipeline.
- `transition_type`: `Forward Progression`, `Same Stage Persistence`, `Possible Stall`, `Stage Regression / Conflicting Signal`, `Reappearing Project`, `Newly Detected Project`, `Mature / Operating`, or `Unknown Transition`.
- `progression_score`: 0 to 100 score for positive movement through entitlement, permit, construction, delivery, or operating stages.
- `stall_risk_score`: 0 to 100 score for possible delay, CEQA risk, financing stress, stage regression, or repeated early-stage persistence.
- `execution_momentum_label`: `Advancing`, `Stable`, `Stalled Risk`, `Reappearing`, `Mature`, `Conflicting`, or `Unknown`.
- `woomi_timing_relevance`: explains whether the transition matters for entry timing, entitlement timing, construction timing, refinancing / recap timing, or general monitoring.

`la_lifecycle_transition_watch.csv` filters transitions for LA / Southern California projects and adds local timing labels such as:

- `Early entitlement watch`
- `Permit issuance watch`
- `Construction start watch`
- `Delivery / lease-up benchmark`
- `Stalled project opportunity watch`
- `Refinancing / recap timing watch`
- `Monitor only`

Why this matters:

- A project mention is less useful than knowing whether it is moving, stuck, reappearing, or conflicting across multiple runs.
- Lifecycle progression helps Woomi time GP conversations, entitlement research, underwriting updates, acquisition monitoring, and construction-readiness reviews.
- Stall-risk tracking is useful for identifying possible rescue-capital, recapitalization, JV, or delayed-development opportunities.

## Project Identity Resolution & Persistent Asset Memory

The script also creates:

```text
output/project_identity.csv
output/project_identity_report.md
output/persistent_asset_memory.csv
output/persistent_asset_memory_report.md
output/la_persistent_asset_watch.csv
output/la_persistent_asset_watch_report.md
```

`project_identity.csv` tries to recognize when different article titles, addresses, project names, sponsors, lenders, deal references, or lifecycle rows refer to the same underlying project or asset.

Important fields:

- `canonical_project_id`: durable project identifier created by the script for cross-file matching.
- `canonical_project_name`: best readable project or asset name for the cluster.
- `canonical_location_key`: normalized location key used for identity matching.
- `identity_confidence`: rule-based confidence score. `100` means exact address plus developer match, `90` means project name plus market plus developer, `80` means address/location plus market, `70` means strong title similarity plus same market, `60` means partial match, and `40` means weak match needing review.
- `matched_by`: plain-English explanation of why the row was matched.
- `duplicate_project_cluster_id`: populated when multiple raw references are grouped into the same project cluster.
- `needs_manual_review`: flags weaker identity matches for cleanup.

`persistent_asset_memory.csv` rolls those canonical project identities into a project memory table. It tracks:

- first and last seen date
- observation count
- source count
- lifecycle stage history
- latest lifecycle stage
- highest opportunity and risk scores
- entitlement, timing, financing, distress, and relationship signal counts
- progression status
- stall risk label
- persistent asset score
- Woomi asset watch priority

`la_persistent_asset_watch.csv` filters persistent asset memory for LA / Southern California projects and adds local site-strategy fields such as `woomi_site_strategy_relevance`, `potential_woomi_strategy_angle`, and `recommended_local_follow_up`.

Why this matters:

- Project tracking breaks down if the same asset appears under several article headlines or partial address references.
- Canonical project IDs reduce duplicate inflation in lifecycle transitions, opportunity radar, relationship graph, and historical memory.
- Persistent asset memory helps Woomi track repeated site, sponsor, entitlement, financing, delivery, and distress signals over time.

## Strategic Signal Quality & Confidence Calibration

The script also creates:

```text
output/signal_quality.csv
output/signal_quality_report.md
output/high_confidence_watchlist.csv
output/high_confidence_watchlist_report.md
```

`signal_quality.csv` scores each canonical project signal so the strategy team can separate institutional-grade intelligence from weak or noisy mentions.

The scoring framework uses:

- source quality, including working sources, institutional sources, local market sources, and placeholder-source penalties
- multi-source confirmation, including repeated project detection, repeated sponsors, and repeated lifecycle stages
- specificity, including addresses, project names, sponsors, lenders, unit counts, dollar amounts, entitlement details, and permit details
- lifecycle consistency, including logical stage progression and absence of conflicting stages
- historical persistence, including recurring observations, financing signals, and entitlement signals

Important fields:

- `overall_signal_quality_score`: 0 to 100 calibrated confidence score.
- `signal_quality_label`: `Institutional Grade`, `High Confidence`, `Moderate Confidence`, `Weak Signal`, or `Noise Risk`.
- `institutional_confidence_label`: `Strong Institutional Signal`, `Institutional Watch`, `Early Institutional Signal`, `Speculative`, or `Weak`.
- `false_positive_risk`: `Very Low`, `Low`, `Moderate`, or `High`.
- `signal_decay_risk`: `Persistent`, `Stable`, `Fading`, `Weakening`, or `Likely Noise`.
- `recommended_signal_action`: `Immediate strategic review`, `Add to executive watchlist`, `Monitor for confirmation`, `Track only`, or `Deprioritize`.

`high_confidence_watchlist.csv` filters the calibrated signal table to the most useful items for management review. It includes institutional-grade and high-confidence project signals, with strategic themes such as refinancing opportunity, entitlement progression, construction start pipeline, institutional capital movement, distressed opportunity, LA urban infill opportunity, affordable housing pipeline, BTR expansion, student housing expansion, and senior housing growth.

Why this matters:

- Early-stage market intelligence can be noisy; confidence calibration reduces false positives before signals influence strategy.
- Institutional-grade signals should be reviewed before weak one-off mentions.
- A high-confidence watchlist helps Woomi focus executive attention on the most durable, specific, and strategically relevant project signals.

## Executive Dashboard Data Layer

The script also creates dashboard-ready files for a future web app:

```text
output/dashboard_summary.csv
output/dashboard_cards.csv
output/dashboard_watchlists.csv
output/executive_dashboard_brief.md
```

These files do not build a UI yet. They organize the existing intelligence outputs into simpler datasets that could later power a web dashboard, Streamlit app, internal portal, or BI tool.

Recommended executive reading order:

1. `executive_dashboard_brief.md`
2. `high_confidence_watchlist_report.md`
3. `signal_quality_report.md`
4. `opportunity_radar_report.md`
5. `la_persistent_asset_watch_report.md`

Dashboard files:

- `dashboard_summary.csv`: one row per run with top-level metrics such as total articles, high-confidence signals, institutional-grade signals, opportunity count, distress count, LA asset watch count, top market, top sector, top GP, highest-quality signal, and recommended executive focus.
- `dashboard_cards.csv`: card-style rows with title, priority, score, market, sector, GP/developer, summary, why it matters, recommended action, source report, and URL when available.
- `dashboard_watchlists.csv`: watchlist rows grouped by category, including high-confidence signals, opportunities, distress, LA assets, GP watchlist, entitlement, lifecycle, capital flow, market entry, and source activation.
- `executive_dashboard_brief.md`: concise human-readable summary for management review.

Why this matters:

- A dashboard layer separates data preparation from UI development.
- Future frontend work can read simple CSV files instead of reconstructing strategy logic.
- Executives can review the Markdown brief immediately while the project remains a beginner-friendly single-file Python MVP.

## Refactor & Stabilization Layer

The script now includes a lightweight maintenance layer so the large single-file MVP is safer to modify before adding UI or product features.

New outputs:

```text
output/pipeline_manifest.csv
output/pipeline_manifest.md
output/pipeline_health.csv
output/pipeline_health_report.md
output/error_log.csv
output/run_summary.md
```

`pipeline_manifest.csv` and `pipeline_manifest.md` list the major output files, their category, generated status, row count or Markdown section count, short description, and recommended reader. This is the best place to check what the pipeline produced.

`pipeline_health.csv` and `pipeline_health_report.md` run simple checks:

- required output files exist
- CSV files are readable
- important expected columns are present
- important outputs are not unexpectedly empty
- the dated archive folder exists
- dashboard files and high-confidence watchlist files were generated
- the source registry has entries

Health status labels:

- `OK`: no maintenance action needed
- `Warning`: the run completed, but something should be reviewed
- `Error`: a major output or expected structure is missing
- `Not Checked`: reserved for future checks

`error_log.csv` is append-only. It records non-fatal issues such as failed feeds, placeholder sources, missing files, missing columns, and health-check warnings. The script continues running where possible.

`run_summary.md` is the short beginner-friendly close-out for each run. Open it when you want quick counts, health status, and the next file to read.

Common troubleshooting:

- If source feeds fail, open `source_health_report.md` and `source_activation_report.md`.
- If outputs are missing, open `pipeline_health_report.md`.
- If a CSV structure changed unexpectedly, check `pipeline_health.csv` for missing columns.
- If there are many placeholder sources, review `gp_source_coverage_report.md` and replace blank source URLs only when a public feed is confirmed.
- If article counts look too low, review source health first, then consider whether `MIN_RELEVANCE_SCORE` is too strict.

## Korean Executive Reporting Layer

The script can generate Korean-language executive reports for Korean executives and strategy team members while keeping all original English reports.

Settings in `news_collector.py`:

```python
GENERATE_KOREAN_REPORTS = True
USE_GPT_TRANSLATION = False
```

This version is rule-based only. It does not call OpenAI, GPT, or any paid translation API. It translates common labels, section headers, priorities, market labels, action labels, and recurring strategic phrases, then creates concise Korean executive summaries from the structured CSV data.

Korean output files:

```text
output/executive_dashboard_brief_ko.md
output/weekly_strategy_memo_ko.md
output/executive_priority_brief_ko.md
output/opportunity_radar_report_ko.md
output/distress_watchlist_report_ko.md
output/high_confidence_watchlist_report_ko.md
output/la_asset_watch_report_ko.md
output/la_entitlement_watch_report_ko.md
output/la_development_lifecycle_watch_report_ko.md
output/gp_watchlist_report_ko.md
output/korean_reporting_index.md
```

Recommended Korean reading order:

1. `executive_dashboard_brief_ko.md`
2. `executive_priority_brief_ko.md`
3. `high_confidence_watchlist_report_ko.md`
4. `opportunity_radar_report_ko.md`
5. `la_asset_watch_report_ko.md`
6. `gp_watchlist_report_ko.md`
7. `weekly_strategy_memo_ko.md`

Use cases:

- 경영진 10분 브리핑: `executive_dashboard_brief_ko.md`
- 주간 전략회의: `weekly_strategy_memo_ko.md`
- LA / California 부지 모니터링: `la_asset_watch_report_ko.md`, `la_entitlement_watch_report_ko.md`
- GP / 파트너 후보 검토: `gp_watchlist_report_ko.md`
- 리파이낸싱 / 부실 기회 검토: `distress_watchlist_report_ko.md`, `opportunity_radar_report_ko.md`
- 투자위원회 사전 검토: `executive_priority_brief_ko.md`, `high_confidence_watchlist_report_ko.md`

Limitations:

- This is not full natural-language translation.
- Company names, project names, and most market names intentionally remain in English for source matching.
- Korean summaries are generated from structured fields, so weak source data can still produce short or generic Korean bullets.
- Future GPT translation can be added later by changing `USE_GPT_TRANSLATION`, but it is intentionally off for this MVP.

CSV columns:

- `collected_at`
- `source`
- `published`
- `relevance_score`
- `priority`
- `action_level`
- `market_focus`
- `strategic_angle`
- `decision_use`
- `strategic_implication`
- `woomi_relevance`
- `recommended_next_step`
- `reason_for_inclusion`
- `market_signal`
- `extracted_numbers`
- `article_text_sample`
- `llm_analysis_prompt`
- `llm_prompt_quality_score`
- `llm_prompt_quality_label`
- `missing_prompt_context`
- `gpt_strategic_analysis`
- `topics`
- `matched_keywords`
- `title`
- `url`

## Run

```bash
python news_collector.py
```

## Beginner-Friendly Structure

The project intentionally remains a single Python file for now.

The file is organized into sections:

1. Imports and package checks
2. User settings / configuration
3. Source registry
4. Keyword dictionaries
5. Shared utility functions
6. RSS / article collection
7. Filtering and scoring
8. Entity / project canonicalization
9. Deal / asset / lifecycle extraction
10. Intelligence layer generators
11. Report writers
12. Archive / output helpers
13. Main pipeline

## Future Improvements

- Add AI summaries
- Add strategic implications for Korean developers entering the US market
- Add daily automation
- Track market-level supply and demand
- Track institutional investor and developer activity
- Add a separate configuration file once the project grows beyond MVP stage
- ## System Notes

### Automation Architecture
cron-job.org
→ GitHub workflow_dispatch
→ news_collector.py
→ output/*.csv
→ Streamlit dashboard

### Why external cron is used
GitHub scheduled cron execution was unreliable for this project.
workflow_dispatch triggered externally via cron-job.org is currently more stable.

### Streamlit behavior
Streamlit Cloud may cache CSV outputs or enter sleep mode.
If latest outputs are not reflected:
- Refresh app
- Use refresh button
- Reboot app if necessary

### CoStar Intake Policy
- No scraping
- No login automation
- No paywall bypass
- Manual CSV/XLSX intake only
