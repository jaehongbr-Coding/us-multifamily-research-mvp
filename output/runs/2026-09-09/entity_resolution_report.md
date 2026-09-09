# Entity Resolution Report

Generated: 2026-09-09 01:05:06

- Total raw entities reviewed: 265
- Total canonical entities created: 66
- Possible duplicate entity groups: 11
- Weak matches needing review: 191
- Unknown entities needing review: 4

## Top Canonical Firms

- Unknown: 150 occurrence(s)
- Berkadia: 21 occurrence(s)
- Marcus & Millichap: 20 occurrence(s)
- Brookfield: 15 occurrence(s)
- CBRE: 9 occurrence(s)
- Kennedy Wilson: 9 occurrence(s)
- Fannie Mae: 8 occurrence(s)
- Freddie Mac: 8 occurrence(s)
- JLL: 8 occurrence(s)
- AvalonBay: 7 occurrence(s)

## Top Canonical Markets

- Sun Belt: 67 occurrence(s)
- California: 45 occurrence(s)
- Los Angeles: 42 occurrence(s)
- Other / Unknown: 37 occurrence(s)
- New York: 24 occurrence(s)
- National: 22 occurrence(s)
- Unknown: 13 occurrence(s)
- South Florida: 12 occurrence(s)
- Santa Monica: 6 occurrence(s)
- Arizona: 5 occurrence(s)

## Possible Duplicate Entities

- Berkadia: Berkadia, General Project Signal - Other / Unknown - Berkadia Secures $12M in LIHTC Equity for Michigan Housing Property, berkadia
- Brookfield: Brookfield, brookfield
- CBRE: CBRE, cbre
- California: Acquisition - California - MBK Rental Living, Haseko Sell 315-Unit Zia Multifamily Community in Anaheim, Acquisition - California - Mixed-use project rises at 1801 E. 4th St. in Santa Ana, Acquisition - California - Tishman Speyer Acquires 376-Unit Anaheim Rental Community, Acquisition - Riverside / California - What multifamily firms bought and sold this summer, California, Construction Financing - California - CEDARst Snags $80M Construction Loan for San Diego Apartments, Disposition / Exit - California - Marcus & Millichap Closes Sale of Bay Area Assisted Living, Disposition / Exit - Santa Monica / California - Marcus & Millichap Brokers Two Santa Monica Multifamily Portfolio Sales, Disposition / Exit - Santa Monica / California - Marcus & Millichap Brokers Two Santa Monica Multifamily Sales Each Exceeding $1M Per Unit, Entitlement / Permitting - California - Rendering vs. Reality: Apartments at 1408 W. Jefferson Blvd. in Exposition Park, General Project Signal - California - WNC Closes on 23rd California-Focused Affordable Housing Fund, Riverside / California, San Francisco / California, Santa Monica / California
- Fannie Mae: Fannie Mae, JV / Partnership - California - Newmark Arranges Fannie Mae Loan on San Clemente Active-Adult Complex, fannie mae
- Freddie Mac: Freddie Mac, freddie mac
- JLL: JLL, jll
- Kennedy Wilson: General Project Signal - Atlanta / Georgia - Kennedy Wilson, Shimizu Corp. partner on $139M multifamily build in Georgia, Kennedy Wilson, kennedy wilson
- Los Angeles: Acquisition - Arizona - Evergreen Development Acquires 11.7 Acres in Mesa, Arizona, Plans Mixed-Use Project, Acquisition - Atlanta / Georgia - ParkProperty Acquires 280-Unit Buckhead Apartment Community, Acquisition - Atlanta / Georgia - Passco Offloads Buckhead Rental Asset for $87.5M, Acquisition - Atlanta / Georgia - Saratoga Capital Pays $98.4M at Auction for Atlanta Apartment Community, Acquisition - National - American Healthcare REIT Acquires Eight Senior Housing Communities for $696M, Atlanta / Georgia, Construction Financing - Los Angeles / California - Mixed-use building starts to rise at 8025 Santa Monica Blvd. in West Hollywood, Construction Financing - Miami / Florida - Shoma Group Obtains $172.5M C-PACE Loan for North Bay Village Development, Construction Financing - National - Gantry Secures $48.3M for Minnesota Class A Multifamily Construction Takeout Loan, Dallas / Texas, Development Start - Los Angeles / California - Construction begins for affordable housing at former MacLaren Hall site in El Monte, Disposition / Exit - Los Angeles / California - Metro scores $150M in federal funding for Vermont BRT Line, Disposition / Exit - Miami / Florida - Cortland Offloads 812 West Palm Beach Apartment Units for $208M, Entitlement / Permitting - Los Angeles / California - Sunset Boulevard bus lanes, Kroenke buys Angels, and more, Entitlement / Permitting - San Francisco / California - New Building Permits Filed In Balboa Reservoir Masterplan, San Francisco, General Project Signal - Dallas / Texas - Goldenrod Advancing $400M Fort Worth Mixed-Use Project, General Project Signal - Miami / Florida - Pinnacle Secures Financing for Fort Lauderdale Affordable Sr. Housing, General Project Signal - Miami / Florida - Terra Lands $245M Financing for Newly Completed Upland Park Development, General Project Signal - New York City / New York - GAIA Lands One-Year Extension on Williamsburg Multifamily Loan, General Project Signal - Texas - Oxbow Greenlit for Tobin Hill Apartments, Office Space, JV / Partnership - Other / Unknown - Building Permits Issued For West Oakland BART Affordable Housing, Los Angeles, Los Angeles / California, Office-to-Residential Conversion - Atlanta / Georgia - JLB Pursuing Buckhead Office-to-Apartments Conversion, Office-to-Residential Conversion - Los Angeles / California - Ian Schrager’s West Hollywood Hotel Redevelopment Scores $116M Bridge Financing
- New York: Acquisition - New York City / New York - New Empire Lines Up Three Manhattan Development Sites, Brooklyn, Construction Financing - New York City / New York - Affinius Capital Provides $310M Construction Loan for Jersey City Multifamily Project, Disposition / Exit - New York - Marcus & Millichap Arranges Sale of Multifamily Asset in Upstate New York, Disposition / Exit - New York City / New York - Mann Group Buys Luxury Apartments at 130 Hope Street in Williamsburg, Manhattan, New York, New York City / New York

