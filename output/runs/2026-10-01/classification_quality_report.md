# Classification Quality Report

Generated: 2026-10-01 01:50:23

## Classification Summary

- Total articles classified: 74
- Topic distribution: development_pipeline: 16; transaction_market: 12; capital_markets: 11; supply_demand: 9; gp_activity: 7; institutional_capital: 6; macro_financing: 6; research_data: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 16 article(s), high 0, medium 11, low 5, unknown 0. Top markets: Other / Unknown (5); New York City / New York (2); Phoenix / Arizona (2); Florida (2); Denver / Colorado (1).
- transaction_market: 12 article(s), high 3, medium 6, low 3, unknown 0. Top markets: California (4); Atlanta / Georgia (3); New York City / New York (2); Other / Unknown (1); Phoenix / Arizona (1).
- capital_markets: 11 article(s), high 3, medium 7, low 1, unknown 0. Top markets: Miami / Florida (4); Other / Unknown (2); Sun Belt (1); Phoenix / Arizona (1); Los Angeles / California (1).
- supply_demand: 9 article(s), high 0, medium 0, low 9, unknown 0. Top markets: Other / Unknown (7); National (2).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (4); National (2); Phoenix / Arizona (1).
- institutional_capital: 6 article(s), high 1, medium 4, low 1, unknown 0. Top markets: California (2); Miami / Florida (2); Washington DC (1); New York City / New York (1).
- macro_financing: 6 article(s), high 0, medium 0, low 1, unknown 5. Top markets: Los Angeles / California (2); Other / Unknown (2); Denver / Colorado (1); California (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Southeast (1); California (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (1); San Francisco / California (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- Proposed high-rise poised for another step forward at 1000 La Brea Ave. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing takes shape at 5110 Washington Blvd. in Mid-City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing coming to 18444 Plummer St. in Northridge (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Modular units rise for affordable housing at 1141 N. Vermont Ave. in East Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Griffis Residential Receives $86M in Financing for Denver Apartment Community (REBusiness Online, Denver / Colorado): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Mixed-use project takes shape at 5566 Pico Blvd. in Mid-City (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Insights from Connect Apartments: Finding Opportunities in Challenges (VIDEO) (Connect CRE California, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- WinnCompanies Funds $48M Transit-Oriented Mixed-Income Multifamily Project The Exchange Salem in Massachusetts (Yield PRO, National): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Preliminary Plans For 770 Golden Gate Avenue, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Related Affiliate Obtains $167M Loan Package for Miami Apartment Community (Connect CRE Apartments, Miami / Florida): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Institutional Property Advisors Closes $40.5M Multifamily Sale in San Diego County (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- 340-unit affordable housing complex debuts in Glendale (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- N. Phoenix Apartments Trade for $58.7M (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Investor Takes Over Distressed Atlanta Apartment Asset (Connect CRE Atlanta, Atlanta / Georgia): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Thompson Thrift Pursuing 319-Unit Powder Springs Rental Community (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: lease_up. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 19

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.