# Classification Quality Report

Generated: 2026-10-31 02:02:59

## Classification Summary

- Total articles classified: 82
- Topic distribution: development_pipeline: 20; transaction_market: 13; capital_markets: 11; gp_activity: 9; supply_demand: 8; macro_financing: 7; other: 7; institutional_capital: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 20 article(s), high 0, medium 4, low 16, unknown 0. Top markets: Other / Unknown (7); Seattle (2); Los Angeles / California (2); Atlanta / Georgia (2); California (2).
- transaction_market: 13 article(s), high 3, medium 7, low 3, unknown 0. Top markets: Atlanta / Georgia (4); California (3); Other / Unknown (2); New York City / New York (1); Phoenix / Arizona (1).
- capital_markets: 11 article(s), high 5, medium 6, low 0, unknown 0. Top markets: Sun Belt (2); Los Angeles / California (2); Austin / Texas (1); California (1); New York City / New York (1).
- gp_activity: 9 article(s), high 0, medium 0, low 1, unknown 8. Top markets: Other / Unknown (4); Phoenix / Arizona (2); National (2); Arizona (1).
- supply_demand: 8 article(s), high 0, medium 0, low 8, unknown 0. Top markets: Other / Unknown (5); National (2); Texas (1).
- macro_financing: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (3); San Francisco / California (1); Los Angeles / California (1); California (1); Virginia (1).
- other: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Los Angeles / California (2); Other / Unknown (2); San Francisco / California (2); Santa Monica / California (1).
- institutional_capital: 4 article(s), high 0, medium 2, low 2, unknown 0. Top markets: Riverside / California (2); Other / Unknown (1); Atlanta / Georgia (1).
- research_data: 3 article(s), high 0, medium 0, low 0, unknown 3. Top markets: California (2); Other / Unknown (1).

## Low Confidence / Unknown Articles

- Eastern Bank Lends on Adaptive Reuse of Former New London Newspaper Headquarters (Connect CRE, Other / Unknown): Development-stage terms detected: redevelopment, adaptive_reuse. Primary topic set to development_pipeline; confidence low.
- 200-Unit Affordable Housing Project Planned in North Seattle (Connect CRE, Seattle): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Fresh renderings for Tishman Speyer projects in Downtown Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Affordable housing underway at 5403 S. Inglewood Blvd. in Del Rey (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 37-unit affordable housing complex underway at 3751 S. Delmas Ter. in Palms (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- 25 apartments completed at 11013 Hartsook St. in North Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- 390 apartments underway at 6615 PCH in Long Beach (Urbanize LA, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Modular affordable housing takes shape at 4301 S. Vermont Ave. (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Affordable housing starts work at 400 Centinela Ave. in Inglewood (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- 12 homes pitched for 2315 S. Oakwood Ave. in Venice (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Construction Starts For 39340 Fremont Boulevard, Fremont (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Toro Development Opens $560M Medley Mixed-Use Destination in Johns Creek, Georgia (REBusiness Online, Atlanta / Georgia): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Arrow Secures $13.25M CMBS Financing for East Brunswick Multifamily Property (Yield PRO, Other / Unknown): Financing type keywords detected: cmbs. Primary topic set to gp_activity; confidence low.
- Voorhees Greenlights 178-Unit Office-To-Resi Conversion Amid Multifamily Boom (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Fourth Sale Closes in Anaheim Multifamily Portfolio (Connect CRE Orange County, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Realty Capital Breaks Ground on 289-Unit Apartment Complex in Granbury, Texas (REBusiness Online, Texas): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- 45-Story Tower Proposed For 325 Fremont Street, SoMa, San Francisco (SF YIMBY, San Francisco / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Prosper Greenlights $2B Italian-Themed Community (Connect CRE Texas, Dallas / Texas): Development-stage terms detected: entitlement, zoning. Primary topic set to development_pipeline; confidence low.
- Leon Multifamily Building 343-Unit N. Phoenix Venture (Connect CRE Phoenix, Phoenix / Arizona): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Additional low/unknown rows omitted: 35

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.