## Weak Matches Needing Manual Review

- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, gp_intelligence.csv)
- Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital -> Acquires 280-Unit Buckhead Apartment Community ParkProperty Capital (40, institutional_relationships.csv)
- Acquisition - Other / Unknown - Marcus & Millichap Brokers $15.2M Sale of Chicago Apartment Building -> Acquisition - Other / Unknown - Marcus & Millichap Brokers $15.2M Sale of Chicago Apartment Building (40, relationship_graph.csv)
- Affinius Capital -> Affinius Capital (40, deal_pipeline.csv)
- Affinius Capital -> Affinius Capital (40, gp_intelligence.csv)
- Affinius Capital -> Affinius Capital (40, institutional_relationships.csv)
- Affinius Capital -> Affinius Capital (40, relationship_graph.csv)
- America -> America (40, deal_pipeline.csv)
- America -> America (40, relationship_graph.csv)
- Arizona -> Arizona (40, articles.csv)
- Arizona -> Arizona (40, deal_pipeline.csv)
- Arizona -> Arizona (40, regional_intelligence.csv)
- Arizona -> Arizona (40, relationship_graph.csv)
- AvalonBay -> AvalonBay (40, deal_pipeline.csv)
- AvalonBay -> AvalonBay (40, gp_intelligence.csv)

## Relationship Graph Improvement Notes

- Canonical source and target names are now written into relationship_graph.csv.
- Deal rows now include canonical GP/developer, lender, capital partner, and market fields.
- Weak and unknown entities should be reviewed before relying on multi-run network counts.

## Recommended Cleanup Actions

- Add confirmed aliases for repeated weak matches.
- Review unknown lender, capital partner, and project/deal entities.
- Expand the market alias dictionary when new submarkets appear repeatedly.
