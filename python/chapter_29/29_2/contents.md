# 싱글턴 패턴(Singleton Pattern)

싱글턴 패턴은 애플리케이션 개발에서 가장 많이 쓰이는 생성 디자인 패턴이다.

## 싱글턴 패턴의 개요

싱글턴 디자인 패턴은 글로벌하게 접근 가능한 단 한 개의 객체만을 허용하는 패턴이다. 따라서 싱글턴은 로깅이나 데이터베이스 관련 작업,
프린턴 스풀러 등의 애플리케이션에서 동일한 리소스에 대한 동시 요청의 충돌을 막기 위해 한 개의 인스턴스만 필요한 경우에 주로 쓰인다.   

예를 들어 데이터의 일관성 유지를 위해 DB에 작업을 수행하는 한 개의 데이터베이스 개겣가 필요한 경우 또는 여러 서비스의 로그를 한 개의
로그 파일에 순차적으로 동일한 로깅 객체를 사용해 남기는 경우에 적합한 패턴이다.

싱글턴 디자인 패턴의 목적인 다음과 같다.

+ 클래스에 대한 단일 객체 생성
+ 전역 객체 제공
+ 공유된 리소스에 대한 동시 접근 제어

생성자를 private로 선언하고 객체를 초기화하는 static 함수를 만들면 간단하게 싱글턴을 구현할 수 있다. 첫 호출에 객체가 생성되고 클래스는
동일한 객체를 계속 반환한다.

하지만 파이썬에서 생성자를 private로 선언할 수 없기 때문에 다른 방법이 필요하다. 

## 파이썬 싱글턴 패턴 구현

1. 한 개의 Singleton 클래스 인스턴스를 생성한다.
2. 이미 생성된 인스턴스가 있다면 재사용한다.

```python
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s1 = Singleton()
print('object created', s1)

s2 = Singleton()
print('object created', s2)
```

위 코드를 보면 __new__ 메서드(파이썬 전용 특수 생성자)를 오버라이드해 객체를 생성한다. __new__ 메서드는 s1객체가 이미 존재하는지 확인하고,
hasattr 메서드는 cls객체가 instance 속성을 가지고 있는지 확인한다.   
클래스 객체가 이미 존재하는지 확인하는 과정이다. s1 객체를 요청하면 hasattr()는 이미 객체가 생성됐음을 확인하고 해당 인스턴스를 반환한다.

> hasattr() 메서드
> > 해당 객체가 명시한 속성을 가지고 있는지 확인하는 파이썬 메서드

## 게으른 초기화(Lazy instantiation)

게으른 초기화는 싱글턴 패턴의 한 종류이다. 모듈을 임포트할 때 아직 필요하지 않은 시점에 실수로 객체를 미리 생성하는 경우가 있다.   
게으른 초기화는 인스턴스가 꼭 필요할 때 생성한다. 사용할 수 있는 리소스가 제한적인 상황일 때 객체가 꼭 필요한 시점에 생성하는 방식이다.   

다음 코드의 "s = Singleton()" 부분은 __init__ 함수를 실행하지만 객체는 생성하지 않는다. 대신 Singleton.getInstance() 부분에서 객체가
생성된다.

```python
class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('called... __init__ method')
        else:
            print('instance already created:', self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


# 클래스를 초기화했지만 객체는 생성하지 않음.
s1 = Singleton()
# 객체 생성
print('object created', Singleton.getInstance())
# 객체는 이미 생성됐음
s2 = Singleton()
```

## 모듈 싱글턴(Module Singleton)

파이썬의 임포트 방식 때문에 모든 모듈은 기본적으로 싱글턴이다. 파이썬의 작성 방식은 다음과 같다.
1. 파이썬 모듈이 임포트됐는지 확인한다.
2. 임포트됐다면 해당 객체를 반환하고 안 됐다면 임포트하고 인스턴스화 한다.
3. 모듈은 임포트와 동시에 초기화된다. 하지만 같은 모듈을 다시 임포트하면 초기화하지 않는다. 한 개의 객체만 유지하고 반환되는 싱글턴 방식이다.

## 모노스테이트 싱글턴 패턴(The Monostate Singleton Pattern)

모노스페이트 싱글턴 패턴은 이름 그대로 모든 객체가 같은 상태를 공유하는 패턴이다.   

다음의 코드를 보면 __dict__변수(파이썬 특수 변수)를 __shared_state 클래스 변수로 지정했다. 파이썬은 __dict__변수에 클래스 내 모든 객체의
상태를 저장한다. 모든 생성된 인스턴스의 상태를 __shared_state로 지정한다. 따라서 b1과 b2 인스턴스를 따로 생성해도 한 개의 객체만 만드는
싱글턴 패턴과는 달리 두 개의 객체가 생성된다. 하지만 객체의 상태를 나타내는 b1.__dict__와 b2.__dict__는 같다. 따라서 b1 객체의 x 값을 4로
설정하면 모든 객체가 공유하는 __dict__변수에 복사돼 b1의 x값도 1에서 4로 바뀐다.

```python
class Borg:
    __shared_state = {'1': '2'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state


b1 = Borg()
b2 = Borg()

b1.x = 5

# b1과 b2는 서로 다른 객체다.
print('Borg object "b1":', b1)
print('Borg object "b2":', b2)

print('-' * 100)

# b1과 b2는 상태를 공유한다.
print('object state "b1":', b1.__dict__)
print('object state "b2":', b2.__dict__)
```

다음과 같이 __new__메서드를 사용해 구현하는 방법도 있다.
> __new___ 메서드
> > 객체 인스턴스를 생성하는 메서드

```python
class Borg:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
```

## 싱글턴과 메타글래스

