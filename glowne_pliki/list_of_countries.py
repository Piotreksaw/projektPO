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
from FileReader import Country, FileReader


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

    def __get_num_of_countries(self):
        list_of = FileReader("eurostat.csv").getCountries()
        num_of_countires = len(list_of)
        return num_of_countires

    def __prepare_buttons_grid(self):
        # list_of_countries = FileReader("eurostat.csv").getCountries()
        layout = QVBoxLayout()

        for btn in self.__buttons:
            layout.addWidget(btn)

        self.setLayout(layout)

    def __create_button(self):
        num_of_buttons = self.__get_num_of_countries()

        for i in range(num_of_buttons):
            colour = self.__find_rand_color()

            btn = AddingButton(str(i), colour)
            self.__buttons.append(btn)


    def __find_rand_color(self):
        color_id = random.randint(0, len(self.__Colors) - 1)
        color = self.__Colors[color_id]

        return color
