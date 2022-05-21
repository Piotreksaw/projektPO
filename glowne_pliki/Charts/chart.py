import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
# from PyQt5.QtChart import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5.QtGui import QIcon, QPixmap


class create_Chart(FigureCanvasQTAgg):
    def __init__(self, width = 5, height = 5, dpi = 100):
        self.__fig = Figure(figsize=(width, height), dpi= dpi)
        super().__init__(self.__fig)

        self.__axes = None

    def add_new_plot(self, func, name, color):
        if self.__axes is None:
            self.__axes = self.__fig.add_subplot(111)

        x_start = -100
        x_end = 100

        xx = range(x_start, x_end)
        yy = [func(x) for x in xx]

        self.__axes.plot(xx, yy, color, label= name)
        self.__axes.legend()
        self.draw()