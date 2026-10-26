# Classification Quality Report

Generated: 2026-10-26 01:00:42

## Classification Summary

- Total articles classified: 79
- Topic distribution: development_pipeline: 21; transaction_market: 13; capital_markets: 11; supply_demand: 11; institutional_capital: 8; macro_financing: 6; gp_activity: 5; other: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 21 article(s), high 3, medium 5, low 13, unknown 0. Top markets: Other / Unknown (7); California (4); Los Angeles / California (3); San Francisco / California (2); Atlanta / Georgia (2).
- transaction_market: 13 article(s), high 2, medium 5, low 6, unknown 0. Top markets: Atlanta / Georgia (4); Louisville / Kentucky (1); Washington DC (1); Phoenix / Arizona (1); Colorado (1).
- capital_markets: 11 article(s), high 4, medium 4, low 3, unknown 0. Top markets: Los Angeles / California (4); Miami / Florida (2); California (2); Nevada (1); New York City / New York (1).
- supply_demand: 11 article(s), high 0, medium 0, low 11, unknown 0. Top markets: Other / Unknown (7); National (2); Miami / Florida (1); California (1).
- institutional_capital: 8 article(s), high 4, medium 1, low 3, unknown 0. Top markets: Other / Unknown (4); Seattle (1); Texas (1); Phoenix / Arizona (1); Atlanta / Georgia (1).
- macro_financing: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (3); Sun Belt (1); Los Angeles / California (1); California (1).
- gp_activity: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Other / Unknown (3); Los Angeles / California (1); National (1).
- other: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: Los Angeles / California (2); Texas (1).
- research_data: 1 article(s), high 0, medium 0, low 0, unknown 1. Top markets: Los Angeles / California (1).

## Low Confidence / Unknown Articles

- 6 Blackstone multifamily properties move to servicing (Multifamily Dive, Seattle): Institutional activity terms detected: private_equity_activity. Primary topic set to institutional_capital; confidence low.
- FIRST DRAFT LIVE: Why Sun Belt Multifamily Giant Cortland Is Moving Its Money North (Bisnow, Sun Belt): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- CBRE Arranges Sale of Future Mixed-Use Development in Wisconsin (Connect CRE, Louisville / Kentucky): Capital event keywords detected: acquisition, disposition. Primary topic set to transaction_market; confidence low.
- Northmarq Arranges $96M Refi on SoCal Apartment Portfolio (Connect CRE, Los Angeles / California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- City Council upholds approval of mixed-use project at 12555 Ventura Blvd. in Studio City (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- Affordable housing slated for 5003 N. Kester Ave. in Sherman Oaks (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- L.A. County Supes approve gap financing for affordable housing at 5010 E. 3rd St. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Expansion of apartment complex at 6007 Sunset survives appeal (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Eight townhomes in the works at 146 N. Berendo St. in Koreatown (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Hollywood's Yamashiro Complex Gets $25M Refinance: The Los Angeles Deal Sheet (Bisnow, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Retail market tightens, L.A. multifamily sales jump, and more (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Developer plans high-rise apartments at 6409 Sunset Blvd. in Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- New Building Permits For Backyard ADUs at 466 Frederick Street, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: permit. Primary topic set to development_pipeline; confidence low.
- Colliers Facilitates Sale of Boutique Multifamily Property in Seattle (Yield PRO, Seattle): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Multifamily starts fell in September amid high construction costs (Multifamily Dive, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Brighton Multifamily Draws Record Pool of Potential Buyers (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993 (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Additional low/unknown rows omitted: 31

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.