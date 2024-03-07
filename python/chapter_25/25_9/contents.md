# 25-9. PROCEDURE & FUNCTION

## PROCEDURE

> 프로시저 (Procedure) 란?
> > 프로시저는 `일련의 쿼리를 모아 마치 하나의 함수처럼 실행`하기 위한 쿼리 집합이다.

+ __프로시저 장점__
  + 하나의 요청으로 여러 SQL 문을 실행할 수 있다. (네트워크 부하를 줄임)
  + 내부 중간 코드로 변환되어 처리 속도가 빨라진다.
  + DB 트리거와 결합하여 복잡한 규칙에 의한 데이터의 참조무결성 유지가 가능하게 된다.
+ __프로시저 단점__
  + 재사용성이 좋지 못하다.

    
## FUNCTION

프로시저(Procedure)와 비슷하지만, 함수의 경우 특별한 데이터 타입으로 특별한 연산을 할 때 더 용이하다.

기본 형태는 다음과 같다.

```sql
DELIMITER $$
CREATE FUNCTION IF NOT EXISTS 함수명(매개변수 자료형) RETURNS 반환_자료형
BEGIN
    DECLARE 변수명 <자료형> DEFAULT NULL;
    
    수행할 쿼리
    RETURN 반환값
END $$
DELIMITER ;
```

다음은 두 수를 받아 곱한 결과를 반환하는 함수이다.

```sql
DELIMITER $$
CREATE FUNCTION IF NOT EXISTS multiply(a DOUBLE, b DOUBLE) RETURNS DOUBLE
BEGIN
    RETURN a * b;
END $$
DELIMITER;
```

위에서 BEGIN ~ END 사이에 구문 문자인 `; (세미콜론)`때문에 오류가 발생하지 않도록 `DELIMITER`명령어를 통해 기존 구문 문자인
`; (세미콜론)`을 `$$`로 바꿔주는 해준다.

함수는 다음과 같이 `SELECT`명령어를 통해 사용할 수 있다.

```sql
SELECT 함수명(매개변수);
```

함수에서 변수 선언은 아래 명령어를 통해 할 수 있다. 

```sql
DECLARE <변수명> <자료형>;
```

### 함수 확인

```sql
SHOW CREATE FUNCTION <함수명>;
```

### 함수 삭제

```sql
DROP FUNCTION <함수명>;
```