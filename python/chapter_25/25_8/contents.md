# EVENT (Scheduler)

> 이벤트 스케쥴러 (Event Scheduler)
> > 이벤트 스케쥴러는 말 그대로 이벤트 발생 계획을 말하는 것이다. 이를 테면, 한 달에 한 번 데이터베이스 데이터 백업, 임시 데이터 삭제등이 있을 것이다.

`EVENT Scheduler`는 주기적으로 데이터베이스에 작업을 해야 할 경우 사용한다. 만약 지속적으로 쌓이는 임시(Temporary) 데이터가 있을 때, 해당 테이블을
일정 간격으로 지워줌으로써 용량 차지가 되지 않게끔 한다.

## EVENT Scheduler 설정

* Event Scheduler 사용하기 위해선 설정을 `ON`으로 변경해주어야 한다. 이 명령은 다음과 같다.

```sql
SET GLOBAL event_scheduler = ON;
```

* 이벤트 설정 확인 명령은 다음과 같다.

```sql
SHOW VARIABLES LIKE 'event%';
```

## EVENT Scheduler 생성

* 이벤트 스케쥴러 형식

```sql
CREATE EVENT [IF NOT EXISTS]
    <event_name>
    ON SCHEDULE <schedule> # 반복할 시간 및 기간
    [ON COMPLETION [NOT] PRESERVE]
    [ENABLE | DISABLE | DISABLE ON SLAVE]
    [COMMENT <이벤트 설명>]
    DO 
        <수행 SQL>;
        
schedule: {
    AT TIMESTAMP [+ INTERVAL interval] ... | EVERY INTERVAL
    [STARTS TIMESTAMP [+ INTERVAL interval] ...]
    [ENDS TIMESTAMP [+ INTERVAL interval] ...]
}

interval: {
    quantity: {
        YEAR | QUARTER | MONTH | DAY | HOUR | MINUTE | WEEK | SECONDS | YEAR_MONTH | DAY_HOUR | DAY_MINUTE |
        DAY_SECOND | HOUR_MINUTE | HOUR_SECOND | MINUTE_SECOND
    }
}
```

+ __AT <timestamp>__
  + 특정 시간에 단 한번 실행
    + ex) ON SCHEDULE AT '2024-03-07 00:00:00'
+ __EVERY <interval>__
  + 반복 실행
    + ex) ON SCHEDULE EVERY 1 DAY
+ __STARTS <timestamp>, ENDS <timestamp>__
  + 시작일 ~ 종료일 지정
  + ex) ON SCHEDULE EVERY 1 DAY STARTS '2024-01-01 00:00:00' ENDS '2024-12-31 00:00:00'
+ __ON COMPLETION NOT PRESERVE ENABLE__
  + 해당 설정은 이벤트를 수행 후 삭제 여부를 지정한다.
  + 이벤트 수행 후, 이벤트를 삭제하고 싶지 않다면 `NOT`을 제거한 __ON COMPLETION PRESERVE ENABLE__ 을 사용한다.

* 현재 시간+10초부터 이벤트 스케쥴러 시작하여 매 10초마다 INSERT SQL 실행

```sql
CREATE EVENT IF NOT EXISTS  ev_insert_to_test_table
    ON SCHEDULE EVERY 10 SECOND
    STARTS (TIMESTAMP (CURRENT_TIME) + INTERVAL 10 SECOND )
    COMMENT 'every time 10 sec!!'
    DO
        INSERT INTO test_table(name, ctime) VALUES ('event data', NOW());
```

* 현재 시간+10초에 단 한번 INSERT SQL 실행

```sql
CREATE EVENT IF NOT EXISTS ev_once_cmd
    ON SCHEDULE
        AT (TIMESTAMP (CURRENT_TIME) + INTERVAL 10 SECOND )
    ON COMPLETION PRESERVE
    ENABLE
    COMMENT 'once command event'
    DO
        INSERT INTO test_table(name, ctime) VALUES ('once event data', NOW());
```

* 매일 새벽 3시에 `history` 테이블에서 30일 전의 데이터를 삭제

