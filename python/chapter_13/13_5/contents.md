# 동시성 관리 구현에 유용한 모듈 (futures, asyncio)

## asyncio (Asynchronous I/O) 비동기 프로그래밍

asyncio는 비동기 프로그래밍을 위한 모듈이며, CPU 작업과 I/O를 병렬로 처리하게 해준다.   

동기(synchronous) 처리는 특정 작업이 끝나면 다음 작업을 처리하는 순차처리 방식이다.   
비동기(asynchronous) 처리는 여러 작업을 처리하도록 예약한 뒤 작업이 끝나면 결과를 받는 방식이다.   

## 네이티브 코루틴 만들기 

먼저 asyncio를 사용하려면 다음과 같이 async def로 네이티브 코루틴을 만든다. 참고로 파이썬에서는 제네레이터 기반의 코루틴과 구분하기 위해 async def로 만든 코루틴은 네이티브 코루틴이라고 한다.   

```python
async def 함수이름():
    코드...
```

```python
import asyncio

async def hello():               # async def로 네이티브 코루틴을 만듦
    print('hello, world!')
    
loop = asyncio.get_event_loop()  # 이벤트 루프를 얻음
loop.run_until_complete(hello()) # hello가 끝날 때까지 기다림
loop.close()                     # 이벤트 루프를 닫음

# 결과
hello, world!
```

먼저 async def로 hello를 만든다. 그 다음 asyncio.get_event_loop 함수로 이벤트 루프를 얻고 loop.run_until_complete(hello())와 같이 run_until_complete에 코루틴 객체를 넣는다.   

* 이벤트루프 = asyncio.get_event_loop()
* 이벤트루프.run_until_complete(코루틴객체 또는 퓨처객체)

```python
loop = asyncio.get_event_loop()  # 이벤트 루프를 얻음
loop.run_until_complete(hello()) # hello가 끝날 때까지 기다림
```

run_until_complete는 네이티브 코루틴이 이벤트 루프에서 실행되도록 예약하고 해당 네이티브 코루틴이 끝날 때까지 기다린다. 이렇게 하면 이벤트 루프를 통해서 hello 코루틴이 실행된다. 할 일이 끝났으면 loop.close로 이벤트 루프를 닫아준다.   

## await로 네이티브 코루틴 실행

다음과 같이 await 뒤에 코루틴 객체, 퓨처 객체, 태스크 객체를 지정하면 해당 객체가 끝날 때까지 기다린 뒤 결과를 반환한다. await는 단어 듯 그대로 특정 객체가 끝날 때까지 기다린다.   

* 변수 = await 코루틴객체
* 변수 = await 퓨처객체
* 변수 = await 태스크객체

여기서 주의할 점이 있는데 await는 네이티브 코루틴 안에서만 사용할 수 있다는 것이다.   

다음은 두 수를 더하는 네이티브 코루틴을 만들고 코루틴에서 1초 대기한 뒤 결과를 반환하는 예제이다.   

```python
import asyncio


async def add(a, b):
    print('{0} + {1}'.format(a, b))
    await asyncio.sleep(1.0)    # 1초 대기. asyncio.sleep도 네이티브 코루틴
    return a + b


async def print_add(a, b):
    # await로 다른 네이티브 코루틴 실행하고 반환값 저장
    res = await add(a, b)
    print('{0} + {1} = {2}'.format(a, b, res))


# 이벤트 루트 얻음
loop = asyncio.get_event_loop()
# print_add가 끝날 때까지 이벤트 루프 실행
loop.run_until_complete(print_add(1, 2))
# 이벤트 루프 닫음
loop.close()


# 결과
1 + 2
1 + 2 = 3
```

print_add에서는 await로 add를 실행하고 반환값을 변수에 저장한다. 이렇게 코루틴 안에서 다른 코루틴을 실행할 때는 await를 사용한다.   

add에서는 await asyncio.sleep(1.0)으로 1초 대기한 뒤 return a+b로 두 수를 더한 결과를 반환한다. 사실 await asyncio.sleep(1.0)은 없어도 되지만 코루틴이 비동기로 실행된느 모습을 확인하기 위해 사용했다. 특히 asyncio.sleep도 네이티브 코루틴이라 await를 사용해야 한다.   

## 퓨처와 태스크

퓨처(asyncio.Future)는 미래에 할 일을 표현하는 클래스인데 할 일을 취소하거나 상태 확인, 완료 및 결과 설정에 사용한다.   

태스크(asyncio.Task)는 asyncio.Future의 파생 클래스이며 asyncio.Future의 기능과 실행할 코루틴의 객체를 포함하고 있다. 태스크는 코루틴의 실행을 취소하거나 상태 확인, 완료 및 결과 설정에 사용한다.    

## 비동기로 웹 페이지 가져오기

asynio를 사용하여 비동기로 웹 페이지를 가져와보자.   

