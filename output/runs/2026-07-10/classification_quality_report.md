# Classification Quality Report

Generated: 2026-07-10 00:06:50

## Classification Summary

- Total articles classified: 84
- Topic distribution: capital_markets: 17; transaction_market: 15; gp_activity: 13; supply_demand: 12; development_pipeline: 10; macro_financing: 6; other: 6; institutional_capital: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- capital_markets: 17 article(s), high 7, medium 8, low 2, unknown 0. Top markets: Other / Unknown (7); New York City / New York (3); Miami / Florida (2); Houston / Texas (1); California (1).
- transaction_market: 15 article(s), high 5, medium 8, low 2, unknown 0. Top markets: Other / Unknown (2); New York (2); Miami / Florida (2); Phoenix / Arizona (2); Los Angeles / California (2).
- gp_activity: 13 article(s), high 0, medium 0, low 1, unknown 12. Top markets: National (3); Atlanta / Georgia (2); Miami / Florida (2); Other / Unknown (2); Los Angeles / California (1).
- supply_demand: 12 article(s), high 1, medium 0, low 11, unknown 0. Top markets: Other / Unknown (8); National (3); Atlanta / Georgia (1).
- development_pipeline: 10 article(s), high 1, medium 6, low 3, unknown 0. Top markets: Other / Unknown (4); Miami / Florida (1); California (1); New York City / New York (1); Houston / Texas (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (3); Houston / Texas (1); California (1); Los Angeles / California (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Los Angeles / California (3); San Francisco / California (1); Other / Unknown (1); New York City / New York (1).
- institutional_capital: 4 article(s), high 0, medium 2, low 2, unknown 0. Top markets: Virginia (1); Riverside / California (1); New York City / New York (1); Other / Unknown (1).
- research_data: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: Santa Monica / California (1).

## Low Confidence / Unknown Articles

- Kennedy Wilson, Jamison partner on 4K affordable units in LA (Multifamily Dive, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Koreatown offices at 3700 Wilshire Blvd. to be converted to housing (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Fresh renderings for mixed-use project at 2716 Ocean Park Blvd. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- NMHC Survey: Builders, Developers Optimistic About Long-Term Multifamily Construction Activity (REBusiness Online, Washington DC): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Avalon Bay Planning Apartments, Retail in South Miami (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- 45-Unit Garden Apartment Property Trades in LA’s Palms Neighborhood (Connect CRE California, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Berkadia Arranges Sale and Financing of 270-Unit Multifamily Community in Manassas Virginia (Yield PRO, Virginia): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Wood framing rises for mixed-use building at 9431 Venice Blvd. in Palms (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Nashville Developer Eyes Former Dance Club Site for Apartment Tower (Connect CRE Apartments, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Dezer Advancing Plan for 600 N. Miami Apartment Units (Connect CRE South Florida, Miami / Florida): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- The Sunbelt and Multifamily: Oversupply Isn’t the Whole Story (Connect CRE, Atlanta / Georgia): Supply/demand terms detected: supply_pressure, oversupply. Primary topic set to supply_demand; confidence low.
- Structural columns buckle on 21st floor of Manhattan adaptive reuse project (Multifamily Dive, New York City / New York): Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Grubb Nabs $377M FiDi Construction Loan: The N.Y. Deal Sheet (Bisnow, New York City / New York): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: construction_financing. Financing type keywords detected: construction_loan. Primary topic set to capital_markets; confidence low.
- Texas apartment owners face uphill battles (Multifamily Dive, Houston / Texas): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Work trudges along for Pico Pico Library in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Additional low/unknown rows omitted: 26

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.