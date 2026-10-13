# Classification Quality Report

Generated: 2026-10-13 03:24:23

## Classification Summary

- Total articles classified: 79
- Topic distribution: transaction_market: 19; development_pipeline: 17; capital_markets: 13; supply_demand: 9; gp_activity: 6; macro_financing: 6; other: 6; institutional_capital: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 19 article(s), high 3, medium 8, low 8, unknown 0. Top markets: Other / Unknown (4); California (4); Atlanta / Georgia (4); Seattle (3); Austin / Texas (2).
- development_pipeline: 17 article(s), high 1, medium 5, low 11, unknown 0. Top markets: Other / Unknown (6); California (3); Los Angeles / California (2); Houston / Texas (1); Phoenix / Arizona (1).
- capital_markets: 13 article(s), high 7, medium 3, low 3, unknown 0. Top markets: Miami / Florida (3); Other / Unknown (3); National (1); Florida (1); Washington DC (1).
- supply_demand: 9 article(s), high 0, medium 0, low 9, unknown 0. Top markets: Other / Unknown (6); National (2); Miami / Florida (1).
- gp_activity: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (3); New York (1); National (1); San Francisco / California (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (3); Colorado (1); Los Angeles / California (1); Tennessee (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Los Angeles / California (3); San Francisco / California (3).
- institutional_capital: 3 article(s), high 0, medium 3, low 0, unknown 0. Top markets: Washington DC (1); Miami / Florida (1); Riverside / California (1).

## Low Confidence / Unknown Articles

- Northmarq Secures $50M Refinancing of Multifamily Asset in MN (Connect CRE, National): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- New look for Westwood housing complex at 11027 W. Strathmore Dr. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing secures financing at 1756 Colorado Blvd. in Pasadena (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Completion nears for mixed-use project at 10608 Pico Blvd. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Senior housing completed at 14513 Central Avenue in Baldwin Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- First phase of housing and healthcare campus commences at 800 N. Main St. in Chinatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- LAUSD board moves forward with plans for housing at sites in West Hollywood and Woodland Hills (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Plans Revealed For 228 Collins Street in Inner Richmond, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- PCD Receives Approval for 120-Acre Mixed-Use Development in Pearland, Texas (REBusiness Online, Houston / Texas): Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Revere Beach Apartments Sell For $77M (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: disposition. Institutional activity terms detected: gp_disposition. Primary topic set to transaction_market; confidence low.
- Development Group Starts Work on 371-Unit Boynton Beach Multifamily Venture (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Marcus & Millichap Arranges Sale of New Multifamily Townhome Property in Southern California (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Marcus & Millichap Brokers $5.9M Sale of 23-Unit Multifamily Property in Upland Californi (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Alta Housing Breaks Ground on 108-Unit Affordable Housing Community in Mountain View, California (REBusiness Online, California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Catholic Charities Cuts Ribbon on $143M Affordable Seniors Housing in Brownsville (Connect CRE, New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Institutional Property Advisors Completes Two Multifamily Sales in the South Puget Sound Region (Yield PRO, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Pair Of Evanston Apartment Buildings Trade Hands, Including A Reinsdorf-Backed Sale (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- PREMIER Design + Build Launches Adaptive Reuse at Merritt 7 Complex (Connect CRE Apartments, New York): Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 29

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.