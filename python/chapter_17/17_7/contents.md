# QFileDialog

```python
from PySide6 import QtWidgets, QtGui, QtCore


FILE_FILTERS = [
    'Houdini files (*.hip)',
    'Text files (*.txt)',
    'All files (*)',
]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('My Application')

        layout = QtWidgets.QVBoxLayout()

        button1 = QtWidgets.QPushButton('Open file')
        button1.clicked.connect(self.get_filename)

    @staticmethod
    def get_filename():
        caption = 'Open file'
        initial_dir = ''
        initial_filter = FILE_FILTERS[3]

        dialog = QtWidgets.QFileDialog()
        dialog.setWindowTitle(caption)
        dialog.setDirectory(initial_dir)
        dialog.setNameFilters(FILE_FILTERS)
        dialog.selectNameFilter(initial_filter)
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)

        ok = dialog.exec()

        print('result: ', ok, dialog.selectedFiles(), dialog.selectedNameFilter())

    @staticmethod
    def get_filenames():
        caption = 'Open files'
        initial_dir = ''
        initial_filter = FILE_FILTERS[1]

        dialog = QtWidgets.QFileDialog()
        dialog.setWindowTitle(caption)
        dialog.setDirectory(initial_dir)
        dialog.setNameFilters(FILE_FILTERS)
        dialog.selectNameFilter(initial_filter)
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)

        ok = dialog.exec()

        print('result: ', ok, dialog.selectedFiles(), dialog.selectedNameFilter())

...
```

## [Qt Help](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QFileDialog.html)
