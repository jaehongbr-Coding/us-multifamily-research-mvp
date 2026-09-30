# Classification Quality Report

Generated: 2026-09-30 01:52:25

## Classification Summary

- Total articles classified: 74
- Topic distribution: transaction_market: 18; development_pipeline: 13; gp_activity: 10; supply_demand: 10; capital_markets: 9; macro_financing: 6; research_data: 4; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 18 article(s), high 8, medium 7, low 3, unknown 0. Top markets: Atlanta / Georgia (4); New York City / New York (3); Other / Unknown (3); California (2); Los Angeles / California (1).
- development_pipeline: 13 article(s), high 0, medium 6, low 7, unknown 0. Top markets: Other / Unknown (7); Miami / Florida (1); Houston / Texas (1); Austin / Texas (1); Phoenix / Arizona (1).
- gp_activity: 10 article(s), high 0, medium 0, low 0, unknown 10. Top markets: Other / Unknown (5); Phoenix / Arizona (2); Sun Belt (1); National (1); New York City / New York (1).
- supply_demand: 10 article(s), high 0, medium 0, low 10, unknown 0. Top markets: Other / Unknown (7); National (3).
- capital_markets: 9 article(s), high 3, medium 6, low 0, unknown 0. Top markets: Miami / Florida (3); Other / Unknown (2); Florida (2); Los Angeles / California (2).
- macro_financing: 6 article(s), high 0, medium 0, low 1, unknown 5. Top markets: Los Angeles / California (2); Other / Unknown (2); Las Vegas / Nevada (1); California (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: California (2); Los Angeles / California (1); Southeast (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Other / Unknown (2); Southeast (1).
- institutional_capital: 1 article(s), high 0, medium 0, low 1, unknown 0. Top markets: Washington DC (1).

## Low Confidence / Unknown Articles

- Marcus & Millichap Arranges $14.2M Sale of 71-Unit Multifamily Property in Los Angeles (Yield PRO, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Affordable housing coming to 18444 Plummer St. in Northridge (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Modular units rise for affordable housing at 1141 N. Vermont Ave. in East Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Another LAX people mover delay, Brightline faces financial troubles, and more (Urbanize LA, Las Vegas / Nevada): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Mixed-use project takes shape at 5566 Pico Blvd. in Mid-City (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Gilbane Building 308-Unit Multifamily Student Housing Apartments in Raleigh (Yield PRO, Sun Belt): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- More design tweaks for infill housing at 810 N. Marengo Ave. in Pasadena (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 47 apartments completed at 2535 Alsace Ave. in West Adams (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Boston's High-Rise Multifamily Era Is Over. Developers Don't Expect It To Return Soon (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- 340-unit affordable housing complex debuts in Glendale (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable Housing Nearly Complete at 950 West Julian Street, San Jose (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Insights from Connect Apartments: Finding Opportunities in Challenges (VIDEO) (Connect CRE Apartments, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- McShane and Continental Properties Begin Construction on Their 25th Development Located in Opelika Alabama (Yield PRO, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- N. Phoenix Apartments Trade for $58.7M (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Austin Developer Greenlit to Build Apartment Units at Former School Site (Connect CRE Texas, Austin / Texas): Development-stage terms detected: zoning. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 24

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.