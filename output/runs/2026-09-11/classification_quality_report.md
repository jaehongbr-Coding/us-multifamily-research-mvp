# Classification Quality Report

Generated: 2026-09-11 00:51:21

## Classification Summary

- Total articles classified: 79
- Topic distribution: transaction_market: 16; capital_markets: 14; development_pipeline: 14; supply_demand: 10; gp_activity: 9; macro_financing: 6; other: 4; institutional_capital: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 16 article(s), high 4, medium 8, low 4, unknown 0. Top markets: California (3); New York City / New York (2); Other / Unknown (2); Los Angeles / California (2); Atlanta / Georgia (2).
- capital_markets: 14 article(s), high 5, medium 5, low 4, unknown 0. Top markets: Miami / Florida (5); Other / Unknown (4); New York City / New York (1); Southeast (1); Seattle (1).
- development_pipeline: 14 article(s), high 1, medium 5, low 8, unknown 0. Top markets: Other / Unknown (7); Texas (2); Atlanta / Georgia (2); New York (1); Colorado (1).
- supply_demand: 10 article(s), high 0, medium 0, low 10, unknown 0. Top markets: Other / Unknown (5); National (4); Los Angeles / California (1).
- gp_activity: 9 article(s), high 0, medium 0, low 1, unknown 8. Top markets: Other / Unknown (5); National (2); Phoenix / Arizona (1); Miami / Florida (1).
- macro_financing: 6 article(s), high 0, medium 0, low 2, unknown 4. Top markets: Other / Unknown (2); Los Angeles / California (1); Dallas / Texas (1); California (1); Atlanta / Georgia (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Santa Monica / California (1); Other / Unknown (1).
- institutional_capital: 3 article(s), high 0, medium 2, low 1, unknown 0. Top markets: Other / Unknown (1); Atlanta / Georgia (1); Sun Belt (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); Other / Unknown (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Former Sunkist HQ to become 95 apartments (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Housing unwrapped at 11261 Santa Monica Boulevard (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Mixed-use building starts to rise at 8025 Santa Monica Blvd. in West Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Construction begins for affordable housing at former MacLaren Hall site in El Monte (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Dominium to Build 350 Affordable BTR Units in Terrell (Connect CRE Texas, Dallas / Texas): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Infill housing coming to 1030 N. Sierra Bonita Ave. in West Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Draper and Kramer Arranges $93.5M Refinancing for Chicago Multifamily Property (REBusiness Online, Other / Unknown): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Mixed-use project to rise at 225 N. 2nd Ave. in Arcadia (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Zoning Adjustment Board Meeting Tomorrow For 2955 Shattuck Avenue, Berkeley (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: zoning. Primary topic set to development_pipeline; confidence low.
- Colliers Team Closes Sale of 107-Unit Central Valley Apartments (Connect CRE California, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Meeting Tonight for Amoeba Apartments in Southside, Berkeley (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- TSB Capital Arranges Refinancing for 448-Bed Student Housing Community Near Northern Arizona University (REBusiness Online, Arizona): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Fair housing construction accessibility complaints now have a deadline, HUD says (Multifamily Dive, National): Supply/demand terms detected: effective_rent_growth, occupancy. Primary topic set to supply_demand; confidence low.
- Marcus & Millichap Arranges $5.4M Sale and $3.8M Financing of 20-Unit Multifamily Property in Los Angeles (Yield PRO, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 29

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.