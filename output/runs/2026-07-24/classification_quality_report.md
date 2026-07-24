# Classification Quality Report

Generated: 2026-07-24 00:02:18

## Classification Summary

- Total articles classified: 78
- Topic distribution: development_pipeline: 16; gp_activity: 12; transaction_market: 12; supply_demand: 11; capital_markets: 8; macro_financing: 8; institutional_capital: 7; other: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 16 article(s), high 0, medium 6, low 10, unknown 0. Top markets: Other / Unknown (7); Los Angeles / California (2); Houston / Texas (1); Beverly Hills / California (1); Dallas / Texas (1).
- gp_activity: 12 article(s), high 0, medium 0, low 1, unknown 11. Top markets: Other / Unknown (3); National (2); Los Angeles / California (1); Atlanta / Georgia (1); Phoenix / Arizona (1).
- transaction_market: 12 article(s), high 1, medium 7, low 4, unknown 0. Top markets: California (5); Atlanta / Georgia (2); San Francisco / California (1); Miami / Florida (1); Other / Unknown (1).
- supply_demand: 11 article(s), high 0, medium 0, low 11, unknown 0. Top markets: Other / Unknown (7); National (4).
- capital_markets: 8 article(s), high 5, medium 2, low 1, unknown 0. Top markets: New York City / New York (2); Miami / Florida (2); Phoenix / Arizona (2); Other / Unknown (1); Washington DC (1).
- macro_financing: 8 article(s), high 0, medium 0, low 0, unknown 8. Top markets: Other / Unknown (4); Los Angeles / California (2); California (1); National (1).
- institutional_capital: 7 article(s), high 2, medium 3, low 2, unknown 0. Top markets: Los Angeles / California (3); Dallas / Texas (1); New York City / New York (1); Riverside / California (1); California (1).
- other: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Santa Monica / California (1); California (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Colorado (1); Los Angeles / California (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Beverly Hills upholds approval of Builder's Remedy project at 232 S. Tower Dr. (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Mixed-use building proposed at 305 E. Colorado St. in Glendale (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Kennedy Wilson plans 133 apartments at 700 Colorado Ave. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Workforce housing for Metro employees could rise at 4421 S. Crenshaw Blvd. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Developer nabs financing for affordable housing at 14th & Wilshire in Santa Monica (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Mixed-use project planned at 1134 N. La Brea Ave. in West Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Mixed-use building rises at 450 The Promenade N. in Downtown Long Beach (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- JLL Nabs Listing for 345-Unit Uptown Dallas Apartment Tower (Connect CRE Apartments, Dallas / Texas): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Dallas Apartment Builder Inks $78.7M Refi (Connect CRE Texas, Dallas / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Avalon Bay Planning Apartments, Retail in South Miami (Connect CRE South Florida, Miami / Florida): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- JLL Arranges Sale of 1000 Jefferson a 217-Unit Multifamily Community in One of New Jersey’s Most Resilient Submarkets (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Greystar Receives State Funding Award to Redevelop Taunton’s Whittenton Mills (Connect CRE, Other / Unknown): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Grubb Properties Merges Funds To Create $1.9B Apartment REIT (Bisnow, New York City / New York): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Institutional activity terms detected: reit_activity. Primary topic set to institutional_capital; confidence low.
- 1929-Vintage Los Feliz Apartments Sell to Dream Street Capital (Connect CRE, Los Angeles / California): Capital event keywords detected: disposition. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence medium.
- Bonaventure Breaks Ground on $85.3M Multifamily Development in Norfolk (REBusiness Online, Virginia): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Kidder Mathews Arranges Sale of Mixed-Use Apartments in Wenatchee Washington (Yield PRO, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Fresno Apartments Fetch $44M in First-Ever Sale (Connect CRE California, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low. Operator/property management activity detected.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Additional low/unknown rows omitted: 32

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.