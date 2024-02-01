# 01-5. 컴포넌트 및 컨테이너 구획화(Namespace)

## 컴포넌트

Docker는 몇 개의 컴포넌트로 구성되어 있다. 핵심 기능이 되는 Docker Engine을 중심으로 컴포넌트를 조합하여 애플리케이션 실행 환경을 구축한다. 
Docker는 명령줄에서 조작하는 것(CLI)이 중심이다.

### Docker Engine (Docker의 핵심 기능)
Docker 이미지를 생성하고 컨테이너를 기동시키기 위한 Docker의 핵심 기능이다. Docker 명령의 실행이나 Dockerfile에 의한 이미지도 생성한다.

### Docker Registry (이미지 공개 및 공유)
컨테이너의 바탕이 되는 Docker 이미지를 공개 및 공유하기 위한 레지스트리 기능이다. Docker의 공식 레지스트리 서비스인 Docker Hub도 이 
Docker Registry 를 사용하고 있다.

### Docker Compose (컨테이너 일원 관리)
여러 개의 컨테이너 구성 정보를 코드로 정의하고, 명령을 실행함으로써 애플리케이션의 실행 환경을 구성하는 컨테이너들을 일원 관리하기 위한 툴이다.

### Docker Machine (Docker 실행 환경 구축)
로컬 호스트용인 VirtualBox를 비롯하여 Amazon Web Services EC2나 Microsoft Azure와 같은 클라우드 환경에 Docker의 실행 환경을 명령으로 
자동 생성하기 위한 툴이다.

### Docker Swarm (클러스터 관리)
Docker Swarm은 여러 Docker 호스트를 클러스터화하기 위한 툴이다. Docker Swarm에서는 클러스터를 관리하거나 API를 제공하는 역할은 Manager가, 
Docker 컨테이너를 실행하는 역할은 Node가 담당한다. 또한 오픈소스인 Kubernetes도 이용할 수 있다.

---

### Docker를 둘러싼 업체/OSS의 동향

Docker는 Google이나 Amazon과 같은 클라우드 업체를 비롯하여 Red Hat, Microsoft, IBM 등과 같은 시스템 개발을 지지해 온 대부분의 대형 업체 
및 널리 이용되고 있는 오픈소스 등이 지원하고 있다. 다양한 조직이나 시스템과 연계하여 사용할 수 있는 소프트웨어의 특성을 상호운용성(Interoperability)
이라고 한다.

또한 주요 퍼블릭 클라우드 업체는 컨테이너 실행 환경의 풀 매니지드 서비스를 제공한다. 풍부한 서비스를 제공하고 업무 시스템에서의 기동 실적이 많은 
클라우드 서비스인 Amazon Web Services(AWS)의 경우 'Amazon EC2 Container Service'로 Docker 실행 환경의 매니지드 서비스를 제공하고 있다.    
또한 Microsoft의 Azure가 제공하는 'Azure Container Service'는 컨테이너 오케스트레이션 툴을 선택할 수 있는 것이 특징이다. 그리고 Google은 
YouTube 등을 제공하는 자사 내 기반은 모두 컨테이너 기술을 사용하여 구축하고 있다. 

그 노하우를 살려서 오픈소스인 Kubernetes를 손쉽게 이용할 수 있는 매니지드 서비스가 'Google Kubernetes Engine'이다.
Docker는 업체뿐만 아니라 대부분의 오픈소스와의 연계도 간단하다. 오픈소스의 지속적 인티그레이션 툴인 'Jerkins'와 연계하여 테스트를 자동화할 수도 있다. 
또한 애플리케이션 개발자에게는 익순한 'GitHub'와 연계하여 GitHub 상에서 소스가 관리되는 Dockerfile을 Docker Hub와 연계하여 자동으로 빌드하고 
Docker 컨테이너의 바탕이 되는 Docker 이미지를 생성할 수도 있다.

## 컨테이너 구획화(Namespace)

Docker는 컨테이너라는 독립된 환경을 만들고, 그 컨테이너를 구획하하여 애플리케이션의 실행 환경을 만든다. 이 컨테이너를 구획하는 기술은 Linux 커널의 
namespace라는 기능을 사용하고 있다.

namespace는 한글로 '이름공간' 이라고 하는데, 이름공간이란 한 덩어리의 데이터에 이름을 붙여 분할함으로써 충돌 가능성을 줄이고, 쉽게 참조할 수 있게 
하는 개념이다. 이름과 연결된 실체는 그 이름이 어떤 이름공간에 속해 있는지 고유하게 정해진다. 그래서 이름공간이 다르면 동일한 이름이라도 다른 실체로 처리된다.   
Linux 커널의 namespace 기능은 Linux의 오브젝트에 이름을 붙임으로써 다음과 같은 6개의 독립된 환경을 구축할 수 있다.

+ ### PID namespace
  + PID란 Linux에서 각 프로세스에 할당된 고유한 ID를 말한다. PID namespace는 PID와 프로세스를 격리시킨다. namespace가 다른 프로세스끼리는 
서로 액세스할 수 없다.
 
+ ### Network namespace
  + Network namespace는 네트워크 디바이스, IP 주소, 포트 번호, 라우팅 테이블, 필터링 테이블 등과 같은 네트워크 리소스를 격리된 namespace마다 
독립적으로 가질 수 있다. 이 기능을 사용하면 호스트 OS 상에서 사용 중인 포트가 있더라도 컨테이너 안에서 동일한 번호의 포트를 사용할 수 있다.

+ ### UID namespace
  + UID namespace는 UID(사용자 ID), GID(그룹 ID)를 namespace별로 독립적으로 가질 수 있다. namespace 안과 호스트 OS상의 UID/GID가 
서로 연결되어 이름공간 안과 밖에서 서로 다른 UID/GID를 가질 수 있다. 예를 들어 namespace 안에서는 UID/GID가 0인 root 사용자를, 호스트 OS 
상에서는 일반 사용자로서 취급할 수 있다. 이것은 namespace안의 관리자 계정은 호스트 OS에 대해서는 관리 권한을 일절 갖지 않는다는 것을 의미하므로 
보안이 뛰어난 환경으로 격리시킬 수 있다.

+ ### Mount namespace
  + Linux에서 파일 시스템을 사용하기 위해서는 마운트가 필요하다. 마운트란 컴퓨터에 연결된 기기나 기억장치를 OS에 인식시켜 이용 가능한 상태로 만드는 
것을 말한다. MOUNT namespace는 마운트 조작을 하면 namespace안에 격리된 파일 시스템 트리를 만든다. 다른 namespace 가능과 마찬가지로 
namespace 안에서 수행한 마운트는 호스트 OS나 다른 namespace에서는 액세스할 수 없게 되어 있다.

+ ### UTS namespace
  + UTS namespace는 namespace 별로 호스트명이나 도메인명을 독자적으로 가질 수 있다.

+ ### IPC namespace
  + IPC namespace는 프로세스 간의 통신(IPC) 오브젝트를 namespace별로 독립적으로 가질 수 있다. IPC는 System V 프로세스 간의 통신 오브젝트라고 
하는 공유 메모리나 세마포어/메시지 큐를 말한다. 세마포어란 프로세스가 요구하는 자원 관리에 이용되는 배타제어 장치이며, 메시지 큐란 여러 프로세스간에서 
비동기 통신을 할 때 사용되는 큐잉 장치이다. Docker는 이러한 namespace 장치를 사용하여 호스트 상에서 컨테이너를 가상적으로 격리시킨다. 
Docker를 사용할 때 특별히 의식할 필요는 없지만 Docker의 구조를 이해해 두는 것은 중요하다.