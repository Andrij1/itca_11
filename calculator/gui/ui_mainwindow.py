# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(364, 382)
        MainWindow.setMinimumSize(QSize(150, 310))
        MainWindow.setMaximumSize(QSize(364, 382))
        MainWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Display = QLineEdit(self.centralwidget)
        self.Display.setObjectName(u"Display")
        font = QFont()
        font.setPointSize(20)
        self.Display.setFont(font)
        self.Display.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Display.setReadOnly(True)

        self.verticalLayout.addWidget(self.Display)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.BTN_11 = QPushButton(self.centralwidget)
        self.BTN_11.setObjectName(u"BTN_11")
        self.BTN_11.setFont(font)

        self.gridLayout.addWidget(self.BTN_11, 0, 2, 1, 1)

        self.BTN_7 = QPushButton(self.centralwidget)
        self.BTN_7.setObjectName(u"BTN_7")
        self.BTN_7.setFont(font)

        self.gridLayout.addWidget(self.BTN_7, 4, 0, 1, 1)

        self.BTN_12 = QPushButton(self.centralwidget)
        self.BTN_12.setObjectName(u"BTN_12")
        self.BTN_12.setFont(font)

        self.gridLayout.addWidget(self.BTN_12, 0, 3, 1, 1)

        self.BTN_14 = QPushButton(self.centralwidget)
        self.BTN_14.setObjectName(u"BTN_14")
        self.BTN_14.setFont(font)

        self.gridLayout.addWidget(self.BTN_14, 3, 3, 1, 1)

        self.BTN_3 = QPushButton(self.centralwidget)
        self.BTN_3.setObjectName(u"BTN_3")
        self.BTN_3.setFont(font)

        self.gridLayout.addWidget(self.BTN_3, 2, 2, 1, 1)

        self.BTN_8 = QPushButton(self.centralwidget)
        self.BTN_8.setObjectName(u"BTN_8")
        self.BTN_8.setFont(font)

        self.gridLayout.addWidget(self.BTN_8, 4, 1, 1, 1)

        self.BTN_5 = QPushButton(self.centralwidget)
        self.BTN_5.setObjectName(u"BTN_5")
        self.BTN_5.setFont(font)

        self.gridLayout.addWidget(self.BTN_5, 3, 1, 1, 1)

        self.BTN_C = QPushButton(self.centralwidget)
        self.BTN_C.setObjectName(u"BTN_C")
        font1 = QFont()
        font1.setPointSize(14)
        self.BTN_C.setFont(font1)

        self.gridLayout.addWidget(self.BTN_C, 5, 0, 1, 1)

        self.BTN_2 = QPushButton(self.centralwidget)
        self.BTN_2.setObjectName(u"BTN_2")
        self.BTN_2.setFont(font)

        self.gridLayout.addWidget(self.BTN_2, 2, 1, 1, 1)

        self.BTN_10 = QPushButton(self.centralwidget)
        self.BTN_10.setObjectName(u"BTN_10")
        self.BTN_10.setFont(font)

        self.gridLayout.addWidget(self.BTN_10, 0, 1, 1, 1)

        self.BTN_6 = QPushButton(self.centralwidget)
        self.BTN_6.setObjectName(u"BTN_6")
        self.BTN_6.setFont(font)

        self.gridLayout.addWidget(self.BTN_6, 3, 2, 1, 1)

        self.BTN_0 = QPushButton(self.centralwidget)
        self.BTN_0.setObjectName(u"BTN_0")
        self.BTN_0.setFont(font)

        self.gridLayout.addWidget(self.BTN_0, 5, 1, 1, 1)

        self.BTN_X = QPushButton(self.centralwidget)
        self.BTN_X.setObjectName(u"BTN_X")
        self.BTN_X.setFont(font)

        self.gridLayout.addWidget(self.BTN_X, 0, 0, 1, 1)

        self.BTN_PT = QPushButton(self.centralwidget)
        self.BTN_PT.setObjectName(u"BTN_PT")
        self.BTN_PT.setFont(font)

        self.gridLayout.addWidget(self.BTN_PT, 5, 2, 1, 1)

        self.BTN_4 = QPushButton(self.centralwidget)
        self.BTN_4.setObjectName(u"BTN_4")
        self.BTN_4.setFont(font)

        self.gridLayout.addWidget(self.BTN_4, 3, 0, 1, 1)

        self.BTN_9 = QPushButton(self.centralwidget)
        self.BTN_9.setObjectName(u"BTN_9")
        self.BTN_9.setFont(font)

        self.gridLayout.addWidget(self.BTN_9, 4, 2, 1, 1)

        self.BTN_15 = QPushButton(self.centralwidget)
        self.BTN_15.setObjectName(u"BTN_15")
        self.BTN_15.setFont(font)

        self.gridLayout.addWidget(self.BTN_15, 4, 3, 1, 1)

        self.BTN_1 = QPushButton(self.centralwidget)
        self.BTN_1.setObjectName(u"BTN_1")
        self.BTN_1.setFont(font)

        self.gridLayout.addWidget(self.BTN_1, 2, 0, 1, 1)

        self.BTN_13 = QPushButton(self.centralwidget)
        self.BTN_13.setObjectName(u"BTN_13")
        self.BTN_13.setFont(font)

        self.gridLayout.addWidget(self.BTN_13, 2, 3, 1, 1)

        self.BTN_16 = QPushButton(self.centralwidget)
        self.BTN_16.setObjectName(u"BTN_16")
        self.BTN_16.setFont(font)

        self.gridLayout.addWidget(self.BTN_16, 5, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 364, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CALCULATOR", None))
        self.Display.setText("")
        self.BTN_11.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.BTN_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.BTN_12.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.BTN_14.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.BTN_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.BTN_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.BTN_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.BTN_C.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.BTN_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.BTN_10.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.BTN_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.BTN_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BTN_X.setText(QCoreApplication.translate("MainWindow", u"\u232b", None))
        self.BTN_PT.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.BTN_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.BTN_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.BTN_15.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.BTN_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.BTN_13.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.BTN_16.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

