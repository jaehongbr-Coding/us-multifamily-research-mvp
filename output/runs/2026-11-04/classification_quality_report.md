# Classification Quality Report

Generated: 2026-11-04 02:56:26

## Classification Summary

- Total articles classified: 70
- Topic distribution: development_pipeline: 14; transaction_market: 14; gp_activity: 10; institutional_capital: 8; supply_demand: 8; other: 6; capital_markets: 5; macro_financing: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 14 article(s), high 1, medium 5, low 8, unknown 0. Top markets: Other / Unknown (6); Los Angeles / California (3); Los Angeles (1); Sun Belt (1); Miami / Florida (1).
- transaction_market: 14 article(s), high 2, medium 5, low 7, unknown 0. Top markets: Atlanta / Georgia (5); California (3); Other / Unknown (2); Seattle (2); New York City / New York (1).
- gp_activity: 10 article(s), high 0, medium 0, low 0, unknown 10. Top markets: Other / Unknown (4); Phoenix / Arizona (2); Washington DC (1); Connecticut (1); Georgia (1).
- institutional_capital: 8 article(s), high 2, medium 4, low 2, unknown 0. Top markets: Other / Unknown (2); Miami / Florida (2); New York (1); Riverside / California (1); New York City / New York (1).
- supply_demand: 8 article(s), high 0, medium 0, low 8, unknown 0. Top markets: Other / Unknown (4); National (4).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Los Angeles / California (3); Santa Monica / California (1); San Francisco / California (1); Other / Unknown (1).
- capital_markets: 5 article(s), high 2, medium 2, low 1, unknown 0. Top markets: New York City / New York (2); Austin / Texas (1); Phoenix / Arizona (1); Other / Unknown (1).
- macro_financing: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Other / Unknown (3).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: California (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- Muirfield Breaks Ground on Orlando-Area Opportunity Zone Multifamily Development (Yield PRO, Los Angeles): Development-stage terms detected: construction_start, delivery. Primary topic set to development_pipeline; confidence low.
- Housing pitched for 5412 Bellingham Ave. in Valley Village (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Fresh renderings for Tishman Speyer projects in Downtown Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Howard University, Developers Break Ground on 11-Story Multifamily Development in D.C. (REBusiness Online, Washington DC): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Northmarq Brokers Sale of Newly Built Class A Multifamily Property in Lawrence Kansas (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- One Beverly Hills Reaches Milestones Ahead of Schedule (Connect CRE, Los Angeles / California): Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Affordable housing taking shape at 5749 S. Brynhurst Avenue in Hyde Park (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Kraus-Anderson Completes Conversion of Wisconsin Hotel into 146 Affordable Housing Units (REBusiness Online, Other / Unknown): Development-stage terms detected: delivery, renovation_repositioning, adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Marcus & Millichap Brokers $13.6M Sale of 63-Unit Multifamily Property in Davis California (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Kidder Mathews Arranges Sale of 45-Unit Multifamily in Walla Walla (Connect CRE Apartments, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Leon Multifamily Building 343-Unit N. Phoenix Venture (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- ARCTRUST, Edison Equity Teaming Up on 175-Unit Austin-Area 55+ Community (Connect CRE Texas, Austin / Texas): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Origin, Mill Creek Teaming Up on 190-Unit Scottsdale Rental Community (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Preliminary Plans For 49-Story Skyscraper at 501 Brannan Street, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- CSU Dominguez Hills completes new dorms + rec center (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Investor Takes Over Distressed Atlanta Apartment Asset (Connect CRE Atlanta, Atlanta / Georgia): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Additional low/unknown rows omitted: 27

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.