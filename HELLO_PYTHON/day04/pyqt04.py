import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("./pyqt04.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
    
    
    def btnClick(self):
        
        for i in range(1000):
            rnd = (int)(random * 45)
            a = 0
            
            # self.pt1.setPlainText(str(arr[0]))
            # self.pt1.setPlainText(str(arr[1]))
            # self.pt1.setPlainText(str(arr[2]))
            # self.pt1.setPlainText(str(arr[3]))
            # self.pt1.setPlainText(str(arr[4]))
            # self.pt1.setPlainText(str(arr[5]))
            
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()