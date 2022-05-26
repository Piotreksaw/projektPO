from PyQt5.QtWidgets import QWidget, QVBoxLayout

from file_chooser.components.chart import Chart
from file_chooser.components.slider_elem import SliderElem


class ChartPanel(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__create_view()

    def __create_view(self, min_value=0.01, max_value=10, init_value=1):
        self.__chart = Chart(value_factor=init_value, period_factor=init_value)
        self.__value_factor_slider = SliderElem("a", min_value, max_value, init_value, self.__update_chart)
        self.__period_factor_slider = SliderElem("b", min_value, max_value, init_value, self.__update_chart)

        layout = QVBoxLayout()
        layout.addWidget(self.__chart)
        layout.addLayout(self.__value_factor_slider)
        layout.addLayout(self.__period_factor_slider)

        self.setLayout(layout)

        return layout

    def __update_chart(self):
        value_factor = self.__value_factor_slider.get_value()
        period_factor = self.__period_factor_slider.get_value()
        self.__chart.update_plot(value_factor, period_factor)
