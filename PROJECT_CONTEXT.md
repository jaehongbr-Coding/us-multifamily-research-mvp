# PROJECT_CONTEXT.md

## 1. 프로젝트 이름

US Residential Intelligence App

미국 주요 주거시장 뉴스 축적 및 정리 앱

---

## 2. 현재 앱 목표

이 프로젝트의 1차 목표는 미국 주요 주거시장 관련 뉴스를 안정적으로 수집하고, 시장/섹터/이벤트 태그별로 잘 정리해 축적하는 것이다.

기존에는 뉴스 스크랩 앱에서 시장 인텔리전스 앱으로 바로 확장하는 방향을 고려했지만, 현재 방향은 다음과 같이 재정의한다.

- 1단계: Core 15 + Watchlist 8 시장의 주거 관련 뉴스를 안정적으로 수집, 정리, 축적한다.
- 2단계: 충분한 기사 데이터가 쌓인 뒤 전략적 해석, 시장 인텔리전스, GP Action, 브리핑 기능을 고도화한다.

따라서 현재 앱의 핵심은 의미 해석이나 투자 판단이 아니라, 신뢰할 수 있는 기사 데이터베이스를 만드는 것이다.

---

## 3. 1차 목표

Core 15 + Watchlist 8 시장에서 다음 정보를 꾸준히 축적한다.

- 어떤 시장에서 어떤 주거 관련 뉴스가 발생했는가
- 어떤 섹터와 관련된 기사인가
- 어떤 이벤트 태그가 붙을 수 있는가
- 원문 링크와 출처가 신뢰 가능한가
- access_limited 기사인지 여부
- 향후 분석에 사용할 수 있을 만큼 기사 메타데이터가 정리되어 있는가

중요한 원칙은 기사 하나를 `market`, `development`, `gp_capital` 중 하나로 억지로 단일 분류하지 않는 것이다.

기사 하나는 여러 event_tags를 가질 수 있다. 예를 들어 특정 개발 프로젝트의 construction loan 기사는 `development`, `financing/refinancing`, `construction start` 태그를 동시에 가질 수 있다.

---

## 4. 대상 시장

### 4.1 Core 15

- Los Angeles / Southern California
- New York / Northern New Jersey
- Dallas-Fort Worth
- Houston
- Atlanta
- Phoenix
- Miami / South Florida
- Washington DC / Northern Virginia
- Seattle
- Denver
- Austin
- Charlotte
- Raleigh-Durham
- Nashville
- Tampa / St. Petersburg

### 4.2 Watchlist 8

- Orlando
- San Antonio
- Las Vegas
- Salt Lake City
- Jacksonville
- Columbus
- Minneapolis
- San Diego

---

## 5. 관심 섹터

앱은 다음 주거 섹터 관련 뉴스를 우선 수집하고 정리한다.

- Multifamily
- Build-to-Rent
- Single-Family Rental
- Student Housing
- Senior Housing
- Affordable Housing
- Workforce Housing
- Mixed-use Residential

---

## 6. 관심 이벤트 태그

기사에는 하나 이상의 event_tags가 붙을 수 있다. 아래 태그는 상호 배타적이지 않다.

- development
- permit / entitlement
- land / site acquisition
- construction start
- under construction
- delivery / completion
- transaction / sale
- acquisition
- financing / refinancing
- JV / recapitalization
- policy / regulation
- market data / supply-demand
- construction cost
- rent / occupancy / absorption

---

## 7. 핵심 원칙

1. 기사 하나를 시장/개발/GP자본 중 하나로 강제 분류하지 않는다.
2. 기사 하나는 여러 event_tags를 가질 수 있다.
3. 앱의 1차 목적은 의미 해석이 아니라 기사 축적과 정리다.
4. 오늘의 브리핑, 시장 인텔리전스, GP Action 등 해석성 기능은 2단계로 미룬다.
5. Article Feed를 중심 화면으로 강화한다.
6. access_limited 기사는 핵심 분석에서 제외하고 별도 보관한다.
7. 원문 링크, 출처, 날짜, 시장, 섹터, 태그를 안정적으로 남기는 것을 우선한다.
8. 기사 수집과 정리 로직은 단순하고 검증 가능해야 한다.

---

## 8. 1단계 기능 범위

1단계에서 우선 구현하고 안정화할 기능은 다음과 같다.

