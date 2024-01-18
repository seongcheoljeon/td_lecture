# 유용한 모듈 (itertools)

+ itertools
  + [itertools: 효율적인 루핑을 위한 이터레이터](https://docs.python.org/ko/3/library/itertools.html)

이 모듈은 반복 가능한 객체(시퀀스, 반복자, 발생자 등)의 반복자(or 발생자)를 생성하는 몇 개의 함수로 구성되어 있다.   
이들 함수는 메모리와 계산 시간에서 효과적인 연산이 가능하도록 많은 도움을 준다.    
반복자가 효과적인 이유는? __데이터가 요구될 때 필요한 시점에서 데이터를 준비하여 리턴하기 때문이다.__

> 여기에서 설명하는 함수들은 자료의 크기가 크면 클수록 더욱 더 그 효과를 발휘한다.

## chain(*iterables)

* chain 함수는 객체에서 자료를 연속해서 하나씩 넘겨준다.

```python
import itertools as it

l1 = [1, 2, 3]
l2 = [4, 5, 6]

for i in it.chain(l1, l2):
    print(i,)

'''
결과
1 2 3 4 5 6
'''
```

l1, l2에 대한 연속된 데이터를 넘겨준다.

```python
for i in (l1 + l2):
    print(i,)

'''
1 2 3 4 5 6
'''
```

위의 방법은 새로운 리스트를 생성하므로 메모리 낭비 및 속도 저하가 발생한다.

## groupby(iterable[,key])

* groupby 함수는 자료를 그룹 단위로 묶는 데 사용된다. key 함수가 주어지지 않았을 경우, 요소 자료 자체가 키 값이 된다.

```python
lst = [(1, 2), (2, 3), (1, 2), (4, 2)]

for key, group in it.groupby(sorted(lst)):
    print(key, list(group))

'''
결과
(1, 2) [(1, 2), (1, 2)]
(2, 3) [(2, 3)]
(4, 2) [(4, 2)]
'''
```

인수가 정렬되어야 인접한 자료를 한 그룹으로 묶을 수 있다.

두 번째 자료를 기준으로 그룹화하려면 다음과 같이 할 수 있다.

```python
from operator import itemgetter

for key, group in groupby(sorted(lst, key=itemgetter(1)), key=itemgetter(1)):
    print(key, list(group))

'''
결과
2 [(1, 2), (1, 2), (4, 2)]
3 [(2, 3)]
'''
```

itemgetter(1)은 어떤 객체의 [1] 요소 값을 취하는 함수이다. 즉, lambda x: x[1]과 같은 함수이다.

다음의 예는 문장의 단어가 몇 번 반복되는가를 출력한다.

```python
s = 'When you believe in a thing, believe in it all the way, implicitly and unquestionable' 

for key, group in it.groupby(sorted(s.split())):
    print(key, len(list(group)))
```