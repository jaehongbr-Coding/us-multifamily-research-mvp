# Classification Quality Report

Generated: 2026-11-09 02:24:42

## Classification Summary

- Total articles classified: 71
- Topic distribution: development_pipeline: 15; transaction_market: 12; capital_markets: 10; gp_activity: 8; supply_demand: 8; institutional_capital: 5; other: 5; macro_financing: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 15 article(s), high 2, medium 6, low 7, unknown 0. Top markets: Other / Unknown (7); Los Angeles / California (2); Phoenix / Arizona (2); Dallas / Texas (2); Miami / Florida (1).
- transaction_market: 12 article(s), high 1, medium 6, low 5, unknown 0. Top markets: Atlanta / Georgia (3); New York City / New York (3); Seattle (2); Other / Unknown (1); California (1).
- capital_markets: 10 article(s), high 3, medium 4, low 3, unknown 0. Top markets: Other / Unknown (3); Phoenix / Arizona (2); Nashville / Tennessee (1); Washington DC (1); Los Angeles / California (1).
- gp_activity: 8 article(s), high 0, medium 0, low 0, unknown 8. Top markets: Other / Unknown (4); Atlanta / Georgia (1); Phoenix / Arizona (1); California (1); National (1).
- supply_demand: 8 article(s), high 1, medium 0, low 7, unknown 0. Top markets: National (4); Other / Unknown (3); Dallas / Texas (1).
- institutional_capital: 5 article(s), high 0, medium 2, low 3, unknown 0. Top markets: California (1); Miami / Florida (1); Seattle (1); Other / Unknown (1); Atlanta / Georgia (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (2); Santa Monica / California (1); Other / Unknown (1); San Francisco / California (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (4).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (3); California (1).

## Low Confidence / Unknown Articles

- Six homes planned at 1420 S. Point View St. in Mid-City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Construction goes vertical for affordable housing at 21155 Califa St. in Warner Center (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Fresh renderings for Santa Monica apartments at 1338 5th St. (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing planned at 1135 N. Westmoreland Ave. in East Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Excavation underway for affordable housing at 1248 N. Cherokee Ave. in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing on the rise at 3990 S. Wade. St. in Mar Vista (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affinius Capital Provides $226M Loan for Refinancing of Downtown Brooklyn Apartment Tower (REBusiness Online, New York City / New York): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- Wood Partners, GrayCo Capital to Break Ground on 301-Unit Multifamily Community Near Durham (REBusiness Online, California): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Greystar, Vantage Acquire Chamblee Property for 340-Unit Multifamily Community (Connect CRE Apartments, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Groundbreaking For Liberation Park Residences, Oakland (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Atlas Capital Group Buys 360 West 43rd Street Apartments for $143M (Commercial Observer, New York City / New York): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- TruAmerica Breaks Ground On Santa Clarita Multifamily: The Los Angeles Deal Sheet (Bisnow, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Northmarq Arranges Sale of 3 Mid-Rise Multifamily Properties in Ogden and Salt Lake City Utah (Yield PRO, Salt Lake City / Utah): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- 123 homes planned at 902 W. Washington Blvd. in University Park (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Kidder Mathews Arranges $17.5M Sale of 101 Broadway a 44-Unit Mixed-Use Asset in Seattle’s Capitol Hill (Yield PRO, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Trammell Crow Building 248 McKinney Apartment Units, 3 Hotels (Connect CRE Texas, Dallas / Texas): Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 26

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.