# 코루틴(coroutine)

async/await 구문으로 선언된 코루틴은 비동기 애플리케이션을 작성하는 데 선호되는 방식이다.    
예를 들어, 다음 코드는 "hello"를 출력하고 1초간 기다린 다음 "world"를 출력한다.

```python
import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())
```

단지 코루틴을 호출하는 것으로 실행되도록 예약하는 것은 아니다.

```python
>>> main()
<coroutine object main at 0x00aab3432>
```

실제로 코루틴을 실행하기 위해 asyncio는 다음과 같은 메커니즘을 제공한다.

+ 최상위 진입점 “main()” 함수를 실행하는 [asyncio.run()](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.run) 함수 (위의 예제)
+ 코루틴을 기다리기. 다음 코드는 1초를 기다린 후 “hello”를 출력한 다음 또 2초를 기다린 후 “world”를 출력한다.

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```
<pre>
# 결과
started at 09:05:55
hello
world
finished at 09:05:58
</pre>

* 코루틴을 asyncio 태스크로 동시에 실행하는 [asyncio.create_task()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.create_task) 함수.

위의 예를 수정해서 두 개의 say_after 코루틴을 동시에 실행해 보자

```python
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
```
<pre>
# 결과 : 해당 코드는 1초 더 빠르게 실행되었음을 볼 수 있다.
started at 17:14:32
hello
world
finished at 17:14:34
</pre>

* [asyncio.TaskGroup](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.TaskGroup) 클래스는 
[create_task()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.create_task)에 대한 보다 현대적인 대안을 제공한다. 

<pre>
asyncio.TaskGroup은 Python3.11에 새롭게 추가되었다.
</pre>

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")
```
<pre>
# 결과 : 위의 코드와 동일한 결과
</pre>

## awaitable

객체가 [await](https://docs.python.org/ko/3/reference/expressions.html#await) 표현식에서 사용될 수 있을 때 어웨이터블 객체라고 말한다. 
많은 asyncio API는 awaitable를 받아들이도록 설계되었다.

> Unity 2023.1에서도 awaitable를 사용할 수 있다.
>> [Unity 2023.1에 Awaitable 클래스 도입](https://hackernoon.com/ko/Unity-20231%EC%97%90-Waitable-%ED%81%B4%EB%9E%98%EC%8A%A4%EA%B0%80-%EB%8F%84%EC%9E%85%EB%90%98%EC%97%88%EC%8A%B5%EB%8B%88%EB%8B%A4.)

어웨이터블 객체에는 세 가지 주요 유형이 있다: __코루틴, 태스크 및 퓨처__

#### 코루틴(Coroutine)

python coroutine은 awaitable이므로 다른 coroutine에서 기다릴 수 있다.

```python
import asyncio

async def nested():
    return 42

async def main():
    # 그냥 "nested()"를 호출하면 아무 일도 일어나지 않음.
    # 그 이유는, 코루틴 객체가 생성되지만 대기하지 않고 있기 때문이다. 따라서 전혀 실행되지 않는다.
    nested()

    # 아래는 42가 출력된다.
    print(await nested())

asyncio.run(main())
```

__impotant!__ “코루틴” 이라는 용어는 두 가지 밀접한 관련 개념에 사용될 수 있다.
+ 코루틴 함수: [async def 함수](https://docs.python.org/ko/3/reference/compound_stmts.html#async-def)
+ 코루틴 객체: 코루틴 함수를 호출하여 반환된 객체.

#### 태스크(Task)

태스크는 코루틴을 동시에 예약하는 데 사용된다.
코루틴이 [asyncio.create_task()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.create_task)와 같은 함수를 
사용하여 태스크로 감쌀 때 코루틴은 곧 실행되도록 자동으로 예약된다.

```python
import asyncio

async def nested():
    return 42

async def main():
    # nested()가 곧 동시에 실행되도록 예약한다.
    # "main()"과 함께.
    task = asyncio.create_task(nested())

    # 이제 "task"를 사용하여 "nested()"를 취소할 수 있고, 완료될 때까지 기다리기만 하면 된다.
    await task

asyncio.run(main())
```

#### 퓨처(Future)

[Future](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio.Future)는 비동기 연산의 최종 결과를 나타내는 
특별한 저수준 어웨이터블 객체이다. Future 객체를 기다릴 때, 그것은 코루틴이 Future가 다른 곳에서 해결될 때까지 기다릴 것을 뜻한다.   
콜백 기반 코드를 async/await와 함께 사용하려면 asyncio의 Future 객체가 필요하다. 일반적으로 응용 프로그램 수준 코드에서 Future 객체를 만들 필요는 없다.   
때때로 라이브러리와 일부 asyncio API에 의해 노출되는 Future 객체를 기다릴 수 있습니다.   

```python
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
```

Future 객체를 반환하는 저수준 함수의 좋은 예는 [loop.run_in_executor()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor)이다.
