import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QGroupBox, QLineEdit, QTabWidget
# from PyQt5 import QtCore
from buttons import Export_and_something_buttons
from PyQt5. QtCore import pyqtSlot
from tabs import Tabs
from list_of_countries import ButtonsPanel
from Charts.chart import CreateChart
#from Map.doubleslider import SliderApp

from Charts.chart import CreateChart, UpdateDataFromSlider
from Map.doubleslider import SliderApp
from projektPO.dodatkowe_rzeczy.file_chooser__initial_part.file_chooser.components.file_loader import FileLoader





from Charts.chart import CreateChart, UpdateDataFromSlider
from Map.doubleslider import SliderApp
from projektPO.dodatkowe_rzeczy.file_chooser__initial_part.file_chooser.components.file_loader import FileLoader


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        width = 1500
        height = 800
        name = "program"


        self.resize(width, height)
        self.setWindowTitle(name)
        # self.tab_widget = Tabs(self)
        self.__prepare_window()


    def __prepare_window(self):
        # filepath = klasa do danych
        self.__name = "hej"
        self.__update = UpdateDataFromSlider()
        self.__slider = SliderApp(self.__update.push_data_to_chart)
        self.__chart = CreateChart(self.__update.get_boarders)
        self.__tabs = Tabs(self.__chart)
        self.__buttons2 = Export_and_something_buttons()
        self.__button_panel = ButtonsPanel(self.__chart)

        self.__slider = SliderApp()
        self.__loader = FileLoader(self.__name)

        main_layout = QGridLayout()
        main_layout.addWidget(self.__tabs, 0, 0, 1, 9)
        main_layout.addWidget(self.__buttons2, 2, 0, 1, 9 )
        main_layout.addWidget(self.__button_panel, 0, 10, 3, 2 )
        main_layout.addWidget(self.__slider, 1, 0, 1,9 )
        # main_layout.addLayout(self.__loader, 3,0)



        self.setLayout(main_layout)
        self.show()


def main():
    app = QApplication([])
    main_window = MainWindow()

    sys.exit(app.exec_())


if __name__ == "__main__":
   main()