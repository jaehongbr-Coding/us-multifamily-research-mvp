# Classification Quality Report

Generated: 2026-09-22 01:28:17

## Classification Summary

- Total articles classified: 81
- Topic distribution: development_pipeline: 21; transaction_market: 18; supply_demand: 10; capital_markets: 9; gp_activity: 6; macro_financing: 6; institutional_capital: 4; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 21 article(s), high 1, medium 7, low 13, unknown 0. Top markets: Other / Unknown (7); Miami / Florida (4); Atlanta / Georgia (3); San Francisco / California (2); Colorado (1).
- transaction_market: 18 article(s), high 3, medium 10, low 5, unknown 0. Top markets: California (5); Los Angeles / California (3); Atlanta / Georgia (3); Phoenix / Arizona (2); Other / Unknown (2).
- supply_demand: 10 article(s), high 1, medium 0, low 9, unknown 0. Top markets: Other / Unknown (6); National (4).
- capital_markets: 9 article(s), high 4, medium 5, low 0, unknown 0. Top markets: Other / Unknown (3); Miami / Florida (3); Texas (2); New York City / New York (1).
- gp_activity: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (3); Phoenix / Arizona (2); National (1).
- macro_financing: 6 article(s), high 0, medium 0, low 1, unknown 5. Top markets: Other / Unknown (4); California (1); Atlanta / Georgia (1).
- institutional_capital: 4 article(s), high 0, medium 4, low 0, unknown 0. Top markets: Dallas / Texas (1); California (1); Other / Unknown (1); National (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (3); Other / Unknown (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); California (1).

## Low Confidence / Unknown Articles

- Affordable housing in the works at 1945 S. Carmona Ave. in Mid-City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 65 apartments underway at 5909 S. Crenshaw Blvd. in Hyde Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing proposed at 12508 W. Pacific Ave. in Mar Vista (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- New Building Permits For 249 Pennsylvania Avenue, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Multifamily starts plummeted nearly 16% in August (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Marcus & Millichap Closes Multifamily Sale in San Diego’s College East (Connect CRE California, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Construction Nearly Topped Out For 486 West San Carlos Street, San Jose (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Five homes planned at 1254 N. Orange Dr. in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 309-Unit Waterfront Community in Madison Celebrates Grand Opening (Connect CRE, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- HTG Debuts $115M Miami Affordable Housing Project (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Marcus & Millichap Arranges $6.2M Sale of Multifamily Property in the Highland Park Neighborhood of Los Angeles (Yield PRO, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- USF Breaks Ground on $500M Mixed-Use Venture (Connect CRE Apartments, Miami / Florida): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- TCB Breaks Ground on 65-Unit Mixed-Income Housing Project in Provincetown, Massachusetts (REBusiness Online, Other / Unknown): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- JLB Pursuing Buckhead Office-to-Apartments Conversion (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Investor Pays $15M For Nebraska Apartment Community (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Additional low/unknown rows omitted: 26

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.