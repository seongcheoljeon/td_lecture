import sys

from PySide2 import QtWidgets, QtGui, QtCore

# import calcExpr


class CalcUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CalcUI, self).__init__(parent)

        self.__grid_layout = QtWidgets.QGridLayout(self)

        # create ui
        self.set_ui_numbers()

        self.setLayout(self.__grid_layout)

    def set_ui_numbers(self):
        for i in range(9):
            btn = QtWidgets.QPushButton(str(i))
            btn.clicked.connect(self.slot_clicked_btn)
            self.__grid_layout.addWidget(btn, int(i // 3), int(i % 3), alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

    @QtCore.Slot()
    def slot_clicked_btn(self):
        print(self.sender().text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    calc = CalcUI()
    calc.show()
    sys.exit(app.exec_())

