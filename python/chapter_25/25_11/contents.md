# 25-11. Docker를 이용한 MySQL 설치

> docker를 이용하여 MySQL을 설치하는 과정이다. docker를 이용하면 어느 환경에서건 작동하는 Database server를 구축할 수 있다.

`docker compose`는 여러 개의 도커 컨테이너를 실행시키는 툴이다. `docker compose`는 `YAML`형식의 문법을 사용하며 애플리케이션의 
서비스를 구성할 수 있다.

```yaml
version: '3'
services:
  mysql:
    image: mysql:latest
    restart: always
    container_name: mysql
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: <password>
      TZ: Asia/Seoul
    command:
      - --character-set-server=utf8mb4
      - --collation-server=utf8mb4_unicode_ci
    volumes:
      - <config_path>:/etc/mysql/conf.d
      - <data_path>:/var/lib/mysql
```

```shell
docker compose up -d
docker compose logs -f mysql
docker compose exec -it mysql /bin/bash
```

다음은 my.cnf 파일의 내용이다.

```shell
[mysqld]
character-set-server            = utf8mb4
collation-server                = utf8mb4_unicode_ci
secure-file-priv                = ""
```

도커를 재시작했을 때, `World-writable config file '/etc/my.cnf' is ignored` 라는 메시지가 나온다면 
`my.cnf` 권한을 맞춰줘야 한다.

```shell
chmod 755 /etc/mycnf
```
