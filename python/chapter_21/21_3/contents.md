# 21-3. 스레드 풀 (QRunnable, QThreadPool, ...)

## QThread와 QRunnable의 차이점

+ __사용 목적__
  + QThread
    + 개발자가 스레드를 직접 생성하고 제어하기 위한 클래스
    + 스레드의 시작, 종료 등을 직접 관리
  + QRunnable
    + 스레드에서 실행할 작업을 표현하는 인터페이스
    + ThreadPool과 함께 사용되는 구조이며 QThreadPool에 추가된 QRunnable은 풀에 있는 스레드 중 하나에 의해 실행됨
+ __Inheritance Structure__
  + QThread
    + QThread 클래스를 상속하여 새로운 스레드를 생성하고 해당 스레드에서 실행할 작업을 정의
    + `run()` 메서드를 override하여 실행할 작업을 정의
  + QRunnable
    + QRunnable은 추상 클래스이며, 실행할 작업을 정의하기 위해 이를 상속해야 한다.
    + `run()` 메서드를 구현하여 실행할 작업을 정의
+ __스레드 생성 방법__
  + QThread
    + QThread를 인스턴스화하고 `start()` 메서드를 호출하여 스레드 시작
  + QRunnable
    + QRunnable은 `QThreadPool`에 추가도니 후에 스레드 풀에서 실행
+ __리소스 관리__
  + QThread
    + QThread를 개발자가 직접 생성하면 해당 스레드에 대한 자원을 직접 관리해야 하며, 스레드가 더 이상 필요치 않은 경우 명시적으로 종료 및 자원 해제를 해주어야 한다.
  + QRunnable
    + QRunnable은 QThreadPool에 추가도니 후에 스레드 풀에서 관리된다. 
    + 스레드 풀은 스레드의 생성 및 소멸을 관리하므로 개발자가 직접 스레드 리소스를 관리할 필요가 없다.

* __QThread의 장점__
  * 직관적인 스레드 제어
    * 개발자가 스레드의 life-cycle을 직접 제어할 수 있다.
  * 상속을 통한 쉬운 확장
    * 새로운 스레드 동작을 정의하기 위해 `QThread`를 상속하고 `run()` 메서드를 재정의하는 것이 간단하다.
  * 스레드 간 통신
    * Qt의 Signal & Slot 메커니즘을 사용하여 스레드 간 통신이 쉽다.
* __QRunnable의 장점__
  * 리소스 효율성
    * 스레드 풀을 사용하여 스레드 생성 및 관리를 효율적으로 한다.
  * 확장성
    * 스레드 풀에서 실행되므로 시스템의 스레드 제한에 맞춰 자동으로 조절된다.
  * 작업 분배
    * 여러 작업을 스레드 풀에 추가하면 자동으로 분배되므로, 병렬 처리를 위한 효율적인 방법을 제공한다.

+ __QThread를 사용해야 하는 상황__
  + __작업 수행 시간이 긴 경우__
    + 작업 수행 시간이 길 경우, 해당 작업이 완료될 때까지 스레드가 `블로킹`되는 것이 일반적이다. 이는 `QThread`를 사용하여 작업을 수행할 때 자연스레 발생하는 동작이다.
    + 스레드가 블로킹되면 다른 스레드로의 전환이 발생하고, 이는 애플리케이션이 응답성을 유지하는 데 도움이 된다.
  + __직관적인 스레드 제어__
    + 스레드의 라이프사이클을 직접 제어할 수 있으므로 작업이 시작되고 완료될 때 추가 작업을 쉽게 도입할 수 있다.
  + __스레드 생성 및 관리 오버헤드__
    + QThread를 사용하면 개별적인 스레드 객체가 생성되고 제거된다. 작업 수행 시간이 길 경우에는 이러한 오버헤드가 비교적 작으며, 스레드 생성 및 관리의 부담이 크지 않다.

* __QRunnable은 작업 수행 시간이 짧을 때만 사용해야 하나?__
  * 그렇지는 않다! 하지만 QRunnable의 장점을 완전히 활용하기 어려울 수 있다. 왜냐하면, 작업 수행 시간이 긴 경우 작업이 완료될 때까지 스레드가 블로킹되는 문제가 발생할 수 있기 때문이다.

