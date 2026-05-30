# Entity Resolution Report

Generated: 2026-05-30 23:02:08

- Total raw entities reviewed: 141
- Total canonical entities created: 44
- Possible duplicate entity groups: 5
- Weak matches needing review: 106
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 151 occurrence(s)
- Wood Partners: 10 occurrence(s)
- Alliance Residential: 8 occurrence(s)
- JLL: 8 occurrence(s)
- Berkadia: 6 occurrence(s)
- Crescent Communities: 6 occurrence(s)
- Lincoln Property Company: 5 occurrence(s)
- RXR: 5 occurrence(s)
- Blackstone: 2 occurrence(s)
- Freddie Mac: 2 occurrence(s)

## Top Canonical Markets

- Sun Belt: 70 occurrence(s)
- Los Angeles: 38 occurrence(s)
- Other / Unknown: 37 occurrence(s)
- California: 32 occurrence(s)
- New York: 18 occurrence(s)
- Unknown: 16 occurrence(s)
- Florida: 14 occurrence(s)
- National: 14 occurrence(s)
- Southeast: 7 occurrence(s)
- Arizona: 5 occurrence(s)

## Possible Duplicate Entities

- California: California, Disposition / Exit - California - Carlsbad Lifestyle Center Fetches $91M in Sale to 11North, JV / Partnership - California - Joint Venture of PCCP and Alliance Residential Company Acquires 184-Unit Multifamily Commu..., JV / Partnership - California - New Rendering For 650 Divisadero Street, San Francisco, JV / Partnership - California - PCCP, Alliance Residential Snap Up Garden-Style Riverside Complex, Recapitalization - California - PEF Advisors, Freestone Capital Form JV to Recapitalize Affordable Properties
- JLL: Construction Financing - California - JLL Lines Up $144M Construction Loan for Santa Ana Multifamily, General Project Signal - California - JLL Arranges $252M Financing for Huntington Beach Seniors Project, jll
- Los Angeles: Acquisition - Sun Belt - El-Ad Pays $45.5M for Coconut Grove Property, Construction Financing - Los Angeles - Developer scores construction loan for mixed-use project at 8025 Santa Monica Blvd. in Wes..., Construction Financing - National - Basis Investment Group Announces $43M Refinancing and Lease-Up of Newly Constructed Class-..., Construction Financing - New York - Dwight Mortgage Trust Lends $55M on Rockland County, N.Y., Multifamily Development, Construction Financing - Sun Belt - Alta Developers Lands $91.8M Construction Loan for Miami Apartments, Disposition / Exit - Los Angeles - Covina Apartments Trade on In-Place Cash Flow, Rental Upside, Disposition / Exit - Los Angeles - Metro breaks ground on North Hollywood - Pasadena BRT line, Entitlement / Permitting - California - Updated plan for apartments at 1238 Lincoln Blvd. in Santa Monica, Entitlement / Permitting - Los Angeles - 150 apartments debut at 549 S. Harvard Blvd. in Koreatown, Entitlement / Permitting - Los Angeles - Infill housing slated for 349 N. Oakhurst Ave. in Beverly Hills, Entitlement / Permitting - Southeast - 40 apartments slated for 4080 Lafayette Place in Culver City, General Project Signal - Los Angeles - Affordable housing slated for 1418 S. Mansfield Ave. in Mid-City, General Project Signal - Sun Belt - Insignia Pursuing Embassy Row Multifamily Mixed-Use Redevelopment in Atlanta, JV / Partnership - Los Angeles - Logos Faith, St. Rest Break Ground on 138-Unit Affordable Housing, JV / Partnership - Los Angeles - RAND reviews ULA impacts, Mayor's race focuses on housing, and more, Los Angeles, Modular / Construction Innovation - Los Angeles - Modular housing manufacturing proposed for city-owned site at 10901 S. Clovis St. in South..., Office-to-Residential Conversion - National - JBG SMITH Commences Office-to-Residential Conversion in National Landing, Refinancing - New York - PNC Bank Refis West Village Apartment Building With $404M Loan, Refinancing - Other / Unknown - $46M Bridge Loan Refinances Newly Built Moreno Valley Apartments Villa Annette
- New York: JV / Partnership - New York - IPA Arranges $27M Acquisition Loan for Apartment Community in D.C’s NoMa District, Manhattan, New York, Office-to-Residential Conversion - New York - Speaker Spotlight: Adam Greene of RXR
- Sun Belt: Acquisition - Sun Belt - Miami Apartments Trade for $109.9M, Atlanta, Austin, BTR / Build-to-Rent - Sun Belt - Work Begins on 94-Unit Scottsdale Luxury BTR Community, Dallas, Disposition / Exit - Sun Belt - Charlotte Apartment Project Fetches $107M, Disposition / Exit - Sun Belt - Eaton Vance Picks Charlotte Rental Community for $65.8M, Disposition / Exit - Sun Belt - Grand Peaks Sells Miami-Area Apartments for $65.5M, Entitlement / Permitting - Sun Belt - Cambridge Properties Bringing New Life to Aging Charlotte Center, General Project Signal - Sun Belt - Empire Group Starts Work on $170M Phoenix Apartment Tower, General Project Signal - Sun Belt - Insignia Pursuing Embassy Row Redevelopment, Miami, Phoenix, Refinancing - Sun Belt - Georgia Tech Student Housing Investors Ink Refi, Sun Belt

## Weak Matches Needing Manual Review

- Acquisition - Arizona - Wood Partners Sells 278-Unit Alta Rise Multifamily Community in Gilbert, Arizona -> Acquisition - Arizona - Wood Partners Sells 278-Unit Alta Rise Multifamily Community in Gilbert, Arizona (40, relationship_graph.csv)
- Acquisition - Florida - Aventon to Build 270-Unit Port Richey Rental Community -> Acquisition - Florida - Aventon to Build 270-Unit Port Richey Rental Community (40, relationship_graph.csv)
- Acquisition - Other / Unknown - Avison Young Negotiates $19.1M Sale of Apartment Building in Wethersfield, Connecticut -> Acquisition - Other / Unknown - Avison Young Negotiates $19.1M Sale of Apartment Building in Wethersfield, Connecticut (40, relationship_graph.csv)
- Acquisition - Other / Unknown - Multifamily Community River Oaks Apartments in Norfolk Virginia Sells for $10M with Acquis... -> Acquisition - Other / Unknown - Multifamily Community River Oaks Apartments in Norfolk Virginia Sells for $10M with Acquis... (40, relationship_graph.csv)
- Alliance Residential -> Alliance Residential (40, deal_pipeline.csv)
- Alliance Residential -> Alliance Residential (40, gp_intelligence.csv)
- Alliance Residential -> Alliance Residential (40, institutional_relationships.csv)
- Alliance Residential -> Alliance Residential (40, relationship_graph.csv)
- Arizona -> Arizona (40, articles.csv)
- Arizona -> Arizona (40, deal_pipeline.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Arizona -> Arizona (40, relationship_graph.csv)
- Disposition / Exit - California - Carlsbad Lifestyle Center Fetches $91M in Sale to 11North -> California (60, relationship_graph.csv)
- JV / Partnership - California - Joint Venture of PCCP and Alliance Residential Company Acquires 184-Unit Multifamily Commu... -> California (60, relationship_graph.csv)
- JV / Partnership - California - New Rendering For 650 Divisadero Street, San Francisco -> California (60, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
