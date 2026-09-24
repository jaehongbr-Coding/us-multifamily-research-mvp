# Classification Quality Report

Generated: 2026-09-24 01:08:37

## Classification Summary

- Total articles classified: 72
- Topic distribution: transaction_market: 18; development_pipeline: 12; supply_demand: 10; gp_activity: 8; capital_markets: 7; macro_financing: 7; research_data: 4; institutional_capital: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 18 article(s), high 6, medium 8, low 4, unknown 0. Top markets: California (4); Atlanta / Georgia (4); Los Angeles / California (3); Other / Unknown (3); Colorado (1).
- development_pipeline: 12 article(s), high 0, medium 4, low 8, unknown 0. Top markets: Other / Unknown (5); Miami / Florida (2); Atlanta / Georgia (2); New York City / New York (1); Virginia (1).
- supply_demand: 10 article(s), high 0, medium 0, low 10, unknown 0. Top markets: Other / Unknown (7); National (3).
- gp_activity: 8 article(s), high 0, medium 0, low 1, unknown 7. Top markets: Other / Unknown (3); Phoenix / Arizona (2); Texas (1); Nashville / Tennessee (1); National (1).
- capital_markets: 7 article(s), high 3, medium 4, low 0, unknown 0. Top markets: Miami / Florida (2); Washington DC (1); Other / Unknown (1); Austin / Texas (1); Florida (1).
- macro_financing: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Other / Unknown (3); National (1); Los Angeles / California (1); California (1); Atlanta / Georgia (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Colorado (1); California (1).
- institutional_capital: 3 article(s), high 1, medium 2, low 0, unknown 0. Top markets: New York (1); National (1); Kentucky (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: California (1); Los Angeles / California (1); Colorado (1).

## Low Confidence / Unknown Articles

- Northmarq assesses the outlook for multifamily at midyear (Yield PRO, National): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Construction goes vertical for mixed-use project at 155 W. 6th St. in San Pedro (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Apartment complex fully framed at 11250 La Grange Ave. in Sawtelle (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Senior affordable housing starting work at 7556 Woodlake Ave. in West Hills (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Renderings Revealed: Mixed-use project at 305 E. Colorado St. in Glendale (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing in the works at 1945 S. Carmona Ave. in Mid-City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Embrey to Build 296 New Luxury Multifamily Units in San Antonio (Yield PRO, Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily starts plummeted nearly 16% in August (Construction Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Devens Site Will Yield 65 Affordable Apartments (Connect CRE, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- TCB, BHA Complete 223-Unit Multifamily Redevelopment Project in Boston (REBusiness Online, Other / Unknown): Development-stage terms detected: delivery, redevelopment. Primary topic set to development_pipeline; confidence low.
- Audubon Capital Grabs Midtown Atlanta Apartment Asset Prior to Foreclosure (Yield PRO, Atlanta / Georgia): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Five homes planned at 1254 N. Orange Dr. in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- HTG Debuts $115M Miami Affordable Housing Project (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- JLB Pursuing Buckhead Office-to-Apartments Conversion (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Pembroke Realty Provides Updates on $300M Mall Redevelopment in Virginia Beach (REBusiness Online, Virginia): Development-stage terms detected: under_construction, redevelopment. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 24

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.