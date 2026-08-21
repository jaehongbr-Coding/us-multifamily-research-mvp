# Entity Resolution Report

Generated: 2026-08-21 23:24:04

- Total raw entities reviewed: 244
- Total canonical entities created: 78
- Possible duplicate entity groups: 8
- Weak matches needing review: 197
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 160 occurrence(s)
- Marcus & Millichap: 19 occurrence(s)
- CBRE: 15 occurrence(s)
- Berkadia: 9 occurrence(s)
- PCCP: 9 occurrence(s)
- Fannie Mae: 8 occurrence(s)
- Greystone: 7 occurrence(s)
- JPI: 6 occurrence(s)
- Lincoln Property Company: 6 occurrence(s)
- cushman: 6 occurrence(s)

## Top Canonical Markets

- Los Angeles: 61 occurrence(s)
- Sun Belt: 43 occurrence(s)
- Other / Unknown: 39 occurrence(s)
- California: 35 occurrence(s)
- Unknown: 15 occurrence(s)
- New York: 13 occurrence(s)
- Seattle: 13 occurrence(s)
- Texas: 13 occurrence(s)
- National: 9 occurrence(s)
- Colorado: 8 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, berkadia
- CBRE: Acquisition - Riverside / California - CBRE Brokers $34.5M Sale of Turtle Creek Apartments in Riverside, California, CBRE, Refinancing - Texas - CBRE Arranges Loan for Refinancing of 181-Unit Apartment Complex in San Antonio, cbre
- California: Acquisition - California - Bascom Acquires Buena Park Apartments as Value-Add Deal, Beverly Hills / California, California, Development Start - California - 338-unit affordable housing development underway in Tustin, Disposition / Exit - California - Costa Mesa Multifamily Changes Hands for Value-Add Repositioning, Entitlement / Permitting - Beverly Hills / California - Revised look emerges for resi tower at 8844 Burton Way in Beverly Hills, General Project Signal - California - Michaels Organization Set to Break Ground in Davis, Riverside / California
- Fannie Mae: Fannie Mae, JV / Partnership - California - Newmark Arranges Fannie Mae Loan on San Clemente Active-Adult Complex, fannie mae
- Los Angeles: Acquisition - Atlanta / Georgia - ParkProperty Acquires 280-Unit Buckhead Apartment Community, Acquisition - Atlanta / Georgia - Saratoga Capital Pays $98.4M at Auction for Atlanta Apartment Community, Acquisition - Southeast - Club Studio to Co-Anchor $450M Mixed-Use Development in Frederick, Maryland, Atlanta / Georgia, Dallas / Texas, Development Start - Los Angeles / California - Affordable housing fully framed at 9033 Ramsgate Ave. in Westchester, Development Start - Los Angeles / California - Affordable housing takes shape at 17100 Victory Blvd. in Lake Balboa, Disposition / Exit - Los Angeles / California - 49 condos up for sale at 127 N. Madison Ave. in Pasadena, Disposition / Exit - Los Angeles / California - L.A. County Investment Sales Jump 28% in July Thanks to Multifamily, Disposition / Exit - Los Angeles / California - Local Owner-Operator Snags Pico-Robertson Apartment Property, Entitlement / Permitting - Los Angeles / California - 39 apartments approved at 10535 W. Missouri Ave. in West L.A., Entitlement / Permitting - Los Angeles / California - JPI to break ground on 257 apartments at 16911 S. Normandie Ave. in Gardena, Entitlement / Permitting - Los Angeles / California - Report: L.A. permits 8,800 homes in the first half of 2026, General Project Signal - Atlanta / Georgia - Atlanta Beltline Advancing 218-Unit Affordable Apartment Project, General Project Signal - Atlanta / Georgia - Portman, 908 Group Deliver 674-Bed Student Housing Community Near Florida State University, General Project Signal - California - State announces $236M in bond financing for La Brea Tar Pits revamp, General Project Signal - Colorado - Newmark Arranges $45.9M in FHA Financing for Two Class A Multifamily Communities in Grand..., JV / Partnership - Atlanta / Georgia - Mesirow Pays $132M for Midtown Atlanta Apartment Community, JV / Partnership - California - Brixton Capital Launches Multifamily Investment-Management Platform, JV / Partnership - Dallas / Texas - PCCP, RPM Pick Up 358-Unit Arlington Multifamily Community, Los Angeles, Los Angeles / California, Office-to-Residential Conversion - Atlanta / Georgia - JLB Pursuing Buckhead Office-to-Apartments Conversion
- New York: General Project Signal - New York City / New York - Grocery-Anchored Queens Retail Secures $32M Financing, JV / Partnership - New York - Affinius Capital Lends $177M for Multifamily Asset Buy in New Jersey, Yonkers, New York, New York City / New York, Office-to-Residential Conversion - New York - Cushman & Wakefield Arranges $131M Sale of Apartment Building in West Orange, New Jersey, Queens
- Related Companies: General Project Signal - Miami / Florida - Related Planning Apartments on Site at Fort Lauderdale Office Park, related
- Sun Belt: Acquisition - Miami / Florida - West Palm Beach Developer Buys Lot, Apartments on Way, Acquisition - Phoenix / Arizona - Albany Road Snags Loan for Scottsdale MOB Acquisition, Atlanta, Austin, BTR / Build-to-Rent - Phoenix / Arizona - Porter Kyle Adds New 100-Unit BTR Community to East Valley Portfolio, Construction Financing - Phoenix / Arizona - Princeton Developer Obtains Financing for Phase III of 374-Unit Rental Community, Dallas, Development Start - Miami / Florida - NRP Advancing 312-Unit Port St. Lucie Apartment Venture, Miami / Florida, Nashville / Tennessee, Phoenix, Phoenix / Arizona, Sun Belt

## Weak Matches Needing Manual Review

- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, gp_intelligence.csv)
- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, institutional_relationships.csv)
- Affinius Capital -> Affinius Capital (40, gp_intelligence.csv)
- Affinius Capital -> Affinius Capital (40, institutional_relationships.csv)
- Affordable Apartments McDowell Housing Partners -> Affordable Apartments McDowell Housing Partners (40, gp_intelligence.csv)
- Affordable Apartments McDowell Housing Partners -> Affordable Apartments McDowell Housing Partners (40, institutional_relationships.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Associated Bank -> Associated Bank (40, gp_intelligence.csv)
- Associated Bank -> Associated Bank (40, institutional_relationships.csv)
- AvalonBay -> AvalonBay (40, gp_intelligence.csv)
- AvalonBay -> AvalonBay (40, institutional_relationships.csv)
- Bascom Group -> Bascom Group (40, deal_pipeline.csv)
- Bascom Group -> Bascom Group (40, gp_intelligence.csv)
- Bascom Group -> Bascom Group (40, institutional_relationships.csv)
- Bascom Group -> Bascom Group (40, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
