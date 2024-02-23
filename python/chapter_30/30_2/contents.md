# 30-2. Python에서의 TDD

## 대표적인 TDD Module

* [unittest](https://docs.python.org/ko/3/library/unittest.html)
  * unittest 단위 테스트 프레임워크는 파이썬이 기본적으로 제공한다.
* [pytest](https://docs.pytest.org/en/8.0.x/)
  * pytest 단위 테스트 프레임워크는 third-party 모듈이다. 그래서 설치가 필요하다.
    * `pip install -U pytest`

> `unittest`와 `pytest` 프레임워크 중 어느 것을 사용해도 좋다.   
> 나의 선택은 `pytest` 프레임워크!

### unittest와 pytest 비교

```python
import unittest

class LowerTestCase(unittest.TestCase):
    def test_lower(self):
        self.assertEqual('ABCDEFG'.lower(), 'abcdefg')
```

```python
import pytest

def test_lower():
    assert 'ABCDEFG'.lower() == 'abcdefg'
```

위의 코드에서 보다시피 `pytest` 방식이 더 간단하다. `unittest`는 클래스를 꼭 구현하여 `unittest.TestCase`를 상속 받아 테스트를
진행해야하는 반면, `pytest`는 단순히 테스트 함수를 작성하기만 하면 된다.   

또한 `unittest`는 `JUnit`이라는 `Java` 기반의 `TDD` 프레임워크에 영향을 받은 프레임워크라 [PEP8 Python Style Guide](https://peps.python.org/pep-0008/)
에서 권장하는 `Snake Case`가 아닌 `Camel Case`를 사용해야 한다. 이렇게되면 코딩 스타일의 일관성을 잃게 된다.

그래서 나의 선택은... `pytest` 프레임워크!

## pytest 단위 테스트 프레임워크

간단한 TDD를 작성해 보자.

```python
# first_test.py

# func1 테스트 코드 작성
def test_func1():
    assert func1(5) == 10


# func1 구현
def func1(x):
    return x + 6
```

위와 같이 코드 작성 후, 해당 디렉토리로 이동하여 다음과 같이 테스트를 진행할 수 있다.

```shell
# cd <테스트 코드가 존재하는 디렉토리 경로>

python -m pytest first_test.py
```

> -m [module] 옵션의 의미
> > -m 옵션 다음으로 나오는 [module]을 import 한 후, python script 실행

위의 결과는 테스트 실패로 나올 것이다. 그리고 왜 실패했는지 알려줄 것이다. 만약 여러 개의 테스트 함수가 존재한다면... 몇 개의 테스트가 `통과(pass)`했고, 
`실패(fail)`했는 지와 총 테스트 시간을 알려준다.

## pytest 단위 테스트 구조

단위 테스트 파일들을 하나의 디렉토에서 관리하는 것이 더 편할 것이다. 그래야 실제 코드와 분리할 수 있어 효율적이다.

다음은 테스트 코드와 실제 코드와의 분리 모습이다.

```
project/
    code/
        __init__.py
        code1.py
        code2.py
        code3.py
        ...
    tests/
        test_code1.py
        test_code2.py
        test_code3.py
        ...
```

이러한 구조가 만들어진다면, `pytest`로 다음과 같이 단위 테스트를 진행할 수 있다.

```shell
python -m pytest tests
```

## Skip (특정 단위 테스트 건너뛰기)

`@pytest.mark.skip` 데코레이터를 사용하면 특정 단위 테스트를 건너 뛸 수 있다.

[skip](https://docs.pytest.org/en/stable/how-to/skipping.html#skip)은 말 그대로 해당 단위 테스트는 스킵하겠다라는 뜻이다. 아직 미완성된 
기능 구현을 잠시 스킵하고 나머지는 테스트할 때 주로 사용한다.

다음은 pytest에서 제공하는 데코레이터로 Caculator.add 메서드를 건너뛰는 예이다.

```python
@pytest.mark.skip(reason='그냥...')
def test_add():
    calc = core_calc.Calculator()
    assert calc.add(1, 2) == 2
```

## Parametrize (매개변수 테스트)

`@pytest.mark.parametrize` 데코레이터를 사용하면 매개변수 테스트를 수행할 수 있다.

[parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html#parametrizemark)는 테스트 함수의 매개변수에 설정한 값들을 
전달하여 테스트를 진행한다.

```python
@pytest.mark.parametrize('x, y', [(2, 1), (4, 3), (4, 5)])
def test_sub(x, y):
    calc = core_calc.Calculator()
    assert calc.subtract(x, y) == 1
```

위의 코드는 테스트 코드 함수에 개발자가 설정한 매개변수 값을 차례로 실행하며 테스트를 진행한다.

다음과 같이 예상되는 결과 값도 함께 전달하여 테스트를 진행할 수 있다.

```python
@pytest.mark.parametrize('x, y, z', [(2, 1, 1), (4, 3, 1), (4, 5, 1)])
def test_sub(x, y, z):
    calc = core_calc.Calculator()
    assert calc.subtract(x, y) == z
```


## fixture

