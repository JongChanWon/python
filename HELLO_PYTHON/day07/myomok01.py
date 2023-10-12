import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.Qt import QLabel

form_class = uic.loadUiType("./myomok01.ui")[0]


class WindowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.flag_wb = True
        
        self.setupUi(self)
        
        for i in range(10):
            for j in range(10):
                piece = QPushButton('', self)
                piece.setIcon(QtGui.QIcon('0.png'))
                piece.setIconSize(QtCore.QSize(40,40))
                piece.setGeometry(QtCore.QRect(i*40, j*40, 40, 40))
                piece.clicked.connect(self.btnClick)
    
    def btnClick(self):
        
        if self.flag_wb: 
            self.sender().setIcon(QtGui.QIcon('1.png'))
        else:
            self.sender().setIcon(QtGui.QIcon('2.png'))
        self.flag_wb = not self.flag_wb
        
        # self.pb.setIcon(QtGui.QIcon('1.png'))
        # print(self.sender())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()