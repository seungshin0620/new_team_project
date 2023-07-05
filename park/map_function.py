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
        self.setMaximumSize(100, 100)
        self.initself()
    def initself(self):
        self.a = mpampa()
        self.a.real_map(37, 127)
        self.a.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mapwidget = MapFunction()
    sys.exit(app.exec_())

