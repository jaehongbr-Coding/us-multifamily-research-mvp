# Routing Balance Report

- Market Intelligence count: 16
- Development Activity count: 59
- GP / Capital Activity count: 1
- Excluded count: 1
- Rent/Demand candidate count: 5
- Project anchor article count: 58
- Development-excluded transaction article count: 2
- Low-value promotional excluded count: 1
- Site / Parcel positive candidates count: 5
- Site / Parcel excluded transaction count: 1
- Source missing count: 0
- Market missing count: 0
- Stage missing count: 57

## Rent/Demand Titles
- Multifamily Absorption Rate Remains Below 50%
- Centralization Associated with Occupancy Uplift
- Rent Prices Continue to Rise, While Absorption Remains Low
- Multifamily Developer Confidence Holds Steady in First Quarter
- Multifamily Developer Confidence Increases in Third Quarter, But Still in Negative Territory

## Excluded Promotional Articles
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | chat-with-chief-economist promotional format

## Site / Parcel Included Examples
- Mesa West Capital Joint Venture Provides $83M for Seattle Multifamily Apartment Community Olin Fields | Development Activity | site/parcel signal with project anchor: acres + development/site signal
- Yorba Linda Parking Lot Sells for Townhome Redevelopment | Development Activity | site/parcel signal with project anchor: development site
- Developer Buys Land Near Charlotte Transit Station, Apartments on Way | Development Activity | site/parcel signal with project anchor: acquired land
- S3 Capital Lends $101M on Luxury Resort Project Near Orlando | Development Activity | site/parcel signal with project anchor: to build
- Portman Targeting Duluth for Mixed-Use Project | Development Activity | site/parcel signal with project anchor: to build

## Site / Parcel Excluded Transaction Examples
- Miami-Dade County Sells Apartment Site for $10 | Development Activity | operating-asset transaction guard

## Sample Validation
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | Excluded | rent_demand=No | low_value_promotional: chat-with-chief-economist promotional format
- GID Secures $68M Refinancing for Luxury Austin Multifamily Asset Eleven by Windsor | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (unit/site count: 257-unit)
- The Connor Group Acquires $52M Louisville Luxury Multifamily Property | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (unit/site count: 270-unit; project/asset term: community)
- Camden Property Acquires Multifamily Apartment Asset for $43.5M in Nashville | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (unit/site count: 196-unit; project/asset term: community)
- North American Development Group Begins Work on 476-Unit Delray Beach Rental Community | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (unit/site count: 476-unit; execution milestone: broke ground; site/parcel signal: site; project/asset term: development; project financing tied to anchor: construction loan)
- Mesa West Capital Joint Venture Provides $83M for Seattle Multifamily Apartment Community Olin Fields | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (unit/site count: 352-unit; project/asset term: community)
- KeyBank Provides $56M in Financing for Midwest Seniors Multifamily Housing | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (unit/site count: 96-unit; project/asset term: project; project financing tied to anchor: construction loan)
- 22-Property NJ Workforce Portfolio Refinanced for $38M | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (project/asset term: apartments)
- New-Construction San Diego Apartments Score $53M Bridge Loan | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (unit/site count: 137-unit; address/street: 3090 polk ave; execution milestone: delivered; project/asset term: community)
- Affordable housing on the rise at 1405 S. Broadway in DTLA | Development Activity | rent_demand=No | development_project_anchor: Project / Asset (unit/site count: 303 units; site/parcel signal: site; project/asset term: project)