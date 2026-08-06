# Classification Quality Report

Generated: 2026-08-06 00:01:04

## Classification Summary

- Total articles classified: 82
- Topic distribution: development_pipeline: 17; capital_markets: 14; transaction_market: 14; supply_demand: 13; gp_activity: 7; institutional_capital: 6; macro_financing: 5; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 17 article(s), high 0, medium 10, low 7, unknown 0. Top markets: Other / Unknown (6); San Francisco / California (3); Los Angeles / California (2); New York (1); Dallas / Texas (1).
- capital_markets: 14 article(s), high 6, medium 8, low 0, unknown 0. Top markets: Miami / Florida (4); Florida (2); Los Angeles / California (1); Dallas / Texas (1); Phoenix / Arizona (1).
- transaction_market: 14 article(s), high 2, medium 10, low 2, unknown 0. Top markets: California (3); Los Angeles / California (2); Atlanta / Georgia (2); Sun Belt (1); Seattle (1).
- supply_demand: 13 article(s), high 0, medium 1, low 12, unknown 0. Top markets: Other / Unknown (7); National (3); Atlanta / Georgia (1); Sun Belt (1); Georgia (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (3); National (2); New York City / New York (1); California (1).
- institutional_capital: 6 article(s), high 0, medium 3, low 3, unknown 0. Top markets: Atlanta / Georgia (2); Dallas / Texas (1); Virginia (1); New York City / New York (1); California (1).
- macro_financing: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (2); California (1); Los Angeles / California (1); Texas (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Santa Monica / California (1); California (1); Los Angeles / California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); California (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- JLL Lists Staten Island Waterfront Development for $45M (Connect CRE, New York): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Lightstone Capital Originates Senior Loans for Two San Diego Multifamily Properties (Connect CRE, California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Adaptive reuse project starting up at 6380 Wilshire Boulevard (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- New plan for affordable housing at 2127 S. Westwood Boulevard (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- New look for 353-unit development at 1633 26th St. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Afforable housing slated for property at 1850 Atlantic Ave. in Long Beach (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Construction goes vertical for affordable housing at 1540 Court St. in Echo Park (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Jamison pivots to affordable housing at 975 S. Manhattan Pl. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Small lot homes with ADUs pitched for 18220 Superior St. in Northridge (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- CBRE Arranges Sale of $112M Lynnwood Apartment Complex (Connect CRE Apartments, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Camden Property Trust Completes Largest U.S Multifamily Sale Since 2024 (Connect CRE Apartments, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Atlanta Beltline Advancing 218-Unit Affordable Apartment Project (Connect CRE Atlanta, Atlanta / Georgia): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Lument’s Vic Clark Provides Preview on How Deals Are Getting Done for Upcoming Texas Multifamily 2026 (Connect CRE Texas, Dallas / Texas): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Capital Square Launches $42.95M DST for Apartment Community Near Richmond Virginia (Yield PRO, Virginia): Institutional activity terms detected: gp_acquisition, gp_disposition. Primary topic set to institutional_capital; confidence low.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- LJS Development Breaks Ground on 25-Unit Affordable Housing Project in Randolph, New Jersey (REBusiness Online, Other / Unknown): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 22

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.