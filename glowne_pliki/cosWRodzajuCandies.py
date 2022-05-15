import sys
import random

from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class Chart(FigureCanvasQTAgg):

    def __init__(self, width = 5, height = 5, dpi = 100):
        self.__fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.__fig)

        self.__axes = None

    def addNewPlot(self, func, name, color):
        if self.__axes is None:
            self.__axes = self.__fig.add_subplot(111)

        x_start = -100
        x_end = 100
        xx = range(x_start, x_end)
        yy = [func(x) for x in xx]

        self.__axes.plot(xx, yy, color, label= name)
        self.__axes.legend()
        self.draw()

class RandomFunctionButton(QPushButton):
    def __init__(self, button_name, func, color, chart_panel):
        super(RandomFunctionButton, self).__init__(button_name)
        self.__chart_panel = chart_panel
        self.__func = func
        self.__color = color

    def __update_chart_panel(self):
        name = self.text()
        self.__chart_panel.add_new_plot(self.__func, name, self.__color)

        self.__create_and_add_button()

    def __create_and_add_button(self, wigth = 30, height = 15):
        pass




class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)


    def __init_default_value(self):
        self.__x_padding = 300
        self.__y_padding = 300
        self.__width = 800
        self.__height = 600

    def __init_view(self):
        chart_panel = Chart()
