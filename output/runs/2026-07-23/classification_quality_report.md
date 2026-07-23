# Classification Quality Report

Generated: 2026-07-23 00:02:39

## Classification Summary

- Total articles classified: 83
- Topic distribution: gp_activity: 14; transaction_market: 14; development_pipeline: 12; supply_demand: 12; capital_markets: 11; institutional_capital: 9; macro_financing: 7; other: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- gp_activity: 14 article(s), high 0, medium 0, low 1, unknown 13. Top markets: National (3); New York City / New York (2); Other / Unknown (2); Los Angeles / California (1); Atlanta / Georgia (1).
- transaction_market: 14 article(s), high 3, medium 6, low 5, unknown 0. Top markets: California (6); Other / Unknown (3); Northern Virginia / Virginia (1); Miami / Florida (1); Phoenix / Arizona (1).
- development_pipeline: 12 article(s), high 1, medium 7, low 4, unknown 0. Top markets: Other / Unknown (3); Atlanta / Georgia (2); Los Angeles / California (2); Seattle (1); Dallas / Texas (1).
- supply_demand: 12 article(s), high 0, medium 0, low 12, unknown 0. Top markets: Other / Unknown (7); National (4); New York City / New York (1).
- capital_markets: 11 article(s), high 4, medium 6, low 1, unknown 0. Top markets: Phoenix / Arizona (4); Dallas / Texas (2); Miami / Florida (2); Los Angeles / California (1); Washington DC (1).
- institutional_capital: 9 article(s), high 1, medium 5, low 3, unknown 0. Top markets: New York City / New York (2); Los Angeles / California (2); Other / Unknown (1); Riverside / California (1); West Palm Beach / Florida (1).
- macro_financing: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (4); California (1); Los Angeles / California (1); National (1).
- other: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Santa Monica / California (1); California (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (2).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- CDK Lending Supplies $37M Loan for Newark Apartments Project (Commercial Observer, Other / Unknown): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Kennedy Wilson plans 133 apartments at 700 Colorado Ave. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Workforce housing for Metro employees could rise at 4421 S. Crenshaw Blvd. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Developer nabs financing for affordable housing at 14th & Wilshire in Santa Monica (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Mixed-use project planned at 1134 N. La Brea Ave. in West Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Mixed-use building rises at 450 The Promenade N. in Downtown Long Beach (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- L.A. County approves plan for mixed-use complex in Willowbrook (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- New plan for housing approved at 4741 Libbit Ave. in Encino (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Dallas Apartment Builder Inks $78.7M Refi (Connect CRE Apartments, Dallas / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Avalon Bay Planning Apartments, Retail in South Miami (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- 320-Unit Gilbert Apartment Community Trades to Camden (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- NYC’s Conversion Break Producing Far More Units Than New-Construction Sweetener (Commercial Observer, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Grubb Properties Merges Funds To Create $1.9B Apartment REIT (Bisnow, New York City / New York): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Institutional activity terms detected: reit_activity. Primary topic set to institutional_capital; confidence low.
- BWE Secures $100M First Mortgage Financing for Luxury Multifamily Apartments in Midtown Manhattan (Yield PRO, New York City / New York): Institutional activity terms detected: gp_acquisition, gp_disposition. Primary topic set to institutional_capital; confidence low.
- Bascom Buys 183-Unit Orange County, Calif., Complex for $53M (Commercial Observer, California): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- PCCP Provides $51.8M Refi of Gilbert 236-Unit Multifamily Community (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 30

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.