# Classification Quality Report

Generated: 2026-11-06 03:13:42

## Classification Summary

- Total articles classified: 71
- Topic distribution: development_pipeline: 14; supply_demand: 10; gp_activity: 9; transaction_market: 9; capital_markets: 8; institutional_capital: 8; macro_financing: 6; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 14 article(s), high 1, medium 7, low 6, unknown 0. Top markets: Other / Unknown (8); Los Angeles / California (2); Miami / Florida (1); Phoenix / Arizona (1); California (1).
- supply_demand: 10 article(s), high 1, medium 1, low 8, unknown 0. Top markets: National (6); Other / Unknown (4).
- gp_activity: 9 article(s), high 0, medium 0, low 0, unknown 9. Top markets: Other / Unknown (3); Connecticut (2); Washington DC (1); Phoenix / Arizona (1); California (1).
- transaction_market: 9 article(s), high 2, medium 4, low 3, unknown 0. Top markets: Atlanta / Georgia (4); California (2); Other / Unknown (1); Sun Belt (1); Salt Lake City / Utah (1).
- capital_markets: 8 article(s), high 4, medium 2, low 2, unknown 0. Top markets: Nashville / Tennessee (2); San Francisco / California (1); New York (1); Colorado (1); National (1).
- institutional_capital: 8 article(s), high 0, medium 3, low 5, unknown 0. Top markets: Other / Unknown (2); National (1); New York City / New York (1); Miami / Florida (1); New York (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (4); California (1); Los Angeles / California (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (2); Los Angeles / California (2).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: California (2); Los Angeles / California (1).

## Low Confidence / Unknown Articles

- Ari Azarbarzin joins JLL Capital Markets in Washington, D.C. (Yield PRO, Washington DC): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Vivmark Touts Integration and Growth in First Quarterly Earnings Call (Commercial Observer, National): Capital event keywords detected: merger_acquisition. Primary topic set to institutional_capital; confidence low.
- Excavation underway for affordable housing at 1248 N. Cherokee Ave. in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing on the rise at 3990 S. Wade. St. in Mar Vista (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 377 apartments rise next to Brea Mall (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- US Apartment Rents Inch Higher in Q3 as Supply Wave Subsides (Connect CRE Apartments, National): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- One Beverly Hills Reaches Milestones Ahead of Schedule (Connect CRE California, Los Angeles / California): Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Affordable housing taking shape at 5749 S. Brynhurst Avenue in Hyde Park (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Zoning Worksheet Filed for Multifamily Building at 425 W Macarthur Boulevard in Oakland (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: zoning. Primary topic set to development_pipeline; confidence low.
- Leon Multifamily Building 343-Unit N. Phoenix Venture (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Marcus & Millichap Closes $29.85M Sale and Arranges Financing for Two Multifamily Assets in West Hollywood (Yield PRO, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- 123 homes planned at 902 W. Washington Blvd. in University Park (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- CSU Dominguez Hills completes new dorms + rec center (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Trammell Crow Building 248 McKinney Apartment Units, 3 Hotels (Connect CRE Apartments, Dallas / Texas): Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Investor Takes Over Distressed Atlanta Apartment Asset (Connect CRE Atlanta, Atlanta / Georgia): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Shorter Apartment Construction Time in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery, permit. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 26

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.