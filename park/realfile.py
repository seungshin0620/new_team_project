"""Schedule Function
일정표 = id, name, image, pos세부기능 id로 db검색"""
import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QFrame, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.uic.properties import QtGui

from addSchedule import AddSchedule_Function
from schedule_function import Ui_Form as adschedule_ui

class ScheduleFunction(QWidget, adschedule_ui):
    def __init__(self):
        super().__init__()
        self.setui_intit()
        self.in_widget_function()
        self.pushButton.clicked.connect(self.add_btn)
        self.list_del = []
        self.add_item()
        self.pushButton_3.clicked.connect(self.function_del)
    def setui_intit(self):
        self.setupUi(self)

    def add_btn(self):
        a = AddSchedule_Function()
        self.vlaout.insertWidget(len(self.vlaout)-1, a)
        self.switch_ = True
        n = a.findChild(QLabel)
        f = n.parent()
        f = f.parent()
        self.list_del.append(f)


    def add_item(self):
        self.vspacer = QSpacerItem(20, 100, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.vlaout.addItem(self.vspacer)

    def in_widget_function(self):
        """스크롤 위젯 설정"""
        self.vlaout = QVBoxLayout(self)
        widget = QWidget(self)
        widget.setLayout(self.vlaout)
        self.scrollArea.setWidget(widget)
    def function_del(self):
        self.list_del[-1].deleteLater()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    sub_function = ScheduleFunction()

    sub_function.show()
    app.exec_()

