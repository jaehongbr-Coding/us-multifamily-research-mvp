# Classification Quality Report

Generated: 2026-07-07 23:59:00

## Classification Summary

- Total articles classified: 81
- Topic distribution: development_pipeline: 20; transaction_market: 13; supply_demand: 11; capital_markets: 9; institutional_capital: 8; gp_activity: 6; macro_financing: 6; other: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 20 article(s), high 1, medium 11, low 8, unknown 0. Top markets: Other / Unknown (4); Atlanta / Georgia (3); Los Angeles / California (2); Miami / Florida (2); California (2).
- transaction_market: 13 article(s), high 1, medium 6, low 6, unknown 0. Top markets: Phoenix / Arizona (3); Los Angeles / California (2); New York City / New York (2); Dallas / Texas (1); Atlanta / Georgia (1).
- supply_demand: 11 article(s), high 1, medium 0, low 10, unknown 0. Top markets: Other / Unknown (8); National (3).
- capital_markets: 9 article(s), high 5, medium 4, low 0, unknown 0. Top markets: Other / Unknown (3); California (2); Miami / Florida (2); Seattle (1); National (1).
- institutional_capital: 8 article(s), high 1, medium 5, low 2, unknown 0. Top markets: National (2); Other / Unknown (2); California (1); Riverside / California (1); Florida (1).
- gp_activity: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: National (2); Atlanta / Georgia (1); Miami / Florida (1); Other / Unknown (1); New York City / New York (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (4); New York (1); Los Angeles / California (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Beverly Hills / California (1); Santa Monica / California (1); San Francisco / California (1); Miami / Florida (1); Dallas / Texas (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); Santa Monica / California (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Fresh renderings for mixed-use project at 2716 Ocean Park Blvd. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Mixed-use affordable housing slated for 9700 W. Venice Blvd. in Palms (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 23 homes slated for 227 N. Swall Drive in Beverly Hills (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- SB 79 takes effect, Measure ULA to remain, and more (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- City Council upholds approval of mixed-use project at 1410 Main St. in Venice (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- New details for plans to convert L.A. World Trade center into affordable housing (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 45-Unit Garden Apartment Property Trades in LA’s Palms Neighborhood (Connect CRE Apartments, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Meridian Arranges 10-Year Refi Loan for Kew Gardens Apartments (Connect CRE, New York): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Nuveen Buys Pair of Upper West Side Multifamily Properties for $75M (Commercial Observer, New York City / New York): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Trademark Opens The Vickery in Ft. Worth (Connect CRE Texas, Dallas / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Walker & Dunlop Arranges $232M Financing for Workforce Housing Portfolio (Yield PRO, Florida): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- KTGY and SHAC Mark Announce Groundbreaking of 11 El Camino Real in San Carlos California (Yield PRO, California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Berkadia Hires C&W’s Blake Okland as Chief Revenue Officer (Commercial Observer, National): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Developer Planning 220-Unit Homestead-Area Rental Community (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Trevato Breaks Ground on $120M Multifamily Development at Former Water Park in Jacksonville Beach (REBusiness Online, Florida): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Dezer Advancing Plan for 600 N. Miami Apartment Units (Connect CRE South Florida, Miami / Florida): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 26

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.