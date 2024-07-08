from PyQt5.QtWidgets import *
from PyQt5 import uic       #사용자인터페이스클레스
import sys


form_class = uic.loadUiType('expq5.ui')[0]

class windowClass(QMainWindow, form_class):   
    def __init__(self):
        super().__init__()  #괄호 빠트리지 않기
        self.setupUi(self)
        self.pb1.clicked.connect(self.main)  
        self.pb2.clicked.connect(self.main) 
        self.pb3.clicked.connect(self.main) 
        self.pb4.clicked.connect(self.main)
        self.pb5.clicked.connect(self.main)  
        self.pb6.clicked.connect(self.main) 
        self.pb7.clicked.connect(self.main) 
        self.pb8.clicked.connect(self.main)
        self.pb9.clicked.connect(self.main)
        self.pb0.clicked.connect(self.main) 
        self.pbequal.clicked.connect(self.main)
        self.pbsum.clicked.connect(self.main)  
        self.pbsub.clicked.connect(self.main) 
        self.pbmul.clicked.connect(self.main) 
        self.pbdiv.clicked.connect(self.main)
        self.pbcan.clicked.connect(self.main)
        self.result.setEnabled(False)
        self.textValue = ''
 #-----------------------------------------------------------------      
    #기능구현
    def main(self) :  
        value = self.sender().text()
        if value == 'C':        #value 값이 C이면
            print('clear')          #clear 프린트 출력 후 
            self.result.setText('0')  #
            self.textValue = ''
        elif value == '=':
            print('=')
            try :
                resultValue = eval(self.textValue.lstrip("0")) #입력한 숫자를 하나씩 누적
                self.result.setText(str(resultValue))
                
            except : 
                self.result.setText("error")   
        else:
            if value == 'X':
                value = "*"
            self.textValue =  self.textValue + value
            print(self.textValue)
            self.result.setText(self.textValue)
        
    
        

#----------------------------------------------------------------------    
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)   
    my = windowClass()      
    my.show()
    app.exec_()   