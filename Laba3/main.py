import sys
import numpy as np
from gui import *

import Eiler
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIntValidator


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.MyFunction)

    def MyFunction(self):
        try:
            a = float(self.ui.textEdit.toPlainText())
            b = float(self.ui.textEdit_2.toPlainText())
            h = float(self.ui.textEdit_3.toPlainText())
            yo = float(self.ui.textEdit_5.toPlainText())
            if (a < b) and (h!=0):
                self.ui.plainTextEdit.setPlainText("")
                dy = Eiler.backwardEuler('myFunc', np.array([yo]),np.array([a, b]),h)
                self.ui.textEdit_4.setPlainText(str(dy))
            else:
                self.ui.textEdit_4.setPlainText(str(0))
        except ValueError:
            self.ui.plainTextEdit.setPlainText("Input numbers")



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
