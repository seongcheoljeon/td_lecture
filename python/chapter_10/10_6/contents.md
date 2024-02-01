# 죽음의 다이아몬드 (the Deadly Diamond of Death: DDD) 란?

한 번에 둘 이상의 클래스를 파생받는 경우, 다시 말해 여러 부모를 둔 경우를 두고 다중 상속(multiple inheritance) 이라고 칭한다. 이 방식의 장점은 
매우 직관적이라는 것이다. 하지만 사실 별로 권장되는 방법은 아닌데, 바로 밑의 '죽음의 다이아몬드' 때문에 일반 클래스를 다중 상속하는건 극히 꺼려지며 
인터페이스 용도의 클래스에서만 상속받는게 일반적이다. 사실 다중 상속은 이런저런 것으로 대체 가능하므로 __인터페이스 다중 상속을 제외__하고 다중 상속되는 
상황 자체가 이미 잘못된 접근일 확률이 높다.
Java와 C#은 아예 문법적으로 다중 상속을 하지 못하도록 막아 놓았다. 그나마 예외로는 C++의 Signal/Slot이나 GUI에서 부모 자식 관계를 이용한 
자동 메모리 관리와 기본 GUI 컴포넌트의 상속, 또는 Qt(프레임워크)의 QObject 정도가 있다. C++ 이외에 파이썬도 다중상속이 가능하다.   
멤버변수가 있는 클래스를 다중상속했을 경우 다중상속으로 인해 2번째 이후로 오는 클래스는 첫 번째 클래스 다음 순서로 메모리에 올라오기 때문에 원본 
클래스와는 메모리 위치가 다르며, 이에 대한 메모리 주소 처리를 요구하기 때문에 추가적인 오버헤드가 발생한다.

## 협동적 메서드와 super()

<pre>
협동적 클래스(Cooperative Classes)란? 협동적 super call을 호출하는 다중 상속 관계에 있는 클래스들을 말한다.
</pre>

### 기존 클래스의 문제점

기존 클래스의 문제점을 살펴보자. 이것은 __파이썬만의 문제가 아니라 대부분 객체지향 언어에서 발생할 수 있는 문제__ 이다.

예를 들어, 어떤 클래스(A)가 있고 서브 클래스(B)에서 슈퍼 클래스의 save 메서드를 확장하려 한다.

```python
class A:
    def save(self):
        print('call - A class save')
        
class B:
    def save(self):
        print('call - B class save')
        A.save(self)
```

A의 save는 A만의 자료를 저장하고 B의 save는 B만의 자료를 저장한다. 따라서 클래스 B의 save는 A.save를 호출한다.   
__그러나 다이아몬드 관계인 경우 문제가 발생한다__ 다음 클래스를 살펴보자.

```python
class A(object):
    def save(self):
        print('call - A class save')
        
class B(A):
    def save(self):
        print('call - B class save')
        A.save(self)
        
class C(A):
    def save(self):
        print('call - C class save')
        A.save(self)
        
class D(B, C):
    def save(self):
        print('call - D class save')
        B.save(self)
        C.save(self)

'''
결과
D -> B -> A -> C -> A
'''
```

* 이것을 수행하면 A의 데이터가 두 번이나 저장된다.
  * B에 의해 한 번
  * C에 의해 한 번

위의 것을 현재 알고 있는 지식으로만 해결하면 다음과 같이 할 수 있겠다.

```python
class A(object):
    def save(self):
        print('call - A class save')

class B(A):
    def _save(self):
        print('call - B class save')
        
    def save(self):
        self._save()
        A.save(self)

class C(A):
    def _save(self):
        print('call - C class save')
        
    def save(self):
        self._save()
        A.save(self)

class D(B, C):
    def _save(self):
        print('call - D class save')
        
    def save(self):
        self._save()
        B.save(self)
        C.save(self)
        A.save(self)

'''
D -> B -> C -> A
'''
```

즉, 어떤 클래스의 save는 자신의 정보만을 저장하는 self._save()를 호출한 후에 슈퍼 클래스의 지역 정보를 저장하는 메서드를 일일이 호출해야 한다.   
해결은 되었지만, 누가 봐도 좋은 코드라고 말할 수 없다. 클래스 D는 슈퍼 클래스들의 모든 구조를 알아야 save 메서드를 작성할 수 있다. ___이러한 내용은 
객체지향 언어가 추구하고 있는 방향과는 상반된 것이다.___     
또한 코드의 이식성이 크게 떨어지며 나중에 C를 제거하거나, 또 다른 클래스 E를 슈퍼 클래스로 추가하려면 D의 코드는 다시 작성되어야 한다.


## 협동적 클래스를 이용한 문제 해결

위와 같은 문제는 super를 이용한 협동적 클래스로 해결 가능하다. super()는 다음과 같은 형식을 가진다.

> super(class name, self).method()
> 슈퍼 클래스의 "메서드"를 호출하라.

슈퍼 클래스는 여러 개가 있을 수 있다. 따라서 어떤 슈퍼 클래스를 호출하는가는 **self.__class__.__mro__ 와 클래스 이름** 을 이용하여 결정된다.   
예를 들어, self.__class__.__mro__가 (w, x, y, z)이고 클래스 이름이 x일 경우 x 다음에 있는 y 메서드가 호출된다.

```python
class A(object):
    def save(self):
        print('call save - A class')

class B(A):
    def save(self):
        print('call save - B class')
        super(B, self).save()

class C(A):
    def save(self):
      print('call save - C class')
      super(C, self).save()

class D(B, C):
    def save(self):
      print('call save - D class')
      super(D, self).save()
      
'''
결과
D -> B -> C -> A
'''
```

### 클래스의 __mro__
```python
A.__mro__
(<class '__main__.A'>, <type 'object'>)

d = D()
d.__class__.__mro__
(<class '__main__.D>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>)
```

super는 self.__class__.__mro__의 순서에 따라 save()를 호출한다고 했다. super는 self.__class__.__mro__에서 자신의 클래스 다음의 클래스 
객체의 save를 호출한다.   
예를 들어, super(C, self).save()에서 전달된 self.__class__.__mro__가 (D, B, C, A, object)라면, A.save(self)를 호출한다.

### 단계적 설명
1. d.save()에 의해 super(D, self).save()가 호출.
2. self는 d이고 d.__class__.__mro__가 (D, B, C, A, object)이므로 super(D, self).save()에 의하여 B.save(self)가 호출
3. B.save(self)에 의해 super(B, self).save()가 호출. 이 때 self는 여전히 'd' 임에 주의해야 한다. self.__class__.__mro__는 여전히 (D, B, C, A, object) 값을 가진다. 따라서 super(B, self).save()는 B 다음 클래스인 C에서 C.save(self)를 호출한다.
4. 같은 방법으로 super(C, self).save()는 A.save(self)를 호출한다.

> 이와 같은 super를 사용하면 앞서 해결 할 수 없었던 슈퍼 클래스 메서드의 호출 문제를 깔끔하게 해결할 수 있다.