# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc01\Desktop\mainwindow_2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usernumEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernumEdit.setGeometry(QtCore.QRect(20, 20, 591, 51))
        self.usernumEdit.setObjectName("usernumEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 113, 20))
        self.lineEdit.setMouseTracking(False)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(142, 79, 141, 31))
        self.nameEdit.setObjectName("nameEdit")
        self.textEdit_chat = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_chat.setGeometry(QtCore.QRect(20, 160, 581, 391))
        self.textEdit_chat.setObjectName("textEdit_chat")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 120, 113, 20))
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.changeEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.changeEdit.setGeometry(QtCore.QRect(140, 120, 181, 31))
        self.changeEdit.setObjectName("changeEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEdit.setGeometry(QtCore.QRect(302, 79, 141, 31))
        self.passwordEdit.setObjectName("passwordEdit")
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(460, 80, 131, 31))
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(460, 120, 131, 31))
        self.pushButton_update.setObjectName("pushButton_update")
        self.textEdit_send = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_send.setGeometry(QtCore.QRect(20, 570, 581, 51))
        self.textEdit_send.setObjectName("textEdit_send")
        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setGeometry(QtCore.QRect(20, 630, 581, 31))
        self.pushButton_send.setObjectName("pushButton_send")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "Nickname :"))
        self.lineEdit_3.setText(_translate("MainWindow", "Change password :"))
        self.pushButton_login.setText(_translate("MainWindow", "Login"))
        self.pushButton_update.setText(_translate("MainWindow", "Update password"))
        self.pushButton_send.setText(_translate("MainWindow", "Send"))

