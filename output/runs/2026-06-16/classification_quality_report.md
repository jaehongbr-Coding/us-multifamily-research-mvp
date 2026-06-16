# Classification Quality Report

Generated: 2026-06-16 01:43:20

## Classification Summary

- Total articles classified: 82
- Topic distribution: supply_demand: 13; transaction_market: 13; capital_markets: 12; gp_activity: 12; development_pipeline: 11; macro_financing: 6; institutional_capital: 5; other: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- supply_demand: 13 article(s), high 1, medium 0, low 12, unknown 0. Top markets: Other / Unknown (7); National (3); Miami / Florida (1); Texas (1); Washington DC (1).
- transaction_market: 13 article(s), high 4, medium 5, low 4, unknown 0. Top markets: Phoenix / Arizona (2); National (2); Washington DC (2); Dallas / Texas (2); Houston / Texas (1).
- capital_markets: 12 article(s), high 7, medium 4, low 1, unknown 0. Top markets: Miami / Florida (3); New York (2); Other / Unknown (2); California (2); Los Angeles / California (1).
- gp_activity: 12 article(s), high 0, medium 0, low 1, unknown 11. Top markets: California (2); Other / Unknown (2); Dallas / Texas (2); National (2); Florida (1).
- development_pipeline: 11 article(s), high 2, medium 3, low 6, unknown 0. Top markets: Other / Unknown (3); Los Angeles / California (3); Phoenix / Arizona (2); California (1); Seattle (1).
- macro_financing: 6 article(s), high 0, medium 0, low 1, unknown 5. Top markets: Other / Unknown (4); Los Angeles / California (2).
- institutional_capital: 5 article(s), high 0, medium 5, low 0, unknown 0. Top markets: Other / Unknown (2); Miami / Florida (1); Connecticut (1); Atlanta / Georgia (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (2); Other / Unknown (1); San Francisco / California (1); Washington DC (1).
- research_data: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (3); California (1); Other / Unknown (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- World Cup descends on L.A., CicLAvia on June 28, and more (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Big mixed-use project clears a hurdle at 12555 Ventura Blvd. in Studio City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Work to commence next year for affordable housing at 2321 Fairview St. in Burbank (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Wrapping off for affordable housing at 714 S. Grand View Street in Westlake (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 230 apartments unwrapped at 640 S. St. Andrews Pl. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- 77-unit affordable housing complex proposed at 8811 Reading Ave. in Westchester (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Apartments Along Burton Way Trade for $603K Per Unit (Connect CRE California, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Greystar Eyeing 896 Doral Apartment Units (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: effective_rent_growth. Primary topic set to supply_demand; confidence low.
- Downtown Chicago Apartment Conversion Project Begins Pre-Leasing (Connect CRE Apartments, Other / Unknown): Development-stage terms detected: delivery, adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Updated Plans For 4095 Pacific Boulevard, San Mateo (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Formal Application For 926 Natoma Street in SoMa, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Woodfield Development Begins Construction on Luxury Multifamily Community Connerton Apartments in Land O’ Lakes Florida (Yield PRO, Florida): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Marysville Breaks Ground on Affordable Housing Development (Connect CRE Apartments, Seattle): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Insignia Pursuing Embassy Row Redevelopment (Connect CRE Atlanta, Atlanta / Georgia): Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Affordable housing takes shape at 711 S. New Hampshire Ave. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- JLL Arranges $252M Financing for Huntington Beach Seniors Project (Connect CRE Orange County, California): Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- How Safehold’s Ground Lease is Unlocking Multifamily Development (Commercial Observer, California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 31

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.