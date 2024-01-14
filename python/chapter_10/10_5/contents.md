# 추상 클래스 (abstract class)

### 추상 메소드(abstract method)
추상 메소드(abstract method)란 자식 클래스에서 반드시 오버라이딩해야만 사용할 수 있는 메소드를 의미한다.   
추상 메소드를 선언하여 사용하는 목적은 추상 메소드가 포함된 클래스를 상속받는 자식 클래스가 반드시 추상 메소드를 구현하도록 하기 
위함이다.

예를 들면 모듈처럼 중복되는 부분이나 공통적인 부분은 미리 다 만들어진 것을 사용 하고, 이를 받아 사용하는 쪽에서는 자신에게 필요한 
부분만을 재정의하여 사용함으로써 생산성이 향상되고 배포 등이 쉬워지기 때문이다.

이러한 추상 메소드는 선언부만이 존재하며, 구현부는 작성되어 있지 않다.

바로 이 작성되어 있지 않은 구현부를 자식 클래스에서 오버라이딩하여 사용하는 것이다.

### 추상 클래스(abstract class)
하나 이상의 추상 메소드를 포함하는 클래스를 가리켜 추상 클래스(abstract class)라고 한다.
이러한 추상 클래스는 객체 지향 프로그래밍에서 중요한 특징인 다형성을 가지는 메소드의 집합을 정의할 수 있도록 해준다.
즉, 반드시 사용되어야 하는 메소드를 추상 클래스에 추상 메소드로 선언해 놓으면, 이 클래스를 상속받는 모든 클래스에서는 
이 추상 메소드를 반드시 재정의해야 한다.

```python
import abc


class Animal(metaclass=abc.ABCMeta):
    # 추상 클래스
    @abc.abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print('walk!!')


class Dog(Animal):
    def move(self):
        print('run!!')


class Tiger(Animal):
    def move(self):
        print('aaag!')


h = Human()
d = Dog()
t = Tiger()

h.move()
d.move()
t.move()
```

## 다형성 (polymorphism)

+ 같은 모양의 코드가 다른 동작을 하는 것을 다형성이라고 한다.
  + override와는 다른 개념!
    + 오버라이드는 단순히 덮어 씌우는 것이고, 다형성은 같은 코드가 다른 형태를 띄는 개념.



