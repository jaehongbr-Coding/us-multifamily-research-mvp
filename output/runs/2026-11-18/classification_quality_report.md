# Classification Quality Report

Generated: 2026-11-18 04:02:46

## Classification Summary

- Total articles classified: 67
- Topic distribution: development_pipeline: 16; transaction_market: 13; institutional_capital: 8; capital_markets: 7; supply_demand: 7; gp_activity: 5; macro_financing: 5; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 16 article(s), high 1, medium 10, low 5, unknown 0. Top markets: Other / Unknown (8); Phoenix / Arizona (2); Miami / Florida (2); California (1); New York City / New York (1).
- transaction_market: 13 article(s), high 2, medium 3, low 8, unknown 0. Top markets: Atlanta / Georgia (3); California (2); Florida (1); Other / Unknown (1); Riverside / California (1).
- institutional_capital: 8 article(s), high 0, medium 4, low 4, unknown 0. Top markets: Other / Unknown (3); Virginia (1); Denver / Colorado (1); California (1); Miami / Florida (1).
- capital_markets: 7 article(s), high 2, medium 4, low 1, unknown 0. Top markets: Other / Unknown (2); Miami / Florida (2); Denver / Colorado (1); Dallas / Texas (1); Phoenix / Arizona (1).
- supply_demand: 7 article(s), high 0, medium 0, low 7, unknown 0. Top markets: Other / Unknown (3); National (3); New York City / New York (1).
- gp_activity: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (3); Austin / Texas (1); National (1).
- macro_financing: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (2); Los Angeles / California (1); New York City / New York (1); California (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); Other / Unknown (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (2).
- operations_property_management: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: Virginia (1).

## Low Confidence / Unknown Articles

- Debt, Equity Secured for Evanston Luxury High-Rise Development (Connect CRE, Other / Unknown): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Affordable housing underway at 6908 Baird Ave. in Reseda (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing takes shape at 3985 S. Meier St. in Mar Vista (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Costco-anchored project adds more housing at 5035 Coliseum St. in Baldwin Hills (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Developers Break Ground on 420-Unit Multifamily Community in Metro D.C. (REBusiness Online, Virginia): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Cushman & Wakefield Brokers $44M Sale of 240-Unit Apartments in Sheboygan (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Advanced Real Estate Pays $56 Million for Ontario Multifamily Complex (Connect CRE California, Riverside / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Fresno Low-Rise Trades to Private Buyer in All-Cash Deal (Connect CRE California, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- New, downsized look for housing project at 1521 E. Grand Ave. in El Segundo (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 'Graffiti towers' no more: Oceanwide Plaza is officially cleaned up (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- EJF Capital to Build BTR Community in Indianapolis (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Graffiti Removal Sets Stage for Sale of Oceanwide Plaza (Connect CRE California, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Mamdani’s NYC public housing rebuild plan skirts DSA rebuke (HousingWire, New York City / New York): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- $320M Redevelopment of Astoria Boys and Girls Club Includes Affordable Housing (Connect CRE Apartments, New York City / New York): Development-stage terms detected: construction_start, redevelopment. Primary topic set to development_pipeline; confidence low.
- Taylor Morrison to Start Work on 161-Unit Austin BTR Community (Connect CRE Texas, Austin / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Four townhomes coming to 1155 N. Heliotrope Dr. in East Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Additional low/unknown rows omitted: 21

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.