# Classification Quality Report

Generated: 2026-05-27 23:02:07

## Classification Summary

- Total articles classified: 85
- Topic distribution: development_pipeline: 19; capital_markets: 18; transaction_market: 17; supply_demand: 14; institutional_capital: 10; gp_activity: 7
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 19 article(s), high 3, medium 10, low 6, unknown 0. Top markets: Other / Unknown (5); Los Angeles (4); Sun Belt (4); California (3); Southeast (1).
- capital_markets: 18 article(s), high 12, medium 6, low 0, unknown 0. Top markets: California (6); Sun Belt (4); New York (2); Other / Unknown (2); Texas (1).
- transaction_market: 17 article(s), high 2, medium 15, low 0, unknown 0. Top markets: Sun Belt (7); California (4); New York (3); Other / Unknown (2); Texas (1).
- supply_demand: 14 article(s), high 1, medium 2, low 11, unknown 0. Top markets: Other / Unknown (7); National (4); Sun Belt (2); Los Angeles (1).
- institutional_capital: 10 article(s), high 3, medium 2, low 5, unknown 0. Top markets: Other / Unknown (5); New York (2); California (1); National (1); Los Angeles (1).
- gp_activity: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Sun Belt (2); Other / Unknown (2); National (2); Southeast (1).

## Low Confidence / Unknown Articles

- Affordable housing slated for 1418 S. Mansfield Ave. in Mid-City (Urbanize LA, Los Angeles): Development-stage terms detected: planning_commission. Primary topic set to development_pipeline; confidence low.
- 17 apartments planned at 2217 S. Fox Hills Dr. in Century City (Urbanize LA, Los Angeles): Development-stage terms detected: planning_commission, entitlement, zoning. Primary topic set to development_pipeline; confidence low.
- New housing slated for 1045 Locust Street in Pasadena (Urbanize LA, Southeast): Development-stage terms detected: density_bonus. Primary topic set to gp_activity; confidence low.
- Insignia Pursuing Embassy Row Redevelopment (Connect CRE Atlanta, Sun Belt): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Multifamily starts rose again in April (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Work Begins on 94-Unit Scottsdale Luxury BTR Community (Connect CRE Phoenix, Sun Belt): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- S2 Capital Launches Sun Belt Development Platform (Bisnow, Sun Belt): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Belgravia Converting Former Wake Forest Classrooms to Mixed-Use Project (Connect CRE Apartments, Sun Belt): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Shorter Apartment Construction Time in 2024 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery, permit. Primary topic set to development_pipeline; confidence low.
- Barnat Launches Phase II of Mixed-Income Multifamily Near Beverly MBTA Station (Connect CRE Apartments, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Cambridge Properties Bringing New Life to Aging Charlotte Center (Connect CRE Charlotte, Sun Belt): Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- First Quarter 2026 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Fourth Quarter 2025 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Overall Housing Starts Inch Lower in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Third Quarter 2025 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Blackstone Real Estate Debt Strategies Launches Homebuilder Lending Platform (Blackstone Real Estate, New York): Institutional activity terms detected: lender_activity, private_equity_activity. Primary topic set to institutional_capital; confidence low.
- Renderings revealed: Arts District towers at 2143 E. Violet Street (Urbanize LA, Los Angeles): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Additional low/unknown rows omitted: 9

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.