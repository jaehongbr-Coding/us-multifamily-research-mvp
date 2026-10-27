# Classification Quality Report

Generated: 2026-10-27 01:51:04

## Classification Summary

- Total articles classified: 81
- Topic distribution: development_pipeline: 19; transaction_market: 17; supply_demand: 10; capital_markets: 9; macro_financing: 8; gp_activity: 7; institutional_capital: 5; other: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 19 article(s), high 0, medium 6, low 13, unknown 0. Top markets: Other / Unknown (6); California (6); Los Angeles / California (3); New York (1); Atlanta / Georgia (1).
- transaction_market: 17 article(s), high 2, medium 10, low 5, unknown 0. Top markets: Atlanta / Georgia (5); Other / Unknown (3); New York City / New York (2); Austin / Texas (2); California (2).
- supply_demand: 10 article(s), high 0, medium 0, low 10, unknown 0. Top markets: Other / Unknown (6); National (2); Miami / Florida (1); California (1).
- capital_markets: 9 article(s), high 1, medium 6, low 2, unknown 0. Top markets: Los Angeles / California (2); Miami / Florida (2); Other / Unknown (1); Washington DC (1); Tennessee (1).
- macro_financing: 8 article(s), high 0, medium 0, low 1, unknown 7. Top markets: Other / Unknown (2); Austin / Texas (1); Los Angeles / California (1); Colorado (1); California (1).
- gp_activity: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (3); National (2); Phoenix / Arizona (1); Virginia (1).
- institutional_capital: 5 article(s), high 1, medium 1, low 3, unknown 0. Top markets: Other / Unknown (2); Seattle (1); California (1); Atlanta / Georgia (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (3); Other / Unknown (1); Texas (1).
- research_data: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: Los Angeles / California (1).

## Low Confidence / Unknown Articles

- 6 Blackstone multifamily properties move to servicing (Multifamily Dive, Seattle): Institutional activity terms detected: private_equity_activity. Primary topic set to institutional_capital; confidence low.
- Marcus & Millichap Arranges $7.35M Sale of 36-Unit Multifamily Property in Los Angeles (Yield PRO, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Northmarq Closes Sale of 312-Unit Multifamily Community in Clarksville Indiana (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- JLL Capital Markets Arranges Sale and Financing of 341-Unit Luxury High-Rise in Austin (Yield PRO, Austin / Texas): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- New look for proposed apartment complex at 5600 Hollywood Blvd. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Bjarke Ingels-designed project in the works at 2810 N. Hyperion Ave. in Silver Lake (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Alveare affordable housing topped out at 1405 S. Broadway in DTLA (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Mixed-use project completed at Sunset and Fairfax in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- City Council upholds approval of mixed-use project at 12555 Ventura Blvd. in Studio City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Affordable housing slated for 5003 N. Kester Ave. in Sherman Oaks (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- L.A. County Supes approve gap financing for affordable housing at 5010 E. 3rd St. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affinius Capital Originates $97.9M Refinancing for Multifamily Community in D.C. (REBusiness Online, Washington DC): Capital event keywords detected: refinancing, joint_venture. Primary topic set to capital_markets; confidence low.
- CBRE Arranges Sale of Future Mixed-Use Development in Wisconsin (Connect CRE Apartments, Louisville / Kentucky): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- Northmarq Arranges $96M Refi on SoCal Apartment Portfolio (Connect CRE Apartments, Los Angeles / California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Eight townhomes in the works at 146 N. Berendo St. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- JLL Arranges $333.3M Financing for a Luxury 3-Property Colorado Multifamily Portfolio (Yield PRO, Colorado): No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Retail market tightens, L.A. multifamily sales jump, and more (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- MidPen Housing Completes 176-Unit Ira D. Hall Square Apartments in Silicon Valley (REBusiness Online, California): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Origin, Mill Creek Teaming Up on 190-Unit Scottsdale Rental Community (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 34

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.