---

* QRunnable
  * 작업의 컨테이너
* QThreadPool
  * 작업 스레드의 관리자

> `QRunnable`은 실행할 작업을 나타내는 인터페이스이고, `QThreadPool`은 이러한 작업을 관리하고 실행하는 스레드 풀을 제공한다.   
> 따라서 `QRunnable`은 실행할 작업을 정의하고, `QThreadPool`은 이러한 작업을 관리하고 병렬로 실행한다.

## QRunnable

사용자 정의 QRunnable을 정의하려면 기본 QRunnable 클래스를 서브클래싱한 다음 실행하려는 코드를 run() 메서드 내에 배치할 수 있다.

```python
class Worker(QRunnable):
    # worker threads...

    def run(self):
        # work code...
        print('thread start')

        time.sleep(5)
        print('thread complete')
```

다른 스레드에서 함수를 실행하는 것은 단순히 Worker 인스턴스를 생성한 다음 이를 QThreadPool 인스턴스에 전달하면 자동으로 실행된다.

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.threadpool = QThreadPool()

        print('maximum {0} threads'.format(self.threadpool.maxThreadCount()))
```

마지막으로 run_thread 메서드를 생성하고 풀에 넣는다.

```python
def run_thread(self):
    worker = Worker()
    self.threadpool.start(worker)
```

전체 코드는 다음과 같다.

```python
import time
from PySide2 import QtWidgets, QtGui, QtCore


class Worker(QtCore.QRunnable):
    def __init__(self):
        super().__init__()

    def run(self):
        print('thread start')

        time.sleep(5)
        print('thread complete')


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #
        self.central_widget = QtWidgets.QWidget()
        vlayout = QtWidgets.QVBoxLayout()
        btn = QtWidgets.QPushButton('push button')
        vlayout.addWidget(btn)
        self.central_widget.setLayout(vlayout)
        self.setCentralWidget(self.central_widget)
        #

        self.threadpool = QtCore.QThreadPool()
        # 명시적으로 스레드 개수 제한. 
        # self.threadpool.setMaxThreadCount(3)

        btn.clicked.connect(self.run_thread)

        print('maximum {0} threads'.format(self.threadpool.maxThreadCount()))

    def run_thread(self):
        worker = Worker()
        self.threadpool.start(worker)

        
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec_()
```

해당 UI의 PushButton을 여러 번 누르면 `.maxThreadCount`에 의해 보고 된 개수까지 스레드가 즉시 실행되는 것을 볼 수 있다. 이미 이 개수의
활성 워커가 있는 상태에서 버튼을 다시 누르면 스레드를 사용할 수 있을 때까지 후속 워커가 대기열에 추가된다.

위의 코드는 QThreadPool이 사용할 이상적인 스레드 수를 결정하였다. 이 숫자는 컴퓨터마다 다르며 최적의 성능을 얻도록 설계되어 있다. 그러나 
때때로 특정 개수의 스레드가 필요한 경우가 있다. 이 경우 `.setMaxThreadCount`를 사용해 이 값을 명시적으로 설정할 수 있다. 이 값은 스레드 
풀마다의 값이다.

### 시그널 & 슬롯을 이용한 예제

```python
import time
import sys
import random

from PySide2 import QtWidgets, QtGui, QtCore


class WorkerSignals(QtCore.QObject):
    # 데이터 없음
    finished = QtCore.Signal()
    # 문자열
    error = QtCore.Signal(str)
    # 딕셔너리
    result = QtCore.Signal(dict)


