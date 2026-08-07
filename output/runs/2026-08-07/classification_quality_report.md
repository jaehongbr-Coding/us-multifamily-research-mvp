# Classification Quality Report

Generated: 2026-08-07 01:42:27

## Classification Summary

- Total articles classified: 77
- Topic distribution: capital_markets: 18; development_pipeline: 15; supply_demand: 13; transaction_market: 10; macro_financing: 6; institutional_capital: 5; gp_activity: 4; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- capital_markets: 18 article(s), high 9, medium 9, low 0, unknown 0. Top markets: Miami / Florida (4); Seattle (2); Florida (2); Los Angeles / California (1); New York City / New York (1).
- development_pipeline: 15 article(s), high 0, medium 8, low 7, unknown 0. Top markets: Other / Unknown (5); Los Angeles / California (2); California (2); Atlanta / Georgia (1); Nashville / Tennessee (1).
- supply_demand: 13 article(s), high 0, medium 1, low 12, unknown 0. Top markets: Other / Unknown (7); National (4); Atlanta / Georgia (1); Sun Belt (1).
- transaction_market: 10 article(s), high 1, medium 8, low 1, unknown 0. Top markets: Atlanta / Georgia (3); Miami / Florida (3); Phoenix / Arizona (2); California (2).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (2); California (1); Los Angeles / California (1); New York City / New York (1); Texas (1).
- institutional_capital: 5 article(s), high 0, medium 2, low 3, unknown 0. Top markets: Atlanta / Georgia (2); Dallas / Texas (1); Virginia (1); California (1).
- gp_activity: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (2); National (2).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (1); Santa Monica / California (1); California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); Southeast (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- L.A. County approves $15M for supportive housing at Metropolitan State Hospital campus (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing with retail pitched for 2306 W. Jefferson Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Adaptive reuse project starting up at 6380 Wilshire Boulevard (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- New plan for affordable housing at 2127 S. Westwood Boulevard (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- New look for 353-unit development at 1633 26th St. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Afforable housing slated for property at 1850 Atlantic Ave. in Long Beach (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Lightstone Capital Originates Senior Loans for Two San Diego Multifamily Properties (Connect CRE California, California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Camden Property Trust Completes Largest U.S Multifamily Sale Since 2024 (Connect CRE California, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Preliminary Permits Filed For 110 Glenwood Avenue, Atherton (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Atlanta Beltline Advancing 218-Unit Affordable Apartment Project (Connect CRE Atlanta, Atlanta / Georgia): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Lument’s Vic Clark Provides Preview on How Deals Are Getting Done for Upcoming Texas Multifamily 2026 (Connect CRE Texas, Dallas / Texas): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Capital Square Launches $42.95M DST for Apartment Community Near Richmond Virginia (Yield PRO, Virginia): Institutional activity terms detected: gp_acquisition, gp_disposition. Primary topic set to institutional_capital; confidence low.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Nation’s Leading Cottage-Style BTR Developer Opens Third Avilla homes Neighborhood in Greater Tampa (Yield PRO, Tampa / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- W. Palm Beach Investor Buys Condo Property, Converting to Apartment Units (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Institutional Property Advisors Negotiates Suburban New York City Multifamily Asset Sale (Yield PRO, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Additional low/unknown rows omitted: 19

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.