# Classification Quality Report

Generated: 2026-09-10 00:53:36

## Classification Summary

- Total articles classified: 84
- Topic distribution: transaction_market: 19; development_pipeline: 17; capital_markets: 13; gp_activity: 9; supply_demand: 9; macro_financing: 7; institutional_capital: 4; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 19 article(s), high 3, medium 11, low 5, unknown 0. Top markets: California (3); Los Angeles / California (2); Other / Unknown (2); Dallas / Texas (2); New York City / New York (2).
- development_pipeline: 17 article(s), high 2, medium 5, low 10, unknown 0. Top markets: Other / Unknown (10); Atlanta / Georgia (3); Houston / Texas (1); Florida (1); New York (1).
- capital_markets: 13 article(s), high 5, medium 6, low 2, unknown 0. Top markets: Miami / Florida (7); Los Angeles / California (2); Other / Unknown (1); New York City / New York (1); Las Vegas / Nevada (1).
- gp_activity: 9 article(s), high 0, medium 0, low 0, unknown 9. Top markets: Other / Unknown (3); Atlanta / Georgia (1); Houston / Texas (1); Phoenix / Arizona (1); Dallas / Texas (1).
- supply_demand: 9 article(s), high 0, medium 0, low 9, unknown 0. Top markets: Other / Unknown (5); National (4).
- macro_financing: 7 article(s), high 0, medium 0, low 2, unknown 5. Top markets: Los Angeles / California (2); Other / Unknown (2); Dallas / Texas (1); California (1); Atlanta / Georgia (1).
- institutional_capital: 4 article(s), high 1, medium 1, low 2, unknown 0. Top markets: Dallas / Texas (1); California (1); National (1); Denver / Colorado (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Santa Monica / California (1); Los Angeles / California (1); National (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Other / Unknown (2); Los Angeles / California (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Interra Realty Brokers $19.2M Sale of Loft Apartment Building in Chicago’s River North Neighborhood (Yield PRO, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Housing unwrapped at 11261 Santa Monica Boulevard (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Mixed-use building starts to rise at 8025 Santa Monica Blvd. in West Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Construction begins for affordable housing at former MacLaren Hall site in El Monte (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Sunset Boulevard bus lanes, Kroenke buys Angels, and more (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Building Permits Issued For West Oakland BART Affordable Housing (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Eastwind Breaks Ground on 264-Unit Multifamily Development on Florida’s Space Coast (REBusiness Online, Florida): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Dominium to Build 350 Affordable BTR Units in Terrell (Connect CRE Apartments, Dallas / Texas): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Infill housing coming to 1030 N. Sierra Bonita Ave. in West Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Pre-Application Filed For 1100 Los Gamos Drive, San Rafael (SF YIMBY, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Mixed-use project to rise at 225 N. 2nd Ave. in Arcadia (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- What multifamily firms bought and sold this summer (Multifamily Dive, Riverside / California): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- Zoning Adjustment Board Meeting Tomorrow For 2955 Shattuck Avenue, Berkeley (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: zoning. Primary topic set to development_pipeline; confidence low.
- Bullish on Multifamily, Selective on Deals: Investors Navigate a More Disciplined Market (Connect CRE Apartments, National): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Kennedy Wilson, Shimizu Corp. partner on $139M multifamily build in Georgia (Multifamily Dive, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Cadence McShane Wins Texas REDnews Multifamily Project of the Year Award for Westgrove (Yield PRO, Houston / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Colliers Team Closes Sale of 107-Unit Central Valley Apartments (Connect CRE, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Additional low/unknown rows omitted: 30

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.