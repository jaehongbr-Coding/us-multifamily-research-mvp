# Routing Balance Report

- Market Intelligence count: 19
- Development Activity count: 66
- GP / Capital Activity count: 9
- Excluded count: 2
- Rent/Demand candidate count: 7
- Project anchor article count: 60
- Development-excluded transaction article count: 8
- Low-value promotional excluded count: 2
- Site / Parcel positive candidates count: 8
- Site / Parcel excluded transaction count: 0
- Source missing count: 0
- Market missing count: 0
- Stage missing count: 75

## Rent/Demand Titles
- Multifamily Market Sees Strongest Demand Since Mid-2024 As Asking Rents Dip
- Multifamily Absorption Rate Remains Below 50%
- Centralization Associated with Occupancy Uplift
- Rent Prices Continue to Rise, While Absorption Remains Low
- Multifamily Developer Confidence Holds Steady in First Quarter
- Multifamily Developer Confidence Increases in Third Quarter, But Still in Negative Territory
- South Florida Retail Markets Show Sub-5% Vacancy

## Excluded Promotional Articles
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | chat-with-chief-economist promotional format
- 2026 Resident Experience Management Report | promotional/event keyword: whitepaper

## Site / Parcel Included Examples
- Ponce Bank Lends $50M for Canarsie Apartments | Development Activity | site/parcel signal with project anchor: to build
- Financing Secured for Centennial Yards Mixed-Use Project | Development Activity | site/parcel signal with project anchor: plans to build
- Apartment Developer Pursuing Phillips Place for Multifamily Community | Development Activity | site/parcel signal with project anchor: to build
- Developer Duo Adding 350 Apartments to Dunwoody Mixed-Use Project | Development Activity | site/parcel signal with project anchor: to build
- Developer Acquires Los Angeles Site for Multifamily Affordable Housing Project | Development Activity | site/parcel signal with project anchor: parcel
- Dezer Advancing Plan for 600 N. Miami Apartment Units | Development Activity | site/parcel signal with project anchor: to build
- Nicholas & Associates to Build 263-Unit Luxury Apartment Community in Madison, Wisconsin | Development Activity | site/parcel signal with project anchor: to build
- New Housing Law To Send Institutional Investors Flocking To Build-To-Rent | Development Activity | site/parcel signal with project anchor: to build

## Site / Parcel Excluded Transaction Examples
- None

## Sample Validation
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | Excluded | rent_demand=No | low_value_promotional: chat-with-chief-economist promotional format
- 320-Unit Gilbert Multifamily Apartment Community Sells to Camden Living | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (unit/site count: 320-unit; project/asset term: community)
- Cushman & Wakefield Arranges $59M for Luxury Washington DC Multifamily Property The Ellington | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (unit/site count: 190-unit; address/street: 1301 u street; project/asset term: multifamily property)
- Walker & Dunlop Arranges $46.5M Refinance Loan for Austin-Area Multifamily Rental Community | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (project/asset term: community)
- Ponce Bank Lends $50M for Canarsie Apartments | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (address/street: 951 east 108th street; execution milestone: to build; project/asset term: project; project financing tied to anchor: construction financing)
- Greystone Real Estate Capital Closes $137M Affordable Housing Development Fund | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (project/asset term: development; project financing tied to anchor: construction financing)
- Greystar Sells Virginia Apartment Tower for $216M | GP / Capital Activity | rent_demand=No | headline-level GP, transaction, financing, or capital event detected
- Greystone Real Estate Capital Closes on Second Affordable Housing Fund | GP / Capital Activity | rent_demand=No | property-level financing, lender, refinancing, or recapitalization signal detected
- Apartments under construction at 5547 N. Elmer Ave. in North Hollywood | Development Activity | rent_demand=No | development_project_anchor: Approval / Entitlement (address/street: 5547 n. elmer ave; site/parcel signal: site; project/asset term: project)
- 525 apartments start to rise at 22107 S. Vermont Ave. in West Carson | Development Activity | rent_demand=No | development_project_anchor: Project / Asset (unit/site count: 525 apartments; address/street: 22107 s. vermont ave; project/asset term: development)