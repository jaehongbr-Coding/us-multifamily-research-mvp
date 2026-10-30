# Classification Quality Report

Generated: 2026-10-30 02:25:43

## Classification Summary

- Total articles classified: 76
- Topic distribution: transaction_market: 15; development_pipeline: 13; capital_markets: 11; gp_activity: 8; supply_demand: 8; macro_financing: 7; other: 7; institutional_capital: 6
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 15 article(s), high 1, medium 10, low 4, unknown 0. Top markets: Atlanta / Georgia (4); Other / Unknown (3); California (3); New York (1); Utah (1).
- development_pipeline: 13 article(s), high 0, medium 5, low 8, unknown 0. Top markets: Other / Unknown (4); Los Angeles / California (2); Atlanta / Georgia (2); Florida (1); Dallas / Texas (1).
- capital_markets: 11 article(s), high 8, medium 3, low 0, unknown 0. Top markets: Other / Unknown (2); Los Angeles / California (2); Dallas / Texas (2); Houston / Texas (1); San Francisco / California (1).
- gp_activity: 8 article(s), high 0, medium 0, low 0, unknown 8. Top markets: Other / Unknown (3); Phoenix / Arizona (2); Arizona (1); National (1); Dallas / Texas (1).
- supply_demand: 8 article(s), high 0, medium 0, low 8, unknown 0. Top markets: Other / Unknown (5); National (2); Miami / Florida (1).
- macro_financing: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (3); San Francisco / California (1); Los Angeles / California (1); California (1); Virginia (1).
- other: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Los Angeles / California (3); Other / Unknown (2); San Francisco / California (2).
- institutional_capital: 6 article(s), high 1, medium 3, low 2, unknown 0. Top markets: California (2); Other / Unknown (2); Miami / Florida (1); Atlanta / Georgia (1).
- research_data: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: California (1).

## Low Confidence / Unknown Articles

- 37-unit affordable housing complex underway at 3751 S. Delmas Ter. in Palms (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 25 apartments completed at 11013 Hartsook St. in North Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- 390 apartments underway at 6615 PCH in Long Beach (Urbanize LA, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Modular affordable housing takes shape at 4301 S. Vermont Ave. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affordable housing starts work at 400 Centinela Ave. in Inglewood (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- 12 homes pitched for 2315 S. Oakwood Ave. in Venice (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Groundbreaking held for mixed-use project at 3800 W. 6th St. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- New look for proposed apartment complex at 5600 Hollywood Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Construction Starts For 39340 Fremont Boulevard, Fremont (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Historic Kansas City Country Club Plaza MF Asset Trades (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Apartments, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- 45-Story Tower Proposed For 325 Fremont Street, SoMa, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Prosper Greenlights $2B Italian-Themed Community (Connect CRE Texas, Dallas / Texas): Development-stage terms detected: entitlement, zoning. Primary topic set to development_pipeline; confidence low.
- Leon Multifamily Building 343-Unit N. Phoenix Venture (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Origin, Mill Creek Teaming Up on 190-Unit Scottsdale Rental Community (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- The Saint Clair Brings Affordable Apartments and Commercial Space to Downtown Yonkers Near Metro-North (Yield PRO, New York): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993 (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Origin Investments, Mill Creek Residential to Develop 190-Unit Apartment Community in Old Town Scottsdale (REBusiness Online, Phoenix / Arizona): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 25

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.