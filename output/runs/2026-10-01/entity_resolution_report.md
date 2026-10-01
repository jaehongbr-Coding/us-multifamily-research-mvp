# Entity Resolution Report

Generated: 2026-10-01 01:50:31

- Total raw entities reviewed: 226
- Total canonical entities created: 63
- Possible duplicate entity groups: 11
- Weak matches needing review: 157
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 125 occurrence(s)
- JLL: 30 occurrence(s)
- Berkadia: 21 occurrence(s)
- Walker & Dunlop: 17 occurrence(s)
- Blackstone: 16 occurrence(s)
- Greystone: 12 occurrence(s)
- Freddie Mac: 11 occurrence(s)
- IPA: 11 occurrence(s)
- Brookfield: 9 occurrence(s)
- Marcus & Millichap: 9 occurrence(s)

## Top Canonical Markets

- Sun Belt: 66 occurrence(s)
- California: 40 occurrence(s)
- Los Angeles: 35 occurrence(s)
- Other / Unknown: 34 occurrence(s)
- New York: 26 occurrence(s)
- South Florida: 12 occurrence(s)
- Unknown: 12 occurrence(s)
- National: 9 occurrence(s)
- Southeast: 7 occurrence(s)
- Denver / Colorado: 6 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, Disposition / Exit - California - Berkadia Arranges Sale of Westchester Apartments at a Three-Year Per-Unit High, berkadia
- Blackstone: Blackstone, Refinancing - California - Blackstone, LBA Land $270M Office Refi in L.A.’s Culver City, blackstone
- Brookfield: Brookfield, brookfield
- California: Acquisition - California - MMCC Arranges Financing for Orange Multifamily Acquisition, California, Disposition / Exit - California - Family Office Acquires Fresno Apartments from Long-Term Owner, Disposition / Exit - California - Institutional Property Advisors Closes $40.5M Multifamily Sale in San Diego County, Disposition / Exit - California - San Ramon Apartments Fetch $78M After 15-Year Hold, General Project Signal - California - WNC Closes on 23rd California-Focused Affordable Housing Fund, JV / Partnership - California - MBK Rental Living Transforms 100-Year-Old Timber School into New Residential Community in..., San Francisco / California
- Freddie Mac: Freddie Mac, freddie mac
- Greystone: Greystone, Office-to-Residential Conversion - Miami / Florida - Greystone Provides $167M Financing for Affordable Housing Tower Development in Miami
- JLL: JLL, jll
- Los Angeles: Acquisition - Atlanta / Georgia - ParkProperty Acquires 280-Unit Buckhead Apartment Community, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Acquisition - Phoenix / Arizona - D.R. Horton Divests of 260-Unit Ascend at Black Canyon Multifamily Property in Phoenix, Atlanta / Georgia, BTR / Build-to-Rent - Phoenix / Arizona - Empire Lands $65.5M Refi on Phoenix BTR Community, Dallas / Texas, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Disposition / Exit - New York City / New York - Long Island City Redevelopment Site Trades to Queens Developer, Entitlement / Permitting - Los Angeles / California - Affordable housing takes shape at 5110 Washington Blvd. in Mid-City, Entitlement / Permitting - Los Angeles / California - Proposed high-rise poised for another step forward at 1000 La Brea Ave., Entitlement / Permitting - San Francisco / California - Preliminary Plans For 770 Golden Gate Avenue, San Francisco, General Project Signal - Florida - Subtext Opens VERVE Orlando an Elevated Student Living Near the University of Central Flor..., General Project Signal - Los Angeles / California - Affordable housing coming to 18444 Plummer St. in Northridge, JV / Partnership - California - Affirmed Housing Breaks Ground on Affordable TOD in La Mesa, JV / Partnership - New York City / New York - Alcion Ventures, Slate Offload 60 East 12th Street for $83M, L.A., Los Angeles, Los Angeles / California, Modular / Construction Innovation - Los Angeles / California - Modular units rise for affordable housing at 1141 N. Vermont Ave. in East Hollywood, Refinancing - Los Angeles / California - Investor Duo Obtains $270M Refi on 387K-SF Culver City Office Property, Refinancing - Miami / Florida - JSB Capital Lands $238M Refi on Doral Apartment Community, Refinancing - Miami / Florida - RIVANI Lands $114.3M Refi on Miami Beach Office/Retail Project, Refinancing - Miami / Florida - Walker & Dunlop Arranges $238M Refinancing for Landmark South Apartments in Doral, Florida, Refinancing - National - GGP Lines Up $400M Loan To Refinance New England's Largest Mall
- New York: Acquisition - New York City / New York - Ariel Property Advisors Negotiates $75M Sale of Two Manhattan Apartment Buildings, Brooklyn, Disposition / Exit - New York City / New York - Arrow Linen Site in Park Slope Sells for Residential Development, Disposition / Exit - New York City / New York - Residential Multifamily Redevelopment Property Trades For $55M in Brooklyn’s Park Slope Ne..., Manhattan, New York, New York City, New York City / New York, Queens
- Related Companies: General Project Signal - Miami / Florida - Related Affiliate Obtains $167M Loan Package for Miami Apartment Community, related

## Weak Matches Needing Manual Review

- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, gp_intelligence.csv)
- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, institutional_relationships.csv)
- America -> America (40, deal_pipeline.csv)
- America -> America (40, relationship_graph.csv)
- Ariel Property Advisors -> Ariel Property Advisors (40, gp_intelligence.csv)
- Ariel Property Advisors -> Ariel Property Advisors (40, institutional_relationships.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Disposition / Exit - California - Berkadia Arranges Sale of Westchester Apartments at a Three-Year Per-Unit High -> Berkadia (60, relationship_graph.csv)
- Refinancing - California - Blackstone, LBA Land $270M Office Refi in L.A.’s Culver City -> Blackstone (60, relationship_graph.csv)
- San Francisco / California -> California (60, articles.csv)
- San Francisco / California -> California (60, deal_pipeline.csv)
- San Francisco / California -> California (60, relationship_graph.csv)
- Acquisition - California - MMCC Arranges Financing for Orange Multifamily Acquisition -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Family Office Acquires Fresno Apartments from Long-Term Owner -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Institutional Property Advisors Closes $40.5M Multifamily Sale in San Diego County -> California (60, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
