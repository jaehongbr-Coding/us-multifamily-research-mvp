# Classification Quality Report

Generated: 2026-10-21 01:20:24

## Classification Summary

- Total articles classified: 66
- Topic distribution: development_pipeline: 16; supply_demand: 13; capital_markets: 9; transaction_market: 8; gp_activity: 7; institutional_capital: 6; macro_financing: 3; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 16 article(s), high 1, medium 5, low 10, unknown 0. Top markets: Other / Unknown (4); California (2); San Francisco / California (2); National (2); Los Angeles / California (1).
- supply_demand: 13 article(s), high 0, medium 0, low 13, unknown 0. Top markets: Other / Unknown (7); Miami / Florida (2); National (2); California (1); Atlanta / Georgia (1).
- capital_markets: 9 article(s), high 1, medium 5, low 3, unknown 0. Top markets: California (4); Miami / Florida (2); Other / Unknown (1); Southeast (1); Los Angeles / California (1).
- transaction_market: 8 article(s), high 0, medium 6, low 2, unknown 0. Top markets: Atlanta / Georgia (3); Other / Unknown (2); Dallas / Texas (1); California (1); Los Angeles / California (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (3); National (2); Phoenix / Arizona (1); New York City / New York (1).
- institutional_capital: 6 article(s), high 0, medium 2, low 4, unknown 0. Top markets: Other / Unknown (2); Seattle (1); Denver / Colorado (1); National (1); California (1).
- macro_financing: 3 article(s), high 0, medium 0, low 1, unknown 2. Top markets: Other / Unknown (3).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); Other / Unknown (1).
- research_data: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: Other / Unknown (1).

## Low Confidence / Unknown Articles

- 6 Blackstone multifamily properties move to servicing (Multifamily Dive, Seattle): Institutional activity terms detected: private_equity_activity. Primary topic set to institutional_capital; confidence low.
- New supportive housing opens at 8209 Sepulveda Blvd. in the Valley (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- 32 apartments proposed at 806 N. Sweetzer Ave. in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Rendering vs. Reality: 176 apartments at 2225 Sunset Boulevard in Echo Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- PCCP Provides $41M Refinancing for Multifamily Community in San Diego (REBusiness Online, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- PCCP Provides $41M Refi on North Park Multifamily (Connect CRE California, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- 75 apartments planned at 925 Eucalyptus Ave. in Inglewood (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Development Group Starts Work on 371-Unit Boynton Beach Multifamily Venture (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- New Building Permits For 230 Anza Street in Lone Mountain, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Continental Properties Closes $203M Multifamily Fund (Yield PRO, National): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Forbright Bank Provides $50M for Southern California R&D Campus (Commercial Observer, California): Supply/demand terms detected: effective_rent_growth, vacancy, occupancy. Primary topic set to supply_demand; confidence low.
- Multifamily starts fell in September amid high construction costs (Multifamily Dive, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Kennedy Wilson Eyeing School Site for Denver Apartment Community (Connect CRE Apartments, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- NYCHA Cuts Ribbon on $636M Rehab of East Brooklyn Apartments (Connect CRE, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Morgan with Crow Holdings Capital Open 404-Unit Multifamily Community in Tampa Bay Area (Yield PRO, Tampa / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Trammell Crow Breaks Ground On Office-To-Resi Conversion In Dallas: The DFW Deal Sheet (Bisnow, Dallas / Texas): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- High Street Residential, Barings Break Ground in Redwood City (Connect CRE Apartments, California): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Additional low/unknown rows omitted: 26

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.