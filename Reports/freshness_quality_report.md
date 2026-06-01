# Freshness Quality Report

Generated: 2026-06-01 09:31:33

## Freshness Summary

- Total articles reviewed: 35
- fresh_0_3d: 22
- recent_4_14d: 9
- stale_15_30d: 2
- old_31d_plus: 2
- unknown_date: 0

## Old Articles Excluded From Representative Evidence

- Centralization Associated with Occupancy Uplift (Multifamily Executive, 2026-03-02): published date parsed; article age 91 day(s)
- Investment, NOI, and Covenants: Managing the risks (Multifamily Executive, 2026-05-01): published date parsed; article age 31 day(s)

## Old Articles Excluded From Development Activity Top Exposure

- No 31d+ development article is expected to rank in top current exposure after score penalty.

## Old Articles Excluded From GP / Capital Activity

- Investment, NOI, and Covenants: Managing the risks (Multifamily Executive): repeat exposure penalty; low relevance or thin evidence; historical article over 30 days old

## Unknown Date Articles

- No articles had unparseable published dates.

## Sources With Stale / Unknown Dates

- Multifamily Executive: 3 stale/old/unknown-date article(s)
- Blackstone Real Estate: 1 stale/old/unknown-date article(s)

## Recommended Source / Date Parsing Fixes

- Review sources with repeated `unknown_date` rows and confirm whether RSS entries expose `published` or `updated` fields.
- Treat 31d+ articles as historical/background context unless they are explicit follow-up items.
- Keep articles in `articles.csv`, but suppress old rows from current evidence, development, GP/capital, and market signal top exposure.
- If a source backfills old articles into RSS, prefer collected-date only as a fallback and keep the article in review status.