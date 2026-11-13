# Classification Quality Report

Generated: 2026-11-13 03:10:31

## Classification Summary

- Total articles classified: 82
- Topic distribution: development_pipeline: 17; transaction_market: 15; capital_markets: 11; gp_activity: 9; institutional_capital: 9; supply_demand: 9; macro_financing: 5; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 17 article(s), high 2, medium 9, low 6, unknown 0. Top markets: Other / Unknown (5); Florida (2); National (2); California (2); Phoenix / Arizona (1).
- transaction_market: 15 article(s), high 1, medium 9, low 5, unknown 0. Top markets: Atlanta / Georgia (3); California (3); Florida (2); National (2); Dallas / Texas (1).
- capital_markets: 11 article(s), high 4, medium 5, low 2, unknown 0. Top markets: National (2); Other / Unknown (2); Miami / Florida (1); Riverside / California (1); Austin / Texas (1).
- gp_activity: 9 article(s), high 0, medium 0, low 1, unknown 8. Top markets: Other / Unknown (3); New York City / New York (2); New York (1); Los Angeles / California (1); California (1).
- institutional_capital: 9 article(s), high 1, medium 4, low 4, unknown 0. Top markets: Dallas / Texas (3); Other / Unknown (2); Miami / Florida (1); California (1); New York City / New York (1).
- supply_demand: 9 article(s), high 1, medium 0, low 8, unknown 0. Top markets: National (5); Other / Unknown (3); San Francisco / California (1).
- macro_financing: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (2); California (1); Miami / Florida (1); Dallas / Texas (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Other / Unknown (1); Houston / Texas (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (3).

## Low Confidence / Unknown Articles

- Jacob Fulop Files Plans for Two 99-Unit Buildings in East Harlem (Commercial Observer, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Affordable housing takes shape at 3455 Slauson Ave. in Hyde Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Work underway for affordable housing at 6144 N. Hazelhurst Pl. in North Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Construction begins for mixed-use project at 11111 Jefferson Blvd. in Culver City (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affordable housing rising at 2626 Cullen St. in Mid-City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Fresh renderings for West Hollywood's Melrose Triangle development (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 152 apartments planned at 2315 Marine Ave. in Gardena (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Plaza Lakes to Develop 130,000 SF Shopping Center in Kissimmee, Florida (REBusiness Online, Florida): Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Marcus & Millichap Arranges $2.6M Sale of 28-Unit Multifamily Property in South Lake Tahoe California (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- JLL Arranges $104M Loan for Refinancing for Manhattan Multifamily Portfolio (REBusiness Online, Riverside / California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- White Plains Project is First to Break Ground on NY State’s Housing Acceleration Fund (Connect CRE, New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
-  (Yield PRO, Florida): Capital event keywords detected: acquisition. Financing type keywords detected: agency_debt. Supply/demand terms detected: effective_rent_growth, occupancy. Institutional activity terms detected: lender_activity, gp_acquisition. Primary topic set to transaction_market; confidence medium.
- Advanced Real Estate Buys Inland Empire Apartment Complex for $56M (Commercial Observer, Riverside / California): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- 3 multifamily groundbreakings you may have missed (Multifamily Dive, California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Related Building 494 Boca Raton Apartment Units (Connect CRE South Florida, Miami / Florida): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Pacific Urban Investors Pays Over $500k/Unit for Seattle MF Property (Connect CRE Apartments, Seattle): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Senior housing to start work at 861 E. Walnut St. in Pasadena (Urbanize LA, Dallas / Texas): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 26

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.