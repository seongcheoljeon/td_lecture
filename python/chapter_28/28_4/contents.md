# 28-4. API 서버(FastAPI)

> FastAPI는 Python으로 API를 구축할 수 있게 해주는 빠르고 효율적인 웹 프레임워크이다.

마이크로서비스가 인기를 끌면서 API의 역할이 중요해졌고, 이에 따라 효율적으로 API를 개발할 수 있는 방법이 필요해졌다. FastAPI는 이런 요구를 
충족시켜주는 프레임워크이다. FastAPI를 사용하면 직관적이고 간단하게 API를 개발할 수 있으며 학습 난이도 또한 높지 않아 도입하기 쉽다.

FastAPI는 빠르고 가벼우며 [Flask](https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html)나 
[Django](https://docs.djangoproject.com/ko/5.0/intro/)와 같은 프레임워크보다 배우기 쉽다. 

+ __fastapi__
  + 애플리케이션을 구축하기 위해 필요한 프레임워크
+ __uvicorn__
  + 애플리케이션을 실행하기 위한 비동기(asynchronous)방식의 서버 게이트웨이 인터페이스

## FastAPI 설치 및 실행

```shell
pip install --upgrade pip
pip install fastapi uvicorn requests
```

api.py라는 파일을 생성 후 FastAPI의 새 인스턴스를 생성한다.

```python
from fastapi import FastAPI

app = FastAPI()
```
app 변수에 FastAPI를 초기화해서 라우트(route)를 생성할 수 있다.

```python
# 아래의 코드는 GET 유형의 요청을 받아서 메시지를 반환하는 '/' 라우트를 만든 것이다.

@app.get('/')
async def welcome() -> dict:
    return {
      'message': 'Hello World!'
    }
```

uvicorn을 사용하여 애플리케이션 실행해보자.

```shell
uvicorn api:app --port 8000 --reload
```

+ __file:instance__
  + ex) api:app
  + FastAPI 인스턴스가 존재하는 파이썬 파일과 FastAPI 인스턴스를 가지고 있는 변수 지정
+ __--port PORT__
  + 애플리케이션에 접속할 수 있는 포트 변호 지정
+ __--reload__
  + 선택적 인수로, 파일이 변경될 때마다 애플리케이션을 재시작

## 라우팅

라우팅은 웹 애플리케이션을 구축하는 데 있어 핵심적인 부분으로, 클라이언트가 서버로 보내는 HTTP 요청을 처리하는 프로세스이다. HTTP 요청이 지정한
라우트로 전송되면 미리 정의된 로직이 해당 요청을 처리해서 반환한다.

FastAPI의 라우팅은 사용하기 쉽고 유연하며 소규모와 대규모 애플리케이션 개발 시에도 사용할 수 있는 핵심 기술이다.

### FastAPI의 라우팅

라우트는 HTTP 요청 메서드의 요청을 수락하고 선택적으로 인수를 받을 수 있도록 정의된다. 요청이 특정 라우트로 전달되면 애플리케이션은 라우트 처리기(route handler)가
요청을 처리하기 전에 해당 라우트가 정의되어 있는지 확인한다. 라우트 처리기는 서버로 전송된 요청을 처리하는 함수다.   

> 라우트 처리기의 예로는 요청을 받아 데이터베이스에서 특정 데이터를 추출하는 함수가 있다.

#### HTTP 요청 메서드

HTTP 요청 메서드는 HTTP 메서드 처리 유형을 정의하는 식별자다. 표준 메서드에는 GET, POST, PUT, PATCH, DELETE등이 있다.

+ __GET__
  + 특정한 리소스를 가져오도록 요청
  + GET 요청은 데이터를 가져올 때만 사용해야 한다.
+ __HEAD__
  + GET 메서드의 요청과 동일하지만, 응답 본문(body)을 포함하지 않는다. 응답코드와 HEAD만 가져온다.
  + 웹서버 정보 확인, 버전 확인, 최종 수정 일자 확인 등의 용도로 사용
+ __POST__
  + 서버로 데이터 전송
  + 요청된 자원을 생성(CREATE)한다.
+ __PUT__
  + 요청된 자원을 수정(UPDATE)한다. 
+ __DELETE__
  + 특정 리소스 삭제 요청
+ __CONNECT__
  + 동적으로 서버 터널 교환 
  + 프록시 기능 요청시 사용
