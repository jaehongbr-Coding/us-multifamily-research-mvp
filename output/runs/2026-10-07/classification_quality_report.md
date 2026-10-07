# Classification Quality Report

Generated: 2026-10-07 02:09:00

## Classification Summary

- Total articles classified: 72
- Topic distribution: transaction_market: 17; capital_markets: 12; development_pipeline: 12; supply_demand: 9; macro_financing: 7; gp_activity: 6; other: 4; institutional_capital: 3
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 17 article(s), high 4, medium 7, low 6, unknown 0. Top markets: California (4); Other / Unknown (3); Atlanta / Georgia (3); Los Angeles / California (1); Phoenix / Arizona (1).
- capital_markets: 12 article(s), high 3, medium 7, low 2, unknown 0. Top markets: National (2); Other / Unknown (2); California (2); Southeast (1); New York City / New York (1).
- development_pipeline: 12 article(s), high 2, medium 5, low 5, unknown 0. Top markets: Other / Unknown (6); Phoenix / Arizona (2); Atlanta / Georgia (1); Tennessee (1); Austin / Texas (1).
- supply_demand: 9 article(s), high 0, medium 0, low 9, unknown 0. Top markets: Other / Unknown (7); National (2).
- macro_financing: 7 article(s), high 0, medium 0, low 0, unknown 7. Top markets: Other / Unknown (5); California (1); Los Angeles / California (1).
- gp_activity: 6 article(s), high 0, medium 0, low 0, unknown 6. Top markets: Other / Unknown (4); Los Angeles / California (1); National (1).
- other: 4 article(s), high 0, medium 0, low 0, unknown 4. Top markets: Santa Monica / California (1); Denver / Colorado (1); Other / Unknown (1); San Francisco / California (1).
- institutional_capital: 3 article(s), high 1, medium 1, low 1, unknown 0. Top markets: Miami / Florida (2); New York (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Beverly Hills / California (1); Santa Monica / California (1).

## Low Confidence / Unknown Articles

- Fresh imagery for proposed housing complex at 1238 Lincoln Blvd. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Mixed-use project proposed at 177 S. Robertson Blvd. in Beverly Hills (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- SoLa Impact score $93M financing package for housing at 252 W. Imperial Highway (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- North Hollywood Apartments Trade to Locally Based LLC (Connect CRE California, Los Angeles / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Cambridge Residential Tower Secures $522M Loan: The Boston Deal Sheet (Bisnow, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- JLL Arranges $276M Refi for Newport Beach Seniors Communities (Connect CRE Orange County, California): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low.
- Design tweaks for affordable housing at 1238 7th St. in Santa Monica (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Marcus & Millichap Arranges $7.1M Sale of 32-Unit Multifamily Property in Anaheim California (Yield PRO, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Related Affiliate Obtains $167M Loan Package for Miami Apartment Community (Connect CRE South Florida, Miami / Florida): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993 (Connect CRE, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Speed cams coming soon, RAND Corporation reports on Santa Monica, and more (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Construction loan issued for affordable housing at 400 Centinela Ave. in Inglewood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Capital event keywords detected: construction_financing. Financing type keywords detected: construction_loan. Primary topic set to capital_markets; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- N. Phoenix Apartments Trade for $58.7M (Connect CRE Phoenix, Phoenix / Arizona): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Marcus & Millichap Brokers $31.9M Sale of the Largest Private Market-Rate Apartment Portfolio in Newport Rhode Island (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Multifamily Missing Middle Construction: First Quarter 2026 (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Erland Construction Partners with Nordblom on New Dedham Multifamily (Connect CRE, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Investor Takes Over Distressed Atlanta Apartment Asset (Connect CRE Atlanta, Atlanta / Georgia): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Additional low/unknown rows omitted: 22

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.