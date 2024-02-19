# ToDo List 제작

## UI 구성

- UI 제작

|객체 이름|타입|설명|
|:---:|:---:|:---:|
|todo_view|QListView|현재 할 일 리스트|
|todo_edit|QLineEdit|새로운 할 일 리스트를 위한 텍스트 입력|
|add_button|QPushButton|할 일 리스트에 추가되는 새로운 할 일 생성|
|delete_button|QPushButton|현재 선택된 할 일을 삭제하고 할 일 리스트에서 제거|
|complete_button|QPushButton|현재 선택된 할 일을 완료 표시|

## 모델

Qt는 리스트, 트리, 테이블을 포함한 다양한 모델 기반을 제공한다. 다음 예에서는 결과를 QListView에 표시한다. 이에 대해 일치하는
기본 모델은 "QAbstractListModel"이다. 모델의 개요 정의는 다음과 같다.

```python
class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super(TodoModel, self).__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text

    def rowCount(self, index):
        return len(self.todos)
```

.todos 변수는 데이터 저장소이다. rowCount()와 data() 메서드는 리스트 모델에 대해 구현해야 하는 표준 모델 메서드이다.

전체 코드

```python
import json
import sys


from PySide2 import QtWidgets, QtGui, QtCore


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role=...):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text

        if role == QtCore.Qt.DecorationRole:
            status, text = self.todos[index.row()]
            if status:
                return QtGui.QPixmap()

    def rowCount(self, parent=...):
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # layout
        self.vbox_layout = QtWidgets.QVBoxLayout()
        hbox_btns_layout = QtWidgets.QHBoxLayout()
        # widgets
        self.add_btn = QtWidgets.QPushButton('add')
        self.del_btn = QtWidgets.QPushButton('delete')
        self.compl_btn = QtWidgets.QPushButton('complete')
        self.todo_edit = QtWidgets.QLineEdit()

        self.view = QtWidgets.QListView()
        self.model = TodoModel()
        self.load()

        self.view.setModel(self.model)

        # set layout
        self.vbox_layout.addWidget(self.view)
        hbox_btns_layout.addWidget(self.del_btn)
        hbox_btns_layout.addWidget(self.compl_btn)
        self.vbox_layout.addLayout(hbox_btns_layout)
        self.vbox_layout.addWidget(self.todo_edit)
        self.vbox_layout.addWidget(self.add_btn)

        widget = QtWidgets.QWidget(self)
        widget.setLayout(self.vbox_layout)

        self.setCentralWidget(widget)

        #
        self.add_btn.pressed.connect(self.add)
        self.del_btn.pressed.connect(self.delete)
        self.compl_btn.pressed.connect(self.complete)

    def add(self):
        text = self.todo_edit.text()
        if text:
            self.model.todos.append((False, text))
            # 새로 고침 트리거
            self.model.layoutChanged.emit()
            self.todo_edit.clear()
            self.save()

    def delete(self):
        indexes = self.view.selectedIndexes()
        if indexes:
            index = indexes[0]

            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.view.clearSelection()
            self.save()

    def complete(self):
        indexes = self.view.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.dataChanged.emit(index, index)
            self.view.clearSelection()
            self.save()

    def load(self):
        try:
            with open('data.json', 'r') as fp:
                self.model.todos = json.load(fp)
        except Exception:
            pass

    def save(self):
        with open('data.json', 'w') as fp:
            data = json.dump(self.model.todos, fp)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
```