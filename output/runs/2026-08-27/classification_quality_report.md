# Classification Quality Report

Generated: 2026-08-27 04:18:46

## Classification Summary

- Total articles classified: 76
- Topic distribution: development_pipeline: 16; transaction_market: 12; supply_demand: 11; capital_markets: 9; institutional_capital: 9; gp_activity: 5; macro_financing: 5; other: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 16 article(s), high 0, medium 6, low 10, unknown 0. Top markets: Other / Unknown (3); Los Angeles / California (2); Atlanta / Georgia (2); Georgia (2); Sun Belt (1).
- transaction_market: 12 article(s), high 2, medium 7, low 3, unknown 0. Top markets: California (2); Other / Unknown (2); Seattle (2); Sun Belt (1); Georgia (1).
- supply_demand: 11 article(s), high 0, medium 0, low 11, unknown 0. Top markets: Other / Unknown (8); National (3).
- capital_markets: 9 article(s), high 3, medium 5, low 1, unknown 0. Top markets: Other / Unknown (2); San Francisco / California (1); Los Angeles / California (1); New York City / New York (1); Phoenix / Arizona (1).
- institutional_capital: 9 article(s), high 3, medium 1, low 5, unknown 0. Top markets: Other / Unknown (3); California (2); Phoenix / Arizona (1); Miami / Florida (1); New York (1).
- gp_activity: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (2); California (1); Dallas / Texas (1); National (1).
- macro_financing: 5 article(s), high 0, medium 0, low 1, unknown 4. Top markets: Other / Unknown (2); Washington DC (1); Atlanta / Georgia (1); New York City / New York (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: California (2); San Francisco / California (1); National (1); Santa Monica / California (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: California (1); Colorado (1); Los Angeles / California (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Affordable housing on the rise at 728 Lagoon Ave. in Wilmington (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing slated for 2000 E. Colorado Blvd. in Pasadena (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing complex slated for 5922 N. Lemp Ave. in North Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- City Planning Commission approves townhomes + storage facility at 7528 Bellaire Ave. in Sun Valley (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: planning_commission. Primary topic set to development_pipeline; confidence low.
- Merchants Capital Provides $193M in Financing for Two Affordable Housing Projects in Rocklin, California (REBusiness Online, California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Meeting Tonight For 451 El Camino Real, Santa Clara (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 40-Story Skyscraper Proposed Near Civic Center, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Berkadia Adds Experienced Multifamily Sales Team in Boston (Connect CRE, Other / Unknown): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Mixed-use project unwrapped at 3555 S. Overland Ave. in Palms (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Beyond the Rent: The economic signals multifamily leaders should watch this fall (Multifamily Dive, Washington DC): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- 408 apartments rise at 2828 N. MainPlace Dr. in Santa Ana (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Newmark Arranges Sale of The Bowie a 350-Unit Multifamily Community in Sandy Springs Georgi (Yield PRO, Georgia): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Offices to make way for housing at 21221 S. Western Ave. in Torrance (Urbanize LA, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- NRP Advancing 312-Unit Port St. Lucie Apartment Venture (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- The Vesper on Tennyson Apartments Now Leasing in Denver’s Historic Berkeley Neighborhood (Yield PRO, Denver / Colorado): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Landmark Properties Delivers 1,261-Bed Student Housing Near USC Campus (Connect CRE California, Los Angeles / California): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 29

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.