# Classification Quality Report

Generated: 2026-08-19 23:23:08

## Classification Summary

- Total articles classified: 82
- Topic distribution: transaction_market: 20; development_pipeline: 14; supply_demand: 14; institutional_capital: 10; gp_activity: 8; macro_financing: 6; capital_markets: 4; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 20 article(s), high 7, medium 10, low 3, unknown 0. Top markets: Other / Unknown (4); California (3); San Francisco / California (2); Colorado (1); New York (1).
- development_pipeline: 14 article(s), high 1, medium 6, low 7, unknown 0. Top markets: Other / Unknown (4); Los Angeles / California (2); California (2); Atlanta / Georgia (2); Florida (1).
- supply_demand: 14 article(s), high 0, medium 0, low 14, unknown 0. Top markets: Other / Unknown (7); National (4); New York City / New York (1); Atlanta / Georgia (1); Florida (1).
- institutional_capital: 10 article(s), high 3, medium 3, low 4, unknown 0. Top markets: Dallas / Texas (2); California (2); Phoenix / Arizona (1); New York (1); Other / Unknown (1).
- gp_activity: 8 article(s), high 0, medium 0, low 0, unknown 8. Top markets: Miami / Florida (3); Other / Unknown (2); National (2); Los Angeles / California (1).
- macro_financing: 6 article(s), high 0, medium 0, low 1, unknown 5. Top markets: Los Angeles / California (2); Other / Unknown (2); Atlanta / Georgia (1); California (1).
- capital_markets: 4 article(s), high 0, medium 3, low 1, unknown 0. Top markets: Phoenix / Arizona (1); Atlanta / Georgia (1); Houston / Texas (1); Miami / Florida (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Other / Unknown (2); San Francisco / California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (3).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- New York’s 485-x Is Teaching Developers to Stay Below 100 Apartments at a Time (Commercial Observer, New York City / New York): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Massachusetts AG Orders Post-Merger Sale of Two Boston Apartment Towers (Connect CRE, Other / Unknown): Capital event keywords detected: merger_acquisition, disposition. Primary topic set to institutional_capital; confidence low.
- Affordable housing takes shape at 17100 Victory Blvd. in Lake Balboa (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- 39 apartments approved at 10535 W. Missouri Ave. in West L.A. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Senior affordable housing rising at 19300 Sherman Way in Reseda (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing project moves forward at 3401 Cerritos Ave. in Long Beach (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- State awards $6.5 million for affordable housing at 2518 Cesar E. Chavez Ave. in Boyle Heights (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing under construction at 9038 S. Reading Ave. in Westchester (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Prism Partners Trades Two-Building Edison Lofts for $131M (Connect CRE Apartments, New York): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Developer Eyeing 143-Acre “Italian Village” in Prosper (Connect CRE Texas, Dallas / Texas): Institutional activity terms detected: private_equity_activity. Primary topic set to institutional_capital; confidence low.
- Multifamily starts tumbled in July (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Marcus & Millichap Arranges Sale of Multifamily Apartment Property in Greenville South Carolina Suburb (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Atlanta Beltline Advancing 218-Unit Affordable Apartment Project (Connect CRE Atlanta, Atlanta / Georgia): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- PCCP, RPM Pick Up 358-Unit Arlington Multifamily Community (Connect CRE Apartments, Dallas / Texas): Capital event keywords detected: joint_venture, acquisition. Primary topic set to institutional_capital; confidence low.
- Triten Snags Refi on 342-Unit Houston Rental Community (Connect CRE Texas, Houston / Texas): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Simon | Anderson Multifamily Team Arranges Sale of SEDU Apartment Building in Seattle’s Capitol Hill Neighborhood (Yield PRO, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Updated Plans For 2513 Irving Street, Sunset District, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Additional low/unknown rows omitted: 29

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.