# Classification Quality Report

Generated: 2026-11-14 02:55:58

## Classification Summary

- Total articles classified: 77
- Topic distribution: transaction_market: 21; development_pipeline: 16; supply_demand: 9; capital_markets: 8; gp_activity: 7; macro_financing: 6; institutional_capital: 4; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 21 article(s), high 3, medium 10, low 8, unknown 0. Top markets: California (5); Atlanta / Georgia (3); Other / Unknown (2); Riverside / California (2); Los Angeles / California (2).
- development_pipeline: 16 article(s), high 1, medium 9, low 6, unknown 0. Top markets: Other / Unknown (4); California (3); National (2); San Francisco / California (2); Miami / Florida (2).
- supply_demand: 9 article(s), high 1, medium 0, low 8, unknown 0. Top markets: Other / Unknown (3); National (3); San Francisco / California (2); Texas (1).
- capital_markets: 8 article(s), high 4, medium 3, low 1, unknown 0. Top markets: Other / Unknown (3); Southeast (1); National (1); Miami / Florida (1); Denver / Colorado (1).
- gp_activity: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Other / Unknown (4); Los Angeles / California (1); California (1); National (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: California (2); Other / Unknown (2); Miami / Florida (1); Dallas / Texas (1).
- institutional_capital: 4 article(s), high 0, medium 1, low 3, unknown 0. Top markets: Other / Unknown (2); California (1); Atlanta / Georgia (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); Other / Unknown (1); Washington DC (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (2).

## Low Confidence / Unknown Articles

- Northmarq Brokers $4M Sale of 46-Unit Las Flores Apartments in Fresno (Yield PRO, California): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- Fresno Low-Rise Trades to Private Buyer in All-Cash Deal (Connect CRE, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- $39M Construction Takeout Financing Secured for Suburban Milwaukee MF (Connect CRE, Other / Unknown): Institutional activity terms detected: gp_acquisition, gp_disposition. Primary topic set to institutional_capital; confidence low.
- Costco-anchored project adds more housing at 5035 Coliseum St. in Baldwin Hills (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing takes shape at 3455 Slauson Ave. in Hyde Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Work underway for affordable housing at 6144 N. Hazelhurst Pl. in North Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Construction begins for mixed-use project at 11111 Jefferson Blvd. in Culver City (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Construction Topped Out For 641 5th Street, West Sacramento (SF YIMBY, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- JLL Arranges $39.1M in Financing for Apartment Complex in Suburban Milwaukee (REBusiness Online, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- 152 apartments planned at 2315 Marine Ave. in Gardena (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Advanced Real Estate Pays $56 Million for Ontario Multifamily Complex (Connect CRE, Riverside / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- The Mogharebi Group Arranges $56.2M Sale of 253-Unit Inland Empire Apartment Community in Ontario California (Yield PRO, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Rosewood Property Co. Begins Leasing 370-Unit Multifamily Project in Irving (REBusiness Online, Texas): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low. Operator/property management activity detected.
- Marcus & Millichap Arranges $6.6M Sale of 64-Unit Multifamily Portfolio in Saint Paul (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Graffiti Removal Sets Stage for Sale of Oceanwide Plaza (Connect CRE California, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Advanced Real Estate Buys Inland Empire Apartment Complex for $56M (Commercial Observer, Riverside / California): Capital event keywords detected: acquisition. Primary topic set to transaction_market; confidence low.
- 3 multifamily groundbreakings you may have missed (Multifamily Dive, California): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Apartment rents diverge: San Francisco rises, the Sun Belt falls (HousingWire, San Francisco / California): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Related Building 494 Boca Raton Apartment Units (Connect CRE South Florida, Miami / Florida): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Additional low/unknown rows omitted: 25

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.