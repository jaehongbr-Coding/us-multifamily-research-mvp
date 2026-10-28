# Classification Quality Report

Generated: 2026-10-28 02:02:15

## Classification Summary

- Total articles classified: 88
- Topic distribution: development_pipeline: 21; transaction_market: 16; capital_markets: 14; supply_demand: 11; gp_activity: 7; institutional_capital: 7; macro_financing: 6; other: 6
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 21 article(s), high 2, medium 8, low 11, unknown 0. Top markets: Other / Unknown (8); California (5); Los Angeles / California (3); Kentucky (2); Seattle (1).
- transaction_market: 16 article(s), high 2, medium 8, low 6, unknown 0. Top markets: Other / Unknown (4); Atlanta / Georgia (4); California (3); National (2); Utah (1).
- capital_markets: 14 article(s), high 6, medium 5, low 3, unknown 0. Top markets: California (3); Other / Unknown (3); Los Angeles / California (2); Miami / Florida (2); Denver / Colorado (1).
- supply_demand: 11 article(s), high 0, medium 0, low 11, unknown 0. Top markets: Other / Unknown (6); California (2); National (2); Miami / Florida (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (3); Phoenix / Arizona (2); Arizona (1); National (1).
- institutional_capital: 7 article(s), high 0, medium 2, low 5, unknown 0. Top markets: California (2); New York (1); Texas (1); New York City / New York (1); Other / Unknown (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: California (2); Other / Unknown (2); San Francisco / California (1); Virginia (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Los Angeles / California (4); Other / Unknown (1); San Francisco / California (1).

## Low Confidence / Unknown Articles

- Northmarq Arranges Sale of Record-Setting 627-Unit Multifamily Community in Lawrence Kansas (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Marcus & Millichap Arranges $9.65M Sale of 35-Unit Multifamily Property in Anaheim California (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Orange County, Calif., Apartment Sales Up 15.6%, but Values Fall (Commercial Observer, California): Supply/demand terms detected: effective_rent_growth, occupancy. Primary topic set to supply_demand; confidence low.
- PCCP Provides $164M Senior Loan for Paramus Multifamily Project (Connect CRE, New York): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- 12 homes pitched for 2315 S. Oakwood Ave. in Venice (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Groundbreaking held for mixed-use project at 3800 W. 6th St. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- New look for proposed apartment complex at 5600 Hollywood Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Bjarke Ingels-designed project in the works at 2810 N. Hyperion Ave. in Silver Lake (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Alveare affordable housing topped out at 1405 S. Broadway in DTLA (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Mixed-use project completed at Sunset and Fairfax in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Akara, DEVEN to Break Ground on 305-Bed Student Housing Project Near San Diego State University (REBusiness Online, California): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Essex Realty Group Closes 12-Unit Rogers Park Multifamily Transaction (Connect CRE Apartments, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Eight townhomes in the works at 146 N. Berendo St. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Retail market tightens, L.A. multifamily sales jump, and more (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Leon Multifamily Building 343-Unit N. Phoenix Venture (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Capital Flooded Into Bay Area Apartments. Then Treasury Yields Spiked (Bisnow, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- National City Investment Group Commences Workforce Housing Build (Connect CRE California, California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Transwestern, NewQuest Advancing Kyle Mixed-Use Project (Connect CRE Texas, Texas): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Origin, Mill Creek Teaming Up on 190-Unit Scottsdale Rental Community (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 35

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.