# 스레드 (Thread)

여기에서 설명할 모듈은 threading이다. 이 모듈은 thread 모듈의 고수준 인터페이스를 지니고 있다. 가벼운 프로세스(Lightweight Process)라고 
하기도 하는 쓰레드는 프로세스 안에서 실행되는 단위이다.

하나의 프로세스 안에 쓰레드는 여러 개 존재할 수 있다. 하나의 프로세스에 하나의 쓰레드만 존재한다면 싱글 쓰레드 프로세스(Single Thread Process) 이고, 
두 개 이상의 쓰레드가 존재한다면 멀티쓰레드 프로세스(Multithread Process) 라고 한다.

쓰레드는 하나의 프로세스 안에 있는 '작은 프로세스'라고 생각할 수 있다. 하나의 프로세스 안에 있는 쓰레드들은 각각 독립적인 스택을 가지고 수행되나, 
코드와 자료를 공유한다. 따라서 쓰레드 간에 자료를 공유, 교환하는 것이 (프로세스 간의 자원 공유에 비해서) 매우 쉽다. 

CPU가 하나이므로 쓰레드의 수행은 어느 시점에서라도 중단되고 다른 쓰레드로 실행권이 넘어갈 수 있다. 쓰레드의 수행은 독립적이어서 다른 쓰레드와의 실
행 순서에 관한 어떠한 가정도 할 수 없다.

> CPython 구현상의 세부사항: Global Interpreter Lock 때문에, 한 번에 하나의 쓰레드만이 실행된다. 따라서 멀티 프로세서에서 threading 
> 모듈을 사용했을 때 성능상의 이점은 전혀 없다. 병렬 프로그래밍으로 성능을 향상시키고 싶다면 multiprocessing 모듈을 사용해야 한다.   
> 하지만, 성능상의 이점이 없다고 해도 많은 I/O 처리가 동시에 필요할 때 threading 으로 해결할 수 있다.

## threading 모듈의 도구

+ __threading.activeCount()__
  + 현재 살아 있는 thread의 개수 반환.
+ __threading.currentThread()__
  + 현재 thread 객체를 반환.
+ __threading.enumerate()__
  + 현재 살아 있는 모든 thread 반환.
+ __threading.Condition()__
  + 새로운 condition variable 객체 반환. 
  + condition variable은 내부에 하나의 쓰레드 대기 큐(Queue)를 가진다. wait() 를 호출하는 쓰레드는 이 대기 큐에 넣어지고 대기(Sleep) 
  상태에 들어간다. notify()를 호출하는 쓰레드는 이 대기 큐에서 하나의 쓰레드를 깨운다.
+ __threading.Event()__
  + Event 객체는 네 개의 메소드를 가지고 있다. ( set(), clear(), wait(), isSet() ) Event 객체는 내부에 하나의 이벤트 플래그를 가진다. 
  초기 값은 0이다.set() 메소드는 내부 플래그를 1로 만들어 주고, clear() 메소드는 0으로 만든다.wait() 메소드는 내부 플래그가 1이면 즉시 리턴되며, 0이면 다른 스레드에 의해서 1이 될 때까지 블록(대기) 상태에 들어간다. wait()는 내부 플래그 값을 바꾸지 않는다.
+ __threading.Lock()__
  + lock 객체를 생성. 
  + 하나의 스레드가 정보를 갱신하는 동안 다른 스레드가 그 변수에 접근하지 못하도록 해야 할 때 쓰인다.
+ __threading.RLock()__
  + RLock 클래스 객체는 Lock 객체와 같으나, 락을 소유하고 있는 스레드가 두 번 이상 acquire와 release를 호출 할 수 있다. 
  acquire 한 만큼 release 해야 락이 해제된다.
