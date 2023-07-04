import sys
import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit
from PyQt5.uic.properties import QtWidgets
import sqlite3

from login_ui import Ui_Form as ui_login


class login(QWidget, ui_login):
    def __init__(self):
        super().__init__()
        self.switch_clear = True
        self.setupUi(self)
        # 윈도우 타이틀 숨김
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 시작화면 고정
        self.stackedWidget.setCurrentIndex(0)
        # 버튼 클릭 이벤트 메서드
        self.connect_event()
        # 페이드 인 이벤트
        self.show()
        self.fade()

    def fade(self):
        for i in range(100):
            i = i/100
            self.setWindowOpacity(0+i)
            time.sleep(0.01)

    def login_Function(self):
        self.stackedWidget.setCurrentIndex(0)
        db = sqlite3.connect("data.db")
        cur = db.cursor()
        user_info = cur.execute("select * from user_info")
        user = self.id_line.text()
        password = self.pw_line.text()
        try:
            if len(user) == 0 or len(password) == 0:
                self.error_lbl.setText("아이디 또는 비밀번호를 입력해주세요.")
            else:
                conn = sqlite3.connect("data.db")
                cur = conn.cursor()
                query = 'SELECT pw FROM user_info WHERE id = \''+user+"\'"
                cur.execute(query)
                result_pass = cur.fetchone()[0]
                if result_pass == password:
                    self.stackedWidget.setCurrentIndex(2)
                else:
                    self.error_lbl.setText("비밀번호가 틀렸습니다.")
        except:
            self.error_lbl.setText("아이디 또는 비밀번호가 틀렸습니다.")

    def join_Function(self, switc_):
        if switc_:
            clear_list = self.findChildren(QLineEdit)
            for i in clear_list:
                i.clear()
        self.stackedWidget.setCurrentIndex(1)
        name = self.name_line.text()
        user = self.id_line2.text()
        password = self.pw_line2.text()
        password_check = self.pwch_line.text()
        age = self.age_com.currentText()
        db = sqlite3.connect("data.db")
        cur = db.cursor()
        user_info = cur.execute("select * from user_info")
        id_check = user_info.fetchall()
        for i in id_check:
            for j in i:
                if j == name:
                    self.error_lbl_2.setText("이미 존재하는 유저입니다.")
                    return
                elif j == user:
                    self.error_lbl_2.setText("이미 존재하는 아이디입니다.")
                    return
        if len(user) == 0 or len(password) == 0 or len(password_check) == 0:
            self.error_lbl_2.setText("모든 항목을 입력해주세요.")
            return
        elif password != password_check:
            self.error_lbl_2.setText("비밀번호가 일치하지 않습니다.")
            return
        else:
            print(111)
            conn = sqlite3.connect('data.db')
            cur = conn.cursor()
            user_info_ = [name, user, password, age]
            cur.execute('INSERT INTO user_info (name, id, pw, age) VALUES (?,?,?,?)', user_info_)
            conn.commit()
            a = cur.execute("select * from user_info")
            print(a.fetchall())
            conn.close()
            self.login_Function()
        self.switch_clear = True
    def connect_event(self):
        """연결 이벤트"""
        self.esc_btn.clicked.connect(self.close)
        self.join_btn.clicked.connect(lambda x: self.join_Function(True))
        self.cancel_btn.clicked.connect(lambda x:self.stackedWidget.setCurrentIndex(0))
        self.login_btn.clicked.connect(self.login_Function)
        self.clear_btn.clicked.connect(lambda x:self.join_Function(False))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = login()
    myWindow.show()


    def show_error_message(message, traceback):

        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec()
        traceback.print_exc()


    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)


    app.exec_()

