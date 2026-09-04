# Classification Quality Report

Generated: 2026-09-04 00:49:55

## Classification Summary

- Total articles classified: 85
- Topic distribution: transaction_market: 17; capital_markets: 14; development_pipeline: 13; gp_activity: 12; supply_demand: 10; institutional_capital: 7; macro_financing: 6; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 17 article(s), high 4, medium 6, low 7, unknown 0. Top markets: California (3); Atlanta / Georgia (3); Austin / Texas (2); Other / Unknown (2); West Palm Beach / Florida (1).
- capital_markets: 14 article(s), high 6, medium 8, low 0, unknown 0. Top markets: Miami / Florida (3); Other / Unknown (2); California (2); Washington DC (1); Sun Belt (1).
- development_pipeline: 13 article(s), high 0, medium 4, low 9, unknown 0. Top markets: Atlanta / Georgia (4); Other / Unknown (3); New York (1); Los Angeles / California (1); Miami / Florida (1).
- gp_activity: 12 article(s), high 0, medium 0, low 0, unknown 12. Top markets: Other / Unknown (3); National (2); Atlanta / Georgia (1); Phoenix / Arizona (1); Dallas / Texas (1).
- supply_demand: 10 article(s), high 0, medium 1, low 9, unknown 0. Top markets: Other / Unknown (6); National (2); Colorado (1); Dallas / Texas (1).
- institutional_capital: 7 article(s), high 2, medium 1, low 4, unknown 0. Top markets: California (3); Virginia (1); New York (1); Kentucky (1); National (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (2); Dallas / Texas (1); California (1); Los Angeles / California (1); Atlanta / Georgia (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); San Francisco / California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (3).

## Low Confidence / Unknown Articles

- Apartment cap rates inched up to 5.6% in July: MSCI (Multifamily Dive, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Walker & Dunlop Arranges $142M HUD Financing for Two Virginia Multifamily Construction Projects on Behalf of Bonaventure (Yield PRO, Virginia): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- IPA Capital Markets Arranges $40.3M Financing for 312-Unit Multifamily Apartment Community Birwood Heights in San Antonio (Yield PRO, Dallas / Texas): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- 200 apartments fully framed at 3863 Carson Street in Torrance (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affordable housing under construction at 14243 Sylvan St. in Van Nuys (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- L.A. County approves up to $20M for affordable housing in Claremont (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Construction begins for mixed-use project at 11905 Wilshire Blvd. in Brentwood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Rendering vs. Reality: Affordable housing at 1201 N. Detroit St. in West Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- L.A.'s new build apartments are shrinking (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Rendering vs. Reality: Mixed-use complex at 3900 S. Figueroa St. in Expo Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- JLL Secures $76.3M in Financing for Luxury Apartment Development in West St. Paul (REBusiness Online, National): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Miami-Dade Public Agency Advancing $126.4M Affordable Housing Project (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- City Opens Housing Lottery for 227 South Bronx Apartments (Connect CRE Apartments, Atlanta / Georgia): Development-stage terms detected: under_construction, delivery. Primary topic set to development_pipeline; confidence low.
- Holladay, Urban League Open East Nashville Affordable Housing Community (REBusiness Online, Nashville / Tennessee): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Passco Sells Buckhead Apartment Complex: The Atlanta Deal Sheet (Bisnow, Atlanta / Georgia): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: disposition. Institutional activity terms detected: gp_disposition. Primary topic set to transaction_market; confidence low.
- Ridge Capital Offloads Two Ukiah Apartment Complexes (Connect CRE California, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- What multifamily firms bought and sold this summer (Multifamily Dive, Riverside / California): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- HMF Americana Developing Charlotte Mixed-Use Community (Connect CRE Apartments, Atlanta / Georgia): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Meeting Scheduled for New Apartments at 2051 Market Street in San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Additional low/unknown rows omitted: 33

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.