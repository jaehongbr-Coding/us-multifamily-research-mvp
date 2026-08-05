# Routing Balance Report

- Market Intelligence count: 15
- Development Activity count: 70
- GP / Capital Activity count: 6
- Excluded count: 2
- Rent/Demand candidate count: 4
- Project anchor article count: 67
- Development-excluded transaction article count: 7
- Low-value promotional excluded count: 2
- Site / Parcel positive candidates count: 4
- Site / Parcel excluded transaction count: 0
- Source missing count: 0
- Market missing count: 0
- Stage missing count: 65

## Rent/Demand Titles
- Multifamily Absorption Rate Remains Below 50%
- Rent Prices Continue to Rise, While Absorption Remains Low
- Multifamily Developer Confidence Holds Steady in First Quarter
- Multifamily Developer Confidence Increases in Third Quarter, But Still in Negative Territory

## Excluded Promotional Articles
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | chat-with-chief-economist promotional format
- 2026 Resident Experience Management Report | promotional/event keyword: whitepaper

## Site / Parcel Included Examples
- Development Site with Uncommonly Long Frontage Sells in Brooklyn | Development Activity | site/parcel signal with project anchor: development site
- Blackstone Affiliate Proposing 252 Affordable Denton Housing Units | Development Activity | site/parcel signal with project anchor: to build
- Financing Secured for Centennial Yards Mixed-Use Project | Development Activity | site/parcel signal with project anchor: plans to build
- New Permits Filed for Apartments at 5139 MacArthur Boulevard in Oakland | Development Activity | site/parcel signal with project anchor: parcel

## Site / Parcel Excluded Transaction Examples
- None

## Sample Validation
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | Excluded | rent_demand=No | low_value_promotional: chat-with-chief-economist promotional format
- Capital City Real Estate Closes Construction Financing for 318-Unit Spivey Grove Multifamily Community in Stockbridge Georgia | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (unit/site count: 318-unit; address/street: 138 and spivey road; project/asset term: development; project financing tied to anchor: construction financing)
- IZO Capital Closes $25.6M Workforce Housing Construction Loan Near Jackson Hole Wyoming | GP / Capital Activity | rent_demand=No | gp_capital_platform: lending platform without project anchor
- Berkadia Arranges $19.1M Financing for Miami Based Investors Acquisition of Build-to-Rent Community in Greater Orlando | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (address/street: 101 single-family rental homes in st; project/asset term: community)
- Concord Summit Capital Arranges $50M Construction Loan for 268-Unit Multifamily Project in Fort Worth Texas | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (unit/site count: 268-unit; project/asset term: project; project financing tied to anchor: construction loan)
- The Richman Group Closes $225M in Permanent Financing Across Three Florida Luxury Multifamily Apartment Communities | GP / Capital Activity | rent_demand=No | property-level financing, lender, refinancing, or recapitalization signal detected
- Marcus & Millichap Brokers $9.75M Sale and $7.3M Financing of 73-Unit Multifamily Property in Oakland California | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (unit/site count: 73-unit; project/asset term: apartments; project financing tied to anchor: acquisition financing)
- Development Site with Uncommonly Long Frontage Sells in Brooklyn | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (site/parcel signal: site; project/asset term: development)
- Marcus & Millichap Finalizes Deal in Sacramento’s Greenhaven Neighborhood | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (unit/site count: 34-unit; address/street: 915 johnfer way; project/asset term: apartments)
- New look for 353-unit development at 1633 26th St. in Santa Monica | Development Activity | rent_demand=No | development_project_anchor: Project / Asset (unit/site count: 353-unit; address/street: 1633 26th st; execution milestone: proposed; project/asset term: project)