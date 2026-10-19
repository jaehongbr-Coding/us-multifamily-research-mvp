# Classification Quality Report

Generated: 2026-10-19 00:51:48

## Classification Summary

- Total articles classified: 79
- Topic distribution: development_pipeline: 17; capital_markets: 16; transaction_market: 15; supply_demand: 12; gp_activity: 6; macro_financing: 5; institutional_capital: 3; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 17 article(s), high 1, medium 5, low 11, unknown 0. Top markets: Other / Unknown (5); National (2); Austin / Texas (2); Dallas / Texas (1); Los Angeles / California (1).
- capital_markets: 16 article(s), high 5, medium 9, low 2, unknown 0. Top markets: Other / Unknown (4); Miami / Florida (3); California (3); Dallas / Texas (1); Florida (1).
- transaction_market: 15 article(s), high 3, medium 7, low 5, unknown 0. Top markets: Other / Unknown (3); Atlanta / Georgia (3); Dallas / Texas (2); California (2); New York City / New York (2).
- supply_demand: 12 article(s), high 0, medium 0, low 12, unknown 0. Top markets: Other / Unknown (6); Miami / Florida (2); National (2); New York (1); Atlanta / Georgia (1).
- gp_activity: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (5); National (1).
- macro_financing: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: New York City / New York (2); Other / Unknown (2); Los Angeles / California (1).
- institutional_capital: 3 article(s), high 0, medium 3, low 0, unknown 0. Top markets: Miami / Florida (1); California (1); New York City / New York (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (1); Santa Monica / California (1); Other / Unknown (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); Colorado (1).

## Low Confidence / Unknown Articles

- Groundbreaking of Age-Restricted Affordable Housing for Wildfires Survivors in California (Yield PRO, Los Angeles / California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- PCCP Provides $41M Refi on North Park Multifamily (Connect CRE, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Rendering vs. Reality: 176 apartments at 2225 Sunset Boulevard in Echo Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Developers land financing for mixed-use project at 11111 Jefferson Blvd. in Culver City (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Southwest Valley Community Plans take a step forward (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Jamison flips to affordable housing at 679 S. Harvard Blvd. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- More Pasadena affordable housing in the works at 1976 E. Colorado Blvd. (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing takes shape at 327 S. Harbor Blvd. in San Pedro (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Development Group Starts Work on 371-Unit Boynton Beach Multifamily Venture (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Annex Group Breaks Ground on $71M Affordable Housing Community in Indianapolis (REBusiness Online, National): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Essex Realty Group Closes Sale of Rogers Park Apartment Building (Connect CRE, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- New Building Permits For 230 Anza Street in Lone Mountain, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- National City Investment Group Breaks Ground on 120-Unit Apartment Community in California (REBusiness Online, California): Development-stage terms detected: construction_start, delivery. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- NYC Multifamily Sales Rise YTD Despite Sharp Pullback in Q3 (Connect CRE Apartments, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Morgan Opens 345-Unit Multifamily Community in North Austin’s Tech Corridor (Yield PRO, Austin / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Gilbane, Strada Development Break Ground on Affordable Tower in Castle Hill/Soundview (Connect CRE, New York): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- 229-Unit Lawton Multifamily Community Trades Hands (Connect CRE Apartments, Dallas / Texas): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 26

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.