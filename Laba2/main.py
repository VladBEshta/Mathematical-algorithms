import sys
from gui import *

import rect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIntValidator


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.MyFunction)
        self.ui.pushButton_2.clicked.connect(self.MyEXP)

    def MyFunction(self):
        try:
            a = float(self.ui.textEdit.toPlainText())
            b = float(self.ui.textEdit_2.toPlainText())
            n = float(self.ui.textEdit_3.toPlainText())
            self.ui.plainTextEdit.setPlainText("")
            S = rect.rec(a,b,n)
            self.ui.textEdit_4.setPlainText(str(S))

        except ValueError:
            self.ui.plainTextEdit.setPlainText("Input numbers")

    def MyEXP(self):
        try:
            p = float(self.ui.textEdit_7.toPlainText())
            self.ui.plainTextEdit.setPlainText("")
            k = rect.eshka(p)
            self.ui.textEdit_6.setPlainText(str(k))


        except ValueError:
            self.ui.plainTextEdit.setPlainText("Input numbers")


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
