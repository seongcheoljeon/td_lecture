# 08-6. `__slots__`

[__slots__관련 공식 문서](https://docs.python.org/ko/3/reference/datamodel.html#slots)

> `__slots__`는 파이썬 클래스의 컨텍스트에서만 사용된다.   

## `__slots__`를 왜 사용할까?
간단히 설명하자면, `__slots__`는 메모리 공간과 액세스 속도 측면에서 더 효율적이며, 기본 Python 데이터 액세스 방법보다 조금 더 안전하다는 것이다.    
기본적으로 파이썬은 클래스의 새 인스턴스를 생성할 때 클래스에 대한 `__dict__`어트리뷰트를 생성한다. `__dict__`어트리뷰트는 키가 변수 이름이고 
값이 변수 값인 딕셔너리이다.    
이를 통해 동적 변수를 생성할 수 있지만, 잡히지 않는 오류가 발생할 수도 있다. 예를 들어 기본 `__dict__`를 사용하면 변수 이름의 철자가 틀릴 경우, 
새 변수가 생성되지만... `__slots__`를 사용하면 AttributeError가 발생한다.

```python
class TestSlot:
    __slots__ = ('slot_a', 'slot_b', 'slot_c')

    def __init__(self):
        self.slot_a = 'slot A'
        self.slot_b = 'slot B'
        self.slot_c = 'slot C'


if __name__ == '__main__':
    ts = TestSlot()
    print(ts.slot_a)
    print(ts.slot_b)
    print(ts.slot_c)

    # error 발생! __slots__에 등록되어있지 않으므로
    ts.slot_d = 'slot D'
```

`__slots__`선언을 사용하면 데이터 멤버를 명시적으로 선언할 수 있고, 파이썬이 메모리에서 해당 멤버를 위한 공간을 예약하며, `__dict__` 및 `__weakref__`
어트리뷰트가 생성되지 않도록 할 수 있다. 또한 `__slots__`에 선언되지 않은 변수가 생성되지 않도록 한다.

```python
class TestSlot2:
    def __init__(self):
        self.slot_var = 'slot variable'


if __name__ == '__main__':
    ts2 = TestSlot2()
    # ts2.slot_var의 값을 변경하려 하였으나... 실수로 _(언더바)가 더 들어간 상태
    ts2.slot__var = 'abcd'

    print(ts2.__dict__.keys())
    print(ts2.__dict__.values())
```

## `__slots__`를 사용하지 않아야하는 이유 

예를 들어 클래스에서 동적 어트리뷰트 생성이나 약한 참조를 사용하려는 경우와 같이 __slots__를 사용하지 않으려는 경우가 있을 수 있다.    
이러한 경우 `__slots__` 선언의 마지막 요소로 `__dict__` 또는 `__weakref__`를 추가하면 된다.


