# Classification Quality Report

Generated: 2026-11-05 03:13:31

## Classification Summary

- Total articles classified: 74
- Topic distribution: development_pipeline: 14; capital_markets: 11; transaction_market: 10; gp_activity: 9; institutional_capital: 9; supply_demand: 8; other: 6; macro_financing: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 14 article(s), high 2, medium 6, low 6, unknown 0. Top markets: Other / Unknown (7); Los Angeles / California (2); Southeast (1); Miami / Florida (1); Washington DC (1).
- capital_markets: 11 article(s), high 5, medium 4, low 2, unknown 0. Top markets: New York City / New York (4); San Francisco / California (1); New York (1); Colorado (1); Las Vegas / Nevada (1).
- transaction_market: 10 article(s), high 1, medium 5, low 4, unknown 0. Top markets: Atlanta / Georgia (5); Other / Unknown (3); California (2).
- gp_activity: 9 article(s), high 0, medium 0, low 0, unknown 9. Top markets: Other / Unknown (4); Phoenix / Arizona (2); Washington DC (1); Connecticut (1); National (1).
- institutional_capital: 9 article(s), high 3, medium 2, low 4, unknown 0. Top markets: Other / Unknown (2); Los Angeles / California (1); Miami / Florida (1); Nevada (1); Southeast (1).
- supply_demand: 8 article(s), high 0, medium 0, low 8, unknown 0. Top markets: Other / Unknown (4); National (3); New York City / New York (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Los Angeles / California (3); Other / Unknown (2); San Francisco / California (1).
- macro_financing: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (3); California (1); Los Angeles / California (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: California (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- Ari Azarbarzin joins JLL Capital Markets in Washington, D.C. (Yield PRO, Washington DC): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Brookfield Gives Up DTLA's Beaudry Apartment Tower (Bisnow, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Institutional activity terms detected: private_equity_activity. Primary topic set to institutional_capital; confidence low.
- JLL Arranges Refi for Mixed-Use Residential on Long Island’s South Shore (Connect CRE, New York): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- 377 apartments rise next to Brea Mall (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Housing pitched for 5412 Bellingham Ave. in Valley Village (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Boutique Arlington Heights Apartments Sell for $25M (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Affordable housing taking shape at 5749 S. Brynhurst Avenue in Hyde Park (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- One Beverly Hills Reaches Milestones Ahead of Schedule (Connect CRE Apartments, Los Angeles / California): Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Ware Malcomb Completes Historic Residential Conversion in Downtown Chicago (Connect CRE Apartments, Other / Unknown): Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Leon Multifamily Building 343-Unit N. Phoenix Venture (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Marcus & Millichap Closes $29.85M Sale and Arranges Financing for Two Multifamily Assets in West Hollywood (Yield PRO, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Origin, Mill Creek Teaming Up on 190-Unit Scottsdale Rental Community (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- 123 homes planned at 902 W. Washington Blvd. in University Park (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Preliminary Plans For 49-Story Skyscraper at 501 Brannan Street, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- CSU Dominguez Hills completes new dorms + rec center (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Investor Takes Over Distressed Atlanta Apartment Asset (Connect CRE Atlanta, Atlanta / Georgia): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Additional low/unknown rows omitted: 26

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.