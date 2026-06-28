# Classification Quality Report

Generated: 2026-06-28 00:03:36

## Classification Summary

- Total articles classified: 77
- Topic distribution: capital_markets: 15; supply_demand: 12; transaction_market: 11; development_pipeline: 10; institutional_capital: 9; gp_activity: 7; other: 6; macro_financing: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- capital_markets: 15 article(s), high 8, medium 6, low 1, unknown 0. Top markets: National (3); California (3); San Francisco / California (1); New York (1); Atlanta / Georgia (1).
- supply_demand: 12 article(s), high 1, medium 1, low 10, unknown 0. Top markets: Other / Unknown (7); National (4); Austin / Texas (1).
- transaction_market: 11 article(s), high 3, medium 7, low 1, unknown 0. Top markets: Other / Unknown (4); Phoenix / Arizona (2); Miami / Florida (2); Atlanta / Georgia (1); Austin / Texas (1).
- development_pipeline: 10 article(s), high 1, medium 4, low 5, unknown 0. Top markets: Miami / Florida (3); Other / Unknown (2); New York City / New York (2); Los Angeles / California (1); California (1).
- institutional_capital: 9 article(s), high 0, medium 7, low 2, unknown 0. Top markets: Riverside / California (4); Dallas / Texas (2); Other / Unknown (2); New York City / New York (1).
- gp_activity: 7 article(s), high 0, medium 0, low 2, unknown 5. Top markets: National (3); California (2); Other / Unknown (1); Atlanta / Georgia (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Los Angeles / California (4); Washington DC (1); New York City / New York (1).
- macro_financing: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (3); Santa Monica / California (1); New York City / New York (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (2).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Affordable housing on the rise at 1405 S. Broadway in DTLA (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 100 rental townhomes deput at 1771 Blake Ave. in Frogtown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing fully-framed at 4129 Centinela Ave. in Del Rey (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Construction goes vertical for mixed-use project at 1902 Wilshire Blvd. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affordable housing under constructiona t 1740 N. Wilton Place in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- MMCC Arranges $54M HUD-Insured Loan for Refinancing of Metro Houston Apartment Community (REBusiness Online, Houston / Texas): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- ULA bill fizzles in Sacramento, LAX people mover delays, and more (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Dallas Greenlights $200M Oak Lawn Residential Tower (Connect CRE Apartments, Dallas / Texas): Capital event keywords detected: merger_acquisition. Primary topic set to institutional_capital; confidence low.
- Newsom Signs Bill Putting $11B Housing Bond on November Ballot (Connect CRE California, California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Forman Provides Loan to Kickstart Marble Falls Mixed-Use Project (Connect CRE Texas, Austin / Texas): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- REIT's Liquidation Plan Upended After $280M Sale Falls Through (Bisnow, Riverside / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Institutional activity terms detected: reit_activity. Primary topic set to institutional_capital; confidence low.
- Tishman Speyer’s TS Communities Lines Up Funds for Next Phase of Edgemere Commons (Connect CRE Apartments, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Developer Planning 220-Unit Homestead-Area Rental Community (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- JLL Arranges $252M Financing for Huntington Beach Seniors Project (Connect CRE Orange County, California): Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Starwood Quietly Reveals Plans For Conversion In Downtown D.C. (Bisnow, Washington DC): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Why Adam America has moved into student housing (Multifamily Dive, National): Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- Additional low/unknown rows omitted: 19

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.