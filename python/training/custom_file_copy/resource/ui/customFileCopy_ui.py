# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customFileCopy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow__filecopy(object):
    def setupUi(self, MainWindow__filecopy):
        if not MainWindow__filecopy.objectName():
            MainWindow__filecopy.setObjectName(u"MainWindow__filecopy")
        MainWindow__filecopy.resize(703, 501)
        self.centralwidget = QWidget(MainWindow__filecopy)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit__srcdir = QLineEdit(self.widget)
        self.lineEdit__srcdir.setObjectName(u"lineEdit__srcdir")

        self.horizontalLayout_2.addWidget(self.lineEdit__srcdir)

        self.toolButton__srcdir = QToolButton(self.widget)
        self.toolButton__srcdir.setObjectName(u"toolButton__srcdir")

        self.horizontalLayout_2.addWidget(self.toolButton__srcdir)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit__targetdir = QLineEdit(self.widget)
        self.lineEdit__targetdir.setObjectName(u"lineEdit__targetdir")

        self.horizontalLayout_3.addWidget(self.lineEdit__targetdir)

        self.toolButton__targetdir = QToolButton(self.widget)
        self.toolButton__targetdir.setObjectName(u"toolButton__targetdir")

        self.horizontalLayout_3.addWidget(self.toolButton__targetdir)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton__start = QPushButton(self.widget)
        self.pushButton__start.setObjectName(u"pushButton__start")

        self.horizontalLayout.addWidget(self.pushButton__start)

        self.pushButton__pause = QPushButton(self.widget)
        self.pushButton__pause.setObjectName(u"pushButton__pause")

        self.horizontalLayout.addWidget(self.pushButton__pause)

        self.pushButton__stop = QPushButton(self.widget)
        self.pushButton__stop.setObjectName(u"pushButton__stop")

        self.horizontalLayout.addWidget(self.pushButton__stop)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textBrowser__debug = QTextBrowser(self.widget)
        self.textBrowser__debug.setObjectName(u"textBrowser__debug")

        self.verticalLayout.addWidget(self.textBrowser__debug)

        self.splitter.addWidget(self.widget)
        self.listWidget = QListWidget(self.splitter)
        self.listWidget.setObjectName(u"listWidget")
        self.splitter.addWidget(self.listWidget)

        self.verticalLayout_2.addWidget(self.splitter)

        MainWindow__filecopy.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow__filecopy)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 703, 20))
        MainWindow__filecopy.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow__filecopy)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow__filecopy.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow__filecopy)

        QMetaObject.connectSlotsByName(MainWindow__filecopy)
    # setupUi

    def retranslateUi(self, MainWindow__filecopy):
        MainWindow__filecopy.setWindowTitle(QCoreApplication.translate("MainWindow__filecopy", u"Custom File Copy", None))
        self.toolButton__srcdir.setText(QCoreApplication.translate("MainWindow__filecopy", u"...", None))
        self.toolButton__targetdir.setText(QCoreApplication.translate("MainWindow__filecopy", u"...", None))
        self.pushButton__start.setText(QCoreApplication.translate("MainWindow__filecopy", u"Start", None))
        self.pushButton__pause.setText(QCoreApplication.translate("MainWindow__filecopy", u"Pause", None))
        self.pushButton__stop.setText(QCoreApplication.translate("MainWindow__filecopy", u"Stop", None))
    # retranslateUi

