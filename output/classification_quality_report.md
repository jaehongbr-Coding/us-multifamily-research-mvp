# Classification Quality Report

Generated: 2026-06-01 06:48:06

## Classification Summary

- Total articles classified: 65
- Topic distribution: development_pipeline: 17; supply_demand: 13; capital_markets: 12; institutional_capital: 9; gp_activity: 7; transaction_market: 6; research_data: 1
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 17 article(s), high 2, medium 7, low 8, unknown 0. Top markets: Los Angeles / California (4); Other / Unknown (4); Atlanta / Georgia (2); Santa Monica / California (1); Phoenix / Arizona (1).
- supply_demand: 13 article(s), high 1, medium 2, low 10, unknown 0. Top markets: Other / Unknown (7); National (3); Phoenix / Arizona (2); Los Angeles / California (1).
- capital_markets: 12 article(s), high 7, medium 5, low 0, unknown 0. Top markets: California (3); Miami / Florida (2); New York City / New York (1); Los Angeles / California (1); Other / Unknown (1).
- institutional_capital: 9 article(s), high 1, medium 4, low 4, unknown 0. Top markets: Other / Unknown (3); Santa Monica / California (1); Northern Virginia / Virginia (1); Los Angeles / California (1); Riverside / California (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: National (2); Los Angeles / California (1); Other / Unknown (1); Miami / Florida (1); Las Vegas / Nevada (1).
- transaction_market: 6 article(s), high 1, medium 5, low 0, unknown 0. Top markets: Atlanta / Georgia (2); Los Angeles / California (1); Wethersfield / Connecticut (1); Miami / Florida (1); California (1).
- research_data: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: National (1).

## Low Confidence / Unknown Articles

- RAND reviews ULA impacts, Mayor's race focuses on housing, and more (Urbanize LA, Santa Monica / California): Capital event keywords detected: joint_venture. Development-stage terms detected: entitlement, zoning, permit. Supply/demand terms detected: effective_rent_growth. Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence medium.
- Infill housing slated for 349 N. Oakhurst Ave. in Beverly Hills (Urbanize LA, Los Angeles / California): Development-stage terms detected: planning_commission, density_bonus, zoning. Primary topic set to development_pipeline; confidence low.
- Updated plan for apartments at 1238 Lincoln Blvd. in Santa Monica (Urbanize LA, Santa Monica / California): Development-stage terms detected: density_bonus, zoning, permit. Primary topic set to development_pipeline; confidence low.
- Affordable housing slated for 1418 S. Mansfield Ave. in Mid-City (Urbanize LA, Los Angeles / California): Development-stage terms detected: planning_commission. Primary topic set to development_pipeline; confidence low.
- Uncommon Developers Takes Community-Building Approach (Connect CRE California, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- First Projects Advance Under San Francisco's New Zoning Plan, But Costs Hold Pipeline To A Trickle (Bisnow, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: zoning. Institutional activity terms detected: lender_activity. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Insignia Pursuing Embassy Row Redevelopment (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Work Begins on 94-Unit Scottsdale Luxury BTR Community (Connect CRE Phoenix, Phoenix / Arizona): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Lee & Associates’ Report: Industrial and Multifamily Slow, Office Recovers, Retail Demand Holds (REBusiness Online, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Modular housing manufacturing proposed for city-owned site at 10901 S. Clovis St. in South LA (Urbanize LA, Los Angeles / California): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- W. Palm Beach Developer Eyeing 25-Story Apartment Tower (Connect CRE South Florida, Miami / Florida): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Cambridge Properties Bringing New Life to Aging Charlotte Center (Connect CRE Charlotte, Atlanta / Georgia): Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- First Quarter 2026 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Fourth Quarter 2025 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Overall Housing Starts Inch Lower in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Third Quarter 2025 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Blackstone Real Estate Debt Strategies Launches Homebuilder Lending Platform (Blackstone Real Estate, New York): Institutional activity terms detected: lender_activity, private_equity_activity. Primary topic set to institutional_capital; confidence low.
- Additional low/unknown rows omitted: 10

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.