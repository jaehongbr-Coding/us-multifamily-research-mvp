# Classification Quality Report

Generated: 2026-09-02 00:51:10

## Classification Summary

- Total articles classified: 83
- Topic distribution: transaction_market: 20; development_pipeline: 13; supply_demand: 13; capital_markets: 10; gp_activity: 7; institutional_capital: 5; macro_financing: 5; other: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 20 article(s), high 5, medium 7, low 8, unknown 0. Top markets: California (4); Other / Unknown (2); Atlanta / Georgia (2); Seattle (2); Miami / Florida (2).
- development_pipeline: 13 article(s), high 1, medium 6, low 6, unknown 0. Top markets: Other / Unknown (5); Atlanta / Georgia (3); Miami / Florida (2); Los Angeles / California (1); California (1).
- supply_demand: 13 article(s), high 0, medium 1, low 12, unknown 0. Top markets: Other / Unknown (7); National (2); New York City / New York (1); California (1); Dallas / Texas (1).
- capital_markets: 10 article(s), high 6, medium 3, low 1, unknown 0. Top markets: Miami / Florida (5); Riverside / California (2); Tampa / Florida (1); California (1); National (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (3); Phoenix / Arizona (1); Texas (1); Austin / Texas (1); National (1).
- institutional_capital: 5 article(s), high 2, medium 1, low 2, unknown 0. Top markets: California (1); Austin / Texas (1); Georgia (1); Miami / Florida (1); National (1).
- macro_financing: 5 article(s), high 0, medium 0, low 1, unknown 4. Top markets: Other / Unknown (3); San Francisco / California (1); Atlanta / Georgia (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (2); California (1); San Francisco / California (1); Other / Unknown (1).
- research_data: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (5).

## Low Confidence / Unknown Articles

- JLL Capital Markets Led Sales Efforts for 100-Unit Multifamily Community Sale in New Jersey (Yield PRO, Other / Unknown): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- Construction begins for mixed-use project at 11905 Wilshire Blvd. in Brentwood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Rendering vs. Reality: Affordable housing at 1201 N. Detroit St. in West Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- L.A.'s new build apartments are shrinking (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Rendering vs. Reality: Mixed-use complex at 3900 S. Figueroa St. in Expo Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Eldercare facility approved for site at 5353 N. Del Moreno Dr. in Woodland Hills (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Affordable housing topped off at 8911 Ramsgate Ave. in Westchester (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing complex underway at 708 S. Gramercy Dr. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Northmarq Brokers Record Multifamily Sale in Wichita (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- New York City Sees Nation’s Fastest Multifamily Rent Growth (Connect CRE Apartments, New York City / New York): Supply/demand terms detected: effective_rent_growth, occupancy. Primary topic set to supply_demand; confidence low.
- CBRE Brokers Sale of Vintage Redlands Apartments (Connect CRE California, Riverside / California): Capital event keywords detected: disposition. Supply/demand terms detected: effective_rent_growth. Primary topic set to transaction_market; confidence medium.
- Torrance Apartments Trade for $350K/Unit (Connect CRE California, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Development Team Starts Work on Milpitas Affordable Housing Project (Connect CRE Apartments, California): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Miami-Dade Public Agency Advancing $126.4M Affordable Housing Project (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Institutional Property Advisors Brokers Sale and Arranges Financing for Lakefront Multifamily Asset in Seattle (Yield PRO, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Gantry Arranges $22.8M Loan for Kansas Student Housing Property (REBusiness Online, Other / Unknown): Financing type keywords detected: cmbs. Primary topic set to macro_financing; confidence low.
- Rendering vs. Reality: Torrance's Gable House Apartments (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Dallas Multifamily 2026 Panelists Cautious, Hopeful About Industry Future (Connect CRE, Dallas / Texas): Supply/demand terms detected: effective_rent_growth, vacancy, occupancy. Primary topic set to supply_demand; confidence low.
- Former Factory to Receive New Life as Affordable Homes in Upstate NY (Connect CRE, New York): Supply/demand terms detected: vacancy. Primary topic set to supply_demand; confidence low.
- Additional low/unknown rows omitted: 31

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.