class Worker(QtCore.QRunnable):
    def __init__(self, iterations=5):
        super().__init__()

        self.signals = WorkerSignals()
        self.iterations = iterations

    def run(self):
        # self.args, self.kwargs로 러너 함수 초기화
        try:
            res = 0
            n = 0
            while n < self.iterations:
                time.sleep(0.01)
                res = 2 / (30 - n)
                n += 1
        except Exception as err:
            self.signals.error.emit(str(err))

        else:
            self.signals.finished.emit()
            self.signals.result.emit({'number': n, 'value': res})


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #
        self.central_widget = QtWidgets.QWidget()
        vlayout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel()
        btn = QtWidgets.QPushButton('push button')
        vlayout.addWidget(self.label)
        vlayout.addWidget(btn)
        self.central_widget.setLayout(vlayout)
        self.setCentralWidget(self.central_widget)

        self.counter = 0

        self.threadpool = QtCore.QThreadPool()

        btn.clicked.connect(self.run_thread)

        print('maximum {0} threads'.format(self.threadpool.maxThreadCount()))

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.set_timer_str)
        self.timer.start()

    def run_thread(self):
        worker = Worker(iterations=random.randint(10, 50))
        worker.signals.result.connect(self.worker_output)
        worker.signals.finished.connect(self.worker_complete)
        worker.signals.error.connect(self.worker_error)
        self.threadpool.start(worker)

    def worker_output(self, s):
        print('result: ', s)

    def worker_complete(self):
        print('thread complete!')

    def worker_error(self, t):
        print('error: ', t)

    def any_work(self):
        print('thread start')
        time.sleep(5)
        print('thread complete')

    def set_timer_str(self):
        self.counter += 1
        self.label.setText('counter: {}'.format(self.counter))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec_()

```

위의 코드는 스레드의 완료 알림 뿐만 아니라 에러가 발생하면 해당 메시지를 받을 수 있도록 설계했다.

---

### Progress Watcher

스레드를 사용해 오래 실행되는 작업을 수행하는 경우, 사용자에게 작업 진행 상황을 알려야 한다. 이를 수행하는 일반적인 방법은 사용자에게 
프로그래스바를 보여줘 작업이 얼마나 완료됐는지를 나타내는 것이다. 프로그래스바를 보여주려면 워커에서 현재 진행 상태를 내보내야 한다.

```python
import time

from PySide2 import QtWidgets, QtGui, QtCore


class WorkerSignals(QtCore.QObject):
    progress = QtCore.Signal(int)

    
class Worker(QtCore.QRunnable):
    def __init__(self):
        super().__init__()

        self.signals = WorkerSignals()

    def run(self):
        total = 1000

        for i in range(total):
            progress_val = int(i / (total - 1) * 100)
            self.signals.progress.emit(progress_val)
            time.sleep(0.01)

            
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #
        self.central_widget = QtWidgets.QWidget()
        vlayout = QtWidgets.QVBoxLayout()
        self.progress = QtWidgets.QProgressBar()
        btn = QtWidgets.QPushButton('start button')
        vlayout.addWidget(self.progress)
        vlayout.addWidget(btn)
        self.central_widget.setLayout(vlayout)
        self.setCentralWidget(self.central_widget)

        self.threadpool = QtCore.QThreadPool()
        print('maximum thread: {0}'.format(self.threadpool.maxThreadCount()))

        btn.pressed.connect(self.execute)

    def execute(self):
        worker = Worker()
        worker.signals.progress.connect(self.update_progress)
        self.threadpool.start(worker)

    @QtCore.Slot(int)
    def update_progress(self, progress):
        self.progress.setValue(progress)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec_()
```

다른 러너가 이미 작업 중일 때 버튼을 누르면 문제가 발생한다. 두 러너가 진행률을 동일한 프로그레스바로 내보내므로 값이 앞뒤로 점프한다.

단일 프로그래스바로 여러 워커를 추적하는 것이 가능하다. 두 가지만 있으면 된다. 
1. 각 워커의 진행률 값을 저장할 위치
2. 각 워커의 고유 식별자이다.

각각의 진행률 업데이트에서 모든 워커의 평균 진행률을 계산하고 표시할 수 있다.

```python
import time
import uuid
import random

from PySide2 import QtWidgets, QtGui, QtCore


class WorkerSignals(QtCore.QObject):
    progress = QtCore.Signal(str, int)
    finishded = QtCore.Signal(str)
    

