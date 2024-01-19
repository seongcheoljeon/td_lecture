# QThread

QObject, QThread 예제

```python
import sys
import time

from PySide2 import QtWidgets, QtCore


class Worker(QtCore.QObject):
    progress = QtCore.Signal(int)
    completed = QtCore.Signal(int)

    @QtCore.Slot(int)
    def do_work(self, n):
        for i in range(1, n+1):
            time.sleep(1)
            self.progress.emit(i)

        self.completed.emit(i)


class MainWindow(QtWidgets.QMainWindow):
    work_requested = QtCore.Signal(int)

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setGeometry(200, 200, 400, 100)
        self.setWindowTitle('QThread Test')

        self.widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setValue(0)

        self.btn_start = QtWidgets.QPushButton('start', clicked=self.start)

        layout.addWidget(self.progress_bar)
        layout.addWidget(self.btn_start)

        self.worker = Worker()
        self.worker_thread = QtCore.QThread()

        self.worker.progress.connect(self.update_progress)
        self.worker.completed.connect(self.finished)

        self.work_requested.connect(self.worker.do_work)

        self.worker.moveToThread(self.worker_thread)

        self.worker_thread.start()

        self.show()

    def start(self):
        self.btn_start.setEnabled(False)
        n = 5
        self.progress_bar.setMaximum(n)
        self.work_requested.emit(n)

    def update_progress(self, v):
        self.progress_bar.setValue(v)

    def finished(self, v):
        self.progress_bar.setValue(v)
        self.btn_start.setEnabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
```