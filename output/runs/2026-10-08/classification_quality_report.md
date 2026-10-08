# Classification Quality Report

Generated: 2026-10-08 02:34:46

## Classification Summary

- Total articles classified: 76
- Topic distribution: development_pipeline: 16; capital_markets: 14; transaction_market: 13; supply_demand: 10; gp_activity: 7; macro_financing: 6; institutional_capital: 3; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 16 article(s), high 1, medium 5, low 10, unknown 0. Top markets: Other / Unknown (8); Phoenix / Arizona (2); Los Angeles / California (1); Atlanta / Georgia (1); Florida (1).
- capital_markets: 14 article(s), high 6, medium 4, low 4, unknown 0. Top markets: Houston / Texas (3); California (3); Other / Unknown (2); Phoenix / Arizona (1); Washington DC (1).
- transaction_market: 13 article(s), high 3, medium 7, low 3, unknown 0. Top markets: Atlanta / Georgia (5); Florida (1); San Francisco / California (1); California (1); Virginia (1).
- supply_demand: 10 article(s), high 0, medium 0, low 10, unknown 0. Top markets: Other / Unknown (7); National (2); Miami / Florida (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (4); Los Angeles / California (1); Atlanta / Georgia (1); National (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (4); Tennessee (1); Los Angeles / California (1).
- institutional_capital: 3 article(s), high 1, medium 1, low 1, unknown 0. Top markets: Miami / Florida (2); Other / Unknown (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: California (1); Santa Monica / California (1); San Francisco / California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Santa Monica / California (2); Beverly Hills / California (1).
- entitlement_policy: 1 article(s), high 0, medium 0, low 1, unknown 0. Top markets: New York City / New York (1).

## Low Confidence / Unknown Articles

- Mixed-use project slated to replace Mel's Drive-In in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 388 apartments to replace offices at 3200 E. Carson St. in Lakewood (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing completed at 7220 Maie Avenue in Florence-Firestone (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Fresh imagery for proposed housing complex at 1238 Lincoln Blvd. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Mixed-use project proposed at 177 S. Robertson Blvd. in Beverly Hills (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Updated Renderings For 360 5th Street in SoMa, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Design tweaks for affordable housing at 1238 7th St. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Development Group Starts Work on 371-Unit Boynton Beach Multifamily Venture (Connect CRE Apartments, Miami / Florida): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Related Affiliate Obtains $167M Loan Package for Miami Apartment Community (Connect CRE South Florida, Miami / Florida): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- WinnCompanies Lines Up Financing for Mixed-Income Salem TOD (Connect CRE, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Dwight Capital Finances $60M Loan for Iowa Multifamily Community (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Construction loan issued for affordable housing at 400 Centinela Ave. in Inglewood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: construction_financing. Financing type keywords detected: construction_loan. Primary topic set to capital_markets; confidence low.
- Neshaminy Mall Redevelopment Plans Revealed: The Philadelphia Deal Sheet (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993 (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Investor Takes Over Distressed Atlanta Apartment Asset (Connect CRE Atlanta, Atlanta / Georgia): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Additional low/unknown rows omitted: 28

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.