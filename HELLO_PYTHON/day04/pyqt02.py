import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./pyqt02.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        print(self)
        
        txt = self.le.text()
        print(txt)
        num = int(txt)
        num -= 1
        txt2 = str(num)
        self.le.setText(txt2)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()