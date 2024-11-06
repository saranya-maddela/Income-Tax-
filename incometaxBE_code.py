from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from incometaxFE import *

class Saranya(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.tax)
        self.ui.pushButton_2.clicked.connect(self.reset)
        self.ui.pushButton_3.clicked.connect(self.exit)
    def exit(self):
        sys.exit()
    def reset(self):
        self.ui.enter.clear()
        self.ui.label_2.clear()
    def tax(self):
        income=float(self.ui.enter.text())
        tax=0
        if income>=700000:
            if 0<income<=300000:
                tax=0
            elif 300000<income<=600000:
                tax=0+300000*0.05
            elif 600000<income<=900000:
                tax=0+300000*0.05+(income-600000)*0.1
            elif 900000<income<=1200000:
                tax=0+300000*0.05+300000*0.1+(income-900000)*0.15
            elif 1200000<income<=1500000:
                tax=0+300000*0.05+300000*0.1+300000*0.2+(income-1500000)*0.3
        self.ui.label_2.setText("Payable Tax = {}".format(tax))


if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Saranya()
    w.show()
    sys.exit(app.exec_())
