# Classification Quality Report

Generated: 2026-10-20 01:36:57

## Classification Summary

- Total articles classified: 69
- Topic distribution: supply_demand: 13; capital_markets: 12; development_pipeline: 12; transaction_market: 12; gp_activity: 6; institutional_capital: 6; macro_financing: 4; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- supply_demand: 13 article(s), high 1, medium 0, low 12, unknown 0. Top markets: Other / Unknown (6); National (3); Miami / Florida (2); New York (1); Atlanta / Georgia (1).
- capital_markets: 12 article(s), high 3, medium 6, low 3, unknown 0. Top markets: Other / Unknown (3); California (3); Miami / Florida (2); Dallas / Texas (1); New York City / New York (1).
- development_pipeline: 12 article(s), high 0, medium 3, low 9, unknown 0. Top markets: Other / Unknown (5); National (3); Dallas / Texas (1); New York City / New York (1); San Francisco / California (1).
- transaction_market: 12 article(s), high 3, medium 4, low 5, unknown 0. Top markets: Atlanta / Georgia (5); Other / Unknown (3); Dallas / Texas (1); California (1); Washington DC (1).
- gp_activity: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (5); National (1).
- institutional_capital: 6 article(s), high 1, medium 2, low 3, unknown 0. Top markets: California (1); Miami / Florida (1); New York City / New York (1); New York (1); Texas (1).
- macro_financing: 4 article(s), high 0, medium 0, low 1, unknown 3. Top markets: Other / Unknown (3); Houston / Texas (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); Santa Monica / California (1).
- research_data: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: Other / Unknown (1).

## Low Confidence / Unknown Articles

- $62.1M Refinancing Secured for North Carolina Multifamily Community (Yield PRO, Other / Unknown): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- 32 apartments proposed at 806 N. Sweetzer Ave. in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Rendering vs. Reality: 176 apartments at 2225 Sunset Boulevard in Echo Park (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Developers land financing for mixed-use project at 11111 Jefferson Blvd. in Culver City (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Southwest Valley Community Plans take a step forward (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- PCCP Provides $41M Refi on North Park Multifamily (Connect CRE Apartments, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- HSR, Barings Break Ground on 501-Unit Multifamily Project in Redwood City, California (REBusiness Online, California): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- The South Florida Real Estate Market Leans Evermore on the Wealthy (Commercial Observer, Miami / Florida): Institutional activity terms detected: family_office_activity. Primary topic set to institutional_capital; confidence low.
- Stimdel Properties Files Plans to Build 612 Apartments in Astoria (Commercial Observer, New York City / New York): Development-stage terms detected: zoning. Primary topic set to development_pipeline; confidence low.
- Development Group Starts Work on 371-Unit Boynton Beach Multifamily Venture (Connect CRE South Florida, Miami / Florida): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- New Building Permits For 230 Anza Street in Lone Mountain, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Distressed Sales Jump 26%, Led By Multifamily Deals (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: distress_sale. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- 229-Unit Lawton Multifamily Community Trades Hands (Connect CRE Texas, Dallas / Texas): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993 (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Fresh renderings for new workforce housing at 315 N. Pasadena Ave. (Urbanize LA, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Additional low/unknown rows omitted: 26

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.