- Core 15 + Watchlist 8 시장 중심의 뉴스 수집
- 주거 섹터별 기사 정리
- event_tags 기반 기사 정리
- Article Feed 중심 화면
- 기사 원문 링크 유지
- 출처, 날짜, 제목, 요약, 시장, 섹터, 이벤트 태그 저장
- access_limited 기사 별도 보관
- output CSV/Markdown 기반의 단순하고 안정적인 실행 구조
- output 파일이 없거나 비어 있어도 앱이 죽지 않는 방어 로직

1단계에서는 `Article Feed`가 가장 중요한 화면이다.

---

## 9. 2단계 기능 범위

2단계는 충분한 기사 데이터가 쌓인 뒤 고도화한다.

- 오늘의 브리핑
- 시장 인텔리전스
- 오늘의 Hot Market
- 개발현황 해석
- GP Action
- GP / Capital 동향 분석
- 전략적 해석
- 시장별 트렌드 비교
- 섹터별 기회/리스크 해석
- 장기 기사 축적 데이터를 기반으로 한 월간/분기 리포트

2단계 기능은 1단계 데이터 구조가 안정화된 뒤 확장한다. 해석성 기능이 기사 축적 구조보다 앞서가면 앱의 기준이 흔들릴 수 있으므로, 현재는 Article Feed와 태그 구조를 우선한다.

---

## 10. 주요 파일

- `app.py`
  - Streamlit 앱 화면과 Article Feed 표시를 담당한다.

- `news_collector.py`
  - 뉴스 수집, 필터링, 저장 로직을 담당한다.

- `requirements.txt`
  - Python 패키지 의존성을 정의한다.

- `.gitignore`
  - output 파일과 실행 결과물을 Git에서 제외한다.

- `README.md`
  - 프로젝트 설명과 실행 방법을 문서화한다.

- `scripts/`
  - QA, 자동화, 보조 실행 스크립트를 보관한다.

- `PROJECT_CONTEXT.md`
  - Codex가 프로젝트 목적, 현재 방향, 우선순위를 이해하기 위한 기준 문서다.

---

## 11. 현재 UI 방향

현재 UI는 Article Feed를 중심으로 정리한다.

우선순위는 다음과 같다.

1. Article Feed
2. 시장/섹터/event_tags 필터
3. access_limited 기사 분리
4. 기사 원문 링크 접근성
5. 기사 축적 현황 확인
6. 이후 브리핑/인텔리전스 화면 확장

현재 단계에서 브리핑, GP Action, 시장 인텔리전스 화면은 참고 기능 또는 2단계 기능으로 본다.

---

## 12. access_limited 기사 처리

Urbanize, SF YIMBY 등 일부 소스는 접속 직후 짧게 본문이 보였다가 제한 화면으로 전환될 수 있다.

이런 기사는 수집 결과에 포함될 수 있지만, 핵심 분석이나 인텔리전스 판단에는 바로 사용하지 않는다.

처리 원칙은 다음과 같다.

- access_limited 여부를 별도 표시한다.
- Article Feed 하단 또는 별도 섹션에 보관한다.
- 핵심 분석/해석에서는 제외한다.
- 원문 접근성이 개선되거나 신뢰 가능한 요약이 확보되면 다시 사용할 수 있다.

---

## 13. Codex 작업 원칙

Codex가 작업할 때는 다음 원칙을 따른다.

1. 요청받은 파일만 수정한다.
2. 기존 기능을 삭제하거나 단순화하기 전에 사용자에게 확인한다.
3. 기사 원문 링크 기능을 보존한다.
4. output 파일이 없거나 비어 있어도 앱이 죽지 않게 한다.
5. 새 기능보다 안정적인 기사 축적 구조를 우선한다.
6. Article Feed 관련 작업에서는 category보다 event_tags 구조를 우선 고려한다.
7. access_limited 기사는 핵심 분석에서 제외하고 별도 보관한다.
8. 수정 후 문법 검사 또는 실행 확인 방법을 알려준다.

---

## 14. 다음 작업 방향

다음 단계에서는 코드 변경 전에 다음 순서로 작업한다.

1. 현재 output CSV 구조 확인
2. 기사별 market / sector / event_tags 필드 현황 확인
3. Article Feed에서 event_tags를 표시하는 방식 설계
4. 단일 category 중심 분류를 event_tags 중심 구조로 점진 전환
5. access_limited 기사 분리 방식 안정화
6. 충분한 기사 데이터가 쌓인 뒤 2단계 인텔리전스 기능 재정비