```sql
# `ev_daily_delete` 라는 이름의 이벤트 생성
CREATE EVENT IF NOT EXISTS ev_daily_delete
# 해당 이벤트가 매일 실행되도록 스케쥴 설정
  ON SCHEDULE EVERY 1 DAY
# 해당 이벤트가 처음 실행되는 시간 설정
    STARTS (TIMESTAMP(CURRENT_DATE) + INTERVAL 1 DAY)
    DO
# `history` 테이블에서 30일 이전의 데이터를 삭제한다.
    DELETE FROM history WHERE created_date < DATE(NOW() - INTERVAL 30 DAY);
```

* 현재 시각으로부터 10분 후 모든 데이터 제거

```sql
CREATE EVENT IF NOT EXISTS history_data
  ON SCHEDULE
    AT DATE_ADD(NOW(), INTERVAL 10 MINUTE)
  ON COMPLETION NOT PRESERVE
  ENABLE
  COMMENT 'delete data'
  DO
    TRUNCATE history;
```

## EVENT Scheduler 목록 확인

```sql
SELECT * FROM information_schema.EVENTS;

# 혹은

SHOW EVENTS;
```

## EVENT Scheduler 삭제

```sql
DROP EVENT IF EXISTS <이벤트 이름>;
```

## EVENT Schduler 수정

```sql
ALTER 
    [DEFINER = user]
    EVENT <event_name>
    [ON SCHEDULE schedule]
    [ON COMPLETION [NOT] PRESERVE]
    [RENAME TO <new_event_name>]
    [ENABLE | DISABLE | DISABLE ON SLAVE]
    [COMMENT 'event comment']
    [DO event_body]
```

이벤트를 수정하려면 `ALTER EVENT` 명령을 사용한다. 

다음의 예는 생성한 이벤트를 매일 오전 10시에 실행되도록 변경하는 예이다.

```sql
ALTER EVENT ev_daily_delete
  ON SCHEDULE EVERY 1 DAY
  STARTS (TIMESTAMP(CURRENT_DATE) + INTERVAL 1 DAY + INTERVAL 1 HOUR);
```

---

# Cron VS EVENT Scheduler 장단점

> Cron
> > Cron은 특정 시간에 특정 동작을 하는 것을 말한다. 대표적으로 [Linux Cron](https://docs.rockylinux.org/ko/guides/automation/cron_jobs_howto)이 있다. 그 외에는 `Spring Scheduling`, `Node-cron` 등이 있다.

> Event Scheduler
> > DB에서 정기적으로 특정 시간에 작업을 수행시킬 수 있다. 대표적으로는 `MySQL`의 `Event scheduler`, `Oracle scheduler` 등이 있다.

+ __Cron__
  + __장점__
    + 예상하기 쉬운 위치에 존재 (이 점을 과소평가해선 안 된다).
    + 원하는 곳으로 성공/오류 메시지를 전달할 수 있음.
    + 웹 서버와 DB의 역할을 분리하여 관리 가능.
    + 일부 DB 작업은 MySQL이 오프라인 상태(ex: 전체 백업)로 진행되는데 이러한 작업에는 크론을 사용해야 함.
      + 일부 작업은 크론으로, 일부 작업은 MySQL Event로 수행하는 것은 상당히 좋지 않음.
    + Shell 스크립트로 운용 시, Event에 Dependency(의존성)를 부여할 수 있음.
  + __단점__
    + DB와의 통신으로인해 지연 시간 발생.

+ __Event Scheduler__
  + __장점__
    + 외부 스크립트를 사용할 필요 없음.
    + 매변 쿼리를 컴파일할 필요가 없음.
    + 성능이 뛰어남.
  + __단점__
    + 기능 변경 시, DB에 접근한 후 수정해야 함.
    + 이벤트 존재유무 파악하기 힘듦.

## 정리

SQL의 작업이라면 MySQL Event에서 처리하는 것이 합리적일 것이다. 즉, MySQL Event에서 `데이터 정리`, `최적화` 등의 작업은 MySQL EVENT가 
더 나은 선택이다.

만약 SQL의 작업이 아니라면, `Cron`을 사용하는 것이 좋은 선택이다.
