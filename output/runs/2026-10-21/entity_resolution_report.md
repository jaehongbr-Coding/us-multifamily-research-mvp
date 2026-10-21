# Entity Resolution Report

Generated: 2026-10-21 01:20:31

- Total raw entities reviewed: 209
- Total canonical entities created: 59
- Possible duplicate entity groups: 8
- Weak matches needing review: 157
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 114 occurrence(s)
- JLL: 33 occurrence(s)
- Kennedy Wilson: 17 occurrence(s)
- Blackstone: 15 occurrence(s)
- Berkadia: 9 occurrence(s)
- High Street Residential: 9 occurrence(s)
- Marcus & Millichap: 8 occurrence(s)
- PCCP: 8 occurrence(s)
- Hines: 7 occurrence(s)
- IPA: 6 occurrence(s)

## Top Canonical Markets

- California: 45 occurrence(s)
- Los Angeles: 43 occurrence(s)
- Other / Unknown: 38 occurrence(s)
- Sun Belt: 32 occurrence(s)
- National: 15 occurrence(s)
- Unknown: 15 occurrence(s)
- Southeast: 7 occurrence(s)
- New York: 6 occurrence(s)
- South Florida: 6 occurrence(s)
- Seattle: 5 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Acquisition - Miami / Florida - Berkadia Arranges Refis for 3 S. Florida Rental Communities, Berkadia, berkadia
- Blackstone: Blackstone, General Project Signal - Denver / Colorado - Blackstone’s 2021 $1.3B CMBS Multifamily Loan Hits Special Servicing, General Project Signal - Seattle - 6 Blackstone multifamily properties move to servicing, blackstone
- California: Acquisition - California - Forbright Bank Provides $50M for Southern California R&D Campus, Acquisition - San Francisco / California - Hamilton Zanze Announces Sale of Indigo 19 Multifamily Community in Virginia Beach, California, Construction Financing - California - PCCP Provides $41M Refi on North Park Multifamily, Construction Financing - California - PCCP Provides $41M Refinancing for Multifamily Community in San Diego, Disposition / Exit - California - Anaheim Deal Represents Investor’s First Multifamily Buy Since 1993, Disposition / Exit - California - Anaheim Sale is First Closing in Broader Multifamily Portfolio, Entitlement / Permitting - San Francisco / California - New Building Permits For 230 Anza Street in Lone Mountain, San Francisco, General Project Signal - Other / Unknown - Fresh renderings for new workforce housing at 315 N. Pasadena Ave., JV / Partnership - California - High Street Residential, Barings Break Ground in Redwood City, San Diego, San Francisco / California, Southern California
- JLL: General Project Signal - Los Angeles / California - JLL Arranges $50M Bridge Loan for Thousand Oaks R&D and Office Campus, JLL, Newport Beach Seniors Communities JLL Capital, Refinancing - California - JLL Arranges $276M Refi for Newport Beach Seniors Communities, jll
- Kennedy Wilson: Disposition / Exit - Phoenix / Arizona - Kennedy Wilson Eyeing School Site for Denver Apartment Community, Kennedy Wilson, Office-to-Residential Conversion - California - Kennedy Wilson’ Vintage Housing Buys Foreclosed San Diego Tower for Multifamily Redevelopm..., kennedy wilson
- Los Angeles: Acquisition - Atlanta / Georgia - Hines Pays $237.8M for Buckhead Rental Community, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Acquisition - Dallas / Texas - IPA Arranges Sale of 288-Unit Apartment Complex in Red Oak, Texas, Atlanta / Georgia, Construction Financing - California - Purpose-Built Student Housing Near SDSU Has Financing in Place, Dallas / Texas, Disposition / Exit - Atlanta / Georgia - Investor Takes Over Distressed Atlanta Apartment Asset, Disposition / Exit - Los Angeles / California - Newly Constructed Palmdale McDonald’s Trades in All-Cash Deal, Entitlement / Permitting - Los Angeles / California - 32 apartments proposed at 806 N. Sweetzer Ave. in Hollywood, Entitlement / Permitting - Los Angeles / California - Rendering vs. Reality: 176 apartments at 2225 Sunset Boulevard in Echo Park, Entitlement / Permitting - Other / Unknown - 75 apartments planned at 925 Eucalyptus Ave. in Inglewood, General Project Signal - Atlanta / Georgia - FCP Trades 260-Unit Atlanta-Area Rental Asset for $55M, General Project Signal - Los Angeles / California - New supportive housing opens at 8209 Sepulveda Blvd. in the Valley, JV / Partnership - National - Habitat, Cabrera Capital Break Ground on LeClaire Courts Mixed-Use Redevelopment in Chicag..., Los Angeles, Los Angeles / California, Office-to-Residential Conversion - Dallas / Texas - Trammell Crow Breaks Ground On Office-To-Resi Conversion In Dallas: The DFW Deal Sheet, Refinancing - Miami / Florida - Little Havana Apartment Owners Land $50.8M Refi
- New York: General Project Signal - New York City / New York - NYCHA Cuts Ribbon on $636M Rehab of East Brooklyn Apartments, New York, New York City, New York City / New York
- Sun Belt: Atlanta, Austin, Dallas, General Project Signal - Miami / Florida - Aimco Advancing Luxury Edgewater Apartments, Miami / Florida, Phoenix, Phoenix / Arizona, Sun Belt, Tampa / Florida

## Weak Matches Needing Manual Review

- A10 Capital -> A10 Capital (40, gp_intelligence.csv)
- A10 Capital -> A10 Capital (40, institutional_relationships.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- BTR / Build-to-Rent - Other / Unknown - Build-to-rent now eligible for Federal Housing Administration financing -> BTR / Build-to-Rent - Other / Unknown - Build-to-rent now eligible for Federal Housing Administration financing (40, relationship_graph.csv)
- Acquisition - Miami / Florida - Berkadia Arranges Refis for 3 S. Florida Rental Communities -> Berkadia (60, relationship_graph.csv)
- General Project Signal - Denver / Colorado - Blackstone’s 2021 $1.3B CMBS Multifamily Loan Hits Special Servicing -> Blackstone (60, relationship_graph.csv)
- General Project Signal - Seattle - 6 Blackstone multifamily properties move to servicing -> Blackstone (60, relationship_graph.csv)
- Cabrera Capital -> Cabrera Capital (40, gp_intelligence.csv)
- Cabrera Capital -> Cabrera Capital (40, institutional_relationships.csv)
- San Francisco / California -> California (60, articles.csv)
- San Francisco / California -> California (60, deal_pipeline.csv)
- San Francisco / California -> California (60, relationship_graph.csv)
- Acquisition - California - Forbright Bank Provides $50M for Southern California R&D Campus -> California (60, relationship_graph.csv)
- Acquisition - San Francisco / California - Hamilton Zanze Announces Sale of Indigo 19 Multifamily Community in Virginia Beach -> California (60, relationship_graph.csv)
- Construction Financing - California - PCCP Provides $41M Refi on North Park Multifamily -> California (60, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
