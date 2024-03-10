# 28-4. API 엔드포인트 아키텍처 패턴
 
API의 엔드포인트 구조를 구현하는 방식에도 널리 알려지고 사용되는 패턴들이 있다. 크게 `2가지`가 있는데, 하나는 `REST` 방식이록 다른 하나는 `GraphQL`이다. 

`REST` 방식은 가장 널리 사용되는 API 엔드포인트 아키텍처 패턴(architecture pattern)이다. 이미 많은 API 시스템들이 `REST` 방식으로 구현되어
있다.

`GraphQL`은 페이스북이 개발한 기술이며, 비교적 최근에 나온 기술이다.

## RESTful HTTP API

`REST(Representation State Transfer)ful HTTP API`는 API 시스템을 구현하기 위한 아키텍처의 한 형식이다. REST의 개념은 로이 필딩(Roby Fielding) 박사가
2000년 그의 박사학위 논문으로 처음 소개하였다.

`RESTful` API는 API에서 전송하는 리소스(resource)를 URI로 표현하고 해당 리소스에 행하고자 하는 의도를 HTTP 메소드로 정의하는 방식이다.
각 엔드포인트는 처리하는 리소스를 표현하는 고유의 URL 주소를 가지고 있으며, 해당 리소스에 행할 수 있는 행위를 표현하는 HTTP 메서드를 처리할 수 있게 된다.

예를 들어, 사용자 정보를 리턴하는 "/users"라는 엔드포인트에서 사용자 정보를 받아 오는 HTTP 요청은 다음과 같이 표현할 수 있다.

```shell
HTTP GET /users
GET /users
```

새로운 사용자를 생성하는 엔드포인트는 URI를 "/user"로 정하고 HTTP 요청은 다음과 같이 표현할 수 있다.

```shell
POST /user
{
  "name": "scii",
  "email": scii@gamil.com
}
```

이러한 구조로 설계된 API를 `RESTful API`라고 한다.

To be continue...

