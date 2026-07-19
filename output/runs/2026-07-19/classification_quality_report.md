# Classification Quality Report

Generated: 2026-07-19 23:59:29

## Classification Summary

- Total articles classified: 96
- Topic distribution: transaction_market: 19; supply_demand: 16; gp_activity: 14; development_pipeline: 13; capital_markets: 12; institutional_capital: 9; other: 5; research_data: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 19 article(s), high 8, medium 6, low 5, unknown 0. Top markets: Los Angeles / California (4); California (3); Phoenix / Arizona (3); Other / Unknown (2); Nashville / Tennessee (1).
- supply_demand: 16 article(s), high 2, medium 0, low 14, unknown 0. Top markets: Other / Unknown (8); National (5); Dallas / Texas (1); New York City / New York (1); Miami / Florida (1).
- gp_activity: 14 article(s), high 0, medium 0, low 1, unknown 13. Top markets: Other / Unknown (5); National (2); Atlanta / Georgia (1); Sun Belt (1); Miami / Florida (1).
- development_pipeline: 13 article(s), high 1, medium 4, low 8, unknown 0. Top markets: Atlanta / Georgia (3); Other / Unknown (3); San Francisco / California (2); Los Angeles / California (1); Dallas / Texas (1).
- capital_markets: 12 article(s), high 3, medium 8, low 1, unknown 0. Top markets: Miami / Florida (3); Washington DC (2); New York City / New York (1); National (1); Virginia (1).
- institutional_capital: 9 article(s), high 2, medium 5, low 2, unknown 0. Top markets: New York City / New York (2); New York (1); Houston / Texas (1); Riverside / California (1); Other / Unknown (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (2); Texas (1); San Francisco / California (1); Santa Monica / California (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Southeast (1); National (1).
- macro_financing: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Other / Unknown (3).
- entitlement_policy: 1 article(s), high 0, medium 1, low 0, unknown 0. Top markets: Denver / Colorado (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- CBRE Facilitates Sale of Garden-Style Apartment for $78M in Ocean Side California (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Cushman & Wakefield Arranges $59M for Luxury Washington DC Multifamily Property The Ellington (Yield PRO, Washington DC): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Apartments under construction at 5547 N. Elmer Ave. in North Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- 525 apartments start to rise at 22107 S. Vermont Ave. in West Carson (Urbanize LA, Texas): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 70-unit affordable housing complex underway at 1201 E. 119th St. in Watts (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Avalon Bay Planning Apartments, Retail in South Miami (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- 320-Unit Gilbert Apartment Community Trades to Camden (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- Garden-Style Apartments Go for $78M in North County San Diego (Connect CRE California, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- $100M Luxury Apartment Complex Tower in Pre-Development Near Highland Park in Dallas (Yield PRO, Dallas / Texas): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Construction goes vertical for mixed-use project at at 400 San Vicente Blvd. (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Silicon Valley Cities See Spike In Office Demolitions (Bisnow, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: zoning. Primary topic set to development_pipeline; confidence low.
- Nicholas & Associates Tapped as Contractor for Ground-Up Multifamily Development in Madison (Connect CRE, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Renderings Revealed: $2.2-billion senior housing complex in Warner Center (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Missing Middle Housing For 2615 Ashby Avenue in Elmwood, Berkeley (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Apartment Developer Pursuing Phillips Place for Multifamily Community (Connect CRE Apartments, Atlanta / Georgia): Development-stage terms detected: zoning. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- NYC Multifamily Sales Reflect “Two Very Different Markets” in Q2 (Connect CRE Apartments, New York City / New York): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 36

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.