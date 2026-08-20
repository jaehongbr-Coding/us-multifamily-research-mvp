# Classification Quality Report

Generated: 2026-08-20 23:25:37

## Classification Summary

- Total articles classified: 86
- Topic distribution: transaction_market: 18; development_pipeline: 13; institutional_capital: 12; supply_demand: 12; gp_activity: 9; macro_financing: 7; capital_markets: 6; other: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 18 article(s), high 7, medium 8, low 3, unknown 0. Top markets: Other / Unknown (4); San Francisco / California (2); New York City / New York (2); California (2); Colorado (1).
- development_pipeline: 13 article(s), high 0, medium 6, low 7, unknown 0. Top markets: Other / Unknown (4); Los Angeles / California (2); Atlanta / Georgia (2); Florida (1); New York (1).
- institutional_capital: 12 article(s), high 3, medium 5, low 4, unknown 0. Top markets: New York (3); Dallas / Texas (2); California (2); Phoenix / Arizona (1); Other / Unknown (1).
- supply_demand: 12 article(s), high 0, medium 0, low 12, unknown 0. Top markets: Other / Unknown (7); National (4); Atlanta / Georgia (1).
- gp_activity: 9 article(s), high 0, medium 0, low 1, unknown 8. Top markets: Miami / Florida (3); National (2); California (1); Los Angeles / California (1); Other / Unknown (1).
- macro_financing: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Los Angeles / California (3); Other / Unknown (2); Atlanta / Georgia (1); California (1).
- capital_markets: 6 article(s), high 2, medium 4, low 0, unknown 0. Top markets: New York City / New York (2); Phoenix / Arizona (2); Kentucky (1); Atlanta / Georgia (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (3); Beverly Hills / California (1); San Francisco / California (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); California (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- CBRE Arranges Sale of Boutique Bergen County Apartments (Connect CRE, New York): Capital event keywords detected: joint_venture, disposition. Primary topic set to institutional_capital; confidence low.
- 338-unit affordable housing development underway in Tustin (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing takes shape at 17100 Victory Blvd. in Lake Balboa (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- 39 apartments approved at 10535 W. Missouri Ave. in West L.A. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Senior affordable housing rising at 19300 Sherman Way in Reseda (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Affordable housing project moves forward at 3401 Cerritos Ave. in Long Beach (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Developer Eyeing 143-Acre “Italian Village” in Prosper (Connect CRE Texas, Dallas / Texas): Institutional activity terms detected: private_equity_activity. Primary topic set to institutional_capital; confidence low.
- Mixed-use complex unwrapped at 7050 Van Nuys Blvd. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Multifamily starts tumbled in July (Multifamily Dive, National): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Interra Realty Brokers Edgewater Apartment Transaction (Connect CRE, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Core Spaces Breaks Ground on 2,201-Bed Student Housing Project Near Texas A&M University (REBusiness Online, Texas): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Marcus & Millichap Arranges Sale of Multifamily Apartment Property in Greenville South Carolina Suburb (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- L.A. County Investment Sales Jump 28% in July Thanks to Multifamily (Commercial Observer, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Atlanta Beltline Advancing 218-Unit Affordable Apartment Project (Connect CRE Atlanta, Atlanta / Georgia): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Revised look emerges for resi tower at 8844 Burton Way in Beverly Hills (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Michaels Organization Set to Break Ground in Davis (Connect CRE Apartments, California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- PCCP, RPM Pick Up 358-Unit Arlington Multifamily Community (Connect CRE Texas, Dallas / Texas): Capital event keywords detected: joint_venture, acquisition. Primary topic set to institutional_capital; confidence low.
- Additional low/unknown rows omitted: 31

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.