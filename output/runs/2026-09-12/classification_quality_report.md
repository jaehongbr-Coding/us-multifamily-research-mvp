# Classification Quality Report

Generated: 2026-09-12 00:56:35

## Classification Summary

- Total articles classified: 80
- Topic distribution: development_pipeline: 16; transaction_market: 15; capital_markets: 12; supply_demand: 10; gp_activity: 9; macro_financing: 7; other: 5; institutional_capital: 4
- Classification is rule-based and conservative. Low or unknown labels should be treated as review queues, not failures.

## Topic Distribution

- development_pipeline: 16 article(s), high 2, medium 5, low 9, unknown 0. Top markets: Other / Unknown (10); Los Angeles / California (2); Atlanta / Georgia (2); California (1); Dallas / Texas (1).
- transaction_market: 15 article(s), high 3, medium 7, low 5, unknown 0. Top markets: Other / Unknown (4); California (4); New York City / New York (2); Dallas / Texas (2); Atlanta / Georgia (2).
- capital_markets: 12 article(s), high 7, medium 3, low 2, unknown 0. Top markets: Miami / Florida (5); New York City / New York (2); Other / Unknown (2); National (1); West Palm Beach / Florida (1).
- supply_demand: 10 article(s), high 0, medium 0, low 10, unknown 0. Top markets: Other / Unknown (6); National (3); Los Angeles / California (1).
- gp_activity: 9 article(s), high 0, medium 0, low 0, unknown 9. Top markets: Other / Unknown (4); Phoenix / Arizona (3); Miami / Florida (1); National (1).
- macro_financing: 7 article(s), high 0, medium 0, low 2, unknown 5. Top markets: Other / Unknown (3); Los Angeles / California (1); Dallas / Texas (1); California (1); Atlanta / Georgia (1).
- other: 5 article(s), high 0, medium 0, low 0, unknown 5. Top markets: Los Angeles / California (3); Santa Monica / California (1); Other / Unknown (1).
- institutional_capital: 4 article(s), high 0, medium 2, low 2, unknown 0. Top markets: Los Angeles / California (1); Miami / Florida (1); Seattle (1); Other / Unknown (1).
- research_data: 2 article(s), high 0, medium 0, low 0, unknown 2. Top markets: Other / Unknown (1); Los Angeles / California (1).

## Low Confidence / Unknown Articles

- Northmarq Arranges combined $67.25M Sales of 2 Multifamily Apartments in Lombard and Naperville Illinois (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Cushman & Wakefield Brokers Sale of Fully Leased Rochester Apartments (Connect CRE, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- 13 apartments approved for empty lot at 4127 E. Supreme Court (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. Development-stage terms detected: entitlement. Primary topic set to development_pipeline; confidence low.
- 75 aparmtents slated for 7034 N. Baird Ave. in Reseda (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Former Sunkist HQ to become 95 apartments (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Housing unwrapped at 11261 Santa Monica Boulevard (Urbanize LA, Santa Monica / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Mixed-use building starts to rise at 8025 Santa Monica Blvd. in West Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to macro_financing; confidence unknown.
- Dominium to Build 350 Affordable BTR Units in Terrell (Connect CRE Texas, Dallas / Texas): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- WNC Closes on 23rd California-Focused Affordable Housing Fund (Connect CRE Orange County, California): Financing type keywords detected: tax_credit_financing. Primary topic set to macro_financing; confidence low.
- Infill housing coming to 1030 N. Sierra Bonita Ave. in West Hollywood (Urbanize LA, Los Angeles / California): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- MidPen Housing Completes 50-Unit Jessie Street Terrace Affordable Housing Property in Santa Cruz (REBusiness Online, California): Development-stage terms detected: delivery, redevelopment. Primary topic set to development_pipeline; confidence low.
- C-PACE Financing is Now a Capital Stack Conversation (Connect CRE, Los Angeles / California): Institutional activity terms detected: lender_activity. Primary topic set to institutional_capital; confidence low.
- Fengate, Mavrek Break Ground on 25-Story Apartment Tower in Chicago’s West Loop (REBusiness Online, National): Supply/demand terms detected: effective_rent_growth, vacancy, occupancy. Primary topic set to supply_demand; confidence low.
- Best Year for Missing Middle Construction Since 2007 (NAHB Eye on Housing - Multifamily, Other / Unknown): Supply/demand terms detected: supply_pressure. Primary topic set to supply_demand; confidence low.
- Colliers Team Closes Sale of 107-Unit Central Valley Apartments (Connect CRE California, California): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Meeting Tonight for Amoeba Apartments in Southside, Berkeley (SF YIMBY, Other / Unknown): Limited/paywalled article; classification is based on title, URL, source, and available lead text only. No clear rule-based event keyword was detected. Primary topic set to other; confidence unknown.
- Starwood Capital, Trinitas to Develop Three Student Housing Communities Totaling 2,046 Beds (REBusiness Online, Miami / Florida): Capital event keywords detected: joint_venture. Primary topic set to institutional_capital; confidence low.
- $83M Sale of Two Oregon Multifamily Assets Brokered by Institutional Property Advisors (Yield PRO, Other / Unknown): Capital event keywords detected: disposition. Primary topic set to transaction_market; confidence low.
- Slate Property Group Secures $63M Refinancing for Chelsea Multifamily Portfolio (Yield PRO, New York City / New York): Capital event keywords detected: refinancing. Primary topic set to capital_markets; confidence low. Operator/property management activity detected.
- Share of Apartments Built in Buildings with 50+ Units Moves Higher in 2025 (NAHB Eye on Housing - Multifamily, Other / Unknown): Development-stage terms detected: delivery. Primary topic set to development_pipeline; confidence low.
- Additional low/unknown rows omitted: 31

## Data Quality Notes

- Source summaries and RSS snippets can be thin, so some articles remain low confidence until full context is available.
- Similar financing and transaction language can overlap; detailed fields should be read together rather than as one definitive label.
- Market labels remain conservative when geography is not explicit.

## Recommended Rule Improvements

- Review low-confidence rows after several runs and add source-specific terms only when repeated misclassification is visible.
- Add sponsor/lender dictionaries gradually as relationship intelligence matures.
- Keep broad words such as multifamily, housing, and property from driving development classification by themselves.