class Worker(QtCore.QRunnable):
    def __init__(self):
        super().__init__()

        # 고유 식별 hex 값 생성
        self.job_id = uuid.uuid4().hex
        self.signals = WorkerSignals()

    def run(self):
        total = 1000
        # 임의의 지연 값
        delay = random.random() / 100

        for i in range(total):
            progress_val = int(i / (total - 1) * 100)
            self.signals.progress.emit(self.job_id, progress_val)
            time.sleep(delay)

        self.signals.finishded.emit(self.job_id)

        
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #
        self.central_widget = QtWidgets.QWidget()
        vlayout = QtWidgets.QVBoxLayout()
        self.progress = QtWidgets.QProgressBar()
        btn = QtWidgets.QPushButton('start button')
        self.lbl_status = QtWidgets.QLabel('0 workers')
        vlayout.addWidget(self.lbl_status)
        vlayout.addWidget(self.progress)
        vlayout.addWidget(btn)
        self.central_widget.setLayout(vlayout)
        self.setCentralWidget(self.central_widget)

        # 현재 워커의 진행률을 딕셔너리에 저장
        self.worker_progress = dict()

        self.threadpool = QtCore.QThreadPool()
        print('maximum thread: {0}'.format(self.threadpool.maxThreadCount()))

        btn.pressed.connect(self.execute)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.refresh_progress)
        self.timer.start()

    def cleanup(self, job_id):
        if job_id in self.worker_progress:
            del self.worker_progress[job_id]
        self.refresh_progress()

    def refresh_progress(self):
        progress = self.calulate_progress()
        print(self.worker_progress)
        self.progress.setValue(progress)
        self.lbl_status.setText(f'{len(self.worker_progress)} workers')

    def calulate_progress(self):
        if not self.worker_progress:
            return 0
        return sum(v for v in self.worker_progress.values()) / len(self.worker_progress)

    def execute(self):
        worker = Worker()
        worker.signals.progress.connect(self.update_progress)
        worker.signals.finishded.connect(self.cleanup)
        # 실행
        self.threadpool.start(worker)

    @QtCore.Slot(str, int)
    def update_progress(self, job_id, progress):
        self.worker_progress[job_id] = progress

        
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec_()
```

위의 코드에서는 각 워커의 대한 식별자로 [UUID4](https://docs.python.org/ko/3/library/uuid.html) 식별자를 사용하였다.

위의 코드를 실행하여 여러개의 워커를 생성 후 프로그레스바를 보면, 아직까지도 프로그레스바의 상태가 앞뒤로 이동하는 것을 볼 수 있다. 그 이유는
작업이 완료되는 시점에 워커를 즉시 제거하기 때문이다. 즉, 평균 계산에서 100을 제거하면 평균 값이 떨어지게 되므로 이것을 수정해야 한다.

해결책은 다음과 같다.

__모든 프로그레스바가 100에 도달할 때만 항목을 제거한다.__

```python
def cleanup(self):
    if all(v >= 100 for v in self.worker_progress.values()):
        self.worker_progress.clear()
    self.refresh_progress()
```

### 스레드를 이용한 PyQtGraph

해당 코드는 각 워커에 대한 데이터가 별로도 유지되고 개별적으로 플롯에 그리는 코드이다. 각 워커는 서로 다른 속도로 데이터를 생성한다.

```python
import time
import uuid
import random

from PySide2 import QtWidgets, QtGui, QtCore

import pyqtgraph


class WorkerSignals(QtCore.QObject):
    data = QtCore.Signal(tuple)


