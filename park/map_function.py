import sys
import folium
from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QVBoxLayout

from map_fuction import Ui_Mapfuction as mapf
from tetest import mpampa

class MapFunction(QWidget, mapf):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(1000, 1000)
        self.a = mpampa()
        # self.a.real_map()
        self.label_1 = QWidget(self)
        self.laout_ = QVBoxLayout(self.label_1)
        self.laout_.addWidget(self.a)
        self.label_1.resize(1000, 1000)
        self.label_1.show()
        # self.vlaout = QVBoxLayout(self)
        # self.vlaout.addWidget(self.a)
        # widget = QWidget(self)
        # widget.setLayout(self.vlaout)
        # self.a.show()


    # def initself(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mapwidget = MapFunction()
    mapwidget.show()
    sys.exit(app.exec_())

