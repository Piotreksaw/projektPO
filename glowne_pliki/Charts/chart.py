import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
# from PyQt5.QtChart import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5.QtGui import QIcon, QPixmap

from projektPO.glowne_pliki.FileReader import FileReader, Country


class CreateChart(FigureCanvasQTAgg):
    def __init__(self, width = 5, height = 5, dpi = 100):
        self.__fig = Figure(figsize=(width, height), dpi= dpi)
        super().__init__(self.__fig)
        self.start = 0
        self.end = 10

        self.__axes = None

    def add_new_plot(self, name, price, date, color):
        if self.__axes is None:
            self.__axes = self.__fig.add_subplot(111)


        xx = date[self.start, self.end]
        yy = price[self.start, self.end]

        self.__axes.plot(xx, yy, color, label= name)
        self.__axes.legend()
        self.draw()

