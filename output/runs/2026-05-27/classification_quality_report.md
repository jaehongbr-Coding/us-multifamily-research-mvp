# Classification Quality Report

Generated: 2026-05-27 01:36:18

## Classification Summary

- Total articles classified: 85
- Topic distribution: transaction_market: 23; development_pipeline: 22; supply_demand: 15; capital_markets: 9; institutional_capital: 9; gp_activity: 7
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 23 article(s), high 4, medium 19, low 0, unknown 0. Top markets: Sun Belt (7); Other / Unknown (4); California (3); National (2); Florida (2).
- development_pipeline: 22 article(s), high 3, medium 8, low 11, unknown 0. Top markets: Other / Unknown (7); Sun Belt (6); Los Angeles (5); California (3); Southeast (1).
- supply_demand: 15 article(s), high 1, medium 3, low 11, unknown 0. Top markets: Other / Unknown (8); National (5); Sun Belt (1); Los Angeles (1).
- capital_markets: 9 article(s), high 6, medium 3, low 0, unknown 0. Top markets: California (4); Sun Belt (3); Florida (1); New York (1).
- institutional_capital: 9 article(s), high 3, medium 2, low 4, unknown 0. Top markets: Other / Unknown (3); National (2); New York (2); Sun Belt (1); Los Angeles (1).
- gp_activity: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: National (3); Other / Unknown (2); Southeast (1); California (1).

## Low Confidence / Unknown Articles

- 17 apartments planned at 2217 S. Fox Hills Dr. in Century City (Urbanize LA, Los Angeles): Development-stage terms detected: planning_commission, entitlement, zoning. Primary topic set to development_pipeline; confidence low.
- Adaptive reuse planned for Westwood office tower at 10900 Wilshire Blvd. (Urbanize LA, Los Angeles): Development-stage terms detected: entitlement, zoning, adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Affordable housing unwrapped at 611 S. Hobart Blvd. in Koreatown (Urbanize LA, California): Development-stage terms detected: density_bonus, zoning, permit. Primary topic set to development_pipeline; confidence low.
- Avison Young Markets Echo Park Multifamily Portfolio (Connect CRE California, Los Angeles): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- New housing slated for 1045 Locust Street in Pasadena (Urbanize LA, Southeast): Development-stage terms detected: density_bonus. Primary topic set to gp_activity; confidence low.
- Developer revives plan for Best Western hotel at 2645 S. Western Ave. in Jefferson Park (Urbanize LA, Los Angeles): Development-stage terms detected: planning_commission, permit. Primary topic set to development_pipeline; confidence low.
- Insignia Pursuing Embassy Row Redevelopment (Connect CRE Atlanta, Sun Belt): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Multifamily starts rose again in April (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Kolbe Completes New Multifamily Development in Wisconsin (Connect CRE, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Work Begins on 94-Unit Scottsdale Luxury BTR Community (Connect CRE Phoenix, Sun Belt): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- NexMetro Debuts 229-Unit San Tan Valley BTR Community (Connect CRE Phoenix, Sun Belt): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Shorter Apartment Construction Time in 2024 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery, permit. Primary topic set to development_pipeline; confidence low.
- $28M Housing, Mixed-Use Development in Baltimore Breaks Ground (Connect CRE Apartments, Other / Unknown): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Cambridge Properties Bringing New Life to Aging Charlotte Center (Connect CRE Charlotte, Sun Belt): Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- First Quarter 2026 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Fourth Quarter 2025 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Overall Housing Starts Inch Lower in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Third Quarter 2025 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Additional low/unknown rows omitted: 13

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.