# Classification Quality Report

Generated: 2026-11-19 03:59:43

## Classification Summary

- Total articles classified: 58
- Topic distribution: development_pipeline: 18; supply_demand: 9; transaction_market: 8; institutional_capital: 6; gp_activity: 5; macro_financing: 4; other: 4; capital_markets: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 18 article(s), high 2, medium 10, low 6, unknown 0. Top markets: Other / Unknown (5); Los Angeles / California (2); Atlanta / Georgia (2); Florida (2); New York City / New York (1).
- supply_demand: 9 article(s), high 0, medium 0, low 9, unknown 0. Top markets: National (4); Other / Unknown (4); Tampa / Florida (1).
- transaction_market: 8 article(s), high 2, medium 3, low 3, unknown 0. Top markets: Atlanta / Georgia (3); Texas (1); Beverly Hills / California (1); Other / Unknown (1); California (1).
- institutional_capital: 6 article(s), high 1, medium 3, low 2, unknown 0. Top markets: Other / Unknown (1); California (1); New York (1); Sun Belt (1); Miami / Florida (1).
- gp_activity: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (4); National (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Other / Unknown (2).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (2); Los Angeles (1); Los Angeles / California (1).
- capital_markets: 2 article(s), high 0, medium 2, low 0, unknown 0. Top markets: Denver / Colorado (1); Miami / Florida (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (2).

## Low Confidence / Unknown Articles

- 269 homes to replace nursery at 7639 Topanga Canyon Blvd. in Canoga Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- New plan for housing at 452 N. Los Robles Ave. in Pasadena (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Multifamily housing unwrapped at 4429 S. Vermont Ave. in South L.A. (Urbanize LA, Los Angeles): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing underway at 6908 Baird Ave. in Reseda (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing takes shape at 3985 S. Meier St. in Mar Vista (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- JLL Arranges Financing for 419-Unit Luxury Multifamily Development in Evanston, Illinois (REBusiness Online, Other / Unknown): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- JLL Arranges $31M Sale of Boutique Apartment Property in Chicago (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- New, downsized look for housing project at 1521 E. Grand Ave. in El Segundo (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 'Graffiti towers' no more: Oceanwide Plaza is officially cleaned up (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- How apartment developers can successfully install connected services (Multifamily Dive, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily starts rose in October amid high borrowing, materials costs (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Denver Investor Pays $193M for Fenway Apartment Complex (Connect CRE, Denver / Colorado): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- New $200M Tampa Rental Community to Include Mark Wahlberg’s Gym (Connect CRE Apartments, Tampa / Florida): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Four townhomes coming to 1155 N. Heliotrope Dr. in East Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Shorter Apartment Construction Time in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery, permit. Primary topic set to development_pipeline; confidence low.
- Portman Begins Mixed-Use Redevelopment of 20-Acre Office Campus in Metro Atlanta (REBusiness Online, Atlanta / Georgia): Development-stage terms detected: entitlement, zoning, redevelopment. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 15

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.