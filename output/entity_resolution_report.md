# Entity Resolution Report

Generated: 2026-11-05 03:13:42

- Total raw entities reviewed: 241
- Total canonical entities created: 66
- Possible duplicate entity groups: 11
- Weak matches needing review: 169
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 136 occurrence(s)
- JLL: 36 occurrence(s)
- CBRE: 21 occurrence(s)
- Marcus & Millichap: 20 occurrence(s)
- Blackstone: 17 occurrence(s)
- Fannie Mae: 15 occurrence(s)
- Berkadia: 7 occurrence(s)
- Greystone: 7 occurrence(s)
- Hines: 7 occurrence(s)
- UDR: 7 occurrence(s)

## Top Canonical Markets

- Los Angeles: 58 occurrence(s)
- Other / Unknown: 48 occurrence(s)
- Sun Belt: 43 occurrence(s)
- California: 28 occurrence(s)
- New York: 26 occurrence(s)
- Unknown: 21 occurrence(s)
- Southeast: 9 occurrence(s)
- Nevada: 8 occurrence(s)
- Washington DC: 6 occurrence(s)
- Colorado: 4 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, Construction Financing - New York City / New York - Berkadia Provides $219M to Rehab Rangel Houses in New York City
- Blackstone: Blackstone, blackstone
- Brookfield: Brookfield, Refinancing - Los Angeles / California - Brookfield Gives Up DTLA's Beaudry Apartment Tower, brookfield
- CBRE: Acquisition - Other / Unknown - CBRE Brokers Sale of 540-Unit Multifamily Portfolio in Metro Des Moines, CBRE, cbre
- California: California, Disposition / Exit - California - Anaheim Sale is First Closing in Broader Multifamily Portfolio, Disposition / Exit - California - Fourth Sale Closes in Anaheim Multifamily Portfolio, Disposition / Exit - California - HealthCore Pays $130M for Six-Building NorthBay Health MOB Portfolio, General Project Signal - California - Affordable housing taking shape at 5749 S. Brynhurst Avenue in Hyde Park, JV / Partnership - California - 377 apartments rise next to Brea Mall, Refinancing - San Francisco / California - Northmarq Arranges $105M Refinance Loan for Apartment Community in Mountain View Californi..., San Francisco / California, Southern California
- Fannie Mae: Fannie Mae, General Project Signal - Other / Unknown - Northmarq Provides $26.1M in Fannie Mae Financing for Foxmoor Apartments in Sioux Falls, Refinancing - Colorado - Newmark Arranges $24.5M Fannie Mae Refinancing for Lakewood Colorado Apartments, fannie mae
- Freddie Mac: Freddie Mac, freddie mac
- JLL: BTR / Build-to-Rent - Washington DC - Ari Azarbarzin joins JLL Capital Markets in Washington, D.C., JLL, JV / Partnership - Nashville / Tennessee - JLL Arranges $310M Financing for Landmark Riverfront Mixed-Use Development in Nashville, Refinancing - New York - JLL Arranges Refi for Mixed-Use Residential on Long Island’s South Shore, South Shore JLL Capital, jll
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - ORIX Acquires Buckhead Apartments for $83M, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Atlanta / Georgia, Construction Financing - Other / Unknown - HUD launches ‘express lane’ for LIHTC multifamily construction loans, Development Start - Los Angeles / California - Work begins for La Brea Tar Pits and Page Museum revamp, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Disposition / Exit - Atlanta / Georgia - Perimeter Center Rental Community Goes for $120M, Disposition / Exit - Los Angeles / California - Benedict Canyon Acquires Neighboring West Hollywood Properties, Disposition / Exit - Los Angeles / California - Marcus & Millichap Closes $29.85M Sale and Arranges Financing for Two Multifamily Assets i..., Entitlement / Permitting - Los Angeles / California - Housing pitched for 5412 Bellingham Ave. in Valley Village, Entitlement / Permitting - Other / Unknown - Plans Approved For 990 El Camino Real, San Bruno, General Project Signal - Los Angeles / California - 16-story residential tower planned at 8240 Sunset Blvd. in West Hollywood, General Project Signal - Los Angeles / California - One Beverly Hills Reaches Milestones Ahead of Schedule, General Project Signal - Miami / Florida - BTI, Bridge Score $109M for Hollywood’s Bread Building, General Project Signal - Other / Unknown - 123 homes planned at 902 W. Washington Blvd. in University Park, General Project Signal - Southeast - McCormack Baron Salazar, Baltimore City Secure Financing for $398M Affordable Housing Rede..., JV / Partnership - Atlanta / Georgia - Morehouse, Spelman Debut $147M Student Housing Project, Las Vegas, Las Vegas / Nevada, Los Angeles, Los Angeles / California, Refinancing - Las Vegas / Nevada - Bascom Group Obtains $30.8M Refinancing for Multifamily Property in Las Vegas
- New York: Brooklyn, Manhattan, New York, New York City, New York City / New York, Office-to-Residential Conversion - New York City / New York - Metro Loft, David Werner Secure $231M Loan for Midtown East Residential Conversion, Office-to-Residential Conversion - New York City / New York - Northwind Group Provides $231M Construction Loan for Office-to-Residential Conversion Proj..., Refinancing - New York City / New York - Affinius Lends $226M on Newly Completed Brooklyn Rental Tower

## Weak Matches Needing Manual Review

- Acquisition - Other / Unknown - Northmarq Arranges $17M Sale, $14M Acquisition Financing for Omaha MF -> Acquisition - Other / Unknown - Northmarq Arranges $17M Sale, $14M Acquisition Financing for Omaha MF (40, relationship_graph.csv)
- Affinius Capital -> Affinius Capital (40, deal_pipeline.csv)
- Affinius Capital -> Affinius Capital (40, gp_intelligence.csv)
- Affinius Capital -> Affinius Capital (40, institutional_relationships.csv)
- Affinius Capital -> Affinius Capital (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Bascom Group -> Bascom Group (40, deal_pipeline.csv)
- Bascom Group -> Bascom Group (40, gp_intelligence.csv)
- Bascom Group -> Bascom Group (40, institutional_relationships.csv)
- Bascom Group -> Bascom Group (40, relationship_graph.csv)
- Construction Financing - New York City / New York - Berkadia Provides $219M to Rehab Rangel Houses in New York City -> Berkadia (60, relationship_graph.csv)
- Bridge Investment Group -> Bridge Investment Group (40, gp_intelligence.csv)
- Bridge Investment Group -> Bridge Investment Group (40, institutional_relationships.csv)
- Refinancing - Los Angeles / California - Brookfield Gives Up DTLA's Beaudry Apartment Tower -> Brookfield (60, relationship_graph.csv)
- Acquisition - Other / Unknown - CBRE Brokers Sale of 540-Unit Multifamily Portfolio in Metro Des Moines -> CBRE (60, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