class Worker(QtCore.QRunnable):
    def __init__(self):
        super().__init__()

        # 고유 식별 hex 값 생성
        self.worker_id = uuid.uuid4().hex
        self.signals = WorkerSignals()

    def run(self):
        total = 1000
        y2 = random.randint(0, 10)
        # 임의의 지연 값
        delay = random.random() / 100
        value = 0

        for i in range(total):
            y = random.randint(0, 10)
            value += i * y2 - i * y

            self.signals.data.emit((self.worker_id, i, value))
            time.sleep(delay)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.threadpool = QtCore.QThreadPool()

        self.x = dict()
        self.y = dict()
        self.lines = dict()

        layout = QtWidgets.QVBoxLayout()
        self.graph_widget = pyqtgraph.PlotWidget()
        self.graph_widget.setBackground('w')
        layout.addWidget(self.graph_widget)

        btn = QtWidgets.QPushButton('create new worker')
        btn.pressed.connect(self.execute)

        layout.addWidget(btn)

        w = QtWidgets.QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

    def execute(self):
        worker = Worker()
        worker.signals.data.connect(self.receive_data)

        self.threadpool.start(worker)

    def receive_data(self, data):
        worker_id, x, y = data

        if worker_id not in self.lines:
            self.x[worker_id] = [x]
            self.y[worker_id] = [y]

            # random color
            pen = pyqtgraph.mkPen(
                width=2,
                color=(
                    random.randint(100, 255),
                    random.randint(100, 255),
                    random.randint(100, 255),
                ),
            )
            self.lines[worker_id] = self.graph_widget.plot(self.x[worker_id], self.y[worker_id], pen=pen)
            return

        self.x[worker_id].append(x)
        self.y[worker_id].append(y)

        self.lines[worker_id].setData(self.x[worker_id], self.y[worker_id])

        
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec_()
```

시스템에서 사용 가능한 최대 스레드까지 새 워커를 시작할 수 있다. 100개의 값을 생성한 후 워커는 종료되고 다음 대기열 워커가 시작돼 값을 새 줄로 추가한다.

### 실행 중인 QRunnable 정지

__QRunnable을 시작하면 기본적으로 중지할 수 있는 방법이 없다.__ 만약 사용자가 실수로 작업을 시작하면 앉아서 완료될 때까지 기다려야 한다.
러너를 죽일 수 있는 방법은 없지만, 멈추게 요청할 수는 있다. 다음의 예는 플래그를 사용해 러너가 중지해야 함을 알리는 방법이다.

> 컴퓨팅에서 플래그(flag)는 현재 또는 상태 변경을 알리는 데 사용되는 변수다. 선박이 깃발을 사용해 서로 통신하는 방법이라고 생각하면 된다.

다음 코드는 0.01초마다 증가하는 프로그레스바와 Stop 버튼이 있는 간단한 러너이다. Stop을 클릭하면 워커가 종료되고 프로그레스바를 영구적으로 중지한다.

```python
import time

from PySide2 import QtWidgets, QtGui, QtCore


class WorkerKilledException(Exception):
    pass


class WorkerSignals(QtCore.QObject):
    progress = QtCore.Signal(int)


class JobRunner(QtCore.QRunnable):
    signals = WorkerSignals()

    def __init__(self):
        super().__init__()

        self.is_killed = False

    def run(self):
        try:
            for i in range(100):
                JobRunner.signals.progress.emit(i + 1)
                time.sleep(0.1)

                if self.is_killed:
                    raise WorkerKilledException
        except WorkerKilledException:
            pass

    def kill(self):
        self.is_killed = True


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        w = QtWidgets.QWidget()
        hbox = QtWidgets.QHBoxLayout()
        w.setLayout(hbox)

        btn_stop = QtWidgets.QPushButton('Stop')

        hbox.addWidget(btn_stop)

        self.setCentralWidget(w)

        self.status = self.statusBar()
        self.progress = QtWidgets.QProgressBar()
        self.status.addPermanentWidget(self.progress)

        self.threadpool = QtCore.QThreadPool()

        self.runner = JobRunner()
        self.runner.signals.progress.connect(self.slot_update_progress)
        self.threadpool.start(self.runner)

        btn_stop.pressed.connect(self.runner.kill)

    def slot_update_progress(self, progress):
        self.progress.setValue(progress)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec_()
```

* 러너를 죽여야 하는지 여부를 나타내는 플래그는 `is_kill`이다.
* 각 루프에서 `is_killed`가 `True`인지 여부를 테스트해 예외를 던진다.
* 예외를 포착하면 여기서 완료 또는 에러 시그널을 내보낸다.
* `kill()` 메서드를 구현하여 `worker.kill()`을 호출해 종료할 수 있다.

위의 예에서는 단일 워커만 있다. 그러나 많은 애플리케이션에서는 스레드를 더 많이 사용할 수 있다. *__여러 러너가 실행 중일 때 워커 중지를 
어떻게 처리해야 할까?__*

중지가 모든 워커를 중지하게 하려면, 위의 코드를 아무것도 바꾸지 않아도 된다. 모든 워커를 동일한 `Stop` 시그널에 연결하고 해당 시그널이 발생하면 
모든 워커가 중지될 것이다.

개별 워커를 중지할 수 있으려면 각 러너에 대해 UI 어디간에 별도의 버튼을 생성하거나 워커를 추적하고 죽이는 더 나은 인터페이스를 제공하는 관리자를
구현해야 한다.