+ __threading.Semaphore([value])__
  + semaphore 객체는 생성. 
  + 세마포어는 카운터로 관리한다. 카운터는 acquire() 메소드를 사용하면 -1 이 되고, release() 메소드를 
  사용하면 +1 이 된다. 만약, acquire()를 실행할 때 카운터 값이 0이면 스레드는 세마포 변수 대기 큐에 넣어져 
  블럭 상태(Block, 실행을 멈추고 어떤 사건이 일어나기를 대기하는 상태. CPU를 점유하지 않는다.) 로 들어간다.release() 는 우선 세마포 변수에 대기하고 있는 쓰레드가 있는지를 검사한다. 만일 스레드가 존재하면 그들 중 가장 오래 대기하고 있던 스레드 하나를 풀어 준다. 스레드가 대기 큐에 없으면 카운터 값을 단순히 1 증가한다.
+ __threading.BoundedSemaphore([value])__
  + bounded semaphore 객체를 생성. 
  + bounded semaphore 란 현재 값이 초기 값을 초과하지 않는지 검사하는 기능이 추가되어 있다. 초기 값을 초과할 경우 ValueError 예외가 
  발생한다. 제한된 자원을 관리할 때 사용된다.
+ __threading.local -> Class__
  + thread의 local data를 나타내는 class이다. 
  + thread local 데이터를 관리하기 위해서는 local로 인스턴스를 생성하면 된다.data = threading.local()data = 1스레드마다, 
  인스턴스의 값이 다르다.
+ __threading.Thread -> Class__
  + thread를 조작할 때 사용하는 클래스이다.
  + threading.Timer -> Class일정 시간 간격마다 스레드에서 특정 함수를 실행하도록 하기 위해 사용한다.
+ __threading.stack_size([size])__
  + 새로운 스레드를 생성했을 때 스레드의 스택 크기를 반환한다.

## Thread 객체

```python
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={})
```

키워드로 인자를 전달하는 Thread의 생성자

+ __group__
  + 반드시 None, 차후 확장을 고려한 것이다.
+ __target__
  + run() 메소드가 호출될 때 실행할 함수를 지정한다. 
  + 기본은 None이다.
+ __name__
  + thread의 이름을 뜻한다. 
  + 기본으로 'Thread-N' 형태로 지어진다.
+ __args__
  + target에 전달할 인자를 tuple형태로 받는다.
+ __kwargs__
  + target에 전달할 인자를 dictionary 형태로 받는다.
+ __subclass__
    + subclass를 만들 때 생성자를 override 하려면, Thread.init() 를 가장 먼저 실행하도록 해야 한다.

---

+ __start()__
  + thread를 시작한다.
  + thread마다 한번씩 실행해야 한다. 이 메소드는 run() 메소드를 실행하도록 해준다. 동일한 thread에 한번 이상 실행하면 RuntimeError 예외 발생.
+ __run()__
  + run() 메소드는 target 함수를 호출한다. override 가능.
+ __join([timeout])__
  + thread 가 종료할 때까지 기다린다. 
  + join() 메소드가 실행된 지점에서 thread가 종료할 때까지 기다린다.
  + 기본 timeout 인자는 None 이다. float point나 fraction 형으로 인자를 초 단위로 지정할 수 있다. 
  + join() 은 언제나 None 을 반환한다. 만약 join() 을 호출한 뒤 언제 timeout이 발생하는지 알고 싶다면, isAlive() 를 호출해야 한다. 
  + timeout이 지난 다음에 아직 thread가 살아 있다면 thread는 종료된다.join은 여러번 호출 될 수 있다.
  + 현재 thread가 deadlock을 유발하려고 하면 join()은 RuntimeError 를 발생시킨다. 또는 시작하지 않은 thread에서 join()을 호출해도 마찬가지 예외가 발생한다.
+ __name__
  + 이 문자열은 식별하기 위한 용도로만 사용하고 특별한 의미는 없다. 
  + 여러 thread가 같은 이름을 가져도 상관 없다. 초기 이름은 생성자에 의해 지정된다.
