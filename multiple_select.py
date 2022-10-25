# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiple_select.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("NDVI selection")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 10, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 60, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 110, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 210, 111, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 260, 111, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 261, 281))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 160, 111, 31))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NDVI selection"))
        self.pushButton.setText(_translate("Dialog", "Select all"))
        self.pushButton_2.setText(_translate("Dialog", "Clear selection"))
        self.pushButton_3.setText(_translate("Dialog", "Add files"))
        self.pushButton_4.setText(_translate("Dialog", "Ok"))
        self.pushButton_5.setText(_translate("Dialog", "Cancel"))
        self.pushButton_6.setText(_translate("Dialog", "Remove file"))

