# PROJECT_CONTEXT.md

## 1. 프로젝트 이름

US Residential Intelligence App  
미국 주거시장 전략 리서치 앱

---

## 2. 프로젝트 목적

이 앱은 미국 주거 및 멀티패밀리 개발시장 관련 뉴스를 수집하고,  
부동산 디벨로퍼 역량 강화와 해외 투자전략 수립에 필요한 시장 시그널을 정리하기 위한 내부 리서치 도구이다.

단순 뉴스 수집기가 아니라, 다음과 같은 질문에 답하는 것을 목표로 한다.

- 현재 미국 주거 개발시장은 어떤 국면인가?
- 어느 지역에서 개발, 거래, 자본 유입, 규제 변화가 활발한가?
- 주요 GP / Developer들은 어디에서 어떤 움직임을 보이고 있는가?
- 금리, 대출환경, 건설비, 임대수요 변화가 개발시장에 어떤 영향을 주는가?
- 향후 우미글로벌 / 우미 USA의 미국 주거 개발 역량 강화에 참고할 만한 시그널은 무엇인가?

---

## 3. 사용자 배경

사용자는 해외 상업용 부동산 펀드 설정 및 간접투자 업무를 수행해온 부동산 펀드매니저이다.

현재 우미글로벌 본사 차원에서 미국 현지 디벨로퍼 역량 강화를 위한 중장기 전략 수립을 담당하고 있다.

우미건설은 미국 상업용 부동산 시장에서 주거 상품, 특히 멀티패밀리 등 개발사업의 Developer 지위 확보를 목표로 하고 있다.

---

## 4. 현재 개발 단계

현재 단계는 MVP 이후의 초기 고도화 단계이다.

초기 MVP는 다음 기능을 목표로 한다.

- 미국 주거시장 관련 뉴스 수집
- RSS 또는 공개 웹 기반 기사 수집
- 키워드 기반 필터링
- 기사 제목, 출처, 날짜, URL 저장
- CSV 파일로 결과 저장
- Streamlit 기반 웹 앱 화면 구성

향후 목표는 다음과 같다.

- Excel 리포트 출력
- Markdown 리포트 출력
- 기사 요약 추가
- 한국어 번역 레이어 추가
- GP / Developer Intelligence Layer 추가
- Residential Sector Coverage Layer 추가
- 시장 시그널 분석 고도화
- 모바일 웹 대응

---

## 5. 기술 스택

현재 또는 예상 기술 스택은 다음과 같다.

- Python
- Streamlit
- GitHub
- VS Code
- CSV
- 향후 Excel / Markdown
- 향후 데이터베이스 적용 가능성 있음

---

## 6. 주요 파일

현재 핵심 파일은 다음과 같다.

- `app.py`  
  Streamlit 웹 앱의 메인 화면 파일

- `news_collector.py`  
  뉴스 수집, 필터링, 저장 로직을 담당하는 파일

- `README.md`  
  프로젝트 설명 및 실행 방법 문서

- `articles/`  
  수집된 기사 결과가 저장되는 폴더

- `PROJECT_CONTEXT.md`  
  AI 비서와 Codex가 프로젝트의 목적, 구조, 방향성을 이해하기 위한 기준 문서

---

## 7. 핵심 화면 구성

앱의 메인 홈 화면은 다음 5개 섹션을 중심으로 구성한다.

### 7.1 오늘의 Highlight

아래 섹션들의 핵심 내용을 요약해서 보여주는 영역이다.

- 오늘의 Top 기사
- 오늘의 Hot Market
- 개발현황
- 오늘의 GP Action

단순 제목 나열이 아니라, 오늘 시장에서 읽을 수 있는 핵심 시그널을 짧게 정리해야 한다.

### 7.2 오늘의 Top 기사

수집된 기사 중 중요도와 관련성이 높은 Top 5 기사를 보여준다.

각 기사에는 가능하면 다음 정보가 포함되어야 한다.

- 제목
- 출처
- 날짜
- URL
- 관련 섹터
- 관련 지역
- 관련 시그널
- 간단 요약

### 7.3 오늘의 Hot Market

거래, 개발, 인허가, 자본 유입, GP 활동 관련 뉴스가 많이 포착된 지역 또는 도시 Top 10을 보여준다.

단, 단순히 permit / entitlement 뉴스가 많다는 이유만으로 Hot Market으로 과대평가하지 않도록 주의한다.  
Permit과 entitlement 뉴스는 공공자료 기반 보도 편향이 있을 수 있으므로, 거래, 자본 유입, 임대수요, 개발 착공, GP activity와 함께 종합적으로 판단한다.

### 7.4 개발현황

지역별 개발 관련 정보를 정리한다.

가능하면 다음 구분을 사용한다.

- 신규 개발
- 온고잉 개발
- 중단 또는 취소
- 인허가 / entitlement
- 착공 / construction start
- 준공 / delivery

### 7.5 오늘의 GP Action

주요 GP, Developer, Institutional Investor의 움직임을 정리한다.

예시 대상은 다음과 같다.

- Blackstone
- Brookfield
- Greystar
- Related
- Kennedy Wilson
- Harrison Street
- PCCP
- 기타 빠르게 성장하는 GP / Developer

GP Action은 단순 기사 수가 아니라, 시장 방향성과 자본 흐름을 보여주는 중요한 선행 시그널로 본다.

---

## 8. 주요 분석 주제

앱은 다음 주제를 중심으로 기사를 수집하고 분석한다.

### 8.1 Macro & Financing

