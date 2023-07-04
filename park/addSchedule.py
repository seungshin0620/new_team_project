"""addSchedule_Functino"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QPushButton, QVBoxLayout, QLabel
from untitled import Ui_AddwidgetFunction as addwidget_function


class AddSchedule_Function(QWidget, addwidget_function):
    def __init__(self):
        super().__init__()
        self.show_function()
        self.pushButton.clicked.connect(lambda x=None, y=self.pushButton: self.del_function(y))

    def show_function(self):
        """show!"""
        self.setupUi(self)
    def del_function(self, a):
        print(a.text())
        self.deleteLater()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    addwidget_function = AddSchedule_Function()
    addwidget_function.show()
    app.exec_()

