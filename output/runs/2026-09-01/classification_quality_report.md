# Classification Quality Report

Generated: 2026-09-01 01:41:57

## Classification Summary

- Total articles classified: 80
- Topic distribution: development_pipeline: 15; transaction_market: 14; capital_markets: 12; supply_demand: 9; gp_activity: 8; institutional_capital: 8; macro_financing: 6; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 15 article(s), high 1, medium 5, low 9, unknown 0. Top markets: Other / Unknown (5); California (3); Atlanta / Georgia (3); Los Angeles / California (1); New York City / New York (1).
- transaction_market: 14 article(s), high 4, medium 4, low 6, unknown 0. Top markets: Atlanta / Georgia (3); California (2); National (2); Miami / Florida (2); West Palm Beach / Florida (1).
- capital_markets: 12 article(s), high 4, medium 3, low 5, unknown 0. Top markets: Other / Unknown (4); California (2); Miami / Florida (2); Los Angeles / California (1); Dallas / Texas (1).
- supply_demand: 9 article(s), high 0, medium 1, low 8, unknown 0. Top markets: Other / Unknown (7); National (2).
- gp_activity: 8 article(s), high 0, medium 0, low 1, unknown 7. Top markets: Other / Unknown (3); Atlanta / Georgia (1); Seattle (1); Phoenix / Arizona (1); Houston / Texas (1).
- institutional_capital: 8 article(s), high 2, medium 4, low 2, unknown 0. Top markets: California (3); Sun Belt (1); Other / Unknown (1); New York (1); Miami / Florida (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (3); Seattle (1); San Francisco / California (1); Atlanta / Georgia (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: California (2); Santa Monica / California (1); Los Angeles / California (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (4).

## Low Confidence / Unknown Articles

- Investor Pays $23.5M For Two Apartment Multifamily Portfolio in Northern California (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Cortland Sells West Palm Apartments For $208M: The South Florida Deal Sheet (Bisnow, Atlanta / Georgia): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: disposition. Institutional activity terms detected: gp_disposition. Primary topic set to transaction_market; confidence low.
- Chicago's Slow Apartment Pipeline Fueling Deals And Adaptive Reuse (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- CBRE Brokers Sale of Vintage Redlands Apartments (Connect CRE, Riverside / California): Capital event keywords detected: disposition. Supply/demand terms detected: effective_rent_growth. Primary topic set to transaction_market; confidence medium.
- Torrance Apartments Trade for $350K/Unit (Connect CRE, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Rendering vs. Reality: Mixed-use complex at 3900 S. Figueroa St. in Expo Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Eldercare facility approved for site at 5353 N. Del Moreno Dr. in Woodland Hills (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Affordable housing topped off at 8911 Ramsgate Ave. in Westchester (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing complex underway at 708 S. Gramercy Dr. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing starts to rise at 216 S. Avenue 24 in Lincoln Heights (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 12-story residential building pitched for 1517 15th St. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Knighthead Funding Provides $32M Loan for Refinancing of Metro Chicago Apartment Community (REBusiness Online, Other / Unknown): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Affinius Capital Provides Loan for Refinancing of 594-Unit Apartment Community in Fort Worth (REBusiness Online, Dallas / Texas): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Knighthead Funding Provides $32M Refinancing for Newly Built MF in Glenview (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Greenstone Partners Brokers Two Chicago Multifamily Transactions (Connect CRE, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Miami-Dade Public Agency Advancing $126.4M Affordable Housing Project (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Rendering vs. Reality: Torrance's Gable House Apartments (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Atlanta Developer Plans $343M Mixed-Use Project In Downtown Durham (Bisnow, Atlanta / Georgia): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Community Roots Housing, Kids Co. Launch Buildout of Learning Center at Seattle Housing Development (Connect CRE, Seattle): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Additional low/unknown rows omitted: 32

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.