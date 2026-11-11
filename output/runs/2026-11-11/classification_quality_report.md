# Classification Quality Report

Generated: 2026-11-11 02:33:55

## Classification Summary

- Total articles classified: 85
- Topic distribution: development_pipeline: 21; transaction_market: 14; capital_markets: 12; institutional_capital: 10; macro_financing: 9; gp_activity: 6; supply_demand: 6; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 21 article(s), high 1, medium 9, low 11, unknown 0. Top markets: Other / Unknown (8); California (4); Dallas / Texas (3); Miami / Florida (2); San Francisco / California (1).
- transaction_market: 14 article(s), high 1, medium 8, low 5, unknown 0. Top markets: California (4); Atlanta / Georgia (4); Other / Unknown (4); Dallas / Texas (1); New York City / New York (1).
- capital_markets: 12 article(s), high 3, medium 5, low 4, unknown 0. Top markets: National (3); Other / Unknown (1); Denver / Colorado (1); Riverside / California (1); Arizona (1).
- institutional_capital: 10 article(s), high 1, medium 4, low 5, unknown 0. Top markets: Other / Unknown (2); Seattle (1); Sun Belt (1); Miami / Florida (1); Phoenix / Arizona (1).
- macro_financing: 9 article(s), high 0, medium 0, low 0, unknown 9. Top markets: Other / Unknown (3); California (2); National (1); Miami / Florida (1); Dallas / Texas (1).
- gp_activity: 6 article(s), high 0, medium 0, low 1, unknown 5. Top markets: Other / Unknown (3); California (1); San Francisco / California (1); National (1).
- supply_demand: 6 article(s), high 0, medium 0, low 6, unknown 0. Top markets: Other / Unknown (3); National (3).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); New York City / New York (1); Denver / Colorado (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (3).

## Low Confidence / Unknown Articles

- Berkadia Completes Sale and Secures Financing for Multifamily Property in Everett Washington (Yield PRO, Seattle): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- JLL Arranges $104M Financing for Uptown Multifamily Portfolio (Connect CRE, Riverside / California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Construction begins for mixed-use project at 11111 Jefferson Blvd. in Culver City (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affordable housing rising at 2626 Cullen St. in Mid-City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Fresh renderings for West Hollywood's Melrose Triangle development (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Six homes planned at 1420 S. Point View St. in Mid-City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Construction goes vertical for affordable housing at 21155 Califa St. in Warner Center (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- New Building Permits For ADU at 4300 17th Street in Corona Heights, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Dinerstein Cos., PCCP Receive $92.1M Refinancing for Multifamily Community in Mesa, Arizona (REBusiness Online, Arizona): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- $212M Sale, Financing Arranged by JLL for Seniors Housing in Lincolnwood (Connect CRE Apartments, National): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- MMCC Arranges Credit Union Financing for Three Central Valley Multifamily Properties (Connect CRE California, California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Groundbreaking For Liberation Park Residences, Oakland (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Cushman & Wakefield Brokers $44M Sale of 240-Unit Apartment Community in Sheboygan Wisconsin to Axiom Properties (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Mayor Wu Proposes Inclusionary Zoning Changes to Ease Developers’ Financial Burden (Connect CRE, Other / Unknown): Development-stage terms detected: zoning. Primary topic set to development_pipeline; confidence low.
- Site prep begins for housing at 2301 N. Sepulveda Blvd. in Manhattan Beach (Urbanize LA, New York City / New York): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Cerritos College plans 102-unit student housing complex (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- BMC Investments To Move Away From Office, Hotel Developments, Focus On Apartments (Bisnow, Denver / Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 3 multifamily groundbreakings you may have missed (Multifamily Dive, California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Multifamily’s Refinancing Crunch Is Raising the Stakes for AI (Commercial Observer, National): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Additional low/unknown rows omitted: 33

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.