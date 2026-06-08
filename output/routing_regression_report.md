# Routing Regression Report

## Project-First Routing Summary

- Market Intelligence count: 20
- Development Activity count: 62
- GP / Capital Activity count: 8
- Project anchor article count: 58

## Regression Samples

- MISSING | expected Development Activity | PCCP, Alliance Residential Snap Up Garden-Style Riverside Complex
- PASS | expected Development Activity | actual Development Activity | Alta Developers Lands $91.8M Construction Loan for Miami Apartments | anchor=True | reason=development_project_anchor: project financing/capital event tied to project (unit/site count: 314-unit; address/street: 6075 sunset drive; project/asset term: project; project financing tied to anchor: construction loan; named asset/project hint: alta )
- MISSING | expected Development Activity | Partnership Breaks Ground on $147M Affordable Housing Redevelopment
- MISSING | expected Development Activity | Basis Investment Group Secures $43M Financing for Newly Built Philadelphia MF
- PASS | expected Development Activity | actual Development Activity | JLL Arranges $252M Financing for Huntington Beach Seniors Project | anchor=True | reason=development_project_anchor: capital event with identifiable project/asset (unit/site count: 214-unit; project/asset term: project; named asset/project hint: huntington beach)
- PASS | expected Development Activity | actual Development Activity | Portman Targeting Duluth for Mixed-Use Project | anchor=True | reason=development_project_anchor: Project / Asset (unit/site count: 55 acres; execution milestone: targeting; project/asset term: project; named asset/project hint: duluth)
- MISSING | expected Development Activity | Aventon to Build 270-Unit Port Richey Rental Community
- MISSING | expected Development Activity | First Projects Advance Under San Francisco's New Zoning Plan
- MISSING | expected Development Activity | Jefferson Apartment Group Delivers Luxury Multifamily Community
- MISSING | expected GP / Capital Activity | Berkshire Hathaway acquires BTR player Taylor Morrison
- MISSING | expected GP / Capital Activity | Blackstone Real Estate Debt Strategies Launches Homebuilder Lending Platform
- MISSING | expected Market Intelligence | Rent growth is positive for the month of May
- MISSING | expected Market Intelligence | Multifamily construction spending lower in April
- PASS | expected Market Intelligence | actual Market Intelligence | Rent Prices Continue to Rise, While Absorption Remains Low | anchor=False | reason=market_macro_guard: rent, demand, vacancy, absorption, or leasing article without project anchor

## Result

- Checked samples present in current run: 4
- Passed expected section: 4
- Missing sample titles: 10