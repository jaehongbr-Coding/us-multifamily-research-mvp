# Entity Resolution Report

Generated: 2026-11-24 06:48:08

- Total raw entities reviewed: 266
- Total canonical entities created: 74
- Possible duplicate entity groups: 8
- Weak matches needing review: 214
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 123 occurrence(s)
- Berkadia: 24 occurrence(s)
- CBRE: 21 occurrence(s)
- UDR: 13 occurrence(s)
- High Street Residential: 12 occurrence(s)
- Lincoln Property Company: 10 occurrence(s)
- JLL: 9 occurrence(s)
- Blackstone: 8 occurrence(s)
- Hines: 7 occurrence(s)
- Benefit Street Partners: 6 occurrence(s)

## Top Canonical Markets

- Sun Belt: 63 occurrence(s)
- Los Angeles: 43 occurrence(s)
- Other / Unknown: 30 occurrence(s)
- California: 24 occurrence(s)
- National: 21 occurrence(s)
- New York: 15 occurrence(s)
- Unknown: 11 occurrence(s)
- Seattle: 9 occurrence(s)
- South Florida: 8 occurrence(s)
- Northern Virginia / Virginia: 6 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Acquisition - Virginia - Berkadia Arranges Sale & Financing of 396-Unit Alexandria Virginia Community, Berkadia, Refinancing - Miami / Florida - Berkadia Secures $34.12M Loan to Refinance 403-Unit Workforce Housing in Kissimmee Florida, berkadia
- Blackstone: Blackstone, blackstone
- CBRE: Acquisition - San Francisco / California - CBRE Negotiates Sale of Inn at Union Square Hotel in San Francisco, CBRE, cbre
- California: California, Disposition / Exit - California - Fourth Sale Closes in Anaheim Multifamily Portfolio, Disposition / Exit - California - Torrance to break ground on World War II Japanese American Incarceration Monument, JV / Partnership - California - American Campus Communities Expands Partnership with UC Irvine, San Francisco / California, Santa Monica / California
- JLL: JLL, Refinancing - Dallas / Texas - JLL Arranges Loan for Refinancing of Mixed-Use Portfolio in Fort Worth, jll
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - ORIX Acquires Buckhead Apartments for $83M, Acquisition - Los Angeles / California - Rob Kane On Lincoln Property Company’s $6B Southern California Development Pipeline, Acquisition - Miami / Florida - Tishman Speyer Adds Dania Beach Rental Asset to Florida Holdings, Acquisition - Other / Unknown - Bonaventure Acquires 274-Unit Apartment Community in Plainfield, Indiana, Acquisition - Texas - Dominium Acquires Land for First San Antonio Affordable Housing Development, Atlanta / Georgia, Construction Financing - Miami / Florida - Namdar Group Lands $345M to Build West Brickell Rental Tower, Construction Financing - New York - East Village Multifamily Secures $203M Construction Financing, Dallas / Texas, Disposition / Exit - Atlanta / Georgia - Perimeter Center Rental Community Goes for $120M, Disposition / Exit - Miami / Florida - Eastwind to Build Westlake Multifamily Community, Entitlement / Permitting - Los Angeles / California - City Council upholds approval of apartments at 2413 Silver Lake Blvd., Entitlement / Permitting - Los Angeles / California - Developers seek bond financing for affordable housing in the Valley, Entitlement / Permitting - Los Angeles / California - Mixed-use project reaches its peak at at 6052 W. Olympic Blvd., Entitlement / Permitting - Santa Monica / California - Santa Monica has new plans for affordable housing next to Downtown Metro stop, Entitlement / Permitting - Southeast - Mixed-use project starts to rise at 3313 Sunset Blvd. in Silver Lake, General Project Signal - Los Angeles / California - Exterior takes shape for $300m Kali Hotel in Inglewood, General Project Signal - Miami / Florida - Namdar Lands $345M Loan To Build Brickell Apartments: The South Florida Deal Sheet, General Project Signal - National - New plan for housing at 4600 Wilshire Blvd., JV / Partnership - Atlanta / Georgia - Morehouse, Spelman Debut $147M Student Housing Project, JV / Partnership - California - Work Gets Started on Carlsbad Village Mixed-Use Project, JV / Partnership - Miami / Florida - Fort Lauderdale JV Scores $285M Refi for 42-Story Apartment Tower, JV / Partnership - Northern Virginia / Virginia - Blackfin, JSB Capital Buy Northern Virginia Apartments for $69M, JV / Partnership - Northern Virginia / Virginia - REIT Sells 400-Unit Arlandria Apartment Community For $69M, Los Angeles, Los Angeles / California, Office-to-Residential Conversion - Los Angeles / California - 405 ExpressLanes, Metro ridership, and more, Refinancing - Sun Belt - Santander Bank Provides $34M Refi for Orlando-Area Workforce Housing
- New York: Construction Financing - New York City / New York - Partnership Receives $305M in Construction Financing for Manhattan Multifamily Project, New York, New York City, New York City / New York, Refinancing - New York City / New York - JP Morgan Supplies $90M Refi for Murray Hill Multifamily Tower
- Sun Belt: Acquisition - Austin / Texas - Jackson Square Spins Off 280-Unit Pflugerville Rental Property, Atlanta, Austin, Austin / Texas, Construction Financing - Miami / Florida - SCALE Lending Issues $345M Construction Loan for Multifamily Project in Miami’s Brickell N..., Dallas, General Project Signal - Phoenix / Arizona - Cross Harbor Scores $78.5M Financing for Tempe Rental Community, JV / Partnership - Phoenix / Arizona - High Street Residential Joint Venture Complete Scottsdale Luxury Apartment Project, JV / Partnership - Phoenix / Arizona - Weidner Apartment Homes Spends $91M on Denver Apartment Property, Miami, Miami / Florida, Orlando, Phoenix, Phoenix / Arizona, Sun Belt

## Weak Matches Needing Manual Review

- Acquisition - National - Gantry Secures $16M for Saint Ann Missouri Luxury Multifamily Redevelopment -> Acquisition - National - Gantry Secures $16M for Saint Ann Missouri Luxury Multifamily Redevelopment (40, relationship_graph.csv)
- America -> America (40, deal_pipeline.csv)
- America -> America (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Benefit Street Partners -> Benefit Street Partners (40, deal_pipeline.csv)
- Benefit Street Partners -> Benefit Street Partners (40, gp_intelligence.csv)
- Benefit Street Partners -> Benefit Street Partners (40, institutional_relationships.csv)
- Benefit Street Partners -> Benefit Street Partners (40, relationship_graph.csv)
- Acquisition - Virginia - Berkadia Arranges Sale & Financing of 396-Unit Alexandria Virginia Community -> Berkadia (60, relationship_graph.csv)
- Refinancing - Miami / Florida - Berkadia Secures $34.12M Loan to Refinance 403-Unit Workforce Housing in Kissimmee Florida -> Berkadia (60, relationship_graph.csv)
- Acquisition - San Francisco / California - CBRE Negotiates Sale of Inn at Union Square Hotel in San Francisco -> CBRE (60, relationship_graph.csv)
- CIM Group -> CIM Group (40, deal_pipeline.csv)
- CIM Group -> CIM Group (40, gp_intelligence.csv)
- CIM Group -> CIM Group (40, institutional_relationships.csv)
- CIM Group -> CIM Group (40, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
