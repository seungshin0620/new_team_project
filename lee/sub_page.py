import datetime
import sys
import time

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QCompleter, QVBoxLayout, QSizePolicy, QSpacerItem, QFrame, \
    QScrollArea, QDialog
from PyQt5.uic.properties import QtWidgets
import sqlite3

from sub_ui import Ui_Dialog as ui_sub


class Sub_Page(QDialog, ui_sub):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 윈도우 타이틀 숨김
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.x_btn_2.clicked.connect(self.close)
        self.move(695, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = Sub_Page()
    mainApp.show()
    app.exec_()