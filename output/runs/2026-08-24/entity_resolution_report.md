# Entity Resolution Report

Generated: 2026-08-24 23:22:33

- Total raw entities reviewed: 216
- Total canonical entities created: 70
- Possible duplicate entity groups: 9
- Weak matches needing review: 165
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 144 occurrence(s)
- Marcus & Millichap: 31 occurrence(s)
- Berkadia: 9 occurrence(s)
- CBRE: 9 occurrence(s)
- Fannie Mae: 8 occurrence(s)
- Freddie Mac: 8 occurrence(s)
- Alliance Residential: 6 occurrence(s)
- JPI: 6 occurrence(s)
- Bascom Group: 5 occurrence(s)
- PCCP: 5 occurrence(s)

## Top Canonical Markets

- Los Angeles: 56 occurrence(s)
- Sun Belt: 42 occurrence(s)
- Other / Unknown: 40 occurrence(s)
- California: 20 occurrence(s)
- Unknown: 18 occurrence(s)
- New York: 10 occurrence(s)
- Seattle: 9 occurrence(s)
- Colorado: 8 occurrence(s)
- Louisiana: 8 occurrence(s)
- South Florida: 8 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, berkadia
- CBRE: CBRE, cbre
- California: Acquisition - California - Bascom Acquires Buena Park Apartments as Value-Add Deal, Beverly Hills / California, California, Disposition / Exit - California - Costa Mesa Multifamily Changes Hands for Value-Add Repositioning, Entitlement / Permitting - Beverly Hills / California - Revised look emerges for resi tower at 8844 Burton Way in Beverly Hills
- Fannie Mae: Fannie Mae, JV / Partnership - California - Newmark Arranges Fannie Mae Loan on San Clemente Active-Adult Complex, fannie mae
- Freddie Mac: Freddie Mac, freddie mac
- Los Angeles: Acquisition - Atlanta / Georgia - ParkProperty Acquires 280-Unit Buckhead Apartment Community, Acquisition - Atlanta / Georgia - Saratoga Capital Pays $98.4M at Auction for Atlanta Apartment Community, Acquisition - Los Angeles / California - Marcus & Millichap Brokers $5.3M Sale of Los Angeles Apartment Building, Atlanta / Georgia, BTR / Build-to-Rent - Dallas / Texas - W Properties Mixing BTR and Garden-Style Apartments in Melissa, Dallas / Texas, Development Start - Los Angeles / California - Affordable housing fully framed at 9033 Ramsgate Ave. in Westchester, Disposition / Exit - Los Angeles / California - 49 condos up for sale at 127 N. Madison Ave. in Pasadena, Disposition / Exit - Los Angeles / California - Local Owner-Operator Snags Pico-Robertson Apartment Property, Disposition / Exit - Los Angeles / California - Woodland Hills Country Club, Mayoral debate, and more, Disposition / Exit - Seattle - Kidder Mathews Arranges Sale of Capitol Hill Apartment Building, Entitlement / Permitting - Los Angeles / California - JPI to break ground on 257 apartments at 16911 S. Normandie Ave. in Gardena, Entitlement / Permitting - Other / Unknown - Mixed-use project unwrapped at 3555 S. Overland Ave. in Palms, General Project Signal - Atlanta / Georgia - Atlanta Beltline Advancing 218-Unit Affordable Apartment Project, General Project Signal - Colorado - Newmark Arranges $45.9M in FHA Financing for Two Class A Multifamily Communities in Grand..., General Project Signal - Los Angeles / California - Affordable housing complex slated for 5922 N. Lemp Ave. in North Hollywood, General Project Signal - Los Angeles / California - City Planning Commission approves townhomes + storage facility at 7528 Bellaire Ave. in Su..., JV / Partnership - California - Brixton Capital Launches Multifamily Investment-Management Platform, Los Angeles, Los Angeles / California, Office-to-Residential Conversion - Atlanta / Georgia - JLB Pursuing Buckhead Office-to-Apartments Conversion
- New York: Construction Financing - New York - Newmark Arranges $277M Loan for Urby/Rockpoint JV on Jersey City Apartments, Manhattan, New York, New York City / New York, Refinancing - New York City / New York - Timber Equities Receives $27.5M Loan for Refinancing of Manhattan Apartment Building
- Related Companies: General Project Signal - Miami / Florida - Related Planning Apartments on Site at Fort Lauderdale Office Park, related
- Sun Belt: Acquisition - Miami / Florida - West Palm Beach Developer Buys Lot, Apartments on Way, Acquisition - Phoenix / Arizona - Albany Road Snags Loan for Scottsdale MOB Acquisition, Atlanta, Austin, Construction Financing - Phoenix / Arizona - Princeton Developer Obtains Financing for Phase III of 374-Unit Rental Community, Dallas, Development Start - Miami / Florida - NRP Advancing 312-Unit Port St. Lucie Apartment Venture, JV / Partnership - Miami / Florida - Integra Investments, City of North Miami Begin Preleasing for 342-Unit Mixed-Income Apartm..., Miami, Miami / Florida, Nashville / Tennessee, Phoenix, Phoenix / Arizona, Refinancing - Miami / Florida - Investor Team Scores $53.5M Refi on Doral Center Offices, Sun Belt

## Weak Matches Needing Manual Review

- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, gp_intelligence.csv)
- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, institutional_relationships.csv)
- Acquisition - Baton Rouge / Louisiana - Marcus & Millichap Arranges Sale of Two Louisiana Multifamily Properties Totaling 462 Unit... -> Acquisition - Baton Rouge / Louisiana - Marcus & Millichap Arranges Sale of Two Louisiana Multifamily Properties Totaling 462 Unit... (40, relationship_graph.csv)
- Acquisition - Houston / Texas - Alliance Building Houston-Area Complex Amid Declining Multifamily Construction -> Acquisition - Houston / Texas - Alliance Building Houston-Area Complex Amid Declining Multifamily Construction (40, relationship_graph.csv)
- Acquisition - Other / Unknown - Marcus & Millichap Brokers $20.4M Sale of Chicago Multifamily Property -> Acquisition - Other / Unknown - Marcus & Millichap Brokers $20.4M Sale of Chicago Multifamily Property (40, relationship_graph.csv)
- Acquisition - Washington DC - Bonaventure Acquires Ownership Interest in Chevy Chase MF Development -> Acquisition - Washington DC - Bonaventure Acquires Ownership Interest in Chevy Chase MF Development (40, relationship_graph.csv)
- Alliance Residential -> Alliance Residential (40, deal_pipeline.csv)
- Alliance Residential -> Alliance Residential (40, gp_intelligence.csv)
- Alliance Residential -> Alliance Residential (40, institutional_relationships.csv)
- Alliance Residential -> Alliance Residential (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- AvalonBay -> AvalonBay (40, gp_intelligence.csv)
- AvalonBay -> AvalonBay (40, institutional_relationships.csv)
- BTR / Build-to-Rent - Other / Unknown - Stark Enterprises to Develop 164-Unit Build-to-Rent Community in Grimes, Iowa -> BTR / Build-to-Rent - Other / Unknown - Stark Enterprises to Develop 164-Unit Build-to-Rent Community in Grimes, Iowa (40, relationship_graph.csv)
- Bascom Group -> Bascom Group (40, deal_pipeline.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
