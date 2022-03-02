# short-projects
Ex short projects collection
- 페이지별 필요한 API, 데이터
    - 홈화면(검색창)
        - 전체 주식 리스트 받아옴
            - 국내 : 종목명, 종목단축코드  (ex. 삼성전자 | 005930 )
            
            ```json
            { 
            	"name": string,
            // 종목명
            	"stockCode": number
            // 종목단축코드
            }
            ```
            
            - 해외 : 종목명(심볼), 기업명, 거래소  (ex. AAPL | Apple Inc | NASDAQ)
            
            ```json
            {
            	"symbol": string,
            // 종목명
            	"companyName": string,
            // 기업이름
            	"marketType": string
            // 거래소 정보
            }
            ```
            
    - 국내
        - 국내주식 검색전
            - 최근조회, 관심종목
                - Parameters
                    - 종목코드들
                - Returns
                    
                    ```json
                    {
                    	"name":string,
                    	// 종목명
                    	"stockCode":number,
                    	// 종목 고유코드
                    	"basIdx":number,
                    	// 기준 시점의 지수값
                    	"vs":number,
                    	// 전일 대비 등락
                    	"fltRt":number,
                    	// 전일 대비 등락에 따른 비율
                    }
                    ```
                    
            - 주가지수
                - Parameters
                    - 지수타입(코스피, 코스닥, 코스피200)
                - Returns
                    - 해당 지수 타입별(코스피, 코스닥, 코스피200)
                    
                    ```json
                    {
                    	"basDt":date,
                    	// 기준일자
                    	"idxNm":string,
                    	// 지수명칭
                    	"basIdx":number,
                    	// 기준시점의 지수값
                    	"vs":number,
                    	// 전일 대비 등락
                    	"fltRt":number,
                    	// 전일 대비 등락에 따른 비율
                    	"timeIdxs":[{
                    			"basTime":date,
                    			// 기준시간
                    			"basIdx":number,
                    			//기준시간의 지수값
                    	}],
                    	// 시간대별 지수정보
                    }
                    ```
                    
            - TOP종목
                - Parameters
                    - 필터타입(상한가, 하한가, 상승, 보합, 하락, 거래량상위, 시가총액상위)
                - Returns
                    - 해당 필터타입에 해당하는 TOP 10 (상한가, 하한가, 상승, 보합, 하락, 거래량상위, 시가총액상위)
                    
                    ```json
                    {
                    	"name":string,
                    	// 종목명
                    	"stockCode":number,
                    	// 종목 고유코드
                    	"date":date,
                    	// 날짜
                    	"basIdx":number,
                    	// 기준 시점의 지수값
                    	"vs":number,
                    	// 전일 대비 등락
                    	"fltRt":number,
                    	// 전일 대비 등락에 따른 비율
                    	"trCnt": number,
                    	// 거래량
                    	"mrktCap": number,
                    	// 시가총액
                    }
                    ```
                    
            - 환율
                - Parameters
                    - ...
                - Returns
                    
                    ```json
                    {
                    	"name":string,
                    	// 환율유형(미국, 유럽, 일본, 중국, 영국)
                    	"date":date,
                    	// 날짜
                    	"basExchRt":number,
                    	//기준 시점의 환율
                    	"dateExchRt":[{
                    			"basDate":date,
                    			// 기준날짜
                    			"basExchRt":number,
                    			//기준시간의 지수값
                    	}],
                    	// 기간별 환율정보
                    
                    ...환율정보(상세내용 확정 전)
                    
                    }
                    ```
                    
            - 시장지표
                - Parameters
                    - ...
                - Returns
                    
                    ```json
                    {
                    	"date":date,
                    	// 날짜
                    	"itrstRt":number,
                    	//기준 시점의 금리
                    	"itrstRtFltRt":number,
                    	//기준 시점의 금리 등락률
                    	"itrGold":number,
                    	//기준 시점의 국제 금
                    	"itrGoldFltRt":number,
                    	//기준 시점의 국제 금 등락률
                    	"dmsticGold":number,
                    	//기준 시점의 국내 금
                    	"dmsticGoldFltRt":number,
                    	//기준 시점의 국내 금 등락률
                    	"oilPrc":number,
                    	//기준 시점의 유가
                    	"oilPrcFltRt":number,
                    	//기준 시점의 유가 등락률
                    }
                    ```
                    
        - 국내주식 검색 후
            - ~~종목 개요 정보(상단표) = 하단의 ‘종목 정보’와 겹치는 지 확인 후 처리~~
                - Parameters
                    - 종목단축코드
                - Returns
                    - 종목명(기업명)
                    - 회사 설명
                    - 전일가
                    - 상장된 주식 수
                    - 거래소
                    - 시가총액
                    - 52주 최저가/최고가
                    - EPS(FN가이드, KRX, 추정)
                    
                    ```json
                    {
                    	"name": string,
                    // 종목명
                    	"recap": string,
                    // 기업 소개
                    	"start": number,
                    // 시가
                    	"end": number,
                    // 종가
                    	"
                    }
                    ```
                    
            - 종목 정보
                - 최근 1년치 종목정보를 받아옴
                - Parameter
                    - code(종목 코드)
                - Returns
                    
                    ```json
                    {
                    	"name":string,
                    	// 종목명
                    	"stockCode":number,
                    	// 종목 고유코드
                    	"date":date,
                    	// 날짜 YYYYMMDD
                    	"high":number,
                    	// 일중 최고가
                    	"low":number,
                    	// 일중 최저가
                    	"start":number,
                    	// 시가
                    	"end":number,
                    	// 종가
                    	"dr":boolean,
                    	// 전일 대비 등락 여부(양봉, 음봉)
                    	"drRate":number
                    	// 전일 대비 등락 비율
                    	"type": string,
                    	// 코스피 코스닥 코넥스
                    	"dStock": number,
                    	// 유통 주식 수
                    	"enStock": number,
                    	// 상장된 주식 수
                    	"deTr": boolean,
                    	// 전일 대비 체결수량 증가여부
                    	"deTr" :number,
                    	// 전일 대비 체결수량
                    	"deTr" : number
                    	// 당일 체결수량* 거래별 체결 가격( 거래대금 )
                    }
                    ```
                    
            - 카테고리
                - parameter
                    - code(종목 코드)
                    - start(시작기간)
                    - end(끝나는 기간)
                - returns
                
                ```json
                {
                	"date":string,
                	// YYDDMM
                	"value":number
                	// 해당 기간동안의 퍼센트
                }
                ```
                
            - 언론사
                - parameter
                    - code(종목 코드)
                    - start(시작기간)
                    - end(끝나는 기간)
                - return
                
                ```json
                {
                	"name":string,
                	// 언론사명
                	"value":number
                	// 해당 기간동안의 수
                }
                ```
                
            - 키워드
                - parameter
                    - code(종목 코드)
                    - start(시작기간)
                    - end(끝나는 기간)
                - return
                
                ```json
                {
                	"date":string,
                	// YYDDMM
                	"value":number
                	// value
                }
                ```
                
        - 국내 주식뉴스분석
            - 특정 종목의 주가와 거래량
                - Parameters
                    - 종목의 코드
                - Returns
                    - 날짜별 주가
                    - 날짜별 거래량
            - 특정 종목의 뉴스
                - Parameters
                    - 종목의 코드
                    - 일자(기간이 될 수 있음)
                - Returns
                    - 날짜별 뉴스
                    - 날짜별 버즈량
                    - 날짜별 카테고리 분석
                    - 날짜별 키워드 분석
                    - 날짜별 언론사 분석
                    - 뉴스별 감정지수
        - 국내 기업정보
            - 특정 종목의 주가와 거래량
                - Parameters
                    - code(종목 코드)
                    - start
                    - end
                - Returns
                    
                    ```json
                    {
                    	"date":string,
                    	// YYDDMM
                    	"name":string,
                    	// 종목명
                    	"stockCode":number,
                    	// 종목 고유코드
                    	"date":date,
                    	// 날짜 YYDDMM
                    	"high":number,
                    	// 일중 최고가
                    	"low":number,
                    	// 일중 최저가
                    	"start":number,
                    	// 시가
                    	"end":number,
                    	// 종가
                    	"dr":boolean,
                    	// 전일 대비 등락 여부(양봉, 음봉)
                    	"vs":number,
                    	// 전일 대비 등락
                    	"trCnt": number,
                    	// 거래량
                    }
                    ```
                    
            - 특정 종목의 재무제표
                - Parameters
                    - code(종목 코드)
                - Returns
                    
                    ```json
                    {
                    	"date":string,
                    	// YYDDMM
                      "revenue":number,
                      // 매출액
                    	"opInc":number,
                    	// 영업이익
                    	"netInc":number,
                    	// 당기순이익
                      "opMargin":number,
                    	// 영업이익률(계산가능)
                    	"netMargin":number,
                    	// 순이익률(계산가능)
                    	"deptEquity":number,
                    	// 부채비율
                    	"quick":number,
                    	// 당좌비율
                    	"reserve":number,
                    	// 유보율
                    	"roe":number,
                    	// ROE(계산가능)
                    	"eps":number,
                    	// EPS(계산가능)
                    	"per":number,
                    	// PER(계산가능)
                    	"bps":number,
                    	// BPS(계산가능)
                    	"pbr":number,
                      // PBR(계산가능)
                    	"devidend":number,
                    	// 주당배당금
                    	"devidendPer":number
                    	// 시가배당률(계산가능)
                    }
                    ```
                    
        - 국내 재무데이터
            - 특정 종목의 재무비율
                - Parameters
                    - 종목의 코드
                - Returns
                    
                    ```json
                    {
                    	"date":string,
                    	// YYDDMM
                      "marketCap":number,
                      // 시가총액
                    	"enterpriseVal":number,
                    	// 기업가치
                    	"epsQoQ":number,
                    	// 직전 분기 대비 주당순이익 증가율
                    	"peRatio":number,
                    	// 주가수익률
                    	"bvps":number,
                    	// 주당 순자산
                    	"pbRatio":number,
                    	// 주당장부가치비율
                    	"roa":number,
                    	// ROA
                    	"roe":number,
                    	// ROE
                    	"devidend":number,
                    	// 주당배당금
                    	"devidendPer":number
                    	// 시가배당률(계산가능)
                    }
                    ```
                    
            - 특정 종목의 대차대조표
                - Parameters
                    - 종목의 코드
                - Returns
                    
                    ```json
                    {
                    	"date":string,
                    	// YYDDMM
                      "totalAssets":number,
                      // 총자산
                    	"cashAndEq":number,
                    	// 현금 및 현금 등가물
                    	"investmentsCurrent":number,
                    	// 단기투자
                      "acctRec":number,
                    	// 매출채권
                    	"acctRec":number,
                    	// 미수금
                    	"inventory":number,
                    	// 재고자산
                    	"assetsNonCurrent":number,
                    	// 비유동성 투자자산
                    	"investmentsNonCurrent":number,
                    	// 장기투자
                    	"ppeq":number,
                    	// 유형고정자산
                    	"intangibles":number,
                    	// 무형자산
                    	"totalLiabilities":number,
                    	// 총부채
                    	"taxAssets":number,
                    	// 법인세자산
                    	"liabilitiesCurrent":number,
                    	// 유동부채
                    	"debtCurrent":number,
                    	// 단기부채
                    	"acctPay":number,
                    	// 외상 매출금
                    	"liabilitiesNonCurrent":number,
                    	// 비유동부채
                    	"debtNonCurrent":number,
                    	// 장기부채
                    	"deposits":number,
                    	// 보증금
                    	"deferredRev":number,
                    	// 선수수익/이연수익
                    	"taxLiabilities":number,
                    	// 세금부채
                    	"equity":number,
                    	// 자본
                    	"retainedEarnings":number,
                    	// 이익잉여금
                    	"accoci":number,
                    	// 기타 포괄손익누계액
                    }
                    ```
                    
            - 특정 종목의 손익계산서
                - Parameters
                    - 종목의 코드
                - Returns
                    
                    ```json
                    {
                    	"date":string,
                    	// YYDDMM
                      "opinc":number,
                      // 영업이익
                    	"grossProfit":number,
                    	// 매출 총이익
                    	"revenue":number,
                    	// 매출액
                      "costRev":number,
                    	// 매출원가
                    	"opex":number,
                    	// 영업비용
                    	"rnd":number,
                    	// R&D
                    	"":number,
                    	// 유현고정자산
                    	"":number,
                    	// 영업외 수익
                    	"intexp":number,
                    	// 이자비용
                    	"taxExp":number,
                    	// 법인세비용
                    	"ebt":number,
                    	// 세전이익
                    	"ebit":number,
                    	// 이자 및 세전이익
                    	"ebitda":number,
                    	// 법인세, 이자, 감가상각비 차감전 이익
                    	"consolidatedIncome":number,
                    	// 통합소득
                    	"netinc":number,
                    	// 당기순이익
                    	"nonControllingInterests":number,
                    	// 비통제이자를 포함한 당기순이익
                    	"netIncDiscOps":number,
                    	// 중단영업순이익
                    	"prefDVDs":number,
                    	// 우선배당손익계산서 영향
                    	"netIncComStock":number,
                    	// 보통주 순이익
                    	"eps":number,
                    	// 주당순이익
                    	"epsDil":number,
                      // 희석주당순이익
                    	"shareswa":number,
                    	// 가중평균주식
                    	"shareswaDil":number,
                    	// 희석가중평균주식
                    }
                    ```
                    
            - 특정 종목의 현금흐름표(미정)
                - Parameters
                    - 종목의 코드
                - Returns
                    
                    ```json
                    {
                    	"date":string,
                    	// YYDDMM
                      "ncf":number,
                      // 현금및현금성자산의 순현금흐름
                    	"ncfo":number,
                    	// 영업에서의 순현금흐름
                    	"depamor":number,
                    	// 유형자산 감가상각, 무형자산 감가상각 & 자산증가
                      "sbcomp":number,
                    	// 주식 기반 보상
                    	"ncfi":number,
                    	// 투자로부터의 순현금흐름
                    	"capex":number,
                    	// 자본적지출
                    	"investmentsAcqDisposals":number,
                    	// 투자자산 취득 및 처분
                    	"businessAcqDisposals":number,
                    	// 사업 인수 및 처분
                    	"freeCashFlow":number,
                    	// 잉여 현금 흐름
                    	"ncff":number,
                    	// 재무활동으로 인한 현금흐름
                    	"payDiv":number,
                    	// 배당금지급 및 현금분배
                    	"issrepayEquity":number,
                    	// 자본의 배급 혹은 상환
                    	"issrepayDebt":number,
                    	// 부채의 배급 혹은 상환
                    	"ncfx":number,
                    	// 환율변동이 현금에 미치는 영향
                    }
                    ```
                    
        - 국내 기업공시
            - 특정 종목의 공시 리스트
                - Parameters
                    - code (종목 코드)
                        - 종목 코드 검색 후 공시 API요청 시 아래 요청인자 필요 ([open DART 공시검색 개발가이드](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019001))
                            - crtfc_key : API 인증키
                            - corp_code : 고유번호(종목 코드와 다르며 검색어로 입력된 종목코드를 이 고유번호로 바꿔주어야 함)
                            - bgn_de : 시작일
                            - end_de : 종료일
                            - last_reprt_at : 최종보고서 검색여부
                            - pblntf_ty : 공시유형
                            - pblntf_detail_ty : 공시상세유형
                            - corp_cls : 법인구분
                            - sort : 정렬
                            - sort_mth : 정렬방법
                            - page_no : 페이지 번호
                            - page_count : 페이지 별 건수
                - Returns
                    
                    ```jsx
                    {
                    	"status":string,
                    	// 에러 및 정보 코드
                    	"message": string,
                    	// 에러 및 정보 메시지
                    	"page_no": number,
                    	// 페이지 번호
                    	"page_count":number,
                    	// 페이지 별 건수
                    	"total_count":number,
                    	// 총 건수
                    	"total_page":number,
                    	// 총 페이지 수
                    	"list": [ // 공시 리스트
                    		{
                    			"corp_cls": string,
                    			// 법인구분
                    			"corp_name": string,
                    			// 종목명(법인명)
                    			"corp_code": string,
                    			// 고유번호
                    			"stock_code": string,
                    			// 종목코드
                    			"report_nm": string,
                    			// 보고서명
                    			"rcept_no": string,
                    			// 접수번호
                    			"flr_nm": string,
                    			// 공시 제출인명
                    			"rcept_dt": string,
                    			// 접수일자
                    			"rm": string,
                    			// 비고
                    			"origin_link": string
                    			// 원문링크
                    		},
                    		...
                    	]
                    }
                    ```
                    
        - 국내 statistics
        - 국내 screener
            - 원하는 범위값에 해당하는 주식 종목들
                - Parameters
                    - 시가총액 범위
                    - 외국인소진율 범위
                    - PER 범위
                    - PBR 범위
                    - 배당수익률 범위
                    - ROE 범위
                - Returns
                    - 해당 범위에 속하는 주식 종목들
                    
                    ```json
                    {
                      "items":[{
                    		"name":string,
                    	  // 종목명
                    		"ticker":string,
                    		// 심볼
                    		"type":string,
                    		// 코스피 코스닥 코넥스
                    		"marketCap":number,
                    		// 시가총액
                    		}
                    	]
                    }
                    ```
                    
    - 해외
        - 해외주식 검색전
            - 최근조회, 관심종목
                - Parameters
                    - 종목코드들
                - Returns
                    
                    ```json
                    {
                    	"name":string,
                    	// 종목명
                    	"stockCode":number,
                    	// 종목 고유코드
                    	"basIdx":number,
                    	// 기준 시점의 지수값
                    	"vs":number,
                    	// 전일 대비 등락
                    	"fltRt":number,
                    	// 전일 대비 등락에 따른 비율
                    }
                    ```
                    
            - 주가지수
                - Parameters
                    - 지수타입(S,&P500, QQQ, DOW)
                - Returns
                    - 해당 지수 타입별(S,&P500, QQQ, DOW)
                    
                    ```json
                    {
                    	"basDt":date,
                    	// 기준일자
                    	"idxNm":string,
                    	// 지수명칭
                    	"basIdx":number,
                    	// 기준시점의 지수값
                    	"vs":number,
                    	// 전일 대비 등락
                    	"fltRt":number,
                    	// 전일 대비 등락에 따른 비율
                    	"timeIdxs":[{
                    			"basTime":date,
                    			// 기준시간
                    			"basIdx":number,
                    			//기준시간의 지수값
                    	}],
                    	// 시간대별 지수정보
                    }
                    ```
                    
            - 해외주요지수
                - Parameters
                    - ...
                - Returns
                    
                    ```json
                    {
                    	"country":string,
                    	// 국가명
                    	"idxNm":string,
                    	// 지수명
                    	"basIdx":number,
                    	// 현재가
                    	"vs":number,
                    	// 전일 대비 등락
                    	"fltRt":number,
                    	// 전일 대비 등락에 따른 비율
                    	"date":date,
                    	// 기준시간
                    }
                    ```
                    
            - 주요뉴스
                - Parameters
                    - ...
                - Returns
                    
                    ```json
                    {
                    	"title":string,
                    	// 뉴스제목
                    	"press":string,
                    	// 언론사
                    	"date":date,
                    	// 날짜
                    	"url":string,
                    	// 링크주소
                    }
                    ```
                    
            - 국제환율
                - Parameters
                    - ...
                - Returns
                    
                    ```json
                    {
                    	"name":string,
                    	// 환율유형(미국, 유럽, 일본, 중국, 영국)
                    	"date":date,
                    	// 날짜
                    	"basExchRt":number,
                    	//기준 시점의 환율
                    	"dateExchRt":[{
                    			"basDate":date,
                    			// 기준날짜
                    			"basExchRt":number,
                    			//기준시간의 지수값
                    	}],
                    	// 기간별 환율정보
                    
                    ...환율정보(상세내용 확정 전)
                    
                    }
                    ```
                    
            - 분야
                - Parameters
                    - ...
                - Returns
                    
                    ```json
                    {
                    	"categoray":string,
                    	// 유형 (S&P500, Russell2000, Gold, Oil, Tech, Energy, Financial, Discretionary, Staples, Materials, Industrials, Health Care, Utilities)
                    	"fltRt":number,
                    	// 전일 대비 등락에 따른 비율
                    }
                    ```
                    
        - 해외주식 검색후
            - 종목 개요 정보(상단표)
                - Parameters
                    - 종목명(symbol)
                - Returns
                    - 기업 이름
                    - 회사 설명
                    - 현재가
                    - 시가
                    - 최고가
                    - 최저가
                    - 전일가
                    - 거래량
                    - 거래대금
        - 해외 주식뉴스분석
            
            
        - 해외기업정보
            - 특정 종목의 주가와 거래량
                - Parameters
                    - code(종목 코드)
                    - start
                    - end
                - Returns
                    
                    ```json
                    {
                    	"name":string,
                    	// 종목명
                    	"stockCode":number,
                    	// 종목 고유코드
                    	"date":date,
                    	// 날짜 YYDDMM
                    	"high":number,
                    	// 일중 최고가
                    	"low":number,
                    	// 일중 최저가
                    	"start":number,
                    	// 시가
                    	"end":number,
                    	// 종가
                    	"dr":boolean,
                    	// 전일 대비 등락 여부(양봉, 음봉)
                    	"vs":number,
                    	// 전일 대비 등락
                    	"trCnt": number,
                    	// 거래량
                    }
                    ```
                    
            - 특정 종목의 재무제표
                - Parameters
                    - code(종목 코드)
                - Returns
                    
                    ```json
                    {
                      "revenue":number,
                      // 매출액
                    	"opInc":number,
                    	// 영업이익
                    	"netInc":number,
                    	// 당기순이익
                      "opMargin":number,
                    	// 영업이익률(계산가능)
                    	"netMargin":number,
                    	// 순이익률(계산가능)
                    	"deptEquity":number,
                    	// 부채비율
                    	"quick":number,
                    	// 당좌비율
                    	"reserve":number,
                    	// 유보율
                    	"poe":number,
                    	// POE(계산가능)
                    	"eps":number,
                    	// EPS(계산가능)
                    	"per":number,
                    	// PER(계산가능)
                    	"bps":number,
                    	// BPS(계산가능)
                    	"pbr":number,
                      // PBR(계산가능)
                    	"devidend":number,
                    	// 주당배당금
                    	"devidendPer":number
                    	// 시가배당률(계산가능)
                    }
                    ```
                    
        - 해외 재무데이터
            
            
        - 해외 기업공시 - 시티팔콘 API 가이드 확인 불가로 작성에 어려움이 있음
            - 특정 종목의 공시 리스트
                - Parameter
                    - code (종목 코드)
                    - filters 세부 항목
                        - period
                        - source 4종
                        - category 14종
                        - type (100종 이상)
                - Returns
                    
                    ```json
                    {
                    	"status":string,
                    	// 에러 및 정보 코드
                    	"message": string,
                    	// 에러 및 정보 메시지
                    	"page_no": number,
                    	// 페이지 번호
                    	"page_count":number,
                    	// 페이지 별 건수
                    	"total_count":number,
                    	// 총 건수
                    	"total_page":number,
                    	// 총 페이지 수
                    	"list": [ // 공시 리스트
                    		{
                    			"corp_name": string,
                    			// 종목명(법인명) 
                    			"corp_code": string,
                    			// 고유번호 
                    			"stock_code": string,
                    			// 종목코드 
                    			"report_nm": string,
                    			// 보고서명 
                    			"source": string,
                    			// 출처 
                    			"flng_dt": string,
                    			// 공시접수일자 
                    			"flng_ctgy": string,
                    			// 공시카테고리 
                    			"flng_type": string,
                    			// 공시타입 
                    			"actn_dt": string,
                    			// Action date
                    			"origin_link": string
                    			// 원문링크
                    			...
                    		},
                    		...
                    	]
                    }
                    ```
                    
        - 해외 statistics
        - 해외 screener
            - 원하는 범위값에 해당하는 주식 종목들
                - Parameters
                    - 시가총액 범위
                    - PER 범위
                    - PBR 범위
                    - 배당수익률 범위
                    - ROE 범위
                - Returns
                    - 해당 범위에 속하는 주식 종목들
                    
                    ```json
                    {
                      "items":[{
                    		"name":string,
                    	  // 종목명
                    		"ticker":string,
                    		// 심볼
                    		"type":string,
                    		// Nasdaq, NYSE
                    		"marketCap":number,
                    		// 시가총액
                    		}
                    	]
                    }
                    ```