+ __OPTIONS__
  + 웹서버에서 지원되는 메소드의 종류를 확인할 경우 사용
+ __PATCH__
  + 리소스의 부분만을 수정
+ __TRACE__
  + 원격지 서버에 루프백 메시지 호출하기 위해 테스트용으로 사용

#### HTTP 응답 코드

서버에서의 처리 결과는 응답 메시지의 상태 라인에 있는 상태 코드(status code)를 보고 파악할 수 있다. 상태 코드는 세 자리 숫자로 되어 있는데 
첫 번째 숫자는 HTTP 응답의 종류를 구분하는 데 사용하며 나머지 2개의 숫자는 세부적인 응답 내용 구분을 위한 번호이다.

현재 100~500번 대까지 상태 코드가 정의되어 있는데 첫 번째 자리 숫자에 따라 다음과 같이 5가지로 분류해서 사용하고 있다.

+ __1XX__
  + Informational (정보 제공)
  + 임시 응답으로 현재 클라이언트의 요청까지는 처리되었으니 계속 진행하라는 의미이다. HTTP 1.1 버전부터 추가되었다.
+ __2XX__
  + Success (성공)
  + 클라이언트의 요청이 서버에서 성공적으로 처리되었다는 의미이다.
+ __3XX__
  + Redirection (리다이렉션)
  + 완전한 처리를 위해서 추가 동작이 필요한 경우이다. 주로 서버의 주소 또는 요청한 URI의 웹 문서가 이동되었으니 그 주소로 다시 시도하라는 
  의미이다.
+ __4XX__
  + Client Error (클라이언트 에러)
  + 없는 페이지를 요청하는 등 클라이언트의 요청 메시지 내용이 잘못된 경우를 의미한다.
+ __5XX__
  + Server Error (서버 에러)
  + 서버 사정으로 메시지 처리에 문제가 발생한 경우이다. 서버의 부하, DB 처리 과정 오류, 서버에서 예외가 발생하는 경우를 의미.

### APIRouter 클래스를 사용한 라우팅

APIRouter 클래스는 다중 라우팅을 위한 경로 처리 클래스로, fastapi 패키지에 포함되어 있다.

> APIRouter 클래스를 통해 애플리케이션 라우팅과 로직을 독립적으로 구성하고 모듈화할 수 있다.

fastapi 패키지에서 APIRouter 클래스를 import 한 후 APIRouter() 인스턴스를 생성할 수 있다. 라우팅 메서드는 다음과 같이 APIRouter() 
인스턴스를 사용해 생성한다.

```python
from fastapi import APIRouter

router = APIRouter()

@router.get('/hello')
async def func() -> dict:
    return {
      'message': 'world!'
    }
```

APIRouter 클래스를 사용해서 새로운 라우트와 라우트 처리기를 만들어보자. 

```python
from fastapi import APIRouter

todo_router = APIRouter()

todo_list = []

@todo_router.post('/todo')
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {
        'message': '할 일 추가 완료!'
    }

@todo_router.get('/todo')
async def retrieve_todos() -> dict:
    return {
        'todos': todo_list
    }
```
위 코드에서는 todo 처리를 위해 두 개의 라우트를 추가하였다. 첫 번째 라우트는 todo_list에 todo를 추가하는 POST 메서드이고, 두 번째 라우튼
모든 todo 아이템을 todo_list에서 조회하는 GET 메서드이다.

> APIRouter 클래스는 FastAPI 클래스와 동일한 방식으로 작동한다. 하지만 uvicorn은 APIRouter() 인스턴스를 사용해서 애플리케이션을 실행할 수 없다.   
> APIRouter 클래스를 사용해 정의한 라우터를 FastAPI() 인스턴스에 추가해야 외부에서 접근 가능하다.

> __include_router()__
> > include_router(router1, router2, ...) 메서드는 APIRouter 클래스로 정의한 라우트를 메인 애플리케이션의 인스턴스로 추가한다.   
> > 이렇게 하면 라우트를 전체 애플리케이션에서 사용할 수 있다.

```python
from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get('/')
async def func() -> dict:
    return {
        'message': 'Hello World!'
    }

app.include_router(todo_router)
```

```shell
# 애플리케이션 실행

uvicorn api:app --port 8000 --reload
```

curl로 GET 요청을 전송해 애플리케이션 테스트

