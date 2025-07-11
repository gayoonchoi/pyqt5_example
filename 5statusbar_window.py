## Ex 3-5. 상태바 만들기.
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


# 앞의 5가지는 QWidget 부모 클래스를 상속받았지만
# 지금은 QMainWindow로부터 상속 받는다. 

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
