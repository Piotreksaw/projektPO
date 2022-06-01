import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from glowne_pliki.main.buttons import Export_and_something_buttons
from tabs import Tabs
from glowne_pliki.main.list_of_countries import ButtonsPanel
from glowne_pliki.charts.chart import CreateChart
from glowne_pliki.main.doubleslider import SliderApp
from glowne_pliki.file_loader.file_loader import FileLoader


# klasa tworząca główne okno
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        width = 1500
        height = 800
        name = "Energio-Map"
        # Nadanie wielkości dla okna oraz tytułu
        self.resize(width, height)
        self.setWindowTitle(name)
        self.__prepare_window()

    # metoda tworząca obiekty do dodania do obszaru
    def __prepare_window(self):
        self.__name = "Select file to read"
        self.__fileloader = FileLoader(self.__name)
        self.__chart = CreateChart()
        self.__filepath = self.__fileloader.maybe_selected_file
        self.__buttons = Export_and_something_buttons(self.__chart, self.__fileloader)
        self.__button_panel = ButtonsPanel(self.__chart, self.__filepath)
        self.__slider = SliderApp(self.__chart, self.__filepath, self.__button_panel)
        self.__tabs = Tabs(self.__chart)
        # wywołanie metody dodającej widgety
        self.__adding_widgets()

    # metoda służąca do dodania widgetów do obszaru
    def __adding_widgets(self):
        main_layout = QGridLayout()
        main_layout.addWidget(self.__tabs, 0, 0, 1, 9)
        main_layout.addWidget(self.__buttons, 2, 0, 1, 9)
        main_layout.addWidget(self.__button_panel, 0, 10, 3, 2)
        main_layout.addWidget(self.__slider, 1, 0, 1, 9)
        main_layout.addLayout(self.__fileloader, 3, 0)

        self.setLayout(main_layout)
        self.show()


# metoda wywołująca główne okno, miłe puszczenie oczka do programistów C
def main():
    app = QApplication([])
    main_window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
