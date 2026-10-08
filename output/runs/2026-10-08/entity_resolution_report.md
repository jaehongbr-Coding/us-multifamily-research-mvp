# Entity Resolution Report

Generated: 2026-10-08 02:34:58

- Total raw entities reviewed: 240
- Total canonical entities created: 68
- Possible duplicate entity groups: 9
- Weak matches needing review: 184
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 131 occurrence(s)
- Hines: 17 occurrence(s)
- JLL: 17 occurrence(s)
- Walker & Dunlop: 16 occurrence(s)
- Berkadia: 9 occurrence(s)
- Freddie Mac: 9 occurrence(s)
- Marcus & Millichap: 8 occurrence(s)
- Fannie Mae: 7 occurrence(s)
- Greystone: 7 occurrence(s)
- JPI: 6 occurrence(s)

## Top Canonical Markets

- Sun Belt: 50 occurrence(s)
- California: 45 occurrence(s)
- Other / Unknown: 42 occurrence(s)
- Los Angeles: 39 occurrence(s)
- Unknown: 15 occurrence(s)
- Virginia: 10 occurrence(s)
- Florida: 8 occurrence(s)
- Houston / Texas: 7 occurrence(s)
- New York: 6 occurrence(s)
- Santa Monica: 6 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, berkadia
- California: Acquisition - San Francisco / California - IPA Arranges $14.7M Sale of Apartment Complex in Forest Grove, Oregon, Beverly Hills / California, California, Development Start - San Francisco / California - Updated Renderings For 360 5th Street in SoMa, San Francisco, Disposition / Exit - California - Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993, Entitlement / Permitting - Beverly Hills / California - Mixed-use project proposed at 177 S. Robertson Blvd. in Beverly Hills, Entitlement / Permitting - San Francisco / California - New Building Permits Issued For Mission Bay Block 4 East, San Francisco, Entitlement / Permitting - Santa Monica / California - Fresh imagery for proposed housing complex at 1238 Lincoln Blvd. in Santa Monica, General Project Signal - Santa Monica / California - Design tweaks for affordable housing at 1238 7th St. in Santa Monica, Orange County, Refinancing - California - El Dorado Hills Office Complex Refinanced within Tight Timeframe, Refinancing - California - Nexus Obtains $276M Refinance for Orange County Senior Portfolio, San Francisco / California, Santa Monica / California, Southern California
- Fannie Mae: Fannie Mae, fannie mae
- Freddie Mac: Freddie Mac, freddie mac
- JLL: JLL, Newport Beach Seniors Communities JLL Capital, Refinancing - California - JLL Arranges $276M Refi for Newport Beach Seniors Communities, jll
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Acquires 99 West Paces Apartments in Atlanta for $240M, Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - ParkProperty Acquires 280-Unit Buckhead Apartment Community, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Acquisition - Dallas / Texas - Hines Acquires Dallas Apartments, Retail for $170.5M, Acquisition - Florida - Newmark Arranges $45M Financing for Orlando Apartment Acquisition, Acquisition - Southeast - BAM Capital Acquired 334-Unit Multifamily Community in Leland North Carolina, Acquisition - Virginia - 5 multifamily deals you may have missed last week, Atlanta / Georgia, BTR / Build-to-Rent - Phoenix / Arizona - Empire Lands $65.5M Refi on Phoenix BTR Community, Construction Financing - Los Angeles / California - Construction loan issued for affordable housing at 400 Centinela Ave. in Inglewood, Dallas / Texas, Development Start - Los Angeles / California - Affordable housing completed at 7220 Maie Avenue in Florence-Firestone, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Disposition / Exit - Colorado - Marcus & Millichap Arranges $6.55M Sale of Applewood Townhomes in Lakewood Colorado, Disposition / Exit - Los Angeles / California - The Bloc Office and Retail Come Up for Sale in DTLA, Disposition / Exit - Other / Unknown - Neshaminy Mall Redevelopment Plans Revealed: The Philadelphia Deal Sheet, Disposition / Exit - Santa Monica / California - Mixed-use project slated to replace Mel's Drive-In in Santa Monica, Entitlement / Permitting - California - 388 apartments to replace offices at 3200 E. Carson St. in Lakewood, JV / Partnership - Miami / Florida - Development Group Scores Financing for 502-Unit Fort Lauderdale Apartment Complex, Los Angeles, Los Angeles / California, Refinancing - Dallas / Texas - Nitya Capital Refinances 432-Unit Apartment Community in South Dallas, Refinancing - Miami / Florida - JSB Capital Lands $238M Refi on Doral Apartment Community
- New York: General Project Signal - New York City / New York - The Interest Rate Hike Shifts the Calculus on New York City Multifamily Investing, New York, New York City, New York City / New York
- Related Companies: General Project Signal - Miami / Florida - Related Affiliate Obtains $167M Loan Package for Miami Apartment Community, related
- Sun Belt: Atlanta, Austin, Austin / Texas, Dallas, Development Start - Austin / Texas - OHT Helming 402-Unit Austin Rental Community, Development Start - Phoenix / Arizona - Empire Group Starts Work on $288M Tempe Apartment Community, Entitlement / Permitting - Phoenix / Arizona - Development Team Pursuing 376-Unit Tempe Apartment Venture, Miami / Florida, Orlando, Phoenix, Phoenix / Arizona, Sun Belt

## Weak Matches Needing Manual Review

- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, gp_intelligence.csv)
- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, institutional_relationships.csv)
- Affinius Capital -> Affinius Capital (40, deal_pipeline.csv)
- Affinius Capital -> Affinius Capital (40, gp_intelligence.csv)
- Affinius Capital -> Affinius Capital (40, institutional_relationships.csv)
- Affinius Capital -> Affinius Capital (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- BAM Capital -> BAM Capital (40, gp_intelligence.csv)
- BAM Capital -> BAM Capital (40, institutional_relationships.csv)
- Beverly Hills -> Beverly Hills (40, deal_pipeline.csv)
- Beverly Hills -> Beverly Hills (40, relationship_graph.csv)
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
