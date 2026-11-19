# Entity Resolution Report

Generated: 2026-11-19 03:59:48

- Total raw entities reviewed: 203
- Total canonical entities created: 49
- Possible duplicate entity groups: 9
- Weak matches needing review: 138
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 104 occurrence(s)
- JLL: 14 occurrence(s)
- CBRE: 11 occurrence(s)
- Marcus & Millichap: 11 occurrence(s)
- Kennedy Wilson: 10 occurrence(s)
- Blackstone: 8 occurrence(s)
- Hines: 7 occurrence(s)
- Kairoi Residential: 7 occurrence(s)
- Merchants Capital: 7 occurrence(s)
- Benefit Street Partners: 6 occurrence(s)

## Top Canonical Markets

- Los Angeles: 56 occurrence(s)
- Sun Belt: 43 occurrence(s)
- Other / Unknown: 30 occurrence(s)
- California: 16 occurrence(s)
- New York: 12 occurrence(s)
- Unknown: 11 occurrence(s)
- Florida: 9 occurrence(s)
- Denver / Colorado: 6 occurrence(s)
- South Florida: 6 occurrence(s)
- National: 5 occurrence(s)

## Possible Duplicate Entities

- Blackstone: Blackstone, blackstone
- CBRE: CBRE, cbre
- California: Beverly Hills / California, California, Disposition / Exit - California - Anaheim Sale is First Closing in Broader Multifamily Portfolio, Disposition / Exit - California - Fourth Sale Closes in Anaheim Multifamily Portfolio, JV / Partnership - California - American Campus Communities Expands Partnership with UC Irvine
- Freddie Mac: Freddie Mac, freddie mac
- JLL: Disposition / Exit - Other / Unknown - JLL Arranges $31M Sale of Boutique Apartment Property in Chicago, JLL, JV / Partnership - Other / Unknown - JLL Arranges Financing for 419-Unit Luxury Multifamily Development in Evanston, Illinois, jll
- Kennedy Wilson: Acquisition - Beverly Hills / California - Kennedy Wilson Sells 334-Unit Atlas Apartments in Issaquah, Washington for $149M, General Project Signal - Tampa / Florida - New $200M Tampa Rental Community to Include Mark Wahlberg’s Gym, Kennedy Wilson, kennedy wilson
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - ORIX Acquires Buckhead Apartments for $83M, Atlanta / Georgia, Construction Financing - Miami / Florida - Work Underway on 311-Unit Oakland Park Apartment Building, Development Start - Virginia - 3 apartment projects broke ground last week, Disposition / Exit - Atlanta / Georgia - Perimeter Center Rental Community Goes for $120M, Disposition / Exit - Atlanta / Georgia - Portman Begins Mixed-Use Redevelopment of 20-Acre Office Campus in Metro Atlanta, Disposition / Exit - Los Angeles / California - 269 homes to replace nursery at 7639 Topanga Canyon Blvd. in Canoga Park, Entitlement / Permitting - Los Angeles - Multifamily housing unwrapped at 4429 S. Vermont Ave. in South L.A., Entitlement / Permitting - Los Angeles / California - Affordable housing takes shape at 3985 S. Meier St. in Mar Vista, Entitlement / Permitting - Los Angeles / California - Affordable housing underway at 6908 Baird Ave. in Reseda, Entitlement / Permitting - New York City / New York - MTA Approves EMP Capital as Developer of 1119 Pacific Street in Brooklyn, Entitlement / Permitting - Other / Unknown - New plan for housing at 452 N. Los Robles Ave. in Pasadena, General Project Signal - Austin / Texas - Morgan Completes 345-Unit Multifamily Project in North Austin, General Project Signal - Los Angeles / California - Ascent Developer Solutions Closes $220M Residential Loan Securitization, General Project Signal - Los Angeles / California - Four townhomes coming to 1155 N. Heliotrope Dr. in East Hollywood, General Project Signal - Los Angeles / California - Los Angeles Ranks 5th in the Nation for Number of Apartment Units Under Construction, General Project Signal - Miami / Florida - 13th Floor, ANF Complete $89M Hallandale Beach Rental Community, JV / Partnership - Atlanta / Georgia - Morehouse, Spelman Debut $147M Student Housing Project, JV / Partnership - Los Angeles / California - 'Graffiti towers' no more: Oceanwide Plaza is officially cleaned up, JV / Partnership - Miami / Florida - Fort Lauderdale JV Scores $285M Refi for 42-Story Apartment Tower, JV / Partnership - New York - PCCP Joint Venture Announce Development of Class A Multifamily Property in Baldwin New Yor..., L.A., Los Angeles, Los Angeles / California
- New York: Brooklyn, New York, New York City / New York
- Sun Belt: Atlanta, Austin, Austin / Texas, Charlotte, Dallas, General Project Signal - Phoenix / Arizona - Cross Harbor Scores $78.5M Financing for Tempe Rental Community, General Project Signal - Sun Belt - Merchants Capital Secures $15M for Affordable Housing Development, Miami / Florida, Phoenix, Phoenix / Arizona, Sun Belt, Tampa, Tampa / Florida

## Weak Matches Needing Manual Review

- Acquisition - Texas - IPA Negotiates Sale of 399-Unit Apartment Community in Grapevine, Texas -> Acquisition - Texas - IPA Negotiates Sale of 399-Unit Apartment Community in Grapevine, Texas (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Benefit Street Partners -> Benefit Street Partners (40, deal_pipeline.csv)
- Benefit Street Partners -> Benefit Street Partners (40, gp_intelligence.csv)
- Benefit Street Partners -> Benefit Street Partners (40, institutional_relationships.csv)
- Benefit Street Partners -> Benefit Street Partners (40, relationship_graph.csv)
- Beverly Hills -> Beverly Hills (40, deal_pipeline.csv)
- Beverly Hills -> Beverly Hills (40, relationship_graph.csv)
- Beverly Hills / California -> California (60, articles.csv)
- Beverly Hills / California -> California (60, deal_pipeline.csv)
- Beverly Hills / California -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Anaheim Sale is First Closing in Broader Multifamily Portfolio -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Fourth Sale Closes in Anaheim Multifamily Portfolio -> California (60, relationship_graph.csv)
- JV / Partnership - California - American Campus Communities Expands Partnership with UC Irvine -> California (60, relationship_graph.csv)
- Denver -> Denver (40, deal_pipeline.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
