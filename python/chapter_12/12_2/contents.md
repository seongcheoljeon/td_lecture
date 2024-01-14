# 제네레이터 생성

range(count)처럼 동작하는 제네레이터를 만들어 보자.

```python
def number_generator(stop: int) -> int:
    i = 0
    while i < stop:
        yield i
        i += 1


for i in number_generator(3):
    print(i)
    
    
# 결과
0
1
2
```

### yield에서 함수 호출

```python
def upper_generator(x: list) -> str:
    for i in x:
        yield i.upper()


fruits = ['apple', 'pear', 'grape']
for i in upper_generator(fruits):
    print(i, end=' ')
    
    
# 결과
APPLE PEAR GRAPE
```

[chapter_12 목록으로...](../index.md)
