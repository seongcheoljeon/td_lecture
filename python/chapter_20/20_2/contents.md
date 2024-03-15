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

GUI프로그래밍에서 계층적 데이터를 표시해야 하는 경우 `QTreeView`가 제격이다. `QTreeView`는 윈도우 파일 탐색기에서 볼 수 있는 폴더 구조와
같은 `계층적 데이터`를 보여줄 때 사용된다.

```python
from PySide6 import QtWidgets, QtGui, QtCore


class TreeViewExample(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 600)
        self.setAnimated(True)
        self.__rootdir = QtCore.QDir('/home/seongcheoljeon')
        self.setup_ui()

    def setup_ui(self):
        # 파일 시스템 모델 생성
        self.__model = QtWidgets.QFileSystemModel()
        self.__model.setRootPath(self.__rootdir.path())  # 루트 경로 설정

        # 트리 뷰 생성 및 설정
        tree_view = QtWidgets.QTreeView()
        tree_view.setModel(self.__model)
        tree_view.doubleClicked.connect(self.__openfile)

        # 루트 경로를 트리 뷰에 설정
        root_index = self.__model.index(self.__rootdir.path())
        tree_view.setRootIndex(root_index)

        # 메인 윈도우에 트리 뷰 추가
        self.setCentralWidget(tree_view)

    def __openfile(self, index: QtCore.QModelIndex):
        print(index)
        if not self.__model.isDir(index):
            model_idx = self.__model.index(index.row(), 0, index.parent())
            fpath = self.__model.filePath(model_idx)
            print(fpath)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = TreeViewExample()
    window.show()
    app.exec()
```

## QTreeWidget의 예는 다음과 같다.

```python
from PySide2 import QtWidgets, QtGui, QtCore


data = {
    "asset1": [["smoke", "NSS"], ["fire", "NSS"], ["water", "CSS"]],
    "asset2": [["dest", "TDD"], ["expl", "ZXX"]],
    "asset3": [["sand", "RND"], ["bomb", "ZQQ"]],
}


class MainWindow(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setColumnCount(2)
        self.setHeaderLabels(["Name", "Project"])

        items = list()

        for key, val in data.items():
            item = QtWidgets.QTreeWidgetItem([key])
            for v in val:
                child = QtWidgets.QTreeWidgetItem([v[0], v[1]])
                item.addChild(child)
            items.append(item)

        self.insertTopLevelItems(0, items)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    m = MainWindow()
    m.show()
    app.exec_()
```