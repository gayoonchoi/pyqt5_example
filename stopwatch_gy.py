# 최가윤 - 계산기 만들어보기 - 완성 X 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, QTime, QCoreApplication

class MyApp(QWidget): 
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): 
        # Stop watch icon 추가 
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('icon/watch_stop.png')) 
        
        #self.statusBar().showMessage('Ready')
        okButton = QPushButton('Start')
        cancelButton = QPushButton('Stop')

        hbox = QHBoxLayout()  
        hbox.addStretch(1)   
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1) 

        vbox = QVBoxLayout()
        vbox.addStretch(3) 
        vbox.addLayout(hbox) 
        vbox.addStretch(1) 

        self.setLayout(vbox)
        self.setWindowTitle('Box Layout')

        # 종료 버튼 추가 
        btn2 = QPushButton('Timer Check Quit', self)
        # btn2.move(50, 50) 
        btn2.resize(btn2.sizeHint())
        btn2.clicked.connect(QCoreApplication.instance().quit),,

        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
# 시작 
# 중단
# 재개 