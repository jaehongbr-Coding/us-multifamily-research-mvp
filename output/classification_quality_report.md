# Classification Quality Report

Generated: 2026-10-18 00:41:28

## Classification Summary

- Total articles classified: 78
- Topic distribution: capital_markets: 17; development_pipeline: 15; transaction_market: 15; supply_demand: 12; gp_activity: 6; macro_financing: 5; other: 3; research_data: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- capital_markets: 17 article(s), high 4, medium 10, low 3, unknown 0. Top markets: Other / Unknown (5); Miami / Florida (3); California (2); Dallas / Texas (1); Florida (1).
- development_pipeline: 15 article(s), high 1, medium 4, low 10, unknown 0. Top markets: Other / Unknown (6); Los Angeles / California (2); National (2); Washington DC (1); California (1).
- transaction_market: 15 article(s), high 3, medium 6, low 6, unknown 0. Top markets: Other / Unknown (4); Dallas / Texas (3); Atlanta / Georgia (3); California (2); Texas (1).
- supply_demand: 12 article(s), high 0, medium 0, low 12, unknown 0. Top markets: Other / Unknown (6); Miami / Florida (2); National (2); New York (1); Atlanta / Georgia (1).
- gp_activity: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (5); National (1).
- macro_financing: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: New York City / New York (2); Other / Unknown (2); Los Angeles / California (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (1); Santa Monica / California (1); Other / Unknown (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (1); Colorado (1); Other / Unknown (1).
- institutional_capital: 2 article(s), high 0, medium 2, low 0, unknown 0. Top markets: Miami / Florida (1); California (1).

## Low Confidence / Unknown Articles

- Groundbreaking of Age-Restricted Affordable Housing for Wildfires Survivors in California (Yield PRO, Los Angeles / California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- PCCP Provides $41M Refi on North Park Multifamily (Connect CRE, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Rendering vs. Reality: 176 apartments at 2225 Sunset Boulevard in Echo Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Developers land financing for mixed-use project at 11111 Jefferson Blvd. in Culver City (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Southwest Valley Community Plans take a step forward (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Jamison flips to affordable housing at 679 S. Harvard Blvd. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- More Pasadena affordable housing in the works at 1976 E. Colorado Blvd. (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing takes shape at 327 S. Harbor Blvd. in San Pedro (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Rendering vs. Reality: Mixed-use building at 1808 Lincoln Blvd. in Venice (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Development Group Starts Work on 371-Unit Boynton Beach Multifamily Venture (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Annex Group Breaks Ground on $71M Affordable Housing Community in Indianapolis (REBusiness Online, National): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Essex Realty Group Closes Sale of Rogers Park Apartment Building (Connect CRE, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- National City Investment Group Breaks Ground on 120-Unit Apartment Community in California (REBusiness Online, California): Development-stage terms detected: construction_start, delivery. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- NYC Multifamily Sales Rise YTD Despite Sharp Pullback in Q3 (Connect CRE Apartments, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Landmark Delivers 34-Story Multifamily Student Housing Tower in Philadelphia (Yield PRO, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Gilbane, Strada Development Break Ground on Affordable Tower in Castle Hill/Soundview (Connect CRE, New York): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- 229-Unit Lawton Multifamily Community Trades Hands (Connect CRE Apartments, Dallas / Texas): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 28

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.