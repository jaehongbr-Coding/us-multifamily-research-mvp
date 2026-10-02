# Classification Quality Report

Generated: 2026-10-02 02:02:20

## Classification Summary

- Total articles classified: 71
- Topic distribution: development_pipeline: 18; transaction_market: 11; supply_demand: 10; capital_markets: 9; gp_activity: 7; institutional_capital: 5; macro_financing: 5; research_data: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 18 article(s), high 2, medium 8, low 8, unknown 0. Top markets: Other / Unknown (6); Phoenix / Arizona (3); California (2); Miami / Florida (1); Texas (1).
- transaction_market: 11 article(s), high 2, medium 7, low 2, unknown 0. Top markets: Atlanta / Georgia (3); Other / Unknown (2); Phoenix / Arizona (2); Seattle (1); California (1).
- supply_demand: 10 article(s), high 0, medium 0, low 10, unknown 0. Top markets: Other / Unknown (7); National (3).
- capital_markets: 9 article(s), high 6, medium 3, low 0, unknown 0. Top markets: Nashville / Tennessee (2); Los Angeles / California (1); New York (1); Phoenix / Arizona (1); Florida (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (4); National (2); Phoenix / Arizona (1).
- institutional_capital: 5 article(s), high 1, medium 3, low 1, unknown 0. Top markets: Los Angeles / California (1); Dallas / Texas (1); California (1); Salt Lake City / Utah (1); Miami / Florida (1).
- macro_financing: 5 article(s), high 0, medium 0, low 1, unknown 4. Top markets: Los Angeles / California (2); Other / Unknown (2); California (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (3); Southeast (1).
- other: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); San Francisco / California (1).

## Low Confidence / Unknown Articles

- Proposed high-rise poised for another step forward at 1000 La Brea Ave. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing takes shape at 5110 Washington Blvd. in Mid-City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing coming to 18444 Plummer St. in Northridge (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Modular units rise for affordable housing at 1141 N. Vermont Ave. in East Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Mixed-use project takes shape at 5566 Pico Blvd. in Mid-City (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Preliminary Plans For 770 Golden Gate Avenue, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Related Affiliate Obtains $167M Loan Package for Miami Apartment Community (Connect CRE South Florida, Miami / Florida): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Thompson Thrift to Develop 300-Unit The Highline Apartment Property Near Boise (REBusiness Online, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- New details for affordable housing at 1150 Sunset Blvd. in Echo Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- N. Phoenix Apartments Trade for $58.7M (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Alamo Heights Apartment Owners Eyeing Major Addition (Connect CRE Apartments, Texas): Development-stage terms detected: zoning. Primary topic set to development_pipeline; confidence low.
- Investor Takes Over Distressed Atlanta Apartment Asset (Connect CRE Atlanta, Atlanta / Georgia): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Thompson Thrift Pursuing 319-Unit Powder Springs Rental Community (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: lease_up. Primary topic set to development_pipeline; confidence low.
- Shorter Apartment Construction Time in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery, permit. Primary topic set to development_pipeline; confidence low.
- NFL Team Owner Building 504-Unit N. Phoenix Apartment Project (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 19

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.