# Classification Quality Report

Generated: 2026-06-04 00:01:36

## Classification Summary

- Total articles classified: 81
- Topic distribution: development_pipeline: 23; supply_demand: 14; transaction_market: 14; capital_markets: 12; gp_activity: 9; institutional_capital: 8; other: 1
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 23 article(s), high 2, medium 10, low 11, unknown 0. Top markets: California (5); Los Angeles / California (5); Other / Unknown (5); Atlanta / Georgia (2); New York (1).
- supply_demand: 14 article(s), high 1, medium 1, low 12, unknown 0. Top markets: Other / Unknown (7); National (3); Phoenix / Arizona (2); Sun Belt (1); Miami / Florida (1).
- transaction_market: 14 article(s), high 2, medium 11, low 1, unknown 0. Top markets: Other / Unknown (3); California (3); Atlanta / Georgia (2); Miami / Florida (2); National (1).
- capital_markets: 12 article(s), high 5, medium 7, low 0, unknown 0. Top markets: California (3); New York City / New York (2); Sarasota / Florida (1); Los Angeles / California (1); Austin / Texas (1).
- gp_activity: 9 article(s), high 0, medium 0, low 0, unknown 9. Top markets: Texas (2); National (2); Southeast (1); Other / Unknown (1); Dallas / Texas (1).
- institutional_capital: 8 article(s), high 1, medium 2, low 5, unknown 0. Top markets: Other / Unknown (3); San Francisco / California (2); New York (1); Sun Belt (1); Riverside / California (1).
- other: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: National (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Institutional activity terms detected: lender_activity. Primary topic set to supply_demand; confidence medium.
- BHI Provides Condo Inventory Loan for Ground-Up Luxury Project (Connect CRE, New York): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Proposed apartments face appeal at 3411 Foothill Blvd. in Glendale (Urbanize LA, New York): Development-stage terms detected: planning_commission, density_bonus, zoning. Primary topic set to development_pipeline; confidence low.
- Venice Dell affordable housing project notches legal win (Urbanize LA, Los Angeles / California): Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- St. John Properties, Somerset Break Ground on $148M Multifamily Community in Baltimore County (REBusiness Online, Southeast): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Affirmed Housing, VTA Break Ground on San Jose TOD (Connect CRE California, California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Mayor Bass: Adaptive Reuse Key to Revitalizing Downtown LA (Connect CRE California, Los Angeles / California): Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Construction Tops Out at La Mesa Townhome/Apartment Complex (Connect CRE Apartments, California): Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Flow Enters West Coast With $175M San Jose Multifamily Buy (Bisnow, Miami / Florida): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: acquisition. Institutional activity terms detected: lender_activity. Primary topic set to transaction_market; confidence low.
- Insignia Pursuing Embassy Row Redevelopment (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Work Begins on 94-Unit Scottsdale Luxury BTR Community (Connect CRE Phoenix, Phoenix / Arizona): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Renters remain cautious but demand holds steady (Multifamily Dive, Sun Belt): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low. Operator/property management activity detected.
- Charlotte BTR Investors Pause Deals As They Await Fate Of Federal Housing Bill (Bisnow, Sun Belt): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Seco Planning 12-Story, $100M FW Apartment Highrise (Connect CRE Apartments, Dallas / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Phase Three of The Tobin Estate Apartments Now Leasing in San Antonio (Yield PRO, Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Austin Church Eyeing 880-Unit Rental Project (Connect CRE Texas, Austin / Texas): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Good + Roberts Tops Out on $29M San Diego Multifamily Mixed-Use Housing Development (Yield PRO, California): Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 19

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.