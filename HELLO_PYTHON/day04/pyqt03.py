import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./pyqt03.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        num1 = self.te1.toPlainText()
        num2 = self.te2.toPlainText()
        
        result = int(num1) * int(num2)
        self.te3.setText(str(result))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()