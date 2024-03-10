# 15-8. Database ORM(SQLAlchemy)

파이썬 코드에서 DB와 연결하기 위해서 사용할 수 있는 다양한 라이브러리가 있는데, 그 중 `SQLAlchemy`라는 라이브러리가 파이썬에서 가장 널리 
쓰이는 라이브러리 중 하나다. `SQLAlchemy` 라이브러리를 사용하여 파이썬 코드에서 데이터베이스에 연결하여 `SQL`을 실행시킬 수 있다.

SQLAlchemy는 ORM(Object Relational Mapper)이다.

> ORM(Object Relational Mapper)이란?
> > 관계형 데이터베이스의 테이블들을 프로그래밍 언어의 클래스로 표현할 수 있게 해주는 것을 말한다.
> > 즉, 클래스를 사용해서 테이블들을 표현하고 데이터를 저장, 읽기, 업데이트 등을 할 수 있게 해준다.
> 
> > ORM을 이용하면 데이터베이스를 정말 편하게 사용할 수 있다. 하지만 데이터베이스를 처음 시작하거나 배우는 단계라면,
> > 처음부터 ORM을 사용하면 좋지 못하다. 그 이유는 SQL을 배울 수가 없어서다. 데이터베이스의 SQL을 먼저 익숙하게 만들고
> > 그 다음 ORM을 사용하는 것이 좋다.

## SQLAlchemy 설치

```shell
pip install sqlalchemy
```

SQLAlchemy에서 `MySQL`을 사용하기 위해서는 MySQL용 `DBAPI` 또한 설치해야 한다. `DBAPI`는 이름 그대로 DB를 사용하기 위한 `API`이다.

`DBAPI`를 설치해야 해당 데이터베이스를 사용할 수 있다. `MySQL`용 `DBAPI`는 여러 가지가 있는데, 그 중 MySQL의 공식 파이썬 DBAPI인 
`MySQL-Connector`를 사용하도록 하자.

```shell
pip install mysql-connector-python
```

SQLAlchemy를 사용하면 데이터베이스에 연결하여 SQL을 실행시켜 데이터베이스로부터 데이터를 읽어 들이거나 생성하거나 할 수 있다.

예를 들어, users 테이블에서 사용자의 이름과 이메일을 다음과 같이 읽어 들일 수 있다.

```python
from sqlalchemy import create_engine, text


db = {
    "user": "root",
    "password": "1234",
    "host": "localhost",
    "port": 3306,
    "database": "test_db",
}

db_url = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}?charset=utf8"
database = create_engine(db_url, encoding="utf-8", max_overflow=0)

params = {"name": "scii"}
rows = database.execute(
    text("SELECT * FROM users WHERE name = :name"), params
).fetchall()
```
