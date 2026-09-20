# Classification Quality Report

Generated: 2026-09-20 00:43:08

## Classification Summary

- Total articles classified: 81
- Topic distribution: transaction_market: 20; development_pipeline: 18; supply_demand: 9; capital_markets: 7; institutional_capital: 7; macro_financing: 7; gp_activity: 6; other: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 20 article(s), high 4, medium 11, low 5, unknown 0. Top markets: California (6); New York City / New York (3); Atlanta / Georgia (3); Phoenix / Arizona (2); Dallas / Texas (1).
- development_pipeline: 18 article(s), high 2, medium 5, low 11, unknown 0. Top markets: Other / Unknown (7); Miami / Florida (2); Atlanta / Georgia (2); Los Angeles / California (1); San Francisco / California (1).
- supply_demand: 9 article(s), high 0, medium 0, low 9, unknown 0. Top markets: Other / Unknown (6); National (3).
- capital_markets: 7 article(s), high 4, medium 2, low 1, unknown 0. Top markets: Miami / Florida (4); New York City / New York (1); Other / Unknown (1); Texas (1).
- institutional_capital: 7 article(s), high 2, medium 4, low 1, unknown 0. Top markets: Other / Unknown (3); California (1); Dallas / Texas (1); New York City / New York (1); Georgia (1).
- macro_financing: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Other / Unknown (5); California (1); Atlanta / Georgia (1).
- gp_activity: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (3); Colorado (1); National (1); Phoenix / Arizona (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (4); San Francisco / California (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- Downtown Brooklyn Development Site Fetches $84M (Connect CRE, New York City / New York): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- 65 apartments underway at 5909 S. Crenshaw Blvd. in Hyde Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing proposed at 12508 W. Pacific Ave. in Mar Vista (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- L.A. County Supes approve apartments at 7914 Broadway Ave. in West Whittier (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Apartments slated for 3648 S. Empire Dr. in Palms (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing completed at 1408 W. 162nd St. in South L.A. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- New Building Permits For 249 Pennsylvania Avenue, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Construction Underway For Alexan Icon, South San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Multifamily starts plummeted nearly 16% in August (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Construction Nearly Topped Out For 486 West San Carlos Street, San Jose (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Marcus & Millichap Closes Multifamily Sale in San Diego’s College East (Connect CRE, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Mixed-use building starts to rise at 8000 Beverly Blvd. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Decron Buys Miracle Mile Apartments For $114M: The Los Angeles Deal Sheet (Bisnow, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Thompson Thrift Hosts Ribbon Cutting for 276-Unit Multifamily Community Switch Luxury Apartments in Colorado Springs (Yield PRO, Colorado): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- HTG Debuts $115M Miami Affordable Housing Project (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Developer Pays $7M For Planned Old Town Conversion: The D.C. Deal Sheet (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Capstone Breaks Ground on 256-Unit Multifamily Development in Centerton, Arkansas (REBusiness Online, Southeast): Development-stage terms detected: construction_start, delivery. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 27

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.