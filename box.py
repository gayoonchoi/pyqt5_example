## Ex 4-2. 박스 레이아웃.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()  # 수평 박스를 하나 만들고, 두 개의 버튼과 양 쪽에 빈 공간을 추가합니다.
        hbox.addStretch(1)    # 이 addStretch() 메서드는 신축성있는 빈 공간을 제공합니다.
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1) # 두 버튼 양쪽의 stretch factor가 1로 같기 때문에 이 두 빈 공간의 크기는 창의 크기가 변화해도 항상 같습니다.

        vbox = QVBoxLayout()
        vbox.addStretch(3) # 수직 박스의 stretch factor는 수평 박스를 아래쪽으로 밀어내서 두 개의 버튼을 창의 아래쪽에 위치하도록 합니다.
        vbox.addLayout(hbox) # 다음으로 수평 박스(hbox)를 수직 박스(vbox)에 넣어줍니다.
        vbox.addStretch(1) # 이 때에도 수평 박스 위와 아래의 빈 공간의 크기는 항상 3:1을 유지합니다.

        self.setLayout(vbox)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

