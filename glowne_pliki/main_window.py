import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from buttons import Export_and_something_buttons
from tabs import Tabs
from list_of_countries import ButtonsPanel
from projektPO.glowne_pliki.chart import CreateChart
from Map.doubleslider import SliderApp
from file_loader import FileLoader
from file_reader import FileReader

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
        self.__name = "program czasem działający"
        # self.__loader = FileLoader(self.__name)
        # self.__filepath = self.__loader.selected_filepath
        self.__chart = CreateChart()
        self.__fileloader = FileLoader(self.__name)
        self.__filepath = self.__fileloader.maybe_selected_file
        print(self.__filepath)
        self.__buttons = Export_and_something_buttons(self.__chart, self.__fileloader)

        # self.__readfile = FileReader(self.__filepath)
        self.__button_panel = ButtonsPanel(self.__chart, self.__filepath)
        self.__slider = SliderApp(self.__chart, self.__filepath)
        self.__tabs = Tabs(self.__chart)
        # self.__slider = SliderApp(self.__chart, self.__filepath)
        self.__adding_widgets()

    def __adding_widgets(self):

        main_layout = QGridLayout()
        main_layout.addWidget(self.__tabs, 0, 0, 1, 9)
        main_layout.addWidget(self.__buttons, 2, 0, 1, 9)
        main_layout.addWidget(self.__button_panel, 0, 10, 3, 2)
        main_layout.addWidget(self.__slider, 1, 0, 1, 9)
        main_layout.addLayout(self.__fileloader, 3, 0)

        self.setLayout(main_layout)
        self.show()


def main():
    app = QApplication([])
    main_window = MainWindow()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
