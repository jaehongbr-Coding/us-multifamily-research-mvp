# Classification Quality Report

Generated: 2026-07-09 00:10:33

## Classification Summary

- Total articles classified: 75
- Topic distribution: development_pipeline: 14; transaction_market: 14; supply_demand: 11; capital_markets: 8; gp_activity: 8; macro_financing: 7; other: 6; institutional_capital: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 14 article(s), high 1, medium 7, low 6, unknown 0. Top markets: Other / Unknown (5); Miami / Florida (2); Dallas / Texas (2); New York City / New York (2); California (1).
- transaction_market: 14 article(s), high 3, medium 5, low 6, unknown 0. Top markets: Phoenix / Arizona (4); Miami / Florida (3); Los Angeles / California (2); Dallas / Texas (2); Northern Virginia / Virginia (1).
- supply_demand: 11 article(s), high 1, medium 0, low 10, unknown 0. Top markets: Other / Unknown (8); National (3).
- capital_markets: 8 article(s), high 3, medium 5, low 0, unknown 0. Top markets: Miami / Florida (3); Phoenix / Arizona (1); California (1); New York City / New York (1); Colorado (1).
- gp_activity: 8 article(s), high 0, medium 0, low 0, unknown 8. Top markets: National (2); Los Angeles / California (1); Southeast (1); Atlanta / Georgia (1); Miami / Florida (1).
- macro_financing: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (3); Los Angeles / California (2); Houston / Texas (1); California (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Los Angeles / California (2); San Francisco / California (2); Beverly Hills / California (1); Dallas / Texas (1).
- institutional_capital: 5 article(s), high 2, medium 2, low 1, unknown 0. Top markets: Other / Unknown (2); California (1); Riverside / California (1); Miami / Florida (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Santa Monica / California (1); Los Angeles / California (1).

## Low Confidence / Unknown Articles

- Kennedy Wilson, Jamison partner on 4K affordable units in LA (Multifamily Dive, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Northmarq Arranges $21.7M Sale of Rise at the Northern Apartments in Phoenix (Yield PRO, Phoenix / Arizona): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Koreatown offices at 3700 Wilshire Blvd. to be converted to housing (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Fresh renderings for mixed-use project at 2716 Ocean Park Blvd. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Mixed-use affordable housing slated for 9700 W. Venice Blvd. in Palms (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 23 homes slated for 227 N. Swall Drive in Beverly Hills (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Avalon Bay Planning Apartments, Retail in South Miami (Connect CRE Apartments, Miami / Florida): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- 45-Unit Garden Apartment Property Trades in LA’s Palms Neighborhood (Connect CRE California, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Construction Tops Out at 19-Story Fulton Market Mixed-Use Development (Connect CRE, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Marcus & Millichap Arranges $4.75M Sale of Multifamily Community Fireside Apartments in Phoenix (Yield PRO, Phoenix / Arizona): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Southfield City Council Approves $65.1M Office Redevelopment Project in Metro Detroit (REBusiness Online, Other / Unknown): Development-stage terms detected: entitlement, redevelopment. Primary topic set to development_pipeline; confidence low.
- Trademark Opens The Vickery in Ft. Worth (Connect CRE Texas, Dallas / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Woodfield to Begin Construction on 285-Unit Apartment Community in Charleston (REBusiness Online, Southeast): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Developer Planning 220-Unit Homestead-Area Rental Community (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Dezer Advancing Plan for 600 N. Miami Apartment Units (Connect CRE South Florida, Miami / Florida): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Structural columns buckle on 21st floor of Manhattan adaptive reuse project (Multifamily Dive, New York City / New York): Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 26

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.