그 전에 다음과 같이 asyncio를 사용하지 않고 웹 페이지를 순차적으로 가져오겠다. urllib, request의 urlopen으로 웹 페이지를 가져온 뒤 웹 페이지의 길이를 출력해보자.   

```python
# 동기(순차적)로 웹페이지 가져오기

from time import time
from urllib.request import Request, urlopen

urls = ['https://www.google.co.kr/search?q=' + i
            for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']
        ]

begin = time()
result = []
for url in urls:
    # user-agent가 없으면 403에러 발생
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    response = urlopen(request)
    page = response.read()
    result.append(len(page))


print(result)
end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))


# 결과
[74443, 137795, 84429, 327409, 65139, 154872]
실행 시간: 4.865초
```

그럼 이제 asyncio를 사용해서 비동기로 실행해보자.   

```python
import asyncio
from time import time
from urllib.request import Request, urlopen

urls = ['https://www.google.co.kr/search?q=' + i
            for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']
        ]

async def fetch(url):
    # user-agent가 없으면 403 에러 발생
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = await loop.run_in_executor(None, urlopen, request)
    page = await loop.run_in_executor(None, response.read)
    return len(page)

async def main():
    # 태스크(퓨처) 객체를 리스트로 만듦
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]
    # 결과를 한꺼번에 가져옴
    result = await asyncio.gather(*futures)
    print(result)


begin = time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))


# 결과
[72734, 119950, 84669, 79735, 65231, 154872]
실행 시간: 1.484초
```

asyncio를 사용하니 실행 시간이 4초대에서 1초대로 줄었습니다.   

urlopen이나 response.read 같은 함수는 결과가 나올 때까지 코드 실행이 중단(block)되는데 이런 함수들을 블로킹 I/O(blocking I/O) 함수라고 부른다. 특히 네이티브 코루틴 안에서 블로킹 I/O 함수를 실행하려면 이벤트 루프의 run_in_excutor 함수를 사용하여 다른 스레드에서 병렬로 실행시켜야 한다.   

run_in_executor의 첫 번째 인수는 executor인데 함수를 실행시켜줄 스레드 풀 또는 프로세스 풀이다. 여기서는 None을 넣어서 기본 스레드 풀을 사용한다. 그리고 두 번째 인수에는 실행할 함수를 넣고 세 번째 인수부터는 실행할 함수에 들어갈 인수를 차례대로 넣어준다.   

* 이벤트루프.run_in_executor(None, 함수, 인수1, 인수2, 인수3)

run_in_executor도 네이티브 코루틴이므로 await로 실행한 뒤 결과를 가져온다.   

main에서는 네이티브 코루틴 여러 개를 동시에 실행하는데 , 이때는 먼저 asyncio.ensure_future 함수를 사용하여 태스크(asyncio.Task) 객체를 생성하고 리스트로 만들어준다.   

* 태스크객체 = asyncio.ensure_future(코루틴객체 또는 퓨처객체)

그 다음 태스크 리스트를 asyncio.gather 함수에 넣어준다. asyncio.gather는 모든 코루틴 객체(퓨처, 태스크 객체)가 끝날 때까지 기다린 뒤 결과(반환값)를 리스트로 반환한다.   

* 변수 = await asyncio.gather(코루틴객체1, 코루틴객체2)

asyncio.gather는 리스트가 아닌 위치 인수로 객체를 받으므로 태스크 객체를 리스트로 만들었다면 asyncio.gather(*futures)와 같이 리스트를 언패킹해서 넣어준다. 또한, asyncio.gather도 코루틴이므로 await로 실행한 뒤 결과를 가져온다.   

참고로 asyncio.gather에 퓨처 객체를 넣은 순서와 결과 리스트에서 요소의 순서는 일치하지 않을 수도 있다.   

--- 

run_in_executor 같은 함수는 위치 인수만 넣을 수 있는데 파이썬에서는 키워드 인수를 많이 사용한다. run_in_executor에 키워드 인수를 사용하는 함수를 넣을 때는 functools.partial을 사용해야 한다. functools.partial은 이름 그대로 부분 함수를 만들어주는 기능이다.   

* functools.partial(함수, 위치인수, 키워드인수)

```python
import functools

async def hello(executor):
    await loop.run_in_executor(None, functools.partial(print, 'hello', 'python', end=' ')
```

functools.partial은 인수가 포함된 부분 함수를 반환하는데, 반환된 함수에 다시 인수를 지정해서 호출할 수 있다.   

```python
>>> import functools
>>> hello = functools.partial(print. 'hello', 'python', end=' ')
>>> hello()
hello python
>>> hello('script', sep='-')
hello-python-script
```

## async with와 async for 사용하기

* async with : 클래스나 함수를 비동기로 처리한 뒤 결과를 반환하는 문법이다. 
* async for : 비동기로 반복하는 문법이다.

### async with

