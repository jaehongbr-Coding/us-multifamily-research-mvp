# Classification Quality Report

Generated: 2026-10-22 01:16:46

## Classification Summary

- Total articles classified: 75
- Topic distribution: supply_demand: 13; transaction_market: 13; institutional_capital: 11; capital_markets: 10; development_pipeline: 10; gp_activity: 8; macro_financing: 5; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- supply_demand: 13 article(s), high 0, medium 0, low 13, unknown 0. Top markets: Other / Unknown (8); Miami / Florida (2); National (2); Los Angeles / California (1).
- transaction_market: 13 article(s), high 2, medium 6, low 5, unknown 0. Top markets: Atlanta / Georgia (3); Los Angeles / California (2); Dallas / Texas (2); Other / Unknown (2); New York (1).
- institutional_capital: 11 article(s), high 3, medium 3, low 5, unknown 0. Top markets: National (3); Other / Unknown (3); California (2); Seattle (1); New York (1).
- capital_markets: 10 article(s), high 2, medium 6, low 2, unknown 0. Top markets: California (2); Miami / Florida (2); Other / Unknown (1); Florida (1); Southeast (1).
- development_pipeline: 10 article(s), high 0, medium 3, low 7, unknown 0. Top markets: Other / Unknown (5); California (2); Los Angeles / California (1); Atlanta / Georgia (1); Florida (1).
- gp_activity: 8 article(s), high 0, medium 0, low 0, unknown 8. Top markets: Other / Unknown (4); San Francisco / California (2); National (2).
- macro_financing: 5 article(s), high 0, medium 0, low 1, unknown 4. Top markets: Other / Unknown (3); California (1); New York City / New York (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Other / Unknown (2); Santa Monica / California (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: San Francisco / California (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- 6 Blackstone multifamily properties move to servicing (Multifamily Dive, Seattle): Institutional activity terms detected: private_equity_activity. Primary topic set to institutional_capital; confidence low.
- Senior affordable housing underway at 233 N. Second Ave. in Covina (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affordable housing under construction at 12461 Louise Ave. in Del Rey (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- New supportive housing opens at 8209 Sepulveda Blvd. in the Valley (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- PCCP Provides $41M Refinancing for Multifamily Community in San Diego (REBusiness Online, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- 75 apartments planned at 925 Eucalyptus Ave. in Inglewood (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Development Group Starts Work on 371-Unit Boynton Beach Multifamily Venture (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- High Street Residential, Barings Break Ground in Redwood City (Connect CRE California, California): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Preliminary Application For Affordable Housing at 55 Lapu-Lapu Street in SoMa, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Colliers Facilitates $20M Sale of Multifamily Property in Seattle (Connect CRE Apartments, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Developer Buys Land For Active Adult Apartments Near Novant Health Hospital (Bisnow, Sun Belt): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Mixed-use project approved for 2701 190th St. in Redondo Beach (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Multifamily starts fell in September amid high construction costs (Multifamily Dive, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Brooklyn Surpasses Manhattan in Multifamily Sales in Q3: Report (Commercial Observer, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- L.A. Multifamily Sales Jump 44% (Commercial Observer, Los Angeles / California): Supply/demand terms detected: effective_rent_growth, occupancy. Primary topic set to supply_demand; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993 (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 30

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.