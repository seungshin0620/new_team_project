import sys

import folium
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication


class mpampa(QWidget):
    def __init__(self):
        super().__init__()

    def real_map(self, Latitud, longitude):
        m = folium.Map(location=[Latitud, longitude], zoom_start=16)
        w = QtWebEngineWidgets.QWebEngineView(self)
        w.setHtml(m.get_root().render())
        w.setMinimumSize(100, 100)
        w.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mapinfo = mpampa()
    mapinfo.show()
    sys.exit(app.exec_())