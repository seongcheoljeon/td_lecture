# 매개변수와 반환값이 존재하는 데코레이터

매개변수와 반환값을 처리하는 데코레이터는 어떻게 만드는지 알아보자. 다음은 함수의 매개변수와 반환값을 출력하는 데코레이터다.

```python
def trace(func):
    def wrapper(a, b):
        r = func(a, b)
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))
        return r
    return wrapper

@trace
def add(a, b):
    return a + b
    
print(add(2, 5))


# 결과
add(a=2, b=5) -> 7
7
```
add 함수를 호출했을 때 데코레이터를 통해 매개변수와 반환값이 출력되었다. 매개변수와 반환값을 처리하는 데코레이터를 만들 때는 먼저 안쪽 
wrapper 함수의 매개변수를 호출할 함수 add(a, b)의 매개변수와 똑같이 만들어준다.   
wrapper 함수 안에서는 func를 호출하고 반환값을 변수에 저장한다. 그 다음 print로 매개변수와 반환값을 출력한다. 이때 func에는 매개변수 
a, b를 그대로 넣어준다. 또한 add 함수는 두 수를 더해 반환해야 하므로 func의 반환값을 return으로 반환해준다.   
만약 wrapper함수에서 func의 반환값을 반환하지 않으면 add 함수를 호출해도 반환값이 나오지 않으므로 주의해야 한다.

## 가변 인수 함수 데코레이터

def add(a, b)는 매개변수의 개수가 고정된 함수이다. 매개변수가 고정되지 않은 함수는 어떻게 처리할까? 이때는 wrapper 함수를 가변 인수 
함수로 만들면 된다.

```python
def trace(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))
        return r
    return wrapper

@trace
def get_max(*args):
    return max(args)

@trace
def get_min(**kwargs):
    return min(kwargs.values())

print(get_max(5, 7))
print(get_min(x=10, y=20, z=30))


# 결과
get_max(args=(5, 7), kwargs={}) -> 7
7
get_min(args=(), kwargs={'x': 10, 'y': 20, 'z': 30}) -> 10
10
```

## 매개변수가 있는 데코레이터

데코레이터는 값을 지정해서 동작을 바꿀 수 있다. 다음은 함수의 반환값이 특정 수의 배수인지 확인하는 데코레이터이다.

```python
def is_multiple(x):
    def real_decorator(func):
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print('{0}의 반환값은 {1}의 배수이다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아니다.'.format(func.__name__, x))
            return r
        return wrapper
    return real_decorator

@is_multiple(3)
def add(a, b):
    return a + b

print(add(10 ,20))
print(add(2, 5))


# 결과
add의 반환값은 3의 배수이다.
30
add의 반환값은 3의 배수가 아니다.
7
```

실행해보면 add함수의 반환값이 3의 배수인지 아닌지 알려준다.   
지금까지 데코레이터를 만들 때 함수 안에 함수를 하나만 만들었다. 하지만 매개변수가 있는 데코레이터를 만들 때는 함수를 하나 더 
만들어야 한다.   
먼저 is_multiple 함수를 만들고 데코레이터가 사용할 매개변수 x를 지정한다. 그리고 is_multiple 함수 안에서 실제 데코레이터 역할을 
하는 real_decorator를 만든다.    
즉, 이 함수에서 호출할 함수를 매개변수로 받는다. 그 다음 real_decorator 함수 안에서 wrapper 함수를 
만들어주면 된다.

```python
def is_multiple(x):            # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func):  # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):     # 호출할 함수의 매개변수와 똑같이 지정
```

데코레이터를 사용할 때는 데코레이터에 ()를 붙인 뒤 인수를 넣어주면 된다.

```python
@데코레이터(인수)
def 함수이름():
    code...
```

매개변수가 있는 데코레이터를 여러 개 지정할 때는 다음과 같이 인수를 넣은 데코레이터를 여러 줄로 지정해준다.

```python
@데코레이터1(인수)
@데코레이터2(인수)
def 함수이름():
    코드
```

### 만약 원래 함수 이름이 안나온다면?   
데코레이터를 여러 개 사용하면 데코레이터에서 반환된 wrapper 함수가 다른 데코레이터로 들어간다. 따라서 함수의 __name__을 출력해보면 
wrapper가 나온다.   
함수의 원래 이름을 출력하고 싶다면 functools 모듈의 wraps 데코레이터를 사용해야 한다.

```python
import functools

def is_multiple(x):
    def real_decorator(func):
        @functools.wraps(func)      # @functools.wraps에 func를 넣은 뒤 wrapper 함수 위에 지정
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print('{0}의 반환값은 {1}의 배수이다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아니다.'.format(func.__name__, x))
            return r
        return wrapper
    return real_decorator
```

__@functools.wraps는 원래 함수의 정보를 유지시켜준다. 따라서 디버깅할 때 유용하므로 데코레이터를 만들 때는 @functools.wraps를 사용하는 
것이 좋다.__
