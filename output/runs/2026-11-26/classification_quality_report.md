# Classification Quality Report

Generated: 2026-11-26 04:43:16

## Classification Summary

- Total articles classified: 75
- Topic distribution: transaction_market: 17; capital_markets: 15; development_pipeline: 12; gp_activity: 9; supply_demand: 9; other: 4; institutional_capital: 3; macro_financing: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 17 article(s), high 1, medium 11, low 5, unknown 0. Top markets: Other / Unknown (5); Atlanta / Georgia (4); Los Angeles / California (2); Miami / Florida (2); National (1).
- capital_markets: 15 article(s), high 10, medium 4, low 1, unknown 0. Top markets: Miami / Florida (4); Other / Unknown (3); New York City / New York (3); Seattle (2); Santa Monica / California (1).
- development_pipeline: 12 article(s), high 0, medium 4, low 8, unknown 0. Top markets: Other / Unknown (5); New York (2); Los Angeles / California (2); Houston / Texas (1); San Francisco / California (1).
- gp_activity: 9 article(s), high 0, medium 0, low 0, unknown 9. Top markets: Other / Unknown (6); Atlanta / Georgia (1); National (1); Kentucky (1).
- supply_demand: 9 article(s), high 0, medium 0, low 9, unknown 0. Top markets: Other / Unknown (4); National (2); Houston / Texas (1); Dallas / Texas (1); New York City / New York (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (3); National (1).
- institutional_capital: 3 article(s), high 1, medium 1, low 1, unknown 0. Top markets: California (1); Other / Unknown (1); Atlanta / Georgia (1).
- macro_financing: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Other / Unknown (2); California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (1); Santa Monica / California (1); New York City / New York (1).

## Low Confidence / Unknown Articles

- CBRE Arranges $85M Loan for Two New Jersey Multifamily Assets (Yield PRO, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- OC Investor Group Buys Two Apartment Properties in Venice (Connect CRE, Los Angeles / California): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- 10 condos planned at 2254 S. Wellesley Ave. in Sawtelle (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Coastal Commission upholds approval of project at 1410 S. Main St. in Venice (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Affordable housing commences work at 2201 E. 1st St. in Boyle Heights (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Santa Monica has new plans for affordable housing next to Downtown Metro stop (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Dwight Capital Finances $52M Loan for Mixed-Use Multifamily Community in Michigan (Connect CRE, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Culver City adopts parking maximums for new development (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 725 Houston Apartments Sit Vacant As Fercan Kalkan Fights Foreclosure (Bisnow, Houston / Texas): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Supply/demand terms detected: vacancy. Primary topic set to supply_demand; confidence low.
- New plan for housing at 4600 Wilshire Blvd. (Urbanize LA, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- HTG Opens Doors to 101-Unit Houston Mixed-Income Housing Project (Connect CRE Apartments, Houston / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Marcus & Millichap Brokers $10.1M Sale of Harlan Apartments First Offered Since 1972 (Yield PRO, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Space Craft Adding to Charlotte Multifamily Holdings (Connect CRE Apartments, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Report: L.A. permits 12,700 homes through third quarter of 2026 (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- JV Closes on $38.4M Refi for Fort Lauderdale Mixed-Use Venture (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Preliminary Permits Filed For 300 Lake Street, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Declining Conditions for Multifamily Missing Middle (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 23

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.