# 30-4. Observer Pattern

옵서버 패턴에서 `객체(서브젝트)`는 `자식(옵서버)`의 목록을 유지하며 서브젝트가 옵서버에 정의된 메서드를 호출할 때마다 옵서버에 이를 알린다.
분산형 애플리케이션에는 사용자가 요청한 작업을 수행하는 다수의 서비스가 엮여 있다. 각 서비스가 수행하는 다양한 연산은 객체 상태에 직접적인 영향을 받는다.

유저 서비스가 사용자 요청을 처리하는 웹 사이트의 사용자 가입 절차를 예로 들어보자. 웹 사이트에는 사용자의 계정 상태를 확인하고 이메일을 발송하는 이메일
서비스가 있다. 사용자가 가입을 하면 유지 서비스는 이메일 서비스의 메소드를 호출해 계정 인증 이메일을 발송한다. 계정은 인증됐지만 포인트가 부족한 경우 
사용자에게 이를 알리는 이메일을 발송한다.

애플리케이션을 구성하는 여러 서비스를 관리하는 코어 서비스는 옵서버의 상태를 모니터링하는 서브젝트다. 옵서버는 서브젝트의 상태에 따라 자신의 객체 상태를 
변경하거나 필요한 연산을 수행한다. __이처럼 종속된 서비스가 코어 서비스의 `상태`를 `참고하는 구조`에는 `옵서버 디자인 패턴`이 `적합`하다.__

> __브로드캐스트나 게시(Publish)/구독(Subscribe) 시스템에서 옵서버 디자인 패턴이 자주 사용된다.__

인스타그램으로 예를 들어보자. 만약 내가 인싸라면 나의 인스타그램 계정을 팔로잉하는 사람들이 많을 것이다. 내가 새로운 글을 올리거나 글이 수정되면
구독자들은 알림을 받는다. 알림 방식 중 하나는 이메일이다. 이 상황을 옵서버 패턴으로 구현한다면 인스타그램은 구독자 또는 옵서버의 목록을 
유지하는 `서브젝트`다. 인스타그램에 새로운 글이 등록되면 이메일 또는 각 옵서버가 선택한 방식으로 알림을 보낸다.

옵서버 패턴의 목적은 다음과 같다.

+ 객체 간 `일대다(1:N)` 관계를 형성하고 객체의 상태를 다른 종속 객체에 자동으로 알린다.
+ 서브젝트의 핵심 부분을 캡슐화한다.

옵서버 패턴은 다음과 같은 상황에 적합하다.

+ 분산 시스템의 이벤트 서비스를 구현할 때
+ 뉴스 에이전시 프레임워크
+ 주식 시장 모델

```python
class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    def __init__(self, subject: Subject):
        subject.register(self)

    def notify(self, subject: Subject, *args):
        print(type(self).__name__, ":: got", args, "from ", subject)


class Observer2:
    def __init__(self, subject: Subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ":: got", args, "from ", subject)


if __name__ == "__main__":
    sub = Subject()
    ob1 = Observer1(sub)
    ob2 = Observer2(sub)
    sub.notify_all("notification")
```

옵서버 패턴으 기쉉원의 각 역할은 다음과 같다.

+ __서브젝트(Subject)__
  + Subject는 Observer를 관리한다. 
  + Observer는 Subject 클래스의 register()와 deregister() 메서드를 호출해 자신을 등록한다. 
  + Subject는 여러 옵서버를 관리한다.
+ __옵서버(Observer)__
  + 서브젝트를 감시하는 객체를 위한 인터페이스를 제공한다.
  + 서브젝트의 상태를 알 수 있도록 ConcreteObserver가 구현해야 하는 메서드를 정의한다.
+ __ConcreteObserver__
  + Subject의 상태를 저장한다.
  + 서브젝트에 대한 정보와 실제 상태를 일관되게 유지하기 위해 Observer 인터페이스를 구현한다.

순서는 간단하다. ConcreteObserver는 Observer 인터페이스를 구현해 자신을 Subject에 등록한다. 상태 변화가 있을 때마다 Subject는 Observer의
알림 메서드를 통해 모든 ConcreteObserver에 알린다.

## 옵서버 패턴 사용 사례
