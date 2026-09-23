# Classification Quality Report

Generated: 2026-09-23 01:17:04

## Classification Summary

- Total articles classified: 77
- Topic distribution: transaction_market: 21; development_pipeline: 13; supply_demand: 10; capital_markets: 9; gp_activity: 8; macro_financing: 6; other: 4; institutional_capital: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 21 article(s), high 5, medium 11, low 5, unknown 0. Top markets: California (7); Atlanta / Georgia (3); Denver / Colorado (2); Los Angeles / California (2); Other / Unknown (2).
- development_pipeline: 13 article(s), high 1, medium 6, low 6, unknown 0. Top markets: Other / Unknown (5); Dallas / Texas (2); Miami / Florida (2); Atlanta / Georgia (2); Washington DC (1).
- supply_demand: 10 article(s), high 0, medium 0, low 10, unknown 0. Top markets: Other / Unknown (7); National (3).
- capital_markets: 9 article(s), high 5, medium 3, low 1, unknown 0. Top markets: Miami / Florida (5); New York City / New York (2); Texas (1); Austin / Texas (1).
- gp_activity: 8 article(s), high 0, medium 0, low 1, unknown 7. Top markets: Other / Unknown (3); Phoenix / Arizona (2); Florida (1); Nashville / Tennessee (1); National (1).
- macro_financing: 6 article(s), high 0, medium 0, low 1, unknown 5. Top markets: Other / Unknown (4); California (1); Atlanta / Georgia (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Other / Unknown (1); Colorado (1).
- institutional_capital: 3 article(s), high 0, medium 2, low 1, unknown 0. Top markets: Dallas / Texas (1); National (1); Other / Unknown (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Colorado (1); Los Angeles / California (1); California (1).

## Low Confidence / Unknown Articles

- Renderings Revealed: Mixed-use project at 305 E. Colorado St. in Glendale (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing in the works at 1945 S. Carmona Ave. in Mid-City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Multifamily starts plummeted nearly 16% in August (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Marcus & Millichap Closes Multifamily Sale in San Diego’s College East (Connect CRE California, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Five homes planned at 1254 N. Orange Dr. in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Cushman & Wakefield Lands Palm City Development Marketing Assignment (Connect CRE Apartments, Florida): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Adam America Real Estate and JW Capital Management Secure $180M Refinancing of Student Housing Property in Miami (Yield PRO, Miami / Florida): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- HTG Debuts $115M Miami Affordable Housing Project (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- 309-Unit Waterfront Community in Madison Celebrates Grand Opening (Connect CRE Apartments, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- JLB Pursuing Buckhead Office-to-Apartments Conversion (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Investor Takes Over Distressed Atlanta Apartment Asset (Connect CRE Atlanta, Atlanta / Georgia): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Thompson Thrift Pursuing 319-Unit Powder Springs Rental Community (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: lease_up. Primary topic set to development_pipeline; confidence low.
- Saratoga Capital Pays $98.4M at Auction for Atlanta Apartment Community (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Essex Realty Group Markets 13-Unit Multifamily Property in North Park (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Shorter Apartment Construction Time in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery, permit. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 24

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.