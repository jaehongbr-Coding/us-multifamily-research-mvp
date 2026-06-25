# Classification Quality Report

Generated: 2026-06-25 00:14:47

## Classification Summary

- Total articles classified: 80
- Topic distribution: development_pipeline: 14; capital_markets: 13; supply_demand: 12; transaction_market: 12; gp_activity: 11; institutional_capital: 7; macro_financing: 5; other: 5
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 14 article(s), high 2, medium 6, low 6, unknown 0. Top markets: Los Angeles / California (4); Miami / Florida (3); Other / Unknown (3); California (2); Dallas / Texas (1).
- capital_markets: 13 article(s), high 6, medium 6, low 1, unknown 0. Top markets: New York City / New York (4); National (2); Seattle (1); Other / Unknown (1); New York (1).
- supply_demand: 12 article(s), high 0, medium 1, low 11, unknown 0. Top markets: Other / Unknown (7); National (5).
- transaction_market: 12 article(s), high 3, medium 6, low 3, unknown 0. Top markets: Sun Belt (2); California (2); Phoenix / Arizona (1); Houston / Texas (1); Other / Unknown (1).
- gp_activity: 11 article(s), high 0, medium 0, low 2, unknown 9. Top markets: National (3); Other / Unknown (2); California (2); Riverside / California (1); Sun Belt (1).
- institutional_capital: 7 article(s), high 0, medium 3, low 4, unknown 0. Top markets: New York (2); Riverside / California (1); Dallas / Texas (1); San Francisco / California (1); Austin / Texas (1).
- macro_financing: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (3); Santa Monica / California (1); Los Angeles / California (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: San Francisco / California (2); Santa Monica / California (1); Other / Unknown (1); Los Angeles / California (1).
- research_data: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: California (1).

## Low Confidence / Unknown Articles

- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist (Multifamily Executive, National): Supply/demand terms detected: effective_rent_growth, concession. Primary topic set to supply_demand; confidence low.
- Hunt Capital Partners Launches $125M Dallas Adaptive Reuse Venture (Yield PRO, Dallas / Texas): Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- Greystone Provides HUD/FHA Loan for Central NJ Multifamily (Connect CRE, New York): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Construction goes vertical for mixed-use project at 1902 Wilshire Blvd. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affordable housing under constructiona t 1740 N. Wilton Place in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: under_construction. Primary topic set to development_pipeline; confidence low.
- Affordable housing takes shape at 733 S. Burlington Ave. in Westlake (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Linc Housing plans new project at 3590 Elm Ave. in Long Beach (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Work beginning for Taix redevelopment at 1911 Sunset Blvd. in Echo Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: redevelopment. Primary topic set to development_pipeline; confidence low.
- Adaptive reuse project gets colorful new exterior at 3325 Wilshire Blvd. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- New plan for apartments at 745 17th Street in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Retail-to-Housing Conversion Proposed At 145 Bosworth Street, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Quarterra, Eldridge Acre Partners Break Ground on Murrieta Apartments (Connect CRE Apartments, Riverside / California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- The City of Salisbury to Convert Former Textile Mill into Multifamily Affordable Housing Units (Yield PRO, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Newmark Arranges $52M Refi for Cypress Apartment Owner (Connect CRE Texas, Houston / Texas): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Meeting Tomorrow At 906 Clement Street, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Missing Middle Weakness (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Lowes Foods to Anchor Mixed-Use Project in Mooresville, North Carolina (REBusiness Online, Sun Belt): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Developer Planning 220-Unit Homestead-Area Rental Community (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- JLL Arranges $252M Financing for Huntington Beach Seniors Project (Connect CRE Orange County, California): Financing type keywords detected: public_subsidy. Primary topic set to gp_activity; confidence low.
- Additional low/unknown rows omitted: 27

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.