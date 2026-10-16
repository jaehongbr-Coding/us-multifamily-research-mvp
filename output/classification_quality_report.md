# Classification Quality Report

Generated: 2026-10-16 01:01:33

## Classification Summary

- Total articles classified: 77
- Topic distribution: transaction_market: 15; development_pipeline: 13; capital_markets: 12; supply_demand: 11; gp_activity: 8; institutional_capital: 6; macro_financing: 4; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 15 article(s), high 1, medium 5, low 9, unknown 0. Top markets: California (4); Atlanta / Georgia (4); Dallas / Texas (3); Other / Unknown (2); Miami / Florida (1).
- development_pipeline: 13 article(s), high 0, medium 2, low 11, unknown 0. Top markets: Other / Unknown (8); National (2); Atlanta / Georgia (1); Southeast (1); Dallas / Texas (1).
- capital_markets: 12 article(s), high 3, medium 8, low 1, unknown 0. Top markets: California (4); Miami / Florida (2); Georgia (1); Other / Unknown (1); New York City / New York (1).
- supply_demand: 11 article(s), high 0, medium 0, low 11, unknown 0. Top markets: Other / Unknown (7); Miami / Florida (2); National (2).
- gp_activity: 8 article(s), high 0, medium 0, low 0, unknown 8. Top markets: Other / Unknown (6); California (1); National (1).
- institutional_capital: 6 article(s), high 2, medium 2, low 2, unknown 0. Top markets: California (3); Florida (1); Miami / Florida (1); Other / Unknown (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (2); Los Angeles / California (1); New York City / New York (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Santa Monica / California (1); Other / Unknown (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Colorado (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- Marcus & Millichap Facilitates Sale of Two-Property Multifamily Distressed Portfolio in Dallas (Yield PRO, Dallas / Texas): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- JLL Closes Sale of Retail and Multifamily Portfolio in Dallas’ Bishop Arts District (Yield PRO, Dallas / Texas): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Developers land financing for mixed-use project at 11111 Jefferson Blvd. in Culver City (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Southwest Valley Community Plans take a step forward (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Jamison flips to affordable housing at 679 S. Harvard Blvd. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- More Pasadena affordable housing in the works at 1976 E. Colorado Blvd. (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing takes shape at 327 S. Harbor Blvd. in San Pedro (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Warner Center development site showing activity at 6160 Variel Ave. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- New look for Westwood housing complex at 11027 W. Strathmore Dr. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- CBRE Arranges $40M Sale of 178-Unit MF in Downtown Portland (Connect CRE Apartments, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Embrey Scores $76.2M Financing for 354-Unit Orlando Apartment Community (Connect CRE Apartments, Florida): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- New look for large apartment complex at 444 N. Fair Oaks Ave. in Pasadena (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Kennedy Wilson Partners with Hulic, Fuyo General Lease on San Jose Apartment Deal (Connect CRE California, California): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Rendering vs. Reality: Mixed-use building at 1808 Lincoln Blvd. in Venice (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Wood framing rising for mixed-use project at 5843 W. Pico Blvd. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Development Group Starts Work on 371-Unit Boynton Beach Multifamily Venture (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- North County Apartment Duo Trades for $37M (Connect CRE California, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Apartments Being Developed on Parking Lot Adjacent to Local Grocer in San Diego Area (Yield PRO, California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 34

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.