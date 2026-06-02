# Routing Regression Report

## Project-First Routing Summary

- Market Intelligence count: 15
- Development Activity count: 57
- GP / Capital Activity count: 5
- Project anchor article count: 53

## Regression Samples

- PASS | expected Development Activity | actual Development Activity | PCCP, Alliance Residential Snap Up Garden-Style Riverside Complex | anchor=True | reason=development_project_anchor: capital event with identifiable project/asset (unit/site count: 184-unit; address/street: 9170 indiana ave; execution milestone: delivered; project/asset term: community)
- PASS | expected Development Activity | actual Development Activity | Alta Developers Lands $91.8M Construction Loan for Miami Apartments | anchor=True | reason=development_project_anchor: project financing/capital event tied to project (unit/site count: 314-unit; address/street: 6075 sunset drive; site/parcel signal: drive; project/asset term: project; project financing tied to anchor: construction loan)
- PASS | expected Development Activity | actual Development Activity | Partnership Breaks Ground on $147M Affordable Housing Redevelopment in Poughkeepsie, New York | anchor=True | reason=development_project_anchor: capital event with identifiable project/asset (unit/site count: 69 apartments; execution milestone: breaks ground; project/asset term: development)
- PASS | expected Development Activity | actual Development Activity | Basis Investment Group Secures $43M Refinancing for Newly Built Philadelphia MF | anchor=True | reason=development_project_anchor: project financing/capital event tied to project (execution milestone: lease-up; project/asset term: development; project financing tied to anchor: construction loan)
- PASS | expected Development Activity | actual Development Activity | JLL Arranges $252M Financing for Huntington Beach Seniors Project | anchor=True | reason=development_project_anchor: capital event with identifiable project/asset (unit/site count: 214-unit; project/asset term: project; named asset/project hint: huntington beach)
- PASS | expected Development Activity | actual Development Activity | Portman Targeting Duluth for Mixed-Use Project | anchor=True | reason=development_project_anchor: Project / Asset (unit/site count: 55 acres; execution milestone: targeting; project/asset term: project; named asset/project hint: duluth)
- MISSING | expected Development Activity | Aventon to Build 270-Unit Port Richey Rental Community
- PASS | expected Development Activity | actual Development Activity | First Projects Advance Under San Francisco's New Zoning Plan, But Costs Hold Pipeline To A Trickle | anchor=True | reason=development_project_anchor: Delivery / Opening (execution milestone: opened; project/asset term: project)
- PASS | expected Development Activity | actual Development Activity | Jefferson Apartment Group Delivers Luxury Multifamily Community J Optimist Park in Charlotte North Carolina | anchor=True | reason=development_project_anchor: Delivery / Opening (unit/site count: 350-unit; address/street: 1130 n. college street; execution milestone: delivers; site/parcel signal: street; project/asset term: development)
- PASS | expected GP / Capital Activity | actual GP / Capital Activity | Berkshire Hathaway acquires BTR player Taylor Morrison for $8.5B | anchor=False | reason=gp_capital_corporate_mna: acquires btr player
- PASS | expected GP / Capital Activity | actual GP / Capital Activity | Blackstone Real Estate Debt Strategies Launches Homebuilder Lending Platform | anchor=False | reason=gp_capital_platform: lending platform without project anchor
- PASS | expected Market Intelligence | actual Market Intelligence | Rent growth is positive for the month of May | anchor=False | reason=market_macro_guard: rent, demand, vacancy, absorption, or leasing article without project anchor
- PASS | expected Market Intelligence | actual Market Intelligence | Multifamily construction spending lower in April | anchor=False | reason=generic policy, market, or research article excluded from Development Activity
- PASS | expected Market Intelligence | actual Market Intelligence | Rent Prices Continue to Rise, While Absorption Remains Low | anchor=False | reason=market_macro_guard: rent, demand, vacancy, absorption, or leasing article without project anchor

## Result

- Checked samples present in current run: 13
- Passed expected section: 13
- Missing sample titles: 1