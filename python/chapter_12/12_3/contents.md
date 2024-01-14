# yield from 키워드로 외부에 데이터 전달

<pre>
yield from 키워드는 파이썬 3.3 이상부터 사용 가능!
</pre>

### yield from으로 값을 여러 번 바깥으로 전달

지금까지 yield로 값을 한 번씩 바깥으로 전달했다. 그래서 값을 여러 번 바깥으로 전달할 때는 for 또는 while 반복문으로 반복하면서
yield를 사용했다. 다음은 리스트의 1, 2, 3을 바깥으로 전달한다.

```python
def number_generator():
    x = [1, 2, 3]
    for i in x:
        yield i

for i in number_generator():
    print(i)
```

이런 경우에는 매번 반복문을 사용하지 않고 yield from 을 사용하면 된다. yield from에는 반복 가능한 객체, 이터레이터, 제네레이터
객체를 지정한다.

+ yield from 반복가능한객체
+ yield from 이터레이터
+ yield from 제네레이터객체

```python
>>> g = number_generator()
>>> next(g)
1
>>> next(g)
2
>>> next(g)
3
>>> next(g)    # StopIteration 예외 발생
```

다음은 yield from에 리스트를 지정해서 숫자 1, 2, 3을 바깥으로 전달하는 예제이다.

```python
def number_generator():
    x = [1, 2, 3]
    yield from x        # 리스트 요소를 하나씩 바깥으로 전달
    
for i in number_generator():
    print(i)
    
    
# 결과
1
2
3
```

### yield from에 제네레이터 객체 지정

```python
def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

def three_genertor():
    yield from number_generator(3)

for i in three_genertor():
    print(i)
```

number_generator는 매개변수로 받은 숫자 직전까지 숫자를 만들어낸다. 그리고 three_generator에서는
yield from number_generator(3)과 같이 yield from에 제네레이터 객체를 지정했다.   
number_generator(3)은 숫자를 세 개를 만들어내므로 yield from number_generator(3)은 숫자를 세 번 바깥으로 전달한다.
따라서 for 반복문에 three_generator()를 사용하면 숫자를 세 번 출력한다.

[chapter_12 목록으로...](../index.md)