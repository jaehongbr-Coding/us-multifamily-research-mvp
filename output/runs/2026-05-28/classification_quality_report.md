# Classification Quality Report

Generated: 2026-05-28 23:01:55

## Classification Summary

- Total articles classified: 79
- Topic distribution: capital_markets: 17; supply_demand: 16; development_pipeline: 15; institutional_capital: 11; transaction_market: 11; gp_activity: 9
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- capital_markets: 17 article(s), high 9, medium 8, low 0, unknown 0. Top markets: California (6); Other / Unknown (3); Sun Belt (3); New York (2); Los Angeles (1).
- supply_demand: 16 article(s), high 1, medium 2, low 13, unknown 0. Top markets: Other / Unknown (7); National (4); Sun Belt (3); Los Angeles (2).
- development_pipeline: 15 article(s), high 1, medium 5, low 9, unknown 0. Top markets: Other / Unknown (6); Sun Belt (5); Los Angeles (2); California (1); Southeast (1).
- institutional_capital: 11 article(s), high 2, medium 4, low 5, unknown 0. Top markets: Other / Unknown (4); New York (3); Los Angeles (1); Texas (1); California (1).
- transaction_market: 11 article(s), high 3, medium 8, low 0, unknown 0. Top markets: Sun Belt (6); California (2); New York (1); Los Angeles (1); Seattle (1).
- gp_activity: 9 article(s), high 0, medium 0, low 1, unknown 8. Top markets: Sun Belt (3); National (2); Southeast (1); Los Angeles (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- Updated plan for apartments at 1238 Lincoln Blvd. in Santa Monica (Urbanize LA, California): Development-stage terms detected: density_bonus, zoning, permit. Primary topic set to development_pipeline; confidence low.
- Affordable housing slated for 1418 S. Mansfield Ave. in Mid-City (Urbanize LA, Los Angeles): Development-stage terms detected: planning_commission. Primary topic set to development_pipeline; confidence low.
- 17 apartments planned at 2217 S. Fox Hills Dr. in Century City (Urbanize LA, Los Angeles): Development-stage terms detected: planning_commission, entitlement, zoning. Primary topic set to development_pipeline; confidence low.
- Portman to Bring 30,000 SF Food Hall to Savona Mill Redevelopment in Charlotte (REBusiness Online, Sun Belt): Development-stage terms detected: redevelopment, adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- New Rendering For 650 Divisadero Street, San Francisco (SF YIMBY, California): Capital event keywords detected: joint_venture. Development-stage terms detected: entitlement. Institutional activity terms detected: gp_acquisition, gp_disposition. Primary topic set to institutional_capital; confidence medium.
- New housing slated for 1045 Locust Street in Pasadena (Urbanize LA, Southeast): Development-stage terms detected: density_bonus. Primary topic set to gp_activity; confidence low.
- Insignia Pursuing Embassy Row Redevelopment (Connect CRE Atlanta, Sun Belt): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Multifamily starts rose again in April (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Work Begins on 94-Unit Scottsdale Luxury BTR Community (Connect CRE Phoenix, Sun Belt): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Uncommon Developers Takes Community-Building Approach (Connect CRE Apartments, Los Angeles): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- S2 Capital Launches Sun Belt Development Platform (Bisnow, Sun Belt): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Shorter Apartment Construction Time in 2024 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery, permit. Primary topic set to development_pipeline; confidence low.
- Cambridge Properties Bringing New Life to Aging Charlotte Center (Connect CRE Charlotte, Sun Belt): Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Modular housing manufacturing proposed for city-owned site at 10901 S. Clovis St. in South LA (Urbanize LA, Los Angeles): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Homeless Coalition Converting Denver YMCA Space to Apartments (Connect CRE Apartments, Sun Belt): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Miami Multifamily Market Nose-Dives As Hopes For Supply Relief Fade (Bisnow, Sun Belt): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- First Quarter 2026 Multifamily Construction Data (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: effective_rent_growth, supply_pressure. Primary topic set to supply_demand; confidence low.
- Additional low/unknown rows omitted: 16

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.