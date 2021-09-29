

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(385, 523)
        Dialog.setStyleSheet("background-color: black;\n"
"")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 100, 231, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 170, 231, 51))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 250, 231, 51))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Mostrar-Hora"))
        self.pushButton_2.setText(_translate("Dialog", "Mostrar-Mes"))
        self.pushButton_3.setText(_translate("Dialog", "Mostrar-Ano"))
