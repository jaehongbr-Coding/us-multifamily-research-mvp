# Classification Quality Report

Generated: 2026-09-15 01:12:15

## Classification Summary

- Total articles classified: 71
- Topic distribution: transaction_market: 17; capital_markets: 11; development_pipeline: 11; gp_activity: 10; supply_demand: 9; macro_financing: 6; other: 4; research_data: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 17 article(s), high 2, medium 7, low 8, unknown 0. Top markets: California (3); Los Angeles / California (3); Atlanta / Georgia (3); Other / Unknown (2); Dallas / Texas (2).
- capital_markets: 11 article(s), high 5, medium 5, low 1, unknown 0. Top markets: Miami / Florida (5); Other / Unknown (2); Phoenix / Arizona (1); Washington DC (1); Florida (1).
- development_pipeline: 11 article(s), high 2, medium 2, low 7, unknown 0. Top markets: Other / Unknown (7); Atlanta / Georgia (2); Los Angeles / California (1); California (1).
- gp_activity: 10 article(s), high 0, medium 0, low 0, unknown 10. Top markets: Other / Unknown (3); Phoenix / Arizona (2); Sun Belt (1); Miami / Florida (1); National (1).
- supply_demand: 9 article(s), high 0, medium 0, low 9, unknown 0. Top markets: Other / Unknown (6); National (3).
- macro_financing: 6 article(s), high 0, medium 0, low 1, unknown 5. Top markets: Other / Unknown (4); California (1); Atlanta / Georgia (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (3); California (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); Southeast (1).
- institutional_capital: 1 article(s), high 0, medium 0, low 1, unknown 0. Top markets: Los Angeles / California (1).

## Low Confidence / Unknown Articles

- Marcus & Millichap Arranges $8.64M Sale of 62-Unit Multifamily Property in Santa Catalina Island California (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Sales Of Lower-End Apartments Surge In Philly As Landlords Face Financial Issues (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Echo Park-adjacent apartments proposed at 820 N. Laguna Ave. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Metrolink fares rise, California condos dying, and more (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 13 apartments approved for empty lot at 4127 E. Supreme Court (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- 75 apartments slated for 7034 N. Baird Ave. in Reseda (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Former Sunkist HQ to become 95 apartments (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Interra Realty Brokers $19M Sale of River North Apartment Building (Connect CRE Apartments, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- C-PACE Financing is Now a Capital Stack Conversation (Connect CRE California, Los Angeles / California): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Rockefeller Group Files Plans to Build 340 Apartments at 200 West 97th Street (Commercial Observer, New York City / New York): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Short-Term Rental Giant Airbnb Launches $250M Housing Construction Fund (Commercial Observer, National): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- 101-Unit Luxury Multifamily Community in Marina del Rey California Trades for $24.8M (Yield PRO, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Embrey’s Garrett Karam Discusses Multifamily Investment Strategies (Commercial Observer, Sun Belt): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Essex Realty Group Markets 20-Unit Multifamily Portfolio in Chicago (Connect CRE, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Advance Realty Completes 52-Unit Apartment Building in Hoboken (REBusiness Online, Other / Unknown): Development-stage terms detected: delivery, redevelopment. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 28

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.