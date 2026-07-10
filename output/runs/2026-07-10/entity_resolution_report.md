# Entity Resolution Report

Generated: 2026-07-10 00:07:04

- Total raw entities reviewed: 282
- Total canonical entities created: 79
- Possible duplicate entity groups: 11
- Weak matches needing review: 202
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 126 occurrence(s)
- JLL: 40 occurrence(s)
- CBRE: 22 occurrence(s)
- Berkadia: 17 occurrence(s)
- AvalonBay: 14 occurrence(s)
- Alliance Residential: 10 occurrence(s)
- Marcus & Millichap: 10 occurrence(s)
- Kennedy Wilson: 9 occurrence(s)
- Freddie Mac: 8 occurrence(s)
- Merchants Capital: 8 occurrence(s)

## Top Canonical Markets

- Sun Belt: 50 occurrence(s)
- Other / Unknown: 48 occurrence(s)
- Los Angeles: 41 occurrence(s)
- New York: 39 occurrence(s)
- California: 30 occurrence(s)
- Unknown: 20 occurrence(s)
- South Florida: 12 occurrence(s)
- Houston / Texas: 7 occurrence(s)
- Virginia: 7 occurrence(s)
- Washington DC: 7 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Acquisition - Virginia - Berkadia Negotiates Sale of 20-Story High-Rise Apartment Tower in Arlington, Virginia, Berkadia, Disposition / Exit - Virginia - Berkadia Arranges Sale and Financing of 270-Unit Multifamily Community in Manassas Virgini..., Refinancing - Sun Belt - Berkadia Arranges $85.4M Refinancing for Two Orlando-Area Multifamily Communities, berkadia
- Brookfield: Brookfield, JV / Partnership - Other / Unknown - Brookfield JV Buys Site For 6,500-Unit Project In Boston Suburbs, brookfield
- CBRE: Acquisition - New York - CBRE Arranges Over $150M in Multifamily Sales, CBRE, cbre
- California: Acquisition - California - Eagle Real Estate, Vistria Group Acquire 402-Unit Apartment Community in Garden Grove, Cal..., Acquisition - California - Orange County Apartment Complex Sells for $133M, California, Disposition / Exit - California - Yorba Linda Parking Lot Sells for Townhome Redevelopment, Entitlement / Permitting - Santa Monica / California - Fresh renderings for mixed-use project at 2716 Ocean Park Blvd. in Santa Monica, JV / Partnership - Riverside / California - C&C Development Opens Affordable Housing in Irvine, Orange County, Riverside / California, San Diego, San Francisco / California, Santa Monica / California
- Fannie Mae: Acquisition - Other / Unknown - Northmarq Arranges Fannie Mae Financing for Lawrence Apartments, Fannie Mae, fannie mae
- Freddie Mac: Freddie Mac, freddie mac
- JLL: JLL, Refinancing - New York City / New York - JLL Arranges $352M Loan for Refinancing of Midtown Manhattan Office Building, Refinancing - Other / Unknown - JLL Arranges $124.6M Refinancing for Luxury Apartment Tower in Chicago, jll
- Kennedy Wilson: Kennedy Wilson, Office-to-Residential Conversion - Los Angeles / California - Kennedy Wilson, Jamison partner on 4K affordable units in LA, Refinancing - New York City / New York - Watermark Lands $105M Refinance for Multifamily Rental Community in Queens, kennedy wilson
- Los Angeles: Acquisition - Atlanta / Georgia - Lion Real Estate Picks Up Atlanta Apartments for $51M, Acquisition - Dallas / Texas - Marcus & Millichap Brokers Sale of 249-Unit Apartment Complex in North Dallas, Acquisition - Los Angeles / California - How Alliance Residential secured 2K apartments in 6 months, Acquisition - Miami / Florida - Avalon Bay Planning Apartments, Retail in South Miami, Acquisition - Miami / Florida - Pembroke Pines Rental Asset Trades for $80.5M, Atlanta / Georgia, Construction Financing - Other / Unknown - Priority Capital Advisory Secures $11.5M Loan for Recapitalization of Wisconsin Multifamil..., Dallas / Texas, Development Start - Dallas / Texas - JVP Begins Work on 110K-SF Office Building at Frisco’s The Mix, Disposition / Exit - Los Angeles / California - 45-Unit Garden Apartment Property Trades in LA’s Palms Neighborhood, Disposition / Exit - New York - Pantzer Acquires Class A Multifamily in Downtown Stamford, General Project Signal - Atlanta / Georgia - Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project, General Project Signal - Los Angeles / California - MMCC Arranges Financing for Northridge Offices, General Project Signal - Miami / Florida - Dezer Advancing Plan for 600 N. Miami Apartment Units, JV / Partnership - California - Foundation Complete For 1523 Harrison Street, Downtown Oakland, Los Angeles, Los Angeles / California, Office-to-Residential Conversion - Los Angeles / California - Koreatown offices at 3700 Wilshire Blvd. to be converted to housing, Office-to-Residential Conversion - Washington DC - GoodHomes Buys Washington DC Hotel with Plans for Multifamily Conversion, Refinancing - California - Slatt Capital Arranges Life Company Loan for Novato Multifamily
- New York: Construction Financing - New York City / New York - Grubb Nabs $377M FiDi Construction Loan: The N.Y. Deal Sheet, JV / Partnership - New York City / New York - Charney, Tavros Begin Leasing 260-Unit Apartment Building in Brooklyn, Manhattan, New York, New York City, New York City / New York, Office-to-Residential Conversion - New York City / New York - One Project's Buckling Beams And Sagging Floors Rattle NYC's 19M SF Conversion Pipeline, Office-to-Residential Conversion - New York City / New York - Structural columns buckle on 21st floor of Manhattan adaptive reuse project, Queens

## Weak Matches Needing Manual Review

- Acquisition - Other / Unknown - $8.6M Acquisition Financing Secured for 88-Unit Charleston-Area Community with Full Tax Ab... -> Acquisition - Other / Unknown - $8.6M Acquisition Financing Secured for 88-Unit Charleston-Area Community with Full Tax Ab... (40, relationship_graph.csv)
- Affinius Capital -> Affinius Capital (40, deal_pipeline.csv)
- Affinius Capital -> Affinius Capital (40, gp_intelligence.csv)
- Affinius Capital -> Affinius Capital (40, institutional_relationships.csv)
- Affinius Capital -> Affinius Capital (40, relationship_graph.csv)
- Alliance Residential -> Alliance Residential (40, deal_pipeline.csv)
- Alliance Residential -> Alliance Residential (40, gp_intelligence.csv)
- Alliance Residential -> Alliance Residential (40, institutional_relationships.csv)
- Alliance Residential -> Alliance Residential (40, relationship_graph.csv)
- Ameris Bank -> Ameris Bank (40, gp_intelligence.csv)
- Ameris Bank -> Ameris Bank (40, institutional_relationships.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Arlington, Virginia -> Arlington, Virginia (40, deal_pipeline.csv)
- Arlington, Virginia -> Arlington, Virginia (40, relationship_graph.csv)
- AvalonBay -> AvalonBay (40, deal_pipeline.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
