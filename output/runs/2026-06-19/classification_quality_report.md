# Classification Quality Report

Generated: 2026-06-19 00:28:03

## Classification Summary

- Total articles classified: 78
- Topic distribution: development_pipeline: 18; supply_demand: 14; gp_activity: 12; transaction_market: 12; capital_markets: 11; other: 4; macro_financing: 3; institutional_capital: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 18 article(s), high 3, medium 5, low 10, unknown 0. Top markets: Other / Unknown (5); Los Angeles / California (3); California (2); Phoenix / Arizona (2); Dallas / Texas (2).
- supply_demand: 14 article(s), high 1, medium 0, low 13, unknown 0. Top markets: Other / Unknown (8); National (4); Texas (1); Washington DC (1).
- gp_activity: 12 article(s), high 0, medium 0, low 3, unknown 9. Top markets: Los Angeles / California (2); Other / Unknown (2); National (2); Seattle (1); Beverly Hills / California (1).
- transaction_market: 12 article(s), high 3, medium 5, low 4, unknown 0. Top markets: Phoenix / Arizona (2); Denver / Colorado (2); Other / Unknown (2); New York City / New York (1); Beverly Hills / California (1).
- capital_markets: 11 article(s), high 3, medium 7, low 1, unknown 0. Top markets: Miami / Florida (3); Florida (2); California (2); New York City / New York (1); Georgia (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: California (2); Los Angeles / California (1); National (1).
- macro_financing: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Other / Unknown (3).
- institutional_capital: 2 article(s), high 0, medium 1, low 1, unknown 0. Top markets: Washington DC (1); Florida (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); San Francisco / California (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- New Affordable Housing Project Moves Forward in Puyallup (Connect CRE, Seattle): Financing type keywords detected: tax_credit_financing. Primary topic set to gp_activity; confidence low.
- Developer retools plan for mixed-use project at 3800 W. 6th St. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Construction begins for 47 apartments at 7337 Fountain Ave. in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Seven-story, 82-unit apartment building pitched for 402 Atlantic Ave. in Long Beach (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Developer secures $85m loan for mixed-use project at 55 N. La Cienega Blvd. in Beverly Hills (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- City Planning Commission approves 76 apartments at 2413 N. Silver Lake Boulevard (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: planning_commission. Primary topic set to development_pipeline; confidence low.
- Affordable housing slated for 5139 N. Colfax Ave. in Valley Village (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Meeting Tonight For 1275 South California Street, Walnut Creek (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Nuveen Provides $38.6M in C-PACE Financing for Seniors Housing Development in Central Texas (REBusiness Online, Texas): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Inside The Turmoil Clouding Miami's Largest Affordable Housing Project (Bisnow, Miami / Florida): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Highlights from Connect Midwest Multifamily Trends 2026: Development, Construction, Operations, PropTech & Design Trends for the Modern Renter (VIDEO) (Connect CRE, Other / Unknown): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Multifamily Starts Tumble 40% As Housing Construction Hits 6-Year Low (Bisnow, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Long-Delayed Candlestick Point Development Advances with Board of Supervisors Approval (Connect CRE California, San Francisco / California): Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- American Landmark appoints new investment chief (Multifamily Dive, Phoenix / Arizona): Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- Palladium Delivers $65M Fort Worth Affordable Housing Venture (Connect CRE Texas, Dallas / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- JLL Arranges $252M Financing for Huntington Beach Seniors Project (Connect CRE Orange County, California): Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- Post Brothers President Matthew Pestronk On D.C.’s $750M Office Conversion (Commercial Observer, New York City / New York): Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 30

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.