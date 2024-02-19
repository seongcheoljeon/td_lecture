# 20-3. Qt 모델에서 SQL 데이터베이스 쿼리

[QtSql 공식 문서](https://doc.qt.io/qtforpython-6/PySide6/QtSql/QSqlDatabase.html)

## 데이터베이스 연결

서버기반의 DB(PostgreSQL, MySQL, MariaDB 등)와 파일 기반(SQLite) 데이터베이스는 모두 Qt에서 지원하며 설정 방법만 다르다.

```python
from PySide2 import QtSql

db = QtSql.QSqlDatabase('QMYSQL')
db.setHostName('127.0.0.1')
db.setDatabaseName('dummy_db')
db.setUserName('root')
db.setPassword('')

ok = db.open()
```

## QSQlTableModel로 테이블 표시

```python
model = QSqlTableModel(db=db)
model.setTable('<table name>')
model.select()
```
.select() 메서드로 데이터를 불러들인다. 즉 .select()를 호출해 모델에 데이터베이스를 쿼리하고 결과를 보여줄 준비가 된 상태로 유지한다.   
이 데이터를 QTableView에 표시하려면 .setModel() 메서드에 전달하기만 하면 된다.

```python
table = QTableView()
table.setModel(self.model)
```

전체 코드

```python
from PySide2 import QtWidgets, QtGui, QtCore, QtSql

db = QtSql.QSqlDatabase('QMYSQL')
db.setHostName('127.0.0.1')
db.setDatabaseName('dummy_db')
db.setUserName('root')
db.setPassword('')

ok = db.open()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.view = QtWidgets.QTableView()
        self.model = QtSql.QSqlTableModel(db=db)
        
        self.view.setModel(self.model)
        self.model.setTable('<table name>')
        # 열 인덱스로 데이터 정렬
        self.model.setSort(2, QtCore.Qt.SortOrder.DescendingOrder)
        self.model.select()
        
        self.setMinimumSize(QtCore.QSize(1024, 720))
        self.setCentralWidget(self.view)
```

### 데이터 편집

QTableView에 표시된 데이터베이스 데이터는 기본적으로 편집할 수 있다. 변경 사항은 편집을 마친 직후 데이터베이스에 다시 유지된다.

Qt는 편집 동작에 대해 일부 제어를 제공하며, 앱 유형에 따라 변경할 수 있다.

|계획|설명|
|---|---|
|QSqlTableModel.EditStrategy.OnFieldChange|사용자가 편집된 셀의 선택을 취소하면 변경 사항이 자동으로 적용된다.|
|QSqlTableModel.EditStrategy.OnRowChange|사용자가 다른 행을 선택하면 변경 사항이 자동으로 적용된다.|
|QSqlTableModel.EditStrategy.OnManualSubmit|변경 사항은 모델에 캐시되고 .submitAll()이 호출될 때에만 데이터베이스에 기록되거나 revertAll()이 호출될 때 삭제된다.|

.setEditStrategy를 호출해 모델에 대한 현재 편집 전략을 설정할 수 있다. 예를 들면 다음과 같다.
> self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnRowChange)

### 열 정렬

열 이름을 사용해 테이블 정렬

```python
self.model.setTable('<table name>')
idx = self.model.fieldIndex('name')
self.model.setSort(idx, QtCore.Qt.SortOrder.DescendingOrder)
self.model.select()
```



