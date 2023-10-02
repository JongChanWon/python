import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("./pyqt05.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
    
    
    def btnClick(self):
        # dan = self.le.text()
        # idan = int(dan)
        #
        # txt = ""
        # txt += "{} * {} = {}\n".format(idan,1,idan*1)
        # txt += "{} * {} = {}\n".format(idan,2,idan*2)
        # txt += "{} * {} = {}\n".format(idan,3,idan*3)
        # txt += "{} * {} = {}\n".format(idan,4,idan*4)
        # txt += "{} * {} = {}\n".format(idan,5,idan*5)
        # txt += "{} * {} = {}\n".format(idan,6,idan*6)
        # txt += "{} * {} = {}\n".format(idan,7,idan*7)
        # txt += "{} * {} = {}\n".format(idan,8,idan*8)
        # txt += "{} * {} = {}\n".format(idan,9,idan*9)
        # self.te.setText(txt)
        
        txt = self.le.text()
        num = int(txt)
        form = ""
            # 1 ~ 9까지 구구단의 형태로 form에 담기
        for i in range(1,10):
            # form += "%d * %d  = %d\n" %(num, i, num*i)
            form += f"{num} * {i} = {num*i}\n"
        # 텍스트 출력하기        
        # self.pte.setPlainText(form)
        self.te.setText(form)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()