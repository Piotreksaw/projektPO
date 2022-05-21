import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QGroupBox, QLineEdit, QTabWidget, QPushButton
# from PyQt5 import QtCore
from Map.geo_example import MapChart
from candies_example import CandiesChart

path_to_data = "dane_do_mapy.geojson"

class Tabs(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(50, 50)
        self.tabs.addTab(self.tab1, "Wykres")
        self.tabs.addTab(self.tab2, "Mapa")
        self.tab1.layout = QVBoxLayout()
        self.chart = CandiesChart()
        self.tab1.layout = QVBoxLayout(self.chart)
        # self.pushButton1 = QPushButton("PyQt5 button")
        # self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
