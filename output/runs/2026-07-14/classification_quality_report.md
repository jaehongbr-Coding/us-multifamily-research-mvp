# Classification Quality Report

Generated: 2026-07-14 23:54:20

## Classification Summary

- Total articles classified: 79
- Topic distribution: transaction_market: 19; capital_markets: 13; supply_demand: 12; development_pipeline: 9; gp_activity: 8; other: 6; research_data: 5; macro_financing: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 19 article(s), high 6, medium 6, low 7, unknown 0. Top markets: Phoenix / Arizona (4); California (3); Other / Unknown (3); Atlanta / Georgia (2); Miami / Florida (2).
- capital_markets: 13 article(s), high 8, medium 4, low 1, unknown 0. Top markets: Miami / Florida (3); Other / Unknown (3); California (2); New York (2); Texas (1).
- supply_demand: 12 article(s), high 0, medium 0, low 12, unknown 0. Top markets: Other / Unknown (7); National (3); Dallas / Texas (2).
- development_pipeline: 9 article(s), high 1, medium 3, low 5, unknown 0. Top markets: San Francisco / California (2); Atlanta / Georgia (2); Other / Unknown (2); California (1); Los Angeles / California (1).
- gp_activity: 8 article(s), high 0, medium 0, low 1, unknown 7. Top markets: Miami / Florida (2); National (2); Atlanta / Georgia (1); Los Angeles / California (1); Other / Unknown (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Washington DC (1); Los Angeles (1); California (1); Other / Unknown (1); Atlanta / Georgia (1).
- research_data: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (5).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (3); Los Angeles / California (1).
- institutional_capital: 3 article(s), high 1, medium 2, low 0, unknown 0. Top markets: Texas (1); Riverside / California (1); California (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Garden-Style Apartments Go for $78M in North County San Diego (Connect CRE, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- AMLI Residential plans 975 new homes at 100 West Walnut in Pasadena (Urbanize LA, Washington DC): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing reaches its peak at 1747 Stoner Ave. in Sawtelle (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 157-unit affordable housing complex rising at 7408 S. Figueroa Street (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing starts work at 11031 Aqua Vista Street in Studio City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing commences work at 5637 S. Broadway (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Behind the LAX people mover fiasco, CicLAvia returns on July 19, and more (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Longtime plan for Arts District apartments showing life signs at 1800 E. 7th Street (Urbanize LA, Los Angeles): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 78-unit affordable housing complex to rise at 12025 Hoffman St. in Studio City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Meeting Tomorrow For 470 West San Carlos Street, San Jose (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Formal Application For Empire Theater Redevelopment in West Portal, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Final Approval For 3896 Stevens Creek Boulevard, San Jose (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Northmarq Arranges Refinancing of 199-Unit Apartment Complex in Corpus Christi (REBusiness Online, Texas): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- 320-Unit Gilbert Apartment Community Trades to Camden (Connect CRE Apartments, Phoenix / Arizona): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- Sundance Bay Snags $95.7M Financing on Two Texas Rental Communities (Connect CRE Texas, Dallas / Texas): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Avalon Bay Planning Apartments, Retail in South Miami (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 28

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.