# Entity Resolution Report

Generated: 2026-06-17 00:18:23

- Total raw entities reviewed: 212
- Total canonical entities created: 56
- Possible duplicate entity groups: 9
- Weak matches needing review: 159
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 132 occurrence(s)
- JLL: 37 occurrence(s)
- Berkadia: 16 occurrence(s)
- CBRE: 14 occurrence(s)
- Brookfield: 9 occurrence(s)
- Marcus & Millichap: 9 occurrence(s)
- Greystar: 6 occurrence(s)
- Quarterra: 6 occurrence(s)
- Wood Partners: 6 occurrence(s)
- PEF Advisors: 5 occurrence(s)

## Top Canonical Markets

- Los Angeles: 49 occurrence(s)
- Sun Belt: 49 occurrence(s)
- California: 37 occurrence(s)
- Other / Unknown: 34 occurrence(s)
- New York: 15 occurrence(s)
- National: 12 occurrence(s)
- Unknown: 12 occurrence(s)
- South Florida: 8 occurrence(s)
- Houston / Texas: 6 occurrence(s)
- Texas: 6 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, berkadia
- Brookfield: Brookfield, brookfield
- CBRE: CBRE, cbre
- California: Acquisition - California - Investor in Postal Real Estate Scores Off-Market Deal in San Diego, Acquisition - California - Levin Johnston Finalizes 1031 Exchange for Livermore Apartments, Beverly Hills / California, California, Disposition / Exit - California - Former Bank Branch Positioned as Development Opportunity in Garden Grove Sale, Disposition / Exit - California - Yorba Linda Parking Lot Sells for Townhome Redevelopment, General Project Signal - California - Work to commence next year for affordable housing at 2321 Fairview St. in Burbank, Recapitalization - California - PEF Advisors, Freestone Capital Form JV to Recapitalize Affordable Properties, Refinancing - California - Newly Opened Santa Cruz Luxury Hotel Refinanced for $115M, San Francisco / California
- Greystar: General Project Signal - Miami / Florida - Greystar Eyeing 896 Doral Apartment Units, Greystar
- JLL: General Project Signal - California - JLL Arranges $252M Financing for Huntington Beach Seniors Project, JLL, Memory Care Project JLL Capital, jll
- Los Angeles: Acquisition - Houston / Texas - MetroNational Buys 244-Room Moran Hotel at CITYCENTRE in West Houston, Acquisition - Los Angeles / California - World Cup descends on L.A., CicLAvia on June 28, and more, Acquisition - Louisiana - Muss Development, Amesbury Acquire 270-Unit Apartment Community in Lake Charles, Louisiana, Atlanta / Georgia, BTR / Build-to-Rent - Phoenix / Arizona - Porter Kyle Builders Names Industry Veteran John Rowland Vice President of Construction, Construction Financing - Beverly Hills / California - Developer secures $85m loan for mixed-use project at 55 N. La Cienega Blvd. in Beverly Hil..., Construction Financing - Miami / Florida - 13th Floor Obtains $134M Construction Loan for Douglas Final Phase, Dallas / Texas, Disposition / Exit - Dallas / Texas - 452-Unit Value-Add Multifamily Community Trades in FW, Disposition / Exit - Phoenix / Arizona - Quarterra Sells 290-Unit Kierland Rental Asset, Entitlement / Permitting - Los Angeles / California - Affordable housing slated for 5139 N. Colfax Ave. in Valley Village, Entitlement / Permitting - Los Angeles / California - City Planning Commission approves 76 apartments at 2413 N. Silver Lake Boulevard, Entitlement / Permitting - Los Angeles / California - City Planning Commission approves residential towers at 2143 E. Violet St. in DTLA, Entitlement / Permitting - Los Angeles / California - Fast Approvals, Slow Delivery: Just 23% Of Units Approved Under ED 1 Have Been Permitted, Entitlement / Permitting - Other / Unknown - Updated Plans For 4095 Pacific Boulevard, San Mateo, Entitlement / Permitting - Texas - Final Approval For 1215 Bordeaux Drive, Sunnyvale, General Project Signal - Atlanta / Georgia - Insignia Pursuing Embassy Row Redevelopment, General Project Signal - Atlanta / Georgia - Meeting Tomorrow For 3521 Homestead Road, Santa Clara, General Project Signal - Dallas / Texas - Palladium Delivers $65M Fort Worth Affordable Housing Venture, General Project Signal - Houston / Texas - 342 Apartment Units Planned Near Big Rivers Waterpark, JV / Partnership - Los Angeles / California - Big mixed-use project clears a hurdle at 12555 Ventura Blvd. in Studio City, JV / Partnership - Other / Unknown - LaSalle Acquires Student Housing Complex Near Michigan State University, Los Angeles, Los Angeles / California, Office-to-Residential Conversion - Los Angeles / California - Affordable housing takes shape at 711 S. New Hampshire Ave. in Koreatown, Office-to-Residential Conversion - Washington DC - Rockpoint, LCOR, Potomac Investment Properties Plan Georgetown Office-to-Residential Redev...
- New York: Construction Financing - New York - JV Obtains Construction Loan for East Brunswick Assisted Living/Memory Care Project, JV / Partnership - New York City / New York - Hawkins Way JV Grows NYC Student Housing Portfolio with Upper West Side Sale-Leaseback, New York, New York City / New York, Nyc, Operational / Property Management Tech - New York - Podcast | Can AI Help Developers Break Ground Faster ft. Pulley COO Andreas Rotenberg
- Sun Belt: Atlanta, Austin, Construction Financing - Miami / Florida - Developer Duo Closes on $67.5M Financing for Coral Gables Condos, Dallas, Disposition / Exit - Phoenix / Arizona - Wood Partners Sells Gilbert Apartments for $81.6M, General Project Signal - Phoenix / Arizona - Albuquerque Developers Building 272 Affordable Housing Units, JV / Partnership - Miami / Florida - JV Raises $100M for Coral Gables Mixed-Use Project, Miami / Florida, Office-to-Residential Conversion - Phoenix / Arizona - Camelback Office-to-Apartment Conversion Nearly Complete, Phoenix, Phoenix / Arizona, Sun Belt

## Weak Matches Needing Manual Review

- Arizona -> Arizona (40, regional_intelligence.csv)
- Beacon Bank -> Beacon Bank (40, gp_intelligence.csv)
- Beacon Bank -> Beacon Bank (40, institutional_relationships.csv)
- Beverly Hills -> Beverly Hills (40, deal_pipeline.csv)
- Beverly Hills -> Beverly Hills (40, relationship_graph.csv)
- Beverly Hills / California -> California (60, articles.csv)
- Beverly Hills / California -> California (60, deal_pipeline.csv)
- Beverly Hills / California -> California (60, relationship_graph.csv)
- San Francisco / California -> California (60, articles.csv)
- Acquisition - California - Investor in Postal Real Estate Scores Off-Market Deal in San Diego -> California (60, relationship_graph.csv)
- Acquisition - California - Levin Johnston Finalizes 1031 Exchange for Livermore Apartments -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Former Bank Branch Positioned as Development Opportunity in Garden Grove Sale -> California (60, relationship_graph.csv)
- Disposition / Exit - California - Yorba Linda Parking Lot Sells for Townhome Redevelopment -> California (60, relationship_graph.csv)
- General Project Signal - California - Work to commence next year for affordable housing at 2321 Fairview St. in Burbank -> California (60, relationship_graph.csv)
- Recapitalization - California - PEF Advisors, Freestone Capital Form JV to Recapitalize Affordable Properties -> California (60, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
