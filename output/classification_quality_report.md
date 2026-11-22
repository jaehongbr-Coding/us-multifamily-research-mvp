# Classification Quality Report

Generated: 2026-11-22 02:51:07

## Classification Summary

- Total articles classified: 64
- Topic distribution: transaction_market: 16; development_pipeline: 13; supply_demand: 8; gp_activity: 7; institutional_capital: 6; other: 6; macro_financing: 4; capital_markets: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 16 article(s), high 2, medium 8, low 6, unknown 0. Top markets: Other / Unknown (3); Atlanta / Georgia (3); Dallas / Texas (2); California (2); Miami / Florida (2).
- development_pipeline: 13 article(s), high 1, medium 6, low 6, unknown 0. Top markets: Other / Unknown (7); Los Angeles / California (1); Atlanta / Georgia (1); National (1); New York City / New York (1).
- supply_demand: 8 article(s), high 0, medium 0, low 8, unknown 0. Top markets: National (4); Other / Unknown (3); Houston / Texas (1).
- gp_activity: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Other / Unknown (4); Los Angeles / California (1); California (1); National (1).
- institutional_capital: 6 article(s), high 2, medium 2, low 2, unknown 0. Top markets: California (2); National (1); Virginia (1); Miami / Florida (1); Atlanta / Georgia (1).
- other: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (2); Los Angeles (1); Austin / Texas (1); San Francisco / California (1); Los Angeles / California (1).
- macro_financing: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (2); Los Angeles / California (1); California (1).
- capital_markets: 2 article(s), high 0, medium 2, low 0, unknown 0. Top markets: Miami / Florida (2).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); Southeast (1).

## Low Confidence / Unknown Articles

- CBRE Arranges Two Property 540-Unit Multifamily Portfolio Sale in Des Moines Suburb (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Hudson County Luxury Multifamily Trades for $46M (Connect CRE, New York): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Mixed-use project reaches its peak at at 6052 W. Olympic Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Developers seek bond financing for affordable housing in the Valley (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- City Council upholds approval of apartments at 2413 Silver Lake Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Mixed-use project starts to rise at 3313 Sunset Blvd. in Silver Lake (Urbanize LA, Southeast): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 269 homes to replace nursery at 7639 Topanga Canyon Blvd. in Canoga Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- New plan for housing at 452 N. Los Robles Ave. in Pasadena (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Multifamily housing unwrapped at 4429 S. Vermont Ave. in South L.A. (Urbanize LA, Los Angeles): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Fresh renderings for infill housing at 511 S. Oak Knoll Ave. in Pasadena (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Inland, Reuter Walton Break Ground on 342-Unit Citywalk Apartments in Rochester, Minnesota (REBusiness Online, National): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- How apartment developers can successfully install connected services (Multifamily Dive, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Work Gets Started on Carlsbad Village Mixed-Use Project (Connect CRE, California): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- Multifamily starts rose in October amid high borrowing, materials costs (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Plans Take Shape for Mixed-Use Project Next to the Hillsdale Caltrain Station (Connect CRE California, California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Marcus & Millichap Capital Corporation Arranges $8.5 Million Financing for Multifamily Property in San Diego County (Yield PRO, California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Construction Underway At 2138 Kittredge Street, Downtown Berkeley (SF YIMBY, Austin / Texas): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Developers Secure Approval for 55-Story Miami Waterfront Multifamily Tower (Yield PRO, Miami / Florida): Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 21

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.