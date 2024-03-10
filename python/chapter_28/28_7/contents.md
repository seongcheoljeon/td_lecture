# 28-7. API 개발을 위한 유용한 툴

## [httpie](https://httpie.io/)

cURL보다 쉽게 터미널에서 HTTP 요청을 보낼 수 있게 해주는 툴이다.

```shell
http -v http://localhost:5000/ping
http -v POST http://localhost:5000/sign-up name=scii email=scii@gmail.com password=1234
```

## [thunder client](https://www.thunderclient.com/)

Thunder Client는 단순하고 깔끌한 디자인으로 `Visual Studio Code`용 경량 `Rest API` 클라이언트 확장 프로그램이다.

+ __특징__
  + 간단한 HTTP 요청
  + 환경 변수 및 변수 사용
  + 테스트 및 검증
  + 콜렉션과 폴더 구조
  + 코드 스니펫 생성
  + 다양한 HTTP 메서드 지원
