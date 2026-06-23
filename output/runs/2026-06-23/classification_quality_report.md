# Classification Quality Report

Generated: 2026-06-23 23:58:39

## Classification Summary

- Total articles classified: 76
- Topic distribution: development_pipeline: 17; transaction_market: 14; gp_activity: 11; supply_demand: 11; capital_markets: 10; other: 5; macro_financing: 4; institutional_capital: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 17 article(s), high 2, medium 6, low 9, unknown 0. Top markets: Los Angeles / California (4); California (3); Other / Unknown (3); Miami / Florida (1); Phoenix / Arizona (1).
- transaction_market: 14 article(s), high 3, medium 10, low 1, unknown 0. Top markets: California (5); Other / Unknown (2); Phoenix / Arizona (2); Los Angeles / California (1); Seattle (1).
- gp_activity: 11 article(s), high 0, medium 0, low 3, unknown 8. Top markets: Phoenix / Arizona (3); National (3); California (2); Other / Unknown (1); Houston / Texas (1).
- supply_demand: 11 article(s), high 0, medium 1, low 10, unknown 0. Top markets: Other / Unknown (7); National (4).
- capital_markets: 10 article(s), high 5, medium 4, low 1, unknown 0. Top markets: New York City / New York (2); New York (2); Florida (1); Texas (1); Miami / Florida (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Santa Monica / California (1); Los Angeles / California (1); Beverly Hills / California (1); San Francisco / California (1); Other / Unknown (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (3); Los Angeles / California (1).
- institutional_capital: 2 article(s), high 0, medium 0, low 2, unknown 0. Top markets: San Francisco / California (1); Other / Unknown (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: California (1); Beverly Hills / California (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Affordable housing takes shape at 733 S. Burlington Ave. in Westlake (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Linc Housing plans new project at 3590 Elm Ave. in Long Beach (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Work beginning for Taix redevelopment at 1911 Sunset Blvd. in Echo Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Adaptive reuse project gets colorful new exterior at 3325 Wilshire Blvd. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- New plan for apartments at 745 17th Street in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Measure ULA reform goes to the ballot, Remembering Lorcan O'Herlihy, and more (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Mixed-use project could replace Beverly Hills gas station at 8555 Wilshire Blvd. (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Infill housing in progress at 3676 S. Kelton Ave. in Palms (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Newmark Arranges $52M Refi for Cypress Apartment Owner (Connect CRE Apartments, Houston / Texas): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Work Underway on Student Housing Multifamily Development La Cantera Crossing in San Antonio Texas Near UTSA Campus (Yield PRO, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Meeting Tomorrow At 906 Clement Street, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Zilber Opens Roseville Multifamily with Cottage-Style Residences (Connect CRE California, California): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- American Landmark appoints new investment chief (Multifamily Dive, Phoenix / Arizona): Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- Hunt Helming $125M Dallas Adaptive Reuse Venture (Connect CRE Texas, Dallas / Texas): Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- JLL Arranges $252M Financing for Huntington Beach Seniors Project (Connect CRE Orange County, California): Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- Amazon, C&A Development Plan Capitol Hill Affordable Housing Project (Connect CRE Apartments, Seattle): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- New York Developer Seeks to Build 296 Units in Flushing, Queens (Commercial Observer, New York City / New York): Development-stage terms detected: planning_commission, zoning. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 25

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.