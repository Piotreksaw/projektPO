import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
# from PyQt5.QtChart import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5.QtGui import QIcon, QPixmap

from projektPO.glowne_pliki.FileReader import FileReader, Country


class CreateChart(FigureCanvasQTAgg):
    def __init__(self, width = 11, height = 6, dpi = 90):
        self.__fig = Figure(figsize=(width, height), dpi= dpi)
        super().__init__(self.__fig)
        self.__axes = None

        self.__start = None
        self.__end = None




    def add_data_for_chart(self, name, price, dates, color):
        self.__dates = dates
        self.__price = price
        self.set_chart()

        self.__add_plot(name, self.__dates, self.__price, color)

    def get_start(self, start):
        self.__start = start
        print(self.__start)

    def get_end(self, end):
        self.__end = end

    def __add_plot(self, name, dates, price, color):
        print("test")
        self.__dates = dates

        # print(self.boarders)
        # if self.boarders == None:
        #     pass

        # self.__start = self.__dates.index(self.__dates[0])
        # self.__end = self.__dates.index(self.__dates[-1])
        # print(self.__dates)
        # print(self.__start)
        # print("test2")

        # print("test3")
        # if len(self.boardes[0]) != 0:
        # # print(self.boardes())
        # self.__start = self.boarders[0]
        # self.__end = self.boarders[-1]
        # self.__end = self.__end + 1


        # print(self.__start)
        # print(self.__price[self.__start])
        # print(self.__end)
        # print(self.__price[self.__end])



        xx = dates[self.__start:self.__end]
        yy = price[self.__start:self.__end]

        self.__axes.plot(xx, yy, color, label= name)
        self.__axes.set_xlim([self.__start, self.__end - 1])
        self.__fig.tight_layout()

        self.__axes.legend()
        self.draw()


    def remove_plot(self):
        self.__axes.cla()
        # self.__axes.


    # def boarder_returner(self):
    #     self.__boarders = self.boardes()
    #     return self.__boarders



    def set_chart(self):
        if self.__axes is None:
            # print(dates)
            self.__axes = self.__fig.add_subplot(111)




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

