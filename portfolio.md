# 한상훈 포트폴리오

## 프로젝트

### TG Mentoring - 학원 학생 멘토링 관리 시스템
<image src="https://drive.google.com/uc?id=1-BlC8cRLV7YlEHfvHacIFY1HfHHkEmfw" width="400px">

웹 기반의 학원 학생들에 대한 강사들의 멘토링 프로그램 관리 시스템 어플리케이션을 작성. 학생-강사 간 질문/멘토링 커뮤니케이션을 비롯하여 기본적인 커뮤니티 기능과 메시지, noti 기능을 포함한다. 웹뷰 형태의 안드로이드 어플리케이션.

#### 세부내용
* 개인프로젝트
* cafe24 hosting Apache+PHP+MySQL, android application, BootStrap, jQuery
* [앱 화면 스크린샷.zip](https://drive.google.com/file/d/1OYLtyNITSDE6EP177WcgSZInbUjGik5m/view?usp=sharing)

### SMART DORM - IoT 스마트 기숙사 시스템(똑긱)
<image src="https://drive.google.com/uc?id=1ElDqhExJwWNMtHD3epMHPvDk0ZcrKQGC" width="200px">

MIT random hall bathroom, laundry 서비스를 차용하여 Samsung ARTIK 을 이용한 스마트 기숙사 시스템 어플리케이션을 작성. ([MIT](https://bathroom.mit.edu) - 현재는 운영되고 있지 않은듯) 

ARTIK device와 ARTIK Cloud를 통해 세탁기의 이용 현황 확인 기능과 교내 학사정보 관리 시스템에서 개인 시간표를 크롤링하여 이용하는 스마트 알람 기능을 포함한다.

#### 세부 내용
* 팀프로젝트 - 조장으로 참여, android, api server, artik 전반 담당
* cafe24 hosting Apache+PHP+MySQL, android application, beautifulSoup, [ARTIK Cloud](https://www.artik.io) -RULES, ARTIK Device
* [최종 결과 보고서](https://drive.google.com/file/d/1t5SMyL6oeRTHbqbTtwH8bBSWDX5urZfP/view?usp=sharing) - 6,7페이지에 App 화면 포함
* [프로젝트 제안발표](https://drive.google.com/open?id=0B-YxUAwUHhV-TVpzTUl0Ulo0Qjg)


### SOBS - 교수 OfficeHour 예약 시스템
<image src="https://drive.google.com/uc?id=1931MSp9kjF_mu1UkSxQMXO0J-Z6w8tEC" width="500px">

교수와의 상담을 원하는 학생들과 교수들의 편의를 위하여 성균관대학교 컴퓨터공학과/글로벌경영학과 교수진의 Office Hour 확인/예약 시스템을 작성.

학교 이메일 가입/로그인 기능, [fullCalendar](https://fullcalendar.io) 를 사용한 교수의 면담 가능 시간과 타 학생들의 예약 시간 확인 기능, 메일 전송 기능을 구현. 예약 시 대체 시간을 함께 포함하여 일자 조정.

#### 세부 내용
* 팀프로젝트 - 1인 개발 진행
* cafe24 hosting Apache+PHP+MySQL, jQuery, fullCalendar, phpMailer, summernote
* [gitHub](https://github.com/poerty/officeHour)
* [site link](https://poerty.co.kr/OfficeHour/new.html)

### palmchinese - 중국어 학습 어플리케이션
<image src="https://drive.google.com/uc?id=14zoeWGhAGCG9lOCwnaS9jcUoCCEGYl3P" width="200px">

[팜코리아](http://palmchinese.cafe24.com)의 중국어 교재와 연계한 학습 어플리케이션을 작성. 집필하고 있는 중국어 교재의 내용을 강사가 생성/수정할 수 있는 웹 기반 저작도구와 (그 내용은 실시간으로 어플리케이션에 반영) 학습 및 복습 어플리케이션(현재 사측에서 교재 내용 집필중)

웹 저작도구: 강의(교재)별 문제, 학습 내용 생성 및 수정 기능

어플리케이션: json형태로 받아온 데이터를 기반으로 한 학습, 문제 풀기 기능, 기존 서버와의 통신을 통한 로그인 기능 등

#### 세부 내용
* 팀프로젝트 - 안드로이드 어플리케이션 담당
* nodejs, angular, android application, retrofit
* [최종 발표 ppt](https://drive.google.com/file/d/14XpMOt0gxnHxAOO3w0cU-TMK60jATF3_/view?usp=sharing)
* [시연 영상 mp4](https://drive.google.com/file/d/1bXy7Ofopw1-lxjaXyNNTshbpbp7_wvDJ/view?usp=sharing)


### FOODING - 식품 원재료 및 영양정보 제공 시스템
<image src="https://drive.google.com/uc?id=0B85gXFeYWRPUcUpjTUQ3Z3VrN0U" width="200px">

NFC 태그/QR 코드/id검색 등을 통하여 각 식품에 포함된 재료와 영양정보를 제공하는 어플리케이션을 작성. 원재료부터 재료의 조합에 따라 chain과 같이 모든 식품의 정보를 생성하는 시스템을 통해 구현하였다. 각 사업장(식품가게, 제조사 등) 별 식품 등록을 가능하게 하고, 제조 시, NFC 태그/QR 코드/id검색 등을 통하여 얻은 식품 재료의 조합을 통하여 자동적으로 제조된 식품의 재료와 영양정보를 생성한다.

일반 사용자와 사업자 어플리케이션으로 나누어 개발하였으며, API 서버와 데이터 view 웹도 같이 개발하였다.

사용자용 어플리케이션: NFC 태그/QR 코드/id검색 를 통해 해당 식품의 원재료/영양정보를 검색하는 기능, 비선호식품/칼로리 필터, 외 잡다한 기능

사업자용 어플리케이션: 식품(레시피)를 생성하고 NFC 태그/QR 코드를 생성하는 기능, 식품(레시피) 관리 기능, 서버와의 통신을 통한 회원가입/로그인 기능, 외 잡다한 기능

#### 세부 내용
* 팀프로젝트 - 사업자용 어플리케이션과 API 서버, 웹 담당
* cafe24 hosting Apache+PHP+MySQL, android application, retrofit
* [사업자 App GitHub](https://github.com/CDP-Group2/FOODINGCOMPANY)
* [API Server GitHub](https://github.com/poerty/foodingAPI)
* [시연 영상 mp4](https://drive.google.com/file/d/1KkjbGxosah94qaYFug0I71Pm9kdqMFh_/view?usp=sharing)
* [결과 보고서](https://drive.google.com/file/d/19b9Ex4jC-EN3HRRdQbByOkQa6BIWzdyZ/view?usp=sharing)


### 특정 지점 익일 주가 예측 프로그램

주가 고상승 지점(ex 상한가)의 익일 주가에 대한 예측 모델을 작성. 여러 실험을 통해 최적의 모델을 생성하였고, 학습시킨 모델을 실제 데이터를 통해 검증하였다.

#### 세부 내용
* 개인프로젝트
* python, sklearn, pandas
* [GitHub](https://github.com/poerty/stockEstimation)
* [결과 보고서](https://drive.google.com/file/d/1XA2ZlzHhLc7Q2wCj2jSBdFTqPOuOqJt6/view?usp=sharing)
* [결과 발표 ppt](https://drive.google.com/file/d/1G22ueP4OKvR0LmN__dEIk8jOQIXRC6tD/view?usp=sharing)




## 기타 활동

### DNSNA: DNS Name Autoconfiguration for IoT Home Devices 보조 수행
Naming info query 의 교환을 통해 DNS Server에서 자동적으로 DNS Name Registration 과정을 거치고, Android Device에 DNS Name List 를 쏴주는 것

연구를 진행하는 것을 보며 배우고 보조하는 역할을 맡았다

* 연구실 내 DNS Server 를 설치하고 구동, NI query 소스를 분석하여 자동 dns 업데이트 소스를 작성하였고, 서버와 쿼리를 주고받는 안드로이드 어플리케이션 제작을 맡았음.
* 성균관대학교 산학협력 c-school 총장상 수상

### [Google codejam 2016 2 round 참가(닉네임:poerty)](https://code.google.com/codejam/contest/4314486/scoreboard#sp=961)

* 구글 코드잼 대회에 참가해 2round 진출까지 했으나(총 3000명 진출) 2 round에서 탈락했다.