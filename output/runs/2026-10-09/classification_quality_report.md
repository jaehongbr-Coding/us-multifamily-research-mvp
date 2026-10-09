# Classification Quality Report

Generated: 2026-10-09 02:49:21

## Classification Summary

- Total articles classified: 75
- Topic distribution: transaction_market: 15; development_pipeline: 11; supply_demand: 11; capital_markets: 10; gp_activity: 9; macro_financing: 7; institutional_capital: 5; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 15 article(s), high 2, medium 9, low 4, unknown 0. Top markets: Atlanta / Georgia (4); Seattle (3); Other / Unknown (2); California (2); Los Angeles / California (1).
- development_pipeline: 11 article(s), high 1, medium 4, low 6, unknown 0. Top markets: Other / Unknown (4); Phoenix / Arizona (2); Los Angeles / California (1); Florida (1); National (1).
- supply_demand: 11 article(s), high 0, medium 0, low 11, unknown 0. Top markets: Other / Unknown (7); National (2); Miami / Florida (1); Atlanta / Georgia (1).
- capital_markets: 10 article(s), high 3, medium 5, low 2, unknown 0. Top markets: National (2); Miami / Florida (2); Virginia (2); California (1); Phoenix / Arizona (1).
- gp_activity: 9 article(s), high 0, medium 0, low 0, unknown 9. Top markets: Other / Unknown (5); New York City / New York (1); Georgia (1); Los Angeles / California (1); National (1).
- macro_financing: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (3); Los Angeles / California (2); Tennessee (2).
- institutional_capital: 5 article(s), high 0, medium 4, low 1, unknown 0. Top markets: Washington DC (2); Miami / Florida (2); Florida (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (1); California (1); Santa Monica / California (1); San Francisco / California (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Santa Monica / California (2); Los Angeles / California (1).

## Low Confidence / Unknown Articles

- First phase of housing and healthcare campus commences at 800 N. Main St. in Chinatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- LAUSD board moves forward with plans for housing at sites in West Hollywood and Woodland Hills (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Rendering vs. Reality: Affordable housing at 1400 Long Beach Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Mixed-use project slated to replace Mel's Drive-In in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 388 apartments to replace offices at 3200 E. Carson St. in Lakewood (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing completed at 7220 Maie Avenue in Florence-Firestone (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Fresh imagery for proposed housing complex at 1238 Lincoln Blvd. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Updated Renderings For 360 5th Street in SoMa, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Design tweaks for affordable housing at 1238 7th St. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Development Group Starts Work on 371-Unit Boynton Beach Multifamily Venture (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Developers Scheme To Build More Housing Units As NYC's Tax Incentive Ages (Bisnow, New York City / New York): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Rockland Trust Provides Financing for Quincy Affordable Development (Connect CRE, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Related Affiliate Obtains $167M Loan Package for Miami Apartment Community (Connect CRE South Florida, Miami / Florida): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Space Craft Building 4th Charlotte Optimist Park Rental Community (Connect CRE Apartments, Atlanta / Georgia): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Institutional Property Advisors Brokers $72M Puget Sound MF Sale (Connect CRE Apartments, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- WinnCompany Completes $46M Transit-Oriented Mixed-Income Multifamily Community Near Boston (Yield PRO, National): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993 (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Additional low/unknown rows omitted: 27

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.