+ __ident__
  + 특정 thread의 식별자이다. 
  + thread가 시작하지 않았다면 None으로 되어 있지만 시작하면 0이 아닌 어떤 정수를 가진다. 
  + thread.get_ident() 함수로 읽어 올 수 있다. 새로운 thread가 생성되면 이미 종료된 thread의 ident 값이 재활용될 수 있다.
+ __isAlive()__
  + thread 가 살아 있는지 여부를 반환한다.
  + run() 메소드가 실행된 다음부터 run() 메소드가 종료되는 때까지 True 값을 반환한다. 
  + 모듈 함수 enumerate() 는 살아 있는 thread의 list를 반환한다.
+ __daemon__
  + 현재 thread가 daemon thread인지 아닌지 boolean 값으로 표시되어 있다. 
  + daemon 일 경우 True이다. 
  + start() 메소드가 실행되기 전에 지정되어야 하며, 그렇지 않다면 RuntimeError가 발생한다. 
  + 초기값을 부모 thread로 부터 상속 받는다. 따라서 기본으로 False로 되어 있다.
  + 모든 python 프로그램은 daemon이 아닌 thread가 모두 종료되면 종료된다. 
  + daemon인 thread는 계속 실행되는 상태에서 프로그램은 종료된다.

> 쓰레드를 생성하는 방법은 두 가지가 있다.
> > 1. 호출 가능한 객체(함수 등) 를 생성자에 직접 전달하는 방법
> > 2. 서브 클래스에서 run 메소드를 중복하는 방법

thread 객체가 생성되고 나면 start() 메소드를 실행해야 thread가 실행된다. start() 메소드는 각각의 thread에서 run() 메소드를 호출한다. 

thread 객체가 시작되면, thread는 'alive' 상태가 된다. 이것은 run() 메소드가 종료되거나 예외가 발생 했을 때 종료된다. is_alive() 메소드를 실행하여 살아 있는지 여부를 알 수 있다.

join() 메소드를 호출하여 thread 가 종료될 때까지 기다리도록 할 수 있다.

## 상호 배제 (mutual exclusion, Mutex)

멀티쓰레딩을 하면, 값을 갱신하는 중간에 연산이 다른 쓰레드로 교체되면서 바르지 못한 정보가 유지되지 못할 수 도 있다.

이 같은 문제점을 해결하려면 하나의 쓰레드가 정보를 갱신하는 동안 다른 쓰레드가 그 변수에 접근하지 못하도록 해야 한다. 
모듈 threading은 락(Lock) 객체를 지원한다.

락 객체는 다음의 세가지 메서드를 가진다.

+ __threading.Lock().acquire()__
  + 락을 얻는다. 
  + 일단 하나의 스레드가 락을 얻으면 다른 스레드는 락을 얻을 수 없다.
  + 락을 소유하고 있는 스레드가 release()를 호출할 때까지 대기한다.
  + 락이 해제되면 락을 얻는다.
+ __threading.Lock().release()__
  + 락을 해제한다.
  + 만일 acquire()로 해당 락을 기다리는 스레드가 있으면 그 스레드 중 하나만 락을 얻을 수 있다.
+ __threading.Lock().locked()__
  + 락을 얻었으면 1, 아니면 0을 리턴한다.

전형적인 사용 예

```python
# 전역 변수로 한 번만 lock을 얻는다.

# 여기서 얻어진 lock 객체는 모든 스레드가 공유해야 한다.
lock = threading.Lock()

# 각 스레드는 다음과 같은 코드를 수행한다.

# 락을 얻고 들어 간다. 이미 다른 스레드가 들어가 있으면 락을 얻을 때까지 여기서 자동적으로 대기한다.
lock.acquire()

# 필요한 코드를 수행한다. 상호 배제 영역 (Critical Section)
g_cnt += 1

# 락을 해제한다. 다른 스레드가 이 코드 영역으로 들어갈 수 있도록 허락한다.
lock.release()
```

이와 같인 상호 배타적으로 코드를 수행해야 할 영역을 __임계 영역(Critical Section)__ 이라고 한다.

이러한 상호 배제는 락 객체로 구현 가능하다.

