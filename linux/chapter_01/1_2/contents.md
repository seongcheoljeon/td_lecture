# 01-2. 기본 명령어

## ls (list)

## cp (copy)

## mv (move)

## rm (remove)

## cat

## curl (client url)

curl은 "client url"이란 의미로 클라이언트에서 url을 사용해서 서버와 데이터를 송수신하는 명령어 툴이다.   
다양한 OS 환경에서 HTTP, HTTPS, SMTP, FTP, SMTP 등 다양한 프로토콜을 지원하여 통신 환경에서 자주 쓰인다.

### curl 사용법

> curl [OPTIONS] [URL]

curl의 OPTIONS은 short형인 '-' 와 long형인 '--' 를 제공한다. 가장 기본적인 사용법은 옵션 입력 후에 URL을 입력한다.

|short| long                 | 설명                                                                                 |
|:---|:---------------------|:-----------------------------------------------------------------------------------|
|-k| --insecure           | HTTPS URL 접속 시 SSL 인증서 검사 없이 연결                                                    |
|-i| --head               | HTTP 응답 헤더 표시                                                                      |
|-d| --data               | POST 요청이나 JSON 방식과 같이 request body에 데이터를 담을 때 사용                                   |
|-o| --output             | -o [파일명] 을 사용하면 출력 결과를 파일로 저장                                                      |
|-O| --remote-name        | 파일 저장 시 remote의 file 이름으로 저장                                                       |
|-s| --silent             | 진행 내역이나 메시지 등을 출력하지 않는다.                                                           |
|-X| --request            | request에 사용할 메서드(GET, POST, PUT, DELETE 등)를 지정                                     |
|-v| --verbose            | 동작하는 과정 출력                                                                         |
|-A| --user-agent         | 특정 브라우저인 것처럼 동작하기 위한 설정                                                            |
|-H| --header             | 요청할 헤더 설정                                                                          |
|-L| --location           | 서버에서 HTTP (301, 302 등 리다이렉트) 응답이 오면 리다이렉트.<br/>URL로 따라감 (--max-redirs [횟수])로 지정 가능 |
|-D| --dump-header<file>  | 파일에 응답 헤더 기록                                                                       |
|-u| --user               | 사용자 ID / Password 입력                                                               |
|-f| --fail               | 오류 발생 시, 출력 없이 실패                                                                  |
|-T| --upload-file        | 로컬 파일을 서버로 전송                                                                      |
|-C| --continue-at        | 중지된 다운로드 재시작                                                                       |
|-J| --remote-header-name | 응답 헤더에 있는 파일 이름으로 파일 저장 (curl 7.20 이상)                                             |
|-I| --head               | 응답 헤더만 출력                                                                          |

```shell
# URL 요청에 대한 응답 값 출력
curl https://google.com

# URL 요청에 대한 응답을 info.txt라는 파일에 저장
# -O의 경우 서버에 해당하는 파일명을 갖고 오기 때문에 해당 파일명이 존재하지 않으면, 404 응답이 파일명으로 저장된다.
curl -o info.txt google.com
curl -O google.com/info.txt

# POST 방식으로 JSON 데이터 요청 및 타임아웃 설정
curl --connect-timeout 15 -i \
-H 'Content-Type: application/json' \
-d '{ "todo" : { "id" : 1, "name" : "C++ STL" }' \
-X POST http://127.0.0.1:8000/todo

# HTTP POST에서 파일을 전송할 경우 파일명 앞에 @를 붙여준다.
curl --data-binary -d @data.txt http://127.0.0.1:8080

# FTP 방식으로 통신 
#   -# : 진행률을 #으로 한줄 표시
#   --silent : 진행 과정 비활성화
#   [1-20] : 숫자 시퀀스라면 여러 파일 전송
#   --limit-rate : 전송 속도 제한
curl -# -O ftp://example.com/download.zip
curl --silent ftp://example.com/download.zip
curl ftp://example.com/download[1-20].jpeg
curl --limit-rate 1000K -O ftp://example.com/download.zip

# 사용자 정보 입력 및 프록시가 필요한 경우 사용
curl -u [user]:[password] -x [proxy name]:[port] [URL...]

# SMTP 방식으로 메일 전송 
curl -url [SMTP URL] \
-mail-from [sender_mail] \
-mail-rcpt [receiver_mail] \
-n \
-ssl-reqd \
-u {email}:{password} \
-T [메일 텍스트 파일]

# bearer token을 사용할 경우 -H 옵션 뒤에 토큰을 추가하여 전송
curl -v -L -X POST \
-H 'Accept: application/json' \
-H 'Authorization: Bearer [token]' \
'http://localhost:8080'

# 쿠키 정보를 cookie.txt 파일에 저장
curl -I -c cookie.txt http://localhost:8080

# 쿠키 값을 지정하여 서버에 전송
curl -b "SESSIONID=234wasdfasdf234" http://localhost:8080

# HTTP GET 방식의 응답
curl -X 'GET' 'http://127.0.0.1:8000/todo' -H 'accept: application/json'

# HTTP POST 방식의 데이터 전달
curl -X 'POST' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
    "id": 1,
    "item": "독서하기!"
}'
```

