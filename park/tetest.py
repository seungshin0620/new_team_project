import sys

import folium
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication


class mpampa(QWidget):
    def __init__(self):
        super().__init__()
        # self.resize(500, 500)
        """
        self.latitude = None
        self.longitude = None
        m = folium.Map(location=[latitude, longitude], zoom_start=16)
        """
        m = folium.Map(location=[37, 127], zoom_start=16)
        w = QtWebEngineWidgets.QWebEngineView(self)
        w.setHtml(m.get_root().render())
        w.setMinimumSize(1000, 1000)
        w.setMaximumSize(16447, 16447)
        w.show()

    """
    def set_location(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
    """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mapinfo = mpampa()
    mapinfo.show()
    sys.exit(app.exec_())