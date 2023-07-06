import sys
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QCompleter
from PyQt5.uic.properties import QtWidgets
import sqlite3

from maim_item_ui import Ui_Form as ui_main_item

class main_item(QWidget, ui_main_item):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #윈도우 타이틀 숨김
        self.setWindowFlags(Qt.FramelessWindowHint)

    def value_re(self, image_, title_, long_adr, short_adr):
        self.title_ = title_
        self.label.setPixmap(QPixmap(image_))
        self.label_2.setText(self.title_)
        self.label_3.setText(long_adr)
        self.label_4.setText(short_adr)


    def re_value(self):
        return self.title_

    # def mousePressEvent(self, e):
    #     self.re_value(self.title_)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = main_item()
    mainApp.show()
    app.exec_()

