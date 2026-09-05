# Classification Quality Report

Generated: 2026-09-05 00:38:52

## Classification Summary

- Total articles classified: 82
- Topic distribution: transaction_market: 18; development_pipeline: 16; supply_demand: 11; capital_markets: 10; gp_activity: 10; macro_financing: 7; institutional_capital: 5; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 18 article(s), high 5, medium 6, low 7, unknown 0. Top markets: California (3); Atlanta / Georgia (3); Seattle (2); Other / Unknown (2); National (1).
- development_pipeline: 16 article(s), high 1, medium 5, low 10, unknown 0. Top markets: Other / Unknown (3); Atlanta / Georgia (3); Los Angeles / California (2); New York (1); New York City / New York (1).
- supply_demand: 11 article(s), high 0, medium 1, low 10, unknown 0. Top markets: Other / Unknown (6); National (3); Colorado (1); New York City / New York (1).
- capital_markets: 10 article(s), high 4, medium 5, low 1, unknown 0. Top markets: Miami / Florida (3); Washington DC (1); Sun Belt (1); Dallas / Texas (1); California (1).
- gp_activity: 10 article(s), high 0, medium 0, low 1, unknown 9. Top markets: Other / Unknown (3); New York City / New York (1); Atlanta / Georgia (1); Phoenix / Arizona (1); Dallas / Texas (1).
- macro_financing: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Los Angeles / California (2); Other / Unknown (2); Dallas / Texas (1); California (1); Atlanta / Georgia (1).
- institutional_capital: 5 article(s), high 2, medium 0, low 3, unknown 0. Top markets: California (2); Virginia (1); National (1); Kentucky (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: California (1); Other / Unknown (1); Los Angeles / California (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: California (1); Los Angeles / California (1).

## Low Confidence / Unknown Articles

- Apartment cap rates inched up to 5.6% in July: MSCI (Multifamily Dive, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Walker & Dunlop Arranges $142M HUD Financing for Two Virginia Multifamily Construction Projects on Behalf of Bonaventure (Yield PRO, Virginia): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- IPA Capital Markets Arranges $40.3M Financing for 312-Unit Multifamily Apartment Community Birwood Heights in San Antonio (Yield PRO, Dallas / Texas): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Gaia Lands Another Extension for Williamsburg Apartments’ $48M Loan (Commercial Observer, New York City / New York): Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- Developer Ailanthus Files Plans to Build 400 Apartments at 424 Hoyt Street in Gowanus (Commercial Observer, New York City / New York): Development-stage terms detected: zoning. Primary topic set to development_pipeline; confidence low.
- Mixed-use project rises at 1801 E. 4th St. in Santa Ana (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Rendering vs. Reality: Apartments at 1408 W. Jefferson Blvd. in Exposition Park (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 200 apartments fully framed at 3863 Carson Street in Torrance (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affordable housing under construction at 14243 Sylvan St. in Van Nuys (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- L.A. County approves up to $20M for affordable housing in Claremont (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Construction begins for mixed-use project at 11905 Wilshire Blvd. in Brentwood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- JLL Arranges $78.7M Loan for Refinancing of East Dallas Apartment Community (REBusiness Online, Dallas / Texas): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Cushman & Wakefield Brokers Sale of 280-Unit Oswego Apartment Property (Connect CRE Apartments, National): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Camden Pays $88.6M for Nashville Apartment Highrise (Connect CRE Apartments, Atlanta / Georgia): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Wood Partners Breaks Ground on All-Electric Community Near Boston (Connect CRE Apartments, National): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Partnership Underway on Seniors Housing Project in East Brunswick, New Jersey (REBusiness Online, National): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Miami-Dade Public Agency Advancing $126.4M Affordable Housing Project (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- What multifamily firms bought and sold this summer (Multifamily Dive, Riverside / California): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- MBK Sells Anaheim Apartments To TA Realty For $147M (Bisnow, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: disposition. Institutional activity terms detected: gp_disposition. Primary topic set to transaction_market; confidence low.
- Additional low/unknown rows omitted: 33

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.