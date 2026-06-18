# Classification Quality Report

Generated: 2026-06-18 00:17:25

## Classification Summary

- Total articles classified: 79
- Topic distribution: development_pipeline: 19; gp_activity: 13; transaction_market: 13; supply_demand: 12; capital_markets: 7; other: 6; macro_financing: 5; institutional_capital: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 19 article(s), high 3, medium 9, low 7, unknown 0. Top markets: Phoenix / Arizona (3); Los Angeles / California (3); Other / Unknown (3); California (2); Denver / Colorado (1).
- gp_activity: 13 article(s), high 0, medium 0, low 1, unknown 12. Top markets: National (3); New York City / New York (2); Other / Unknown (2); Beverly Hills / California (1); Houston / Texas (1).
- transaction_market: 13 article(s), high 2, medium 8, low 3, unknown 0. Top markets: Other / Unknown (3); California (3); Sun Belt (1); Phoenix / Arizona (1); Beverly Hills / California (1).
- supply_demand: 12 article(s), high 1, medium 0, low 11, unknown 0. Top markets: Other / Unknown (7); National (4); Washington DC (1).
- capital_markets: 7 article(s), high 4, medium 2, low 1, unknown 0. Top markets: Miami / Florida (3); Other / Unknown (2); Seattle (1); California (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: California (2); Atlanta / Georgia (1); National (1); San Francisco / California (1); Los Angeles / California (1).
- macro_financing: 5 article(s), high 0, medium 0, low 1, unknown 4. Top markets: Other / Unknown (4); National (1).
- institutional_capital: 2 article(s), high 0, medium 2, low 0, unknown 0. Top markets: Miami / Florida (1); Austin / Texas (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (2).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Seven-story, 82-unit apartment building pitched for 402 Atlantic Ave. in Long Beach (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Developer secures $85m loan for mixed-use project at 55 N. La Cienega Blvd. in Beverly Hills (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- City Planning Commission approves 76 apartments at 2413 N. Silver Lake Boulevard (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: planning_commission. Primary topic set to development_pipeline; confidence low.
- Affordable housing slated for 5139 N. Colfax Ave. in Valley Village (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Meeting Tonight For 1275 South California Street, Walnut Creek (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Dwight Capital Provides $36M HUD-Insured Loan for Multifamily Community in Missouri (REBusiness Online, Other / Unknown): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Meeting Tomorrow For 3521 Homestead Road, Santa Clara (SF YIMBY, Atlanta / Georgia): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- El Paso’s Palomar West Apartment Community Trades in Off-Market Sale (Yield PRO, Texas): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Starts Tumble 40% As Housing Construction Hits 6-Year Low (Bisnow, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Long-Delayed Candlestick Point Development Advances with Board of Supervisors Approval (Connect CRE California, San Francisco / California): Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Colleen Wenke of Taconic Partners: 5 Questions (Commercial Observer, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- 342 Apartment Units Planned Near Big Rivers Waterpark (Connect CRE Texas, Houston / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Affordable housing takes shape at 711 S. New Hampshire Ave. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Palladium Delivers $65M Fort Worth Affordable Housing Venture (Connect CRE Texas, Dallas / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- JLL Arranges $252M Financing for Huntington Beach Seniors Project (Connect CRE Orange County, California): Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- Multifamily Financing In 2026: How Are Projects Moving Ahead? (Bisnow, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 28

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.