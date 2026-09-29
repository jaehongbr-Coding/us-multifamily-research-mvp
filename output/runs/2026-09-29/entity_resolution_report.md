# Entity Resolution Report

Generated: 2026-09-29 02:30:18

- Total raw entities reviewed: 234
- Total canonical entities created: 69
- Possible duplicate entity groups: 10
- Weak matches needing review: 177
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 136 occurrence(s)
- JLL: 23 occurrence(s)
- Marcus & Millichap: 12 occurrence(s)
- Walker & Dunlop: 12 occurrence(s)
- Berkadia: 9 occurrence(s)
- Blackstone: 9 occurrence(s)
- IPA: 9 occurrence(s)
- Brookfield: 8 occurrence(s)
- Freddie Mac: 8 occurrence(s)
- Carmel Partners: 7 occurrence(s)

## Top Canonical Markets

- Sun Belt: 67 occurrence(s)
- Other / Unknown: 43 occurrence(s)
- Los Angeles: 30 occurrence(s)
- California: 26 occurrence(s)
- Unknown: 18 occurrence(s)
- New York: 16 occurrence(s)
- South Florida: 12 occurrence(s)
- Washington DC: 10 occurrence(s)
- National: 6 occurrence(s)
- Seattle: 5 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, berkadia
- Blackstone: Blackstone, blackstone
- Brookfield: Brookfield, brookfield
- California: Acquisition - California - Keech Properties Buys Sunsweet Apartments in Silicon Valley for $45M, Acquisition - California - MMCC Arranges Financing for Orange Multifamily Acquisition, Acquisition - California - Tishman Speyer Acquires 376-Unit Anaheim Rental Community, California, Entitlement / Permitting - Southeast - More design tweaks for infill housing at 810 N. Marengo Ave. in Pasadena, General Project Signal - California - WNC Closes on 23rd California-Focused Affordable Housing Fund, Refinancing - San Francisco / California - Northmarq’s Debt + Equity Team Arranges $51.14M Refinancing for 167-Unit Senior Living Cen..., San Francisco / California
- Freddie Mac: Freddie Mac, freddie mac
- JLL: JLL, jll
- Los Angeles: Acquisition - Atlanta / Georgia - ParkProperty Acquires 280-Unit Buckhead Apartment Community, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Acquisition - Atlanta / Georgia - Saratoga Capital Pays $98.4M at Auction for Atlanta Apartment Community, Acquisition - California - LaSalle Acquires 482-Bed Student Housing Community Near San Jose State University, Acquisition - Dallas / Texas - Bader Picks Up 228-Unit Dallas Apartment Community, Acquisition - New York City / New York - Charney Cos. Buys 100,000 SF Commercial Building in Brooklyn, Plans Redevelopment, Acquisition - Other / Unknown - Becovic Residential Acquires Historic Andersonville Property, Atlanta / Georgia, Dallas / Texas, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Entitlement / Permitting - Las Vegas / Nevada - Another LAX people mover delay, Brightline faces financial troubles, and more, General Project Signal - Miami / Florida - BTI Partners Opens 362-Unit Residential Tower in Hollywood, Florida, General Project Signal - Miami / Florida - Developer Launches Investor Offering for 465-Unit Boynton Beach Rental Community, JV / Partnership - National - Negro Leagues Baseball Museum, Grayson Capital Announce Construction Team for New Museum,..., Las Vegas / Nevada, Los Angeles, Los Angeles / California, Modular / Construction Innovation - Los Angeles / California - Modular units rise for affordable housing at 1141 N. Vermont Ave. in East Hollywood, Office-to-Residential Conversion - Other / Unknown - Plans Filed for 155-Unit Office-to-Apartment Conversion in Boston, Refinancing - Los Angeles / California - Investor Duo Obtains $270M Refi on 387K-SF Culver City Office Property, Refinancing - Miami / Florida - JSB Capital Lands $238M Refi on Doral Apartment Community, Refinancing - Miami / Florida - RIVANI Lands $114.3M Refi on Miami Beach Office/Retail Project, Refinancing - Phoenix / Arizona - Carmel Picks Up Second Denver Rental Asset This Month
- New York: Development Start - New York City / New York - In Construction Lending, It’s a Good Time to Be the Right Borrower, New York, New York City, New York City / New York, Refinancing - New York City / New York - Benchmark Real Estate Receives $44.5M Loan for Refinancing of Manhattan Apartment Building
- Related Companies: Development Start - Other / Unknown - Ann Arbor Housing Commission and Related Midwest Break Ground on The Adeline an Affordable..., related
- Sun Belt: Atlanta, Austin, Austin / Texas, Construction Financing - Phoenix / Arizona - Mavik Loans $229M in Construction Financing for Tempe Multifamily, Dallas, Development Start - Miami / Florida - Rilea Group Starts Work on 300-Unit Wynwood Rental Community, Disposition / Exit - Miami / Florida - TA Realty Pays $105M for Wellington Rental Community, Disposition / Exit - Phoenix / Arizona - N. Phoenix Apartments Trade for $58.7M, Entitlement / Permitting - Austin / Texas - Austin Developer Greenlit to Build Apartment Units at Former School Site, Entitlement / Permitting - Phoenix / Arizona - Development Team Pursuing 376-Unit Tempe Apartment Venture, General Project Signal - Phoenix / Arizona - Mesa Expected to Okay $3B Legacy Park Project, Miami, Miami / Florida, Phoenix, Phoenix / Arizona, Refinancing - Miami / Florida - Walker & Dunlop Arranges $238M Refinance for Luxury Miami Multifamily Community, Sun Belt

## Weak Matches Needing Manual Review

- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, gp_intelligence.csv)
- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, institutional_relationships.csv)
- Acquisition - Texas - Marcus & Millichap Brokers Sale of 214-Unit Apartment Complex in Killeen, Texas -> Acquisition - Texas - Marcus & Millichap Brokers Sale of 214-Unit Apartment Complex in Killeen, Texas (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- BTR / Build-to-Rent - Other / Unknown - Onyx+East Opens 23-Unit Build-to-Rent Community in Columbus, Ohio -> BTR / Build-to-Rent - Other / Unknown - Onyx+East Opens 23-Unit Build-to-Rent Community in Columbus, Ohio (40, relationship_graph.csv)
- Becovic Residential -> Becovic Residential (40, gp_intelligence.csv)
- Becovic Residential -> Becovic Residential (40, institutional_relationships.csv)
- CIM Group -> CIM Group (40, deal_pipeline.csv)
- CIM Group -> CIM Group (40, gp_intelligence.csv)
- CIM Group -> CIM Group (40, institutional_relationships.csv)
- CIM Group -> CIM Group (40, relationship_graph.csv)
- San Francisco / California -> California (60, articles.csv)
- San Francisco / California -> California (60, deal_pipeline.csv)
- San Francisco / California -> California (60, relationship_graph.csv)
- Acquisition - California - Keech Properties Buys Sunsweet Apartments in Silicon Valley for $45M -> California (60, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
