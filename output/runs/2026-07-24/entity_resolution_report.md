# Entity Resolution Report

Generated: 2026-07-24 00:02:30

- Total raw entities reviewed: 260
- Total canonical entities created: 74
- Possible duplicate entity groups: 11
- Weak matches needing review: 201
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 145 occurrence(s)
- JLL: 30 occurrence(s)
- Berkadia: 15 occurrence(s)
- CIM Group: 14 occurrence(s)
- Kennedy Wilson: 9 occurrence(s)
- Marcus & Millichap: 9 occurrence(s)
- AvalonBay: 8 occurrence(s)
- CBRE: 8 occurrence(s)
- Hines: 8 occurrence(s)
- IPA: 6 occurrence(s)

## Top Canonical Markets

- Los Angeles: 59 occurrence(s)
- California: 47 occurrence(s)
- Sun Belt: 42 occurrence(s)
- Other / Unknown: 40 occurrence(s)
- New York: 21 occurrence(s)
- Unknown: 17 occurrence(s)
- South Florida: 8 occurrence(s)
- National: 7 occurrence(s)
- Colorado: 6 occurrence(s)
- Seattle: 5 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Acquisition - San Francisco / California - Berkadia Facilitates Sale and Acquisition Financing of Multifamily Property Portfolio in t..., Berkadia, berkadia
- CBRE: Acquisition - California - CBRE Arranges $30M Sale of Six-Building Retail Portfolio in Long Beach, California, CBRE, cbre
- California: Acquisition - California - Bascom Acquires Buena Park Apartments as Value-Add Deal, Acquisition - California - Original Developer Trades Castro Valley Multifamily Duo, Beverly Hills / California, California, Disposition / Exit - California - Fresno Apartments Fetch $44M in First-Ever Sale, Disposition / Exit - California - Marcus & Millichap Closes NorCal Seniors Housing Sale, Entitlement / Permitting - Beverly Hills / California - Beverly Hills upholds approval of Builder's Remedy project at 232 S. Tower Dr., Entitlement / Permitting - California - Meeting Today to Discuss 161 Rancho Drive in San Jose, General Project Signal - California - Interstate Equities Closes Institutional Fund at $215M, JV / Partnership - California - Mixed-use building rises at 450 The Promenade N. in Downtown Long Beach, JV / Partnership - Riverside / California - C&C Development Opens Affordable Housing in Irvine, Riverside / California, San Francisco / California, Santa Monica / California
- Fannie Mae: Fannie Mae, fannie mae
- Greystar: General Project Signal - Other / Unknown - Greystar Receives State Funding Award to Redevelop Taunton’s Whittenton Mills, Greystar
- Greystone: Greystone, Refinancing - Other / Unknown - Greystone Lends $47M for Long Island Section 8 Housing Complex
- JLL: Disposition / Exit - Other / Unknown - JLL Arranges Sale of 1000 Jefferson a 217-Unit Multifamily Community in One of New Jersey’..., JLL, JV / Partnership - Dallas / Texas - JLL Nabs Listing for 345-Unit Uptown Dallas Apartment Tower, jll
- Kennedy Wilson: Kennedy Wilson, Office-to-Residential Conversion - Santa Monica / California - Kennedy Wilson plans 133 apartments at 700 Colorado Ave. in Santa Monica, kennedy wilson
- Los Angeles: Acquisition - Atlanta / Georgia - Lion Real Estate Picks Up Atlanta Apartments for $51M, Acquisition - Atlanta / Georgia - Walton Communities Offloads Two Atlanta Rental Properties, Acquisition - Miami / Florida - Avalon Bay Planning Apartments, Retail in South Miami, Acquisition - New York - ACP Negotiates Sale of 98-Unit Apartment Building in Slingerlands, New York, Atlanta / Georgia, Construction Financing - Miami / Florida - Fort Lauderdale Developer Inks Financing for Condos, Apartments, Retail, Dallas / Texas, Development Start - Atlanta / Georgia - Financing Secured for Centennial Yards Mixed-Use Project, Disposition / Exit - Los Angeles / California - 1929-Vintage Los Feliz Apartments Sell to Dream Street Capital, Disposition / Exit - Los Angeles / California - Sale of Oceanwide Plaza in DTLA Clears Hurdle with Bankruptcy Court Approval, Disposition / Exit - Los Angeles / California - Sony Pictures and Alamo Drafthouse to revive Hollywood's iconic Cinerama Dome, Entitlement / Permitting - Los Angeles / California - Mixed-use project planned at 1134 N. La Brea Ave. in West Hollywood, Entitlement / Permitting - Other / Unknown - Permits Filed for Affordable Housing at 430 Broadway in Oakland, Entitlement / Permitting - Other / Unknown - Signal Hill plans new zoning rules for "oil patch" district, General Project Signal - Atlanta / Georgia - Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project, General Project Signal - Dallas / Texas - Dallas Apartment Builder Inks $78.7M Refi, General Project Signal - Dallas / Texas - Oldham Goodwin Eyeing $71M Fort Worth Affordable Housing Project, General Project Signal - Los Angeles / California - Developer nabs financing for affordable housing at 14th & Wilshire in Santa Monica, JV / Partnership - Los Angeles / California - Bankruptcy court clears the way for Oceanwide Plaza sale, JV / Partnership - Los Angeles / California - CIM Group and Hulic Joint Venture Acquire West Hollywood Multifamily Apartment Property, JV / Partnership - Los Angeles / California - CIM Group, Hulic Acquire West Hollywood Apartment Property, JV / Partnership - Los Angeles / California - Leading Multifamily Developer Joint Venture to Build Luxury Affordable Housing Community i..., Los Angeles, Los Angeles / California
- New York: Construction Financing - New York City / New York - Dwight Capital Provides $66M HUD-Insured Construction Loan for Abilene Multifamily Project, General Project Signal - New York City / New York - M&T RCC Provides $141M Bridge Loan to Newly Built Turtle Bay Apartments, Manhattan, New York, New York City, New York City / New York, Recapitalization - New York City / New York - Grubb Properties Merges Funds To Create $1.9B Apartment REIT

## Weak Matches Needing Manual Review

- Adirondack Capital -> Adirondack Capital (40, gp_intelligence.csv)
- Adirondack Capital -> Adirondack Capital (40, institutional_relationships.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- AvalonBay -> AvalonBay (40, deal_pipeline.csv)
- AvalonBay -> AvalonBay (40, gp_intelligence.csv)
- AvalonBay -> AvalonBay (40, institutional_relationships.csv)
- AvalonBay -> AvalonBay (40, relationship_graph.csv)
- Bankruptcy Court Approval -> Bankruptcy Court Approval (40, gp_intelligence.csv)
- Bankruptcy Court Approval -> Bankruptcy Court Approval (40, institutional_relationships.csv)
- Bascom Group -> Bascom Group (40, deal_pipeline.csv)
- Bascom Group -> Bascom Group (40, gp_intelligence.csv)
- Bascom Group -> Bascom Group (40, institutional_relationships.csv)
- Bascom Group -> Bascom Group (40, relationship_graph.csv)
- Acquisition - San Francisco / California - Berkadia Facilitates Sale and Acquisition Financing of Multifamily Property Portfolio in t... -> Berkadia (60, relationship_graph.csv)
- Beverly Hills -> Beverly Hills (40, deal_pipeline.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
