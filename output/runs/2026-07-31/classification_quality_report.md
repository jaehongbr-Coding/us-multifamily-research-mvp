# Classification Quality Report

Generated: 2026-07-31 00:02:52

## Classification Summary

- Total articles classified: 90
- Topic distribution: transaction_market: 22; capital_markets: 15; supply_demand: 12; development_pipeline: 11; gp_activity: 11; other: 7; institutional_capital: 6; macro_financing: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 22 article(s), high 5, medium 11, low 6, unknown 0. Top markets: Other / Unknown (10); California (3); Los Angeles / California (2); Atlanta / Georgia (2); San Francisco / California (1).
- capital_markets: 15 article(s), high 4, medium 9, low 2, unknown 0. Top markets: Miami / Florida (4); Phoenix / Arizona (3); New York (2); Baton Rouge / Louisiana (1); Florida (1).
- supply_demand: 12 article(s), high 0, medium 0, low 12, unknown 0. Top markets: Other / Unknown (8); National (4).
- development_pipeline: 11 article(s), high 0, medium 5, low 6, unknown 0. Top markets: Other / Unknown (4); Atlanta / Georgia (1); New York City / New York (1); National (1); Miami / Florida (1).
- gp_activity: 11 article(s), high 0, medium 0, low 0, unknown 11. Top markets: Los Angeles / California (2); Miami / Florida (2); Dallas / Texas (2); National (2); Atlanta / Georgia (1).
- other: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Los Angeles / California (2); Santa Monica / California (1); Southeast (1); Other / Unknown (1); New York City / New York (1).
- institutional_capital: 6 article(s), high 1, medium 3, low 2, unknown 0. Top markets: Atlanta / Georgia (2); Riverside / California (2); California (1); Other / Unknown (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (4).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (2).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- $42.75M Refinancing Secured for 301-Unit Luxury Community in Louisiana’s Capital City (Yield PRO, Baton Rouge / Louisiana): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- JLL Arranges the Sale of Twelve 501 Apartments in South Central Twin Cities Suburb (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- CBRE Completes Receivership Sale of Santa Monica Apartments (Connect CRE, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Draft EIR released for Metro-adjacent high-rise at 5350 Wilshire Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 102 apartments break ground at 1717 S. Beloit Ave. in Sawtelle (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Developer pivots to affordable housing at 7715 Crenshaw Blvd. in Hyde Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Affordable housing takes shape at 4706 Centinela Ave. in Del Rey (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Mixed-use building slated for 20160 Roscoe Blvd. in Winnetka (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Updated Permits Approved for 690 Concar Drive in San Mateo (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement, permit. Primary topic set to development_pipeline; confidence low.
- NY Investor Snags First Folsom Apartments on Market in Four Years (Connect CRE California, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Checking in on Alexan West End at 600 Broadway in Long Beach (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Kidder Mathews Arranges Sale of Apartments in Ellensburg (Connect CRE Apartments, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Abby Goldenfarb Joins WinnDevelopment as SVP (Connect CRE, National): Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- PCCP Provides $51.8M Refi of Gilbert 236-Unit Multifamily Community (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Miami's Condo Craze Has Developers Spending Millions On Sales Galleries (Bisnow, Miami / Florida): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Crescent Building 248-Unit Rental Property in N. Phoenix (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 32

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.