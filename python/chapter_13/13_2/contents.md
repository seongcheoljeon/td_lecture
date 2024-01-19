# 프로세스(process) & 스레드(thread)

## 멀티 프로세스(multiprocess)
* 프로세스를 스레드처럼 관리

* multiprocess 모듈은 threading API에 기반을 두고 여러 프로세스 간 작업을 나누는 API를 제공.    
* multiprocess 모듈은 threading 대신 사용해 멀티 코어 CPU의 장점을 누리고 파이썬의 글로벌 인터프리터 락의 병목현상을 피하게 할 수 있다.

multiprocessing 모듈은 threading 모듈과 비슷한 API를 가지고 있는 process 기반의 병렬처리 알고리즘이다 python은 Global Interpreter Lock 
을 이용하여 병행처리 과정에서 발생할 수 있는 문제를 방지한다.    
GIL 은 간단한 구현 때문에 계속 사용되어 있지만, CPU 하나만을 사용하는 것을 가정하였기 때문에 현재 처럼 CPU 안에 코어가 여러개 있다고 하더라도, 
실제로 병렬처리 되지 않고 한번의 하나의 thread 밖에 처리하지 않는다.    
multiprocessing 모듈은 이러한 문제를 회피하기 위해 process 기반으로 병렬처리를 지원하는 모듈이다.

멀티프로세싱 기본두 번째 프로세스를 생성하기 가장 쉬운 방법은 Process 객체를 인스턴스화하며, 목표 함수를 전달하고 start를 호출하는 것이다.

```python
import multiprocessing as multi

def worker():
    print('worker')
    return

jobs = []
for i in range(5):
    p = multi.Process(target=worker)
    jobs.append(p)
    p.start()

''' 결과
worker
worker
worker
worker
worker
'''
```

단어worker가 다섯 번 출력되지만, 각 프로세스가 출력 스트림에 접근하기 위해 경쟁하기 때문에 실행 순서에 따라 결과물이 완전히 깨끗하지 않을 수 있다.

대부분 프로세스를 생성할 때 어떤 작업을 수행해야하는지 인자에 명시하는 편이 더 유용하다. threading 과는 다르게 multiprocessing Process에 
인자를 전달하려면 인자는 pickle을 사용해 직렬화할 수 있어야 한다.

이 예제는 각 워커 프로세스에 출력할 숫자를 전달한다.

```python
import multiprocessing as multi

def worker(num):
    print('worker', num)
    return

jobs = []
for i in range(5):
    p = multi.Process(target=worker, args=(i,))
    jobs.append(p)
    p.start()

'''결과
worker 0
worker 1
worker 2
worker 3
worker 4
'''
```

### 현재 프로세스 판별

인자를 사용해 프로세스를 구별하거나 이름을 붙이는 방식은 번거롭고 필요치도 않다. 각 Process 인스턴스는 기본 값으로 이름이 있고 생성될 때 변경할 수 있다.   
프로세스에 이름을 붙이면 추적하기 쉬워지고, 여러 프로세스가 동시에 실행되는 애플리케이션에서 특히 유용하다.

```python
import time
import multiprocessing as multi


def worker():
    name = multi.current_process().name
    print(name, 'starting')
    time.sleep(2)
    print(name, 'exiting')

def my_service():
    name = multi.current_process().name
    print(name, 'starting')
    time.sleep(3)
    print(name, 'exiting')


service = multi.Process(name='my_service', target=my_service)
worker_1 = multi.Process(name='worker-1', target=worker)
worker_2 = multi.Process(target=worker)

worker_1.start()
worker_2.start()
service.start()

'''결과
worker-1 starting
Process-3 starting
my_service starting
worker-1 exiting
Process-3 exiting
my_service exiting
'''
```

디버그 출력의 각 줄마다 현재 프로세스의 이름이 포함돼 있다. Process-3 이 붙어있는 줄은 이름이 없는 프로세스 worker_1에 대응한다.

### 데몬 프로세스

메인 프로그램은 기본적으로 모든 자식이 종료될 때까지 끝나지 않는다. 하지만 프로세스를 간섭하기 쉬운 방법이 없는 서비스나, 작업 도중에 죽어도 데이터를 
잃거나 훼손하지 않는 프로그램의 경우엔 메인 프로그램이 종료되는 것을 막지 않고 백그라운드에서 실행되는 프로세스가 필요하기도 하다.   
프로세스를 데몬으로 지정하려면 daemon 속성을 True로 설정한다. 기본 값은 데몬이 되지 않게 설정돼 있다.

```python
import sys
import time
import multiprocessing as multi


def daemon():
    p = multi.current_process()
    print('starting:', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('exiting:', p.name, p.pid)
    sys.stdout.flush()

def non_daemon():
    p = multi.current_process()
    print('starting:', p.name, p.pid)
    sys.stdout.flush()
    print('exiting:', p.name, p.pid)
    sys.stdout.flush()


d = multi.Process(name='daemon', target=daemon)
d.daemon = True

n = multi.Process(name='non-daemon', target=non_daemon)
n.daemon = False

d.start()
time.sleep(1)
n.start()

'''결과
starting: daemon 140454
starting: non-daemon 140457
exiting: non-daemon 140457
'''
```

프로그램을 실행하면 데몬 프로세스에게 'exiting' 메시지가 출력되지 않는데, 이는 데몬 프로세스가 2초간 잠들었다가 깨어나기 전에 모든 넌데몬 non-daemon 
프로세스(메인 프로그램 포함) 가 종료되기 때문이다.

데몬 프로세스는 메인 프로그램이 끝나기 전에 자동으로 종료돼 고아가 되는 것을 방지한다.   
데몬 프로세스가 남아있지 않은지는 실행 중인 프로세스 아이디를 화면에 출력하는 ps 같은 명령어로 확인 할 수 있다.

### 프로세스간 객체 전달

multiprocessing느 프로세스간에 객체를 전달하기 위한 두 가지 방법을 제공한다.

#### Queue

<pre>
Queue클래스는 Queue.Queue와 비슷하다.
</pre>

```python
import multiprocessing as multi


def f(q):
    q.put([55, None, 'hello', 'world'])


q = multi.Queue()
p = multi.Process(target=f, args=(q,))
p.start()
print(q.get())
p.join()

'''결과
[55, None, 'hello', 'world']
'''
```

#### 프로세스 각각의 ID를 보여주는 예제

```python
import os
import multiprocessing as multi


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print(name)


info('main line')
p = (multi.Process(target=f, args=('bob',)) for i in range(3))

for th in p:
    th.start()

for th in p:
    th.join()

'''결과
main line
module name: __main__
parent process: 127760
process id: 141125
function f
module name: __main__
parent process: 141125
process id: 141160
bob
function f
module name: __main__
parent process: 141125
process id: 141161
bob
function f
module name: __main__
parent process: 141125
process id: 141162
bob
'''
```
