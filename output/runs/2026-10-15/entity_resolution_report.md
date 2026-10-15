# Entity Resolution Report

Generated: 2026-10-15 01:14:31

- Total raw entities reviewed: 248
- Total canonical entities created: 68
- Possible duplicate entity groups: 11
- Weak matches needing review: 176
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 134 occurrence(s)
- Berkadia: 28 occurrence(s)
- Marcus & Millichap: 17 occurrence(s)
- Fannie Mae: 12 occurrence(s)
- Walker & Dunlop: 12 occurrence(s)
- CBRE: 11 occurrence(s)
- JLL: 10 occurrence(s)
- Brookfield: 9 occurrence(s)
- Kennedy Wilson: 8 occurrence(s)
- Hines: 7 occurrence(s)

## Top Canonical Markets

- Other / Unknown: 50 occurrence(s)
- Sun Belt: 49 occurrence(s)
- Los Angeles: 43 occurrence(s)
- New York: 25 occurrence(s)
- California: 23 occurrence(s)
- Unknown: 19 occurrence(s)
- Seattle: 13 occurrence(s)
- National: 9 occurrence(s)
- Colorado: 8 occurrence(s)
- South Florida: 6 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Acquisition - Miami / Florida - Berkadia Arranges Refis for 3 S. Florida Rental Communities, Acquisition - Other / Unknown - Berkadia Arranges Sale of 228-Unit Multifamily Property Near Madison, Wisconsin, Berkadia, Disposition / Exit - Other / Unknown - Wisconsin MF Portfolio Sale, Financing Deal Completed by Berkadia, berkadia
- Brookfield: Brookfield, brookfield
- CBRE: Acquisition - New York City / New York - CBRE Arranges Acquisition Loan for Fort Greene Mixed-Use, CBRE, Fort Greene Mixed-Use CBRE Capital, cbre
- California: California, Disposition / Exit - California - Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993, Disposition / Exit - California - North County Apartment Duo Trades for $37M, Entitlement / Permitting - Colorado - More Pasadena affordable housing in the works at 1976 E. Colorado Blvd., General Project Signal - Colorado - Affordable housing secures financing at 1756 Colorado Blvd. in Pasadena, JV / Partnership - California - 2 San Jose Multifamily Towers Change Hands For Combined $380M, Riverside / California
- Fannie Mae: Fannie Mae, fannie mae
- Freddie Mac: Freddie Mac, General Project Signal - Other / Unknown - Merchants Capital Secures Freddie Mac Forward TEL Loan for Affordable Multifamily Developm..., freddie mac
- JLL: JLL, Newport Beach Seniors Communities JLL Capital, Refinancing - California - JLL Arranges $276M Refi for Newport Beach Seniors Communities, jll
- Kennedy Wilson: Construction Financing - New York - Western New York Affordable Housing Redevelopment Project Opens with 70-Units, Construction Financing - New York City / New York - Walker & Dunlop Arranges $203M Construction Loan for Manhattan Multifamily Project, JV / Partnership - California - Kennedy Wilson Partners with Hulic, Fuyo General Lease on San Jose Apartment Deal, Kennedy Wilson, kennedy wilson
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Atlanta / Georgia, Construction Financing - Los Angeles / California - CrownGuard Capital Provides $15.5M in Financing for Multifamily Repositioning Project in R..., Dallas / Texas, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Disposition / Exit - Seattle - Kidder Mathews Arranges Sale of 45-Unit Suncrest Apartments in Walla Walla Washington for..., Entitlement / Permitting - Los Angeles / California - 101 homes approved at 5034 N. Clydebank Ave. in unincorporated Covina, Entitlement / Permitting - Los Angeles / California - New look for Westwood housing complex at 11027 W. Strathmore Dr., Entitlement / Permitting - Los Angeles / California - Warner Center development site showing activity at 6160 Variel Ave., General Project Signal - Austin / Texas - Teeple Partners Breaks Ground on 312-Unit Multifamily Project in Bryan, Texas, General Project Signal - New York - Rithm Capital Closes Largest RTL Multifamily Securitization to Date, General Project Signal - Other / Unknown - New look for large apartment complex at 444 N. Fair Oaks Ave. in Pasadena, Inland Empire, JV / Partnership - Dallas / Texas - High Street Converts Dallas Offices into 435-Unit Apartment Community, JV / Partnership - Los Angeles / California - Affordable housing takes shape at 327 S. Harbor Blvd. in San Pedro, JV / Partnership - Miami / Florida - Development Group Scores Financing for 502-Unit Fort Lauderdale Apartment Complex, JV / Partnership - Riverside / California - Upland Apartments with Value-Add Potential Trade to Limited Partnership, Los Angeles, Los Angeles / California, Refinancing - Dallas / Texas - Lone Star Funds Scores $110M Refinancing for Two Stafford Rental Communities
- New York: Brooklyn, Manhattan, New York, New York City / New York, Refinancing - New York City / New York - AXA Equitable Provides $103M Recapitalization for Midtown’s Ellington Building

## Weak Matches Needing Manual Review

- Acquisition - Seattle - Cadence Real Estate Advisors Buys 132-Unit Apartment Property in Seattle -> Acquisition - Seattle - Cadence Real Estate Advisors Buys 132-Unit Apartment Property in Seattle (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Avison Young -> Avison Young (40, gp_intelligence.csv)
- Avison Young -> Avison Young (40, institutional_relationships.csv)
- Bank OZK -> Bank OZK (40, gp_intelligence.csv)
- Bank OZK -> Bank OZK (40, institutional_relationships.csv)
- Acquisition - Miami / Florida - Berkadia Arranges Refis for 3 S. Florida Rental Communities -> Berkadia (60, relationship_graph.csv)
- Acquisition - Other / Unknown - Berkadia Arranges Sale of 228-Unit Multifamily Property Near Madison, Wisconsin -> Berkadia (60, relationship_graph.csv)
- Disposition / Exit - Other / Unknown - Wisconsin MF Portfolio Sale, Financing Deal Completed by Berkadia -> Berkadia (60, relationship_graph.csv)
- Fort Greene Mixed-Use CBRE Capital -> CBRE (60, gp_intelligence.csv)
- Fort Greene Mixed-Use CBRE Capital -> CBRE (60, institutional_relationships.csv)
- Acquisition - New York City / New York - CBRE Arranges Acquisition Loan for Fort Greene Mixed-Use -> CBRE (60, relationship_graph.csv)
- Cadence Real Estate Advisors -> Cadence Real Estate Advisors (40, gp_intelligence.csv)
- Cadence Real Estate Advisors -> Cadence Real Estate Advisors (40, institutional_relationships.csv)
- Riverside / California -> California (60, articles.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
