# Classification Quality Report

Generated: 2026-06-10 11:57:07

## Classification Summary

- Total articles classified: 77
- Topic distribution: supply_demand: 14; development_pipeline: 12; gp_activity: 12; capital_markets: 11; other: 9; institutional_capital: 6; transaction_market: 6; macro_financing: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- supply_demand: 14 article(s), high 1, medium 0, low 13, unknown 0. Top markets: Other / Unknown (8); National (4); Miami / Florida (2).
- development_pipeline: 12 article(s), high 1, medium 8, low 3, unknown 0. Top markets: Other / Unknown (4); California (2); Los Angeles / California (1); Phoenix / Arizona (1); Atlanta / Georgia (1).
- gp_activity: 12 article(s), high 0, medium 0, low 2, unknown 10. Top markets: Other / Unknown (3); National (2); Sun Belt (1); New York City / New York (1); California (1).
- capital_markets: 11 article(s), high 7, medium 3, low 1, unknown 0. Top markets: California (4); Seattle (1); Other / Unknown (1); New York (1); Miami / Florida (1).
- other: 9 article(s), high 0, medium 0, low 0, unknown 9. Top markets: Other / Unknown (3); San Francisco / California (2); Los Angeles (1); Los Angeles / California (1); New York City / New York (1).
- institutional_capital: 6 article(s), high 1, medium 3, low 2, unknown 0. Top markets: New York City / New York (2); Miami / Florida (1); National (1); Florida (1); Houston / Texas (1).
- transaction_market: 6 article(s), high 2, medium 1, low 3, unknown 0. Top markets: Dallas / Texas (1); Sun Belt (1); Other / Unknown (1); Southeast (1); San Francisco / California (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (3); California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: California (3).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Northwood Ravin Launches Pre-Leasing for The Lodges of Huntersville a Built-to-Rent community in Huntersville North Carolina (Yield PRO, Sun Belt): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown. Operator/property management activity detected.
- Apex Investments Files Plans for 224 Apartments in Brooklyn (Commercial Observer, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Rendering vs. Reality: Modular housing complex at 1457 N. Main St. in Chinatown (Urbanize LA, Los Angeles): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Infill housing slated for two sites in Pasadena (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- More housing added to proposed affordable development at 7220 Owensmouth Ave. in Canoga Park (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Election results roll in, SB 79 map rolls out, and more (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- L.A. City Council upholds approval of mixed-use project at 787 S. Alameda St. in DTLA (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Bluhm Family Foundation Breaks Ground on 214-Unit Seniors Housing Community in Huntington Beach, California (REBusiness Online, California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- IPA Capital Markets Arranges $123M Refi for Burlingame Multifamily (Connect CRE Apartments, California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- 290 apartments planned at 18430 Sherman Way in Reseda (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Greystar Eyeing 896 Doral Apartment Units (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- 40-unit development moves forward at 2301 N. Sepulveda Blvd. in Manhattan Beach (Urbanize LA, New York City / New York): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- New Construction Application For 3275-3333 San Bruno Avenue, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Lument Closes $28M Loan for Ohio Residential Multifamily Property (Yield PRO, National): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Marcus & Millichap Brokers Sale of 160-Unit Multifamily Property in Wisconsin (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Insignia Pursuing Embassy Row Redevelopment (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Apartment Market Divergence Grows As Construction Slows And Affordability Pressures Mount (Bisnow, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Additional low/unknown rows omitted: 30

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.