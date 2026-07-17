# Source Recovery Report

Generated: 2026-07-17 00:00:57

## Summary

- Sources reviewed: 163
- Failing attempted sources: 16
- Focus sources reviewed: 11

## Focus Source Status

| source_name | rss_url | status | error_type | last_success_date | last_article_count | fallback | recovery_recommendation |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| GlobeSt | https://www.globest.com/feed/ | Failed | rss_not_found |  | 0 | homepage reachable | RSS feed failed, but fallback page is reachable; consider source-specific parser or sitemap ingestion. |
| Connect CRE | https://www.connectcre.com/feed/ | OK |  | 2026-07-17 | 3 |  | Manual source review needed. |
| The Real Deal | https://therealdeal.com/feed/ | Failed | rss_changed |  | 0 | source page reachable | RSS feed failed, but fallback page is reachable; consider source-specific parser or sitemap ingestion. |
| Connect CRE Apartments | https://www.connectcre.com/feed?property-sector=apartments | OK |  | 2026-07-17 | 8 |  | Manual source review needed. |
| Connect CRE Texas | https://www.connectcre.com/feed?story-market=texas | OK |  | 2026-07-17 | 2 |  | Manual source review needed. |
| Connect CRE South Florida | https://www.connectcre.com/feed?story-market=south-florida | OK |  | 2026-07-17 | 6 |  | Manual source review needed. |
| Connect CRE Phoenix | https://www.connectcre.com/feed?story-market=phoenix | OK |  | 2026-07-17 | 2 |  | Manual source review needed. |
| Connect CRE Atlanta | https://www.connectcre.com/feed?story-market=atlanta | OK |  | 2026-07-17 | 3 |  | Manual source review needed. |
| Connect CRE Charlotte | https://www.connectcre.com/feed?story-market=charlotte | Failed | rss_not_found |  | 0 | no reliable fallback found | Replace the feed URL; current RSS endpoint appears unavailable. |
| Connect CRE Orange County | https://www.connectcre.com/feed?story-market=orange-county | OK |  | 2026-07-17 | 3 |  | Manual source review needed. |
| Connect CRE California | https://www.connectcre.com/feed?story-market=california | OK |  | 2026-07-17 | 5 |  | Manual source review needed. |

## High-Importance Failures

| source_name | status | error_type | GP/Capital | Development | Market | fallback | recommendation |
| --- | --- | --- | ---: | ---: | ---: | --- | --- |
| Berkadia Source Expansion | Failed | rss_changed | 100 | 15 | 37 | homepage reachable | RSS feed failed, but fallback page is reachable; consider source-specific parser or sitemap ingestion. |
| Walker & Dunlop Source Expansion | Failed | rss_changed | 100 | 15 | 37 | homepage reachable | RSS feed failed, but fallback page is reachable; consider source-specific parser or sitemap ingestion. |
| Walker & Dunlop Insights | Failed | rss_changed | 83 | 15 | 51 | homepage reachable | RSS feed failed, but fallback page is reachable; consider source-specific parser or sitemap ingestion. |
| Berkadia Research | Failed | rss_changed | 83 | 15 | 51 | homepage reachable | RSS feed failed, but fallback page is reachable; consider source-specific parser or sitemap ingestion. |
| Blackstone Real Estate Source Expansion | Failed | paywall_restricted | 83 | 15 | 37 | source page reachable | RSS feed failed, but fallback page is reachable; consider source-specific parser or sitemap ingestion. |
| Hines Source Expansion | Failed | paywall_restricted | 83 | 15 | 37 | no reliable fallback found | Do not scrape restricted content; use public RSS, summary pages, or manual intake only. |
| California YIMBY | Failed | feed_parse_error | 8 | 80 | 8 | no reliable fallback found | Inspect feed format; may require alternate feed URL or tolerant XML parsing. |
| Hines Newsroom | Failed | paywall_restricted | 68 | 0 | 0 | no reliable fallback found | Do not scrape restricted content; use public RSS, summary pages, or manual intake only. |
| Blackstone Real Estate | Failed | paywall_restricted | 68 | 0 | 0 | source page reachable | RSS feed failed, but fallback page is reachable; consider source-specific parser or sitemap ingestion. |
| Connect CRE Charlotte | Failed | rss_not_found | 40 | 68 | 8 | no reliable fallback found | Replace the feed URL; current RSS endpoint appears unavailable. |
| Commercial Property Executive | Failed | paywall_restricted | 37 | 39 | 67 | no reliable fallback found | Do not scrape restricted content; use public RSS, summary pages, or manual intake only. |
| Urban Land Institute | Failed | paywall_restricted | 55 | 15 | 37 | not probed | Do not scrape restricted content; use public RSS, summary pages, or manual intake only. |
| NMHC News | Failed | feed_parse_error | 55 | 15 | 37 | not probed | Inspect feed format; may require alternate feed URL or tolerant XML parsing. |
| Multi-Housing News | Failed | paywall_restricted | 15 | 15 | 45 | not probed | Do not scrape restricted content; use public RSS, summary pages, or manual intake only. |
| GlobeSt | Failed | rss_not_found | 29 | 15 | 45 | homepage reachable | RSS feed failed, but fallback page is reachable; consider source-specific parser or sitemap ingestion. |
| The Real Deal | Failed | rss_changed | 29 | 15 | 45 | source page reachable | RSS feed failed, but fallback page is reachable; consider source-specific parser or sitemap ingestion. |

## Failure Type Guide

- `rss_not_found`: configured RSS endpoint appears unavailable.
- `rss_changed`: redirects or source changes suggest the feed URL may have moved.
- `feed_parse_error`: feedparser could not parse the configured feed.
- `html_structure_changed`: configured feed may now return HTML or a changed page structure.
- `paywall_restricted`: access appears restricted; use public feeds or manual intake only.
- `robots_restricted`: do not bypass; use permitted public paths only.
- `timeout`: retry/backoff may help, but the collector remains isolated.
- `unknown`: manual source review needed.

## Recovery Notes

- RSS recovery should prefer official public RSS feeds, sitemap XML, or public category pages.
- Do not automate login, bypass paywalls, or ignore robots restrictions.
- If fallback pages are reachable, add source-specific parsers only after confirming stable public article links.