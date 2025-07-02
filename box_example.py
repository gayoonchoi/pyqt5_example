import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QLabel 생성
        label = QLabel('QLabel', self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet('border: 2px solid black; font-weight: bold; font-size: 16px;')

        # QPushButton 2개 생성
        btn1 = QPushButton('Okay', self)
        btn1.setStyleSheet('border: 2px solid black; font-weight: bold;')

        btn2 = QPushButton('Cancle', self)
        btn2.setStyleSheet('border: 2px solid black; font-weight: bold;')

        # 수평 박스 레이아웃 (버튼들)
        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        # 수직 박스 레이아웃 (전체)
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel & QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# QVBoxLayout을 통해 위에서 아래 방향 배치 
# QHBoxLayout을 통해 버튼 두 개를 한 줄에 나란히 배치
# setStyleSheet()로 각 위젯에 테두리와 글씨 스타일 적용
