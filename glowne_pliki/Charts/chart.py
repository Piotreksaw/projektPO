import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
# from PyQt5.QtChart import *
from io import BytesIO
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot
from PyQt5.QtGui import QIcon, QPixmap

from glowne_pliki.file_reader import FileReader, Country


class CreateChart(FigureCanvasQTAgg):
    # Zmienna potrzebna do stworzenia pdf
    __IMG_FORMAT = "png"

    def __init__(self, width = 11, height = 6, dpi = 90):
        self.__fig = Figure(figsize=(width, height), dpi= dpi)
        super().__init__(self.__fig)

        self.__axes = None
        self.__start = None
        self.__end = None

    def get_img(self):
        img_data = BytesIO()
        self.__fig.savefig(img_data, format=self.__IMG_FORMAT)
        seek_offset = 0
        img_data.seek(seek_offset)
        return img_data

    def add_data_for_chart(self, name, price, dates, color):
        self.__dates = dates
        self.__price = price

        self.set_chart()
        self.__fig.tight_layout()
        self.__add_plot(name, self.__dates, self.__price, color)


    def __add_plot(self, name, dates, price, color):
        # print("test")
        self.__dates = dates

        if self.__start == None and self.__end == None:
            self.__start = self.__dates.index(self.__dates[0])
            self.__end = self.__dates.index(self.__dates[-1]) + 1
            # print(self.__dates)

        self.xx = dates[self.__start:self.__end:1]
        self.xxx = dates[self.__start:self.__end:2]
        self.yy = price[self.__start:self.__end:1]

        # self.__axes.set_xticks(self.xxx)

        self.__axes.plot(self.xx, self.yy, color, label= name)


        self.__axes.legend()

        self.draw()


    def remove_plot(self):
        self.__axes.cla()


    def set_chart(self):
        if self.__axes is None:
            # print(dates)
            self.__fig.add_subplot(111)
            self.__axes = self.__fig.axes[0]

    def get_start(self, start):
        self.__start = start

    def get_end(self, end):
        self.__end = end

    def creat_shorter_x_axis(self, xx):
        self.__new_x = self.xx






# ta klasa jest niewykorzystywana niestety, ponieważ jej implementacja okazała się bardzo uciążliwa,
# zamiast niej jest metoda get_start, get_end
class UpdateDataFromSlider:
    def __init__(self):
        pass


    def push_data_to_chart(self, start, end):
        self.__start = start
        self.__end = end
        # print(self.__start)
        # print(self.__end)
        self.new_boarders = [self.__start, self.__end]


    def boarder_returner(self):
        print(self.new_boarders)
        return self.new_boarders