```python
import threading

g_cnt = 0
lock = threading.Lock()
threads = list()

def counter(_id, count):
    global g_cnt

    for i in range(count):
        print(f'id: {_id} -> {i}')
        lock.acquire()
        g_cnt += 1
        lock.release()

for i in range(3):
    th = threading.Thread(target=counter, args=(i, 3))
    th.start()
    threads.append(th)

for th in threads:
    th.join()

print('-' * 100)
print(threads)
print('-' * 100)
print('total counter: ', g_cnt)
print('exit...')
```

위의 코드를 클래스로 작성하면 다음과 같다.

```python
import threading

g_cnt = 0
lock = threading.Lock()
threads = list()

class MyThread(threading.Thread):
    def run(self):
        global g_cnt

        for i in range(3):
            print(f' {i} ')
            lock.acquire()
            g_cnt += 1
            lock.release()

for i in range(3):
    th = MyThread()
    th.start()
    threads.append(th)

for th in threads:
    th.join()

print('-' * 100)
print(threads)
print('-' * 100)
print('total counter: ', g_cnt)
print('exit...')
```

## Semaphore 객체

세마포어는 가장 오랜된 동기화 프리미티브이다. 세마포어는 내부에 정수형의 카운터 변수를 가지고 있으며, 이 값은 세마포어 변수를 생성할 때 초기화된다.

acquire()에 의해 1씩 감소하고, release()에 의해 값이 1씩 증가한다. 카운터는 0보다 작은 값을 가질 수 없다.

### Semaphore 변수 활용 예

어떤 임계 영역이 있다고 하자. 이 영역에 단지 몇 개의 스레드만이 진입할 수 있도록 허용하고 싶다. 다음 예는 100개의 스레드가 어떤 코드를 500회 반복한다. 
반복하는 코드의 어떤 영역은 최대 3개의 스레드만이 진입할 수 있도록 허용한다.

```python
import threading

# 세마포어 객체 생성
sem = threading.Semaphore(3)

class RestrictedArea(threading.Thread):
    def run(self):
        for i in range(500):
            # before stuff
            sem.acquire()
            # do something...
            sem.release()
            # after stuff

th_lst = list()

# 100개의 스레드 생성
for i in range(100):
    th_lst.append(RestrictedArea())

for th in th_lst:
    th.start()

for th in th_lst:
    th.join()

print('exit...')
```

## Event 객체

Event 객체는 네 개의 메서드를 가지고 있다.

+ __set()__
  + 내부 플래그를 1로 만들어 준다.
+ __clear()__
  + 내부 플래그를 0으로 만든다.
+ __wait()__
  + 내부 플래그가 1이면 즉시 리턴
  + 내부 플래그가 0이면 다른 스레드에 의해서 1이 될 때까지 블록(대기) 상태에 들어간다. 
  + wait() 메서드는 내부 플래그 값을 바꾸지 않는다.
+ __isSet()__

### Event 변수 활용 예

두가지 종류의 스레드가 있다고 하자. 하나는 뭔가를 준비하는 스레드(T1) 이고, 나머지는 준비된 환경 하에서 수행하는 스레드이다. 
당연히 T1이 원하는 작업을 수행한 후에 나머지 다른 스레드가 진행되어야 할 것이다.

이때 Event 동기화를 이용하면 쉽게 문제가 해결된다.

```python
import threading

# Event 객체 생성
event = threading.Event()

class PrepareThread(threading.Thread):
    def run(self):
        event.set()
        print('ready!')

class ActionThread(threading.Thread):
    def run(self):
        # 앞에서 처리할 코드
        print(f'{self.getName()} waiting...')
        # PrepareThread가 준비를 마칠 때까지 대기
        event.wait()
        print(f'{self.getName()} done!')

th_lst = list()

for i in range(5):
    th_lst.append(ActionThread())

for th in th_lst:
    th.start()

PrepareThread().start()

for th in th_lst:
    th.join()
```

