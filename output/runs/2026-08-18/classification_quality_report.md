# Classification Quality Report

Generated: 2026-08-18 23:21:58

## Classification Summary

- Total articles classified: 76
- Topic distribution: transaction_market: 17; supply_demand: 13; institutional_capital: 11; development_pipeline: 10; gp_activity: 8; capital_markets: 6; macro_financing: 4; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 17 article(s), high 5, medium 9, low 3, unknown 0. Top markets: California (3); Other / Unknown (3); Atlanta / Georgia (2); National (1); New York (1).
- supply_demand: 13 article(s), high 0, medium 0, low 13, unknown 0. Top markets: Other / Unknown (7); National (4); New York City / New York (1); Atlanta / Georgia (1).
- institutional_capital: 11 article(s), high 2, medium 6, low 3, unknown 0. Top markets: Other / Unknown (3); California (2); New York (2); Phoenix / Arizona (1); Dallas / Texas (1).
- development_pipeline: 10 article(s), high 0, medium 4, low 6, unknown 0. Top markets: Other / Unknown (3); Los Angeles / California (2); California (1); Austin / Texas (1); Phoenix / Arizona (1).
- gp_activity: 8 article(s), high 0, medium 0, low 0, unknown 8. Top markets: Other / Unknown (2); Miami / Florida (2); National (2); Dallas / Texas (1); Southeast (1).
- capital_markets: 6 article(s), high 1, medium 2, low 3, unknown 0. Top markets: Other / Unknown (3); Phoenix / Arizona (1); Atlanta / Georgia (1); Houston / Texas (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (2); Atlanta / Georgia (1); Los Angeles / California (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (1); San Francisco / California (1); Other / Unknown (1); California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (3).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Cushman & Wakefield Multifamily Advisory Group Brokers Sale of 280-Unit Apartment Community in Oswego Illinois (Yield PRO, National): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low. Operator/property management activity detected.
- New York City’s Next Multifamily Shortage? Buildings to Buy. (Commercial Observer, New York City / New York): Supply/demand terms detected: vacancy, supply_pressure. Primary topic set to supply_demand; confidence low.
- Prism Partners Trades Two-Building Edison Lofts for $131M (Connect CRE, New York): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- $67M Refinancing Secured by JLL for Seniors Housing Property in Kansas (Connect CRE, Other / Unknown): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- Senior affordable housing rising at 19300 Sherman Way in Reseda (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing project moves forward at 3401 Cerritos Ave. in Long Beach (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- State awards $6.5 million for affordable housing at 2518 Cesar E. Chavez Ave. in Boyle Heights (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing under construction at 9038 S. Reading Ave. in Westchester (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- L.A. City Planning Commission approves 379 apartments at 3200 S. La Cienega Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: planning_commission. Primary topic set to development_pipeline; confidence low.
- Residential conversion planned for office building at 1650 S. Westwood Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Developer Eyeing 143-Acre “Italian Village” in Prosper (Connect CRE Apartments, Dallas / Texas): Institutional activity terms detected: private_equity_activity. Primary topic set to institutional_capital; confidence low.
- JPI to Develop $90M Multifamily Project in Northwest Austin (REBusiness Online, Dallas / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily starts tumbled in July (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Multifamily distress grows, but data suggest a contained problem (HousingWire, Other / Unknown): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Atlanta Beltline Advancing 218-Unit Affordable Apartment Project (Connect CRE Atlanta, Atlanta / Georgia): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Greenstone Partners Closes MF Deal in Chicago’s South Suburbs (Connect CRE, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Triten Snags Refi on 342-Unit Houston Rental Community (Connect CRE Texas, Houston / Texas): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Additional low/unknown rows omitted: 27

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.