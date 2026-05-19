# Streamlit Cloud Pilot Deployment

This project is designed for a simple pilot deployment:

- `news_collector.py` runs once every morning in GitHub Actions.
- Updated files under `output/` are committed back to the repository.
- Streamlit Cloud serves `app.py` and reads the latest committed output files.
- The app does not run the collector on each page load.

## Local Run

Refresh the intelligence outputs:

```bash
python news_collector.py
```

Open the Streamlit app:

```bash
python -m streamlit run app.py
```

## GitHub Push

After local verification:

```bash
git add .
git commit -m "Prepare Streamlit dashboard for deployment"
git push
```

## Streamlit Cloud Deployment

1. Push this repository to GitHub.
2. Go to Streamlit Community Cloud.
3. Create a new app from the GitHub repository.
4. Set **Main file path** to:

```text
app.py
```

5. Confirm `requirements.txt` is detected.
6. Deploy the app.
7. Share the Streamlit app URL with the pilot team.

## Daily Refresh

The workflow file is:

```text
.github/workflows/daily_news_collector.yml
```

It runs every day at 8:00 AM Korea time, which is 23:00 UTC on the previous day.

The workflow:

1. Installs dependencies from `requirements.txt`.
2. Runs `python news_collector.py`.
3. Commits updated `output/` files.
4. Pushes the update to GitHub.

Streamlit Cloud then reads the latest committed output files.

## Manual Refresh

To refresh outside the schedule:

1. Open the GitHub repository.
2. Go to **Actions**.
3. Select **Daily News Collector**.
4. Click **Run workflow**.

## Output Structure

Latest app-facing files stay directly under:

```text
output/
```

Dated run snapshots are stored under:

```text
output/runs/YYYY-MM-DD/
```

Each dated run folder includes:

```text
run_manifest.json
```

The manifest records `run_id`, `run_date`, `run_timestamp`, article counts, duplicate counts, and generated output files.

Long-term memory files such as `regime_history.csv` and `regime_timeline.csv` append run-level records over time.

## Mobile Usage

Open the deployed Streamlit URL in a phone browser. The app is optimized for a concise pilot briefing flow:

1. 오늘의 브리핑
2. 시장 인텔리전스
3. 최근 개발 Activity
4. GP / 자본 동향
5. 기사 모음

## Known Limitations

- No login or authentication is included yet.
- No database is used.
- No paid APIs are required.
- Streamlit Cloud displays the latest files committed to GitHub.
- If `output/` files are missing, the app shows friendly missing-file messages instead of crashing.

## Troubleshooting

If the deployed app looks stale:

1. Check the latest GitHub Actions run.
2. Confirm updated files were committed under `output/`.
3. Reboot the Streamlit Cloud app if needed.

If the GitHub Actions run fails:

1. Open the failed workflow logs.
2. Confirm dependencies in `requirements.txt`.
3. Run `python news_collector.py` locally to reproduce the issue.

If Korean text renders incorrectly:

1. Confirm files are saved as UTF-8.
2. Avoid editing Markdown outputs in tools that change file encoding.
3. Re-run `python news_collector.py` and commit the regenerated files.
