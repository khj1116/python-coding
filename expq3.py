from PyQt5.QtWidgets import *
from PyQt5 import uic #사용자인터페이스클레스
import sys


form_class = uic.loadUiType('expq3.ui')[0]
#form_class = uic.loaduiType(r'C:\MYPRO\PYQT\test\expq3.ui')[0]

class windowClass(QMainWindow, form_class):   
    def __init__(self):
        super().__init__()  #괄호 빠트리지 않기
        self.setupUi(self)
        self.rb1.clicked.connect(self.func) 
        self.rb2.clicked.connect(self.func) 
        self.rb3.clicked.connect(self.func) 
        self.rb4.clicked.connect(self.func)
        self.c = 0
    def func(self):
        if self.rb1.isChecked():    #버튼이 선택되었는지
            print('plus')
        elif self.rb2.isChecked():
            print("subtract")
        elif self.rb3.isChecked():
            print("multiply")
        elif self.rb4.isChecked():
            print("divide")
        
       
#----------------------------------------------------------------------    
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)    #응용객체생성
    my = windowClass()      #메인 클래스 호출
    my.show()
    app.exec_()             #이벤트가 발생할 때마다 실행