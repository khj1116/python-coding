from PyQt5.QtWidgets import *
from PyQt5 import uic       #사용자인터페이스클레스
import sys


form_class = uic.loadUiType('expq4.ui')[0]
#form_class = uic.loaduiType(r'C:\MYPRO\PYQT\test\expq3.ui')[0]

class windowClass(QMainWindow, form_class):   
    def __init__(self):
        super().__init__()  #괄호 빠트리지 않기
        self.setupUi(self)
        self.pb1.clicked.connect(self.printText)  #1
        self.pb2.clicked.connect(self.inputText) #2
        self.pb3.clicked.connect(self.appendText) #3
        self.pb4.clicked.connect(self.clearText) #4
        self.a = 0
        self.count = 0    #변수 지정시 init 안에 정의 
        
        
    #기능구현
    def printText(self) :  #1번에 대한 정의
        print(self.tb1.toPlainText())   #toPlainText() : 내부에 있는 텍스트를 가져옴

        
    def inputText(self) : #2번에 대한 정의
        self.a = self.a + 1
        print(self.tb1.setPlainText(f'글자를 셋팅{self.a}'))
        
    def appendText(self) :  #3번에 대한 정의
        
        self.count = self.count + 1
        print(self.tb1.append(f'글자추가{self.count}'))
    def clearText(self) : #4번에 대한 정의
        print(self.tb1.clear())
    
       
#----------------------------------------------------------------------    
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)    #응용객체생성
    my = windowClass()      #메인 클래스 호출
    my.show()
    app.exec_()             #이벤트가 발생할 때마다 실행