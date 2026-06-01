# Entity Resolution Report

Generated: 2026-06-01 07:28:39

- Total raw entities reviewed: 199
- Total canonical entities created: 63
- Possible duplicate entity groups: 5
- Weak matches needing review: 170
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 146 occurrence(s)
- Wood Partners: 11 occurrence(s)
- JLL: 10 occurrence(s)
- Crescent Communities: 7 occurrence(s)
- Alliance Residential: 6 occurrence(s)
- Lincoln Property Company: 6 occurrence(s)
- RXR: 6 occurrence(s)
- Berkadia: 4 occurrence(s)
- Blackstone: 2 occurrence(s)
- Freddie Mac: 2 occurrence(s)

## Top Canonical Markets

- Los Angeles: 65 occurrence(s)
- Sun Belt: 42 occurrence(s)
- California: 33 occurrence(s)
- Other / Unknown: 27 occurrence(s)
- New York: 21 occurrence(s)
- Unknown: 11 occurrence(s)
- South Florida: 8 occurrence(s)
- Denver / Colorado: 6 occurrence(s)
- National: 6 occurrence(s)
- Northern Virginia / Virginia: 6 occurrence(s)

## Possible Duplicate Entities

- California: California, Disposition / Exit - California - Carlsbad Lifestyle Center Fetches $91M in Sale to 11North, JV / Partnership - Riverside / California - PCCP, Alliance Residential Snap Up Garden-Style Riverside Complex, Moreno Valley / California, Recapitalization - California - PEF Advisors, Freestone Capital Form JV to Recapitalize Affordable Properties, Riverside / California, San Francisco / California, Santa Monica / California
- JLL: Construction Financing - California - JLL Lines Up $144M Construction Loan for Santa Ana Multifamily, General Project Signal - California - JLL Arranges $252M Financing for Huntington Beach Seniors Project, jll
- Los Angeles: Atlanta / Georgia, Construction Financing - Los Angeles / California - Developer scores construction loan for mixed-use project at 8025 Santa Monica Blvd. in Wes..., Construction Financing - Miami / Florida - Alta Developers Lands $91.8M Construction Loan for Miami Apartments, Construction Financing - New York - Dwight Mortgage Trust Lends $55M on Rockland County, N.Y., Multifamily Development, Dallas / Texas, Disposition / Exit - Atlanta / Georgia - Charlotte Apartment Project Fetches $107M, Disposition / Exit - Atlanta / Georgia - Eaton Vance Picks Charlotte Rental Community for $65.8M, Disposition / Exit - Los Angeles / California - Covina Apartments Trade on In-Place Cash Flow, Rental Upside, Disposition / Exit - Los Angeles / California - Metro breaks ground on North Hollywood - Pasadena BRT line, Entitlement / Permitting - Atlanta / Georgia - Cambridge Properties Bringing New Life to Aging Charlotte Center, Entitlement / Permitting - Los Angeles / California - 150 apartments debut at 549 S. Harvard Blvd. in Koreatown, Entitlement / Permitting - Los Angeles / California - Infill housing slated for 349 N. Oakhurst Ave. in Beverly Hills, Entitlement / Permitting - San Francisco / California - First Projects Advance Under San Francisco's New Zoning Plan, But Costs Hold Pipeline To A..., Entitlement / Permitting - Santa Monica / California - Updated plan for apartments at 1238 Lincoln Blvd. in Santa Monica, General Project Signal - Atlanta / Georgia - Insignia Pursuing Embassy Row Multifamily Mixed-Use Redevelopment in Atlanta, General Project Signal - Atlanta / Georgia - Insignia Pursuing Embassy Row Redevelopment, General Project Signal - Los Angeles / California - Affordable housing slated for 1418 S. Mansfield Ave. in Mid-City, JV / Partnership - Los Angeles / California - Logos Faith, St. Rest Break Ground on 138-Unit Affordable Housing, JV / Partnership - Santa Monica / California - RAND reviews ULA impacts, Mayor's race focuses on housing, and more, Las Vegas / Nevada, Los Angeles, Los Angeles / California, Modular / Construction Innovation - Los Angeles / California - Modular housing manufacturing proposed for city-owned site at 10901 S. Clovis St. in South..., National Landing, Office-to-Residential Conversion - Northern Virginia / Virginia - JBG SMITH Begins Latest Office-to-Residential Conversion in National Landing Northern Virg..., Office-to-Residential Conversion - Northern Virginia / Virginia - JBG SMITH Commences Office-to-Residential Conversion in National Landing, Refinancing - Atlanta / Georgia - Georgia Tech Student Housing Investors Ink Refi, Refinancing - Moreno Valley / California - $46M Bridge Loan Refinances Newly Built Moreno Valley Apartments Villa Annette, Refinancing - New York City / New York - PNC Bank Refis West Village Apartment Building With $404M Loan
- New York: Manhattan, New York, New York City, New York City / New York, Office-to-Residential Conversion - New York City / New York - Speaker Spotlight: Adam Greene of RXR, Refinancing - New York City / New York - Affinius Capital Led Joint Venture Closes $3.5B Acquisition of Veris Residential
- Sun Belt: Acquisition - Miami / Florida - Miami Apartments Trade for $109.9M, Acquisition - Phoenix / Arizona - Wood Partners Sells 278-Unit Alta Rise Multifamily Community in Gilbert, Arizona, Atlanta, Austin, BTR / Build-to-Rent - Phoenix / Arizona - Work Begins on 94-Unit Scottsdale Luxury BTR Community, Dallas, Disposition / Exit - Miami / Florida - Grand Peaks Sells Miami-Area Apartments for $65.5M, General Project Signal - Miami / Florida - S. Florida Ritz-Carlton Developer Inks $401M Bridge Loan, General Project Signal - Phoenix / Arizona - Empire Group Starts Work on $170M Phoenix Apartment Tower, Miami / Florida, Phoenix, Phoenix / Arizona, Sun Belt

## Weak Matches Needing Manual Review

- Acquisition - Port Richey / Florida - Aventon to Build 270-Unit Port Richey Rental Community -> Acquisition - Port Richey / Florida - Aventon to Build 270-Unit Port Richey Rental Community (40, relationship_graph.csv)
- Acquisition - Wethersfield / Connecticut - Avison Young Negotiates $19.1M Sale of Apartment Building in Wethersfield, Connecticut -> Acquisition - Wethersfield / Connecticut - Avison Young Negotiates $19.1M Sale of Apartment Building in Wethersfield, Connecticut (40, relationship_graph.csv)
- Alliance Residential -> Alliance Residential (40, deal_pipeline.csv)
- Alliance Residential -> Alliance Residential (40, gp_intelligence.csv)
- Alliance Residential -> Alliance Residential (40, institutional_relationships.csv)
- Alliance Residential -> Alliance Residential (40, relationship_graph.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Baton Rouge / Louisiana -> Baton Rouge / Louisiana (40, articles.csv)
- Moreno Valley / California -> California (60, articles.csv)
- Moreno Valley / California -> California (60, deal_pipeline.csv)
- Moreno Valley / California -> California (60, relationship_graph.csv)
- Riverside / California -> California (60, articles.csv)
- Riverside / California -> California (60, deal_pipeline.csv)
- Riverside / California -> California (60, relationship_graph.csv)
- San Francisco / California -> California (60, articles.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
