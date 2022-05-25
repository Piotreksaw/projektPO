import random
import sys

from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from Charts.chart import CreateChart
from FileReader import Country, FileReader


class AddingButton(QPushButton):
    def  __init__(self, btn_name, date, price, chart_panel, color):
        super().__init__(btn_name)
        self.__color = color
        self.__date = date
        self.__price = price
        self.__chart_panel = chart_panel
        self.__status = 0
        self.clicked.connect(self.__update_chart)


    def __update_chart(self):
        name = self.text()
        if self.__status == 0:
            self.__create_and_add_icon_to_btn()
            self.__status = 1
        elif self.__status == 1:
            self.__create_and_add_icon_to_btn()
            self.__status = 0

        CreateChart().add_new_plot( name, self.__date, self.__price, self.__color)



    def __create_and_add_icon_to_btn(self, width = 40, height =5):
        if self.__status == 0:
            shape = ((0,0 ), (width - 1, height -1))
            rectangle = Image.new("RGBA", (width, height))
            rectangle_img = ImageDraw.Draw(rectangle)
            rectangle_img.rectangle(shape, fill=self.__color)
            rectangle_qt = ImageQt(rectangle)
            rectangle_pixmap = QPixmap.fromImage(rectangle_qt)
            rectangle_icon = QIcon(rectangle_pixmap)
            self.setIcon(rectangle_icon)
        else:
            shape = ((0,0 ), (width - 1, height -1))
            rectangle = Image.new("RGBA", (width, height))
            rectangle_img = ImageDraw.Draw(rectangle)
            rectangle_img.rectangle(shape, fill=self.__color)
            rectangle_qt = ImageQt(rectangle)
            rectangle_pixmap = QPixmap.fromImage(rectangle_qt)
            rectangle_icon = QIcon(None)
            self.setIcon(rectangle_icon)

class ButtonsPanel(QGroupBox):
    __Colors = ["blue", "green", "red", "cyan", "magenta", "yellow", "black"]

    def __init__(self, chart_panel):
        super().__init__()
        self.__chart_panel = chart_panel
        self.__buttons = []

        self.__prepare_buttons_grid()

    def __get_list(self):
        list_of = FileReader("eurostat.csv").getCountries()
        return list_of

    def __get_date(self):
        date = FileReader("eurostat.csv").getDates()
        return date

    def __get_data(self):
        data = FileReader("eurostat.csv").getData()
        return data
    def __get_num_of_countries(self):
        list_of = self.__get_list()
        num_of_countires = len(list_of)
        # print(num_of_countires)
        return num_of_countires

    def __prepare_buttons_grid(self):
        self.__create_button()
        layout = QFormLayout()
        groupBox = QGroupBox()

        for btn in self.__buttons:
            layout.addWidget(btn)

        groupBox.setLayout(layout)

        self.scroll = QScrollArea()
        self.scroll.setWidget(groupBox)
        self.scroll.setWidgetResizable(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll)
        self.setLayout(layout)


    def __create_button(self):
        num_of_buttons = self.__get_num_of_countries()

        for i in range(num_of_buttons):
            colour = self.__find_rand_color()

            btn = AddingButton(self.__get_list()[i], self.__get_date()[i], self.__get_data()[i], self.__chart_panel,  colour)
            self.__buttons.append(btn)


    def __find_rand_color(self):
        color_id = random.randint(0, len(self.__Colors) - 1)
        color = self.__Colors[color_id]

        return color
