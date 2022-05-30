import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QGroupBox, QLineEdit, QTabWidget, QPushButton
# from PyQt5 import QtCore
from Map.geo_example import MapChart
from Charts.chart import CreateChart



class Tabs(QWidget):
    def __init__(self, chart):
        super().__init__()
        self.__chart = chart


        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(100,100)
        self.tabs.addTab(self.tab1, "Wykres")
        self.tabs.addTab(self.tab2, "Mapa")
        self.tab1.layout = QVBoxLayout()
        self.tab1.layout.addWidget(self.__chart)
        self.tab1.setLayout(self.tab1.layout)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
