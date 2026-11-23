# Entity Resolution Report

Generated: 2026-11-23 03:32:02

- Total raw entities reviewed: 212
- Total canonical entities created: 50
- Possible duplicate entity groups: 7
- Weak matches needing review: 165
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 122 occurrence(s)
- CBRE: 20 occurrence(s)
- JLL: 14 occurrence(s)
- Blackstone: 8 occurrence(s)
- Bascom Group: 7 occurrence(s)
- Hines: 7 occurrence(s)
- Marcus & Millichap: 7 occurrence(s)
- Benefit Street Partners: 6 occurrence(s)
- Tishman Speyer: 6 occurrence(s)
- northmarq: 6 occurrence(s)

## Top Canonical Markets

- Los Angeles: 55 occurrence(s)
- Sun Belt: 51 occurrence(s)
- Other / Unknown: 32 occurrence(s)
- National: 19 occurrence(s)
- California: 17 occurrence(s)
- New York: 12 occurrence(s)
- Unknown: 12 occurrence(s)
- South Florida: 8 occurrence(s)
- Florida: 5 occurrence(s)
- Seattle: 5 occurrence(s)

## Possible Duplicate Entities

- Blackstone: Blackstone, blackstone
- CBRE: CBRE, Disposition / Exit - Other / Unknown - CBRE Arranges Two Property 540-Unit Multifamily Portfolio Sale in Des Moines Suburb, cbre
- California: California, Disposition / Exit - California - Fourth Sale Closes in Anaheim Multifamily Portfolio, JV / Partnership - California - American Campus Communities Expands Partnership with UC Irvine, Riverside / California
- JLL: JLL, Office-to-Residential Conversion - Other / Unknown - JLL Brokers $31.3M Sale of Boutique Apartment Building in Chicago, Refinancing - Riverside / California - JLL Arranges $104M Financing for Uptown Multifamily Portfolio, jll
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - ORIX Acquires Buckhead Apartments for $83M, Acquisition - Dallas / Texas - Bascom Group Acquires 370-Unit Workforce Housing Property in North Dallas, Acquisition - Dallas / Texas - Machine Investment Group Buys 490-Unit Apartment Community in North Dallas, Acquisition - Miami / Florida - Tishman Speyer Adds Dania Beach Rental Asset to Florida Holdings, Acquisition - Other / Unknown - FPA Multifamily Purchases 599-Unit Property in Portland, Acquisition - Seattle - FPA Multifamily Picks Up 599-Unit MF Community in Portland, Atlanta / Georgia, Construction Financing - Miami / Florida - Work Underway on 311-Unit Oakland Park Apartment Building, Dallas / Texas, Development Start - National - Inland, Reuter Walton Break Ground on 342-Unit Citywalk Apartments in Rochester, Minnesota, Development Start - New York City / New York - Vacant Since 2012 Fire, East Flatbush Site Will Yield 134 New Apartments, Disposition / Exit - Atlanta / Georgia - Perimeter Center Rental Community Goes for $120M, Disposition / Exit - Los Angeles / California - 269 homes to replace nursery at 7639 Topanga Canyon Blvd. in Canoga Park, Disposition / Exit - Los Angeles / California - Advanced Real Estate Acquires Ontario California Multifamily Property for $56M, Disposition / Exit - Miami / Florida - Eastwind to Build Westlake Multifamily Community, Entitlement / Permitting - Los Angeles / California - City Council upholds approval of apartments at 2413 Silver Lake Blvd., Entitlement / Permitting - Los Angeles / California - Developers seek bond financing for affordable housing in the Valley, Entitlement / Permitting - Los Angeles / California - Mixed-use project reaches its peak at at 6052 W. Olympic Blvd., Entitlement / Permitting - Other / Unknown - Fresh renderings for infill housing at 511 S. Oak Knoll Ave. in Pasadena, Entitlement / Permitting - Other / Unknown - New plan for housing at 452 N. Los Robles Ave. in Pasadena, Entitlement / Permitting - Southeast - Mixed-use project starts to rise at 3313 Sunset Blvd. in Silver Lake, General Project Signal - Atlanta / Georgia - Atlantic Cos. Tops Out 278-Unit Apartment Community in Chattanooga, General Project Signal - National - New plan for housing at 4600 Wilshire Blvd., JV / Partnership - Atlanta / Georgia - Morehouse, Spelman Debut $147M Student Housing Project, JV / Partnership - California - Work Gets Started on Carlsbad Village Mixed-Use Project, JV / Partnership - Miami / Florida - Fort Lauderdale JV Scores $285M Refi for 42-Story Apartment Tower, JV / Partnership - National - Inland National Development with Reuter Walton Development Joint Venture Break Ground on M..., Los Angeles, Los Angeles / California, Office-to-Residential Conversion - Los Angeles / California - 405 ExpressLanes, Metro ridership, and more, Refinancing - Salt Lake City / Utah - Northmarq Arranges $25M for Salt Lake City Multifamily Asset Refinance, Salt Lake City, Salt Lake City / Utah
- New York: Brooklyn, Disposition / Exit - New York - Hudson County Luxury Multifamily Trades for $46M, Manhattan, New York, New York City / New York
- Sun Belt: Acquisition - Austin / Texas - Jackson Square Closes out Texas Multifamily Asset Ownership with $37M Sale in Austin Metro, Acquisition - Austin / Texas - Jackson Square Spins Off 280-Unit Pflugerville Rental Property, Atlanta, Austin, Austin / Texas, Construction Financing - Miami / Florida - Centennial Bank Lends $51M to Expand Miami-Dade Nursing Home, Dallas, General Project Signal - Phoenix / Arizona - Cross Harbor Scores $78.5M Financing for Tempe Rental Community, Miami, Miami / Florida, Phoenix, Phoenix / Arizona, Sun Belt

## Weak Matches Needing Manual Review

- Acquisition - Northern Virginia / Virginia - JBG Smith Affiliate Leads $52M NoVA Apartment Buy With Amazon Financing -> Acquisition - Northern Virginia / Virginia - JBG Smith Affiliate Leads $52M NoVA Apartment Buy With Amazon Financing (40, relationship_graph.csv)
- Advanced Real Estate -> Advanced Real Estate (40, gp_intelligence.csv)
- Advanced Real Estate -> Advanced Real Estate (40, institutional_relationships.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Bascom Group -> Bascom Group (40, deal_pipeline.csv)
- Bascom Group -> Bascom Group (40, gp_intelligence.csv)
- Bascom Group -> Bascom Group (40, institutional_relationships.csv)
- Bascom Group -> Bascom Group (40, relationship_graph.csv)
- Benefit Street Partners -> Benefit Street Partners (40, deal_pipeline.csv)
- Benefit Street Partners -> Benefit Street Partners (40, gp_intelligence.csv)
- Benefit Street Partners -> Benefit Street Partners (40, institutional_relationships.csv)
- Benefit Street Partners -> Benefit Street Partners (40, relationship_graph.csv)
- Disposition / Exit - Other / Unknown - CBRE Arranges Two Property 540-Unit Multifamily Portfolio Sale in Des Moines Suburb -> CBRE (60, relationship_graph.csv)
- CIM Group -> CIM Group (40, deal_pipeline.csv)
- CIM Group -> CIM Group (40, gp_intelligence.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
