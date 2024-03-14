# 30-4. Observer Pattern

### _옵서버 패턴은 객체 간의 상호 관계를 관리하고 일대다(1:N) 관계를 형성한다._

---

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
        print(type(self).__name__, "args: ", args, "from ", subject)


class Observer2:
    def __init__(self, subject: Subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, "args: ", args, "from ", subject)


if __name__ == "__main__":
    sub = Subject()
    ob1 = Observer1(sub)
    ob2 = Observer2(sub)
    sub.notify_all("notification")
```

옵서버 패턴 구성원의 각 역할은 다음과 같다.

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

뉴스 에이전시를 옵서버 패턴으로 구현해보자. 뉴스 에이전시는 일반적으로 여러 곳에서 뉴스를 모아 구독자에게 전달한다. 이 경우의 데자인 요소를 생각해보자.
뉴스 에이전시는 실시간 뉴스를 신속하게 구독자에게 전달해야 한다. 기술이 발전하면서 구독자는 단순히 신문이 아닌 이메일과 문자, 음성 메시지 등 다양한 
방식으로 뉴스를 전달받는다. 따라서 추후에 새로운 형태의 매체도 지원할 수 있도록 설계해야 한다.

뉴스 게시자인 서브젝트부터 구현한다.

+ 서브젝트의 행동은 `NewsPublisher` 클래스에 구현한다.
+ `NewsPublisher`는 구독자가 구현할 인터페이스를 제공한다.
+ `Observer`는 `attach()` 메서드를 통해 자신을 `NewsPublisher`에 등록하고 `detach()` 메서드로 등록을 취소한다.
+ `subscribers()`는 `Subject`에 등록된 구독자 목록을 반환한다.
+ `notify_subscriber()`는 `NewPublisher`에 등록된 모든 구독자에게 알림을 보낸다.
+ 뉴스 게시자는 `add_news()` 메서드로 새로운 뉴스를 등록하고 `get_news()`로 최신 뉴스를 확인한 뒤 `Observer`에 전달한다.

### NewsPublisher 클래스 정의

```python
class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latest_news = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
        self.__latest_news = news

    def get_news(self):
        return "news: ", self.__latest_news
```

### Observer 인터페이스 작성

+ `Subscriber`는 `Observer`를 나타낸다. 모든 `ConcreteObserver`의 추상 기본 클래스이다.
+ `Subscriber`에는 `ConcreteObserver`가 구현해야 하는 `update()` 메서드가 있다.
+ `ConcreteObserver`는 `update()`를 구현해 `Subject(NewsPublisher)`로부터 새로운 뉴스 알림을 받는다.

#### Subscriber 추상 클래스 구현부

```python
from abc import ABCMeta, abstractmethod


class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self): ...
```

ConcreteObserver 클래스의 역할은 다음과 같다.

+ `EmailSubscriber`와 `SMSSubscriber`는 `Subscriber 인터페이스`를 구현하는 옵서버다.
+ `AnyOtherObserver`는 Observer와 Subject의 느슨한 관계를 나타내는 또 다른 옵서버다.
+ 각 `ConcreteObserver`의 `__init__()` 메서드는 `attach()` 메서드를 통해 자신을 `NewsPublisher`에 등록한다.
+ `NewsPublisher`는 내부적으로 `ConcreteObserver`의 `update()` 메서드를 호출해 새로운 뉴스를 알린다.

#### SMSSubscriber 클래스 구현부

```python
class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        super().__init__()
        self.publisher: NewsPublisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        super().__init__()
        self.publisher: NewsPublisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        super().__init__()
        self.publisher: NewsPublisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())
```

#### NewPublisher와 SMSSubscriber 클래스의 동작 방법

+ 클라이언트는 ConcreteObserver가 사용할 NewsPublisher 객체를 생성한다.
+ SMSSubscriber와 EmailSubscriber, AnyOtherSubscriber 클래스는 `publisher` 객체를 통해 초기화된다.
+ `ConcreteObserver` 클래스의 `__init()__`은 내부적으로 `NewsPublisher`의 `attach()` 메소드를 호출해 자신을 등록한다.
+ `Subject`에 등록된 모든 구독자(ConcreteObserver)를 출력한다.
+ `NewPublisher(news_publisher)` 객체는 `add_news()` 메서드를 통해 뉴스를 등록한다.
+ `NewsPublisher` 클래스의 `notify_subscribers()` 메서드는 모든 구독자에게 새로운 뉴스를 전달한다. `notify_subscribers()`는 `ConcreteObserver`가
구현한 `update()` 메서드를 내부적으로 호출한다.
+ `NewsPublisher`에는 구독자를 목록에서 제거하는 `detach()` 메서드가 있다.

#### Subject와 Observer의 상호 작용 구현 코드

```python
news_publisher = NewsPublisher()
for subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
    subscribers(news_publisher)

print("\nSubscribers:", news_publisher.subscribers())

