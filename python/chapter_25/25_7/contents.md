# 25-7. Trigger

> 트리거(trigger)는 사전적 의미로 `방아쇠`라는 뜻으로 __Database의 Table에서 어떤 이벤트가 발생했을 때 자동으로 실행되는 것을 말함__

특정 테이블에 레코드가 추가/삭제 혹은 업데이트 등의 이벤트가 발생할 경우, 자동으로 어떠한 행동을 취하고 싶을 때 사용하는 것이 
`트리거(Trigger)`이다.   

즉, `Database`의 `Trigger`는 `특정 이벤트(INSERT, UPDATE, DELETE 등)`가 발생할 때 자동으로 실행되는 Database의 `Procedure(프로시저)`이다.

## Trigger 확인

현재 DB에서 존재하는 trigger를 확인하는 방법은 다음과 같다.

```sql
SHOW TRIGGERS;
```

+ __Trigger__
  + trigger의 이름
+ __Event__
  + trigger가 작동되는 이벤트의 유형 (UPDATE, DELETE, INSERT)
+ __Table__
  + trigger가 연결되어 있는 테이블의 이름
+ __Statement__
  + trigger의 실행 내용 (BEGIN ~ END 사이의 SQL)
+ __Timing__
  + trigger가 실행되는 시기 (BEFORE or AFTER)
+ __Created__
  + trigger가 생성된 날짜 및 시간
+ __sql_mode__
  + trigger 실행에 영향을 미치는 SQL 모드

## Trigger 생성 (CREATE TRIGGER)

```sql
CREATE TRIGGER tgr_after_insert_test_table
    AFTER INSERT ON test_table
    FOR EACH ROW
    BEGIN
        INSERT INTO hist_table (name, ctime) VALUES (NEW.name, NOW());
    END;
```

+ __CREATE TRIGGER__
  + trigger의 이름 지정
+ __BEFORE or AFTER__
  + trigger의 실행 시점 지정
  + __BEFORE__
    + 이벤트 발생 전 실행
  + __AFTER__
    + 이벤트 발생 후 실행
+ __INSERT, UPDATE, DELETE__
  + trigger가 어떤 이벤트에서 발생할지를 지정
+ __TABLE_NAME__
  + trigger가 연결될 테이블의 이름 지정
+ __FOR EACH ROW__
  + 각 행에 대해 trigger를 실행할지 여부 지정
+ __BEGIN ~ END__
  + trigger의 실행 내용 정의
  + trigger 내에서 `NEW`라는 예약어를 사용하여 트리거가 실행된 이벤트로부터 새로 추가된 행의 값을 사용할 수 있다.

`변경 전` 또는 `변경 후`의 행은 `OLD` 와 `NEW` 라는 가상 변수를 사용하여 읽을 수 있다.
* __OLD__
  * 이전 데이터
    * `DELETE`로 제거된 데이터 또는 `UPDATE`로 바뀌기 전의 데이터
* __NEW__
  * 새로운 데이터
    * `INSERT`로 삽입된 데이터 또는 `UPDATE`로 바뀐 후의 데이터

|trigger event|OLD|NEW|
|---|---|---|
|INSERT|X|O|
|UPDATE|O|O|
|DELETE|O|X|

## Trigger 삭제

```sql
DROP TRIGGER trigger_name;
```