# 데코레이터 생성

파이썬은 데코레이터라는 기능을 제공한다. 데코레이터는 장식하다, 꾸미다라는 뜻의 decorate에 er(or)을 붙인  말인데 장식하는 도구 
정도로 설명할 수 있다.   
클래스에서 메서드를 만들 때 @staticmethod, @classmethod, @abstractmethod 등을 붙였는데, 이렇게 @로 시작하는 것들이 데코레이터이다. 
즉, 함수(메서드)를 장식한다고 해서 이런 이름이 붙었다.

```python
class Calc:
    @staticmethod       # 데코레이터
    def add(a, b):
        return a + b
```

## 데코레이터 만드는 방법

데코레이터는 함수를 장식한다고 했는데 도대체 어디에 사용하는 것일까? 데코레이터는 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 
사용한다. 예를 들어 함수의 시작과 끝을 출력하고 싶다면 다음과 같이 함수 시작, 끝부분에 print를 넣어주어야 한다.

```python
def hello():
    print('hello 함수 시작')
    print('hello')
    print('hello 함수 종료')

def world():
    print('world 함수 시작')
    print('world')
    print('world 함수 종료')

hello()
world()


# 결과
hello 함수 시작
hello
hello 함수 종료
world 함수 시작
world
world 함수 종료
```

만약 다른 함수도 시작과 끝을 출력하고 싶다면 함수를 만들 때마다 print를 넣어야 한다. 따라서 함수가 많아지면 매우 번거로워진다.
이런 경우에는 데코레이터를 활용하면 편리하다. 다음은 함수의 시작과 종료를 출력하는 데코레이터이다.

```python
def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 종료')
    return wrapper

def hello():
    print('hello')

def world():
    print('world')

trace_hello = trace(hello)
trace_hello()
trace_world = trace(world)
trace_world()


# 결과
hello 함수 시작
hello
hello 함수 종료
world 함수 시작
world
world 함수 종료
```

먼저 데코레이터 trace는 호출할 함수를 매개변수로 받는다. trace 함수 안에서는 호출할 함수를 감싸는 함수 wrapper를 만든다.   
  wrapper 함수에서는 함수의 시작을 알리는 문자열을 출력하고, trace에서 매개변수로 받는 func를 호출한다. 그 다음 함수의 종료를 
알리는 문자열을 출력한다. 마지막으로 wrapper 함수를 return하여 wrapper 함수 자체를 반환한다.    
즉, 함수 안에서 함수를 만들고 
반환하는 클로저이다.


## @으로 데코레이터 사용하는 방법

이제 @을 사용하여 좀 더 간편하게 데코레이터를 사용해보자. 다음과 같이 호출할 함수 위에 @데코레이터 형식으로 지정한다.

```python
@데코레이터
def 함수이름():
    code...
```

```python
def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 종료')
    return wrapper

@trace
def hello():
    print('hello')

@trace
def world():
    print('world')

hello()
world()


# 결과
hello 함수 시작
hello
hello 함수 종료
world 함수 시작
world
world 함수 종료
```

hello와 world 함수 위에 @trace를 붙인 뒤에 hello와 world 함수를 호출하면 끝이다. 이렇게 데코레이터는 함수를 감싸는 형태로 구성되어 
있다. 따라서 데코레이터는 기존 함수를 수정하지 않으면서 추가 기능을 구현할 때 사용한다.

## 데코레이터 여러 개 지정

함수에는 데코레이터를 여러 개 지정할 수 있다. 다음과 같이 함수 위에 데코레이터를 여러 줄로 지정해준다. 이때 데코레이터가 실행되는 
순서는 위에서 아래 순이다.

```python
@데코레이터
@데코레이터
def 함수이름():
    code...
```

```python
def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper

@decorator1
@decorator2
def hello():
    print('hello')

hello()


# 결과
decorator1
decorator2
hello
```
[chapter 14 목록으로...](../index.md)
