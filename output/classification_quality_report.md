# Classification Quality Report

Generated: 2026-07-28 23:59:43

## Classification Summary

- Total articles classified: 86
- Topic distribution: transaction_market: 20; development_pipeline: 17; supply_demand: 13; capital_markets: 10; gp_activity: 7; institutional_capital: 6; macro_financing: 6; other: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 20 article(s), high 2, medium 9, low 9, unknown 0. Top markets: California (6); Other / Unknown (3); Atlanta / Georgia (2); San Francisco / California (1); Southeast (1).
- development_pipeline: 17 article(s), high 2, medium 6, low 9, unknown 0. Top markets: Los Angeles / California (5); Other / Unknown (4); New York City / New York (2); Texas (1); Phoenix / Arizona (1).
- supply_demand: 13 article(s), high 0, medium 0, low 13, unknown 0. Top markets: Other / Unknown (8); National (4); Austin / Texas (1).
- capital_markets: 10 article(s), high 3, medium 6, low 1, unknown 0. Top markets: Miami / Florida (4); Phoenix / Arizona (2); New York City / New York (1); Florida (1); Atlanta / Georgia (1).
- gp_activity: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Other / Unknown (2); National (2); Atlanta / Georgia (1); Phoenix / Arizona (1); Miami / Florida (1).
- institutional_capital: 6 article(s), high 0, medium 4, low 2, unknown 0. Top markets: Riverside / California (2); Other / Unknown (1); Georgia (1); Atlanta / Georgia (1); California (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (4); Miami / Florida (1); Santa Monica / California (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (2); Southeast (1); Los Angeles / California (1); San Francisco / California (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (2).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Sky Equity Goes Vertical on Tribeca Condos (Connect CRE, New York City / New York): Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Marcus & Millichap Capital Corporation Arranges $16M for Green Bay MF Construction (Connect CRE, Miami / Florida): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Sares Regis Trades South San Francisco Multifamily to Bell Partners (Connect CRE, San Francisco / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Mixed-use building slated for 20160 Roscoe Blvd. in Winnetka (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 93 apartments approved for 8465 Glenoaks Ave. in Sun Valley (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Graffiti tower cleanup begins, Homeless population grows, and more (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- City Planning Commission signs off on mixed-use project at 2800 W. Jefferson Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: planning_commission. Primary topic set to development_pipeline; confidence low.
- More affordable housing underway at 21300 W. Oxnard St. in Warner Center (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Harrison Street Divests Oxnard Independent Living Property (Connect CRE California, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Logos Faith Development Sets 15 Groundbreakings Over the Next Three Years (Connect CRE California, Los Angeles / California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Legacy Lakefront Apartment Community Trades for First Time in Three Decades in Minnesota (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Checking in on Alexan West End at 600 Broadway in Long Beach (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Foundation Work Underway For 2016 Ashby Avenue, South Berkeley (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Rockspring Underway on 254-Acre Mixed-Use Development in Marble Falls, Texas (REBusiness Online, Austin / Texas): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Marcus & Millichap Facilitate Sale of a 41-Unit Orange County Multifamily Property (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- PCCP Provides $51.8M Refi of Gilbert 236-Unit Multifamily Community (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project (Connect CRE Atlanta, Atlanta / Georgia): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 34

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.