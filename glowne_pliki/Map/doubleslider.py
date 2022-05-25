import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QSlider, QGridLayout, QLabel
from PyQt5.Qt import Qt
from PyQt5.QtGui import QFont

class DoubleSlider(QWidget):

    def __init__(self, parent=None, min_val=0, max_val=29):
        super().__init__(parent)

        self.__min_val = min_val
        self.__max_val = max_val
        self.__create_view()

    def __create_label1(self):
        label1 = QLabel()
        label1.setFont(QFont("Sanserif", 13))
        return label1

    def __create_label2(self):
        label2 = QLabel()
        label2.setFont(QFont("Sanserif", 13))
        return label2


    def __create_view(self):
        self.__slider_from = self.__create_slider_from()
        self.__slider_to = self.__create_slider_to()
        self.__label1 = self.__create_label1()
        self.__label2 = self.__create_label2()

        layout = QGridLayout()
        layout.addWidget(self.__slider_from,0,0)
        layout.addWidget(self.__slider_to,1,0)
        layout.addWidget(self.__label1,0,1)
        layout.addWidget(self.__label2,1,1)

        self.setLayout(layout)


    def __create_slider_from(self):

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(self.__min_val)
        slider.setMaximum(self.__max_val-1)
        slider.setTickInterval(1)
        slider.setTickPosition(QSlider.TicksBelow)

        slider.setValue(self.__min_val)
        slider.valueChanged.connect(self.__handle_from_change)

        return slider

    def __create_slider_to(self):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(self.__min_val+1)
        slider.setMaximum(self.__max_val)
        slider.setTickInterval(1)
        slider.setTickPosition(QSlider.TicksBelow)

        slider.setValue(self.__max_val)
        slider.valueChanged.connect(self.__handle_to_change)

        return slider

    def __handle_from_change(self):
        value_from = self.__slider_from.value()
        value_to = self.__slider_to.value()
        a = ("2007-S1","2007-S2","2008-S1","2008-S2","2009-S1","2009-S2","2010-S1","2010-S2","2011-S1","2011-S2","2012-S1","2012-S2","2013-S1","2013-S2","2014-S1","2014-S2","2015-S1","2015-S2","2016-S1","2016-S2","2017-S1","2017-S2","2018-S1","2018-S2","2019-S1","2019-S2","2020-S1","2020-S2","2021-S1","2021-S2")

        self.__label1.setText((str(a[value_from])))

        if value_from >= value_to:
            self.__slider_to.setValue(value_from + 1)

    def __handle_to_change(self):
        value_from = self.__slider_from.value()
        value_to = self.__slider_to.value()
        a = ("2007-S1","2007-S2","2008-S1","2008-S2","2009-S1","2009-S2","2010-S1","2010-S2","2011-S1","2011-S2","2012-S1","2012-S2","2013-S1","2013-S2","2014-S1","202014-S2","2015-S1","2015-S2","2016-S1","2016-S2","2017-S1","2017-S2","2018-S1","2018-S2","2019-S1","2019-S2","2020-S1","2020-S2","2021-S1","2021-S2")

        self.__label2.setText(str(a[value_to]))

        if value_to <= value_from:
            self.__slider_from.setValue(value_to - 1)


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

        self.setCentralWidget(main_widget)

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
