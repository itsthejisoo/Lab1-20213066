# parking lot_app

## introduction
- info of parking lot nearby, leftover parking spot application

## features
1. GPS tracking  
: 사용자 위치를 찾고 근처 주차장을 추천해줍니다.  
2. Booking  
: 주차 공간을 예약할 수 있습니다. 소유하고 있는 포인트로 할인할 수 있습니다.  
3. Monthly fee  
: 월정액을 지불하면 모든 주차장 요금 무료 또는 80% 할인 받을 수 있습니다.  
4. Price comparison  
: 근처 주차장의 요금을 비교해줍니다.  
5. Distance comparison  
: 주차장과 현재 위치 거리를 비교하여 가장 가까운 주차장을 추천해줍니다.  
6. Bookmark favorite lot  
: 즐겨찾기된 주차장은 사용자의 즐겨찾기 파일에 추가됩니다.  
7. Leftover Parking spot  
: 주차장 자리가 얼마 남았는지 확인해줍니다.  

## model
- User
- Lot
- Parking
- Bookmark
- Leftover

## urls
- users  
POST /users/  
: 사용자 등록  
PUT /users/id  
: 사용자 정보수정  
GET /users/id  
: 사용자 세부정보  
POST /users/login   
: 사용자 로그인  
DELETE /users/logout   
: 사용자 로그인  
DELETE /users/deactivate  
: 사용자 계정삭제   
GET /bookmark/  
: 북마크 리스트  
POST /bookmark/  
: 북마크 등록   
DELETE /bookmark/id  
: 북마크 삭제  

- lots  
POST /lots/  
: 주차장 등록  
PUT /lots/id  
: 주차장 정보수정  
GET /lots/id  
: 주차장 세부정보  
GET /lots/map(action)   
: 주차장 맵뷰(예: 서울시)  
GET /lots/distance_odr  
: 주차장 목록 거리순 정렬  
GET /lots/price_odr   
: 주차장 목록 가격순 정렬  
DELETE /lots/id   
: 주차장 삭제  

- parkings  
POST /parkings/   
: 주차 이벤트 생성(주인의 사용내역만)  
GET  /parkings/  
: 유저의 주차 내역 목록(총비용, 주차장 정보)  
GET  /parkings/id  
: 주차세부정보 (총비용, 주차장 정보)   
PUT  /parkings/id/  
: 주차시간을 추가(추가결제)  
