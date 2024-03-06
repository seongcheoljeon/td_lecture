# 25-3. SQL 기초 (SELECT, CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, ...)

> __CRUD란?__
> + Create (INSERT)
>   + 추가
> + Read (SELECT)
>   + 읽기
> + Update (UPDATE)
>   + 수정
> + Delete (DELETE)
>   + 삭제

## DATABASE

### 모든 데이터베이스 조회

```sql
SHOW DATABASES;
```

### 데이터베이스 생성

```sql
CREATE DATABASE IF NOT EXISTS <db_name> DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
```

### 데이터베이스 삭제

DROP DATABASE IF EXISTS <db_name>;

---

## TABLE

### 현재 DB에 존재하는 모든 테이블 조회

```sql
SHOW TABLES;
```

### 테이블 구조 확인

```sql
DESC <table_name>;
```

### 테이블 생성
```sql
CREATE TABLE IF NOT EXISTS <table_name> DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
```

### 조회 결과로 테이블 생성

```sql
CREATE TABLE IF NOT EXISTS <생성 할 table_name> AS (SELECT * FROM <기존의 table_name>);
```

### 테이블 삭제

```sql
DROP TABLE IF EXISTS <table_name>;
```

---

## ALTER (테이블 수정)

ALTER TABLE은 그리 자주 사용하지는 않는다.

### ADD (컬럼 추가)

```sql
ALTER TABLE <table_name> ADD COLUMN <추가할 컬럼> VARCHAR(32) NOT NULL;
```

### MODIFY (컬럼 변경)

```sql
ALTER TABLE <table_name> MODIFY COLUMN <변경할 컬럼> <변경할 컬럼 타입> NULL;
```

```sql
# 컬럼 순서 변경
ALTER TABLE <table_name> MODIFY <순서 변경할 컬럼명> <순서 변경할 컬럼 타입> AFTER <앞에 오는 컬럼명>;
```

### CHANGE (컬럼명까지 변경)

```sql
ALTER TABLE <table_name> CHANGE COLUMN <기존의 컬럼명> <변경할 컬럼명> VARCHAR(32) NULL;
```

### DROP (컬럼 삭제)

```sql
ALTER TABLE <table_name> DROP COLUMN <삭제할 컬럼>
```

### RENAME (테이블명 변경)

```sql
ALTER TABLE <기존의 테이블명> RENAME <변경할 테이블명>
```

### 그 외...

```sql
# 컬럼 디폴트 값 변경
# ex) ALTER TABLE <테이블명> ALTER COLUMN <변경할 컬럼명> SET DEFAULT <디폴트값>;

ALTER TABLE <테이블명> ALTER COLUMN <변경할 컬럼명> SET DEFAULT 100;
```

---

## SELECT <CRUD에서 R(Read)에 해당>

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

---

## INSERT <CRUD에서 C(Create)에 해당>

`INSERT INTO`문을 사용하여 테이블에 새로운 레코드를 추가할 수 있다.

```sql
INSERT INTO <table> (field1, field2, field3, ...) VALUES (data1, data2, data3, ...);
```

생략할 수 있는 필드는 다음과 같다.

+ NULL을 저장할 수 있도록 설정된 필드
+ DEFAULT 제약 조건이 설정된 필드
+ AUTO_INCREMENT 키워드가 설정된 필드

_여러 개의 레코드를 동시에 추가하는 방법은 다음과 같다._

```sql
INSERT INTO <table> (field1, field2) VALUES (data1, data2), (data3, data4), (data5, data6), ...;
```

특정 테이블의 내용을 특정 테이블에 추가하는 것은 `INSERT INTO`와 `SELECT`를 이용하면 된다. 이때 조회 시 출력되는 컬럼들의 데이터형이나 개수가
정확하게 맞아야 한다.

```sql
INSERT INTO <dest table> (field1, field2) SELECT field1, field2 FROM <source table> WHERE <field> LIKE 'J%';
```

---

## DELETE <CRUD에서 D(Delete)에 해당>

테이블에 저당되어 있는 `레코드`를 `삭제`하기 위한 Query문이다.

> DELETE FROM <테이블명> WHERE <조건>;

### 테이블 전체 레코드 삭제

테이블의 모든 데이터를 제거할 때, 다음과 같이 쿼리를 실행하면 된다.

```sql
DELETE FROM <table>;
```

### 조건절을 이용한 특정 레코드 삭제

조건에 부합하는 레코드만 삭제할 경우 다음과 같이 쿼리를 구성하면 된다.

```sql
DELETE FROM <table> WHERE <field> = '<value>';
```

## TRUNCATE

테이블의 모든 데이터를 `완전히 삭제`한다. `TRUNCATE`는 `DROP`과 `CREATE TABLE` 순차적으로 실행한 결과와 같다. 즉, `TRUNCATE`는 레코드 단위가
아닌 테이블 자체를 `초기화`하는 것이다.

```sql
TRUNCATE TABLE <table>;
```

### TRUNCATE와 DELETE의 공통점 / 차이점

+ __공통점__
  + 두 명령어 모두 `테이블의 레코드를 삭제`하기 위하여 사용된다.
+ __차이점__
  + `TRUNCATE`는 `DELETE`보다 더 빠른 수행속도를 보인다. 
  + `TRUNCATE`는 테이블 명세만 남기고 데이터가 존재하던 공간을 모두 제거하므로 `복구 불가능`하다. 또한 `AUTO_INCREMENT`값 역시 `초기화`된다.
  + `DELETE`는 조건절에 맞는 데이터를 `선택하여 삭제`할 수 있지만, `TRUNCATE`는 `전체 데이터만 삭제` 할 수 있다.

---

## UPDATE <CRUD에서 U(Update)에 해당>

데이터베이스의 테이블에서 이미 저장된 값을 수정하는 명령이다. 주의할 점은 조건절이 없다면, 모든 레코드가 변경하려는 값으로 모두 치환될 수 있는 점이다.

```sql
UPDATE <table> SET <field> = '<value>' WHERE <field> = <value>;

ex) UPDATE test_tbl SET name = 'scii' WHERE id = 1;
```