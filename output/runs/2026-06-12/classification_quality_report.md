# Classification Quality Report

Generated: 2026-06-12 00:20:41

## Classification Summary

- Total articles classified: 75
- Topic distribution: development_pipeline: 14; supply_demand: 12; capital_markets: 10; transaction_market: 10; gp_activity: 9; other: 6; institutional_capital: 5; macro_financing: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 14 article(s), high 1, medium 10, low 3, unknown 0. Top markets: Other / Unknown (4); New York City / New York (3); Seattle (1); Riverside / California (1); California (1).
- supply_demand: 12 article(s), high 1, medium 0, low 11, unknown 0. Top markets: Other / Unknown (7); National (3); Miami / Florida (2).
- capital_markets: 10 article(s), high 6, medium 3, low 1, unknown 0. Top markets: California (2); Miami / Florida (1); New York (1); Phoenix / Arizona (1); New York City / New York (1).
- transaction_market: 10 article(s), high 3, medium 2, low 5, unknown 0. Top markets: Phoenix / Arizona (2); Los Angeles / California (2); Dallas / Texas (1); New York (1); Atlanta / Georgia (1).
- gp_activity: 9 article(s), high 0, medium 0, low 1, unknown 8. Top markets: Other / Unknown (2); National (2); California (1); Phoenix / Arizona (1); Miami / Florida (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Los Angeles / California (2); Los Angeles (1); Other / Unknown (1); National (1); San Francisco / California (1).
- institutional_capital: 5 article(s), high 1, medium 4, low 0, unknown 0. Top markets: Miami / Florida (1); New York (1); California (1); Austin / Texas (1); Other / Unknown (1).
- macro_financing: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (3); Los Angeles / California (1); Atlanta / Georgia (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); California (2).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- 230 apartments unwrapped at 640 S. St. Andrews Pl. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 77-unit affordable housing complex proposed at 8811 Reading Ave. in Westchester (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing coming to 1150 Sunset Blvd. in Echo Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Rendering vs. Reality: Modular housing complex at 1457 N. Main St. in Chinatown (Urbanize LA, Los Angeles): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Infill housing slated for two sites in Pasadena (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- More housing added to proposed affordable development at 7220 Owensmouth Ave. in Canoga Park (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Riverside Investment & Development Breaks Ground on West Loop Multifamily Development (Connect CRE Apartments, Riverside / California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Greystar Eyeing 896 Doral Apartment Units (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- High-rise senior housing complex pitched for 6400 Canoga Ave. in Warner Center (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Apartments Along Burton Way Trade for $603K Per Unit (Connect CRE, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Hotel Indigo on the rise at 515 N. Central Ave. in Glendale (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Insignia Pursuing Embassy Row Redevelopment (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Apartment Market Divergence Grows As Construction Slows And Affordability Pressures Mount (Bisnow, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- JLL Arranges $252M Financing for Huntington Beach Seniors Project (Connect CRE Orange County, California): Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- While U.S. Apartment Rents Stall, San Francisco Market Accelerates (Bisnow, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- New York Would Tie Library Redevelopment to Affordable Housing Under New Plan (Commercial Observer, New York City / New York): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
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