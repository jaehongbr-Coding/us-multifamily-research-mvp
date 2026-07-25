# Classification Quality Report

Generated: 2026-07-25 00:04:56

## Classification Summary

- Total articles classified: 86
- Topic distribution: development_pipeline: 17; transaction_market: 17; gp_activity: 12; supply_demand: 12; capital_markets: 11; institutional_capital: 7; macro_financing: 7; research_data: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 17 article(s), high 0, medium 7, low 10, unknown 0. Top markets: Other / Unknown (6); Los Angeles / California (4); New York City / New York (2); Houston / Texas (1); Beverly Hills / California (1).
- transaction_market: 17 article(s), high 4, medium 7, low 6, unknown 0. Top markets: California (5); Other / Unknown (4); Atlanta / Georgia (2); Los Angeles / California (1); Miami / Florida (1).
- gp_activity: 12 article(s), high 0, medium 0, low 1, unknown 11. Top markets: Other / Unknown (3); National (2); New York City / New York (1); Los Angeles / California (1); Atlanta / Georgia (1).
- supply_demand: 12 article(s), high 0, medium 0, low 12, unknown 0. Top markets: Other / Unknown (8); National (4).
- capital_markets: 11 article(s), high 6, medium 4, low 1, unknown 0. Top markets: Miami / Florida (2); Phoenix / Arizona (2); California (1); Other / Unknown (1); New York (1).
- institutional_capital: 7 article(s), high 2, medium 4, low 1, unknown 0. Top markets: Dallas / Texas (1); Other / Unknown (1); Riverside / California (1); National (1); Salt Lake City / Utah (1).
- macro_financing: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (4); Los Angeles / California (2); National (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); Colorado (1).
- other: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: Santa Monica / California (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Marcus & Millichap Brokers Sale of 132-Unit Multifamily Property in the Miracle Mile Neighborhood of Los Angeles (Yield PRO, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Carlyle Group, Haussmann Submit Plans for 99 Units at Brooklyn’s 566 Grand Avenue (Commercial Observer, New York City / New York): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Logos Faith Development Sets 15 Groundbreakings Over the Next Three Years (Connect CRE, Los Angeles / California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- City Planning Commission signs off on mixed-use project at 2800 W. Jefferson Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: planning_commission. Primary topic set to development_pipeline; confidence low.
- More affordable housing underway at 21300 W. Oxnard St. in Warner Center (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Beverly Hills upholds approval of Builder's Remedy project at 232 S. Tower Dr. (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Mixed-use building proposed at 305 E. Colorado St. in Glendale (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Kennedy Wilson plans 133 apartments at 700 Colorado Ave. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Workforce housing for Metro employees could rise at 4421 S. Crenshaw Blvd. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Developer nabs financing for affordable housing at 14th & Wilshire in Santa Monica (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- JLL Nabs Listing for 345-Unit Uptown Dallas Apartment Tower (Connect CRE Texas, Dallas / Texas): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Avalon Bay Planning Apartments, Retail in South Miami (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- 1929-Vintage Los Feliz Apartments Sell to Dream Street Capital (Connect CRE California, Los Angeles / California): Capital event keywords detected: disposition. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence medium.
- Legacy Lakefront Apartment Community Trades for First Time in Three Decades in Minnesota (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Monday Properties Receives Approval for Mixed-Use Development in Arlington, Virginia (REBusiness Online, Virginia): Development-stage terms detected: entitlement, redevelopment. Primary topic set to development_pipeline; confidence low.
- PCCP Provides $51.8M Refi of Gilbert 236-Unit Multifamily Community (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 32

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.