import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QSlider, QGridLayout, QLabel
from PyQt5.Qt import Qt
from PyQt5.QtGui import QFont
from projektPO.glowne_pliki.FileReader import FileReader
from projektPO.glowne_pliki.Charts.chart import UpdateDataFromSlider

class DoubleSlider(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__file = FileReader("eurostat.csv")
        self.__a = self.__file.get_dates()
        self.__min_val = self.__a.index(self.__a[0])
        self.__max_val = self.__a.index(self.__a[-1])

        self.__create_view()





    def __create_label1(self):
        label1 = QLabel()
        label1.setFont(QFont("Sanserif", 13))
        label1.setText(str(self.__a[self.__min_val]))
        return label1

    def __create_label2(self):
        label2 = QLabel()
        label2.setFont(QFont("Sanserif", 13))
        label2.setText((str(self.__a[self.__max_val])))
        return label2


    def __create_view(self):
        self.__slider_from = self.__create_slider_from()
        self.__slider_to = self.__create_slider_to()
        self.__label1 = self.__create_label1()
        self.__label2 = self.__create_label2()
        # self.__slider_from.valueChanged.connect(self.get_current_from_value)
        # self.__slider_to.valueChanged.connect(self.get_current_to_value)

        layout = QGridLayout()
        layout.addWidget(self.__slider_from,0,0)
        layout.addWidget(self.__slider_to,1,0)
        layout.addWidget(self.__label1,0,1)
        layout.addWidget(self.__label2,1,1)

        self.setLayout(layout)


    def __create_slider_from(self):

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(self.__min_val)
        slider.setMaximum(self.__max_val)
        slider.setTickInterval(1)
        slider.setTickPosition(QSlider.TicksBelow)

        slider.setValue(self.__min_val)
        slider.valueChanged.connect(self.__handle_from_change)
        # slider.valueChanged.connect(self.data_pusher())
        #tutaj nie działa!!!

        # slider.valueChanged.connect(self.__pushing_values_forward


        return slider

    def __create_slider_to(self):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(self.__min_val)
        slider.setMaximum(self.__max_val)
        slider.setTickInterval(1)
        slider.setTickPosition(QSlider.TicksBelow)

        slider.setValue(self.__max_val)

        slider.valueChanged.connect(self.__handle_to_change)

        # slider.valueChanged.connect(self.data_pusher())
        # print(self.__handle_from_change())

        return slider

    def __handle_from_change(self):
        value_from = self.__slider_from.value()
        value_to = self.__slider_to.value()

        self.__label1.setText((str(self.__a[value_from])))

        if value_from > value_to:
            self.__slider_to.setValue(value_from )
        self.data_pusher()
        return value_from


    def __handle_to_change(self):
        value_from = self.__slider_from.value()
        value_to = self.__slider_to.value()

        self.__label2.setText(str(self.__a[value_to]))
        # self.get_current_to_value()
        if value_to < value_from:
            self.__slider_from.setValue(value_to)
        self.data_pusher()

    def get_current_from_value(self):
        # print(self.__slider_from.value())
        return self.__slider_from.value()

    def get_current_to_value(self):

        return self.__slider_to.value()

    def data_pusher(self):
        min_val = self.get_current_from_value()
        max_val = self.get_current_to_value()

        self.__update_method(min_val, max_val)



class SliderApp(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__init_view()
        # self.show()

    def __init_view(self):
        # self.setWindowTitle("double slider")
        # self.setGeometry(100,100,960,100)

        main_layout = QGridLayout()
        main_widget = QWidget(self)
        main_widget.setLayout(main_layout)

        self.__add_widgets_to_main_layout(main_layout)
        self.setLayout(main_layout)
        # self.setCentralWidget(main_widget)

    def __add_widgets_to_main_layout(self, main_layout):
        self.__double_slider_widget = DoubleSlider()
        main_layout.addWidget(self.__double_slider_widget)


# def main():
#     app = QApplication([])
#     slider_app = SliderApp()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     main()
