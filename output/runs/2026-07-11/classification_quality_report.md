# Classification Quality Report

Generated: 2026-07-11 23:55:45

## Classification Summary

- Total articles classified: 77
- Topic distribution: transaction_market: 15; supply_demand: 14; capital_markets: 11; development_pipeline: 11; gp_activity: 7; macro_financing: 7; other: 7; institutional_capital: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 15 article(s), high 7, medium 5, low 3, unknown 0. Top markets: Other / Unknown (3); Los Angeles / California (2); Seattle (2); Miami / Florida (2); Phoenix / Arizona (2).
- supply_demand: 14 article(s), high 1, medium 0, low 13, unknown 0. Top markets: Other / Unknown (8); National (3); Houston / Texas (1); Atlanta / Georgia (1); Austin / Texas (1).
- capital_markets: 11 article(s), high 5, medium 5, low 1, unknown 0. Top markets: Miami / Florida (4); New York City / New York (3); California (2); Houston / Texas (1); Florida (1).
- development_pipeline: 11 article(s), high 0, medium 5, low 6, unknown 0. Top markets: Other / Unknown (6); Phoenix / Arizona (1); Georgia (1); New York City / New York (1); Houston / Texas (1).
- gp_activity: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Miami / Florida (2); National (2); Los Angeles / California (1); Atlanta / Georgia (1); Other / Unknown (1).
- macro_financing: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (4); Los Angeles / California (2); Houston / Texas (1).
- other: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Los Angeles / California (4); Los Angeles (1); Other / Unknown (1); New York City / New York (1).
- institutional_capital: 4 article(s), high 0, medium 4, low 0, unknown 0. Top markets: New York (1); Louisville / Kentucky (1); Riverside / California (1); San Francisco / California (1).
- research_data: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: Los Angeles / California (1).

## Low Confidence / Unknown Articles

- Kennedy Wilson, Jamison partner on 4K affordable units in LA (Multifamily Dive, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- 108-Unit Northern Phoenix Value-Add Apartment Community Changes Hands (Yield PRO, Phoenix / Arizona): Development-stage terms detected: renovation_repositioning. Primary topic set to development_pipeline; confidence low.
- Northmarq Brokers $5.25M Sale of 105-Unit Silver Lake Development Site in Los Angeles (Yield PRO, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Behind the LAX people mover fiasco, CicLAvia returns on July 19, and more (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Longtime plan for Arts District apartments showing life signs at 1800 E. 7th Street (Urbanize LA, Los Angeles): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 78-unit affordable housing complex to rise at 12025 Hoffman St. in Studio City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Seven apartments coming to 217 N. Ave. 55 in Highland Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Koreatown offices at 3700 Wilshire Blvd. to be converted to housing (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Avalon Bay Planning Apartments, Retail in South Miami (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Wood framing rises for mixed-use building at 9431 Venice Blvd. in Palms (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Groundbreaking For 11 El Camino Real, San Carlos (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Raven Capital Completes 33-Story Multifamily High-Rise in Houston’s Museum District (REBusiness Online, Houston / Texas): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Preliminary Permits For 2032 Francisco Street, North Berkeley (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Dezer Advancing Plan for 600 N. Miami Apartment Units (Connect CRE South Florida, Miami / Florida): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Structural columns buckle on 21st floor of Manhattan adaptive reuse project (Multifamily Dive, New York City / New York): Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Icon Real Estate Advisors Arranges $3.1M Sale of Clifton New Jersey Mixed-Use Multifamily Property (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Additional low/unknown rows omitted: 25

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.