- Fed 금리 결정
- 미국 10년물 국채금리
- SOFR
- 대출 환경
- 개발 대출 조건
- 은행 대출 태도
- 자본시장 유동성
- 금리 인하 또는 인상 가능성

### 8.2 Equity Flow

- 기관투자자 매입 / 매각
- Blackstone, Brookfield 등 대형 자본의 움직임
- GP의 신규 펀드 조성
- Joint Venture
- Recapitalization
- Distressed opportunity
- Preferred equity / rescue capital

### 8.3 Supply & Demand

- Absorption Rate
- Vacancy Rate
- Effective Rent Growth
- Permits & Starts
- Construction Pipeline
- Deliveries
- Concessions
- Sunbelt oversupply
- Workforce housing demand
- Affordable housing demand

### 8.4 Regulation & Entitlement

- LA / California 주거 개발 규제
- Zoning
- Entitlement
- Permit
- Density bonus
- Affordable housing requirement
- Rent control
- Environmental review

### 8.5 Construction Cost

- 자재비
- 인건비
- 보험료
- 공사비 상승
- General Contractor 동향
- Labor shortage
- Supply chain

---

## 9. 섹터 커버리지

초기 중심 섹터는 미국 주거 및 멀티패밀리이다.

다만 향후 다음 섹터도 함께 커버한다.

- Multifamily
- Student Housing
- Senior Housing
- Build-to-Rent
- Single-Family Rental
- Workforce Housing
- Affordable Housing
- Mixed-use Residential

---

## 10. 선호하는 정보 출처

우선순위가 높은 정보 출처는 다음과 같다.

- WSJ Real Estate
- Commercial Observer
- Bisnow
- Yardi Matrix
- RealPage Analytics
- CoStar News
- GlobeSt
- Multi-Housing News
- Connect CRE
- Urbanize LA
- The Real Deal
- 주요 GP / Developer 보도자료

CoStar는 회사에서 유료 회원으로 접근 가능한 정보가 있으나, 프로그램에서 활용할 때는 이용약관과 접근 권한을 반드시 고려해야 한다.  
무단 스크래핑은 피하고, 허용된 범위 내에서 수동 입력, 다운로드 파일, API, 내부 허가 방식 등을 우선 검토한다.

---

## 11. 중요한 판단 원칙

이 앱은 단순히 기사를 많이 모으는 것이 목적이 아니다.  
중요한 것은 투자전략과 개발역량 강화에 의미 있는 시그널을 선별하는 것이다.

다음 원칙을 따른다.

1. 기사 수가 많다고 반드시 중요한 시장은 아니다.
2. Permit / entitlement 뉴스는 보도 편향이 있을 수 있다.
3. GP / Developer의 실제 자본 투입, 매입, 매각, JV, 개발 착공은 중요한 시그널이다.
4. Macro와 Financing 정보는 개발사업의 feasibility와 exit cap rate에 직접 영향을 주므로 중요하다.
5. Sunbelt 시장은 단순 성장 지역으로 보지 않고, 공급 과잉과 absorption 상황을 함께 검토한다.
6. Affordable / Workforce Housing은 정책, 수요, 자본 측면에서 별도 의미가 있으므로 독립적으로 관찰한다.
7. 기사 제목만 보고 판단하지 않고, 가능하면 본문 요약과 맥락을 함께 본다.
8. 임원 보고용으로 사용할 수 있도록 결론과 시사점을 명확하게 정리한다.

---

## 12. UI / UX 방향

앱은 복잡한 분석 도구보다 매일 아침 빠르게 시장을 읽을 수 있는 리서치 대시보드를 지향한다.

중요한 UI 방향은 다음과 같다.

- 홈 화면은 단순하고 읽기 쉬워야 한다.
- 글자 크기와 여백을 충분히 확보한다.
- 기사 제목만 나열하지 말고, 핵심 요약과 시그널을 함께 보여준다.
- 사용자가 제목 아래에서 바로 기사 내용을 확인할 수 있어야 한다.
- 불필요한 모드 구분은 줄인다.
- 모바일에서도 읽기 편한 구조를 고려한다.

현재 제거하거나 축소하기로 한 항목은 다음과 같다.

- 오늘 우선 액션
- 핵심 관계 구축
- 경영진모드
- 상세분석모드
- 리뷰모드
- Sidebar의 오늘의 집중검토
- Sidebar의 상세필터

---

## 13. 선호하는 표현

앱 내 표현은 직관적이고 실무적인 용어를 사용한다.

선호 표현:

- 시그널 분석
- 시장 인텔리전스
- 시장 국면 요약
- 개발현황
- 오늘의 GP Action
- 오늘의 Hot Market
- 오늘의 Highlight

피하거나 재검토할 표현:

- 고신뢰 신호
- conviction memory
- 시장 timing 해석
- 과도하게 추상적인 AI식 표현
- 근거가 약한 결론형 표현

---

## 14. Codex 작업 원칙

Codex는 코드를 수정하기 전에 다음을 확인해야 한다.

1. 현재 파일 구조 확인
2. 핵심 파일 확인
3. 기존 기능을 깨지 않도록 수정
4. 수정한 파일 목록 제시
5. 실행 방법 제시
6. 테스트 또는 확인 방법 제시
7. 불확실한 부분은 추정하지 말고 명시

Codex에 줄 작업 지시는 가능한 한 다음 형식을 따른다.

```text
목표:
수정 대상:
현재 문제:
원하는 결과:
주의사항:
완료 후 알려줄 내용: