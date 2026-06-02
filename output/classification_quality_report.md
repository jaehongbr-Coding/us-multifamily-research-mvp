# Classification Quality Report

Generated: 2026-06-02 04:54:46

## Classification Summary

- Total articles classified: 79
- Topic distribution: development_pipeline: 23; supply_demand: 15; capital_markets: 14; transaction_market: 11; institutional_capital: 9; gp_activity: 7
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 23 article(s), high 2, medium 10, low 11, unknown 0. Top markets: Los Angeles / California (8); Other / Unknown (4); Atlanta / Georgia (3); San Francisco / California (2); Santa Monica / California (1).
- supply_demand: 15 article(s), high 1, medium 4, low 10, unknown 0. Top markets: Other / Unknown (8); National (5); Phoenix / Arizona (2).
- capital_markets: 14 article(s), high 7, medium 7, low 0, unknown 0. Top markets: California (4); Miami / Florida (3); Washington DC (1); New York City / New York (1); Sarasota / Florida (1).
- transaction_market: 11 article(s), high 1, medium 10, low 0, unknown 0. Top markets: Atlanta / Georgia (3); Other / Unknown (3); California (2); Los Angeles / California (1); Houston / Texas (1).
- institutional_capital: 9 article(s), high 0, medium 5, low 4, unknown 0. Top markets: Riverside / California (2); New York (2); Other / Unknown (2); Santa Monica / California (1); Houston / Texas (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: National (3); Other / Unknown (1); Miami / Florida (1); Las Vegas / Nevada (1); Atlanta / Georgia (1).

## Low Confidence / Unknown Articles

- Mayor Bass: Adaptive Reuse Key to Revitalizing Downtown LA (Connect CRE, Los Angeles / California): Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Venice Dell affordable housing project notches legal win (Urbanize LA, Los Angeles / California): Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- RAND reviews ULA impacts, Mayor's race focuses on housing, and more (Urbanize LA, Santa Monica / California): Capital event keywords detected: joint_venture. Development-stage terms detected: entitlement, zoning, permit. Supply/demand terms detected: effective_rent_growth. Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence medium.
- Infill housing slated for 349 N. Oakhurst Ave. in Beverly Hills (Urbanize LA, Los Angeles / California): Development-stage terms detected: planning_commission, density_bonus, zoning. Primary topic set to development_pipeline; confidence low.
- Updated plan for apartments at 1238 Lincoln Blvd. in Santa Monica (Urbanize LA, Santa Monica / California): Development-stage terms detected: density_bonus, zoning, permit. Primary topic set to development_pipeline; confidence low.
- Jefferson Apartment Group Delivers Luxury Multifamily Community J Optimist Park in Charlotte North Carolina (Yield PRO, Sun Belt): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- First Projects Advance Under San Francisco's New Zoning Plan, But Costs Hold Pipeline To A Trickle (Bisnow, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: zoning. Institutional activity terms detected: lender_activity. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Insignia Pursuing Embassy Row Redevelopment (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Work Begins on 94-Unit Scottsdale Luxury BTR Community (Connect CRE Phoenix, Phoenix / Arizona): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily construction spending lower in April (Yield PRO, National): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Austin Church Eyeing 880-Unit Rental Project (Connect CRE Apartments, Austin / Texas): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- W. Palm Beach Developer Eyeing 25-Story Apartment Tower (Connect CRE South Florida, Miami / Florida): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Cambridge Properties Bringing New Life to Aging Charlotte Center (Connect CRE Charlotte, Atlanta / Georgia): Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- L.A. Mayor Karen Bass On Fast-Tracking Housing and Reviving Downtown (Commercial Observer, Los Angeles / California): Development-stage terms detected: permit, adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- First Quarter 2026 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Fourth Quarter 2025 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Overall Housing Starts Inch Lower in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Additional low/unknown rows omitted: 12

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.