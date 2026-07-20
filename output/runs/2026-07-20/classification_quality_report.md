# Classification Quality Report

Generated: 2026-07-20 23:58:27

## Classification Summary

- Total articles classified: 88
- Topic distribution: development_pipeline: 19; transaction_market: 14; capital_markets: 13; supply_demand: 12; gp_activity: 11; institutional_capital: 7; macro_financing: 4; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 19 article(s), high 0, medium 9, low 10, unknown 0. Top markets: Other / Unknown (6); Los Angeles / California (4); Atlanta / Georgia (3); San Francisco / California (2); Nashville / Tennessee (1).
- transaction_market: 14 article(s), high 4, medium 7, low 3, unknown 0. Top markets: Other / Unknown (4); Phoenix / Arizona (2); Texas (1); Miami / Florida (1); Los Angeles / California (1).
- capital_markets: 13 article(s), high 6, medium 6, low 1, unknown 0. Top markets: Miami / Florida (4); Other / Unknown (3); Houston / Texas (2); Florida (1); Phoenix / Arizona (1).
- supply_demand: 12 article(s), high 0, medium 0, low 12, unknown 0. Top markets: Other / Unknown (7); National (5).
- gp_activity: 11 article(s), high 0, medium 0, low 1, unknown 10. Top markets: Other / Unknown (2); National (2); Atlanta / Georgia (1); Sun Belt (1); Miami / Florida (1).
- institutional_capital: 7 article(s), high 0, medium 5, low 2, unknown 0. Top markets: New York City / New York (1); Washington DC (1); Atlanta / Georgia (1); Los Angeles / California (1); Riverside / California (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (3); California (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Texas (1); San Francisco / California (1); Other / Unknown (1); Santa Monica / California (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Southeast (1); National (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Berkadia Arranges Sale, Financing of 270-Unit VA Multifamily Property (Connect CRE, Washington DC): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Mixed-use building rises at 450 The Promenade N. in Downtown Long Beach (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- L.A. County approves plan for mixed-use complex in Willowbrook (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- New plan for housing approved at 4741 Libbit Ave. in Encino (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Apartments under construction at 5547 N. Elmer Ave. in North Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- 525 apartments start to rise at 22107 S. Vermont Ave. in West Carson (Urbanize LA, Texas): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Graycliff Capital Offloads Two Augusta Apartment Communities (Connect CRE Apartments, Atlanta / Georgia): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Avalon Bay Planning Apartments, Retail in South Miami (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- 320-Unit Gilbert Apartment Community Trades to Camden (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- Construction goes vertical for mixed-use project at at 400 San Vicente Blvd. (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Silicon Valley Cities See Spike In Office Demolitions (Bisnow, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: zoning. Primary topic set to development_pipeline; confidence low.
- Renderings Revealed: $2.2-billion senior housing complex in Warner Center (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily starts climbed in June (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Multifamily rents ticked up in first half of 2026: Yardi (Multifamily Dive, Sun Belt): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Kiser Group Brokers $12M Sale of Rogers Park Apartment Building (Connect CRE, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Dallas Developer Duo Opens 168-Unit Mixed-Income Community (Connect CRE Texas, Dallas / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 31

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.