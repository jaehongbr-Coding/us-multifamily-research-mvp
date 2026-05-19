# Entity Resolution Report

Generated: 2026-05-19 10:10:16

- Total raw entities reviewed: 127
- Total canonical entities created: 39
- Possible duplicate entity groups: 6
- Weak matches needing review: 82
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 107 occurrence(s)
- Blackstone: 8 occurrence(s)
- JLL: 8 occurrence(s)
- Hines: 7 occurrence(s)
- Quarterra: 7 occurrence(s)
- Camden Property Trust: 5 occurrence(s)
- cushman: 4 occurrence(s)
- walker & dunlop: 4 occurrence(s)
- CBRE: 2 occurrence(s)
- High Street Residential: 2 occurrence(s)

## Top Canonical Markets

- Los Angeles: 38 occurrence(s)
- Other / Unknown: 34 occurrence(s)
- Sun Belt: 33 occurrence(s)
- California: 27 occurrence(s)
- New York: 23 occurrence(s)
- Unknown: 15 occurrence(s)
- National: 5 occurrence(s)
- San Francisco: 4 occurrence(s)
- Houston: 2 occurrence(s)
- Arizona: 1 occurrence(s)

## Possible Duplicate Entities

- Blackstone: Blackstone, General Project Signal - New York - Ares Acquires Stake in Rover Pipeline from Blackstone Energy Transition Partners to Serve..., blackstone
- California: California, Entitlement / Permitting - California - Demolition Permits Filed For 772 Pacific Avenue in Chinatown, San Francisco, Office-to-Residential Conversion - California - Silicon Valley Initiative Partnership Receives $74.1M in Financing for Office-to-Residenti..., San Diego, Southern California
- JLL: Office-to-Residential Conversion - Sun Belt - JLL Inks 70,000 SF of New Leases at Westside Paper Adaptive Reuse Development in Atlanta, Refinancing - New York - JLL Capital Markets Announced They Arranged a $141.8M Refinancing for Premier Luxury River..., jll
- Los Angeles: Acquisition - California - WMC Commercial Buys Upland Village Green Multifamily Property in California for $48.5M, Development Start - California - California Transforms Oakland’s Fruitvale Community with Cleanup of Polluted Land for Affo..., Development Start - Los Angeles - The Broad's $100M expansion tops out in DTLA, Development Start - Other / Unknown - Major Development Groundbreaking on Landmark Multifamily Mixed-Use Community The Piazza at..., Disposition / Exit - California - Southern Land Company Launches Mortgage Division, Disposition / Exit - Los Angeles - Quarterra Seeks Buyers For Almost 4,000 Apartments, Disposition / Exit - Los Angeles - Walker & Dunlop Offer High-Profile Ground-Up Mixed-Use Development Opportunity Adjacent to..., Entitlement / Permitting - California - Formal Application Filed For Outer Richmond Safeway Redevelopment, San Francisco, Entitlement / Permitting - Los Angeles - 96 apartments + retail proposed at 8871 W. Venice Blvd., Entitlement / Permitting - Los Angeles - Site prep underway for affordable housing at 4301 S. Vermont Ave., Entitlement / Permitting - Other / Unknown - High Street Residential and Camden Property Trust Advance Durham North Carolina Apartment..., General Project Signal - Los Angeles - New proposal emerges for affordable housing at 1316 Linwood Ave. in Westlake, General Project Signal - Los Angeles - Soaring above the 17-acre One Beverly Hills site, General Project Signal - Los Angeles - Taylor Yard wetland takes shape, General Hospital update, and more, General Project Signal - Sun Belt - Grand Opening Celebration for Affordable Housing Development Palladium Park Row in the Kat..., JV / Partnership - Los Angeles - Lendlease, Aware Super Open Habitat Mixed-Use Campus in Los Angeles, L.A., La County, Los Angeles
- New York: Brooklyn, Construction Financing - New York - Merchants Capital, New York City Provide $42M for Brooklyn Affordable Housing, New York, Refinancing - New York - Barings Refis Williamsburg Wharf With $374M Loan, Refinancing - New York - Dermot Co. Receives $355M Loan for Refinancing of Upper Manhattan Apartment Tower
- Sun Belt: Acquisition - Sun Belt - 11North Acquires 285,497 SF Grocery-Anchored Retail Center in Altamonte Springs, Florida, Acquisition - Sun Belt - Milburn & Company Acquires Luxury 339-Unit Multifamily Community Ascend at Longbow Highpoi..., Atlanta, Austin, Dallas, Development Start - Sun Belt - Struggling To Find Equity, Developers Pull Back On New Builds, General Project Signal - Sun Belt - 13th Floor Secures $47M Loan and Breaks Ground on 222-Unit Venture on the Trail Multifamil..., Miami, Orlando, Phoenix, Sun Belt

## Weak Matches Needing Manual Review

- Arizona -> Arizona (40, regional_intelligence.csv)
- BTR / Build-to-Rent - Other / Unknown - Build-to-rent sale mandate cut from House’s ROAD to Housing bill -> BTR / Build-to-Rent - Other / Unknown - Build-to-rent sale mandate cut from House’s ROAD to Housing bill (40, relationship_graph.csv)
- BTR / Build-to-Rent - Other / Unknown - Cushman & Wakefield Brokers $26.4M Sale of Build-to-Rent Community in Matteson, Illinois -> BTR / Build-to-Rent - Other / Unknown - Cushman & Wakefield Brokers $26.4M Sale of Build-to-Rent Community in Matteson, Illinois (40, relationship_graph.csv)
- General Project Signal - New York - Ares Acquires Stake in Rover Pipeline from Blackstone Energy Transition Partners to Serve... -> Blackstone (60, relationship_graph.csv)
- Entitlement / Permitting - California - Demolition Permits Filed For 772 Pacific Avenue in Chinatown, San Francisco -> California (60, relationship_graph.csv)
- Office-to-Residential Conversion - California - Silicon Valley Initiative Partnership Receives $74.1M in Financing for Office-to-Residenti... -> California (60, relationship_graph.csv)
- Camden Property Trust -> Camden Property Trust (40, deal_pipeline.csv)
- Camden Property Trust -> Camden Property Trust (40, gp_intelligence.csv)
- Camden Property Trust -> Camden Property Trust (40, institutional_relationships.csv)
- Camden Property Trust -> Camden Property Trust (40, relationship_graph.csv)
- Construction Financing - Other / Unknown - Cypress Equity Investments gets $170M loan for two Santa Monica projects -> Construction Financing - Other / Unknown - Cypress Equity Investments gets $170M loan for two Santa Monica projects (40, relationship_graph.csv)
- Development Start - Other / Unknown - Fourth Quarter 2025 Multifamily Construction Data -> Development Start - Other / Unknown - Fourth Quarter 2025 Multifamily Construction Data (40, relationship_graph.csv)
- Development Start - Other / Unknown - Missing Middle Weakness -> Development Start - Other / Unknown - Missing Middle Weakness (40, relationship_graph.csv)
- Development Start - Other / Unknown - Overall Housing Starts Inch Lower in 2025 -> Development Start - Other / Unknown - Overall Housing Starts Inch Lower in 2025 (40, relationship_graph.csv)
- Development Start - Other / Unknown - Third Quarter 2025 Multifamily Construction Data -> Development Start - Other / Unknown - Third Quarter 2025 Multifamily Construction Data (40, relationship_graph.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
