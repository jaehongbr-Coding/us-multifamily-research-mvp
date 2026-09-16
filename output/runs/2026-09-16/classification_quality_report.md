# Classification Quality Report

Generated: 2026-09-16 01:08:28

## Classification Summary

- Total articles classified: 68
- Topic distribution: gp_activity: 13; capital_markets: 12; development_pipeline: 11; transaction_market: 11; supply_demand: 10; macro_financing: 4; other: 4; research_data: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- gp_activity: 13 article(s), high 0, medium 0, low 1, unknown 12. Top markets: Other / Unknown (5); Miami / Florida (2); Atlanta / Georgia (1); Houston / Texas (1); Austin / Texas (1).
- capital_markets: 12 article(s), high 4, medium 6, low 2, unknown 0. Top markets: Miami / Florida (4); Florida (3); Washington DC (1); New York City / New York (1); Seattle (1).
- development_pipeline: 11 article(s), high 2, medium 2, low 7, unknown 0. Top markets: Other / Unknown (6); Atlanta / Georgia (2); Los Angeles / California (1); Miami / Florida (1); National (1).
- transaction_market: 11 article(s), high 2, medium 7, low 2, unknown 0. Top markets: Atlanta / Georgia (3); Other / Unknown (2); California (2); Los Angeles / California (1); Phoenix / Arizona (1).
- supply_demand: 10 article(s), high 0, medium 0, low 10, unknown 0. Top markets: Other / Unknown (6); National (2); San Francisco / California (1); Los Angeles / California (1).
- macro_financing: 4 article(s), high 0, medium 0, low 1, unknown 3. Top markets: Other / Unknown (2); California (1); Atlanta / Georgia (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); California (1); San Francisco / California (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); Southeast (1).
- institutional_capital: 1 article(s), high 0, medium 1, low 0, unknown 0. Top markets: California (1).

## Low Confidence / Unknown Articles

- Stewards Sets Up $240M Deal for Two South Florida Multifamily Properties (Commercial Observer, Miami / Florida): Development-stage terms detected: density_bonus. Primary topic set to gp_activity; confidence low.
- Affordable housing tops out at 10953 Whipple St. in Toluca Lake (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Echo Park-adjacent apartments proposed at 820 N. Laguna Ave. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Metrolink fares rise, California condos dying, and more (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 13 apartments approved for empty lot at 4127 E. Supreme Court (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Plans Refiled for 395 3rd Street in SoMa, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Newmark Arranges $55M Refinancing for Seattle Multifamily Property (Connect CRE Apartments, Seattle): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- With Occupancy Brimming, Investors Pile Into Bay Area Apartments (Bisnow, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Supply/demand terms detected: occupancy. Primary topic set to supply_demand; confidence low.
- Your Third Spot, Buttermilk Cafe to Open at Veridian in Schaumburg, Illinois (REBusiness Online, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- HTG Debuts $115M Miami Affordable Housing Project (Connect CRE Apartments, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Rice Planning 24-Story Multifamily Community (Connect CRE Apartments, Houston / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- JLB Pursuing Buckhead Office-to-Apartments Conversion (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Target to Add Austin-Area Store (Connect CRE Texas, Austin / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Investor Takes Over Distressed Atlanta Apartment Asset (Connect CRE Atlanta, Atlanta / Georgia): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Thompson Thrift Pursuing 319-Unit Powder Springs Rental Community (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: lease_up. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 24

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.