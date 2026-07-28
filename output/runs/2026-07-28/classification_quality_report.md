# Classification Quality Report

Generated: 2026-07-28 00:04:12

## Classification Summary

- Total articles classified: 82
- Topic distribution: development_pipeline: 16; transaction_market: 14; capital_markets: 11; gp_activity: 11; supply_demand: 11; institutional_capital: 7; macro_financing: 7; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 16 article(s), high 0, medium 5, low 11, unknown 0. Top markets: Los Angeles / California (6); Other / Unknown (3); Beverly Hills / California (2); Atlanta / Georgia (1); Colorado (1).
- transaction_market: 14 article(s), high 2, medium 8, low 4, unknown 0. Top markets: California (5); Houston / Texas (2); Atlanta / Georgia (2); Other / Unknown (2); Washington DC (1).
- capital_markets: 11 article(s), high 4, medium 6, low 1, unknown 0. Top markets: Miami / Florida (5); Phoenix / Arizona (3); Georgia (1); New York (1); Atlanta / Georgia (1).
- gp_activity: 11 article(s), high 0, medium 0, low 2, unknown 9. Top markets: Other / Unknown (3); New York City / New York (2); National (2); Atlanta / Georgia (1); Phoenix / Arizona (1).
- supply_demand: 11 article(s), high 0, medium 0, low 11, unknown 0. Top markets: Other / Unknown (8); National (3).
- institutional_capital: 7 article(s), high 1, medium 3, low 3, unknown 0. Top markets: Riverside / California (2); Other / Unknown (1); Dallas / Texas (1); Atlanta / Georgia (1); California (1).
- macro_financing: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (4); Santa Monica / California (1); National (1); Los Angeles / California (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Other / Unknown (2); Los Angeles / California (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); Colorado (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- 93 apartments approved for 8465 Glenoaks Ave. in Sun Valley (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Graffiti tower cleanup begins, Homeless population grows, and more (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- City Planning Commission signs off on mixed-use project at 2800 W. Jefferson Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: planning_commission. Primary topic set to development_pipeline; confidence low.
- More affordable housing underway at 21300 W. Oxnard St. in Warner Center (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Beverly Hills upholds approval of Builder's Remedy project at 232 S. Tower Dr. (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Mixed-use building proposed at 305 E. Colorado St. in Glendale (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Logos Faith Development Sets 15 Groundbreakings Over the Next Three Years (Connect CRE Apartments, Los Angeles / California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- JLL Nabs Listing for 345-Unit Uptown Dallas Apartment Tower (Connect CRE Texas, Dallas / Texas): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- 1929-Vintage Los Feliz Apartments Sell to Dream Street Capital (Connect CRE California, Los Angeles / California): Capital event keywords detected: disposition. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence medium.
- Legacy Lakefront Apartment Community Trades for First Time in Three Decades in Minnesota (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Foundation Work Underway For 2016 Ashby Avenue, South Berkeley (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Livmark Communities Breaks Ground on 457-Unit Multifamily Project in Fort Collins, Colorado (REBusiness Online, Colorado): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Marcus & Millichap Facilitate Sale of a 41-Unit Orange County Multifamily Property (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- PCCP Provides $51.8M Refi of Gilbert 236-Unit Multifamily Community (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Marcus & Millichap Releases Indianapolis Multifamily Report for Q2 2026 (Yield PRO, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Woodfield Development Breaks Ground on $100M Apartment Community in Cary, North Carolina (REBusiness Online, Sun Belt): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 33

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.