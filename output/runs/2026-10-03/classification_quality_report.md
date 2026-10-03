# Classification Quality Report

Generated: 2026-10-03 01:46:31

## Classification Summary

- Total articles classified: 76
- Topic distribution: transaction_market: 17; development_pipeline: 16; capital_markets: 14; supply_demand: 11; institutional_capital: 5; gp_activity: 4; macro_financing: 4; research_data: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 17 article(s), high 3, medium 8, low 6, unknown 0. Top markets: California (3); Atlanta / Georgia (3); Los Angeles / California (2); Other / Unknown (2); Washington DC (2).
- development_pipeline: 16 article(s), high 1, medium 6, low 9, unknown 0. Top markets: Other / Unknown (5); Dallas / Texas (2); Phoenix / Arizona (2); New York City / New York (2); Miami / Florida (1).
- capital_markets: 14 article(s), high 8, medium 5, low 1, unknown 0. Top markets: California (3); Nashville / Tennessee (2); Miami / Florida (2); Other / Unknown (2); Los Angeles / California (1).
- supply_demand: 11 article(s), high 0, medium 0, low 11, unknown 0. Top markets: Other / Unknown (7); National (2); Salt Lake City / Utah (1); Miami / Florida (1).
- institutional_capital: 5 article(s), high 1, medium 3, low 1, unknown 0. Top markets: Los Angeles / California (2); Dallas / Texas (1); Southeast (1); Miami / Florida (1).
- gp_activity: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (3); National (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (2); California (1); Los Angeles / California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); Colorado (1).
- other: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); San Francisco / California (1).

## Low Confidence / Unknown Articles

- North Hollywood Apartments Trade to Locally Based LLC (Connect CRE, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Northmarq Arranges Sale of St. Louis Metro Multifamily Property (Connect CRE, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- SoLa Impact score $93M financing package for housing at 252 W. Imperial Highway (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Senior housing takes shape at 1150 Colorado Blvd. in Arcadia (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Proposed high-rise poised for another step forward at 1000 La Brea Ave. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing takes shape at 5110 Washington Blvd. in Mid-City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- JLL Arranges Equity Placement for 217-Unit Multifamily Development in Bluffdale, Utah (REBusiness Online, Salt Lake City / Utah): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- KAI Build, Revive Capital to Transform Former 7UP Headquarters in Metro St. Louis into Apartments (REBusiness Online, Dallas / Texas): Development-stage terms detected: construction_start, renovation_repositioning. Primary topic set to development_pipeline; confidence low.
- Northmarq Arranges Sale of 315-Unit Multifamily Community in Saint Louis Metro (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Preliminary Plans For 770 Golden Gate Avenue, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Related Affiliate Obtains $167M Loan Package for Miami Apartment Community (Connect CRE South Florida, Miami / Florida): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Charney Companies, Tavros Break Ground on Fifth Gowanus Development (Connect CRE, New York City / New York): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Marcus & Millichap Arranges $5.89M Sale of 41-Unit Multifamily Property in North Hollywood California (Yield PRO, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- New details for affordable housing at 1150 Sunset Blvd. in Echo Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Report: Chicago is America’s Most Competitive Rental Market (Connect CRE Apartments, Miami / Florida): Supply/demand terms detected: vacancy. Primary topic set to supply_demand; confidence low.
- N. Phoenix Apartments Trade for $58.7M (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 21

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.