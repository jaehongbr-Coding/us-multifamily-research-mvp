# Entity Resolution Report

Generated: 2026-11-06 03:13:54

- Total raw entities reviewed: 226
- Total canonical entities created: 59
- Possible duplicate entity groups: 10
- Weak matches needing review: 158
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 119 occurrence(s)
- JLL: 31 occurrence(s)
- Blackstone: 30 occurrence(s)
- Marcus & Millichap: 19 occurrence(s)
- CBRE: 15 occurrence(s)
- Fannie Mae: 10 occurrence(s)
- Greystone: 10 occurrence(s)
- Berkadia: 7 occurrence(s)
- Hines: 7 occurrence(s)
- AvalonBay: 6 occurrence(s)

## Top Canonical Markets

- Sun Belt: 52 occurrence(s)
- Los Angeles: 49 occurrence(s)
- Other / Unknown: 41 occurrence(s)
- California: 32 occurrence(s)
- National: 21 occurrence(s)
- Unknown: 16 occurrence(s)
- New York: 13 occurrence(s)
- Colorado: 4 occurrence(s)
- South Florida: 4 occurrence(s)
- Tennessee: 4 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, General Project Signal - New York City / New York - Berkadia Closes $219M Loan for Affordable Housing Rehab in Manhattan
- Blackstone: Blackstone, Refinancing - Nashville / Tennessee - Blackstone Provides $310M Bridge Loan for Nashville Mixed-Use Tower, blackstone
- CBRE: CBRE, cbre
- California: California, Disposition / Exit - California - Anaheim Sale is First Closing in Broader Multifamily Portfolio, Disposition / Exit - California - Fourth Sale Closes in Anaheim Multifamily Portfolio, Disposition / Exit - California - HealthCore Pays $130M for Six-Building NorthBay Health MOB Portfolio, Entitlement / Permitting - California - Affordable housing on the rise at 3990 S. Wade. St. in Mar Vista, General Project Signal - California - Affordable housing taking shape at 5749 S. Brynhurst Avenue in Hyde Park, JV / Partnership - California - 377 apartments rise next to Brea Mall, Refinancing - San Francisco / California - Northmarq Arranges $105M Refinance Loan for Apartment Community in Mountain View Californi..., San Francisco / California, Southern California
- Fannie Mae: Fannie Mae, Refinancing - Colorado - Newmark Arranges $24.5M Fannie Mae Refinancing for Lakewood Colorado Apartments, fannie mae
- Freddie Mac: Acquisition - Other / Unknown - Greystone Supplies $47M Freddie Mac Loan on Illinois Multifamily Acquisition, Freddie Mac, freddie mac
- JLL: Acquisition - Other / Unknown - JLL Arranges $25M Sale of FourNorth Apartments in Metro Chicago, BTR / Build-to-Rent - Washington DC - Ari Azarbarzin joins JLL Capital Markets in Washington, D.C., JLL, JV / Partnership - Nashville / Tennessee - JLL Arranges $310M Financing for Landmark Riverfront Mixed-Use Development in Nashville, Refinancing - New York - JLL Arranges $154.2M Loan for Refinancing of Long Island Apartment Community, jll
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - ORIX Acquires Buckhead Apartments for $83M, Acquisition - Salt Lake City / Utah - Veritas Investments, Refound Residential Acquire Three Multifamily Properties in Utah, Atlanta / Georgia, Construction Financing - Other / Unknown - HUD launches ‘express lane’ for LIHTC multifamily construction loans, Dallas / Texas, Development Start - Los Angeles / California - Work begins for La Brea Tar Pits and Page Museum revamp, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Disposition / Exit - Atlanta / Georgia - Perimeter Center Rental Community Goes for $120M, Disposition / Exit - Los Angeles / California - Benedict Canyon Acquires Neighboring West Hollywood Properties, Disposition / Exit - Los Angeles / California - Marcus & Millichap Closes $29.85M Sale and Arranges Financing for Two Multifamily Assets i..., Entitlement / Permitting - Dallas / Texas - Trammell Crow Building 248 McKinney Apartment Units, 3 Hotels, Entitlement / Permitting - Los Angeles / California - Excavation underway for affordable housing at 1248 N. Cherokee Ave. in Hollywood, Entitlement / Permitting - Other / Unknown - Plans Approved For 990 El Camino Real, San Bruno, Entitlement / Permitting - Other / Unknown - Zoning Worksheet Filed for Multifamily Building at 425 W Macarthur Boulevard in Oakland, General Project Signal - Los Angeles / California - 16-story residential tower planned at 8240 Sunset Blvd. in West Hollywood, General Project Signal - Los Angeles / California - One Beverly Hills Reaches Milestones Ahead of Schedule, General Project Signal - Miami / Florida - BTI, Bridge Score $109M for Hollywood’s Bread Building, General Project Signal - Other / Unknown - 123 homes planned at 902 W. Washington Blvd. in University Park, JV / Partnership - Atlanta / Georgia - Morehouse, Spelman Debut $147M Student Housing Project, JV / Partnership - New York - Timberlane Partners Purchases Canopy Apartments in Everett, Washington for $82.7M, Los Angeles, Los Angeles / California, Refinancing - Other / Unknown - Canada Pension Plan Investment Board, Salt Lake City / Utah
- New York: Manhattan, New York, New York City / New York
- Sun Belt: Acquisition - Sun Belt - Comstock Agrees to Purchase 672-Unit Ascher Apartment Towers in Uptown Charlotte, Atlanta, Austin, Charlotte, Dallas, Development Start - Phoenix / Arizona - Leon Multifamily Building 343-Unit N. Phoenix Venture, General Project Signal - Miami / Florida - Terra, Fortune Ink $220M Key Biscayne Condo Financing, General Project Signal - Phoenix / Arizona - Cross Harbor Scores $78.5M Financing for Tempe Rental Community, Miami / Florida, Nashville, Nashville / Tennessee, Phoenix, Phoenix / Arizona, Refinancing - Phoenix / Arizona - RED Inks Refi on Camelback Office Building, Sun Belt

## Weak Matches Needing Manual Review

- Arizona -> Arizona (40, regional_intelligence.csv)
- AvalonBay -> AvalonBay (40, deal_pipeline.csv)
- AvalonBay -> AvalonBay (40, gp_intelligence.csv)
- AvalonBay -> AvalonBay (40, institutional_relationships.csv)
- AvalonBay -> AvalonBay (40, relationship_graph.csv)
- General Project Signal - New York City / New York - Berkadia Closes $219M Loan for Affordable Housing Rehab in Manhattan -> Berkadia (60, relationship_graph.csv)
- Refinancing - Nashville / Tennessee - Blackstone Provides $310M Bridge Loan for Nashville Mixed-Use Tower -> Blackstone (60, relationship_graph.csv)
- Bridge Investment Group -> Bridge Investment Group (40, gp_intelligence.csv)
- Bridge Investment Group -> Bridge Investment Group (40, institutional_relationships.csv)
- San Francisco / California -> California (60, articles.csv)
- San Francisco / California -> California (60, deal_pipeline.csv)
- San Francisco / California -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Anaheim Sale is First Closing in Broader Multifamily Portfolio -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Fourth Sale Closes in Anaheim Multifamily Portfolio -> California (60, relationship_graph.csv)
- Disposition / Exit - California - HealthCore Pays $130M for Six-Building NorthBay Health MOB Portfolio -> California (60, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
