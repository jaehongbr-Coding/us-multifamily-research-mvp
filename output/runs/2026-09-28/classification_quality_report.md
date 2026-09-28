# Classification Quality Report

Generated: 2026-09-28 01:26:27

## Classification Summary

- Total articles classified: 75
- Topic distribution: transaction_market: 17; development_pipeline: 15; gp_activity: 12; supply_demand: 10; macro_financing: 8; institutional_capital: 5; capital_markets: 4; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 17 article(s), high 5, medium 7, low 5, unknown 0. Top markets: California (3); Atlanta / Georgia (3); Los Angeles / California (2); San Francisco / California (2); Other / Unknown (1).
- development_pipeline: 15 article(s), high 0, medium 6, low 9, unknown 0. Top markets: Other / Unknown (6); Miami / Florida (3); Atlanta / Georgia (2); Los Angeles / California (1); Dallas / Texas (1).
- gp_activity: 12 article(s), high 0, medium 0, low 1, unknown 11. Top markets: Other / Unknown (4); Phoenix / Arizona (2); New York City / New York (1); Los Angeles / California (1); Southeast (1).
- supply_demand: 10 article(s), high 0, medium 1, low 9, unknown 0. Top markets: Other / Unknown (7); National (2); Colorado (1).
- macro_financing: 8 article(s), high 0, medium 0, low 1, unknown 7. Top markets: Los Angeles / California (2); Other / Unknown (2); Las Vegas / Nevada (1); Beverly Hills / California (1); California (1).
- institutional_capital: 5 article(s), high 0, medium 3, low 2, unknown 0. Top markets: Washington DC (2); New York (1); Las Vegas / Nevada (1); Other / Unknown (1).
- capital_markets: 4 article(s), high 1, medium 3, low 0, unknown 0. Top markets: Other / Unknown (2); New York (1); Miami / Florida (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: California (1); Southeast (1); Denver / Colorado (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- Berkadia Arranges Sale and Financing for 92-Unit MQH Apartments in Fuquay-Varina North Carolina (Yield PRO, New York): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Marcus & Millichap Arranges Sale of 24-Unit Multifamily Property The Marq Apartments in Los Angeles California (Yield PRO, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Another LAX people mover delay, Brightline faces financial troubles, and more (Urbanize LA, Las Vegas / Nevada): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- 270 apartments take shape at 200 E. First American Way in Santa Ana (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Construction goes vertical for mixed-use project at 155 W. 6th St. in San Pedro (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Apartment complex fully framed at 11250 La Grange Ave. in Sawtelle (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Extell Seeks $3.8B Financing for Condos on Former ABC-TV Campus (Connect CRE Apartments, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- LA City Council Approves Largest-Ever Funding Pool for Affordable Housing (Connect CRE California, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Russian Hill Apartments Trade After 50 Years of Family Ownership (Connect CRE California, San Francisco / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- More design tweaks for infill housing at 810 N. Marengo Ave. in Pasadena (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 47 apartments completed at 2535 Alsace Ave. in West Adams (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- At Connect Apartments 2026, Experts See “Generational Buying Opportunities” (Connect CRE, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Skyline Developers Completes 97-Unit Apartment Building in Midtown Manhattan (REBusiness Online, New York City / New York): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- HTG Debuts $115M Miami Affordable Housing Project (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- N. Phoenix Apartments Trade for $58.7M (Connect CRE Apartments, Phoenix / Arizona): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 29

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.