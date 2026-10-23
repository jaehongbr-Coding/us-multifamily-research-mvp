# Entity Resolution Report

Generated: 2026-10-23 01:16:04

- Total raw entities reviewed: 200
- Total canonical entities created: 56
- Possible duplicate entity groups: 8
- Weak matches needing review: 155
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 118 occurrence(s)
- JLL: 32 occurrence(s)
- Hines: 12 occurrence(s)
- Marcus & Millichap: 10 occurrence(s)
- Berkadia: 9 occurrence(s)
- Bascom Group: 8 occurrence(s)
- Blackstone: 8 occurrence(s)
- Affinius Capital: 6 occurrence(s)
- CIM Group: 6 occurrence(s)
- PCCP: 6 occurrence(s)

## Top Canonical Markets

- Los Angeles: 54 occurrence(s)
- California: 48 occurrence(s)
- Other / Unknown: 35 occurrence(s)
- Sun Belt: 26 occurrence(s)
- Unknown: 12 occurrence(s)
- Washington DC: 9 occurrence(s)
- South Florida: 6 occurrence(s)
- New York: 5 occurrence(s)
- Seattle: 5 occurrence(s)
- Colorado: 4 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Acquisition - Miami / Florida - Berkadia Arranges Refis for 3 S. Florida Rental Communities, Berkadia, berkadia
- Blackstone: Blackstone, General Project Signal - Seattle - 6 Blackstone multifamily properties move to servicing, blackstone
- California: Acquisition - Colorado - Broe Group Makes First SoCal Multifamily Acquisition in San Diego, Acquisition - San Francisco / California - Hamilton Zanze Sells 196-Unit Apartment Community in Virgina Beach, California, Disposition / Exit - California - Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993, Disposition / Exit - California - Anaheim Sale is First Closing in Broader Multifamily Portfolio, General Project Signal - California - Affordable housing under construction at 12461 Louise Ave. in Del Rey, General Project Signal - California - How Standard Communities builds workforce rentals in California for under $500,000, General Project Signal - California - Senior affordable housing underway at 233 N. Second Ave. in Covina, JV / Partnership - California - Oberndorf, Bascom Snag Value-Add Opportunity in San Jose, JV / Partnership - California - Partnership Buys Museum Park Apartments in San Jose, California for $53.1M, San Francisco / California, Santa Monica / California
- Fannie Mae: Fannie Mae, fannie mae
- JLL: Acquisition - Florida - JLL Arranges $64M Sale of Office Park in Boca Raton, Florida, General Project Signal - Los Angeles / California - JLL Arranges $50M Bridge Loan for Thousand Oaks R&D and Office Campus, JLL, Newport Beach Seniors Communities JLL Capital, Refinancing - California - JLL Arranges $276M Refi for Newport Beach Seniors Communities, jll
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Atlanta / Georgia, BTR / Build-to-Rent - California - Sacramento Build-for Rent Property Lands $53M Refinancing, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Disposition / Exit - Los Angeles / California - Metro breaks ground on Vermont bus rapid transit line, Entitlement / Permitting - Los Angeles / California - Developer plans high-rise apartments at 6409 Sunset Blvd. in Hollywood, Entitlement / Permitting - Los Angeles / California - Expansion of apartment complex at 6007 Sunset survives appeal, General Project Signal - Los Angeles / California - New supportive housing opens at 8209 Sepulveda Blvd. in the Valley, General Project Signal - Salt Lake City / Utah - Affordable Housing Multifamily Project Advances in Salt Lake City Utah, General Project Signal - San Francisco / California - Lurie Advances Plan for Freedom West 2.0; Would Bring 2,400 Apartments to Western Addition, JV / Partnership - Atlanta / Georgia - Morehouse, Spelman Debut $147M Student Housing Project, JV / Partnership - Los Angeles / California - Partnership Acquires 358-Unit Apartment Community in Arlington, Los Angeles, Los Angeles / California, Office-to-Residential Conversion - Los Angeles / California - New master plan for L.A. General Hospital campus gets key approval, Office-to-Residential Conversion - Santa Monica / California - Santa Monica releases draft plan for airport park conversion, Office-to-Residential Conversion - Washington DC - Carr Properties Plans Office-to-Residential Multifamily Redevelopment Project in Washingto..., Refinancing - Georgia - Newmark Launches Bridge Lending Program, Makes $35M Loan for Georgia Multi Asset, Refinancing - Los Angeles / California - Northmarq Arranges $96M Refi for 1,461-Unit SoCal Portfolio, Refinancing - Miami / Florida - Little Havana Apartment Owners Land $50.8M Refi, Salt Lake City / Utah
- New York: JV / Partnership - New York - SJP Partnership Tops Out Construction on Jersey City Apartments, New York
- Sun Belt: Atlanta, Austin, Dallas, General Project Signal - Miami / Florida - Aimco Advancing Luxury Edgewater Apartments, General Project Signal - Phoenix / Arizona - Thompson Thrift Breaks Ground on 273-Unit Luxury Multifamily Community in Fishers, Indiana, Miami / Florida, Phoenix, Phoenix / Arizona, Sun Belt

## Weak Matches Needing Manual Review

- Acquisition - Other / Unknown - Marcus & Millichap Negotiates $4.9M Sale of Boston Apartment Portfolio -> Acquisition - Other / Unknown - Marcus & Millichap Negotiates $4.9M Sale of Boston Apartment Portfolio (40, relationship_graph.csv)
- Affinius Capital -> Affinius Capital (40, deal_pipeline.csv)
- Affinius Capital -> Affinius Capital (40, gp_intelligence.csv)
- Affinius Capital -> Affinius Capital (40, institutional_relationships.csv)
- Affinius Capital -> Affinius Capital (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Arlington, Virginia -> Arlington, Virginia (40, deal_pipeline.csv)
- Arlington, Virginia -> Arlington, Virginia (40, relationship_graph.csv)
- Bascom Group -> Bascom Group (40, deal_pipeline.csv)
- Bascom Group -> Bascom Group (40, gp_intelligence.csv)
- Bascom Group -> Bascom Group (40, institutional_relationships.csv)
- Bascom Group -> Bascom Group (40, relationship_graph.csv)
- Acquisition - Miami / Florida - Berkadia Arranges Refis for 3 S. Florida Rental Communities -> Berkadia (60, relationship_graph.csv)
- General Project Signal - Seattle - 6 Blackstone multifamily properties move to servicing -> Blackstone (60, relationship_graph.csv)
- CIM Group -> CIM Group (40, deal_pipeline.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
