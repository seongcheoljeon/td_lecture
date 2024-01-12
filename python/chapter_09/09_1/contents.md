# 비공개 속성

python에서는 정보 은닉(information hiding)이 없다. 하지만 "__ (double underscore)" 를 통해 정보 은닉 같은
효과를 나타낼 수 있다.

<pre>
_  (underscore 1개)     : 파일 내에서만 허용
__ (underscore 2개)     : 클래스 내에서만 허용
</pre>

## _ (underscore)

```python
class Custom1:
    def __init__(self):
        self.val = 55

class _Custom2:
    def __init__(self):
        self.val = 55
```
위와 같이 클래스가 a_file.py 파일에 정의되어 있다고 가정하고 b_file.py에서 해당 클래스를 import하여 사용하는 경우,
다음과 같은 결과를 볼 수 있다.

```python
import a_file

# ok
a = a_file.Custom1()
print(a.val)

# error - not defined _Custom2
b = a_file._Custom2()
print(b.val)
```

즉, 언더스코어 1개는 해당 파일안에서만 사용 가능하다는 뜻이다.

## __ (double underscore)

```python
class Custom:
    def __init__(self):
        self.foo = 5
        self.__var = 55

    def get_var(self) -> int:
        return self.__var

custom = Custom()

print(custom.foo)           # ok
print(custom.__var)         # error
print(custom.get_var())     # ok
```

