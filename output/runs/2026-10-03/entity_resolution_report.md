# Entity Resolution Report

Generated: 2026-10-03 01:46:40

- Total raw entities reviewed: 264
- Total canonical entities created: 71
- Possible duplicate entity groups: 11
- Weak matches needing review: 193
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 135 occurrence(s)
- JLL: 31 occurrence(s)
- Marcus & Millichap: 21 occurrence(s)
- Fannie Mae: 16 occurrence(s)
- Berkadia: 15 occurrence(s)
- Walker & Dunlop: 15 occurrence(s)
- Brookfield: 10 occurrence(s)
- Greystone: 7 occurrence(s)
- IPA: 6 occurrence(s)
- JPI: 6 occurrence(s)

## Top Canonical Markets

- Los Angeles: 62 occurrence(s)
- Sun Belt: 59 occurrence(s)
- California: 39 occurrence(s)
- Other / Unknown: 34 occurrence(s)
- Unknown: 13 occurrence(s)
- New York: 11 occurrence(s)
- Florida: 8 occurrence(s)
- South Florida: 8 occurrence(s)
- Southeast: 7 occurrence(s)
- Connecticut: 6 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, Courtesy Berkadia Madison Realty Capital, Disposition / Exit - California - Berkadia Arranges $78M Sale of 200-Unit Multifamily Apartment Community in San Ramon Calif..., berkadia
- Brookfield: Brookfield, Construction Financing - California - Apollo Provides $131M Construction Loan for Brookfield’s California Logistics Center, brookfield
- CBRE: CBRE, cbre
- California: Acquisition - California - Jonathan Rose Companies Acquires Affordable Housing Community in Santa Cruz California, Acquisition - California - MMCC Arranges Financing for Orange Multifamily Acquisition, California, Orange County, Riverside / California, San Francisco / California, Southern California
- Fannie Mae: Fannie Mae, fannie mae
- Freddie Mac: Freddie Mac, freddie mac
- JLL: General Project Signal - Salt Lake City / Utah - JLL Arranges Equity Placement for 217-Unit Multifamily Development in Bluffdale, Utah, JLL, Newport Beach Seniors Communities JLL Capital, Refinancing - California - Bank of America, JLL Provide $276M Refi for SoCal Senior Housing, Refinancing - California - JLL Arranges $276M Refi for Newport Beach Seniors Communities, jll
- Los Angeles: Acquisition - Atlanta / Georgia - ParkProperty Acquires 280-Unit Buckhead Apartment Community, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Acquisition - Houston / Texas - How United Apartment Group plans to hit 50k units under management, Acquisition - Los Angeles / California - Parklet proposed at 8th and Western in Koreatown, Acquisition - Riverside / California - American Landmark Apartments Acquires 350-Unit Multifamily Community in Dallas-Fort Worth, Atlanta / Georgia, BTR / Build-to-Rent - Phoenix / Arizona - Empire Lands $65.5M Refi on Phoenix BTR Community, Construction Financing - Dallas / Texas - JPI Secures Land, Construction Loan for Dallas Mixed-Income Rental Community, Dallas / Texas, Development Start - Dallas / Texas - KAI Build, Revive Capital to Transform Former 7UP Headquarters in Metro St. Louis into Apa..., Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Disposition / Exit - Florida - Newmark Arranges Sale and Financing of 280-Unit Ascend Waterleigh Village in Orlando Metro, Disposition / Exit - Los Angeles / California - Marcus & Millichap Arranges $5.89M Sale of 41-Unit Multifamily Property in North Hollywood..., Disposition / Exit - Los Angeles / California - North Hollywood Apartments Trade to Locally Based LLC, Entitlement / Permitting - California - SoLa Impact score $93M financing package for housing at 252 W. Imperial Highway, Entitlement / Permitting - Los Angeles / California - Affordable housing takes shape at 5110 Washington Blvd. in Mid-City, Entitlement / Permitting - Los Angeles / California - Proposed high-rise poised for another step forward at 1000 La Brea Ave., Entitlement / Permitting - San Francisco / California - Preliminary Plans For 770 Golden Gate Avenue, San Francisco, Entitlement / Permitting - Texas - Alamo Heights Apartment Owners Eyeing Major Addition, General Project Signal - Los Angeles / California - KeyBank Provides $92.9M in Financing for Affordable Housing Development in Los Angeles, General Project Signal - Los Angeles / California - KeyBank Provides $93M Financing for South LA Affordable, JV / Partnership - Dallas / Texas - Partnership Acquires 322-Unit Apartment Community in Denton, Texas, L.A., Los Angeles, Los Angeles / California, Recapitalization - Los Angeles / California - Cityview, PCCP Joint Venture Buys L.A. Apartments for $76M, Refinancing - Miami / Florida - JSB Capital Lands $238M Refi on Doral Apartment Community, Refinancing - Nashville / Tennessee - Helaba Provides $105M Construction Takeout Loan on Nashville Apartments, Refinancing - Other / Unknown - Madison Realty Capital Supplies $127M Refi for Fort Lauderdale Development, Salt Lake City / Utah
- New York: Brooklyn, Development Start - New York City / New York - Charney Companies, Tavros Break Ground on Fifth Gowanus Development, New York, New York City / New York, Refinancing - New York - Olnick Organization Refinances Harlem Apartments for $171M
- Related Companies: General Project Signal - Miami / Florida - Related Affiliate Obtains $167M Loan Package for Miami Apartment Community, related

## Weak Matches Needing Manual Review

- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, gp_intelligence.csv)
- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, institutional_relationships.csv)
- Acquisition - Connecticut - NEPCG Negotiates $6.1M Sale of Apartment Complex in New Haven, Connecticut -> Acquisition - Connecticut - NEPCG Negotiates $6.1M Sale of Apartment Complex in New Haven, Connecticut (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Courtesy Berkadia Madison Realty Capital -> Berkadia (60, gp_intelligence.csv)
- Courtesy Berkadia Madison Realty Capital -> Berkadia (60, institutional_relationships.csv)
- Disposition / Exit - California - Berkadia Arranges $78M Sale of 200-Unit Multifamily Apartment Community in San Ramon Calif... -> Berkadia (60, relationship_graph.csv)
- Construction Financing - California - Apollo Provides $131M Construction Loan for Brookfield’s California Logistics Center -> Brookfield (60, relationship_graph.csv)
- Riverside / California -> California (60, articles.csv)
- Riverside / California -> California (60, deal_pipeline.csv)
- Riverside / California -> California (60, relationship_graph.csv)
- San Francisco / California -> California (60, articles.csv)
- San Francisco / California -> California (60, deal_pipeline.csv)
- San Francisco / California -> California (60, relationship_graph.csv)
- Acquisition - California - Jonathan Rose Companies Acquires Affordable Housing Community in Santa Cruz California -> California (60, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
