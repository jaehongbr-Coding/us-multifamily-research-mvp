# Classification Quality Report

Generated: 2026-07-03 00:06:40

## Classification Summary

- Total articles classified: 81
- Topic distribution: capital_markets: 13; development_pipeline: 13; supply_demand: 12; gp_activity: 11; transaction_market: 11; institutional_capital: 7; macro_financing: 6; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- capital_markets: 13 article(s), high 8, medium 4, low 1, unknown 0. Top markets: California (4); Miami / Florida (2); National (1); New York (1); Denver / Colorado (1).
- development_pipeline: 13 article(s), high 1, medium 5, low 7, unknown 0. Top markets: Other / Unknown (4); Los Angeles / California (3); Miami / Florida (2); California (1); Houston / Texas (1).
- supply_demand: 12 article(s), high 1, medium 1, low 10, unknown 0. Top markets: Other / Unknown (9); National (3).
- gp_activity: 11 article(s), high 0, medium 0, low 0, unknown 11. Top markets: National (3); Atlanta / Georgia (2); Other / Unknown (2); Los Angeles / California (1); New York City / New York (1).
- transaction_market: 11 article(s), high 5, medium 3, low 3, unknown 0. Top markets: Phoenix / Arizona (2); Miami / Florida (2); Seattle (1); Nashville / Tennessee (1); Florida (1).
- institutional_capital: 7 article(s), high 1, medium 4, low 2, unknown 0. Top markets: Los Angeles / California (3); California (1); Riverside / California (1); Phoenix / Arizona (1); New York City / New York (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (4); Santa Monica / California (1); Los Angeles / California (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (3); Other / Unknown (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (3); California (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- CBRE Arranges $24M Sale of 87-Unit Apartment Property in Seattle (Connect CRE, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- New details for plans to convert L.A. World Trade center into affordable housing (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 62 apartments underway at 11103 Hartsook Ave. in North Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing commences work at 825 Hyperion Ave. in Silver Lake (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing takes shape at 1734 S. Barrington Ave. in Sawtelle (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Construction commences for mixed-use project at 2025 and 2051 Wilshire in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Developer revises proposal for apartments at 4728 San Fernando Rd. in Glendale (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Adaptive reuse to create affordable housing at 521 and 530 E. 4th St. in Long Beach (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Affordable housing completed at 3300 Washington Blvd. in Arlington Heights (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- City Planning Commission votes in favor of new zoning rules near three G Line stops (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: planning_commission, zoning. Primary topic set to development_pipeline; confidence low.
- Lender-Owned Tucson Multifamily Apartment Complex Traded for $32M (Yield PRO, Phoenix / Arizona): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Apartment Builders, Developers are Optimistic Long-Term Despite Rising Costs (Connect CRE Apartments, National): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Fairfield Completes 14-Story Houston Multifamily Tower (Connect CRE Texas, Houston / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Revised Plan for Pacific Park Would Bring 5,600 Apartments to Downtown Brooklyn (Connect CRE Apartments, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Developer Planning 220-Unit Homestead-Area Rental Community (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Dwight Capital Closes Two Corpus Christi Loans Totaling $96M (Connect CRE Texas, Texas): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Additional low/unknown rows omitted: 28

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.