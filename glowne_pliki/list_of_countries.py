import random
import sys

from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from FileReader import Country, FileReader


class AddingButton(QPushButton):
    def  __init__(self, country_name, color, chart_panel, filepath):
        super().__init__(country_name)
        self.__color = color
        self.__file = FileReader(filepath)
        self.__country = Country(country_name, self.__file)
        self.__chart_panel = chart_panel
        self.__status = 0
        # print(country_name)
        # print(self.__file.get_dates())
        # print(self.__country.get_all_values_for_country())
        self.clicked.connect(self.__update_chart)


    def __update_chart(self):
        name = self.text()
        if self.__status == 0:
            self.__create_and_add_icon_to_btn()
            self.__chart_panel.add_data_for_chart( name, self.__country.get_all_values_for_country(), self.__file.get_dates(),
                                             self.__color)

            self.__status = 1

        elif self.__status == 1:
            self.__create_and_add_icon_to_btn()
            self.__chart_panel.remove_plot()
            self.__status = 0

    def get_status(self):
        return self.__status


    def remove_plot(self):
        pass



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

    def __init__(self, chart_panel, filepath):
        super().__init__()
        self.__chart_panel = chart_panel
        self.__buttons = []
        self.__filepath = filepath
        self.__file = FileReader(self.__filepath)

        self.__prepare_buttons_grid()

    def __get_num_of_countries(self):
        list_of = self.__file.get_countries()
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

            btn = AddingButton(self.__file.get_countries()[i] , colour, self.__chart_panel, self.__filepath)
            self.__buttons.append(btn)


    def __find_rand_color(self):
        color_id = random.randint(0, len(self.__Colors) - 1)
        color = self.__Colors[color_id]

        return color
