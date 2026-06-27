# Routing Balance Report

- Market Intelligence count: 15
- Development Activity count: 50
- GP / Capital Activity count: 1
- Excluded count: 2
- Rent/Demand candidate count: 4
- Project anchor article count: 48
- Development-excluded transaction article count: 2
- Low-value promotional excluded count: 2
- Site / Parcel positive candidates count: 4
- Site / Parcel excluded transaction count: 1
- Source missing count: 0
- Market missing count: 0
- Stage missing count: 53

## Rent/Demand Titles
- Multifamily Absorption Rate Remains Below 50%
- Rent Prices Continue to Rise, While Absorption Remains Low
- Multifamily Developer Confidence Holds Steady in First Quarter
- Multifamily Developer Confidence Increases in Third Quarter, But Still in Negative Territory

## Excluded Promotional Articles
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | chat-with-chief-economist promotional format
- What Today’s Renters Want From Their Property Managers | promotional/event keyword: sponsored

## Site / Parcel Included Examples
- Yorba Linda Parking Lot Sells for Townhome Redevelopment | Development Activity | site/parcel signal with project anchor: development site
- Developer Buys Land Near Charlotte Transit Station, Apartments on Way | Development Activity | site/parcel signal with project anchor: acquired land
- S3 Capital Lends $101M on Luxury Resort Project Near Orlando | Development Activity | site/parcel signal with project anchor: to build
- Portman Targeting Duluth for Mixed-Use Project | Development Activity | site/parcel signal with project anchor: to build

## Site / Parcel Excluded Transaction Examples
- Miami-Dade County Sells Apartment Site for $10 | Development Activity | operating-asset transaction guard

## Sample Validation
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | Excluded | rent_demand=No | low_value_promotional: chat-with-chief-economist promotional format
- 22-Property NJ Workforce Portfolio Refinanced for $38M | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (project/asset term: apartments)
- New-Construction San Diego Apartments Score $53M Bridge Loan | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (unit/site count: 137-unit; address/street: 3090 polk ave; execution milestone: delivered; project/asset term: community)
- Affordable housing on the rise at 1405 S. Broadway in DTLA | Development Activity | rent_demand=No | development_project_anchor: Project / Asset (unit/site count: 303 units; site/parcel signal: site; project/asset term: project)
- 100 rental townhomes deput at 1771 Blake Ave. in Frogtown | Development Activity | rent_demand=No | development_project_anchor: Leasing / Lease-Up (address/street: 1771 blake ave; execution milestone: leasing; site/parcel signal: site; project/asset term: project)
- Affordable housing fully-framed at 4129 Centinela Ave. in Del Rey | Development Activity | rent_demand=No | development_project_anchor: Project / Asset (address/street: 4129 centinela ave; site/parcel signal: site; project/asset term: project)
- Construction goes vertical for mixed-use project at 1902 Wilshire Blvd. in Santa Monica | Development Activity | rent_demand=No | development_project_anchor: Project / Asset (address/street: 1902 wilshire blvd; project/asset term: project)
- Affordable housing under constructiona t 1740 N. Wilton Place in Hollywood | Development Activity | rent_demand=No | development_project_anchor: Approval / Entitlement (site/parcel signal: site; project/asset term: project)
- Affordable housing takes shape at 733 S. Burlington Ave. in Westlake | Development Activity | rent_demand=No | development_project_anchor: Approval / Entitlement (address/street: 733 s. burlington ave; site/parcel signal: site; project/asset term: project)
- KeyBank Provides $56M in Construction Financing for Ohio Affordable Seniors Housing Project | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (project/asset term: project; project financing tied to anchor: construction loan)