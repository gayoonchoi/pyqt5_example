## Ex 3-1. 창 띄우기.
# blank_window.py 

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

# QWidget이 부모 클래스
# 부모 클래스를 상속 받아서 MyApp이라는 클래스를 생성한다. 
class MyApp(QWidget):

    def __init__(self):
        # super는 부모 클래스를 가리킨다. 
        super().__init__() 
        self.initUI() # MyApp이라는 initUI라는 함수 (자기자신)을 가리킨다. self.initUI() 

    def initUI(self): 
        # 창 이름 변경 
        self.setWindowTitle('My GY Application')
        self.setWindowIcon(QIcon('web.png'))
        self.setGeometry(300, 300, 300, 200)
        # 창을 띄우는 위치 설정 ------------------------------------------ 부모 클래스의 move 메소드가 있어야 실행 가능하다. 
        self.move(300, 300) 
        # 창 사이즈 변경 
        self.resize(600, 600)
        # 창 확인하기 
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
