from math import sin, pi

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class Chart(FigureCanvasQTAgg):
    def __init__(self, value_factor, period_factor, width=10, height=10, dpi=100):
        self.__fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.__fig)

        self.__value_factor = value_factor
        self.__period_factor = period_factor

        self.__init_data()
        self.__init_view()

    def __init_data(self):
        self.__n_of_x = 1000
        self.__min_x = 0
        self.__max_x = 2 * pi

        step_factor = self.__max_x / (self.__n_of_x - 1)
        self.__xx = [i * step_factor for i in range(self.__n_of_x)]
        # another solution (like in MatLab): # self.__xx = np.linspace(self.__min_x, self.__max_x, self.__n_of_x) # import numpy as np

    def __init_view(self):
        self.__ax = self.__fig.add_subplot(111)
        self.__plot_sin()

    def update_plot(self, value_factor, period_factor):
        self.__value_factor = value_factor
        self.__period_factor = period_factor
        self.__plot_sin()

    def __plot_sin(self):
        self.__ax.clear()

        a = self.__value_factor
        b = self.__period_factor

        self.__yy = [a * sin(b * x) for x in self.__xx]

        self.__ax.plot(self.__xx, self.__yy)
        self.__ax.set_xlim([self.__min_x, self.__max_x])
        self.__fig.suptitle("a * sin(b*x)")

        self.__fig.canvas.draw()
