from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys


form_class = uic.loadUiType('expq2.ui')[0]


class windowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.bt1func) #pb1버튼이름, bt1func 실행할 함수 이름
        self.pb2.clicked.connect(self.bt2func) #pb2버튼이름, bt2func 실행할 함수 이름
        self.pb3.clicked.connect(self.bt3func) #pb3버튼이름, bt3func 실행할 함수 이름
        self.c = 0
        
    
#----------------------------------------------------------------------    
    def bt1func(self):
        print('증가버튼을 누름')
        self.c = self.c + 1
        self.lb1.setText(f'Count : {self.c}')  #setText() 위젯이름.쓰기함수
        
    def bt3func(self):
        print('감소버튼을 누름')
        self.c = self.c - 1
        self.lb1.setText(f'Count : {self.c}')
        
    def bt2func(self):
        print('삭제버튼을 누름')
        self.c = 0
        self.lb1.setText(f'Count : {self.c}')           #clear() 위젯이름.지우는 함수
#----------------------------------------------------------------------    
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)    #응용객체생성
    myWindow = windowClass()
    myWindow.show()
    app.exec_()
        