async with는 with 다음에 클래스의 인스턴스를 지정하고 as 뒤에 결과를저장할 변수를 지정한다.   

```python
async with 클래스() as 변수:
    코드...
```

async with로 동작하는 클래스를 만들려면 __aenter__ (asynchronuous enter) 와 __aexit__ (asynchronous exit) 메서드를 구현해야 한다. 그리고 메서드를 만들 때는 반드시 async def를 사용한다.   

```python
class 클래스이름:
    async def __aenter__(self):
        코드...
        
    async def __aexit__(self, exc_type, exc_value, traceback):
        코드...
```

다음은 1초 뒤에 덧셈 결과를 반환하는 클래스이다.   

```python
import asyncio

class AsyncAdd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    async def __aenter__(self):
        await asyncio.sleep(1.0)
        # __aenter__에서 값을 반환하면 as에 지정한 변수에 들어감
        return self.a + self.b

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


async def main():
    async with AsyncAdd(1, 2) as result:
        print(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


# 결과
3
```

__aenter__ 메서드에서 1초 대기한 뒤 self.a와 self.b를 더한 값을 반환하도록 만든다. 이렇게 __aenter__에서 값을 반환하면 as에 지정한 변수에 들어간다. __aexit__메서드는 async with as를 완전히 벗어나면 호출되는데 여기서는 특별히 만들 부분이 없으므로 pass를 넣는다. 메서드 자체가 없으면 에러가 발생한다.   

### async for

async for로 동작하는 클래스를 만들려면 __aiter__ (asynchorous iter) 와 __anext__ (asynchronous next) 메서드를 구현해야 한다. 그리고 메서드를 만들 때는 반드시 async def를 사용한다.   

다음은 1초마다 숫자를 생성하는 비동기 반복자이다.   

```python
import asyncio

class AsyncCounter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current < self.stop:
            await asyncio.sleep(1.0)
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration


async def main():
    async for i in AsyncCounter(3):
        print(i, end=' ')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


# 결과
0 1 2
```

메서드가 __anext__, __aiter__라는 점만 다를 뿐 일반적인 이터레이터와 만드는 방법은 같다. 반복을 끝낼 때는 StopAsyncIteration 예외를 발생시키면 된다. 물론 네이티브 코루틴을 사용할 때는 앞에 await를 붙인다. 비동기 이터레이터를 다 만들었다면 네이티브 코루틴 안에서 async for i in AsynCounter(3) 와 같이 async for에 사용하면 된다.   

## 제네레이터 방식으로 비동기 이터레이터 만들기

yield를 사용하여 제네레이터 방식으로 비동기 이터레이터를 만들 수도 있다. 다음과 같이 async def로 네이티브 코루틴을 만들고 yield를 사용하여 값을 바깥으로 전달하면 된다.   

```python
import asyncio

# 제네레이터 방식으로 만들기
async def async_counter(stop):
    n = 0
    while n < stop:
        yield n
        n += 1
        await asyncio.sleep(1.0)


async def main():
    async for i in async_counter(3):
        print(i, end=' ')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


# 결과
0 1 2
```

## 비동기 표현식

async와 await를 사용하면 리스트, 딕셔너리, 세트, 제네레이터 표현식을 비동기 표현식으로 만들 수 있다.   

* 리스트: [변수 async for 변수 in 비동기이터레이터()]
* 딕셔너리: {키: 값 async for 키, 값 in 비동기이터레이터()}
* 세트: {변수 async for 변수 in 비동기이터레이터()}
* 제네레이터: (변수 async for 변수 in 비동기이터레이터())

```python
async def main():
    a = [i async for i in AsyncCounter(3)]
    print(a)
```

다음과 같이 표현식 안에서 await로 코루틴을 실행할 수도 있다. 여기서는 리스트 표현식을 예로 들었지만 딕셔너리, 세트, 제네레이터 표현식 안에서도 await를 사용할 수 있다.

* [await 코루틴함수() for 코루틴함수 in 코루틴함수리스트]

```python
async def async_one():
    return 1

async def main():
    coroutines = [async_one, async_one, async_one]
    a = [await co() for co in coroutines]
    print(a)    # [1, 1, 1]
```

다음과 같이 표현식 안에서 await로 코루틴을 실행할 수도 있다. 여기서는 리스트 표현식을 예로 들었지만 딕셔너리, 세트, 제네레이터 표현식 안에서도 await를 사용할 수 있다.   

* [await 코루틴함수() for 코루틴함수 in 코루틴함수리스트]

```python
async def async_one():
    return 1

async def main():
    coroutines = [async_one, async_one, async_one]
    a = [await co() for co in coroutines]
    print(a)    # [1, 1, 1]
```

asyncio는 내용이 방대하여 이것만으론 부족하다. 여기서는 asyncio의 기본 사용 방법만 소개했다. 좀 더 깊이 학습하려면 파이썬 공식 문서를 참고해야 한다.   

[asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)