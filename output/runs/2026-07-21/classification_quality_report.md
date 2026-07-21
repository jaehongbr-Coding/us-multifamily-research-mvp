# Classification Quality Report

Generated: 2026-07-21 23:58:12

## Classification Summary

- Total articles classified: 83
- Topic distribution: transaction_market: 21; supply_demand: 13; capital_markets: 11; development_pipeline: 11; gp_activity: 11; macro_financing: 6; institutional_capital: 5; research_data: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 21 article(s), high 3, medium 11, low 7, unknown 0. Top markets: California (9); Los Angeles / California (2); Phoenix / Arizona (2); Other / Unknown (2); Miami / Florida (1).
- supply_demand: 13 article(s), high 0, medium 0, low 13, unknown 0. Top markets: Other / Unknown (7); National (5); Dallas / Texas (1).
- capital_markets: 11 article(s), high 5, medium 4, low 2, unknown 0. Top markets: Miami / Florida (3); New York City / New York (2); Phoenix / Arizona (2); Tampa / Florida (1); Dallas / Texas (1).
- development_pipeline: 11 article(s), high 0, medium 5, low 6, unknown 0. Top markets: Other / Unknown (3); Dallas / Texas (2); Los Angeles / California (2); Atlanta / Georgia (1); Sun Belt (1).
- gp_activity: 11 article(s), high 0, medium 0, low 1, unknown 10. Top markets: National (3); Los Angeles / California (2); Atlanta / Georgia (1); Sun Belt (1); Phoenix / Arizona (1).
- macro_financing: 6 article(s), high 0, medium 0, low 1, unknown 5. Top markets: Other / Unknown (3); California (1); Salt Lake City / Utah (1); Los Angeles / California (1).
- institutional_capital: 5 article(s), high 0, medium 4, low 1, unknown 0. Top markets: New York City / New York (2); Los Angeles / California (1); Riverside / California (1); California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); Southeast (1).
- other: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: San Francisco / California (1); Santa Monica / California (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- JLL secures $78.732M loan for The Flynn at Live Oak (Yield PRO, Dallas / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Los Angeles’ Moribund Multifamily Market Shows Signs of Life (Commercial Observer, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Developer nabs financing for affordable housing at 14th & Wilshire in Santa Monica (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Mixed-use project planned at 1134 N. La Brea Ave. in West Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Mixed-use building rises at 450 The Promenade N. in Downtown Long Beach (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- L.A. County approves plan for mixed-use complex in Willowbrook (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- New plan for housing approved at 4741 Libbit Ave. in Encino (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- U.S. Apartment Demand Outpaces New Supply for First Time Since 2022 (Connect CRE Apartments, National): Supply/demand terms detected: effective_rent_growth, vacancy, absorption. Primary topic set to supply_demand; confidence low.
- Avalon Bay Planning Apartments, Retail in South Miami (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- 320-Unit Gilbert Apartment Community Trades to Camden (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- Marcus & Millichap Capital Corporation Arranges $8M Financing for Boise Multifamily Property (Yield PRO, Salt Lake City / Utah): Financing type keywords detected: agency_debt. Primary topic set to macro_financing; confidence low.
- Construction goes vertical for mixed-use project at at 400 San Vicente Blvd. (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Grubb Properties Merges Funds To Create $1.9B Apartment REIT (Bisnow, New York City / New York): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Institutional activity terms detected: reit_activity. Primary topic set to institutional_capital; confidence low.
- Marcus & Millichap Arranges $3M Sale of Seattle Apartments (Yield PRO, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Rosewood Begins Leasing 359-Unit Multifamily Project in San Antonio (REBusiness Online, Dallas / Texas): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- PCCP Provides $51.8M Refi of Gilbert 236-Unit Multifamily Community (Connect CRE Apartments, Phoenix / Arizona): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 31

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.