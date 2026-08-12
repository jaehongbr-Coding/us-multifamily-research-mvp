# Classification Quality Report

Generated: 2026-08-12 23:41:33

## Classification Summary

- Total articles classified: 89
- Topic distribution: transaction_market: 22; supply_demand: 14; capital_markets: 13; development_pipeline: 9; gp_activity: 8; institutional_capital: 8; other: 7; macro_financing: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 22 article(s), high 2, medium 14, low 6, unknown 0. Top markets: Other / Unknown (4); Phoenix / Arizona (3); California (3); Florida (2); Miami / Florida (2).
- supply_demand: 14 article(s), high 0, medium 2, low 12, unknown 0. Top markets: Other / Unknown (8); National (4); Atlanta / Georgia (1); Sun Belt (1).
- capital_markets: 13 article(s), high 4, medium 9, low 0, unknown 0. Top markets: Miami / Florida (5); Other / Unknown (2); California (2); Salt Lake City / Utah (1); Houston / Texas (1).
- development_pipeline: 9 article(s), high 0, medium 4, low 5, unknown 0. Top markets: Other / Unknown (3); Los Angeles / California (1); California (1); Atlanta / Georgia (1); Houston / Texas (1).
- gp_activity: 8 article(s), high 0, medium 0, low 1, unknown 7. Top markets: Dallas / Texas (2); Other / Unknown (2); National (2); Sun Belt (1); Miami / Florida (1).
- institutional_capital: 8 article(s), high 1, medium 4, low 3, unknown 0. Top markets: New York (3); Other / Unknown (2); Dallas / Texas (1); Atlanta / Georgia (1); California (1).
- other: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (3); Los Angeles / California (2); California (1); National (1).
- macro_financing: 5 article(s), high 0, medium 0, low 1, unknown 4. Top markets: Other / Unknown (2); San Francisco / California (1); Atlanta / Georgia (1); Louisville / Kentucky (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (1); Southeast (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- AV Management Nabs SoHo Mixed-Use for $43M (Connect CRE, New York): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- U.S. Multifamily Gains Momentum in Q2 2026 as Absorption Surges (Connect CRE, National): Supply/demand terms detected: effective_rent_growth, vacancy, absorption. Primary topic set to supply_demand; confidence low.
- Affordable housing proposed at 1058 N. Kingsley Dr. in East Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- After 30-Year Hold, Monarch Offloads Golden Apartment Community (Connect CRE Apartments, Phoenix / Arizona): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- California Awards $239M in Gap Funding to 20 Affordable Projects (Connect CRE Apartments, California): Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Monterey Park approves upsized project at 114 E. Garvey Avenue (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Construction begins for student housing at Long Beach City College (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Walker & Dunlop Arranges $147.5M Debt and Equity Capitalization for Mixed-Use Development in Port Chester New York (Yield PRO, New York): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- 42 apartments slated for 2817 Montrose Ave. in Glendale (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Atlanta Beltline Advancing 218-Unit Affordable Apartment Project (Connect CRE Atlanta, Atlanta / Georgia): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Rendering Revealed: Workforce housing at 315 N. Pasadena Ave. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Texas Multifamily 2026 Preview: Q&A With Red Oak Capital Holdings’ Nick Jans (Connect CRE Apartments, Dallas / Texas): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- L&G, Taurus Partner on Ground-Up Multifamily Project in Greater Boston (Connect CRE Apartments, National): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Teeple Adding 312-Unit Student Housing Project to Texas A&M Offering (Connect CRE Texas, Dallas / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Top markets for apartment sales in H1 2026 (Multifamily Dive, San Francisco / California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Warner Center's beleaguered Promenade mall bites the dust (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Brokerage Veteran Establishes Independent Firm and Celebrates Inaugural Transaction Raritan Riverside in Raritan New Jersey (Yield PRO, Riverside / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Additional low/unknown rows omitted: 29

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.