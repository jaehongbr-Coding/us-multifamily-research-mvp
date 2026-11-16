# Entity Resolution Report

Generated: 2026-11-16 02:35:24

- Total raw entities reviewed: 227
- Total canonical entities created: 68
- Possible duplicate entity groups: 8
- Weak matches needing review: 185
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 139 occurrence(s)
- JLL: 33 occurrence(s)
- Marcus & Millichap: 20 occurrence(s)
- CBRE: 14 occurrence(s)
- Blackstone: 8 occurrence(s)
- Hines: 7 occurrence(s)
- northmarq: 6 occurrence(s)
- Kairoi Residential: 5 occurrence(s)
- Benefit Street Partners: 4 occurrence(s)
- Related Companies: 4 occurrence(s)

## Top Canonical Markets

- California: 49 occurrence(s)
- Los Angeles: 41 occurrence(s)
- Sun Belt: 39 occurrence(s)
- Other / Unknown: 38 occurrence(s)
- Unknown: 18 occurrence(s)
- New York: 16 occurrence(s)
- National: 12 occurrence(s)
- Texas: 9 occurrence(s)
- Southeast: 7 occurrence(s)
- South Florida: 6 occurrence(s)

## Possible Duplicate Entities

- Blackstone: Blackstone, blackstone
- CBRE: Acquisition - Other / Unknown - CBRE Brokers $30M Sale of Multifamily Portfolio in Madison, Wisconsin, CBRE, cbre
- California: Acquisition - California - TruAmerica expands into ground-up development with California project, California, Development Start - California - 3 multifamily groundbreakings you may have missed, Disposition / Exit - California - Anaheim Sale is First Closing in Broader Multifamily Portfolio, Disposition / Exit - California - Fourth Sale Closes in Anaheim Multifamily Portfolio, Disposition / Exit - California - Fresno Low-Rise Trades to Private Buyer in All-Cash Deal, Disposition / Exit - California - Southern California transportation projects awarded new state funding, Disposition / Exit - Riverside / California - Advanced Real Estate Pays $56 Million for Ontario Multifamily Complex, Entitlement / Permitting - San Francisco / California - New Building Permits Filed For 704 North Point Street, San Francisco, General Project Signal - California - Construction Topped Out For 641 5th Street, West Sacramento, JV / Partnership - California - American Campus Communities Expands Partnership with UC Irvine, Riverside / California, San Francisco / California, Southern California
- JLL: Acquisition - Florida - JLL Arranges Sale of 296,419 SF Lifestyle Mixed-Use Center in Coconut Creek, Florida, Acquisition - New York City / New York - JLL Arranges $118.9M Acquisition Loan for Manhattan Apartment Building, General Project Signal - Other / Unknown - JLL Arranges $39.1M in Financing for Apartment Complex in Suburban Milwaukee, JLL, jll
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - ORIX Acquires Buckhead Apartments for $83M, Acquisition - Riverside / California - Advanced Real Estate Buys Inland Empire Apartment Complex for $56M, Atlanta / Georgia, BTR / Build-to-Rent - National - Legislative risk continues to cloud BTR’s capital outlook; here’s why, Construction Financing - Miami / Florida - Kadima Inks Financing for 124-unit Hallandale Beach Condo Project, Construction Financing - Other / Unknown - Rockland Trust Lends on Income-Restricted Apartments in Malden, Dallas / Texas, Disposition / Exit - Atlanta / Georgia - Perimeter Center Rental Community Goes for $120M, Disposition / Exit - California - Marcus & Millichap Arranges Multifamily Affordable Housing Sale in South Lake, Disposition / Exit - Los Angeles / California - Graffiti Removal Sets Stage for Sale of Oceanwide Plaza, Entitlement / Permitting - Dallas / Texas - Hoque Global's $450M Downtown Dallas Project Loses City Incentive, Entitlement / Permitting - Los Angeles / California - Costco-anchored project adds more housing at 5035 Coliseum St. in Baldwin Hills, Entitlement / Permitting - Other / Unknown - 152 apartments planned at 2315 Marine Ave. in Gardena, General Project Signal - Los Angeles / California - Affordable housing takes shape at 3455 Slauson Ave. in Hyde Park, General Project Signal - Los Angeles / California - Four townhomes coming to 1155 N. Heliotrope Dr. in East Hollywood, General Project Signal - Miami / Florida - 13th Floor, ANF Complete $89M Hallandale Beach Rental Community, Inland Empire, JV / Partnership - Atlanta / Georgia - Morehouse, Spelman Debut $147M Student Housing Project, Los Angeles, Los Angeles / California, Refinancing - Other / Unknown - PMG Secures $285M Refi for New Fort Lauderdale Rental
- New York: Disposition / Exit - New York City / New York - Marcus & Millichap Arranges Sale of Multifamily Asset Redevelopment Opportunity in Brookly..., New York, New York City, New York City / New York, Office-to-Residential Conversion - New York City / New York - New York City Office-to-Residential Conversion Secures $231M
- Related Companies: Boca Raton Apartment Units The Related Group, General Project Signal - Miami / Florida - Related Building 494 Boca Raton Apartment Units, related
- Sun Belt: Acquisition - Miami / Florida - Miami-Area Multifamily Project Trades for $54M, Atlanta, Austin, Dallas, General Project Signal - Phoenix / Arizona - Cross Harbor Scores $78.5M Financing for Tempe Rental Community, Miami, Miami / Florida, Phoenix, Phoenix / Arizona, Refinancing - Phoenix / Arizona - RED Inks Refi on Camelback Office Building, Sun Belt

## Weak Matches Needing Manual Review

- Acquisition - Houston / Texas - Houston Apartment Investor Buys 378-Unit Affordable Housing Community -> Acquisition - Houston / Texas - Houston Apartment Investor Buys 378-Unit Affordable Housing Community (40, relationship_graph.csv)
- Acquisition - Northern Virginia / Virginia - Enverra Acquires 260,000 SF Office Campus in Northern Virginia for $42M -> Acquisition - Northern Virginia / Virginia - Enverra Acquires 260,000 SF Office Campus in Northern Virginia for $42M (40, relationship_graph.csv)
- Acquisition - Other / Unknown - Essex Three-Twelve’s Mitir Patel Represents Buyers in Six Chicago Multifamily Transactions -> Acquisition - Other / Unknown - Essex Three-Twelve’s Mitir Patel Represents Buyers in Six Chicago Multifamily Transactions (40, relationship_graph.csv)
- Advanced Real Estate -> Advanced Real Estate (40, gp_intelligence.csv)
- Advanced Real Estate -> Advanced Real Estate (40, institutional_relationships.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Benefit Street Partners -> Benefit Street Partners (40, deal_pipeline.csv)
- Benefit Street Partners -> Benefit Street Partners (40, gp_intelligence.csv)
- Benefit Street Partners -> Benefit Street Partners (40, institutional_relationships.csv)
- Benefit Street Partners -> Benefit Street Partners (40, relationship_graph.csv)
- Acquisition - Other / Unknown - CBRE Brokers $30M Sale of Multifamily Portfolio in Madison, Wisconsin -> CBRE (60, relationship_graph.csv)
- Riverside / California -> California (60, articles.csv)
- Riverside / California -> California (60, deal_pipeline.csv)
- Riverside / California -> California (60, relationship_graph.csv)
- San Francisco / California -> California (60, articles.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
