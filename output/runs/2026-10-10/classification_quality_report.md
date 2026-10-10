# Classification Quality Report

Generated: 2026-10-10 02:08:35

## Classification Summary

- Total articles classified: 76
- Topic distribution: development_pipeline: 17; transaction_market: 16; supply_demand: 12; capital_markets: 9; macro_financing: 6; gp_activity: 5; other: 5; institutional_capital: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 17 article(s), high 1, medium 6, low 10, unknown 0. Top markets: Other / Unknown (6); National (3); Los Angeles / California (2); Phoenix / Arizona (2); California (1).
- transaction_market: 16 article(s), high 2, medium 10, low 4, unknown 0. Top markets: Atlanta / Georgia (4); Los Angeles / California (2); California (2); Other / Unknown (2); Seattle (2).
- supply_demand: 12 article(s), high 0, medium 1, low 11, unknown 0. Top markets: Other / Unknown (7); Miami / Florida (2); National (2); Houston / Texas (1).
- capital_markets: 9 article(s), high 2, medium 4, low 3, unknown 0. Top markets: Dallas / Texas (2); Miami / Florida (2); Washington DC (1); Florida (1); California (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Tennessee (2); Other / Unknown (2); Los Angeles / California (1); National (1).
- gp_activity: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (3); Atlanta / Georgia (1); National (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: San Francisco / California (3); Los Angeles / California (1); California (1).
- institutional_capital: 4 article(s), high 0, medium 3, low 1, unknown 0. Top markets: Washington DC (2); Miami / Florida (2).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); Santa Monica / California (1).

## Low Confidence / Unknown Articles

- Completion nears for mixed-use project at 10608 Pico Blvd. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Senior housing completed at 14513 Central Avenue in Baldwin Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- First phase of housing and healthcare campus commences at 800 N. Main St. in Chinatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- LAUSD board moves forward with plans for housing at sites in West Hollywood and Woodland Hills (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Rendering vs. Reality: Affordable housing at 1400 Long Beach Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Mixed-use project slated to replace Mel's Drive-In in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 388 apartments to replace offices at 3200 E. Carson St. in Lakewood (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing completed at 7220 Maie Avenue in Florence-Firestone (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Plans Revealed For 228 Collins Street in Inner Richmond, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Updated Renderings For 360 5th Street in SoMa, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- JLL Arranges Loan for Refinancing of 300-Unit Apartment Community in Northwest Dallas (REBusiness Online, Dallas / Texas): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Development Group Starts Work on 371-Unit Boynton Beach Multifamily Venture (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Related Affiliate Obtains $167M Loan Package for Miami Apartment Community (Connect CRE South Florida, Miami / Florida): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- LOCAL on Delmar Mixed-Use Community Opens in Suburban St. Louis (REBusiness Online, National): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Governor Kathy Hochul Announces the Completion New Affordable Housing for Seniors in Suffolk County (Yield PRO, New York): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Germantown Developer Reveals Schedule for Mixed-Use Project (Connect CRE Apartments, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Colliers Brokers $18M Sale of 88-Unit Multifamily in Seattle’s Roosevelt Neighborhood (Connect CRE, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 27

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.