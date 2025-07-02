## Ex 5-1. QPushButton.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self) # &은 단축키 설정가능 (alt키) #  'Alt+b' # 이때 QPushButton함수를 통해 버튼의 단축키를 앞에서 설정한다. &Button1 
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2') # 단추 이름 등록  # 단축키는 이 버튼의 단축키는 'Alt+2'  # 이때 setText 함수를 통해 버튼 이름을 표시하고, 해당 단축키를 &2 를 뒤에서 설정한다. 

        btn3 = QPushButton('&Button3', self) 
        # btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
