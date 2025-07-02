import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer, QTime


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 시간 표시용 라벨
        self.label = QLabel('00:00:00', self)
        self.label.setStyleSheet("font-size: 40px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)

        # 버튼 생성
        self.start_btn = QPushButton('Start', self)
        self.stop_btn = QPushButton('Stop', self)
        self.reset_btn = QPushButton('Reset', self)

        # 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.start_btn)
        vbox.addWidget(self.stop_btn)
        vbox.addWidget(self.reset_btn)
        self.setLayout(vbox)

        # 타이머 설정
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        self.time = QTime(0, 0, 0)

        # 버튼 기능 연결
        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.reset_btn.clicked.connect(self.reset)

        # 윈도우 설정
        self.setWindowTitle('Stopwatch')
        self.setGeometry(300, 300, 250, 200)
        self.show()

    def update_time(self):
        self.time = self.time.addSecs(1)
        self.label.setText(self.time.toString("hh:mm:ss"))

    def start(self):
        self.timer.start(1000)  # 1초 간격

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0)
        self.label.setText("00:00:00")


if __name__ == '__main__':
    from PyQt5.QtCore import Qt
    app = QApplication(sys.argv)
    sw = Stopwatch()
    sys.exit(app.exec_())
