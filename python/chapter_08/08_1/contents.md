# namespace

네임스페이스란 객체를 이름에 따라 구분할 수 있는 범위를 말한다. 파이썬 내부의 모든 것들은 전부 객체로 구성되어 있고, 이들은 특정 이름들과의 매핑 관계를 
가지고 있다. 이 매핑을 포함하고 있는 공간을 네임스페이스라고 한다. 네임스페이스의 내부는 __key, value__ 구조이다.

## namespace 종류
+ 내장(builtins) namespace
    + 기본 내장 함수 및 기본 예외들의 이름이 저장됨.
+ 전역(globals) namespace
  + 모듈별로 존재함. 모듈 전체에 통용되는 이름 사용.
+ 클로저(enclosing) namespace
  + 함수 내의 함수에 할당된 이름.
+ 지역(locals) namespace
  + 함수 및 메서드 별로 존재. 함수 내의 지역 변수들이 소속 됨.

<center><img src="images/types_namespace.png" width="813" height="722"></center>       

### builtins namespace
```python
print(dir(__builtins__))
```
### globals namespace
```python
a = 55
print(globals())
```
### enclosing namespace
```python
def a_func():
    a = 'a'
    
    def b_func():
        b = 'b'
        print(a)
    
    b_func()

a_func()
```

### locals namespace
```python
def test_func():
    a = 1005
    print(locals())

print(globals())
```

## nonlocal 키워드
아! 이런 키워드도 있구나하는 정도로 가볍게!   
자주 사용하지는 않지만 가끔씩 만날 수 있다.

```python
def a_func():
    x = 10

    def b_func():
        global x
        x = 50

    b_func()
    print(x)

a_func()
```

```python
def a_func():
    x = 10

    def b_func():
        nonlocal x
        x = 50

    b_func()
    print(x)

a_func()
```

## class로 namespace 만들기

```python
class AClass:
    var = 'AClass: var'

class BClass:
    var = 'BClass: var'

class CClass:
    var = 'CClass: var'

print(AClass.var)
print(BClass.var)
print(CClass.var)
```