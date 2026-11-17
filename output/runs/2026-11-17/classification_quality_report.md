# Classification Quality Report

Generated: 2026-11-17 04:58:34

## Classification Summary

- Total articles classified: 72
- Topic distribution: development_pipeline: 16; transaction_market: 13; capital_markets: 10; supply_demand: 8; gp_activity: 7; macro_financing: 7; institutional_capital: 5; other: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 16 article(s), high 2, medium 9, low 5, unknown 0. Top markets: Other / Unknown (7); California (2); Phoenix / Arizona (2); Miami / Florida (2); San Francisco / California (1).
- transaction_market: 13 article(s), high 2, medium 4, low 7, unknown 0. Top markets: Atlanta / Georgia (3); Other / Unknown (2); California (2); Riverside / California (1); Seattle (1).
- capital_markets: 10 article(s), high 4, medium 4, low 2, unknown 0. Top markets: Other / Unknown (3); Phoenix / Arizona (2); New York City / New York (2); Miami / Florida (2); National (1).
- supply_demand: 8 article(s), high 2, medium 0, low 6, unknown 0. Top markets: Other / Unknown (3); National (3); Austin / Texas (1); San Francisco / California (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (3); New York City / New York (2); Austin / Texas (1); National (1).
- macro_financing: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (2); Los Angeles / California (1); Texas (1); Miami / Florida (1); New York City / New York (1).
- institutional_capital: 5 article(s), high 0, medium 3, low 2, unknown 0. Top markets: National (1); California (1); Miami / Florida (1); Other / Unknown (1); Atlanta / Georgia (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (3); Other / Unknown (1); Houston / Texas (1).
- research_data: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: Los Angeles / California (1).

## Low Confidence / Unknown Articles

- Affordable housing takes shape at 3985 S. Meier St. in Mar Vista (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Costco-anchored project adds more housing at 5035 Coliseum St. in Baldwin Hills (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Construction Topped Out For 641 5th Street, West Sacramento (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Natixis Provides $233.3M Loan for Refinancing of Manhattan Apartment Building (REBusiness Online, New York City / New York): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- CBRE Arranges Sale of 540-Unit Ohio Multifamily Portfolio (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Advanced Real Estate Pays $56 Million for Ontario Multifamily Complex (Connect CRE California, Riverside / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Fresno Low-Rise Trades to Private Buyer in All-Cash Deal (Connect CRE California, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- 152 apartments planned at 2315 Marine Ave. in Gardena (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 'Graffiti towers' no more: Oceanwide Plaza is officially cleaned up (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Off-Market Apartment Sale in Seattle Comes In at $298K/Unit (Connect CRE Apartments, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Graffiti Removal Sets Stage for Sale of Oceanwide Plaza (Connect CRE California, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Villa hires former Century Communities CFO Messenger as CEO (HousingWire, San Francisco / California): Development-stage terms detected: delivery, permit. Primary topic set to development_pipeline; confidence low.
- IPA Arranges $40.3M in Financing for North San Antonio Apartment Community (REBusiness Online, Texas): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Related Building 494 Boca Raton Apartment Units (Connect CRE South Florida, Miami / Florida): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Taylor Morrison to Start Work on 161-Unit Austin BTR Community (Connect CRE Apartments, Austin / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Moody National Tops Out On Apartment Complex At Historic Silo Development (Bisnow, Houston / Texas): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 22

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.