# 이터레이터 생성

__iter__, __next__ 메서드를 구현하여 직접 이터레이터를 만들어보자. 간단하게 range(횟수)처럼 동작하는 이터레이터다.

```python
class Counter:
    def __init__(self, stop: int) -> None:
        self.__current = 0
        self.__stop = stop
        
    def __iter__(self):
        return self
    
    def __next__(self) -> int:
        if self.__current < self.__stop:
            r = self.__current
            self.__current += 1
            return r
        else:
            raise StopIteration
        
    
if __name__ == '__main__':
    for i in Counter(3):
        print(i, end=' ')
        
        
# 결과
0 1 2
```

__iter__ 메서드를 만드는데 여기서는 self만 반환한다. 이 객체는 리스트, 문자열, 딕셔너리, 세트, range처럼 __iter__ 를 호출해줄 
반복 가능한 객체(iterable)가 없으므로 현재 인스턴스를 반환하면 된다. 즉, 이 객체는 반복 가능한 객체이면서 이터레이터이다.   
그 다음에 __next__ 메서드를 만든다. __next__ 에서는 조건에 따라 숫자를 만들어내거나 StopIteration 예외를 발생시킨다.

## 인덱스로 접근할 수 있는 이터레이터

```python
class Counter:
    def __init__(self, stop: int) -> None:
        self.__current = 0
        self.__stop = stop

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.__current < self.__stop:
            r = self.__current
            self.__current += 1
            return r
        raise StopIteration

    def __getitem__(self, item: int) -> int:
        if item < self.__stop:
            return item
        raise IndexError


if __name__ == '__main__':
    print(Counter(3)[2])
    
    
# 결과
2
```

__getitem__ 메서드를 구현하면 인덱스로 접근할 수 있는 이터레이터를 만들 수 있다.

[chapter_11 목록으로...](../index.md)
