# Classification Quality Report

Generated: 2026-11-20 03:53:34

## Classification Summary

- Total articles classified: 65
- Topic distribution: development_pipeline: 13; transaction_market: 13; gp_activity: 8; supply_demand: 8; capital_markets: 7; institutional_capital: 5; other: 5; macro_financing: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 13 article(s), high 1, medium 7, low 5, unknown 0. Top markets: Other / Unknown (6); Los Angeles / California (1); Houston / Texas (1); Phoenix / Arizona (1); California (1).
- transaction_market: 13 article(s), high 1, medium 7, low 5, unknown 0. Top markets: Atlanta / Georgia (3); California (2); Austin / Texas (2); Seattle (1); Houston / Texas (1).
- gp_activity: 8 article(s), high 0, medium 0, low 1, unknown 7. Top markets: Other / Unknown (6); California (1); National (1).
- supply_demand: 8 article(s), high 0, medium 0, low 8, unknown 0. Top markets: National (4); Other / Unknown (3); Atlanta / Georgia (1).
- capital_markets: 7 article(s), high 1, medium 6, low 0, unknown 0. Top markets: Miami / Florida (2); Atlanta / Georgia (1); New York (1); Las Vegas / Nevada (1); Other / Unknown (1).
- institutional_capital: 5 article(s), high 0, medium 3, low 2, unknown 0. Top markets: Sun Belt (1); California (1); Miami / Florida (1); Other / Unknown (1); Atlanta / Georgia (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (3); Los Angeles (1); San Francisco / California (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Other / Unknown (2).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Southeast (1); Los Angeles / California (1).

## Low Confidence / Unknown Articles

- Bell Partners Spends $149M on MF Property in Issaquah, Washington (Connect CRE, Seattle): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- Mixed-use project starts to rise at 3313 Sunset Blvd. in Silver Lake (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 269 homes to replace nursery at 7639 Topanga Canyon Blvd. in Canoga Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- New plan for housing at 452 N. Los Robles Ave. in Pasadena (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Multifamily housing unwrapped at 4429 S. Vermont Ave. in South L.A. (Urbanize LA, Los Angeles): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing underway at 6908 Baird Ave. in Reseda (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Fresh renderings for infill housing at 511 S. Oak Knoll Ave. in Pasadena (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- New, downsized look for housing project at 1521 E. Grand Ave. in El Segundo (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 'Graffiti towers' no more: Oceanwide Plaza is officially cleaned up (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- HTG Celebrates Grand Opening of $34.2M Mixed-Income Community in Houston’s Energy Corridor (Yield PRO, Houston / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- How apartment developers can successfully install connected services (Multifamily Dive, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily starts rose in October amid high borrowing, materials costs (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- CBRE Arranges $45.6M Sale of Newly Constructed 97-Unit Luxury Multifamily Property in West New York New Jersey (Yield PRO, New York): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- McShane to Build 280-Unit Apartment Community in Hoffman Estates, Illinois (REBusiness Online, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- L+M Development Partners Cuts Ribbon for Renovated Chicago Apartments (Connect CRE Apartments, Other / Unknown): Financing type keywords detected: tax_credit_financing. Primary topic set to gp_activity; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Sherman Associates Marks First Residential Opening at Beltline Station in St. Louis Park (Connect CRE Apartments, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 19

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.