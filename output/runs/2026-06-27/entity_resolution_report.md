# Entity Resolution Report

Generated: 2026-06-27 00:08:59

- Total raw entities reviewed: 232
- Total canonical entities created: 64
- Possible duplicate entity groups: 8
- Weak matches needing review: 174
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 127 occurrence(s)
- CBRE: 14 occurrence(s)
- Related Companies: 11 occurrence(s)
- Berkadia: 9 occurrence(s)
- JLL: 8 occurrence(s)
- Marcus & Millichap: 8 occurrence(s)
- Alliance Residential: 6 occurrence(s)
- Greystar: 6 occurrence(s)
- Tishman Speyer: 6 occurrence(s)
- Waterton: 6 occurrence(s)

## Top Canonical Markets

- Sun Belt: 46 occurrence(s)
- California: 44 occurrence(s)
- Los Angeles: 36 occurrence(s)
- Other / Unknown: 32 occurrence(s)
- New York: 22 occurrence(s)
- Unknown: 14 occurrence(s)
- South Florida: 10 occurrence(s)
- National: 9 occurrence(s)
- Riverside: 6 occurrence(s)
- Florida: 4 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, Refinancing - Florida - Berkadia Arranges $100.4M Refinancing for Office Campus in Palm Beach Gardens, Florida, berkadia
- CBRE: CBRE, cbre
- California: California, Disposition / Exit - California - Former Bank Branch Positioned as Development Opportunity in Garden Grove Sale, Disposition / Exit - California - Yorba Linda Parking Lot Sells for Townhome Redevelopment, Disposition / Exit - Riverside / California - Elme Communities selloff hits a snag, General Project Signal - California - New-Construction San Diego Apartments Score $53M Bridge Loan, General Project Signal - California - Newsom Signs Bill Putting $11B Housing Bond on November Ballot, JV / Partnership - Riverside / California - C&C Development Opens Affordable Housing in Irvine, JV / Partnership - Riverside / California - C&C Development, Riverside Charitable Corp. Open 60-Unit Affordable Housing Community in I..., Recapitalization - California - PEF Advisors, Freestone Capital Form JV to Recapitalize Affordable Properties, Riverside / California, Santa Monica / California
- JLL: General Project Signal - California - JLL Arranges $252M Financing for Huntington Beach Seniors Project, JLL, jll
- Los Angeles: Acquisition - Atlanta / Georgia - Developer Buys Land Near Charlotte Transit Station, Apartments on Way, Acquisition - Phoenix / Arizona - Tide Equities Sells Phoenix Rental Asset for $41M, Atlanta / Georgia, BTR / Build-to-Rent - Santa Monica / California - Construction goes vertical for mixed-use project at 1902 Wilshire Blvd. in Santa Monica, Construction Financing - Miami / Florida - NADG Lands $120M to Build Rental on Farmland in Palm Beach County, Construction Financing - Sun Belt - S3 Capital Lends $101M on Luxury Resort Project Near Orlando, Dallas / Texas, Disposition / Exit - Riverside / California - REIT's Liquidation Plan Upended After $280M Sale Falls Through, Entitlement / Permitting - California - Affordable housing takes shape at 733 S. Burlington Ave. in Westlake, Entitlement / Permitting - Los Angeles / California - 159 homes slated for 601 Potrero Grande Dr. in Monterey Park, Entitlement / Permitting - Los Angeles / California - Affordable housing under constructiona t 1740 N. Wilton Place in Hollywood, General Project Signal - Austin / Texas - Forman Provides Loan to Kickstart Marble Falls Mixed-Use Project, General Project Signal - Dallas / Texas - Dallas Greenlights $200M Oak Lawn Residential Tower, General Project Signal - Los Angeles / California - 100 rental townhomes deput at 1771 Blake Ave. in Frogtown, General Project Signal - Los Angeles / California - Affordable housing fully-framed at 4129 Centinela Ave. in Del Rey, General Project Signal - Los Angeles / California - Affordable housing on the rise at 1405 S. Broadway in DTLA, JV / Partnership - Other / Unknown - Buccini Pollin, University of Delaware Top Out $75M Multifamily Project in Newark, Los Angeles, Los Angeles / California, Office-to-Residential Conversion - Washington DC - Starwood Quietly Reveals Plans For Conversion In Downtown D.C., Refinancing - Atlanta / Georgia - Dwight Capital Finances $39M Loan for Oregon Multifamily Development
- New York: Entitlement / Permitting - New York City / New York - Rent Freeze Approved On All Stabilized Leases, Delivering On Mamdani Pledge, General Project Signal - New York City / New York - Tishman Speyer’s TS Communities Lines Up Funds for Next Phase of Edgemere Commons, JV / Partnership - New York City / New York - Partnership Completes 153-Unit Affordable Seniors Housing Project in Brooklyn, New York, New York City, New York City / New York, Queens, Refinancing - New York - 22-Property NJ Workforce Portfolio Refinanced for $38M
- Related Companies: Development Start - Miami / Florida - Related Urban Starts Work on $167M S. Miami Affordable Housing Venture, Related California, related
- Sun Belt: Acquisition - Miami / Florida - Waterton Purchases 358-Unit Apartment Community in South Florida for $80.5M, Acquisition - Phoenix / Arizona - Alliance Sells Phoenix Apartments for $81.4M, Atlanta, Austin, Austin / Texas, Dallas, Development Start - Miami / Florida - Developer Begins Work on 476-Unit Delray Beach Rental Community, General Project Signal - Miami / Florida - Miami-Dade County Sells Apartment Site for $10, Miami / Florida, Orlando, Phoenix, Phoenix / Arizona, Sun Belt

## Weak Matches Needing Manual Review

- Acquisition - Other / Unknown - Associated Bank Originates $17.7M Acquisition Loan for Townhome Community in Metro Des Moi... -> Acquisition - Other / Unknown - Associated Bank Originates $17.7M Acquisition Loan for Townhome Community in Metro Des Moi... (40, relationship_graph.csv)
- Acquisition - Other / Unknown - Connect Midwest Multifamily Trends 2026: Navigating Capital Flow & Deal Dynamics -> Acquisition - Other / Unknown - Connect Midwest Multifamily Trends 2026: Navigating Capital Flow & Deal Dynamics (40, relationship_graph.csv)
- Acquisition - Other / Unknown - Marcus & Millichap Arranges $6.6M Sale of Chicago Apartment Building -> Acquisition - Other / Unknown - Marcus & Millichap Arranges $6.6M Sale of Chicago Apartment Building (40, relationship_graph.csv)
- Alliance Residential -> Alliance Residential (40, deal_pipeline.csv)
- Alliance Residential -> Alliance Residential (40, gp_intelligence.csv)
- Alliance Residential -> Alliance Residential (40, institutional_relationships.csv)
- Alliance Residential -> Alliance Residential (40, relationship_graph.csv)
- Ania Management -> Ania Management (40, gp_intelligence.csv)
- Ania Management -> Ania Management (40, institutional_relationships.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Associated Bank -> Associated Bank (40, gp_intelligence.csv)
- Associated Bank -> Associated Bank (40, institutional_relationships.csv)
- Refinancing - Florida - Berkadia Arranges $100.4M Refinancing for Office Campus in Palm Beach Gardens, Florida -> Berkadia (60, relationship_graph.csv)
- Riverside / California -> California (60, articles.csv)
- Riverside / California -> California (60, deal_pipeline.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
