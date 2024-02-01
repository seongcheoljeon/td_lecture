# 02-1. Docker에서 'Hello World!'

설치한 Docker가 올바르게 작동하는지를 확인하기 위해 Docker 컨테이너를 작성하고 콘솔상에 "Hello World" 라는 문자를 출력해보자.
Docker 컨테이너를 작성 및 실행할 때는 docker container run 명령을 사용한다. 이 명령의 구문은 다음과 같다.

```docker
docker container run <Docker 이미지명> <실행할 명령>
```

1. docker container run : 컨테이너를 작성 및 실행
2. <Docker 이미지명> : 바탕이 되는 Docker 이미지
3. <실행할 명령> : 컨테이너 안에서 실행할 명령

예를 들어 Ubuntu의 이미지를 바탕으로 Docker 컨테이너를 작성 및 실행한 후 작성한 컨테이너 안에서 "Hello World" 를 표시하고 싶을 때는 다음의 
명령을 실행한다.

```docker
docker container run ubuntu:latest /bin/echo 'Hello World!'
```

위의 명령을 실행하면 Docker 컨테이너의 바탕이 되는 Ubuntu의 Docker 이미지가 로컬 환경에 있는지 확인한다. 만일 로컬 환경에 없다면 Docker 
리포지토리에서 Docker 이미지를 다운로드한다.

실행 결과 중에 있는 'ubuntu:latest'는 Ubuntu의 최신 버전의 이미지를 취득한다는 뜻이다. 다운로드가 완료되면 컨테이너가 시작되고, Linux의 echo 
명령이 실행된다.

또한 첫 번째는 Docker 이미지의 다운로드에 시간이 소요되지만, 두 번째부터는 로컬 환경에 다운로드된 Docker 이미지를 바탕으로 Docker 컨테이너를 
시작한다. 해당 명령을 다시 한번 실행해보면 처음보다 빠른 속도로 컨테이너가 시작되는 것을 알 수 있다.

> 로컬 환경에 다운로드된 Docker 이미지를 로컬 캐시라고 한다.

## Docker 버전 확인 (docker version)

설치한 Docker 버전을 확인하려면 docker version 명령을 사용한다. docker version 명령을 실행하면 Docker의 버전이나 Go 언어의 버전, OS, 
아키텍처를 확인할 수 있다.

```yaml
Client: Docker Engine - Community
 Version:           19.03.13
 API version:       1.40
 Go version:        go1.13.15
 Git commit:        4534c46d9d
 Built:             Wed Sep 16 17:02:52 2020
 OS/Arch:           linux/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          19.03.13
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.13.15
  Git commit:       4634c46d9d
  Built:            Wed Sep 16 17:01:20 2020
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.3.7
  GitCommit:        8fba4e557d01810a393d5d25a3655dc101981175
 runc:
  Version:          1.0.0-rc10
  GitCommit:        dc9255a3303feef5b3559f4323d9beb36df0a9dd
 docker-init:
  Version:          0.18.0
  GitCommit:        fec3363
```

> Docker는 클라이언트/서버 아키텍처를 채택하고 있어서 Docker 클라이언트와 Docker 서버가 Remote API를 경유하여 연결되어 있다. 따라서 docker 
명령은 서버로 보내져 처리된다.

## Docker 실행 환경 확인 (docker system info)

docker system info 명령을 실행하면 Docker 실행 환경의 상세 설정이 표시된다.

```yaml
Client:
 Debug Mode: false

Server:
 Containers: 11    <--- 컨테이너 개수
  Running: 0
  Paused: 0
  Stopped: 11
 Images: 2
 Server Version: 19.03.13    <--- Docker 버전
 Storage Driver: overlay2    <--- 스토리지 드라이버 종류
  Backing Filesystem: extfs
  Supports d_type: true
  Native Overlay Diff: true
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
 Swarm: inactive
 Runtimes: runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 8fba4e9a7d05325a393d5d25a3621dc101981175
 runc version: dc920812653feef5b3839f4323d9beb36df0a9dd
 init version: fec3532
 Security Options:
  apparmor
  seccomp
   Profile: default
 Kernel Version: 5.4.0-54-generic
 Operating System: Ubuntu 20.04.1 LTS
 OSType: linux    <--- OS 종류
 Architecture: x86_64    <--- 아키텍처
 CPUs: 12
 Total Memory: 62.73GiB
 Name: scii-ubuntu
 ID: K5TA:DEP8:90AB:3KWA:Q5AB:XSD3:DBAT:HKLO:LZ90:WOIU:GZTY:5Y5L
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Registry: https://index.docker.io/v1/
 Labels:
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
 Live Restore Enabled: false
```

## Docker 디스크 이용 상황 (docker system df)

docker system df 명령을 실행하면 Docker가 사용하고 있는 디스크의 이용 상황이 표시된다.

```yaml
TYPE                TOTAL               ACTIVE              SIZE                RECLAIMABLE
Images              2                   2                   72.89MB             0B (0%)
Containers          11                  0                   0B                  0B
Local Volumes       0                   0                   0B                  0B
Build Cache         0                   0                   0B                  0B
```

상세 내용을 확인할 때는 -v 옵션을 지정한다.
