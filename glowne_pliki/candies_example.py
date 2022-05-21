import random
import sys

from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class CandiesChart(FigureCanvasQTAgg):

    def __init__(self, width=5, height=5, dpi=100):
        self.__fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.__fig)

        self.__axes = None

    def add_new_plot(self, func, name, color):
        if self.__axes is None:
            self.__axes = self.__fig.add_subplot(111)

        x_start, x_end = -100, 100
        xx = range(x_start, x_end)
        yy = [func(x) for x in xx]

        self.__axes.plot(xx, yy, color, label=name)
        self.__axes.legend()
        self.draw()



class RandFuncButton(QPushButton):

    def __init__(self, btn_name, func, color, chart_panel):
        super().__init__(btn_name)
        self.__chart_panel = chart_panel
        self.__func = func
        self.__color = color

        self.clicked.connect(self.__update_chart_panel)

    def __update_chart_panel(self):
        name = self.text()
        self.__chart_panel.add_new_plot(self.__func, name, self.__color)

        self.__create_and_add_icon_to_btn()

    def __create_and_add_icon_to_btn(self, width=30, height=15):
        rectangle_shape = ((0, 0), (width - 1, height - 1))

        rectangle = Image.new("RGBA", (width, height))
        rectangle_img = ImageDraw.Draw(rectangle)
        rectangle_img.rectangle(rectangle_shape, fill=self.__color)

        rectangle_qt = ImageQt(rectangle)
        rectangle_pixmap = QPixmap.fromImage(rectangle_qt)
        rectangle_icon = QIcon(rectangle_pixmap)

        self.setIcon(rectangle_icon)


class ButtonsPanel(QGroupBox):
    __COLORS = ["blue", "green", "red", "cyan", "magenta", "yellow", "black"]

    def __init__(self, chart_panel):
        super().__init__()
        self.__chart_panel = chart_panel
        self.__buttons = []

        self.__prepare_buttons_grid()

    def __prepare_buttons_grid(self):
        self.__create_rand_func_buttons()
        layout = QVBoxLayout()

        for btn in self.__buttons:
            layout.addWidget(btn)

        self.setLayout(layout)

    def __create_rand_func_buttons(self):
        start, end = 1, 10
        num_of_buttons = random.randint(start, end)

        for i in range(num_of_buttons):
            colour = self.__find_rand_color()

            rand_func = self.__create_rand_func()

            btn = RandFuncButton(str(i), rand_func, colour, self.__chart_panel)
            self.__buttons.append(btn)

    def __find_rand_color(self):
        color_id = random.randint(0, len(self.__COLORS) - 1)
        color = self.__COLORS[color_id]

        return color

    def __create_rand_func(self):
        a = random.random()
        b = random.random()
        c = random.random()

        sign_threshold = 0.5
        a_sign = 1 if random.random() > sign_threshold else -1

        func = (lambda a_sign, a, b, c: lambda x: (a_sign * a) * (x ** 2) + (b * x) + c)(a_sign, a, b, c)

        return func


class Candies(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__init_default_value()

        self.setWindowTitle("Candies example")
        self.setGeometry(self.__padding_x, self.__padding_y, self.__width, self.__height)

        self.__init_view()

        self.show()

    def __init_default_value(self):
        self.__padding_x = 300
        self.__padding_y = 300
        self.__width = 800
        self.__height = 600

    def __init_view(self):
        chart_panel = CandiesChart()
        buttons_panel = ButtonsPanel(chart_panel)

        main_layout = QGridLayout()
        main_layout.addWidget(chart_panel, 0, 0)
        main_layout.addWidget(buttons_panel, 0, 1)

        main_widget = QWidget(self)
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)


def main():
    app = QApplication([])

    candies = Candies()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
