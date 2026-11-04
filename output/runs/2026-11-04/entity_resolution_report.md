# Entity Resolution Report

Generated: 2026-11-04 02:56:40

- Total raw entities reviewed: 246
- Total canonical entities created: 65
- Possible duplicate entity groups: 10
- Weak matches needing review: 175
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 132 occurrence(s)
- JLL: 23 occurrence(s)
- Fannie Mae: 14 occurrence(s)
- Marcus & Millichap: 11 occurrence(s)
- Blackstone: 9 occurrence(s)
- CBRE: 9 occurrence(s)
- Brookfield: 8 occurrence(s)
- Equity Residential: 7 occurrence(s)
- Greystone: 7 occurrence(s)
- Hines: 7 occurrence(s)

## Top Canonical Markets

- Los Angeles: 52 occurrence(s)
- Sun Belt: 52 occurrence(s)
- Other / Unknown: 42 occurrence(s)
- California: 28 occurrence(s)
- New York: 25 occurrence(s)
- Unknown: 18 occurrence(s)
- Seattle: 9 occurrence(s)
- South Florida: 8 occurrence(s)
- National: 5 occurrence(s)
- Georgia: 4 occurrence(s)

## Possible Duplicate Entities

- Blackstone: Blackstone, blackstone
- Brookfield: Brookfield, brookfield
- CBRE: CBRE, cbre
- California: California, Disposition / Exit - California - Anaheim Sale is First Closing in Broader Multifamily Portfolio, Disposition / Exit - California - Fourth Sale Closes in Anaheim Multifamily Portfolio, Disposition / Exit - California - HealthCore Pays $130M for Six-Building NorthBay Health MOB Portfolio, Disposition / Exit - California - Marcus & Millichap Brokers $13.6M Sale of 63-Unit Multifamily Property in Davis California, Entitlement / Permitting - Santa Monica / California - Fresh renderings for Tishman Speyer projects in Downtown Santa Monica, General Project Signal - California - Affordable housing taking shape at 5749 S. Brynhurst Avenue in Hyde Park, JV / Partnership - Riverside / California - Legacy Partners Begins Leasing at Ontario Apartments, Riverside / California, San Francisco / California, Santa Monica / California
- Fannie Mae: Fannie Mae, fannie mae
- Freddie Mac: Freddie Mac, freddie mac
- JLL: Acquisition - New York City / New York - JLL Brokers $23.5M Sale of Mixed-Use Development Site in Brooklyn, JLL, jll
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - ORIX Acquires Buckhead Apartments for $83M, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Atlanta / Georgia, Construction Financing - Other / Unknown - HUD launches ‘express lane’ for LIHTC multifamily construction loans, Development Start - Los Angeles - Muirfield Breaks Ground on Orlando-Area Opportunity Zone Multifamily Development, Development Start - Los Angeles / California - Work begins for La Brea Tar Pits and Page Museum revamp, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Disposition / Exit - Atlanta / Georgia - Perimeter Center Rental Community Goes for $120M, Disposition / Exit - Los Angeles / California - Farallon Capital Acquires 460-Unit Multifamily Community La Vista Apartments in Santa Mari..., Disposition / Exit - Other / Unknown - Northmarq Brokers Sale of Newly Built Class A Multifamily Property in Lawrence Kansas, Disposition / Exit - Seattle - Kidder Mathews Arranges Sale of 45-Unit Multifamily in Walla Walla, Entitlement / Permitting - Los Angeles / California - Housing pitched for 5412 Bellingham Ave. in Valley Village, Entitlement / Permitting - Los Angeles / California - Long Beach ADU boom, L.A.'s low homeownership, and more, General Project Signal - Georgia - ECI Group Launches Residential Pre-Leasing at $60M The Averly Richmond Hill Development in..., General Project Signal - Los Angeles / California - One Beverly Hills Reaches Milestones Ahead of Schedule, General Project Signal - Miami / Florida - BTI, Bridge Score $109M for Hollywood’s Bread Building, General Project Signal - Other / Unknown - Jonathan Rose Companies Announce Major Rehabilitation of Ashtabula Towers Preserving Affor..., General Project Signal - Other / Unknown - Northmarq’s Debt + Equity Team Arranges $26.1M in Financing for Class A Multifamily Commun..., Inland Empire, JV / Partnership - Atlanta / Georgia - Morehouse, Spelman Debut $147M Student Housing Project, JV / Partnership - New York - Brightshore Acquires Newly Built Long Island City Luxury Apartments, JV / Partnership - New York City / New York - Partnership Acquires Student Housing Property in Manhattan’s East Village for $28M, La County, Los Angeles, Los Angeles / California
- New York: Brooklyn, Manhattan, New York, New York City, New York City / New York, Office-to-Residential Conversion - New York City / New York - Metro Loft, David Werner Secure $231M Loan for Midtown East Residential Conversion, Refinancing - New York City / New York - Affinius Capital Provides $226M for Downtown Brooklyn Multifamily Building
- Sun Belt: Acquisition - Miami / Florida - Nuveen Sells South Florida Rental for $53M, Atlanta, Austin, Austin / Texas, Dallas, Development Start - Austin / Texas - ARCTRUST, Edison Equity Teaming Up on 175-Unit Austin-Area 55+ Community, Development Start - Phoenix / Arizona - Leon Multifamily Building 343-Unit N. Phoenix Venture, General Project Signal - Miami / Florida - Terra, Fortune Ink $220M Key Biscayne Condo Financing, General Project Signal - Sun Belt - High Street Delivers 370-Unit Apartment Community in Apex, North Carolina, JV / Partnership - Miami / Florida - Eastham Capital, Bender Cos. Acquire 204-Unit Multifamily Community in Omaha, Miami / Florida, Phoenix, Phoenix / Arizona, Refinancing - Austin / Texas - Walker & Dunlop Arranges $117.3M Refinancing of Texas Apartment Portfolio, Refinancing - Phoenix / Arizona - RED Inks Refi on Camelback Office Building, Sun Belt

## Weak Matches Needing Manual Review

- Acquisition - Other / Unknown - Standard Communities Secures $29.3M Acquisition of Affordable Housing Multifamily Building... -> Acquisition - Other / Unknown - Standard Communities Secures $29.3M Acquisition of Affordable Housing Multifamily Building... (40, relationship_graph.csv)
- Affinius Capital -> Affinius Capital (40, deal_pipeline.csv)
- Affinius Capital -> Affinius Capital (40, gp_intelligence.csv)
- Affinius Capital -> Affinius Capital (40, institutional_relationships.csv)
- Affinius Capital -> Affinius Capital (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Bridge Investment Group -> Bridge Investment Group (40, gp_intelligence.csv)
- Bridge Investment Group -> Bridge Investment Group (40, institutional_relationships.csv)
- Riverside / California -> California (60, articles.csv)
- Riverside / California -> California (60, deal_pipeline.csv)
- Riverside / California -> California (60, relationship_graph.csv)
- San Francisco / California -> California (60, articles.csv)
- Santa Monica / California -> California (60, articles.csv)
- Santa Monica / California -> California (60, deal_pipeline.csv)
- Santa Monica / California -> California (60, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
