# Routing Balance Report

- Market Intelligence count: 16
- Development Activity count: 55
- GP / Capital Activity count: 6
- Excluded count: 1
- Rent/Demand candidate count: 7
- Project anchor article count: 54
- Development-excluded transaction article count: 5
- Low-value promotional excluded count: 1
- Site / Parcel positive candidates count: 6
- Site / Parcel excluded transaction count: 0
- Source missing count: 0
- Market missing count: 0
- Stage missing count: 60

## Rent/Demand Titles
- Are rent concessions rising or falling? It’s complicated.
- Multifamily Absorption Rate Remains Below 50%
- Centralization Associated with Occupancy Uplift
- Rent Prices Continue to Rise, While Absorption Remains Low
- Spring leasing gains traction as apartment supply pressure eases
- Multifamily Developer Confidence Holds Steady in First Quarter
- Multifamily Developer Confidence Increases in Third Quarter, But Still in Negative Territory

## Excluded Promotional Articles
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | chat-with-chief-economist promotional format

## Site / Parcel Included Examples
- 19-story high-rise starts work at 6055 Center Drive in Westchester | Development Activity | site/parcel signal with project anchor: parcel
- Mixed-use project slated for 9700 W. Pico Blvd. in Pico-Robertson | Development Activity | site/parcel signal with project anchor: development site
- Proposed apartments face appeal at 3411 Foothill Blvd. in Glendale | Development Activity | site/parcel signal with project anchor: acres + development/site signal
- Seco Planning 12-Story, $100M FW Apartment Highrise | Development Activity | site/parcel signal with project anchor: to build
- W. Palm Beach Developer Eyeing 25-Story Apartment Tower | Development Activity | site/parcel signal with project anchor: to build
- Portman Targeting Duluth for Mixed-Use Project | Development Activity | site/parcel signal with project anchor: to build

## Site / Parcel Excluded Transaction Examples
- None

## Sample Validation
- The Market Data that Matters for the rest of 2026: A Chat with Zillow’s Chief Economist | Excluded | rent_demand=No | low_value_promotional: chat-with-chief-economist promotional format
- Cushman & Wakefield Represents The Green Companies in the Sale of Green House Multifamily Development in Miami | Development Activity | rent_demand=No | development_project_anchor: capital event with identifiable project/asset (unit/site count: 14-story; project/asset term: development)
- Seachange Partners Makes its Debut with Two Affordable Multifamily Developments in Los Angeles Arranged by Berkadia | Development Activity | rent_demand=No | development_project_anchor: project financing/capital event tied to project (address/street: 1711 corinth avenue; project/asset term: project; project financing tied to anchor: construction financing)
- IZO Capital Launches $120M Structured Finance Platform for Multifamily Rental Housing Development | GP / Capital Activity | rent_demand=No | gp_capital_platform: lending platform without project anchor
- 19-story high-rise starts work at 6055 Center Drive in Westchester | Development Activity | rent_demand=No | development_project_anchor: Approval / Entitlement (unit/site count: 19-story; address/street: 6055 center drive; site/parcel signal: site; project/asset term: project)
- Mixed-use project slated for 9700 W. Pico Blvd. in Pico-Robertson | Development Activity | rent_demand=No | development_project_anchor: Approval / Entitlement (unit/site count: 73-acre; address/street: 9700 w. pico blvd; site/parcel signal: site; project/asset term: project)
- Affordable housing proposed for 23022 W. Ventura Blvd. in Woodland Hills | Development Activity | rent_demand=No | development_project_anchor: Approval / Entitlement (address/street: 23022 w. ventura blvd; execution milestone: proposed; site/parcel signal: site; project/asset term: project)
- Proposed apartments face appeal at 3411 Foothill Blvd. in Glendale | Development Activity | rent_demand=No | development_project_anchor: Approval / Entitlement (address/street: 3411 foothill blvd; execution milestone: proposed; project/asset term: project)
- Construction begins for affordable housing at 4151 E. Fountain Ave. in Long Beach | Development Activity | rent_demand=No | development_project_anchor: Construction Start (address/street: 4151 e. fountain ave; execution milestone: groundbreaking; project/asset term: development)
- Construction kicks off for affordable housing at 706 W. 85th Street in South L.A. | Development Activity | rent_demand=No | development_project_anchor: Construction Start (address/street: 706 w. 85th street; execution milestone: groundbreaking; project/asset term: project)