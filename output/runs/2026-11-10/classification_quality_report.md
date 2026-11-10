# Classification Quality Report

Generated: 2026-11-10 04:30:29

## Classification Summary

- Total articles classified: 81
- Topic distribution: development_pipeline: 22; capital_markets: 10; transaction_market: 10; macro_financing: 9; institutional_capital: 8; gp_activity: 7; other: 6; supply_demand: 6
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 22 article(s), high 2, medium 10, low 10, unknown 0. Top markets: Other / Unknown (9); Dallas / Texas (4); California (3); Los Angeles / California (2); San Francisco / California (1).
- capital_markets: 10 article(s), high 1, medium 7, low 2, unknown 0. Top markets: Other / Unknown (2); New York City / New York (2); Phoenix / Arizona (2); Austin / Texas (1); Miami / Florida (1).
- transaction_market: 10 article(s), high 1, medium 6, low 3, unknown 0. Top markets: Atlanta / Georgia (3); Other / Unknown (2); California (1); Tennessee (1); Santa Monica / California (1).
- macro_financing: 9 article(s), high 0, medium 0, low 0, unknown 9. Top markets: Other / Unknown (3); California (2); Los Angeles / California (1); Miami / Florida (1); National (1).
- institutional_capital: 8 article(s), high 0, medium 3, low 5, unknown 0. Top markets: Atlanta / Georgia (2); Other / Unknown (2); National (2); Miami / Florida (1); California (1).
- gp_activity: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Other / Unknown (3); National (2); California (1); Los Angeles / California (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Los Angeles / California (2); Santa Monica / California (1); New York City / New York (1); Dallas / Texas (1); San Francisco / California (1).
- supply_demand: 6 article(s), high 0, medium 0, low 6, unknown 0. Top markets: Other / Unknown (3); National (3).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (3).

## Low Confidence / Unknown Articles

- Marcus & Millichap Closes Sale and Arranges Financing for West Hollywood Multifamily Portfolio (Yield PRO, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Newmark Arranges Refi for Prospect Lefferts Gardens Multifamily (Connect CRE, New York City / New York): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Fresh renderings for West Hollywood's Melrose Triangle development (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Six homes planned at 1420 S. Point View St. in Mid-City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Construction goes vertical for affordable housing at 21155 Califa St. in Warner Center (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Fresh renderings for Santa Monica apartments at 1338 5th St. (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing planned at 1135 N. Westmoreland Ave. in East Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- New Building Permits For ADU at 4300 17th Street in Corona Heights, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Groundbreaking For Liberation Park Residences, Oakland (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Site prep begins for housing at 2301 N. Sepulveda Blvd. in Manhattan Beach (Urbanize LA, New York City / New York): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Cerritos College plans 102-unit student housing complex (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- MMCC Arranges Credit Union Financing for Three Central Valley Multifamily Properties (Connect CRE, California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- 3 multifamily groundbreakings you may have missed (Multifamily Dive, California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- JV Pays Nearly $15M on Property for Nashville Apartment, Retail Venture (Connect CRE Apartments, Atlanta / Georgia): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Related Building 494 Boca Raton Apartment Units (Connect CRE Apartments, Miami / Florida): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Marcus & Millichap Brokers Multifamily Sale in Santa Monica’s Ocean Park Neighborhood (Yield PRO, Santa Monica / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Wu Proposes Loosening Affordable Housing Mandates To Spur Development (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Northmarq Arranges Sale of 3 Property Luxury Multifamily Portfolio in Northern Utah (Yield PRO, Salt Lake City / Utah): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 31

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.