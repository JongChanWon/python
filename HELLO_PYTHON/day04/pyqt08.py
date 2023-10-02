import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit

form_class = uic.loadUiType("./pyqt08.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def getStar(self, cnt):
        ret = ""
        for i in range(cnt):
            ret += "*"
        ret += "\n"
        return ret
        
    def btnClick(self):
        fStar = self.le_first.text()
        lStar = self.le_last.text()
        
        star1 = int(fStar)
        star2 = int(lStar)
        
        txt = ""
        for i in range(star1, star2 + 1):
            txt += self.getStar(i)
        self.te.setText(txt)
        
        # plainText 일때
        # QPlainTextEdit.setPlainText()
        # self.pte.setPlainText(txt)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()