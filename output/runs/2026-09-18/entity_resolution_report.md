# Entity Resolution Report

Generated: 2026-09-18 01:04:53

- Total raw entities reviewed: 238
- Total canonical entities created: 68
- Possible duplicate entity groups: 11
- Weak matches needing review: 174
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 152 occurrence(s)
- JLL: 21 occurrence(s)
- Berkadia: 16 occurrence(s)
- CBRE: 16 occurrence(s)
- Freddie Mac: 14 occurrence(s)
- Avison Young: 12 occurrence(s)
- Marcus & Millichap: 12 occurrence(s)
- Brookfield: 9 occurrence(s)
- Fannie Mae: 8 occurrence(s)
- IPA: 7 occurrence(s)

## Top Canonical Markets

- Los Angeles: 59 occurrence(s)
- Sun Belt: 55 occurrence(s)
- Other / Unknown: 36 occurrence(s)
- New York: 29 occurrence(s)
- California: 23 occurrence(s)
- National: 18 occurrence(s)
- Unknown: 13 occurrence(s)
- South Florida: 12 occurrence(s)
- Texas: 9 occurrence(s)
- Denver / Colorado: 6 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, berkadia
- Brookfield: Brookfield, brookfield
- CBRE: CBRE, Disposition / Exit - Seattle - CBRE Facilitates $85M Sale of Beaverton Apartment Complex, cbre
- California: Acquisition - California - MMCC Arranges Financing for Orange Multifamily Acquisition, Acquisition - California - Tishman Speyer Acquires 376-Unit Anaheim Rental Community, California, Disposition / Exit - California - Private Investor Snags Brea Offices for $28M, General Project Signal - California - WNC Closes on 23rd California-Focused Affordable Housing Fund, General Project Signal - San Francisco / California - Construction Underway For Alexan Icon, South San Francisco, San Francisco / California
- Fannie Mae: Fannie Mae, General Project Signal - New York City / New York - Avison Young Arranges $115M Fannie Mae DUS loan for Rockrose, fannie mae
- Freddie Mac: Freddie Mac, freddie mac
- JLL: JLL, jll
- Kennedy Wilson: General Project Signal - New York City / New York - Wells Fargo Lends $115M for 301-Unit Multifamily Residential Community with Affordable Uni..., Refinancing - New York City / New York - Wells Fargo Refis Long Island City Apartments With $115M Fannie Mae Loan
- Los Angeles: Acquisition - Atlanta / Georgia - ParkProperty Acquires 280-Unit Buckhead Apartment Community, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Acquisition - Atlanta / Georgia - Saratoga Capital Pays $98.4M at Auction for Atlanta Apartment Community, Acquisition - Los Angeles / California - Interra Realty Brokers $19.2M Sale of Chicago Apartment Building, Atlanta / Georgia, BTR / Build-to-Rent - National - Connect Media Presents the Second Annual ApartmentBuildings.com 100, Development Start - Los Angeles / California - Affordable housing tops out at 10953 Whipple St. in Toluca Lake, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Disposition / Exit - Los Angeles / California - Marcus & Millichap Arranges $6.04M Sale of 31-Unit Multifamily Property in Los Angeles, Entitlement / Permitting - Los Angeles / California - Affordable housing proposed at 12508 W. Pacific Ave. in Mar Vista, Entitlement / Permitting - Los Angeles / California - Apartments slated for 3648 S. Empire Dr. in Palms, Entitlement / Permitting - Los Angeles / California - L.A. County Supes approve apartments at 7914 Broadway Ave. in West Whittier, Entitlement / Permitting - Los Angeles / California - USC School of Cinematic Arts plans expansion at 625 W. 32nd St., Entitlement / Permitting - National - Multifamily starts and completions both fall again in August, Entitlement / Permitting - San Francisco / California - Plans Refiled for 395 3rd Street in SoMa, San Francisco, General Project Signal - Austin / Texas - Target to Add Austin-Area Store, General Project Signal - Miami / Florida - Developer Launches Investor Offering for 465-Unit Boynton Beach Rental Community, General Project Signal - Miami / Florida - Pinnacle Secures Financing for Fort Lauderdale Affordable Sr. Housing, General Project Signal - New York - Vango Development Launches Leasing at Third Rutherford-Area Property, General Project Signal - Texas - Embrey to Raze Alamo Heights Rental Units, to Build 296 New Ones, JV / Partnership - Los Angeles / California - Affordable housing completed at 1408 W. 162nd St. in South L.A., Los Angeles, Los Angeles / California, Office-to-Residential Conversion - Atlanta / Georgia - JLB Pursuing Buckhead Office-to-Apartments Conversion, Refinancing - Los Angeles / California - Northmarq Secures $29.3M Refinancing for Dining, Entertainment Center in Los Angeles, Refinancing - Miami / Florida - Rich Properties Snags $38.5M Refi for West Palm Beach Rental Asset
- New York: Acquisition - New York City / New York - Borough Developers Closes on $84M Sale of Downtown Brooklyn Development Site, Brooklyn, Entitlement / Permitting - New York - Ruben Cos. Says It Can't Sell, Finance Navy Yard Multifamily Project, New York, New York City / New York, Queens

## Weak Matches Needing Manual Review

- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, gp_intelligence.csv)
- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, institutional_relationships.csv)
- Acquisition - Northern Virginia / Virginia - Bell Partners Acquires 500+ Apartment Homes in Silicon Valley and Northern Virginia -> Acquisition - Northern Virginia / Virginia - Bell Partners Acquires 500+ Apartment Homes in Silicon Valley and Northern Virginia (40, relationship_graph.csv)
- Acquisition - Washington DC - Goldman Sachs Pays $147M for DC Apartment Building -> Acquisition - Washington DC - Goldman Sachs Pays $147M for DC Apartment Building (40, relationship_graph.csv)
- Affinius Capital -> Affinius Capital (40, gp_intelligence.csv)
- Affinius Capital -> Affinius Capital (40, institutional_relationships.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Avison Young -> Avison Young (40, deal_pipeline.csv)
- Avison Young -> Avison Young (40, gp_intelligence.csv)
- Avison Young -> Avison Young (40, institutional_relationships.csv)
- Avison Young -> Avison Young (40, relationship_graph.csv)
- BTR / Build-to-Rent - Southeast - Trilogy Obtains Construction Loan for 172-Unit Build-to-Rent Project in Huntsville -> BTR / Build-to-Rent - Southeast - Trilogy Obtains Construction Loan for 172-Unit Build-to-Rent Project in Huntsville (40, relationship_graph.csv)
- Bell Partners -> Bell Partners (40, gp_intelligence.csv)
- Bell Partners -> Bell Partners (40, institutional_relationships.csv)
- BridgeCity Capital -> BridgeCity Capital (40, gp_intelligence.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
