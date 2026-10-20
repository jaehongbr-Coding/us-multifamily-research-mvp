# Entity Resolution Report

Generated: 2026-10-20 01:37:05

- Total raw entities reviewed: 195
- Total canonical entities created: 59
- Possible duplicate entity groups: 9
- Weak matches needing review: 148
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 117 occurrence(s)
- JLL: 33 occurrence(s)
- Fannie Mae: 13 occurrence(s)
- Berkadia: 11 occurrence(s)
- Lincoln Property Company: 9 occurrence(s)
- Marcus & Millichap: 9 occurrence(s)
- Hines: 7 occurrence(s)
- Merchants Capital: 5 occurrence(s)
- PCCP: 5 occurrence(s)
- Freddie Mac: 4 occurrence(s)

## Top Canonical Markets

- Los Angeles: 49 occurrence(s)
- Other / Unknown: 44 occurrence(s)
- Sun Belt: 31 occurrence(s)
- California: 28 occurrence(s)
- New York: 21 occurrence(s)
- National: 17 occurrence(s)
- Unknown: 17 occurrence(s)
- South Florida: 6 occurrence(s)
- Texas: 5 occurrence(s)
- Washington DC: 3 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Acquisition - Miami / Florida - Berkadia Arranges Refis for 3 S. Florida Rental Communities, Berkadia, berkadia
- California: California, Construction Financing - California - PCCP Provides $41M Refi on North Park Multifamily, Disposition / Exit - California - Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993, Entitlement / Permitting - San Francisco / California - New Building Permits For 230 Anza Street in Lone Mountain, San Francisco, General Project Signal - Other / Unknown - Fresh renderings for new workforce housing at 315 N. Pasadena Ave., JV / Partnership - California - HSR, Barings Break Ground on 501-Unit Multifamily Project in Redwood City, California, San Francisco / California, Santa Monica / California
- Fannie Mae: Fannie Mae, fannie mae
- Freddie Mac: Freddie Mac, freddie mac
- Greystar: General Project Signal - Other / Unknown - Greystar Opens New 416-Unit Community North of Boston, Greystar
- JLL: Acquisition - Atlanta / Georgia - JLL Brokers Sale of 217-Unit Apartment Building in Hoboken, JLL, Newport Beach Seniors Communities JLL Capital, Refinancing - California - JLL Arranges $276M Refi for Newport Beach Seniors Communities, jll
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Acquisition - Atlanta / Georgia - TruAmerica Acquires 446-Unit Apartment Community in Metro Atlanta, Atlanta / Georgia, Construction Financing - California - Purpose-Built Student Housing Near SDSU Has Financing in Place, Construction Financing - Los Angeles / California - Culver City Mixed-Use Secures $133M Bank OZK Loan, Construction Financing - New York City / New York - Upper East Side Condo Project Lands $52M Construction Loan, Dallas / Texas, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Disposition / Exit - Dallas / Texas - 104 New Apartments Open in Austin for People Exiting Chronic Homelessness, Disposition / Exit - Dallas / Texas - 229-Unit Lawton Multifamily Community Trades Hands, Disposition / Exit - Los Angeles / California - Newly Constructed Palmdale McDonald’s Trades in All-Cash Deal, Entitlement / Permitting - Los Angeles / California - 32 apartments proposed at 806 N. Sweetzer Ave. in Hollywood, Entitlement / Permitting - Los Angeles / California - Rendering vs. Reality: 176 apartments at 2225 Sunset Boulevard in Echo Park, Entitlement / Permitting - New York City / New York - Stimdel Properties Files Plans to Build 612 Apartments in Astoria, Entitlement / Permitting - Santa Monica / California - Southwest Valley Community Plans take a step forward, JV / Partnership - Other / Unknown - Developers land financing for mixed-use project at 11111 Jefferson Blvd. in Culver City, Los Angeles, Los Angeles / California, Operational / Property Management Tech - Atlanta / Georgia - AI Boom, Affordability Drive Rent Gains in a Handful of Apartment Markets, Refinancing - Dallas / Texas - Northmarq Arranges Major Multifamily Refinance in Richardson Texas, Refinancing - Miami / Florida - Little Havana Apartment Owners Land $50.8M Refi, Refinancing - National - A Third of Maturing Multifamily Debt Needs Cash Infusion to Refinance
- New York: General Project Signal - New York - Gilbane, Strada Development Break Ground on Affordable Tower in Castle Hill/Soundview, JV / Partnership - New York City / New York - Partnership Completes $636M Rehabilitation of Two Brooklyn Affordable Housing Communities, Manhattan, New York, New York City, New York City / New York
- Sun Belt: Atlanta, Austin, Dallas, General Project Signal - Miami / Florida - Aimco Advancing Luxury Edgewater Apartments, Miami / Florida, Phoenix, Sun Belt

## Weak Matches Needing Manual Review

- Acquisition - Other / Unknown - Draper and Kramer Acquires 268-Unit Apartment Community in Evanston, Illinois -> Acquisition - Other / Unknown - Draper and Kramer Acquires 268-Unit Apartment Community in Evanston, Illinois (40, relationship_graph.csv)
- Acquisition - Other / Unknown - The Battery Group Has Acquired Multifamily Apartment Community in Indianapolis -> Acquisition - Other / Unknown - The Battery Group Has Acquired Multifamily Apartment Community in Indianapolis (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- BTR / Build-to-Rent - Other / Unknown - Build-to-rent now eligible for Federal Housing Administration financing -> BTR / Build-to-Rent - Other / Unknown - Build-to-rent now eligible for Federal Housing Administration financing (40, relationship_graph.csv)
- Acquisition - Miami / Florida - Berkadia Arranges Refis for 3 S. Florida Rental Communities -> Berkadia (60, relationship_graph.csv)
- Buckhead Investment Partners -> Buckhead Investment Partners (40, gp_intelligence.csv)
- Buckhead Investment Partners -> Buckhead Investment Partners (40, institutional_relationships.csv)
- San Francisco / California -> California (60, articles.csv)
- San Francisco / California -> California (60, deal_pipeline.csv)
- San Francisco / California -> California (60, relationship_graph.csv)
- Santa Monica / California -> California (60, articles.csv)
- Santa Monica / California -> California (60, deal_pipeline.csv)
- Santa Monica / California -> California (60, relationship_graph.csv)
- Construction Financing - California - PCCP Provides $41M Refi on North Park Multifamily -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993 -> California (60, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
