# Classification Quality Report

Generated: 2026-07-17 23:54:45

## Classification Summary

- Total articles classified: 96
- Topic distribution: transaction_market: 19; development_pipeline: 15; gp_activity: 14; supply_demand: 14; capital_markets: 12; institutional_capital: 10; macro_financing: 4; research_data: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 19 article(s), high 7, medium 7, low 5, unknown 0. Top markets: Los Angeles / California (4); California (3); Other / Unknown (3); Phoenix / Arizona (2); Virginia (1).
- development_pipeline: 15 article(s), high 2, medium 4, low 9, unknown 0. Top markets: Atlanta / Georgia (3); Other / Unknown (3); National (2); San Francisco / California (2); Los Angeles / California (1).
- gp_activity: 14 article(s), high 0, medium 0, low 1, unknown 13. Top markets: Other / Unknown (5); National (2); Atlanta / Georgia (1); Sun Belt (1); Miami / Florida (1).
- supply_demand: 14 article(s), high 1, medium 0, low 13, unknown 0. Top markets: Other / Unknown (7); National (5); New York City / New York (1); Miami / Florida (1).
- capital_markets: 12 article(s), high 4, medium 8, low 0, unknown 0. Top markets: Miami / Florida (3); Austin / Texas (2); New York City / New York (1); National (1); Washington DC (1).
- institutional_capital: 10 article(s), high 2, medium 5, low 3, unknown 0. Top markets: New York City / New York (2); Other / Unknown (2); New York (1); Houston / Texas (1); Riverside / California (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (3); Los Angeles / California (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Southeast (1); National (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Texas (1); Washington DC (1); Other / Unknown (1).
- entitlement_policy: 1 article(s), high 0, medium 1, low 0, unknown 0. Top markets: Denver / Colorado (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Apartments under construction at 5547 N. Elmer Ave. in North Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- 525 apartments start to rise at 22107 S. Vermont Ave. in West Carson (Urbanize LA, Texas): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 70-unit affordable housing complex underway at 1201 E. 119th St. in Watts (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing underway at 1035 S. Crenshaw Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- AMLI Residential plans 975 new homes at 100 West Walnut in Pasadena (Urbanize LA, Washington DC): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Avalon Bay Planning Apartments, Retail in South Miami (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- 320-Unit Gilbert Apartment Community Trades to Camden (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- Garden-Style Apartments Go for $78M in North County San Diego (Connect CRE California, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
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
- Multifamily starts climbed in June (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Additional low/unknown rows omitted: 35

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.