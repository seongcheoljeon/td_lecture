# 15-2. 이진 탐색 트리(bisect)

## bisect: 리스트를 정렬된 상태로 유지

> 목적
> > 리스트에 아이템이 추가될 때마다 정렬 함수를 호출하지 않고 리스트를 정렬된 상태로 유지

bisect 모듈은 리스트가 정렬된 상태를 유지하면서 아이템을 넣을 수 있게 구현되어 있다.
커다란 리스트에 아이템이 들어올 때마다 반복적으로 정렬하는 것보다 이 방식이 더 효율적일 수 있다.

### 정렬된 상태로 아이템 추가

insort()를 사용해 리스트가 정렬된 상태를 유지하면서 아이템을 추가하는 예제

```python
import bisect
import random

random.seed(1)

print('new  pos     contents')
print('---  ---     --------')

lst = list()

for i in range(1, 15):
    r = random.randint(1, 100)
    position = bisect.bisect(lst, r)
    bisect.insort(lst, r)

    print('{0:>3} {1:>3}'.format(r, position), '\t', lst)
```

위의 예제는 매우 간단하고 리스트의 크기도 작기 때문에 리스트를 생성한 후에 정렬하는 방식이 더 빠를 것이다.   
하지만 __리스트의 길이가 매우 길어지면 위와 같은 방식을 사용하는 편이 시간과 메모리 낭비를 비약적으로 줄여줄 수 있다.__