# Classification Quality Report

Generated: 2026-06-23 00:07:52

## Classification Summary

- Total articles classified: 75
- Topic distribution: development_pipeline: 17; gp_activity: 14; capital_markets: 11; supply_demand: 11; transaction_market: 11; macro_financing: 4; other: 3; research_data: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 17 article(s), high 2, medium 5, low 10, unknown 0. Top markets: Other / Unknown (4); California (3); Los Angeles / California (2); Georgia (1); Miami / Florida (1).
- gp_activity: 14 article(s), high 0, medium 0, low 3, unknown 11. Top markets: National (3); Los Angeles / California (2); Phoenix / Arizona (2); Other / Unknown (2); New York City / New York (1).
- capital_markets: 11 article(s), high 5, medium 6, low 0, unknown 0. Top markets: Dallas / Texas (3); Miami / Florida (2); California (2); Atlanta / Georgia (1); Phoenix / Arizona (1).
- supply_demand: 11 article(s), high 0, medium 0, low 11, unknown 0. Top markets: Other / Unknown (7); National (4).
- transaction_market: 11 article(s), high 2, medium 3, low 6, unknown 0. Top markets: Other / Unknown (2); Phoenix / Arizona (2); California (2); New York (1); Los Angeles / California (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (3); San Francisco / California (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Santa Monica / California (1); Los Angeles / California (1); Beverly Hills / California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Beverly Hills / California (1); California (1); National (1).
- institutional_capital: 1 article(s), high 0, medium 0, low 1, unknown 0. Top markets: Other / Unknown (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Northmarq Investment Sales team facilitates $14M sale of Mossy Oaks Apartments in Beaufort South Carolina (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Culver City’s Housing Strategy: Don’t Be L.A. (Commercial Observer, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Mott Haven Development Site Set for One or More Residential Buildings (Connect CRE, New York): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Naftali Credit Partners Arranges $75M Debt for Flatbush Condo Project (Connect CRE, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Work beginning for Taix redevelopment at 1911 Sunset Blvd. in Echo Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Adaptive reuse project gets colorful new exterior at 3325 Wilshire Blvd. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- New plan for apartments at 745 17th Street in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Measure ULA reform goes to the ballot, Remembering Lorcan O'Herlihy, and more (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Mixed-use project could replace Beverly Hills gas station at 8555 Wilshire Blvd. (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Infill housing in progress at 3676 S. Kelton Ave. in Palms (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Developer retools plan for mixed-use project at 3800 W. 6th St. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Brook Farm, Manor Park to Develop 336-Unit Multifamily Community in Savannah (REBusiness Online, Georgia): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Levin Johnston Arranges Two Sales on San Francisco Peninsula (Connect CRE California, San Francisco / California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Inside The Turmoil Clouding Miami's Largest Affordable Housing Project (Bisnow, Miami / Florida): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- American Landmark appoints new investment chief (Multifamily Dive, Phoenix / Arizona): Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- Fourth Avenue Capital Breaks Ground on Suburban WA Apartments (Connect CRE Apartments, Seattle): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Hunt Helming $125M Dallas Adaptive Reuse Venture (Connect CRE Apartments, Dallas / Texas): Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 32

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.