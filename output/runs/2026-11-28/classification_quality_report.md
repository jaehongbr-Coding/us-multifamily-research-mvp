# Classification Quality Report

Generated: 2026-11-28 04:34:07

## Classification Summary

- Total articles classified: 74
- Topic distribution: transaction_market: 16; capital_markets: 14; development_pipeline: 13; gp_activity: 9; supply_demand: 9; other: 5; institutional_capital: 3; research_data: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 16 article(s), high 1, medium 8, low 7, unknown 0. Top markets: Other / Unknown (4); Atlanta / Georgia (4); Los Angeles / California (2); Miami / Florida (2); San Francisco / California (1).
- capital_markets: 14 article(s), high 10, medium 2, low 2, unknown 0. Top markets: New York City / New York (4); Miami / Florida (4); Other / Unknown (2); Seattle (1); Dallas / Texas (1).
- development_pipeline: 13 article(s), high 0, medium 3, low 10, unknown 0. Top markets: Other / Unknown (5); Los Angeles / California (2); San Francisco / California (2); Houston / Texas (1); Texas (1).
- gp_activity: 9 article(s), high 0, medium 0, low 1, unknown 8. Top markets: Other / Unknown (6); Atlanta / Georgia (1); National (1); Kentucky (1).
- supply_demand: 9 article(s), high 0, medium 0, low 9, unknown 0. Top markets: Other / Unknown (4); National (2); Houston / Texas (1); Dallas / Texas (1); New York City / New York (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (3); Other / Unknown (2).
- institutional_capital: 3 article(s), high 1, medium 1, low 1, unknown 0. Top markets: California (1); Other / Unknown (1); Atlanta / Georgia (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); New York City / New York (1).
- macro_financing: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Other / Unknown (2).

## Low Confidence / Unknown Articles

- Developer Fernmoor Secures $85M in Financing for North Jersey Developments (Yield PRO, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- OC Investor Group Buys Two Apartment Properties in Venice (Connect CRE, Los Angeles / California): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- New look for Metro joint development at 675 S. Crenshaw Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 10 condos planned at 2254 S. Wellesley Ave. in Sawtelle (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Coastal Commission upholds approval of project at 1410 S. Main St. in Venice (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Affordable housing commences work at 2201 E. 1st St. in Boyle Heights (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Culver City adopts parking maximums for new development (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 725 Houston Apartments Sit Vacant As Fercan Kalkan Fights Foreclosure (Bisnow, Houston / Texas): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Supply/demand terms detected: vacancy. Primary topic set to supply_demand; confidence low.
- HTG Opens Doors to 101-Unit Houston Mixed-Income Housing Project (Connect CRE Apartments, Houston / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Space Craft Adding to Charlotte Multifamily Holdings (Connect CRE Apartments, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Report: L.A. ranks fifth nationally for new apartment construction (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Report: L.A. permits 12,700 homes through third quarter of 2026 (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- JV Closes on $38.4M Refi for Fort Lauderdale Mixed-Use Venture (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Preliminary Permits Filed For 300 Lake Street, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Declining Conditions for Multifamily Missing Middle (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Optimus Properties Buys South Pasadena Mixed-Use Asset for $6.45M (Connect CRE California, Los Angeles / California): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Marcus & Millichap Palo Alto Office Brokers Sale of Multifamily Property Near Santa Clara University (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Additional low/unknown rows omitted: 28

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.