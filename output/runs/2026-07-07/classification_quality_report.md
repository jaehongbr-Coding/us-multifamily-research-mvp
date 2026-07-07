# Classification Quality Report

Generated: 2026-07-07 00:09:48

## Classification Summary

- Total articles classified: 91
- Topic distribution: transaction_market: 20; development_pipeline: 18; supply_demand: 12; capital_markets: 10; gp_activity: 8; macro_financing: 8; institutional_capital: 6; other: 6
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 20 article(s), high 3, medium 8, low 9, unknown 0. Top markets: Other / Unknown (3); Atlanta / Georgia (3); Georgia (2); New York City / New York (2); Phoenix / Arizona (2).
- development_pipeline: 18 article(s), high 1, medium 7, low 10, unknown 0. Top markets: Other / Unknown (7); Los Angeles / California (2); Miami / Florida (2); California (2); Dallas / Texas (2).
- supply_demand: 12 article(s), high 1, medium 1, low 10, unknown 0. Top markets: Other / Unknown (8); National (3); Seattle (1).
- capital_markets: 10 article(s), high 7, medium 3, low 0, unknown 0. Top markets: Other / Unknown (5); New York City / New York (2); California (2); Miami / Florida (1).
- gp_activity: 8 article(s), high 0, medium 0, low 0, unknown 8. Top markets: Atlanta / Georgia (2); National (2); Miami / Florida (1); Other / Unknown (1); Tampa / Florida (1).
- macro_financing: 8 article(s), high 0, medium 0, low 0, unknown 8. Top markets: Other / Unknown (4); Los Angeles / California (2); New York City / New York (1); Sun Belt (1).
- institutional_capital: 6 article(s), high 1, medium 2, low 3, unknown 0. Top markets: California (1); Riverside / California (1); Atlanta / Georgia (1); Other / Unknown (1); Los Angeles / California (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Los Angeles / California (2); Beverly Hills / California (1); Santa Monica / California (1); Miami / Florida (1); Other / Unknown (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (3).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Cushman & Wakefield Brokers $87M Sale of Mason Augusta Apartment Community (Yield PRO, Georgia): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Revised Plan for Pacific Park Development Could Bring 5,600 Multifamily Apartment Units to Downtown Brooklyn (Yield PRO, New York City / New York): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- CBRE Arranges $24M Sale of 87-UnitMultiffamily Apartment Property in Seattle (Yield PRO, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- 45-Unit Garden Apartment Property Trades in LA’s Palms Neighborhood (Connect CRE, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Mixed-use affordable housing slated for 9700 W. Venice Blvd. in Palms (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 23 homes slated for 227 N. Swall Drive in Beverly Hills (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- SB 79 takes effect, Measure ULA to remain, and more (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- City Council upholds approval of mixed-use project at 1410 Main St. in Venice (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- New details for plans to convert L.A. World Trade center into affordable housing (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 62 apartments underway at 11103 Hartsook Ave. in North Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing completed at 3300 Washington Blvd. in Arlington Heights (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Affordable Housing Approved For 175 Marinwood Avenue, Marin County (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Trademark Opens The Vickery in Ft. Worth (Connect CRE Apartments, Dallas / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Fairfield Completes 14-Story Houston Multifamily Tower (Connect CRE Texas, Houston / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Aimco Liquidates Last of Its NYC Portfolio in $23M Sale (Commercial Observer, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Denver Apartment Venture Trades at Steep Loss (Connect CRE, Phoenix / Arizona): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Additional low/unknown rows omitted: 37

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.