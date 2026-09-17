# Classification Quality Report

Generated: 2026-09-17 01:06:52

## Classification Summary

- Total articles classified: 75
- Topic distribution: transaction_market: 15; development_pipeline: 14; capital_markets: 11; supply_demand: 11; gp_activity: 10; macro_financing: 5; other: 5; institutional_capital: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 15 article(s), high 2, medium 9, low 4, unknown 0. Top markets: California (4); Atlanta / Georgia (3); Seattle (2); Phoenix / Arizona (2); Los Angeles / California (1).
- development_pipeline: 14 article(s), high 1, medium 5, low 8, unknown 0. Top markets: Other / Unknown (7); Miami / Florida (2); Atlanta / Georgia (2); Los Angeles / California (1); Dallas / Texas (1).
- capital_markets: 11 article(s), high 4, medium 6, low 1, unknown 0. Top markets: Other / Unknown (4); Miami / Florida (4); Sun Belt (1); California (1); West Palm Beach / Florida (1).
- supply_demand: 11 article(s), high 0, medium 0, low 11, unknown 0. Top markets: Other / Unknown (6); National (2); San Francisco / California (1); Sun Belt (1); Texas (1).
- gp_activity: 10 article(s), high 0, medium 0, low 1, unknown 9. Top markets: Other / Unknown (3); Miami / Florida (2); Houston / Texas (1); Austin / Texas (1); New York (1).
- macro_financing: 5 article(s), high 0, medium 0, low 1, unknown 4. Top markets: Other / Unknown (3); California (1); Atlanta / Georgia (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (3); San Francisco / California (2).
- institutional_capital: 2 article(s), high 0, medium 2, low 0, unknown 0. Top markets: California (1); Other / Unknown (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- Stewards Sets Up $240M Deal for Two South Florida Multifamily Properties (Commercial Observer, Miami / Florida): Development-stage terms detected: density_bonus. Primary topic set to gp_activity; confidence low.
- Apartments slated for 3648 S. Empire Dr. in Palms (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing completed at 1408 W. 162nd St. in South L.A. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Affordable housing tops out at 10953 Whipple St. in Toluca Lake (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Echo Park-adjacent apartments proposed at 820 N. Laguna Ave. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Construction Underway For Alexan Icon, South San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Plans Refiled for 395 3rd Street in SoMa, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Apartment, Townhome Complex in Sammamish Trades Hands (Connect CRE Apartments, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Naranja Grand Phase I Delivers 120 Income-Restricted 55+Senior Apartments and Naranja Grand Phase II Delivers 200 for Families in South Dade (Yield PRO, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Mixed-use building starts to rise at 8000 Beverly Blvd. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- U.S. Apartment Rents Decline for First Time in Eight Months: Report (Commercial Observer, San Francisco / California): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Port of Cleveland Greenlights Multifamily Mixed-Use Redevelopment Project Financing (Yield PRO, Other / Unknown): Development-stage terms detected: entitlement, redevelopment. Primary topic set to development_pipeline; confidence low.
- 29th Street Trades Aurora Apartment Community for $72.5M (Connect CRE Apartments, Phoenix / Arizona): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Space Craft Begins Leasing 389-Unit Apartment Community in Charlotte (REBusiness Online, Sun Belt): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- HTG Debuts $115M Miami Affordable Housing Project (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Rice Planning 24-Story Multifamily Community (Connect CRE Texas, Houston / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 26

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.