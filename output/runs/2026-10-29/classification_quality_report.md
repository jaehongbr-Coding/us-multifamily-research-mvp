# Classification Quality Report

Generated: 2026-10-29 02:09:04

## Classification Summary

- Total articles classified: 83
- Topic distribution: development_pipeline: 17; transaction_market: 14; macro_financing: 12; institutional_capital: 10; supply_demand: 9; capital_markets: 7; gp_activity: 7; other: 7
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 17 article(s), high 0, medium 6, low 11, unknown 0. Top markets: Other / Unknown (5); Los Angeles / California (3); Dallas / Texas (2); California (2); Florida (1).
- transaction_market: 14 article(s), high 1, medium 8, low 5, unknown 0. Top markets: Atlanta / Georgia (4); California (3); Other / Unknown (2); Riverside / California (1); Seattle (1).
- macro_financing: 12 article(s), high 0, medium 0, low 0, unknown 12. Top markets: Other / Unknown (5); California (2); San Francisco / California (1); Los Angeles / California (1); Atlanta / Georgia (1).
- institutional_capital: 10 article(s), high 2, medium 4, low 4, unknown 0. Top markets: Other / Unknown (3); California (1); New York City / New York (1); Washington DC (1); Virginia (1).
- supply_demand: 9 article(s), high 0, medium 0, low 9, unknown 0. Top markets: Other / Unknown (5); National (2); New York City / New York (1); Miami / Florida (1).
- capital_markets: 7 article(s), high 3, medium 4, low 0, unknown 0. Top markets: Miami / Florida (2); California (1); New York (1); Nevada (1); Los Angeles / California (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (3); Phoenix / Arizona (2); Arizona (1); National (1).
- other: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Los Angeles / California (3); Other / Unknown (3); San Francisco / California (1).

## Low Confidence / Unknown Articles

- 390 apartments underway at 6615 PCH in Long Beach (Urbanize LA, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Modular affordable housing takes shape at 4301 S. Vermont Ave. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affordable housing starts work at 400 Centinela Ave. in Inglewood (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- 12 homes pitched for 2315 S. Oakwood Ave. in Venice (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Groundbreaking held for mixed-use project at 3800 W. 6th St. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- New look for proposed apartment complex at 5600 Hollywood Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Bjarke Ingels-designed project in the works at 2810 N. Hyperion Ave. in Silver Lake (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Alveare affordable housing topped out at 1405 S. Broadway in DTLA (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Mixed-use project completed at Sunset and Fairfax in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Construction Starts For 39340 Fremont Boulevard, Fremont (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- CBRE Arranges $85M in Financing for Apartment Community in Downingtown, Pennsylvania (REBusiness Online, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Kidder Mathews Arranges Sale of 54K-SF MF Development Site in Kirkland (Connect CRE Apartments, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Wood Partners Building 372-Unit Charlotte Rental Community (Connect CRE Apartments, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Mattapan Site Will Contain 105 Affordable Housing Units (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: joint_venture, disposition. Primary topic set to institutional_capital; confidence low.
- Development Site Trades within Atlantic Avenue Mixed-Use Plan (Connect CRE, New York City / New York): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Prosper Greenlights $2B Italian-Themed Community (Connect CRE Apartments, Dallas / Texas): Development-stage terms detected: entitlement, zoning. Primary topic set to development_pipeline; confidence low.
- Leon Multifamily Building 343-Unit N. Phoenix Venture (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Affordable Housing Giant Starts $180M Philly Push: The Philadelphia Deal Sheet (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- National City Investment Group Commences Workforce Housing Build (Connect CRE California, California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 35

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.