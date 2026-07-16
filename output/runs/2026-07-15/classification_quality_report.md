# Classification Quality Report

Generated: 2026-07-15 23:59:36

## Classification Summary

- Total articles classified: 79
- Topic distribution: transaction_market: 16; supply_demand: 15; capital_markets: 11; gp_activity: 10; development_pipeline: 7; macro_financing: 6; institutional_capital: 5; research_data: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 16 article(s), high 3, medium 8, low 5, unknown 0. Top markets: Other / Unknown (5); California (3); Atlanta / Georgia (2); Miami / Florida (2); Phoenix / Arizona (2).
- supply_demand: 15 article(s), high 0, medium 2, low 13, unknown 0. Top markets: Other / Unknown (9); National (4); Dallas / Texas (2).
- capital_markets: 11 article(s), high 6, medium 5, low 0, unknown 0. Top markets: Miami / Florida (4); New York (2); Washington DC (1); Florida (1); Dallas / Texas (1).
- gp_activity: 10 article(s), high 0, medium 0, low 1, unknown 9. Top markets: Other / Unknown (2); National (2); Atlanta / Georgia (1); Miami / Florida (1); Los Angeles / California (1).
- development_pipeline: 7 article(s), high 1, medium 3, low 3, unknown 0. Top markets: San Francisco / California (2); Atlanta / Georgia (2); Other / Unknown (2); Los Angeles / California (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (4); Los Angeles / California (1); Connecticut (1).
- institutional_capital: 5 article(s), high 0, medium 3, low 2, unknown 0. Top markets: Dallas / Texas (1); Los Angeles / California (1); Riverside / California (1); California (1); Georgia (1).
- research_data: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (4); National (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Washington DC (1); California (1); Atlanta / Georgia (1); New York City / New York (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Greystar Reveals Plans For 20,000-Home Garden-Style BTR Push (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affordable housing underway at 1035 S. Crenshaw Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- AMLI Residential plans 975 new homes at 100 West Walnut in Pasadena (Urbanize LA, Washington DC): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing reaches its peak at 1747 Stoner Ave. in Sawtelle (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 157-unit affordable housing complex rising at 7408 S. Figueroa Street (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing starts work at 11031 Aqua Vista Street in Studio City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing commences work at 5637 S. Broadway (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Preliminary Permits Resubmitted For 1234 Great Highway, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Meeting Tomorrow For 470 West San Carlos Street, San Jose (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Formal Application For Empire Theater Redevelopment in West Portal, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Garden-Style Apartments Go for $78M in North County San Diego (Connect CRE Apartments, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Sundance Bay Snags $95.7M Financing on Two Texas Rental Communities (Connect CRE Texas, Dallas / Texas): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Avalon Bay Planning Apartments, Retail in South Miami (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- 320-Unit Gilbert Apartment Community Trades to Camden (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- R.D. Olson Construction Builds Affordable Developments Advancing Warner Center 2035 Plan in Woodland Hills California (Yield PRO, Los Angeles / California): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Ziegler Arranges $304M Tax-Exempt Bond for Groton Senior Living Expansion (Connect CRE, Connecticut): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Additional low/unknown rows omitted: 28

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.