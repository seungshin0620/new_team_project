"""addSchedule_Functino"""
import sys

from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QCompleter
from PyQt5.uic.properties import QtGui

from untitled import Ui_AddwidgetFunction as addwidget_function


class AddSchedule_Function(QWidget, addwidget_function):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def add_result_function(self, image, name, info, long_adr, short_adr, num):
        """실 호출 함수"""
        self.label.setPixmap(QPixmap(image))
        self.label_2.setText(name)
        self.label_3.setText(info)
        self.label_4.setText(long_adr)
        self.label_5.setText(short_adr)
        self.label_6.setText(f'{num}')
        self.pushButton.clicked.connect(self.deleteLater)
        self.widget_rock()
        self.btn_clicked_function()


    def widget_rock(self):
        """수정버튼을 누르기전엔 수정못하도록 위젯 락기능"""
        self.pushButton.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.timeEdit.setEnabled(False)
        self.timeEdit_2.setEnabled(False)

    def correction_function(self, x):
        """수정 클릭시 수정 가능하게하는 스위치 기능"""
        if x:
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(True)
            self.timeEdit.setEnabled(True)
            self.timeEdit_2.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(False)
            self.timeEdit.setEnabled(False)
            self.timeEdit_2.setEnabled(False)
    def btn_clicked_function(self):
        """버튼 연결 기능"""
        self.pushButton_2.clicked.connect(lambda x=None: self.correction_function(True))
        self.pushButton_3.clicked.connect(lambda x=None: self.correction_function(False))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    addwidget_function = AddSchedule_Function()
    addwidget_function.show()
    app.exec_()
