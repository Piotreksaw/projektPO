import random
import sys

from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from Charts.chart import create_Chart
# from Charts.chart import create_Chart
from FileReader import Country

# class RandFuncButton(QPushButton):
#
#     def __init__(self, btn_name, color, chart_panel):
#         super().__init__(btn_name)
#         self.__chart_panel = chart_panel
#
#         self.__color = color
#
#         # self.clicked.connect(self.__update_chart_panel)
#
#     def __update_chart_panel(self):
#         name = self.text()
#         self.__chart_panel.add_new_plot(self, name, self.__color)
#
#         self.__create_and_add_icon_to_btn()
#
#     def __create_and_add_icon_to_btn(self, width=30, height=15):
#         rectangle_shape = ((0, 0), (width - 1, height - 1))
#
#         rectangle = Image.new("RGBA", (width, height))
#         rectangle_img = ImageDraw.Draw(rectangle)
#         rectangle_img.rectangle(rectangle_shape, fill=self.__color)
#
#         rectangle_qt = ImageQt(rectangle)
#         rectangle_pixmap = QPixmap.fromImage(rectangle_qt)
#         rectangle_icon = QIcon(rectangle_pixmap)
#
#         self.setIcon(rectangle_icon)
#
# class ButtonsPanel(QGroupBox):
#     __COLORS = ["blue", "green", "red", "cyan", "magenta", "yellow", "black"]
#
#     def __init__(self, chart_panel: create_Chart()):
#         super().__init__()
#         self.__chart_panel = chart_panel
#         self.__buttons = []
#
#         self.__prepare_buttons_grid()
#
#     def __prepare_buttons_grid(self):
#         self.__create_rand_func_buttons()
#         layout = QVBoxLayout()
#
#         for btn in self.__buttons:
#             layout.addWidget(btn)
#
#         self.setLayout(layout)
#
#     def __create_rand_func_buttons(self):
#         start, end = 1, 10
#         num_of_buttons = random.randint(start, end)
#
#         for i in range(num_of_buttons):
#             colour = self.__find_rand_color()
#
#             # rand_func = self.__create_rand_func()
#
#             btn = self.RandFuncButton(str(i), colour, self.__chart_panel)
#             self.__buttons.append(btn)
#
#     def __find_rand_color(self):
#         color_id = random.randint(0, len(self.__COLORS) - 1)
#         color = self.__COLORS[color_id]
#
#         return color

class AddingButton(QPushButton):
    def  __init__(self, btn_name, color):
        super().__init__(btn_name)
        self.__color = color
        self.__create_and_add_icon_to_btn()

    def __create_and_add_icon_to_btn(self, width = 30, height =10):
        shape = ((0,0 ), (width - 1, height -1))
        rectangle = Image.new("RGBA", (width, height))
        rectangle_img = ImageDraw.Draw(rectangle)
        rectangle_img.rectangle(shape, fill=self.__color)

        rectangle_qt = ImageQt(rectangle)
        rectangle_pixmap = QPixmap.fromImage(rectangle_qt)
        rectangle_icon = QIcon(rectangle_pixmap)
        self.setIcon(rectangle_icon)

class ButtonsPanel(QGroupBox):
    __Colors = ["blue", "green", "red", "cyan", "magenta", "yellow", "black"]

    def __init__(self):
        super().__init__()
        self.__buttons = []

    def __prepare_buttons_grid(self):
        # self.
        pass