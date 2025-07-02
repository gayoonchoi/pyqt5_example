## Ex 3-4. 툴팁 나타내기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 글씨체와 글자크기 설정 
        QToolTip.setFont(QFont('SansSerif', 20)) 
        # 창에 tooltip 적용한다. 
        self.setToolTip('This is a <b>QWidget</b> widget')


        btn = QPushButton('Button', self)

        # 버튼에 tooltip을 적용한다. 
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
