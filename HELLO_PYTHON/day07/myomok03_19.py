import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.Qt import QLabel
import win32api

form_class = uic.loadUiType("./myomok03_19.ui")[0]


class WindowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.flag_wb = True
        self.flag_over = False
        self.arr2d = [
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0]
        ]
        
        self.pb2d = []
        self.setupUi(self)
        
        for i in range(19):
            line = []
            for j in range(19):
                piece = QPushButton('', self)
                piece.setIcon(QtGui.QIcon('0.png'))
                piece.setIconSize(QtCore.QSize(40,40))
                piece.setGeometry(QtCore.QRect(j*40, i*40, 40, 40))
                piece.setToolTip("{},{}".format(i,j))
                piece.clicked.connect(self.btnClick)
                line.append(piece)
            self.pb2d.append(line);
            
        self.pb.clicked.connect(self.myreset)
        
        self.myrender()
        
    def myreset(self):
        self.flag_wb = True
        self.flag_over = False
        
        for i in range(19):
            for j in range(19):
                self.arr2d[i][j] = 0
        self.myrender()
        
    def myrender(self):
        for i in range(19):
            for j in range(19):
                # if self.arr2d[i][j] == 0:
                #     self.pb2d[i][j].setIcon(QtGui.QIcon('0.png'))
                # if self.arr2d[i][j] == 1:
                #     self.pb2d[i][j].setIcon(QtGui.QIcon('1.png'))
                # if self.arr2d[i][j] == 2:
                #     self.pb2d[i][j].setIcon(QtGui.QIcon('2.png'))
                
                self.pb2d[i][j].setIcon(QtGui.QIcon(f"{self.arr2d[i][j]}.png"))
                
    def getUP(self, i , j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def getDW(self, i , j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0: # i > 0 이걸로 바까줘도됨?
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    def getLE(self, i , j, stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getRI(self, i , j, stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    def getUL(self, i , j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    def getUR(self, i , j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    def getDL(self, i , j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    def getDR(self, i , j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def btnClick(self):
        
        if self.flag_over == True:
            return
        
        str_ij = self.sender().toolTip()
        
        arr_ij = str_ij.split(',')
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2d[i][j] > 0:
            return
        
        stone = -1
        if self.flag_wb:
            self.arr2d[i][j] = 1
            stone = 1
        else:
            self.arr2d[i][j] = 2
            stone = 2
        self.flag_wb = not self.flag_wb
        
        up = self.getUP(i, j, stone)
        dw = self.getDW(i, j, stone)
        le = self.getLE(i, j, stone)
        ri = self.getRI(i, j, stone)
        ul = self.getUL(i, j, stone)
        ur = self.getUR(i, j, stone)
        dl = self.getDL(i, j, stone)
        dr = self.getDR(i, j, stone)
        
        d1 = ul + dr + 1
        d2 = up + dw + 1
        d3 = ur + dl + 1
        d4 = le + ri + 1
        
        # flag(전역변수) 로 비교 해주는게 좋음- 전역변수니께!!
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            
            if self.flag_wb:
                QMessageBox.about(self,'오목',"흑돌승리")
            else:
                QMessageBox.about(self,'오목',"백돌승리")
            
            self.flag_over = True
            
            # if stone == 1:
            #     win32api.MessageBox(0, "백돌승리", "title", 16)
            #     QMessageBox.about(self,'오목',"백돌승리")
            # elif stone == 2:
            #     win32api.MessageBox(0, "흑돌승리", "title", 16)
            #     QMessageBox.about(self,'오목',"흑돌승리")
        
        
        # print("up", up)
        # print("dw", dw)
        # print("le", le)
        # print("ri", ri)
        # print("ul", ul)
        # print("ur", ur)
        # print("dl", dl)
        # print("dr", dr)
        self.myrender()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()