# Entity Resolution Report

Generated: 2026-06-14 00:09:15

- Total raw entities reviewed: 271
- Total canonical entities created: 82
- Possible duplicate entity groups: 11
- Weak matches needing review: 211
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 158 occurrence(s)
- JLL: 41 occurrence(s)
- Berkadia: 26 occurrence(s)
- CBRE: 16 occurrence(s)
- Quarterra: 15 occurrence(s)
- Marcus & Millichap: 14 occurrence(s)
- Scion Group: 10 occurrence(s)
- Brookfield: 9 occurrence(s)
- Fannie Mae: 7 occurrence(s)
- Greystar: 6 occurrence(s)

## Top Canonical Markets

- Los Angeles: 74 occurrence(s)
- Sun Belt: 67 occurrence(s)
- Other / Unknown: 42 occurrence(s)
- California: 36 occurrence(s)
- Unknown: 17 occurrence(s)
- National: 9 occurrence(s)
- South Florida: 8 occurrence(s)
- Southeast: 7 occurrence(s)
- New York: 6 occurrence(s)
- Seattle: 6 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, Refinancing - Other / Unknown - Berkadia Arranges $35.2M Refinancing for Multifamily Property in Suburban Detroit, berkadia
- Brookfield: Brookfield, brookfield
- CBRE: CBRE, cbre
- California: Beverly Hills / California, California, Construction Financing - Beverly Hills / California - MMCC Arranges $85M in Construction Financing for Beverly Hills Mixed-Use Project, Disposition / Exit - California - Former Bank Branch Positioned as Development Opportunity in Garden Grove Sale, Disposition / Exit - California - Yorba Linda Parking Lot Sells for Townhome Redevelopment, General Project Signal - California - Work to commence next year for affordable housing at 2321 Fairview St. in Burbank, Recapitalization - California - PEF Advisors, Freestone Capital Form JV to Recapitalize Affordable Properties, Refinancing - California - Affinius Lends $120M to Refinance Luxury Multifamily Apartments in San Diegos’s Kearny Mes..., San Diego, San Francisco / California
- Fannie Mae: Fannie Mae, fannie mae
- Freddie Mac: Freddie Mac, freddie mac
- Greystar: General Project Signal - Miami / Florida - Greystar Eyeing 896 Doral Apartment Units, Greystar
- JLL: Construction Financing - California - JLL Lines Up $144M Construction Loan for Santa Ana Multifamily, General Project Signal - California - JLL Arranges $252M Financing for Huntington Beach Seniors Project, JLL, Refinancing - Southeast - JLL Secures $64M Refinancing for 820-Bed Student Housing Community Near Mississippi State..., Santa Ana Multifamily JLL Capital, jll
- Los Angeles: Acquisition - Atlanta / Georgia - The Scion Group Continues Student Housing Spree With $1.5B Acquisition, Acquisition - Florida - BCIP Acquires 32.6 Acres on Florida’s Space Coast, Plans Grocery-Anchored Mixed-Use Develo..., Acquisition - Los Angeles / California - High-rise senior housing complex pitched for 6400 Canoga Ave. in Warner Center, Acquisition - Los Angeles / California - Rockpoint Scores Mid-Rise Apartment Property in Westwood, Acquisition - Los Angeles / California - World Cup descends on L.A., CicLAvia on June 28, and more, Acquisition - New York City / New York - AMAC Holdings Sells Adjacent East Village Buildings for $23.5M, Atlanta / Georgia, BTR / Build-to-Rent - Other / Unknown - RLAM Closes In On 1,000 BTR Units After New Acquisitions, BTR / Build-to-Rent - Phoenix / Arizona - Porter Kyle Builders Names Industry Veteran John Rowland Vice President of Construction, Construction Financing - Atlanta / Georgia - East Bank Developer Inks $80M Construction Loan, Construction Financing - Los Angeles / California - MMCC Arranges $85M Construction Loan for Beverly Hills Mixed-Use, Construction Financing - Miami / Florida - 13th Floor Obtains $134M Construction Loan for Douglas Final Phase, Dallas / Texas, Disposition / Exit - Los Angeles / California - Apartments Along Burton Way Trade for $603K Per Unit, Disposition / Exit - Phoenix / Arizona - Quarterra Multifamily Sells Upscale Multifamily Asset Residences Kierland in Scottsdale, Disposition / Exit - Phoenix / Arizona - Quarterra Sells 290-Unit Kierland Rental Asset, Entitlement / Permitting - Los Angeles / California - 77-unit affordable housing complex proposed at 8811 Reading Ave. in Westchester, Entitlement / Permitting - Los Angeles / California - Hotel Indigo on the rise at 515 N. Central Ave. in Glendale, Entitlement / Permitting - Los Angeles / California - Wrapping off for affordable housing at 714 S. Grand View Street in Westlake, Entitlement / Permitting - San Francisco / California - Formal Application For 926 Natoma Street in SoMa, San Francisco, General Project Signal - Atlanta / Georgia - Insignia Pursuing Embassy Row Redevelopment, General Project Signal - Los Angeles / California - Affordable housing coming to 1150 Sunset Blvd. in Echo Park, General Project Signal - Other / Unknown - Arrow Real Estate Advisors Arranges $70M for Delaware Multifamily Development The Press, JV / Partnership - Los Angeles / California - Big mixed-use project clears a hurdle at 12555 Ventura Blvd. in Studio City, Los Angeles, Los Angeles / California, Office-to-Residential Conversion - Los Angeles / California - 230 apartments unwrapped at 640 S. St. Andrews Pl. in Koreatown, Refinancing - Atlanta / Georgia - Georgia Tech Student Housing Investors Ink Refi, Refinancing - Atlanta / Georgia - QuadReal Property Group Provides $64M Refi for Miss. State Student Housing, Refinancing - Dallas / Texas - Inside Swapnil Agarwal’s efforts to save his apartment portfolio
- New York: Manhattan, New York, New York City / New York

## Weak Matches Needing Manual Review

- Acquisition - Houston / Texas - Interurban Offloads 180-Unit Houston Rental Community -> Acquisition - Houston / Texas - Interurban Offloads 180-Unit Houston Rental Community (40, relationship_graph.csv)
- Acquisition - Washington DC - Sentinel Real Estate Acquires Luxury Apartment Community in Potomac -> Acquisition - Washington DC - Sentinel Real Estate Acquires Luxury Apartment Community in Potomac (40, relationship_graph.csv)
- Affinius Capital -> Affinius Capital (40, gp_intelligence.csv)
- Affinius Capital -> Affinius Capital (40, institutional_relationships.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Arrow Real Estate Advisors -> Arrow Real Estate Advisors (40, gp_intelligence.csv)
- Arrow Real Estate Advisors -> Arrow Real Estate Advisors (40, institutional_relationships.csv)
- BCIP -> BCIP (40, gp_intelligence.csv)
- BCIP -> BCIP (40, institutional_relationships.csv)
- BWE -> BWE (40, gp_intelligence.csv)
- BWE -> BWE (40, institutional_relationships.csv)
- Refinancing - Other / Unknown - Berkadia Arranges $35.2M Refinancing for Multifamily Property in Suburban Detroit -> Berkadia (60, relationship_graph.csv)
- Beverly Hills -> Beverly Hills (40, deal_pipeline.csv)
- Beverly Hills -> Beverly Hills (40, relationship_graph.csv)
- Beverly Hills / California -> California (60, articles.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
