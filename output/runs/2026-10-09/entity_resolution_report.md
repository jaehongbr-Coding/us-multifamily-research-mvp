# Entity Resolution Report

Generated: 2026-10-09 02:49:32

- Total raw entities reviewed: 228
- Total canonical entities created: 70
- Possible duplicate entity groups: 7
- Weak matches needing review: 181
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 135 occurrence(s)
- JLL: 16 occurrence(s)
- IPA: 15 occurrence(s)
- Greystone: 12 occurrence(s)
- Hines: 12 occurrence(s)
- Berkadia: 9 occurrence(s)
- Walker & Dunlop: 9 occurrence(s)
- Marcus & Millichap: 7 occurrence(s)
- JPI: 6 occurrence(s)
- Lincoln Property Company: 6 occurrence(s)

## Top Canonical Markets

- Sun Belt: 50 occurrence(s)
- Los Angeles: 48 occurrence(s)
- Other / Unknown: 35 occurrence(s)
- California: 31 occurrence(s)
- National: 13 occurrence(s)
- Unknown: 13 occurrence(s)
- Seattle: 12 occurrence(s)
- Virginia: 12 occurrence(s)
- New York: 10 occurrence(s)
- Florida: 7 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, berkadia
- California: California, Development Start - San Francisco / California - Updated Renderings For 360 5th Street in SoMa, San Francisco, Disposition / Exit - California - Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993, Disposition / Exit - California - Marcus & Millichap Arranges $7.25M Sale of 19-Unit Townhome Property in Yucaipa California, Entitlement / Permitting - Santa Monica / California - Fresh imagery for proposed housing complex at 1238 Lincoln Blvd. in Santa Monica, General Project Signal - Santa Monica / California - Design tweaks for affordable housing at 1238 7th St. in Santa Monica, San Francisco / California, Santa Monica / California, Southern California
- JLL: JLL, Newport Beach Seniors Communities JLL Capital, Refinancing - California - JLL Arranges $276M Refi for Newport Beach Seniors Communities, jll
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - ParkProperty Acquires 280-Unit Buckhead Apartment Community, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Acquisition - Dallas / Texas - Hines Acquires Dallas Apartments, Retail for $170.5M, Acquisition - Virginia - 5 multifamily deals you may have missed last week, Atlanta / Georgia, BTR / Build-to-Rent - Phoenix / Arizona - Empire Lands $65.5M Refi on Phoenix BTR Community, Construction Financing - Miami / Florida - Terra-Led JV Lands $507M Construction Loan for South Beach Condo Before Pre-Sales, Dallas / Texas, Development Start - Los Angeles / California - Affordable housing completed at 7220 Maie Avenue in Florence-Firestone, Development Start - Los Angeles / California - First phase of housing and healthcare campus commences at 800 N. Main St. in Chinatown, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Disposition / Exit - Los Angeles / California - Recent Capital Improvements Drive Van Nuys Apartment Deal, Disposition / Exit - Los Angeles / California - The Bloc Office and Retail Come Up for Sale in DTLA, Disposition / Exit - Other / Unknown - Interactive Floor Plans Platform Planpoint Exits Stealth, Disposition / Exit - Santa Monica / California - Mixed-use project slated to replace Mel's Drive-In in Santa Monica, Entitlement / Permitting - California - 388 apartments to replace offices at 3200 E. Carson St. in Lakewood, Entitlement / Permitting - Los Angeles / California - LAUSD board moves forward with plans for housing at sites in West Hollywood and Woodland H..., General Project Signal - Atlanta / Georgia - Space Craft Building 4th Charlotte Optimist Park Rental Community, General Project Signal - Los Angeles / California - Rendering vs. Reality: Affordable housing at 1400 Long Beach Blvd., General Project Signal - Other / Unknown - Rockland Trust Provides Financing for Quincy Affordable Development, JV / Partnership - Miami / Florida - Development Group Scores Financing for 502-Unit Fort Lauderdale Apartment Complex, Los Angeles, Los Angeles / California, Office-to-Residential Conversion - Washington DC - Jemal-Led JV Plans 323-Unit Office-to-Resi Conversion in D.C.
- New York: Acquisition - New York - Pantzer Makes Second Tri-State Deal This Year with Woodbridge Multifamily Acquisition, General Project Signal - National - WinnCompany Completes $46M Transit-Oriented Mixed-Income Multifamily Community Near Boston, General Project Signal - New York City / New York - Developers Scheme To Build More Housing Units As NYC's Tax Incentive Ages, New York, New York City / New York, Nyc
- Related Companies: Construction Financing - Miami / Florida - Related Urban Development Group Secures $167M for Phase One of Income Restricted Multifami..., General Project Signal - Miami / Florida - Related Affiliate Obtains $167M Loan Package for Miami Apartment Community, related
- Sun Belt: Atlanta, Austin, Dallas, Development Start - Phoenix / Arizona - Empire Group Starts Work on $288M Tempe Apartment Community, Entitlement / Permitting - Phoenix / Arizona - Development Team Pursuing 376-Unit Tempe Apartment Venture, Miami, Miami / Florida, Phoenix, Phoenix / Arizona, Sun Belt

## Weak Matches Needing Manual Review

- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, gp_intelligence.csv)
- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, institutional_relationships.csv)
- Acquisition - Seattle - IPA Negotiates $72M Sale of Apartment Community in Kent, Washington -> Acquisition - Seattle - IPA Negotiates $72M Sale of Apartment Community in Kent, Washington (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- San Francisco / California -> California (60, articles.csv)
- San Francisco / California -> California (60, deal_pipeline.csv)
- San Francisco / California -> California (60, relationship_graph.csv)
- Santa Monica / California -> California (60, articles.csv)
- Santa Monica / California -> California (60, deal_pipeline.csv)
- Santa Monica / California -> California (60, relationship_graph.csv)
- Development Start - San Francisco / California - Updated Renderings For 360 5th Street in SoMa, San Francisco -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993 -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Marcus & Millichap Arranges $7.25M Sale of 19-Unit Townhome Property in Yucaipa California -> California (60, relationship_graph.csv)
- Entitlement / Permitting - Santa Monica / California - Fresh imagery for proposed housing complex at 1238 Lincoln Blvd. in Santa Monica -> California (60, relationship_graph.csv)
- General Project Signal - Santa Monica / California - Design tweaks for affordable housing at 1238 7th St. in Santa Monica -> California (60, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
