# Classification Quality Report

Generated: 2026-11-03 03:51:47

## Classification Summary

- Total articles classified: 78
- Topic distribution: development_pipeline: 15; transaction_market: 15; capital_markets: 13; gp_activity: 11; supply_demand: 7; institutional_capital: 5; other: 5; macro_financing: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 15 article(s), high 1, medium 6, low 8, unknown 0. Top markets: Other / Unknown (6); Miami / Florida (2); Los Angeles / California (2); Los Angeles (1); California (1).
- transaction_market: 15 article(s), high 1, medium 8, low 6, unknown 0. Top markets: Other / Unknown (6); Atlanta / Georgia (4); California (3); Seattle (1); Denver / Colorado (1).
- capital_markets: 13 article(s), high 5, medium 6, low 2, unknown 0. Top markets: New York City / New York (5); Other / Unknown (2); New York (1); Seattle (1); Dallas / Texas (1).
- gp_activity: 11 article(s), high 0, medium 0, low 1, unknown 10. Top markets: Other / Unknown (5); Phoenix / Arizona (2); Atlanta / Georgia (1); Connecticut (1); Georgia (1).
- supply_demand: 7 article(s), high 0, medium 0, low 7, unknown 0. Top markets: Other / Unknown (4); National (2); Georgia (1).
- institutional_capital: 5 article(s), high 1, medium 2, low 2, unknown 0. Top markets: Other / Unknown (2); New York (1); Riverside / California (1); Atlanta / Georgia (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (3); Santa Monica / California (1); California (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (4).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: California (2); Other / Unknown (1).

## Low Confidence / Unknown Articles

- Muirfield Breaks Ground on Orlando-Area Opportunity Zone Multifamily Development (Yield PRO, Los Angeles): Development-stage terms detected: construction_start, delivery. Primary topic set to development_pipeline; confidence low.
- Housing pitched for 5412 Bellingham Ave. in Valley Village (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Fresh renderings for Tishman Speyer projects in Downtown Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing underway at 5403 S. Inglewood Blvd. in Del Rey (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 37-unit affordable housing complex underway at 3751 S. Delmas Ter. in Palms (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Dwight Capital Provides $23.5M HUD-Insured Refinancing for Northern New Jersey Apartment Complex (REBusiness Online, New York City / New York): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Northmarq Brokers Sale of Newly Built Class A Multifamily Property in Lawrence Kansas (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Kidder Mathews Arranges Sale of 45-Unit Multifamily in Walla Walla (Connect CRE, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Modular Apartment Complex Proposed for 3070 Brook Street, Oakland (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Marcus & Millichap Brokers $13.6M Sale of 63-Unit Multifamily Property in Davis California (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Leon Multifamily Building 343-Unit N. Phoenix Venture (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Bascom Group Obtains $30.8M Refinancing for 200-Unit Multifamily Community in Las Vegas (REBusiness Online, Las Vegas / Nevada): Capital event keywords detected: refinancing, acquisition. Primary topic set to capital_markets; confidence low.
- New Student Housing Towers Lease Up Quickly In University City, But Developers Can't Build More (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: lease_up. Primary topic set to development_pipeline; confidence low.
- ARCTRUST, Edison Equity Teaming Up on 175-Unit Austin-Area 55+ Community (Connect CRE Texas, Austin / Texas): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Golden Apartment Building Sells For $62M To Chicago Company (Bisnow, Denver / Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: disposition. Institutional activity terms detected: gp_disposition. Primary topic set to transaction_market; confidence low.
- Origin, Mill Creek Teaming Up on 190-Unit Scottsdale Rental Community (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 28

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.