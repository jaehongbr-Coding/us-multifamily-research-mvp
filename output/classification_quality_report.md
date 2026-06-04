# Classification Quality Report

Generated: 2026-06-04 08:14:13

## Classification Summary

- Total articles classified: 80
- Topic distribution: supply_demand: 15; development_pipeline: 14; capital_markets: 13; transaction_market: 12; institutional_capital: 9; gp_activity: 8; other: 6; research_data: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- supply_demand: 15 article(s), high 1, medium 1, low 13, unknown 0. Top markets: Other / Unknown (7); National (4); Phoenix / Arizona (2); Sun Belt (1); Miami / Florida (1).
- development_pipeline: 14 article(s), high 2, medium 5, low 7, unknown 0. Top markets: Other / Unknown (4); California (3); Atlanta / Georgia (2); Los Angeles / California (1); Washington DC (1).
- capital_markets: 13 article(s), high 5, medium 7, low 1, unknown 0. Top markets: California (3); New York City / New York (2); Sarasota / Florida (1); Los Angeles / California (1); Austin / Texas (1).
- transaction_market: 12 article(s), high 2, medium 10, low 0, unknown 0. Top markets: California (3); Atlanta / Georgia (2); Other / Unknown (2); National (1); Miami / Florida (1).
- institutional_capital: 9 article(s), high 1, medium 2, low 6, unknown 0. Top markets: Other / Unknown (3); San Francisco / California (2); New York (1); Los Angeles / California (1); Sun Belt (1).
- gp_activity: 8 article(s), high 0, medium 0, low 0, unknown 8. Top markets: National (2); Southeast (1); Other / Unknown (1); Dallas / Texas (1); Texas (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Los Angeles / California (2); New York (1); Texas (1); California (1); Other / Unknown (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: California (1); Santa Monica / California (1); Los Angeles / California (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Institutional activity terms detected: lender_activity. Primary topic set to supply_demand; confidence medium.
- BHI Provides Condo Inventory Loan for Ground-Up Luxury Project (Connect CRE, New York): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Proposed apartments face appeal at 3411 Foothill Blvd. in Glendale (Urbanize LA, New York): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Construction begins for affordable housing at 4151 E. Fountain Ave. in Long Beach (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Construction kicks off for affordable housing at 706 W. 85th Street in South L.A. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Metro-adjacent affordable housing rises at 1640 20th Street in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- New plan unveiled for West Hollywood's Melrose Triangle development (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Venice Dell affordable housing project notches legal win (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- St. John Properties, Somerset Break Ground on $148M Multifamily Community in Baltimore County (REBusiness Online, Southeast): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Affirmed Housing, VTA Break Ground on San Jose TOD (Connect CRE California, California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Mayor Bass: Adaptive Reuse Key to Revitalizing Downtown LA (Connect CRE California, Los Angeles / California): Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Construction Tops Out at La Mesa Townhome/Apartment Complex (Connect CRE Apartments, California): Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Insignia Pursuing Embassy Row Redevelopment (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Multifamily CMBS Loan Distress Keeps Rising (Bisnow, Houston / Texas): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Financing type keywords detected: cmbs. Institutional activity terms detected: lender_activity. Primary topic set to capital_markets; confidence low.
- Work Begins on 94-Unit Scottsdale Luxury BTR Community (Connect CRE Phoenix, Phoenix / Arizona): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Renters remain cautious but demand holds steady (Multifamily Dive, Sun Belt): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low. Operator/property management activity detected.
- Charlotte BTR Investors Pause Deals As They Await Fate Of Federal Housing Bill (Bisnow, Sun Belt): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 24

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.