# Classification Quality Report

Generated: 2026-08-28 06:47:39

## Classification Summary

- Total articles classified: 80
- Topic distribution: development_pipeline: 19; transaction_market: 13; supply_demand: 12; gp_activity: 8; institutional_capital: 8; capital_markets: 6; other: 6; macro_financing: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 19 article(s), high 1, medium 7, low 11, unknown 0. Top markets: Other / Unknown (5); Atlanta / Georgia (4); California (2); New York City / New York (1); Washington DC (1).
- transaction_market: 13 article(s), high 5, medium 4, low 4, unknown 0. Top markets: California (4); Other / Unknown (3); New York City / New York (1); Miami / Florida (1); Seattle (1).
- supply_demand: 12 article(s), high 0, medium 0, low 12, unknown 0. Top markets: Other / Unknown (9); National (3).
- gp_activity: 8 article(s), high 0, medium 0, low 1, unknown 7. Top markets: Other / Unknown (4); Houston / Texas (2); Virginia (1); National (1).
- institutional_capital: 8 article(s), high 2, medium 3, low 3, unknown 0. Top markets: California (4); Other / Unknown (1); National (1); Miami / Florida (1); Atlanta / Georgia (1).
- capital_markets: 6 article(s), high 1, medium 4, low 1, unknown 0. Top markets: Los Angeles / California (1); Phoenix / Arizona (1); Houston / Texas (1); Other / Unknown (1); National (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Santa Monica / California (2); California (2); San Francisco / California (1); National (1).
- macro_financing: 5 article(s), high 0, medium 0, low 1, unknown 4. Top markets: Other / Unknown (2); Washington DC (1); Atlanta / Georgia (1); New York City / New York (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: California (1); Colorado (1); National (1).

## Low Confidence / Unknown Articles

- Stratford Partners JV Buys San Diego-Area Apartments for $34M (Commercial Observer, California): Capital event keywords detected: joint_venture, acquisition. Primary topic set to institutional_capital; confidence low.
- 12-story residential building pitched for 1517 15th St. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing on the rise at 728 Lagoon Ave. in Wilmington (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing slated for 2000 E. Colorado Blvd. in Pasadena (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Bonaventure Begins Construction on $93.3M Apartment Development in Metro Richmond (REBusiness Online, Virginia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Torrington Plans Residential Conversion of Danvers Residence Inn (Connect CRE Apartments, Other / Unknown): Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Bonaventure Breaks Ground on $93M Development in Virginia (Connect CRE Apartments, Washington DC): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low. Operator/property management activity detected.
- Chicago Firm Proposes 40-Story Apartment Tower In Mid-Market (Bisnow, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Meeting Tonight For 451 El Camino Real, Santa Clara (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Concord Summit Capital Arranges $28M in Financing for Metro Houston Mixed-Use Project (REBusiness Online, Houston / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Beyond the Rent: The economic signals multifamily leaders should watch this fall (Multifamily Dive, Washington DC): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- 408 apartments rise at 2828 N. MainPlace Dr. in Santa Ana (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Offices to make way for housing at 21221 S. Western Ave. in Torrance (Urbanize LA, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Sherman Associates Closes $136M Financing for Rochester MF Project (Connect CRE Apartments, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Cross Street, Mavrek Begin Leasing 46-Unit Apartment Building in Chicago (REBusiness Online, Other / Unknown): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Thompson Thrift to Begin Construction of 319-Unit Luxury Multifamily Community Near Atlanta (Yield PRO, Atlanta / Georgia): Development-stage terms detected: lease_up. Primary topic set to development_pipeline; confidence low.
- NRP Advancing 312-Unit Port St. Lucie Apartment Venture (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Belmora Apartments in Lakeview Launch Pre-Leasing (Connect CRE, National): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 33

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.