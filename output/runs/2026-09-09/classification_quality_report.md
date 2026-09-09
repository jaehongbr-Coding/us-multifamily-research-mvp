# Classification Quality Report

Generated: 2026-09-09 01:04:59

## Classification Summary

- Total articles classified: 84
- Topic distribution: development_pipeline: 22; transaction_market: 16; capital_markets: 12; gp_activity: 9; supply_demand: 9; macro_financing: 7; research_data: 4; institutional_capital: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 22 article(s), high 2, medium 6, low 14, unknown 0. Top markets: Other / Unknown (9); Atlanta / Georgia (3); Phoenix / Arizona (2); San Francisco / California (1); Arizona (1).
- transaction_market: 16 article(s), high 4, medium 7, low 5, unknown 0. Top markets: California (2); Santa Monica / California (2); Atlanta / Georgia (2); Los Angeles / California (1); Phoenix / Arizona (1).
- capital_markets: 12 article(s), high 4, medium 8, low 0, unknown 0. Top markets: Miami / Florida (3); National (2); Austin / Texas (2); California (1); Los Angeles / California (1).
- gp_activity: 9 article(s), high 0, medium 0, low 0, unknown 9. Top markets: Other / Unknown (3); Dallas / Texas (2); Atlanta / Georgia (1); Phoenix / Arizona (1); Miami / Florida (1).
- supply_demand: 9 article(s), high 0, medium 0, low 9, unknown 0. Top markets: Other / Unknown (5); National (4).
- macro_financing: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Los Angeles / California (2); Other / Unknown (2); California (1); New York City / New York (1); Atlanta / Georgia (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (2); Los Angeles / California (1); California (1).
- institutional_capital: 3 article(s), high 1, medium 1, low 1, unknown 0. Top markets: Other / Unknown (1); California (1); National (1).
- other: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: California (1); National (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Mixed-use building starts to rise at 8025 Santa Monica Blvd. in West Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Construction begins for affordable housing at former MacLaren Hall site in El Monte (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Sunset Boulevard bus lanes, Kroenke buys Angels, and more (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- Mixed-use project rises at 1801 E. 4th St. in Santa Ana (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Rendering vs. Reality: Apartments at 1408 W. Jefferson Blvd. in Exposition Park (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Building Permits Issued For West Oakland BART Affordable Housing (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- New Building Permits Filed In Balboa Reservoir Masterplan, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Pre-Application Filed For 1100 Los Gamos Drive, San Rafael (SF YIMBY, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Miami-Dade Public Agency Advancing $126.4M Affordable Housing Project (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Mixed-use project to rise at 225 N. 2nd Ave. in Arcadia (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- What multifamily firms bought and sold this summer (Multifamily Dive, Riverside / California): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- GAIA Lands One-Year Extension on Williamsburg Multifamily Loan (Connect CRE, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Kennedy Wilson, Shimizu Corp. partner on $139M multifamily build in Georgia (Multifamily Dive, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Fair housing construction accessibility complaints now have a deadline, HUD says (Multifamily Dive, National): Supply/demand terms detected: effective_rent_growth, occupancy. Primary topic set to supply_demand; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 31

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.