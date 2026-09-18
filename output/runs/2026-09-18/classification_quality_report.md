# Classification Quality Report

Generated: 2026-09-18 01:04:47

## Classification Summary

- Total articles classified: 77
- Topic distribution: transaction_market: 16; supply_demand: 12; development_pipeline: 11; capital_markets: 9; gp_activity: 8; institutional_capital: 6; macro_financing: 6; other: 6
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 16 article(s), high 3, medium 9, low 4, unknown 0. Top markets: California (3); Atlanta / Georgia (3); Los Angeles / California (2); Sun Belt (1); Seattle (1).
- supply_demand: 12 article(s), high 0, medium 0, low 12, unknown 0. Top markets: Other / Unknown (6); National (4); New York (1); Texas (1).
- development_pipeline: 11 article(s), high 1, medium 3, low 7, unknown 0. Top markets: Other / Unknown (4); Miami / Florida (2); Atlanta / Georgia (2); Los Angeles / California (1); National (1).
- capital_markets: 9 article(s), high 4, medium 4, low 1, unknown 0. Top markets: Miami / Florida (3); Other / Unknown (2); New York City / New York (1); Denver / Colorado (1); Southeast (1).
- gp_activity: 8 article(s), high 0, medium 0, low 0, unknown 8. Top markets: Other / Unknown (3); National (2); Austin / Texas (1); Miami / Florida (1); Phoenix / Arizona (1).
- institutional_capital: 6 article(s), high 2, medium 4, low 0, unknown 0. Top markets: Other / Unknown (2); New York City / New York (2); Texas (1); Denver / Colorado (1).
- macro_financing: 6 article(s), high 0, medium 0, low 1, unknown 5. Top markets: Other / Unknown (4); California (1); Atlanta / Georgia (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Los Angeles / California (3); San Francisco / California (2); New York (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); Other / Unknown (1).

## Low Confidence / Unknown Articles

- Affordable housing proposed at 12508 W. Pacific Ave. in Mar Vista (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- L.A. County Supes approve apartments at 7914 Broadway Ave. in West Whittier (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Apartments slated for 3648 S. Empire Dr. in Palms (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing completed at 1408 W. 162nd St. in South L.A. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Affordable housing tops out at 10953 Whipple St. in Toluca Lake (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Construction Underway For Alexan Icon, South San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Plans Refiled for 395 3rd Street in SoMa, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- CBRE Facilitates $85M Sale of Beaverton Apartment Complex (Connect CRE Apartments, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Northmarq Arranges $67M Sale of Two Chicago-Area Apartment Properties (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Multifamily starts plummeted nearly 16% in August (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Marcus & Millichap Arranges $6.04M Sale of 31-Unit Multifamily Property in Los Angeles (Yield PRO, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Mixed-use building starts to rise at 8000 Beverly Blvd. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Ruben Cos. Says It Can't Sell, Finance Navy Yard Multifamily Project (Bisnow, New York): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Vango Development Launches Leasing at Third Rutherford-Area Property (Connect CRE Apartments, New York): Supply/demand terms detected: effective_rent_growth, occupancy. Primary topic set to supply_demand; confidence low.
- Subtext Completes 769-Bed Student Housing Development Near Arizona State University (REBusiness Online, Phoenix / Arizona): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- HTG Debuts $115M Miami Affordable Housing Project (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 27

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.