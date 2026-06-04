# Classification Quality Report

Generated: 2026-06-04 23:02:01

## Classification Summary

- Total articles classified: 79
- Topic distribution: capital_markets: 17; supply_demand: 14; development_pipeline: 13; transaction_market: 9; gp_activity: 8; institutional_capital: 8; other: 6; research_data: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- capital_markets: 17 article(s), high 10, medium 5, low 2, unknown 0. Top markets: Miami / Florida (3); California (3); Other / Unknown (3); Atlanta / Georgia (2); Los Angeles / California (1).
- supply_demand: 14 article(s), high 2, medium 1, low 11, unknown 0. Top markets: Other / Unknown (8); National (3); Phoenix / Arizona (1); Sun Belt (1); Miami / Florida (1).
- development_pipeline: 13 article(s), high 1, medium 4, low 8, unknown 0. Top markets: Other / Unknown (7); California (4); Atlanta / Georgia (1); Miami / Florida (1).
- transaction_market: 9 article(s), high 2, medium 7, low 0, unknown 0. Top markets: Los Angeles / California (2); Miami / Florida (1); Tennessee (1); Houston / Texas (1); Texas (1).
- gp_activity: 8 article(s), high 0, medium 0, low 0, unknown 8. Top markets: Other / Unknown (2); National (2); New York City / New York (1); Dallas / Texas (1); Miami / Florida (1).
- institutional_capital: 8 article(s), high 0, medium 2, low 6, unknown 0. Top markets: Other / Unknown (3); Los Angeles / California (2); Washington DC (1); San Francisco / California (1); California (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Los Angeles / California (2); Other / Unknown (2); New York (1); Texas (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); California (1); Santa Monica / California (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Institutional activity terms detected: lender_activity. Primary topic set to supply_demand; confidence medium.
- 19-story high-rise starts work at 6055 Center Drive in Westchester (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Mixed-use project slated for 9700 W. Pico Blvd. in Pico-Robertson (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing proposed for 23022 W. Ventura Blvd. in Woodland Hills (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Proposed apartments face appeal at 3411 Foothill Blvd. in Glendale (Urbanize LA, New York): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Construction begins for affordable housing at 4151 E. Fountain Ave. in Long Beach (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Construction kicks off for affordable housing at 706 W. 85th Street in South L.A. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Metro-adjacent affordable housing rises at 1640 20th Street in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- New plan unveiled for West Hollywood's Melrose Triangle development (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Construction Tops Out at La Mesa Townhome/Apartment Complex (Connect CRE California, California): Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Affirmed Housing, VTA Break Ground on San Jose TOD (Connect CRE California, California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Zilber Residential Group, Homes by Towne Complete 209-Unit Multifamily Community in Roseville, California (REBusiness Online, California): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Insignia Pursuing Embassy Row Redevelopment (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Multifamily CMBS Loan Distress Keeps Rising (Bisnow, Houston / Texas): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Financing type keywords detected: cmbs. Institutional activity terms detected: lender_activity. Primary topic set to capital_markets; confidence low.
- Renters remain cautious but demand holds steady (Multifamily Dive, Sun Belt): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low. Operator/property management activity detected.
- Condyne Plans Adaptive Reuse of Former Konica Minolta Building (Connect CRE, Other / Unknown): Development-stage terms detected: entitlement, redevelopment, adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Transit-oriented development is booming. Here’s how housing pros can make the most of it. (Multifamily Dive, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 25

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.