# Classification Quality Report

Generated: 2026-10-14 01:37:57

## Classification Summary

- Total articles classified: 72
- Topic distribution: development_pipeline: 18; transaction_market: 14; supply_demand: 11; capital_markets: 10; gp_activity: 6; institutional_capital: 4; macro_financing: 4; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 18 article(s), high 2, medium 6, low 10, unknown 0. Top markets: Other / Unknown (9); National (3); Phoenix / Arizona (1); Sun Belt (1); Austin / Texas (1).
- transaction_market: 14 article(s), high 2, medium 7, low 5, unknown 0. Top markets: Atlanta / Georgia (4); Other / Unknown (3); Austin / Texas (2); Seattle (2); Tampa / Florida (1).
- supply_demand: 11 article(s), high 0, medium 0, low 11, unknown 0. Top markets: Other / Unknown (6); Miami / Florida (2); National (2); Dallas / Texas (1).
- capital_markets: 10 article(s), high 3, medium 5, low 2, unknown 0. Top markets: New York City / New York (2); New York (1); Miami / Florida (1); California (1); Florida (1).
- gp_activity: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (3); Dallas / Texas (1); National (1); San Francisco / California (1).
- institutional_capital: 4 article(s), high 0, medium 3, low 1, unknown 0. Top markets: Miami / Florida (1); Riverside / California (1); Other / Unknown (1); Dallas / Texas (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (2); Colorado (1); Tennessee (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Other / Unknown (1); San Francisco / California (1).
- research_data: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: Los Angeles / California (1).

## Low Confidence / Unknown Articles

- In Sun Belt Multifamily, an Uneven Path Back Toward Boom Times (Commercial Observer, Dallas / Texas): Supply/demand terms detected: effective_rent_growth, supply_pressure, oversupply. Primary topic set to supply_demand; confidence low.
- Warner Center development site showing activity at 6160 Variel Ave. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- New look for Westwood housing complex at 11027 W. Strathmore Dr. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing secures financing at 1756 Colorado Blvd. in Pasadena (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Completion nears for mixed-use project at 10608 Pico Blvd. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- New look for large apartment complex at 444 N. Fair Oaks Ave. in Pasadena (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Wood framing rising for mixed-use project at 5843 W. Pico Blvd. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Development Group Starts Work on 371-Unit Boynton Beach Multifamily Venture (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Leon Capital Provides Equity for 516-Bed Student Housing Project in Binghamton, New York (REBusiness Online, Dallas / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Subtext Opens MXU Residential Property in St. Louis (Connect CRE, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Duplex Proposed For 4368 23rd Street in Noe Valley, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993 (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- IPA Closes Transit-Oriented Multifamily Asset Sale in Seattle (Yield PRO, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- The Bloc is on the block, A peek inside the Colburn Center, and more (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Aimco Advancing Luxury Edgewater Apartments (Connect CRE Apartments, Miami / Florida): Supply/demand terms detected: effective_rent_growth, occupancy. Primary topic set to supply_demand; confidence low.
- Additional low/unknown rows omitted: 24

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.