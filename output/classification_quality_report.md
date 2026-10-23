# Classification Quality Report

Generated: 2026-10-23 01:15:52

## Classification Summary

- Total articles classified: 68
- Topic distribution: development_pipeline: 15; supply_demand: 12; gp_activity: 9; capital_markets: 8; institutional_capital: 8; transaction_market: 8; macro_financing: 5; other: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 15 article(s), high 0, medium 6, low 9, unknown 0. Top markets: Other / Unknown (5); Los Angeles / California (3); California (2); Washington DC (2); Phoenix / Arizona (1).
- supply_demand: 12 article(s), high 0, medium 0, low 12, unknown 0. Top markets: Other / Unknown (7); Miami / Florida (2); National (2); California (1).
- gp_activity: 9 article(s), high 0, medium 0, low 0, unknown 9. Top markets: Other / Unknown (4); National (2); Los Angeles / California (1); San Francisco / California (1); Salt Lake City / Utah (1).
- capital_markets: 8 article(s), high 4, medium 3, low 1, unknown 0. Top markets: Los Angeles / California (2); Miami / Florida (2); California (2); Washington DC (1); Georgia (1).
- institutional_capital: 8 article(s), high 2, medium 3, low 3, unknown 0. Top markets: Other / Unknown (2); California (2); Seattle (1); New York (1); Los Angeles / California (1).
- transaction_market: 8 article(s), high 1, medium 5, low 2, unknown 0. Top markets: Atlanta / Georgia (3); Other / Unknown (1); California (1); Colorado (1); San Francisco / California (1).
- macro_financing: 5 article(s), high 0, medium 0, low 1, unknown 4. Top markets: Other / Unknown (4); California (1).
- other: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); Santa Monica / California (1).
- research_data: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: San Francisco / California (1).

## Low Confidence / Unknown Articles

- 6 Blackstone multifamily properties move to servicing (Multifamily Dive, Seattle): Institutional activity terms detected: private_equity_activity. Primary topic set to institutional_capital; confidence low.
- Expansion of apartment complex at 6007 Sunset survives appeal (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Senior affordable housing underway at 233 N. Second Ave. in Covina (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affordable housing under construction at 12461 Louise Ave. in Del Rey (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- New supportive housing opens at 8209 Sepulveda Blvd. in the Valley (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Development Group Starts Work on 371-Unit Boynton Beach Multifamily Venture (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Developer plans high-rise apartments at 6409 Sunset Blvd. in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Preliminary Application For Affordable Housing at 55 Lapu-Lapu Street in SoMa, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Mixed-use project approved for 2701 190th St. in Redondo Beach (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Multifamily starts fell in September amid high construction costs (Multifamily Dive, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993 (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Aimco Advancing Luxury Edgewater Apartments (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: effective_rent_growth, occupancy. Primary topic set to supply_demand; confidence low.
- Investor Takes Over Distressed Atlanta Apartment Asset (Connect CRE Atlanta, Atlanta / Georgia): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Thompson Thrift Pursuing 319-Unit Powder Springs Rental Community (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: lease_up. Primary topic set to development_pipeline; confidence low.
- Shorter Apartment Construction Time in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery, permit. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 24

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.