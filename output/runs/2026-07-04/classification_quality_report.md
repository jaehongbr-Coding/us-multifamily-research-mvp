# Classification Quality Report

Generated: 2026-07-04 00:05:26

## Classification Summary

- Total articles classified: 81
- Topic distribution: development_pipeline: 19; supply_demand: 13; capital_markets: 12; gp_activity: 11; transaction_market: 9; macro_financing: 6; institutional_capital: 4; research_data: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 19 article(s), high 2, medium 6, low 11, unknown 0. Top markets: Other / Unknown (4); Los Angeles / California (3); Miami / Florida (2); Dallas / Texas (2); California (1).
- supply_demand: 13 article(s), high 1, medium 2, low 10, unknown 0. Top markets: Other / Unknown (9); National (4).
- capital_markets: 12 article(s), high 8, medium 3, low 1, unknown 0. Top markets: Miami / Florida (3); California (2); National (1); New York (1); Denver / Colorado (1).
- gp_activity: 11 article(s), high 0, medium 0, low 0, unknown 11. Top markets: National (3); Atlanta / Georgia (2); Other / Unknown (2); Los Angeles / California (1); New York City / New York (1).
- transaction_market: 9 article(s), high 4, medium 3, low 2, unknown 0. Top markets: Phoenix / Arizona (2); Miami / Florida (2); Seattle (1); Other / Unknown (1); Austin / Texas (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (4); Santa Monica / California (1); Los Angeles / California (1).
- institutional_capital: 4 article(s), high 1, medium 2, low 1, unknown 0. Top markets: Los Angeles / California (2); California (1); Riverside / California (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (3); California (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); Other / Unknown (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- CBRE Arranges $24M Sale of 87-Unit Apartment Property in Seattle (Connect CRE, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- City Council upholds approval of mixed-use project at 1410 Main St. in Venice (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- New details for plans to convert L.A. World Trade center into affordable housing (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 62 apartments underway at 11103 Hartsook Ave. in North Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing commences work at 825 Hyperion Ave. in Silver Lake (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing takes shape at 1734 S. Barrington Ave. in Sawtelle (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Construction commences for mixed-use project at 2025 and 2051 Wilshire in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Developer revises proposal for apartments at 4728 San Fernando Rd. in Glendale (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Adaptive reuse to create affordable housing at 521 and 530 E. 4th St. in Long Beach (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Affordable housing completed at 3300 Washington Blvd. in Arlington Heights (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- New Building Permits Filed For 4148 24th Street, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Palindrome Property Group Secures Financing for Phoenix Multifamily Affordable Project The Residences at Dorsey Station (Yield PRO, Phoenix / Arizona): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Apartment Builders, Developers are Optimistic Long-Term Despite Rising Costs (Connect CRE Apartments, National): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Fairfield Completes 14-Story Houston Multifamily Tower (Connect CRE Texas, Houston / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Revised Plan for Pacific Park Would Bring 5,600 Apartments to Downtown Brooklyn (Connect CRE Apartments, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Developer Planning 220-Unit Homestead-Area Rental Community (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 29

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.