> 메타클래스(Metaclass)란?
> > 메타클래스는 클래스의 클래스이다. 즉 클래스는 자신의 메타클래스의 인스턴스이다.

메타클래스를 사용하면 이미 정의된 파이썬 클래스를 통해 새로운 형식의 클래스를 생성할 수 있다. 예를 들어 MyClass라는 객체가 있다면
MySuper라는 메타클래스를 생성해 MyClass의 행위를 재정의할 수 있다.

파이썬에서 모든 것은 객체다. "a = 5"라면 type(a)는 <type 'int'>를 반환한다. a는 int형 변수라는 뜻이다. 하지만 type(int)는 <type 'type'>을
반환한다. int의 메타클래스는 type 클래스라는 의미이다.

클래스는 메타클래스가 정의한다. class A 구문으로 클래스를 생성하면 파이썬은 A = type(name, bases, dict)를 실행한다.
+ name: 클래스명
+ base: 베이스 클래스
+ dict: 속성값

이미 정의된 메타클래스가 있다면 파이썬은 A = MetaKls(name, bases, dict)를 실행해 클래스를 생성한다.

```python
class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print('----- MyInt -----\n', args)
        return type.__call__(cls, *args, **kwargs)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


i = int(4, 5)
```

> __call__ 메서드
> > 이미 존재하는 클래스의 객체를 생성할 때 호출되는 파이썬의 특수 메서드

위의 코드처럼 int(4, 5)로 int 클래스를 생성하면 MyInt 메타클래스의 __call__ 메서드가 호출된다. 객체 생성을 메타클래스가 제어한다는 의미다.   
싱글턴 디자인 패턴과 같은 개념이다. 메타클래스가 클래스와 객체 생성을 제어한다면 싱글턴을 생성하는 용도로 사용할 수 있다는 의미다.

> 클래스 생성과 인스턴스화를 제어하기 위해 메타클래스는 __new__와 __init__메서드를 오버라이드한다

다음은 메타클래스를 사용해 싱글턴 패턴을 구현한 예제이다.

```python
class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()

print(logger1, logger2)
```

## 싱글턴 패턴 사용 사례

데이터베이스 기반 애플리케이션에서 싱글턴 패턴을 적용한 사례를 살펴보자. 데이터베이스에서 데이터를 읽고 쓰는 클라우드 서비스를 예로 들어보자.
이 클라우드 서비스에는 데이터베이스에 접근하는 여러 모듈이 있다. 각 UI에서 직접 DB 연산을 수행하는 API를 호출한다.

여러 서비스가 한 개의 DB를 공유하는 구조이다. 안정된 클라우드 서비스를 설계하려면 다음 사항들을 반드시 명심해야 한다.

+ 데이터베이스의 일관성을 보존해야 한다. 연산 간의 충돌이 없어야 한다.
+ 다수의 DB 연산을 처리하려면 메모리와 CPU를 효율적으로 사용해야 한다.

```python
import sqlite3


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db.sqlite3')
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()

print('Database objects DB1:', db1)
print('Database objects DB1:', db2)
```

위의 코드를 살펴보면 다음과 같다.

1. MetaSingleton이라는 메타클래스를 생성한다. __call__메서드를 사용해 싱글턴을 생성한다.
2. database 클래스는 MetaSingleton 메타클래스의 도움으로 싱글턴 역할을 한다. 단 한 개의 database 클래스 객체만 생성된다.
3. 앱이 DB 연산을 요청할 때마다 database 클래스를 생성하지만 내부적으로는 한 개의 객체만 생성된다. 따라서 데이터베이스의 동기화가 보장된다.
    리소스를 적게 사용해 메모리와 CPU 사용량을 최적화할 수 있다.

> 단일 어플리케이션 형태가 아닌 여러 어플리케이션이 같은 DB에 접속하는 상황을 생각해보자.   
> 이 경우 각 어플리케이션이 DB에 접근하는 싱글턴을 생성하기 때문에 싱글턴 패턴에 적합하지 않다.   
> DB 동기화가 어렵고 리소스 사용량이 많은 경우다. 싱글턴 패턴보다 연결 풀링(conanection pooling) 기법을 사용하는 것이 더 효율적이다.

## 싱글턴 패턴의 단점

싱글턴 패턴은 효율적이지만 단점도 있다. 싱글턴의 단일 전역 객체는 다음과 같은 문제점이 있다.

+ 전역 변수의 값이 실수로 변경된 것을 모르고 애플리케이션에서 사용될 수 있다.
+ 같은 객체에 대해 여러 참조자가 생길 수 있다. 싱글턴은 한 개의 객체만을 만들기 때문에 객체에 대해 여러 개의 참조가 생간다.
+ 전역 변수에 종속적인 모든 클래스 간 상호관계가 복잡해진다. 전역 변수 수정이 의도치 않게 다른 클래스에도 영향을 줄 수 있다.

## 정리

> * 애플리케이션을 개발할 때 스레드 풀과 캐시, 대화 상자, 레지스트리 설정 등 한 개의 객체만 필요한 경우가 많다. 이런 상황에서 여러 개의
    객체를 생성하는 것은 리소스 낭비다. 따라서 싱글턴 패턴이 적합하다.
> * 싱글턴은 글로벌 액세스 지점을 제공하는 단점이 거의 없는 검증된 패턴이다.
> * 싱글턴 패턴의 단점은 전역 변수가 의도치 않게 다른 클래스에게 영향을 줄 수 있으며 리소스를 많이 사용하는 구조가 될 수 있다.

싱글턴 패턴의 변형인 보그 또는 모노스테이트 패턴이 있다. 싱글턴과는 달리 보그는 상태를 공유하는 여러 개의 객체를 생성한다.