from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys


form_class = uic.loadUiType('expq1.ui')[0]


class windowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.bt1func) #pb1버튼이름, bt1func 실행할 함수 이름
        self.pb2.clicked.connect(self.bt2func) #pb2버튼이름, bt2func 실행할 함수 이름
    
#----------------------------------------------------------------------    
    def bt1func(self):
        print('1번을 누름')
        
    def bt2func(self):
        print('2번을 누름')

#----------------------------------------------------------------------    
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)    #응용객체생성
    myWindow = windowClass()
    myWindow.show()
    app.exec_()
        