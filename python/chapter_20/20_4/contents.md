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

to be continue...

