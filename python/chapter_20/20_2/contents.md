# 20-2. QListView, QTableView, QTreeView

> 변경 사항을 모델에 알리려면 "self.model.layoutChanged.emit()" 를 사용해 모델의 layoutChanged 시그널을 트리거해야 한다.

## QListView

QListView는 1차원 배열 데이터를 표시하는 위젯이다.

```python
import sys

from PySide2 import QtWidgets, QtGui, QtCore


class ListModel(QtCore.QAbstractListModel):
    def __init__(self, data):
        super().__init__()
        self.__data = data

    def data(self, index, role=...):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            return self.__data[index.row()]

    def rowCount(self, parent=...):
        return len(self.__data)

    def headerData(self, section, orientation, role=...):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return 'data'


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.view = QtWidgets.QTableView()

        self.model = ListModel(list(range(15)))

        self.view.setModel(self.model)
        self.setCentralWidget(self.view)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

## QTableView

QTableView는 엑셀과 같은 테이블 뷰로 데이터를 표시하는 위젯이다.

```python
import sys

from PySide2 import QtWidgets, QtGui, QtCore


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.__data = data

    def data(self, index, role=...):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            return self.__data[index.row()][index.column()]

    def rowCount(self, parent=...):
        return len(self.__data)

    def columnCount(self, parent=...):
        return len(self.__data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.view = QtWidgets.QTableView()

        data = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
        ]

        self.model = TableModel(data)

        self.view.setModel(self.model)
        self.setCentralWidget(self.view)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

## QTreeView

to be continue...