news_publisher.add_news("Hello World!")
news_publisher.notify_subscribers()

print("\nDetached:", type(news_publisher.detach()).__name__)
print("\nSubscribers:", news_publisher.subscribers())

news_publisher.add_news("My second news!")
news_publisher.notify_subscribers()
```

## 옵서버 패턴 메서드

Subject의 변경 사항을 Observer에 알리는 방법에는 `Push`와 `Pull` 두 가지 모델이 있다.

### Pull Model

풀 모델에서 Observer는 다음과 같은 역할을 한다.
+ `Subject`는 변경 사항이 있음을 등록된 Observer에 `브로드캐스트(broadcast)`한다.
+ `Observer`는 직접 게시자에게 변경 사항을 요청하고 끌어와야(pull) 한다.
+ `Pull Model`은 Subject가 Observer에 알리는 단계와 Observer가 Subject로부터 필요한 데이터를 받아오는 두 단계가 필요하므로 비효율적이다.

### Push Model

푸시 모델에서 Subject의 역할은 다음과 같다.
+ `Pull Model`과 달리 Subject가 Observer에 데이터를 보낸다.
+ `Subject`는 Observer가 필요로 하지 않는 데이터까지 보낼 수 있다. 따라서 쓸데없이 많은 양의 데이터를 전송해 응답 시간이 늦어질 수 있다.
+ 성능을 위해 `Subject`는 오직 필요한 데이터만 보내야 한다.

## 느슨한 결합과 옵서버 패턴

`느슨한 결합(loose coupling)`은 중요한 소프트웨어 어플리케이션 `설계 원칙`이다. 상호 작용하는 객체 간의 관계를 최대한 느슨하게 구성하는 것이 목적이다.
여기서 `결합`이란 객체가 상호 작용하는 다른 객체에 대해 알고 있는 정도로 의미한다.

느슨한 결합을 추구한 설계는 객체 간의 `의존도`를 줄여 유연한 객체지향 시스템을 만들 수 있다.

__느슨한 결합의 효과__ 는 다음과 같다.

+ 한 부분에 대한 수정이 예기치 않게 다른 부분까지 영향을 끼치는 위험을 줄인다.
+ 테스트와 유지 보수 및 장애 처리가 쉽다.
+ 시스템을 쉽게 여러 부분으로 분리할 수 있다.

옵서버 패턴은 Subject와 Observer의 느슨한 결합을 추구한다.

+ Subject는 정확히 Observer가 어떤 인터페이스를 구현하는지 모른다. ConcreteObserver의 존재를 모른다.
+ 언제든지 새로운 Observer를 추가할 수 있다.
+ 새로운 Observer를 추가해도 Subject를 수정할 필요가 없다. 
  + 위의 예제 코드에서 Subject를 수정하지 않고도 `AnyOtherObserver`를 추가/제거했듯이.
+ Subject 또는 Observer는 독립적이다. Observer는 필요 시, 어디에서도 재사용될 수 있다.
+ Subject 또는 Observer에 대한 수정이 서로에게 아무런 영향을 주지 않는다. 완전 독립성 또는 느슨한 결합 덕분에 걱정 없이 수정할 수 있다.

## 옵서버 패턴의 장단점

+ __옵서버 패턴의 장점__
  + 객체 간의 느슨한 결합 원칙을 따른다.
  + Subject 또는 Observer 클래스를 수정하지 않고 객체 간 자유롭게 데이터를 주고받을 수 있다.
  + 새로운 Observer를 언제든지 추가/제거할 수 있다.
+ __옵서버 패턴의 단점__
  + ConcreteObserver는 상속을 통해 Observer 인터페이스를 구현한다. 컴포지션에 대한 선택권이 없다.
  + 제대로 구현되지 않은 Observer 클래스는 복잡도를 높이고 성능 저하의 원인이 될 수 있다.
  + 애플리케이션에서 알림(Notification) 기능은 간혹 신뢰할 수 없으며 레이스 상태(Race Condition) 또는 비일관성을 초래할 수 있다.

---

## 추가 정리

### 여러 개의 Subject와 Observer를 정의해도 되는가?

다수의 Subject와 Observer가 필요한 경우가 있다. Observer는 정확히 어떤 Subject가 변경됐는지 알아야 한다.

### 누가 변경 사항을 알려야 하는가?

옵서버 패턴에는 `push`와 `pull` 모델이 있다. 보통 Subject가 변경 사항을 알리지만 필요에 따라 Observer가 직접 요청하는 경우도 있다. 하지만 
요청 주기가 너무 짧으면 성능 저하의 요인이 될 수 있다. Subject에 대한 변경이 잦지 않은 경우 특히 조심해야 한다.

### Subject 또는 Observer를 다른 목적으로 사용해도 되는가?

물론 사용하여도 된다. 느슨한 결합 원칙을 따르는 옵서버 패턴에는 Subject와 Observer는 `독립적`이다.
