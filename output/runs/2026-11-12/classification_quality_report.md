# Classification Quality Report

Generated: 2026-11-12 03:38:26

## Classification Summary

- Total articles classified: 85
- Topic distribution: development_pipeline: 18; transaction_market: 17; capital_markets: 11; institutional_capital: 9; macro_financing: 9; gp_activity: 8; supply_demand: 7; research_data: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 18 article(s), high 2, medium 10, low 6, unknown 0. Top markets: Other / Unknown (5); California (3); Miami / Florida (2); National (2); Atlanta / Georgia (1).
- transaction_market: 17 article(s), high 2, medium 10, low 5, unknown 0. Top markets: Atlanta / Georgia (4); California (3); Other / Unknown (3); Seattle (2); Dallas / Texas (2).
- capital_markets: 11 article(s), high 4, medium 5, low 2, unknown 0. Top markets: Other / Unknown (3); Phoenix / Arizona (2); California (1); Miami / Florida (1); Riverside / California (1).
- institutional_capital: 9 article(s), high 0, medium 4, low 5, unknown 0. Top markets: Other / Unknown (2); New York (1); Miami / Florida (1); California (1); Washington DC (1).
- macro_financing: 9 article(s), high 0, medium 0, low 1, unknown 8. Top markets: Other / Unknown (3); California (2); Miami / Florida (2); Dallas / Texas (1); San Francisco / California (1).
- gp_activity: 8 article(s), high 0, medium 0, low 1, unknown 7. Top markets: Other / Unknown (3); California (2); New York City / New York (1); Los Angeles / California (1); National (1).
- supply_demand: 7 article(s), high 0, medium 0, low 7, unknown 0. Top markets: Other / Unknown (3); National (3); New York City / New York (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (4).
- other: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); New York City / New York (1).

## Low Confidence / Unknown Articles

- Jacob Fulop Files Plans for Two 99-Unit Buildings in East Harlem (Commercial Observer, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Bozzuto, Kimco Close on JV for Wilton Mixed-Use Project (Connect CRE, New York): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Affordable housing takes shape at 3455 Slauson Ave. in Hyde Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Work underway for affordable housing at 6144 N. Hazelhurst Pl. in North Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Construction begins for mixed-use project at 11111 Jefferson Blvd. in Culver City (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affordable housing rising at 2626 Cullen St. in Mid-City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Fresh renderings for West Hollywood's Melrose Triangle development (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- ACC Closes on $191M Financing for 1,065-Bed Student Housing Development at UC Irvine (REBusiness Online, California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Northmarq Arranges $105M Refinancing for Madrone Apartments in Silicon Valley (REBusiness Online, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Prado Group Acquires Another Batch Of Former Veritas Apartments (Bisnow, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: acquisition. Institutional activity terms detected: gp_acquisition. Primary topic set to transaction_market; confidence low.
- MMCC Arranges Credit Union Financing for Three Central Valley Multifamily Properties (Connect CRE California, California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Site prep begins for housing at 2301 N. Sepulveda Blvd. in Manhattan Beach (Urbanize LA, New York City / New York): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Cerritos College plans 102-unit student housing complex (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- 3 multifamily groundbreakings you may have missed (Multifamily Dive, California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Related Building 494 Boca Raton Apartment Units (Connect CRE South Florida, Miami / Florida): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Senior housing to start work at 861 E. Walnut St. in Pasadena (Urbanize LA, Dallas / Texas): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Portsmouth Multifamily Deal Marks Buyer’s Entry into the Market (Connect CRE, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 28

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.