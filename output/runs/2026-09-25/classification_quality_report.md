# Classification Quality Report

Generated: 2026-09-25 01:10:11

## Classification Summary

- Total articles classified: 75
- Topic distribution: transaction_market: 22; development_pipeline: 14; gp_activity: 10; supply_demand: 9; macro_financing: 7; capital_markets: 5; institutional_capital: 4; other: 2
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- transaction_market: 22 article(s), high 4, medium 10, low 8, unknown 0. Top markets: California (5); San Francisco / California (4); Other / Unknown (3); Atlanta / Georgia (3); Dallas / Texas (2).
- development_pipeline: 14 article(s), high 0, medium 4, low 10, unknown 0. Top markets: Other / Unknown (5); Miami / Florida (2); Atlanta / Georgia (2); Sun Belt (1); National (1).
- gp_activity: 10 article(s), high 0, medium 0, low 1, unknown 9. Top markets: Other / Unknown (3); Phoenix / Arizona (2); Los Angeles / California (1); Miami / Florida (1); Nashville / Tennessee (1).
- supply_demand: 9 article(s), high 0, medium 0, low 9, unknown 0. Top markets: Other / Unknown (7); National (2).
- macro_financing: 7 article(s), high 0, medium 0, low 1, unknown 6. Top markets: Other / Unknown (2); Beverly Hills / California (1); Los Angeles / California (1); California (1); National (1).
- capital_markets: 5 article(s), high 1, medium 4, low 0, unknown 0. Top markets: Miami / Florida (2); Other / Unknown (1); Austin / Texas (1); Nashville / Tennessee (1).
- institutional_capital: 4 article(s), high 1, medium 1, low 2, unknown 0. Top markets: National (2); New York (1); Washington DC (1).
- other: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: California (1); Colorado (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Los Angeles / California (1); Colorado (1).

## Low Confidence / Unknown Articles

- Northmarq Secures $45M Sale of 87-Unit Bay Area Mixed-Use Multifamily Property (Yield PRO, San Francisco / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Kidder Mathews Arranges $21.8M Sale of Two Apartment Properties in Riverside California (Yield PRO, Riverside / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- LA City Council Approves Largest-Ever Funding Pool for Affordable Housing (Connect CRE, Los Angeles / California): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- 270 apartments take shape at 200 E. First American Way in Santa Ana (Urbanize LA, Beverly Hills / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Construction goes vertical for mixed-use project at 155 W. 6th St. in San Pedro (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Apartment complex fully framed at 11250 La Grange Ave. in Sawtelle (Urbanize LA, California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Senior affordable housing starting work at 7556 Woodlake Ave. in West Hills (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Renderings Revealed: Mixed-use project at 305 E. Colorado St. in Glendale (Urbanize LA, Colorado): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to research_data; confidence unknown.
- Oxford Cos., Crawford Hoying Receive State Approval for Arbor South Mixed-Use Project in Michigan (REBusiness Online, Other / Unknown): Development-stage terms detected: entitlement, zoning. Primary topic set to development_pipeline; confidence low.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Miami's Building Boom Means Keeping Renters Is Just As Hard As Finding Them (Bisnow, Miami / Florida): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Russian Hill Apartments Trade After 50 Years of Family Ownership (Connect CRE, San Francisco / California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Devens Site Will Yield 65 Affordable Apartments (Connect CRE Apartments, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- IPA Closes Built-to-Rent Multifamily Sale in Suburban North Dallas (Yield PRO, Dallas / Texas): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- L&G, Taurus Break Ground on Concord Multifamily (Connect CRE, National): Development-stage terms detected: construction_start. Primary topic set to development_pipeline; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Clear Blue Company Breaks Ground on Nashville-Area Multifamily Affordable Housing Project (Yield PRO, Nashville / Tennessee): Development-stage terms detected: construction_start, delivery. Primary topic set to development_pipeline; confidence low.
- HTG Debuts $115M Miami Affordable Housing Project (Connect CRE South Florida, Miami / Florida): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Multifamily Missing Middle Falls Back (NAHB Eye on Housing - Multifamily, Other / Unknown): No clear rule-based event keyword was detected. Primary topic set to gp_activity; confidence unknown.
- Additional low/unknown rows omitted: 30

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.