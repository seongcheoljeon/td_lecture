# 클래스 기반의 데코레이터

클래스를 활용할 때는 인스턴스를 함수처럼 호출하게 해주는 __call__ 메서드를 구현해야 한다. 다음은 함수의 시작과 종료를 출력하는 
데코레이터이다.

```python
class Trace:
    # 호출할 함수를 인스턴스의 초깃값으로 받음
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print(self.func.__name__, '함수 시작')
        self.func()
        print(self.func.__name__, '함수 종료')

@Trace
def hello():
    print('hello')

hello()


# 결과
hello 함수 시작
hello
hello 함수 종료
```

클래스로 데코레이터를 만들 때는 먼저 __init__ 메서드를 만들고 호출할 함수를 초깃값으로 받는다. 그리고 매개변수로 받은 함수를 속성으로 
저장한다.   
이제 인스턴스를 호출할 수 있도록 __call__ 메서드를 만든다. __call__ 메서드에서는 함수의 시작을 알리는 문자열을 출력하고, 속성 func에 
저장된 함수를 호출한다. 그 다음 함수의 종료를 알리는 문자열을 출력한다.   
데코레이터를 사용하는 방법은 클로저 형태의 데코레이터와 같다. 호출할 함수 뒤에 @을 붙이고 데코레이터를 지정하면 된다.   
참고로 클래스로 만든 데코레이터는 @을 지정하지 않고, 데코레이터의 반환값을 호출하는 방식으로도 사용할 수 있다. 다음과 같이 데코레이터에 
호출할 함수를 넣어서 인스턴스를 생성한 뒤 인스턴스를 호출해주면 된다. 즉, 클래스에 __call__ 메서드를 정의했으므로 함수처럼 ()를 붙여서 
호출할 수 있다.

```python
def hello():
    print('hello')
    
trace_hello = Trace(hello)
trace_hello()    # 인스턴스를 호출. __call__ 메서드가 호출됨.
```

## 클래스로 매개변수와 반환값을 처리하는 데코레이터

클래스로 만든 데코레이터도 매개변수와 반환값을 처리할 수 있다. 다음은 함수의 매개변수를 출력하는 데코레이터이다.

```python
class Trace:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        r = self.func(*args, **kwargs)
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
        return r

@Trace
def add(a, b):
    return a + b

print(add(10, 20))
print(add(a=10, b=20))


# 결과
add(args=(10, 20), kwargs={}) -> 30
30
add(args=(), kwargs={'a': 10, 'b': 20}) -> 30
30
```

클래스로 매개변수와 반한값을 처리하는 데코레이터를 만들 때는 __call__ 메서드에 매개변수를 지정하고, self.func에 매개변수를 넣어서 
호출한 뒤에 반환값을 반환해주면 된다.    
물론 가변 인수를 사용하지 않고, 고정된 매개변수를 사용할 때는 def __call__(self, a, b) 
처럼 만들어도 된다.

## 클래스로 매개변수가 있는 데코레이터 만드는 방법

매개변수가 있는 데코레이터를 만들어보자. 다음은 함수의 반환값이 특정 수의 배수인지 확인하는 데코레이터이다.

```python
import functools

class IsMultiple:
    def __init__(self, x):
        # 데코레이터가 사용할 매개변수를 초깃값으로 받음
        self.__x = x

    # 호출할 함수를 매개변수로 받음
    def __call__(self, func):
        # 호출할 함수의 매개변수와 똑같이 지정
        functools.wraps(func)
        def wrapper(a, b):
            r = func(a, b)
            if r % self.__x == 0:
                print('{0}의 반환값은 {1}의 배수이다.'.format(func.__name__, self.__x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아니다.'.format(func.__name__, self.__x))
            return r
        return wrapper

@IsMultiple(3)
def add(a, b):
    return a + b

print(add(10, 20))
print(add(2, 5))


# 결과
add의 반환값은 3의 배수이다.
30
add의 반환값은 3의 배수가 아니다.
7
```

먼저 __init__ 메서드에서 데코레이터가 사용할 매개변수를 초깃값으로 받는다. 그리고 매개변수를 __call__ 메서드에서 사용할 수 있도록 
속성에 저장한다.    
지금까지 __init__ 에서 호출할 함수를 매개변수로 받았는데 여기서는 데코레이터가 사용할 매개변수를 받는다는 점을 기억하자.   
데코레이터는 기존 함수를 수정하지 않으면서 추가 기능을 구현할 때 사용한다는 점을 기억하면 된다. 보통 데코레이터는 프로그램의 버그를 
찾는 디버깅, 함수의 성능 측정, 함수 실행 전에 데이터 확인 등에 활용한다.

```python
def type_check(type_a, type_b):
    def real_decorator(func):
        def wrapper(a, b):
            if isinstance(a, type_a) and isinstance(b, type_b):
                return func(a, b)
            else:
                raise RuntimeError('자료형이 올바르지 않습니다.')
        return wrapper
    return real_decorator
```

[chapter 14 목록으로...](../index.md)