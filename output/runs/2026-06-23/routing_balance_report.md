# Routing Balance Report

- Market Intelligence count: 16
- Development Activity count: 55
- GP / Capital Activity count: 2
- Excluded count: 2
- Rent/Demand candidate count: 4
- Project anchor article count: 52
- Development-excluded transaction article count: 3
- Low-value promotional excluded count: 2
- Site / Parcel positive candidates count: 5
- Site / Parcel excluded transaction count: 1
- Source missing count: 0
- Market missing count: 0
- Stage missing count: 55

## Rent/Demand Titles
- Multifamily Absorption Rate Remains Below 50%
- Rent Prices Continue to Rise, While Absorption Remains Low
- Multifamily Developer Confidence Holds Steady in First Quarter
- Multifamily Developer Confidence Increases in Third Quarter, But Still in Negative Territory

## Excluded Promotional Articles
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | chat-with-chief-economist promotional format
- What Today’s Renters Want From Their Property Managers | promotional/event keyword: sponsored

## Site / Parcel Included Examples
- Linc Housing plans new project at 3590 Elm Ave. in Long Beach | Development Activity | site/parcel signal with project anchor: to build
- Yorba Linda Parking Lot Sells for Townhome Redevelopment | Development Activity | site/parcel signal with project anchor: development site
- New York Developer Seeks to Build 296 Units in Flushing, Queens | Development Activity | site/parcel signal with project anchor: to build
- Former IHOP Site in Pacific Beach Trades as Redevelopment Opportunity | Development Activity | site/parcel signal with project anchor: development site
- Portman Targeting Duluth for Mixed-Use Project | Development Activity | site/parcel signal with project anchor: to build

## Site / Parcel Excluded Transaction Examples
- Miami-Dade County Sells Apartment Site for $10 | Development Activity | operating-asset transaction guard

## Sample Validation
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | Excluded | rent_demand=No | low_value_promotional: chat-with-chief-economist promotional format
- Berkadia Negotiates $6M Multifamily Sale in Lawndale California | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (unit/site count: 24-unit; project/asset term: apartments)
- Marcus & Millichap Brokers $19.75M Sale and $13.3M Financing of 64-Unit Multifamily Property in Livermore California | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (unit/site count: 64-unit; project/asset term: apartments; project financing tied to anchor: acquisition financing)
- S3 Capital Lends $102M for Hell’s Kitchen Office-to-Resi Conversion | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (address/street: 311 west 43rd street; project/asset term: apartments; project financing tied to anchor: construction financing)
- Peachtree Lends $44M on Florida Panhandle Multifamily Project | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (execution milestone: lease-up; project/asset term: project)
- CBRE Arranges Sale of Townhomes in Kenosha | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (unit/site count: 32-unit; project/asset term: community)
- Walker & Dunlop Arranges $375M Loan for Jersey City Mixed-Use | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (project/asset term: development; project financing tied to anchor: construction loan)
- Affordable housing takes shape at 733 S. Burlington Ave. in Westlake | Development Activity | rent_demand=No | development_project_anchor: Approval / Entitlement (address/street: 733 s. burlington ave; site/parcel signal: site; project/asset term: project)
- Linc Housing plans new project at 3590 Elm Ave. in Long Beach | Development Activity | rent_demand=No | development_project_anchor: Project / Asset (address/street: 3590 elm ave; execution milestone: to build; project/asset term: project)
- Work beginning for Taix redevelopment at 1911 Sunset Blvd. in Echo Park | Development Activity | rent_demand=No | development_project_anchor: Approval / Entitlement (address/street: 1911 sunset blvd; project/asset term: project)