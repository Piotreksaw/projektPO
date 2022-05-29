from io import BytesIO
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class CreateChart(FigureCanvasQTAgg):
    # Zmienna potrzebna do stworzenia pdf
    __IMG_FORMAT = "png"

    def __init__(self, width=11, height=6, dpi=90):
        self.__fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.__fig)

        self.__axes = None

    # Dodanie metody umożliwiającej zapis zdjęcia wykresu
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

        self.__add_plot(name, self.__dates, self.__price, color)

    def __add_plot(self, name, dates, price, color):
        print("test")

        self.__start = self.__dates.index(self.__dates[0])

        self.__end = self.__dates.index(self.__dates[-1])
        print(self.__start)
        print(self.__price[self.__start])
        print(self.__end)
        print(self.__price[self.__end])

        xx = dates[self.__start:self.__end]
        yy = price[self.__start:self.__end]

        self.__axes.plot(xx, yy, color, label=name)
        self.__axes.set_xlim([self.__start, self.__end])
        self.__axes.legend()
        self.draw()

    def remove_plot(self):
        self.__axes.cla()
        # self.__axes.

    # def update_data_from_slider(self, start, end):
    #     self.__start = start
    #     self.__end = end
    #     self.__new_boarders = [self.__start,self.__end]
    #     return self.__new_boarders

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
        print(self.__start)
        print(self.__end)
        self.__new_boarders = [self.__start, self.__end]
        return self.__new_boarders
