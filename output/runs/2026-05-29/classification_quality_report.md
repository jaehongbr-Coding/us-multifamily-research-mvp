# Classification Quality Report

Generated: 2026-05-29 23:01:38

## Classification Summary

- Total articles classified: 74
- Topic distribution: development_pipeline: 17; supply_demand: 16; capital_markets: 14; institutional_capital: 11; transaction_market: 9; gp_activity: 7
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 17 article(s), high 2, medium 8, low 7, unknown 0. Top markets: Los Angeles (4); Sun Belt (4); Other / Unknown (4); California (1); Arizona (1).
- supply_demand: 16 article(s), high 1, medium 2, low 13, unknown 0. Top markets: Other / Unknown (8); National (3); Sun Belt (3); Los Angeles (2).
- capital_markets: 14 article(s), high 9, medium 5, low 0, unknown 0. Top markets: Sun Belt (3); California (3); National (2); New York (2); Florida (2).
- institutional_capital: 11 article(s), high 3, medium 4, low 4, unknown 0. Top markets: Other / Unknown (4); California (3); New York (2); National (1); Los Angeles (1).
- transaction_market: 9 article(s), high 2, medium 7, low 0, unknown 0. Top markets: Sun Belt (5); Other / Unknown (2); Los Angeles (1); California (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: National (2); Sun Belt (2); Los Angeles (1); Other / Unknown (1); Florida (1).

## Low Confidence / Unknown Articles

- Infill housing slated for 349 N. Oakhurst Ave. in Beverly Hills (Urbanize LA, Los Angeles): Development-stage terms detected: planning_commission, density_bonus, zoning. Primary topic set to development_pipeline; confidence low.
- Updated plan for apartments at 1238 Lincoln Blvd. in Santa Monica (Urbanize LA, California): Development-stage terms detected: density_bonus, zoning, permit. Primary topic set to development_pipeline; confidence low.
- Affordable housing slated for 1418 S. Mansfield Ave. in Mid-City (Urbanize LA, Los Angeles): Development-stage terms detected: planning_commission. Primary topic set to development_pipeline; confidence low.
- New Rendering For 650 Divisadero Street, San Francisco (SF YIMBY, California): Capital event keywords detected: joint_venture. Development-stage terms detected: entitlement. Institutional activity terms detected: gp_acquisition, gp_disposition. Primary topic set to institutional_capital; confidence medium.
- Uncommon Developers Takes Community-Building Approach (Connect CRE California, Los Angeles): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Insignia Pursuing Embassy Row Redevelopment (Connect CRE Atlanta, Sun Belt): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Work Begins on 94-Unit Scottsdale Luxury BTR Community (Connect CRE Phoenix, Sun Belt): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Garden Communities Launches Leasing at Luxury Multifamily Community Gardens at Roseland in Roseland New Jersey (Yield PRO, Other / Unknown): Supply/demand terms detected: effective_rent_growth, occupancy. Primary topic set to supply_demand; confidence low.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Cambridge Properties Bringing New Life to Aging Charlotte Center (Connect CRE Charlotte, Sun Belt): Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Modular housing manufacturing proposed for city-owned site at 10901 S. Clovis St. in South LA (Urbanize LA, Los Angeles): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- North Texas Cities Slow New Multifamily Housing Law Through 'Unnecessary Mandates' (Bisnow, Sun Belt): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Miami Multifamily Market Nose-Dives As Hopes For Supply Relief Fade (Bisnow, Sun Belt): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- First Quarter 2026 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Fourth Quarter 2025 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Overall Housing Starts Inch Lower in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Third Quarter 2025 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- W. Palm Beach Developer Eyeing 25-Story Apartment Tower (Connect CRE South Florida, Florida): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 11

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.