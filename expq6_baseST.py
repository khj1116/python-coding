import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *   #QPixmap 실행
from PyQt5 import uic   
from PyQt5.QtCore import *  #QThread 실행
import numpy as np

form_class = uic.loadUiType(r"expq6_base.ui")[0]

class VideoThread(QThread):
    imgData = pyqtSignal(np.ndarray) 

    def __init__(self, video_source=0):
        super().__init__()
        self.video_source = video_source
        self.str1 = ' '
        

    def run(self):
        cap = cv2.VideoCapture(self.video_source)   
        while cap.isOpened():                       
            ret, frame = cap.read()                 
            if ret:
                self.imgData.emit(frame)           
            else:
                break
            cv2.putText(frame, self.str1, (100, 100), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 255, 0))
                                                      
        cap.release() 

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.VT = VideoThread()      
        self.VT.imgData.connect(self.update_image)   
        self.VT.start()

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
        self.ans = ''         
        
        
    def update_image(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                  
        pixmap = QPixmap.fromImage(img) 
                
        self.label.setPixmap(pixmap.scaledToWidth(600)) 
    
    def main(self) :
        value = self.sender().text()
        if value == 'C':
            print('clear')
            self.result.setText('0')
            self.ans=''
        elif value == '=':
            print('=')
            try : 
                resultValue = eval(self.ans.lstrip("0"))
                self.result.setText(str(resultValue))
                self.ans = ''
            
            except : 
                self.result.setText("error")
                
        else :
            if value == "x" :
                value = "*"
            self.ans = self.ans + value
            print(self.ans)
            self.result.setText(self.ans)  
              
        self.VT.str1 = self.ans   #웹캠 화면에 계산기 반환값을 출력               
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())


  
