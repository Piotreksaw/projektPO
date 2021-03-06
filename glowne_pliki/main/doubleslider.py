import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QSlider, QGridLayout, QLabel
from PyQt5.Qt import Qt
from PyQt5.QtGui import QFont
from file_reader import FileReader


class DoubleSlider(QWidget):

    def __init__(self, chart_panel, filepath, list_of_buttons, parent=None):
        super().__init__(parent)
        self.__chart_panel = chart_panel
        self.list_of_buttons = list_of_buttons
        self.__file = FileReader(filepath)

        # wywołanie listy dat która zostanie przekazana dalej do przycisków
        self.__a = self.__file.get_dates()
        self.__min_val = self.__a.index(self.__a[0])
        self.__max_val = self.__a.index(self.__a[-1])

        self.__create_view()

    # klasy tworzące okno pokazujące obecne daty wybrane przez użytkownika
    def __create_label1(self):
        label1 = QLabel()
        label1.setFont(QFont("Sanserif", 12))
        label1.setText(str(self.__a[self.__min_val]))
        return label1

    def __create_label2(self):
        label2 = QLabel()
        label2.setFont(QFont("Sanserif", 12))
        label2.setText((str(self.__a[self.__max_val])))
        return label2

    # metoda tworząca tworząca obiekty
    def __create_view(self):
        self.__slider_from = self.__create_slider_from()
        self.__slider_to = self.__create_slider_to()
        self.__label1 = self.__create_label1()
        self.__label2 = self.__create_label2()
        # wywołanie metody tworzącej układ
        self.__create_layout()

    # metoda tworząca układ z obiektów powyżej stworzonych
    def __create_layout(self):
        layout = QGridLayout()
        layout.addWidget(self.__slider_from, 0, 0)
        layout.addWidget(self.__slider_to, 1, 0)
        layout.addWidget(self.__label1, 0, 1)
        layout.addWidget(self.__label2, 1, 1)

        self.setLayout(layout)

    # metody tworzące slider
    def __create_slider_from(self):

        slider = QSlider(Qt.Horizontal)
        # usawienie wartości minimalnych i maksymalnych
        slider.setMinimum(self.__min_val)
        slider.setMaximum(self.__max_val)
        slider.setTickInterval(1)
        slider.setTickPosition(QSlider.TicksBelow)
        # ustawienie początkowe slidera na pozycje początkową
        slider.setValue(self.__min_val)
        # klinięcie powoduje zmianę wartości używanego indeksu slidera
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

    # metoda odpowiadająca za zaktualizowanie slidera, oraz panelu tektowego
    def __handle_from_change(self):
        value_from = self.__slider_from.value()
        value_to = self.__slider_to.value()
        self.__label1.setText((str(self.__a[value_from])))

        if value_from > value_to:
            self.__slider_to.setValue(value_from)

        # wywołanie metody wykresu zwracająca początek przedziału czasu dla wykresu
        self.__chart_panel.get_start(value_from)
        # wywołanie metody panelu przycisku która została opisana w pliku list_of_countries.py
        self.list_of_buttons.changing_boundaries()

        return value_from

    def __handle_to_change(self):
        value_from = self.__slider_from.value()
        value_to = self.__slider_to.value()
        # ustawienie napisu obok slidera i aktualizcja go
        self.__label2.setText(str(self.__a[value_to]))

        if value_to < value_from:
            self.__slider_from.setValue(value_to)

        # metoda wykresu która zwraca koniec przedziłu dla wykresu
        self.__chart_panel.get_end(value_to)
        # metoda listy przycisków która po przesunieciu slidera zaktualizuje pole wykresu
        self.list_of_buttons.changing_boundaries()
        return value_to


class SliderApp(QWidget):

    def __init__(self, chart_panel, filepath, list_of_buttons, parent=None):
        super().__init__(parent)
        # wywołanie kreatorów
        self.chart_panel = chart_panel
        self.__filepath = filepath
        self.list_of_buttons = list_of_buttons
        # wywołanie układ
        self.__init_view()

    def __init_view(self):
        main_layout = QGridLayout()
        main_widget = QWidget(self)
        main_widget.setLayout(main_layout)

        self.__add_widgets_to_main_layout(main_layout)
        # ustawienie końcowe układu
        self.setLayout(main_layout)

    # metoda dodająca widget stworzony w klasie DoubleSlider tworząca układ
    def __add_widgets_to_main_layout(self, main_layout):
        self.__double_slider_widget = DoubleSlider(self.chart_panel, self.__filepath, self.list_of_buttons)
        main_layout.addWidget(self.__double_slider_widget)
