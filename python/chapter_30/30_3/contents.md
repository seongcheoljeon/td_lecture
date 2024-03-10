# 30-3. Factory Pattern


객체를 만들어 생성자 대신 반환하는 함수를 제공하여 초기화 과정을 외부에서 보지 못하게 숨기고 반환 타입을 제어하는 방법을 `팩토리 패턴(Factor Pattern)`
이라고 한다.

```python
class Car:
    def __init__(self): ...
```

```python
class Benz(Car):
    def __init__(self): ...
```

```python
class Porsche(Car):
    def __init__(self): ...
```

예를 들어, 위와 같이 자동차 클래스를 정의했다고 해보자. 이제 자동차들을 도로에 배치해야 하는 상황이다. 그러면 다음과 같이 코드를 구성할 수도 
있다.

```python
class Road:
    def __init__(self, seq_data):
        for dat in seq_data:
            if dat.name == 'Benz':
                return Benz(dat)
            elif dat.name == 'Porsche':
                return Porsche(dat)
            ...
```

작동 자체에는 문제가 없는 코드이지만, 객체지향적으로 보면 [단일 책임 원칙](../../chapter_10/10_7/contents.md)을 위반하였다. `Road`는 말 
그대로 도로 구현 방법에 대해서만 서술되어야 하는데, 데이터를 읽는 부분에서 `유닛`을 `분류`하는 추가적인 `책임`이 포함되어 있다. 만일 새로운 자동차가
생겨나고, 새로운 자동차를 넣어야 한다면 __전혀 상관없는 Road 클래스를 수정해야 할 것이다.__

그래서 다양한 하위 클래스들을 생성하는(Factory: 공장) 클래스를 만들어 그 클래스에 `책임`을 `위임`하는 것이다.   

다음은 팩토리 패턴을 이용한 메서드 정의이다.

```python
class CarFactory:
    @staticmethod
    def create(data):
        if data.name == 'Benz':
            return Benz(data)
        elif data.name == 'Porsche':
            return Porsche(data)
        ...
```

이후 Road 클래스는 다음과 같이 수정하면 된다.

```python
class Road:
    def __init__(self, seq_data):
        for dat in seq_data:
            return CarFactory.create(seq_data.name)
        ...
```

이렇게 한다면, 새로운 자동차가 추가하는지의 여부에 상관없이 다른 클래스를 수정할 필요가 없어져 `단일 책임 원칙`을 잘 지키는 코드가 된다.