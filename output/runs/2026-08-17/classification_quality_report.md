# Classification Quality Report

Generated: 2026-08-17 23:22:39

## Classification Summary

- Total articles classified: 79
- Topic distribution: transaction_market: 19; supply_demand: 14; development_pipeline: 12; institutional_capital: 10; gp_activity: 7; capital_markets: 5; macro_financing: 5; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 19 article(s), high 4, medium 10, low 5, unknown 0. Top markets: California (3); Other / Unknown (2); Los Angeles / California (2); Miami / Florida (2); Phoenix / Arizona (2).
- supply_demand: 14 article(s), high 0, medium 1, low 13, unknown 0. Top markets: Other / Unknown (9); National (4); Atlanta / Georgia (1).
- development_pipeline: 12 article(s), high 0, medium 5, low 7, unknown 0. Top markets: Other / Unknown (5); California (2); Atlanta / Georgia (2); Los Angeles / California (1); Phoenix / Arizona (1).
- institutional_capital: 10 article(s), high 5, medium 3, low 2, unknown 0. Top markets: California (3); Other / Unknown (2); Phoenix / Arizona (1); National (1); New York (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: National (3); Miami / Florida (2); Other / Unknown (1); Atlanta / Georgia (1).
- capital_markets: 5 article(s), high 2, medium 2, low 1, unknown 0. Top markets: Miami / Florida (1); San Francisco / California (1); California (1); Atlanta / Georgia (1); Georgia (1).
- macro_financing: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (2); San Francisco / California (1); Atlanta / Georgia (1); Los Angeles / California (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Other / Unknown (1); California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); National (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- State awards $6.5 million for affordable housing at 2518 Cesar E. Chavez Ave. in Boyle Heights (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing under construction at 9038 S. Reading Ave. in Westchester (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- L.A. City Planning Commission approves 379 apartments at 3200 S. La Cienega Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: planning_commission. Primary topic set to development_pipeline; confidence low.
- Residential conversion planned for office building at 1650 S. Westwood Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 405 apartments take shape at 6728 Sepulveda Blvd. in Van Nuys (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing coming to 4345 S. Crenshaw Blvd. in Leimert Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Northmarq Arranges $23M for Apartments in Federal Way (Connect CRE Apartments, San Francisco / California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Capstone Completes Construction of 201-Unit Affordable Housing Development in Atlanta (REBusiness Online, Atlanta / Georgia): Development-stage terms detected: delivery, redevelopment. Primary topic set to development_pipeline; confidence low.
- Marcus & Millichap Arranges $5.75M Sale and $3.8M Financing of 16-Unit Multifamily Property in Belmont California (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Marcus & Millichap Brokers $7.2M Sale of Multifamily Asset in Miami (Yield PRO, Miami / Florida): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- Mixed-use senior housing project slated for 540 S. Lake Ave. in Pasadena (Urbanize LA, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Survey: 61% of Investors Hold Negative Multifamily Outlook in 2026, Per Berkadia (Commercial Observer, National): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Atlanta Beltline Advancing 218-Unit Affordable Apartment Project (Connect CRE Atlanta, Atlanta / Georgia): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Thompson Thrift to Develop 300-unit Luxury Apartment Community Outside Birmingham Alabama (Yield PRO, National): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- NRP Advancing 312-Unit Port St. Lucie Apartment Venture (Connect CRE Apartments, Miami / Florida): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Top markets for apartment sales in H1 2026 (Multifamily Dive, San Francisco / California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
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