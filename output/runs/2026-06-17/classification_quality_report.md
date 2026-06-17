# Classification Quality Report

Generated: 2026-06-17 00:18:13

## Classification Summary

- Total articles classified: 76
- Topic distribution: development_pipeline: 15; supply_demand: 14; gp_activity: 12; capital_markets: 9; macro_financing: 7; institutional_capital: 6; transaction_market: 5; other: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 15 article(s), high 2, medium 7, low 6, unknown 0. Top markets: Los Angeles / California (3); California (2); Phoenix / Arizona (2); Other / Unknown (2); Southeast (1).
- supply_demand: 14 article(s), high 1, medium 0, low 13, unknown 0. Top markets: Other / Unknown (7); National (4); Miami / Florida (1); Texas (1); Washington DC (1).
- gp_activity: 12 article(s), high 0, medium 0, low 1, unknown 11. Top markets: Phoenix / Arizona (2); Other / Unknown (2); National (2); Beverly Hills / California (1); Houston / Texas (1).
- capital_markets: 9 article(s), high 4, medium 4, low 1, unknown 0. Top markets: Other / Unknown (2); Miami / Florida (2); California (2); Denver / Colorado (1); Seattle (1).
- macro_financing: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Other / Unknown (4); Los Angeles / California (2); National (1).
- institutional_capital: 6 article(s), high 1, medium 5, low 0, unknown 0. Top markets: Other / Unknown (3); Miami / Florida (1); Washington DC (1); New York City / New York (1).
- transaction_market: 5 article(s), high 1, medium 3, low 1, unknown 0. Top markets: California (2); Phoenix / Arizona (1); Louisiana (1); Dallas / Texas (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Other / Unknown (1); Atlanta / Georgia (1); San Francisco / California (1); Los Angeles / California (1).
- research_data: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Los Angeles / California (2); California (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Developer secures $85m loan for mixed-use project at 55 N. La Cienega Blvd. in Beverly Hills (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- City Planning Commission approves 76 apartments at 2413 N. Silver Lake Boulevard (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: planning_commission. Primary topic set to development_pipeline; confidence low.
- Affordable housing slated for 5139 N. Colfax Ave. in Valley Village (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- World Cup descends on L.A., CicLAvia on June 28, and more (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Big mixed-use project clears a hurdle at 12555 Ventura Blvd. in Studio City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Work to commence next year for affordable housing at 2321 Fairview St. in Burbank (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Opus Development Receives $67M Refinancing for Multifamily Community in Denver (REBusiness Online, Denver / Colorado): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Albuquerque Developers Building 272 Affordable Housing Units (Connect CRE Apartments, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Greystar Eyeing 896 Doral Apartment Units (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Updated Plans For 4095 Pacific Boulevard, San Mateo (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Meeting Tomorrow For 3521 Homestead Road, Santa Clara (SF YIMBY, Atlanta / Georgia): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- 342 Apartment Units Planned Near Big Rivers Waterpark (Connect CRE Apartments, Houston / Texas): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Insignia Pursuing Embassy Row Redevelopment (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Affordable housing takes shape at 711 S. New Hampshire Ave. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Palladium Delivers $65M Fort Worth Affordable Housing Venture (Connect CRE Apartments, Dallas / Texas): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- JLL Arranges $252M Financing for Huntington Beach Seniors Project (Connect CRE Orange County, California): Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- Multifamily Financing In 2026: How Are Projects Moving Ahead? (Bisnow, National): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Additional low/unknown rows omitted: 28

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.