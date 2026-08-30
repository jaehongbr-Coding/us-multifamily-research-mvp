# Classification Quality Report

Generated: 2026-08-30 01:06:41

## Classification Summary

- Total articles classified: 80
- Topic distribution: transaction_market: 16; capital_markets: 14; development_pipeline: 11; supply_demand: 11; institutional_capital: 8; gp_activity: 6; macro_financing: 6; other: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 16 article(s), high 4, medium 8, low 4, unknown 0. Top markets: Miami / Florida (3); Atlanta / Georgia (2); Other / Unknown (2); Seattle (1); Sun Belt (1).
- capital_markets: 14 article(s), high 9, medium 4, low 1, unknown 0. Top markets: Other / Unknown (4); Los Angeles / California (2); San Francisco / California (1); Georgia (1); California (1).
- development_pipeline: 11 article(s), high 2, medium 2, low 7, unknown 0. Top markets: Other / Unknown (5); Atlanta / Georgia (2); Miami / Florida (1); California (1); Beverly Hills / California (1).
- supply_demand: 11 article(s), high 0, medium 1, low 10, unknown 0. Top markets: Other / Unknown (8); National (2); New York City / New York (1).
- institutional_capital: 8 article(s), high 3, medium 3, low 2, unknown 0. Top markets: California (6); Other / Unknown (1); Miami / Florida (1).
- gp_activity: 6 article(s), high 0, medium 0, low 1, unknown 5. Top markets: Other / Unknown (3); New York City / New York (1); Houston / Texas (1); National (1).
- macro_financing: 6 article(s), high 0, medium 0, low 1, unknown 5. Top markets: Other / Unknown (2); Washington DC (1); National (1); Atlanta / Georgia (1); New York City / New York (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: California (3); Santa Monica / California (1); Los Angeles / California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); California (1).

## Low Confidence / Unknown Articles

- Stratford Partners JV Buys San Diego-Area Apartments for $34M (Commercial Observer, California): Capital event keywords detected: joint_venture, acquisition. Primary topic set to institutional_capital; confidence low.
- Affordable housing complex underway at 708 S. Gramercy Dr. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing starts to rise at 216 S. Avenue 24 in Lincoln Heights (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 12-story residential building pitched for 1517 15th St. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing on the rise at 728 Lagoon Ave. in Wilmington (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- JLL Arranges Sale of 252-Unit Multifamily Community in Raleigh (REBusiness Online, Sun Belt): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Miami-Dade Public Agency Advancing $126.4 Affordable Housing Project (Connect CRE Apartments, Miami / Florida): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Beyond the Rent: The economic signals multifamily leaders should watch this fall (Multifamily Dive, Washington DC): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- 408 apartments rise at 2828 N. MainPlace Dr. in Santa Ana (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Rendering vs. Reality: Torrance's Gable House Apartments (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- AEW Adjusts Deployment Plan For $1.8B Real Estate Fund (Bisnow, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Westbridge Realty Group Files Plans for Three 99-Unit Buildings in the Bronx (Commercial Observer, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- JLB Pursuing Buckhead Office-to-Apartments Conversion (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Multifamily new supply set to bottom out in 2027 (Multifamily Dive, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Interra Realty Closes Multifamily Value-Add Deal in Chicago’s South Suburbs (Yield PRO, Other / Unknown): Development-stage terms detected: renovation_repositioning. Primary topic set to development_pipeline; confidence low.
- Work Underway on 388-Unit Rental Community Near The Woodlands (Connect CRE Texas, Houston / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 24

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.