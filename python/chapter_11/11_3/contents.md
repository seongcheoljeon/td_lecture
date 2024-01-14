# iter, next 함수 사용

파이썬 내장 함수 iter, next에 대해 알아보자. iter는 객체의 __iter__ 메서드를 호출해주고, next는 객체의 __next__ 메서드를 호출해준다.

```python
>>> it = iter(range(3))
>>> next(it)
0
>>> next(it)
1
...
```

반복 가능한 객체에서 __iter__를 호출하고 이터레이터에서 __next__ 메서드를 호출한 것과 똑같다. 즉, iter는 반복 가능한 객체에서 
이터레이터를 반환하고 next는 이터레이터에서 값을 차례대로 꺼낸다. iter와 next는 이런 기능 이외에도 다양한 방식으로 사용할 수 있다.

## iter

iter는 반복을 끝낼 값을 지정하면 특정 값이 나올 때 반복을 끝낸다. 이 경우에는 반복 가능한 객체 대신 호출 가능한 객체(callable)를 
넣어준다.    
참고로 반복을 끝낸 값은 sentinel이라고 부르는데 감시병이라는 뜻이다. 즉, 반복을 감시하다가 특정 값이 나오면 반복을 끝낸다고 
해서 sentinel이다.

* iter(호출가능한객체, 반복을끝낼값)

예를 들어 random.randint(0, 5)와 같이 0부터 5까지 무작위로 숫자를 생성할 때 2가 나오면 반복을 끝내도록 만들 수 있다. 이때 호출 
가능한 객체를 넣어야 하므로 매개변수가 없는 함수 또는 람다 표현식으로 만들어준다.

```python
>>> import random
>>> it = iter(lambda: random.randint(0, 5), 2)
>>> next(it)
0
>>> next(it)
3
>>> next(it)
# 만약 여기서 2가 나왔다면 StopIteration 예외가 발생하여 반복 종료
```

next(it)로 숫자를 계속 만들다가 2가 나오면 StopIteration이 발생한다. 다음과 같이 for 반복문에 넣어서 사용할 수도 있다.

```python
import random

if __name__ == '__main__':
    for i in iter(lambda: random.randint(0, 5), 2):
        print(i, end=' ')
        
        
# 결과
1 1 0 5 3 3 5 4
```

이렇게 iter 함수를 활용하면 if 조건문으로 매번 숫자가 2인지 검사하지 않아도 되므로 코드가 좀 더 간단해진다.

## next

next는 기본 값을 지정할 수 있다. 기본 값을 지정하면 반복이 끝나더라도 StopIteration이 발생하지 않고 기본값을 출력한다. 즉, 반복할 수 있을 때는 해당 값을 출력하고, 반복이 끝났을 때는 기본값을 출력한다. 다음은 range(3)으로 0, 1, 2 세 번 반복하는데 next에 기본값으로 10을 지정했다.

* next(반복가능한객체, 기본값)

```python
>>> it = iter(range(3))
>>> next(it, 10)
0
>>> next(it, 10)
1
>>> next(it, 10)
2
>>> next(it, 10)
10
```

이터레이터를 만들 때 __iter__, __next__ 또는 __getitem__ 메서드를 구현해야 한다는 점을 기억해야 한다.

[chapter_11 목록으로...](../index.md)