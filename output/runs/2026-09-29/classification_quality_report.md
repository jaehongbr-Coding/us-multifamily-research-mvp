# Classification Quality Report

Generated: 2026-09-29 02:30:11

## Classification Summary

- Total articles classified: 75
- Topic distribution: development_pipeline: 18; transaction_market: 14; capital_markets: 10; supply_demand: 10; gp_activity: 7; macro_financing: 7; institutional_capital: 5; other: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 18 article(s), high 1, medium 10, low 7, unknown 0. Top markets: Other / Unknown (9); Miami / Florida (3); Seattle (1); Houston / Texas (1); Austin / Texas (1).
- transaction_market: 14 article(s), high 4, medium 6, low 4, unknown 0. Top markets: California (4); Other / Unknown (3); Atlanta / Georgia (3); Texas (1); Dallas / Texas (1).
- capital_markets: 10 article(s), high 2, medium 7, low 1, unknown 0. Top markets: Miami / Florida (3); Phoenix / Arizona (2); Washington DC (1); New York City / New York (1); San Francisco / California (1).
- supply_demand: 10 article(s), high 0, medium 1, low 9, unknown 0. Top markets: Other / Unknown (7); National (2); New York City / New York (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (3); Phoenix / Arizona (2); Sun Belt (1); National (1).
- macro_financing: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Los Angeles / California (2); Other / Unknown (2); Las Vegas / Nevada (1); California (1); Atlanta / Georgia (1).
- institutional_capital: 5 article(s), high 0, medium 3, low 2, unknown 0. Top markets: Washington DC (2); National (2); Denver / Colorado (1).
- other: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Southeast (1); Other / Unknown (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: California (2).

## Low Confidence / Unknown Articles

- Northmarq Lends $19M for 154-Unit Multifamily Property in Pennsylvania (Connect CRE, Washington DC): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Modular units rise for affordable housing at 1141 N. Vermont Ave. in East Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Another LAX people mover delay, Brightline faces financial troubles, and more (Urbanize LA, Las Vegas / Nevada): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- At Connect Apartments 2026, Experts See “Generational Buying Opportunities” (Connect CRE California, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- More design tweaks for infill housing at 810 N. Marengo Ave. in Pasadena (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 47 apartments completed at 2535 Alsace Ave. in West Adams (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- 340-unit affordable housing complex debuts in Glendale (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable Housing Nearly Complete at 950 West Julian Street, San Jose (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Marcus & Millichap Arranges Sale of 206-Unit Indiana MF Property (Connect CRE, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- N. Phoenix Apartments Trade for $58.7M (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Austin Developer Greenlit to Build Apartment Units at Former School Site (Connect CRE Texas, Austin / Texas): Development-stage terms detected: zoning. Primary topic set to development_pipeline; confidence low.
- UAG expands leadership team to accelerate third-party management growth (Yield PRO, Sun Belt): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown. Operator/property management activity detected.
- Investor Takes Over Distressed Atlanta Apartment Asset (Connect CRE Atlanta, Atlanta / Georgia): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Thompson Thrift Pursuing 319-Unit Powder Springs Rental Community (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: lease_up. Primary topic set to development_pipeline; confidence low.
- Saratoga Capital Pays $98.4M at Auction for Atlanta Apartment Community (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Additional low/unknown rows omitted: 21

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.