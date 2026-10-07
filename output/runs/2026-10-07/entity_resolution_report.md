# Entity Resolution Report

Generated: 2026-10-07 02:09:07

- Total raw entities reviewed: 227
- Total canonical entities created: 65
- Possible duplicate entity groups: 9
- Weak matches needing review: 172
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 135 occurrence(s)
- Fannie Mae: 25 occurrence(s)
- JLL: 23 occurrence(s)
- Marcus & Millichap: 18 occurrence(s)
- Berkadia: 9 occurrence(s)
- CBRE: 9 occurrence(s)
- Greystone: 7 occurrence(s)
- Walker & Dunlop: 7 occurrence(s)
- IPA: 6 occurrence(s)
- Lincoln Property Company: 6 occurrence(s)

## Top Canonical Markets

- California: 46 occurrence(s)
- Other / Unknown: 46 occurrence(s)
- Sun Belt: 44 occurrence(s)
- Los Angeles: 29 occurrence(s)
- Unknown: 18 occurrence(s)
- New York: 10 occurrence(s)
- National: 9 occurrence(s)
- Southeast: 7 occurrence(s)
- Houston / Texas: 6 occurrence(s)
- South Florida: 6 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, berkadia
- CBRE: CBRE, Refinancing - New York City / New York - CBRE Arranges Financing for Rent-Stabilized Midwood Multifamily, cbre
- California: Acquisition - California - Jonathan Rose Cos. Acquires Affordable Housing Community in Santa Cruz, California, Acquisition - California - Jonathan Rose Makes Second Acquisition in Santa Cruz, Acquisition - San Francisco / California - Marcus & Millichap Brokers $6.3M Sale of San Francisco Multifamily Portfolio, Beverly Hills / California, California, Disposition / Exit - California - Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993, Disposition / Exit - California - Marcus & Millichap Arranges $7.1M Sale of 32-Unit Multifamily Property in Anaheim Californ..., Entitlement / Permitting - Beverly Hills / California - Mixed-use project proposed at 177 S. Robertson Blvd. in Beverly Hills, Entitlement / Permitting - San Francisco / California - New Building Permits Issued For Mission Bay Block 4 East, San Francisco, Entitlement / Permitting - Santa Monica / California - Fresh imagery for proposed housing complex at 1238 Lincoln Blvd. in Santa Monica, General Project Signal - Santa Monica / California - Design tweaks for affordable housing at 1238 7th St. in Santa Monica, Refinancing - California - El Dorado Hills Office Complex Refinanced within Tight Timeframe, San Francisco / California, Santa Monica / California
- Fannie Mae: Fannie Mae, fannie mae
- JLL: Downtown Residential Conversion JLL Capital, JLL, Newport Beach Seniors Communities JLL Capital, Refinancing - California - JLL Arranges $276M Refi for Newport Beach Seniors Communities, Refinancing - Southeast - JLL Arranges $53M Refinancing for Apartment Community in Huntsville, jll
- Los Angeles: Acquisition - Atlanta / Georgia - ParkProperty Acquires 280-Unit Buckhead Apartment Community, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Acquisition - Houston / Texas - How United Apartment Group plans to hit 50,000 units under management, Acquisition - Other / Unknown - Landmark Properties Expands Presence in Philadelphia with Delivery of The Mark Philadelphi..., Acquisition - Virginia - 5 multifamily deals you may have missed last week, Atlanta / Georgia, BTR / Build-to-Rent - Phoenix / Arizona - Empire Lands $65.5M Refi on Phoenix BTR Community, Construction Financing - Los Angeles / California - Construction loan issued for affordable housing at 400 Centinela Ave. in Inglewood, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Disposition / Exit - Los Angeles / California - North Hollywood Apartments Trade to Locally Based LLC, Disposition / Exit - Los Angeles / California - Speed cams coming soon, RAND Corporation reports on Santa Monica, and more, Disposition / Exit - Other / Unknown - Marcus & Millichap Brokers $31.9M Sale of the Largest Private Market-Rate Apartment Portfo..., Entitlement / Permitting - California - SoLa Impact score $93M financing package for housing at 252 W. Imperial Highway, JV / Partnership - Miami / Florida - Development Group Scores Financing for 502-Unit Fort Lauderdale Apartment Complex, JV / Partnership - New York - Joint Venture Launches Construction on Multifamily at Yonkers’ Ridge Hill Center, JV / Partnership - Other / Unknown - Erland Construction Partners with Nordblom on New Dedham Multifamily, L.A., Los Angeles, Los Angeles / California, Refinancing - Miami / Florida - JSB Capital Lands $238M Refi on Doral Apartment Community, Refinancing - Other / Unknown - Northmarq Arranges $24.7M Refinancing for Class A Multifamily Property in Chicago
- New York: Brooklyn, New York, New York City / New York
- Related Companies: General Project Signal - Miami / Florida - Related Affiliate Obtains $167M Loan Package for Miami Apartment Community, related
- Sun Belt: Atlanta, Austin, Austin / Texas, Dallas, Development Start - Austin / Texas - OHT Helming 402-Unit Austin Rental Community, Development Start - Phoenix / Arizona - Empire Group Starts Work on $288M Tempe Apartment Community, Disposition / Exit - Phoenix / Arizona - N. Phoenix Apartments Trade for $58.7M, Entitlement / Permitting - Phoenix / Arizona - Development Team Pursuing 376-Unit Tempe Apartment Venture, Miami / Florida, Phoenix, Phoenix / Arizona, Sun Belt

## Weak Matches Needing Manual Review

- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, gp_intelligence.csv)
- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, institutional_relationships.csv)
- Acquisition - Florida - Hamilton Point Acquires Central Florida Multifamily Asset for $57M -> Acquisition - Florida - Hamilton Point Acquires Central Florida Multifamily Asset for $57M (40, relationship_graph.csv)
- Acquisition - Other / Unknown - Icon Real Estate Advisors Arranges Sale of 88-Unit East Orange Multifamily Portfolio -> Acquisition - Other / Unknown - Icon Real Estate Advisors Arranges Sale of 88-Unit East Orange Multifamily Portfolio (40, relationship_graph.csv)
- Acquisition - Other / Unknown - Northmarq Provides $22.8M Agency Acquisition Loan for Metro Boston Affordable Housing Comp... -> Acquisition - Other / Unknown - Northmarq Provides $22.8M Agency Acquisition Loan for Metro Boston Affordable Housing Comp... (40, relationship_graph.csv)
- America -> America (40, deal_pipeline.csv)
- America -> America (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Beverly Hills -> Beverly Hills (40, deal_pipeline.csv)
- Beverly Hills -> Beverly Hills (40, relationship_graph.csv)
- Refinancing - New York City / New York - CBRE Arranges Financing for Rent-Stabilized Midwood Multifamily -> CBRE (60, relationship_graph.csv)
- Beverly Hills / California -> California (60, articles.csv)
- Beverly Hills / California -> California (60, deal_pipeline.csv)
- Beverly Hills / California -> California (60, relationship_graph.csv)
- San Francisco / California -> California (60, articles.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
