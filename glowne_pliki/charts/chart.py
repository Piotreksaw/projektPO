from io import BytesIO
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class CreateChart(FigureCanvasQTAgg):

    def __init__(self, width=11, height=6, dpi=90):
        self.__fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.__fig)

        # Zmienna potrzebna do stworzenia pdf
        self.__IMG_FORMAT = "png"

        self.__axes = None
        self.__start = None
        self.__end = None

    # metoda przetwarzająca wykres na obraz
    def get_img(self):
        img_data = BytesIO()

        self.__fig.savefig(img_data, format=self.__IMG_FORMAT)
        seek_offset = 0
        img_data.seek(seek_offset)
        return img_data

    # funkcja służąca do dodania danych do wykresu
    def add_data_for_chart(self, name, price, dates, color):
        self.__dates = dates
        self.__price = price
        self.set_chart()

        self.__fig.tight_layout()
        self.__add_plot(name, self.__dates, self.__price, color)

    # metoda dodająca wykres
    def __add_plot(self, name, dates, price, color):

        if self.__start == None and self.__end == None:
            self.__start = self.__dates.index(dates[0])
            self.__end = self.__dates.index(dates[-1]) + 1

        self.xx = dates[self.__start:self.__end]

        self.new_x_axis = dates[self.__start:self.__end:2]
        self.yy = price[self.__start:self.__end:1]

        self.__axes.plot(self.xx, self.yy, color, label=name)
        self.__axes.set_xticks(self.new_x_axis)
        self.__axes.legend()

        self.draw()

    # metoda usuwająca wykres
    def remove_plot(self):
        self.__fig.clf()
        self.__axes = None
        self.set_chart()

    # funkcja ustawiająca pole do wykresu
    def set_chart(self):
        if self.__axes is None:
            self.__axes = self.__fig.add_subplot(111)
            # self.__axes = self.__fig.axes[0]
            self.__axes.set_title("Wykres zależności cen energii elektrycznej w danym zakresie ")

    # poniższe funkcje zwracają nam początek i koniec
    def get_start(self, start):
        self.__start = start

    def get_end(self, end):
        self.__end = end + 1


# ta klasa jest niewykorzystywana niestety, ponieważ jej implementacja okazała się bardzo uciążliwa,
# zamiast niej jest metoda get_start, get_end, zostawiam w celu pokazania innej metody
class UpdateDataFromSlider:
    def __init__(self):
        pass

    def push_data_to_chart(self, start, end):
        self.__start = start
        self.__end = end

        self.new_boarders = [self.__start, self.__end]

    def boarder_returner(self):
        print(self.new_boarders)
        return self.new_boarders
