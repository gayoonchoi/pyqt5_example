import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Start Label', self)
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel('player1 Label', self)
        label3 = QLabel('player2 Label', self)

        font1 = label1.font()
        font1.setPointSize(24)

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)

        font3 = label3.font()
        font3.setFamily('Times New Roman')
        font3.setBold(True)

        label1.setFont(font1)
        label2.setFont(font2)
        label3.setFont(font3)

        # 수평 레이아웃: label2 (왼쪽) + 공간 + label3 (오른쪽)
        hbox = QHBoxLayout()
        hbox.addWidget(label2)
        hbox.addStretch(1)
        hbox.addWidget(label3)

        # 수직 레이아웃 전체
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
