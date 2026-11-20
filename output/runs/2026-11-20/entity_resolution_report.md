# Entity Resolution Report

Generated: 2026-11-20 03:53:39

- Total raw entities reviewed: 214
- Total canonical entities created: 55
- Possible duplicate entity groups: 8
- Weak matches needing review: 159
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 116 occurrence(s)
- CBRE: 15 occurrence(s)
- Kennedy Wilson: 15 occurrence(s)
- Marcus & Millichap: 11 occurrence(s)
- Benefit Street Partners: 10 occurrence(s)
- Freddie Mac: 10 occurrence(s)
- Walker & Dunlop: 9 occurrence(s)
- Blackstone: 8 occurrence(s)
- Hines: 7 occurrence(s)
- Merchants Capital: 7 occurrence(s)

## Top Canonical Markets

- Los Angeles: 52 occurrence(s)
- Sun Belt: 49 occurrence(s)
- Other / Unknown: 36 occurrence(s)
- California: 19 occurrence(s)
- New York: 14 occurrence(s)
- Unknown: 13 occurrence(s)
- Houston / Texas: 6 occurrence(s)
- South Florida: 6 occurrence(s)
- Florida: 5 occurrence(s)
- National: 5 occurrence(s)

## Possible Duplicate Entities

- Blackstone: Blackstone, blackstone
- CBRE: CBRE, Disposition / Exit - New York - CBRE Arranges $45.6M Sale of Newly Constructed 97-Unit Luxury Multifamily Property in West..., cbre
- California: Acquisition - California - Advanced Real Estate Buys Casitas Apartments in Ontario, California for $56.2M, California, Disposition / Exit - California - Anaheim Sale is First Closing in Broader Multifamily Portfolio, Disposition / Exit - California - Fourth Sale Closes in Anaheim Multifamily Portfolio, JV / Partnership - California - American Campus Communities Expands Partnership with UC Irvine, San Francisco / California
- Freddie Mac: Freddie Mac, freddie mac
- Kennedy Wilson: Construction Financing - Atlanta / Georgia - Kennedy Wilson Breaks Ground on Luxury Multifamily in Atlanta Metro, Kennedy Wilson, Refinancing - New York - Walker & Dunlop Arranges $270M Refi for Journal Square Apartments, kennedy wilson
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - ORIX Acquires Buckhead Apartments for $83M, Atlanta / Georgia, Construction Financing - Las Vegas / Nevada - Bain Capital Joint Venture Secures $94M for Las Vegas Luxury Multifamily Senior Developmen..., Construction Financing - Miami / Florida - Work Underway on 311-Unit Oakland Park Apartment Building, Development Start - Atlanta / Georgia - Work Underway on 33-Story Charlotte Mixed-Use Development, Development Start - Virginia - 3 apartment projects broke ground last week, Disposition / Exit - Atlanta / Georgia - Perimeter Center Rental Community Goes for $120M, Disposition / Exit - Los Angeles / California - 269 homes to replace nursery at 7639 Topanga Canyon Blvd. in Canoga Park, Disposition / Exit - Other / Unknown - Institutional Property Advisors Brokers Sale of 599-Unit Multifamily Property in Portland..., Entitlement / Permitting - Los Angeles - Multifamily housing unwrapped at 4429 S. Vermont Ave. in South L.A., Entitlement / Permitting - Los Angeles / California - Affordable housing underway at 6908 Baird Ave. in Reseda, Entitlement / Permitting - Other / Unknown - Fresh renderings for infill housing at 511 S. Oak Knoll Ave. in Pasadena, Entitlement / Permitting - Other / Unknown - New plan for housing at 452 N. Los Robles Ave. in Pasadena, Entitlement / Permitting - Southeast - Mixed-use project starts to rise at 3313 Sunset Blvd. in Silver Lake, General Project Signal - Atlanta / Georgia - Evolve, Blue Heron Building Clayton Multifamily Community, General Project Signal - Los Angeles / California - Los Angeles Ranks 5th in the Nation for Number of Apartment Units Under Construction, General Project Signal - Miami / Florida - 13th Floor, ANF Complete $89M Hallandale Beach Rental Community, JV / Partnership - Atlanta / Georgia - Morehouse, Spelman Debut $147M Student Housing Project, JV / Partnership - Los Angeles / California - 'Graffiti towers' no more: Oceanwide Plaza is officially cleaned up, JV / Partnership - Miami / Florida - Fort Lauderdale JV Scores $285M Refi for 42-Story Apartment Tower, L.A., Las Vegas, Las Vegas / Nevada, Los Angeles, Los Angeles / California, Refinancing - Florida - Walker & Dunlop Arranges $285M Refinancing for Fort Lauderdale Luxury Multifamily Tower
- New York: Disposition / Exit - New York City / New York - Astoria Apartment Complex Trades for $41M, New York, New York City / New York, Queens
- Sun Belt: Acquisition - Austin / Texas - Marcus & Millichap Arranges $25.8M Sale of Indianapolis Multifamily Portfolio, Acquisition - Austin / Texas - Subtext Expands Student Housing Portfolio with Acquisitions in Austin and Reno, Atlanta, Austin, Austin / Texas, Charlotte, Construction Financing - Miami / Florida - Centennial Bank Lends $51M to Expand Miami-Dade Nursing Home, Dallas, General Project Signal - Phoenix / Arizona - Cross Harbor Scores $78.5M Financing for Tempe Rental Community, General Project Signal - Sun Belt - Merchants Capital Provides $15.5M Financing for Charlotte Affordable Housing Project, Miami, Miami / Florida, Phoenix, Phoenix / Arizona, Sun Belt

## Weak Matches Needing Manual Review

- Acquisition - Houston / Texas - Colliers Brokers Sale of 365-Unit Apartment Community in Katy, Texas -> Acquisition - Houston / Texas - Colliers Brokers Sale of 365-Unit Apartment Community in Katy, Texas (40, relationship_graph.csv)
- Acquisition - Northern Virginia / Virginia - JBG Smith Affiliate Leads $52M NoVA Apartment Buy With Amazon Financing -> Acquisition - Northern Virginia / Virginia - JBG Smith Affiliate Leads $52M NoVA Apartment Buy With Amazon Financing (40, relationship_graph.csv)
- Acquisition - Seattle - Bell Partners Spends $149M on MF Property in Issaquah, Washington -> Acquisition - Seattle - Bell Partners Spends $149M on MF Property in Issaquah, Washington (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Bain Capital Joint Venture -> Bain Capital Joint Venture (40, gp_intelligence.csv)
- Bain Capital Joint Venture -> Bain Capital Joint Venture (40, institutional_relationships.csv)
- Benefit Street Partners -> Benefit Street Partners (40, deal_pipeline.csv)
- Benefit Street Partners -> Benefit Street Partners (40, gp_intelligence.csv)
- Benefit Street Partners -> Benefit Street Partners (40, institutional_relationships.csv)
- Benefit Street Partners -> Benefit Street Partners (40, relationship_graph.csv)
- Disposition / Exit - New York - CBRE Arranges $45.6M Sale of Newly Constructed 97-Unit Luxury Multifamily Property in West... -> CBRE (60, relationship_graph.csv)
- San Francisco / California -> California (60, articles.csv)
- Acquisition - California - Advanced Real Estate Buys Casitas Apartments in Ontario, California for $56.2M -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Anaheim Sale is First Closing in Broader Multifamily Portfolio -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Fourth Sale Closes in Anaheim Multifamily Portfolio -> California (60, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
