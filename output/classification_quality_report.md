# Classification Quality Report

Generated: 2026-11-24 06:47:56

## Classification Summary

- Total articles classified: 72
- Topic distribution: transaction_market: 15; capital_markets: 11; institutional_capital: 10; supply_demand: 9; development_pipeline: 8; gp_activity: 7; other: 5; macro_financing: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 15 article(s), high 3, medium 7, low 5, unknown 0. Top markets: Other / Unknown (3); Atlanta / Georgia (3); Miami / Florida (2); Virginia (1); Northern Virginia / Virginia (1).
- capital_markets: 11 article(s), high 8, medium 3, low 0, unknown 0. Top markets: Miami / Florida (3); New York City / New York (2); National (2); Other / Unknown (1); Sun Belt (1).
- institutional_capital: 10 article(s), high 2, medium 5, low 3, unknown 0. Top markets: California (2); Phoenix / Arizona (2); Seattle (2); Northern Virginia / Virginia (1); National (1).
- supply_demand: 9 article(s), high 0, medium 0, low 9, unknown 0. Top markets: National (5); Other / Unknown (3); Houston / Texas (1).
- development_pipeline: 8 article(s), high 0, medium 3, low 5, unknown 0. Top markets: Other / Unknown (6); Los Angeles / California (1); Phoenix / Arizona (1).
- gp_activity: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Other / Unknown (4); Los Angeles / California (1); New York City / New York (1); National (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (2); Denver / Colorado (1); National (1); Austin / Texas (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (2); Miami / Florida (1); California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Santa Monica / California (1); Los Angeles / California (1); Southeast (1).

## Low Confidence / Unknown Articles

- Denver Multifamily Rents Expected To Remain Below National Average In 2027 (Bisnow, Denver / Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Namdar Lands $345M Loan To Build Brickell Apartments: The South Florida Deal Sheet (Bisnow, Miami / Florida): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- REIT Sells 400-Unit Arlandria Apartment Community For $69M (Bisnow, Northern Virginia / Virginia): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: disposition. Institutional activity terms detected: reit_activity, gp_disposition. Primary topic set to transaction_market; confidence low.
- Santa Monica has new plans for affordable housing next to Downtown Metro stop (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Mixed-use project reaches its peak at at 6052 W. Olympic Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Developers seek bond financing for affordable housing in the Valley (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- City Council upholds approval of apartments at 2413 Silver Lake Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Mixed-use project starts to rise at 3313 Sunset Blvd. in Silver Lake (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Northmarq Arranges $75M Sale, $49M Financing of Milwaukee Multifamily (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- New plan for housing at 4600 Wilshire Blvd. (Urbanize LA, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Approval For 355-415 East Middlefield Road, Mountain View (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- U.S. Apartment Construction Starts Reach 14-Year Quarterly Low (Connect CRE Apartments, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Work Gets Started on Carlsbad Village Mixed-Use Project (Connect CRE California, California): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- How apartment developers can successfully install connected services (Multifamily Dive, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily starts rose in October amid high borrowing, materials costs (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Weidner Apartment Homes Spends $91M on Denver Apartment Property (Connect CRE, Phoenix / Arizona): Capital event keywords detected: joint_venture, acquisition. Primary topic set to institutional_capital; confidence low.
- Garden Communities Progresses with West Hartford Multifamily Development (Connect CRE, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Construction Underway At 2138 Kittredge Street, Downtown Berkeley (SF YIMBY, Austin / Texas): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Additional low/unknown rows omitted: 21

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.