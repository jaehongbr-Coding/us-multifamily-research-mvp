# Entity Resolution Report

Generated: 2026-10-14 01:38:10

- Total raw entities reviewed: 225
- Total canonical entities created: 62
- Possible duplicate entity groups: 8
- Weak matches needing review: 173
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 129 occurrence(s)
- Berkadia: 16 occurrence(s)
- CBRE: 16 occurrence(s)
- Walker & Dunlop: 15 occurrence(s)
- Hines: 12 occurrence(s)
- High Street Residential: 10 occurrence(s)
- JLL: 10 occurrence(s)
- IPA: 9 occurrence(s)
- Marcus & Millichap: 9 occurrence(s)
- walker & dunlop: 6 occurrence(s)

## Top Canonical Markets

- Sun Belt: 59 occurrence(s)
- Los Angeles: 47 occurrence(s)
- Other / Unknown: 42 occurrence(s)
- California: 22 occurrence(s)
- Unknown: 17 occurrence(s)
- New York: 14 occurrence(s)
- Seattle: 8 occurrence(s)
- National: 7 occurrence(s)
- South Florida: 6 occurrence(s)
- Colorado: 4 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Acquisition - Miami / Florida - Berkadia Arranges Refis for 3 S. Florida Rental Communities, Berkadia, berkadia
- CBRE: CBRE, Disposition / Exit - San Francisco / California - Andrew Eisenberg Promoted to CBRE San Francisco Peninsula Market Leader, cbre
- California: California, Disposition / Exit - California - Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993, Entitlement / Permitting - San Francisco / California - Duplex Proposed For 4368 23rd Street in Noe Valley, San Francisco, General Project Signal - Colorado - Affordable housing secures financing at 1756 Colorado Blvd. in Pasadena, Orange County, Riverside / California, San Francisco / California
- JLL: JLL, Newport Beach Seniors Communities JLL Capital, Refinancing - California - JLL Arranges $276M Refi for Newport Beach Seniors Communities, jll
- Kennedy Wilson: Construction Financing - New York - Walker & Dunlop Arranges $203M Financing for East Village Multifamily, Construction Financing - New York City / New York - Walker & Dunlop Arranges $203M in Financing for East Village Mixed-Use Multifamily Propert...
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Acquires Luxury Multifamily Rental Community 99 West Paces for $237.8M in Buckhead, Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Acquisition - Other / Unknown - Greenstone Partners Announce $13.6M Acquisition of 84-Unit Orland Park Multifamily Portfol..., Acquisition - Other / Unknown - Kiser Group Brokers Sale of 345-Unit Apartment Community in Blue Island, Illinois, Acquisition - Tampa / Florida - American Landmark Acquires 292-Unit Apartment Complex in Southeast Houston, Atlanta / Georgia, Dallas / Texas, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Entitlement / Permitting - Los Angeles / California - 101 homes approved at 5034 N. Clydebank Ave. in unincorporated Covina, Entitlement / Permitting - Los Angeles / California - New look for Westwood housing complex at 11027 W. Strathmore Dr., Entitlement / Permitting - Los Angeles / California - Warner Center development site showing activity at 6160 Variel Ave., General Project Signal - Dallas / Texas - Leon Capital Provides Equity for 516-Bed Student Housing Project in Binghamton, New York, General Project Signal - Los Angeles / California - The Bloc is on the block, A peek inside the Colburn Center, and more, General Project Signal - National - Annex Group Completes $62.9M Affordable Housing Development in Des Moines, General Project Signal - Other / Unknown - New look for large apartment complex at 444 N. Fair Oaks Ave. in Pasadena, Inland Empire, JV / Partnership - Dallas / Texas - High Street Converts Dallas Offices into 435-Unit Apartment Community, JV / Partnership - Dallas / Texas - High Street Residential Led Joint Venture Breaks Ground on 435-Unit Class A Multifamily Co..., JV / Partnership - Miami / Florida - Development Group Scores Financing for 502-Unit Fort Lauderdale Apartment Complex, JV / Partnership - Other / Unknown - Ryan Cos. Opens Multifamily Project at Former Ford Motor Co. Twin Cities Assembly Plant, JV / Partnership - Riverside / California - Upland Apartments with Value-Add Potential Trade to Limited Partnership, Los Angeles, Los Angeles / California, Refinancing - Los Angeles / California - Century City’s Anderson Towers Refinanced for $550M
- New York: Construction Financing - New York City / New York - Kinsmen Property, SK Development to Build 184 Apartments at 50 Third Avenue, Manhattan, New York, New York City / New York
- Sun Belt: Acquisition - Austin / Texas - BH Properties Affiliate Purchases 346-Unit Leander Multifamily Project, Acquisition - Austin / Texas - ORIX Buys 322-Unit Austin Apartment Community, Atlanta, Austin, Austin / Texas, Dallas, Development Start - Austin / Texas - OHT Partners Announces Groundbreaking on 402-Unit Multifamily Community in Southwest Austi..., Development Start - Phoenix / Arizona - Empire Group Starts Work on $288M Tempe Apartment Community, Development Start - Sun Belt - 5 apartment projects that recently broke ground, General Project Signal - Miami / Florida - Aimco Advancing Luxury Edgewater Apartments, Miami / Florida, Orlando, Phoenix, Phoenix / Arizona, Sun Belt, Tampa, Tampa / Florida

## Weak Matches Needing Manual Review

- Acquisition - Connecticut - Chozick Realty Negotiates $42M Sale of Apartment Complex in Avon, Connecticut -> Acquisition - Connecticut - Chozick Realty Negotiates $42M Sale of Apartment Complex in Avon, Connecticut (40, relationship_graph.csv)
- Acquisition - Seattle - IPA Brokers Sale of Two Multifamily Communities in South Puget Sound Region -> Acquisition - Seattle - IPA Brokers Sale of Two Multifamily Communities in South Puget Sound Region (40, relationship_graph.csv)
- Anderson Real Estate -> Anderson Real Estate (40, gp_intelligence.csv)
- Anderson Real Estate -> Anderson Real Estate (40, institutional_relationships.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Acquisition - Miami / Florida - Berkadia Arranges Refis for 3 S. Florida Rental Communities -> Berkadia (60, relationship_graph.csv)
- Disposition / Exit - San Francisco / California - Andrew Eisenberg Promoted to CBRE San Francisco Peninsula Market Leader -> CBRE (60, relationship_graph.csv)
- Riverside / California -> California (60, articles.csv)
- Riverside / California -> California (60, deal_pipeline.csv)
- Riverside / California -> California (60, relationship_graph.csv)
- San Francisco / California -> California (60, articles.csv)
- San Francisco / California -> California (60, deal_pipeline.csv)
- San Francisco / California -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993 -> California (60, relationship_graph.csv)
- Entitlement / Permitting - San Francisco / California - Duplex Proposed For 4368 23rd Street in Noe Valley, San Francisco -> California (60, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
