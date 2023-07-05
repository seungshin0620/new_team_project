import time
import sys
from threading import Thread, Event

from PySide6 import QtCore, QtWidgets, QtTest

th_e = Event()


class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.func_init()
        self.progress_status = 0

    def setupUi(self):
        self.setLayout(QtWidgets.QGridLayout())
        self.progress_bar = QtWidgets.QProgressBar(parent=self)
        self.pushButton = QtWidgets.QPushButton("start", parent=self)
        self.layout().addWidget(self.progress_bar)
        self.layout().addWidget(self.pushButton)

    def func_init(self):
        self.pushButton.clicked.connect(self.progress_start)

    def thread_func(self):
        for i in range(100):
            self.progress_bar.setValue(i + 1)
            if th_e.is_set():
                return
            time.sleep(0.2)

    def progress_start(self):
        if not self.progress_status:
            self.thread_ = Thread(target=self.thread_func, daemon=True)
            self.thread_.start()
            self.progress_status = 1
            self.pushButton.setText("stop")
        else:
            th_e.set()
            self.thread_.join()
            th_e.clear()
            self.progress_bar.setValue(0)
            self.progress_status = 0
            self.pushButton.setText("start")


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     main = Main()
#     main.show()
#     app.exec()
"""
왜 정상적인 작동이 되지 않을까요?
qt가 어떻게 작동하는지를 알면 이렇게 하는 것이 잘못됐다는 것을 알 수 있습니다. qt의 실시간 속에서
자신만의 thread를 보장하려면 QThread를 이용해야합니다.
다음을 만듭니다.
"""


class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.func_init()
        self.thread_ = ThreadPart(self)
        self.progress_status = 0

    def setupUi(self):
        self.setLayout(QtWidgets.QGridLayout())
        self.progress_bar = QtWidgets.QProgressBar(parent=self)
        self.pushButton = QtWidgets.QPushButton("start", parent=self)
        self.layout().addWidget(self.progress_bar)
        self.layout().addWidget(self.pushButton)

    def func_init(self):
        self.pushButton.clicked.connect(self.progress_start)

    def progress_start(self):
        if not self.progress_status:
            self.thread_.run()
            self.progress_status = 1
            self.pushButton.setText("stop")
        else:
            self.thread_.terminate()
            self.progress_bar.setValue(0)
            self.progress_status = 0
            self.pushButton.setText("start")


class ThreadPart(QtCore.QThread):
    def __init__(self, p):
        super().__init__(parent=p)

    def run(self):
        for i in range(100):
            self.parent().progress_bar.setValue(i + 1)
            QtTest.QTest.qWait(200)


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     main = Main()
#     main.show()
#     app.exec()


"""
안타깝게도 이것도 답이 아닙니다. 창을 움직이는 실시간 행동에 대해서 thread가 작동하지 않는 문제가
발생합니다. 대체 왜 이런 일이 발생할까요?
우선 정답부터 말하자면 thread를 보장하자니 qt에 맞지 않고, QThread를 쓰면 qt에 맞으나, thread에
맞지 않는 문제가 생기기 때문입니다.
자, 그럼 이제 우리는 qt에 영향을 덜 주면서 그러면서 thread에 맞게 만들어보겠습니다.
"""


class Main(QtWidgets.QWidget):
    signal = QtCore.Signal(int)

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.func_init()
        self.progress_status = 0

    def setupUi(self):
        self.setLayout(QtWidgets.QGridLayout())
        self.progress_bar = QtWidgets.QProgressBar(parent=self)
        self.pushButton = QtWidgets.QPushButton("start", parent=self)
        self.layout().addWidget(self.progress_bar)
        self.layout().addWidget(self.pushButton)

    def func_init(self):
        self.pushButton.clicked.connect(self.progress_start)
        self.signal.connect(self.progress_bar.setValue)

    def thread_func(self):
        for i in range(100):
            self.signal.emit(i+1)
            if th_e.is_set():
                return self.signal.emit(0)
            time.sleep(0.2)

    def progress_start(self):
        if not self.progress_status:
            self.thread_ = Thread(target=self.thread_func, daemon=True)
            self.thread_.start()
            self.progress_status = 1
            self.pushButton.setText("stop")
        else:
            th_e.set()
            self.thread_.join()
            th_e.clear()
            self.progress_status = 0
            self.pushButton.setText("start")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec()
"""
signal을 통해서 통제함으로서 qt의 실시간 반복에 영향을 주지 않으면서 다음신호에 정상적으로 작동하도록
만들었으며 완전 병렬을 제공할 수 있게끔 만들었습니다.
"""
