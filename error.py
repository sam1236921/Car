# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.ADD = QtWidgets.QPushButton(self.widget)
        self.ADD.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(10)
        self.ADD.setFont(font)
        self.ADD.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ADD.setObjectName("ADD")
        self.verticalLayout.addWidget(self.ADD)
        self.DEL = QtWidgets.QPushButton(self.widget)
        self.DEL.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(10)
        self.DEL.setFont(font)
        self.DEL.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DEL.setObjectName("DEL")
        self.verticalLayout.addWidget(self.DEL)
        self.OK = QtWidgets.QPushButton(self.widget)
        self.OK.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(10)
        self.OK.setFont(font)
        self.OK.setObjectName("OK")
        self.verticalLayout.addWidget(self.OK)
        self.XX = QtWidgets.QPushButton(self.widget)
        self.XX.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(10)
        self.XX.setFont(font)
        self.XX.setFocusPolicy(QtCore.Qt.NoFocus)
        self.XX.setObjectName("XX")
        self.verticalLayout.addWidget(self.XX)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "錯誤原因"))
        self.ADD.setText(_translate("Dialog", "add"))
        self.DEL.setText(_translate("Dialog", "delete"))
        self.OK.setText(_translate("Dialog", "OK"))
        self.XX.setText(_translate("Dialog", "cancel"))
