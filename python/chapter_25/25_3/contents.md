# 25-3. SQL 기초 (SELECT, CREATE, DROP, INSERT, UPDATE, DELETE, ...)

## DATABASE

모든 데이터베이스 조회
```sql
SHOW DATABASES;
```

데이터베이스 생성
```sql
CREATE DATABASE <db_name> DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

데이터베이스 삭제
DROP DATABASE IF EXISTS <db_name>;

## TABLE

현재 DB에 존재하는 모든 테이블 조회
```sql
SHOW TABLES;
```

테이블 구조 확인
```sql
DESC <table_name>;
```

테이블 생성
```sql
CREATE DATABASE <table_name> DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

조회 결과로 테이블 생성
```sql
CREATE TABLE <생성 할 table_name> AS (SELECT * FROM <기존의 table_name>);
```

테이블 삭제
```sql
DROP TABLE IF EXISTS <table_name>;
```

## SELECT

데이터베이스에 질의(Query)를 보낼 때 사용

```sql
SELECT * FROM <table> WHERE <조건식>;
```

ex) a가 0이 아니거나 b가 0이 아닌 행 반환
```sql
SELECT * FROM <table> WHERE NOT (a<>0 OR b<>0);
```

### LIKE

특정 문자나 문자열이 포함되어 있는지를 검색하고 싶은 경우 ‘패턴 매칭’(부분 검색)을 사용

ex) text 열에 ABC가 포함되어 있는 행 검색
```sql
SELECT * FROM <table> WHERE text LIKE '%ABC%';
```

### GROUP BY / HAVING

+ GROUP BY
  + 특정 컬럼을 그룹화
+ HAVING
  + 특정 컬럼을 그룹화한 결과에 조건

```sql
SELECT <column> FROM <table> GROUP BY <그룹화 할 컬럼>;
```

ex) 조건 처리 후, 컬럼 그룹화
```sql
SELECT <column> FROM <table> WHERE <조건식> GROUP BY <그룹화 할 컬럼>;
```

ex) 컬럼 그룹화 후, 조건 처리
```sql
SELECT <column> FROM <table> GROUP BY <그룹화 할 컬럼> HAVING <조건식>;
```

ex) 조건 처리한 결과에 컬럼 그룹화 진행 후 조건 처리
```sql
SELECT <column> FROM <table> WHERE <조건식> GROUP BY <그룹화할 컬럼> HAVING <조건식>;
```

ex) 정렬이 필요한 경우
```sql
SELECT <column> FROM <table> WHERE <조건식> GROUP BY <그룹화할 컬럼> HAVING <조건식> ORDER BY <column> [, column2, column3, ...];
```

ex) type 그룹화하여 name 개수를 가져온 후, 그 중 개수가 2개 이상인 데이터 조회
```sql
SELECT type, COUNT(name) AS cnt FROM dummy_table GROUP BY type HAVING cnt >= 2;
```