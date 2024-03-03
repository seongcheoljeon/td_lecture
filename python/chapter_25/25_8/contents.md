# 25-8. 계정 생성/삭제 및 권한 부여/취소 (CREATE USER, DROP USER, GRANT, REVOKE)

> MySQL 기준으로 작성됨

Database 사용자 목록을 조회하기 위해서는 MySQL의 기본 스키마인 `mysql` 데이터베이스의 `user` 테이블을 조회하면 된다.

```sql
USE mysql;

SELECT host, user, plugin, authentication_string FROM user;
```

## 사용자 생성 (CREATE USER)

사용자 생성은 `CREATE USER`명령으로 생성할 수 있다.

```sql
ex) CREATE USER 'user_name'@'host' IDENTIFIED BY 'password';

# 계정 생성 (내부 접근을 허용하는 사용자 추가)
CREATE USER 'seongcheoljeon'@'localhost' IDENTIFIED BY '1234';

# 계정 생성 (외부 접근을 허용하는 사용자 추가)
CREATE USER 'seongcheoljeon'@'%' IDENTIFIED BY '1234';

# 계정 생성 (특정 IP만 접근을 허용하는 사용자 추가)
CREATE USER 'seongcheoljeon'@'152.255.795.10' IDENTIFIED BY '1234';

# 계정 생성 (특정 IP 대역을 허용하는 사용자 추가)
CREATE USER 'seongcheoljeon'@'192.168.%' IDENTIFIED BY '1234';
```

## 사용자 삭제 (DROP USER or DELETE)

`DROP USER` 혹은 `DELETE` 명령어를 통해 사용자를 삭제할 수 있다.

```sql
ex) DROP USER ['user_name']@['server_name'];

DROP USER 'seongcheoljeon'@'%';

# 혹은

DELETE FROM user WHERE user='user';
```

## 사용자 권한 부여

사용자에게 권한을 부여할 때는 `GRANT` 명령어를 통해 부여할 수 있다.

```sql
# ex) GRANT ALL PRIVILEGES ON [database_name].[table_name] TO ['user_name']@['server_name'];

# 권한 설정 (모든 DB에 모든 권한 부여)
GRANT ALL PRIVILEGES ON *.* TO 'seongcheoljeon'@'%';

# 특정 DB에 모든 권한 부여
GRANT ALL PRIVILEGES ON test_db.* TO 'seongcheoljeon'@'%';

# 특정 DB에 특정 권한 부여
GRANT SELECT, INSERT, UPDATE ON test_db.* TO 'seongcheoljeon'@'%';

# 특정 DB의 특정 테이블에 SELECT 권한 부여
GRANT SELECT test_db.asset_table TO 'seongcheoljeon'@'%';

# 특정 DB의 특정 테이블의 column1, column2에 UPDATE 권한 부여
GRANT UPDATE(column1, column2) ON test_db.asset_table TO 'seongcheoljeon'@'%';
```

## 사용자 생성과 동시에 권한 부여

사용자 계정 생성함과 동시에 권한을 부여할 수 있다.

```sql
# ex) GRANT ALL PRIVILEGES ON [database_name].[table_name] TO ['user_name']@['server_name'] IDENTIFIED BY ['password'];

GRANT ALL PRIVILEGES ON test_db.* TO 'seongcheoljeon'@'%' IDENTIFIED BY '1234';
```

## 사용자 권한 취소

사용자 계정의 권한 취소는 `REVOKE` 명령어로 취소할 수 있으며, `GRANT` 명령어 사용법과 비슷하다.

```sql
# ex) REVOKE ALL PRIVILEGES ON [database_name].[table_name] TO ['user_name']@['server_name']; 

# 모든 권한 취소
REVOKE ALL PRIVILEGES ON *.* FROM 'seongcheoljeon'@'%';

# INSERT 권한 취소
REVOKE INSERT ON *.* FROM 'seongcheoljeon'@'%';
```

## 권한 설정 적용 (변경 사항 반영)

```sql
FLUSH PRIVILEGES;
```

## 권한 부여 상태 확인

```sql
SHOW GRANTS FOR 'seongcheoljeon'@'%';
```