# Classification Quality Report

Generated: 2026-07-30 00:00:43

## Classification Summary

- Total articles classified: 84
- Topic distribution: transaction_market: 19; supply_demand: 13; capital_markets: 11; gp_activity: 11; development_pipeline: 10; institutional_capital: 8; macro_financing: 5; other: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 19 article(s), high 2, medium 9, low 8, unknown 0. Top markets: California (8); Other / Unknown (2); Atlanta / Georgia (2); New York City / New York (1); Santa Monica / California (1).
- supply_demand: 13 article(s), high 0, medium 0, low 13, unknown 0. Top markets: Other / Unknown (9); National (4).
- capital_markets: 11 article(s), high 3, medium 7, low 1, unknown 0. Top markets: Miami / Florida (6); Phoenix / Arizona (2); Other / Unknown (1); Atlanta / Georgia (1); Colorado (1).
- gp_activity: 11 article(s), high 0, medium 0, low 0, unknown 11. Top markets: Los Angeles / California (2); National (2); Texas (1); Florida (1); Atlanta / Georgia (1).
- development_pipeline: 10 article(s), high 0, medium 5, low 5, unknown 0. Top markets: Los Angeles / California (3); Other / Unknown (3); Atlanta / Georgia (1); Miami / Florida (1); Beverly Hills / California (1).
- institutional_capital: 8 article(s), high 0, medium 4, low 4, unknown 0. Top markets: Other / Unknown (2); Riverside / California (2); Atlanta / Georgia (2); New York City / New York (1); California (1).
- macro_financing: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (4); Miami / Florida (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Southeast (1); Other / Unknown (1); New York City / New York (1); Los Angeles / California (1); San Francisco / California (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (2).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Developer pivots to affordable housing at 7715 Crenshaw Blvd. in Hyde Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Affordable housing takes shape at 4706 Centinela Ave. in Del Rey (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Mixed-use building slated for 20160 Roscoe Blvd. in Winnetka (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 93 apartments approved for 8465 Glenoaks Ave. in Sun Valley (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- StreetLights Residential Underway on 22-Story Apartment Building in Plano (REBusiness Online, Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Sares Regis Trades South San Francisco Multifamily to Bell Partners (Connect CRE California, San Francisco / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Harrison Street Divests Oxnard Independent Living Property (Connect CRE California, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Legacy Lakefront Apartment Community Trades for First Time in Three Decades in Minnesota (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Checking in on Alexan West End at 600 Broadway in Long Beach (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Foundation Work Underway For 2016 Ashby Avenue, South Berkeley (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Marcus & Millichap Capital Corporation Arranges $16M for Green Bay MF Construction (Connect CRE Apartments, Miami / Florida): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- NY Investor Snags First Folsom Apartments on Market in Four Years (Connect CRE Apartments, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Capstone Begins Construction on 270-Unit Gateway Apartments in Orlando (REBusiness Online, Florida): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Richman Group, Monadnock Plan to Build 420 Units in East Harlem (Commercial Observer, New York City / New York): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Radnor, Madrone to Break Ground on 793-Bed Student Housing Development in Atlanta (REBusiness Online, Atlanta / Georgia): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Marcus & Millichap Facilitate Sale of a 41-Unit Orange County Multifamily Property (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- PCCP Provides $51.8M Refi of Gilbert 236-Unit Multifamily Community (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- Additional low/unknown rows omitted: 34

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.