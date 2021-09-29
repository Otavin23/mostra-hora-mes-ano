import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from date import Ui_Dialog
from datehora import Ui_MainWindow
from mostrarano import Ui_MainWindow
from mostrarmes import Ui_MainWindow


class Principal(QDialog):

    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #Botoes
        self.ui.pushButton.clicked.connect(self.botao_hora)
        self.ui.pushButton_2.clicked.connect(self.botao_mes)
        self.ui.pushButton_3.clicked.connect(self.botao_mostrar_ano)

    def botao_mes(self):
        self.tela_mes = Mostrar_mes()
        self.tela_mes.show()
        self.close()

    def botao_hora(self):
        self.tela_hora = Telahora()
        self.tela_hora.show()
        self.close()

    def botao_mostrar_ano(self):
        self.tela_ano = TelaAno()
        self.tela_ano.show()
        self.close()

class Mostrar_mes(QMainWindow):
    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #botoes
        self.ui.pushButton.clicked.connect(self.botao_mes)

    def botao_mes(self):
        return self.mostrar_mes()

    def mostrar_mes(self):
        import datetime

        tudo = time.localtime()
        print(tudo)
        mes = tudo[1]
        texto = self.ui.label.text()
        if mes == 1:
            texto = self.ui.label.text()
            texto = self.ui.label.setText("          {} JANEIRO".format(mes))
        elif mes == 2:
            texto = self.ui.label.text()
            texto = self.ui.label.setText("          {} FEVEREIRO".format(mes))
        elif mes == 3:
            texto = self.ui.label.text()
            texto = self.ui.label.setText("          {}  MARÇO".format(mes))
        elif mes == 4:
            texto = self.ui.label.text()
            texto = self.ui.label.setText("          {} ABRIL".format(mes))
        elif mes == 5:
            texto = self.ui.label.text()
            texto = self.ui.label.setText("          {} MAIO".format(mes))
        elif mes == 6:
            texto = self.ui.label.text()
            texto = self.ui.label.setText("          {} JUNHO".format(mes))
        elif mes == 7:
            texto = self.ui.label.text()
            texto = self.ui.label.setText("          {} JULHO".format(mes))
        elif mes == 8:
            texto = self.ui.label.text()
            texto = self.ui.label.setText("          {} AGOSTO".format(mes))
        elif mes == 9:
            texto = self.ui.label.text()
            texto = self.ui.label.setText("          {} SETEMBRO".format(mes))
        elif mes == 10:
            texto = self.ui.label.text()
            texto = self.ui.label.setText("          {} OUTUBRO".format(mes))
        elif mes == 11:
            texto = self.ui.label.text()
            texto = self.ui.label.setText("          {} NOVEMBRO".format(mes))
        elif mes == 12:
            texto = self.ui.label.text()
            texto = self.ui.label.setText("          {} DEZEMBRO".format(mes))

class TelaAno(QMainWindow):

    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #botoes
        self.ui.pushButton.clicked.connect(self.botao)

    def botao(self):
        return self.mostrar_ano()

    def mostrar_ano(self):
        import datetime

        tudo = time.localtime()
        print(tudo)
        ano = tudo[0]
        texto = self.ui.label.text()
        texto = self.ui.label.setText("                {}".format(ano))


class Telahora(QMainWindow):
    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Botoa_iniciar
        self.ui.pushButton.clicked.connect(self.mostrar_hora)


    def mostrar_hora(self):
        return self.horass()

    def horass(self):
        import datetime
        tudo = time.localtime()
        hora = tudo[3]
        minuto = tudo[4]
        texto = self.ui.label.text()
        texto = self.ui.label.setText("                {}:{}".format(hora,minuto))

if __name__ == "__main__":
    import os, sys
    app = QApplication(sys.argv)
    window = Principal()
    window.show()
    sys.exit(app.exec_())