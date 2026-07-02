# Routing Balance Report

- Market Intelligence count: 17
- Development Activity count: 66
- GP / Capital Activity count: 2
- Excluded count: 2
- Rent/Demand candidate count: 5
- Project anchor article count: 61
- Development-excluded transaction article count: 2
- Low-value promotional excluded count: 2
- Site / Parcel positive candidates count: 5
- Site / Parcel excluded transaction count: 2
- Source missing count: 0
- Market missing count: 0
- Stage missing count: 67

## Rent/Demand Titles
- Multifamily Absorption Rate Remains Below 50%
- Centralization Associated with Occupancy Uplift
- Rent Prices Continue to Rise, While Absorption Remains Low
- Multifamily Developer Confidence Holds Steady in First Quarter
- Multifamily Developer Confidence Increases in Third Quarter, But Still in Negative Territory

## Excluded Promotional Articles
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | chat-with-chief-economist promotional format
- 2026 Resident Experience Management Report | promotional/event keyword: whitepaper

## Site / Parcel Included Examples
- Affordable housing takes shape at 1734 S. Barrington Ave. in Sawtelle | Development Activity | site/parcel signal with project anchor: former site
- Yorba Linda Parking Lot Sells for Townhome Redevelopment | Development Activity | site/parcel signal with project anchor: development site
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project | Development Activity | site/parcel signal with project anchor: to build
- Dezer Advancing Plan for 600 N. Miami Apartment Units | Development Activity | site/parcel signal with project anchor: to build
- Portman Targeting Duluth for Mixed-Use Project | Development Activity | site/parcel signal with project anchor: to build

## Site / Parcel Excluded Transaction Examples
- BridgeCity Lends $72M on Long Island City Apartments Build | Development Activity | operating-asset transaction guard
- Miami-Dade County Sells Apartment Site for $10 | Development Activity | operating-asset transaction guard

## Sample Validation
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | Excluded | rent_demand=No | low_value_promotional: chat-with-chief-economist promotional format
- Marcus & Millichap Publishes Atlanta Multifamily 2Q 2026 Market Report | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (address/street: 1850 apple valley drive; project/asset term: apartments)
- Marcus & Millichap Publishes Charlotte Multifamily 2Q 2026 Market Report | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (address/street: 9517 newell hickory grove road; project/asset term: apartments)
- BridgeCity Lends $72M on Long Island City Apartments Build | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (address/street: 68 vernon boulevard; execution milestone: to build; site/parcel signal: site; project/asset term: development; project financing tied to anchor: construction financing)
- JV Plans 4,000 Affordable Units in L.A., Starting With Former World Trade Center | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (unit/site count: 512-unit; address/street: 333 flower street; project/asset term: development)
- Affordable housing commences work at 825 Hyperion Ave. in Silver Lake | Development Activity | rent_demand=No | development_project_anchor: Project / Asset (unit/site count: 105 apartments; address/street: 825 hyperion ave; project/asset term: apartments)
- Affordable housing takes shape at 1734 S. Barrington Ave. in Sawtelle | Development Activity | rent_demand=No | development_project_anchor: Approval / Entitlement (address/street: 1734 s. barrington ave; site/parcel signal: site; project/asset term: project)
- Construction commences for mixed-use project at 2025 and 2051 Wilshire in Santa Monica | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (address/street: 2025 wilshire blvd; project/asset term: project; project financing tied to anchor: construction loan)
- Developer revises proposal for apartments at 4728 San Fernando Rd. in Glendale | Development Activity | rent_demand=No | development_project_anchor: Approval / Entitlement (address/street: 4728 san fernando rd; project/asset term: development)
- Adaptive reuse to create affordable housing at 521 and 530 E. 4th St. in Long Beach | Development Activity | rent_demand=No | development_project_anchor: Project / Asset (unit/site count: 15-story; address/street: 521 and 530 e. 4th st; site/parcel signal: site; project/asset term: development)