import datetime
import sys
import time

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QCompleter, QVBoxLayout, QSizePolicy, QSpacerItem, QFrame, \
    QScrollArea
from PyQt5.uic.properties import QtWidgets
import sqlite3

from login_ui import Ui_Form as ui_login
from pythonstudy.trip_pj import sub_page
from pythonstudy.trip_pj.main_item import main_item
from pythonstudy.trip_pj.sub_page import Sub_Page


class Main_Page(QWidget, ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 윈도우 타이틀 숨김
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 버튼 클릭시 색상 변경
        self.a_type = "background-color: rgb(255, 255, 255); " \
                 "border-width:3px; " \
                 "border-top-color: rgb(255, 255, 255); " \
                 "border-right-color: rgb(255, 255, 255); " \
                 "border-left-color: rgb(255, 255, 255); " \
                 "border-bottom-color: rgb(131, 160, 255); " \
                 "border-style:solid; color:rgb(131, 160, 255);" \
                 "color: rgb(131, 160, 255);"
        self.b_type = "background-color: rgb(255, 255, 255);" \
                 "border-width:3px; " \
                 "border-top-color: rgb(255, 255, 255); " \
                 "border-right-color: rgb(255, 255, 255); " \
                 "border-left-color: rgb(255, 255, 255); " \
                 "border-bottom-color: rgb(205, 205, 205); " \
                 "border-style:solid; color:rgb(131, 160, 255);" \
                 "color: rgb(205, 205, 205);"
        self.location_btn.setStyleSheet(self.a_type)
        self.restaurant_btn.setStyleSheet(self.b_type)
        self.hotel_btn.setStyleSheet(self.b_type)

        # 실시간 시간 출력 이벤트
        self.timer = QTimer(self)
        self.timer.start(30000)  # 30초마다 반복
        self.timer.timeout.connect(self.timer_event)
        self.time_lbl.setText(str(datetime.datetime.now().timetz()).split(".")[0][:5])

        # line_edit 자동완성 검색기능
        names = ["박호현", "송준혁", "이승신", "이동녘", "김윤재", "이시연"]
        completer = QCompleter(names)
        self.search_line.setCompleter(completer)
        self.btn_list = [self.location_btn, self.restaurant_btn, self.hotel_btn]
        self.current_menu = 0

        self.in_widget_function()
        self.add_item()
        self.add_btn()
        for i in self.btn_list:
            i.clicked.connect(self.add_btn)

        # 버튼 클릭 이벤트
        self.connect_event()

    # 실시간 시간 출력 함수
    def timer_event(self):
        self.time_lbl.setText(str(datetime.datetime.now().timetz()).split(".")[0][:5])

    def connect_event(self):
        """연결 이벤트"""
        self.esc_btn2.clicked.connect(self.close)
        for idx, btn in enumerate(self.btn_list):
            btn.clicked.connect(lambda x=None, y=idx: self.category_infos(y))

    def category_infos(self, idx):
        if idx == 0:
            self.btn_list[0].setStyleSheet(self.a_type)
            self.btn_list[1].setStyleSheet(self.b_type)
            self.btn_list[2].setStyleSheet(self.b_type)
        if idx == 1:
            self.btn_list[0].setStyleSheet(self.b_type)
            self.btn_list[1].setStyleSheet(self.a_type)
            self.btn_list[2].setStyleSheet(self.b_type)
        if idx == 2:
            self.btn_list[0].setStyleSheet(self.b_type)
            self.btn_list[1].setStyleSheet(self.b_type)
            self.btn_list[2].setStyleSheet(self.a_type)

    def add_btn(self):
        self.vlaout.deleteLater()
        self.in_widget_function()
        self.add_item()
        for i in range(10):
            i = main_item()
            i.value_re(r"C:\Users\KDT113\Desktop\pythonProject\pythonstudy\trip_pj\img\background.png", "흰여울 문화마을", "부산광역시 영도구 흰여울길", "영도구")
            i.mousePressEvent = lambda x=None: self.turn_page(i)
            self.vlaout.insertWidget(len(self.vlaout) - 1, i)

    def turn_page(self, e):
        print(e.re_value())
        self.page_ = Sub_Page()
        self.page_.exec_()

    def add_item(self):
        self.vspacer = QSpacerItem(20, 100, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.vlaout.addItem(self.vspacer)

    def in_widget_function(self):
        """스크롤 위젯 설정"""
        self.vlaout = QVBoxLayout(self)
        widget = QWidget(self)
        widget.setLayout(self.vlaout)
        self.scrollArea.setWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = Main_Page()
    mainApp.show()
    app.exec_()