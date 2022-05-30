import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QSlider, QGridLayout, QLabel
from PyQt5.Qt import Qt
from PyQt5.QtGui import QFont
from glowne_pliki.file_reader import FileReader
from glowne_pliki.Charts.chart import CreateChart

class DoubleSlider(QWidget):

    def __init__(self, chart_panel, filrpath, parent=None):
        super().__init__(parent)
        self.__chart_panel = chart_panel
        self.__file = FileReader(filrpath)
        self.__a = self.__file.get_dates()
        print(self.__a)
        self.__min_val = self.__a.index(self.__a[0])
        print(self.__min_val)
        self.__max_val = self.__a.index(self.__a[-1])
        print(self.__max_val)
        self.__create_view()

    # klasy tworzące okno pokazujące obecne daty wybrane przez użytkownika
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


    # klasa tworząca cały widok slidera
    def __create_view(self):
        self.__slider_from = self.__create_slider_from()
        self.__slider_to = self.__create_slider_to()
        self.__label1 = self.__create_label1()
        self.__label2 = self.__create_label2()
        self.__create_layout()




    def __create_layout(self):
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

        return slider

    def __create_slider_to(self):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(self.__min_val)
        slider.setMaximum(self.__max_val)
        slider.setTickInterval(1)
        slider.setTickPosition(QSlider.TicksBelow)

        slider.setValue(self.__max_val)

        slider.valueChanged.connect(self.__handle_to_change)

        return slider

    def __handle_from_change(self):
        value_from = self.__slider_from.value()
        value_to = self.__slider_to.value()

        self.__label1.setText((str(self.__a[value_from])))

        if value_from > value_to:
            self.__slider_to.setValue(value_from )
        self.__chart_panel.get_start(value_from)
        return value_from


    def __handle_to_change(self):
        value_from = self.__slider_from.value()
        value_to = self.__slider_to.value()

        self.__label2.setText(str(self.__a[value_to]))
        # self.get_current_to_value()
        if value_to < value_from:
            self.__slider_from.setValue(value_to)
        self.__chart_panel.get_end(value_to)





class SliderApp(QWidget):

    def __init__(self, chart_panel, filepath, parent=None):
        super().__init__(parent)
        self.chart_panel = chart_panel
        self.__filepath = filepath

        self.__init_view()
        # self.show()

    def __init_view(self):


        main_layout = QGridLayout()
        main_widget = QWidget(self)
        main_widget.setLayout(main_layout)

        self.__add_widgets_to_main_layout(main_layout)
        self.setLayout(main_layout)
        # self.setCentralWidget(main_widget)

    def __add_widgets_to_main_layout(self, main_layout):
        self.__double_slider_widget = DoubleSlider(self.chart_panel, self.__filepath)
        main_layout.addWidget(self.__double_slider_widget)
