import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QGroupBox, QLineEdit, QTabWidget
# from PyQt5 import QtCore
from buttons import Map_and_Chart_buttons, Export_and_something_buttons
from PyQt5. QtCore import pyqtSlot


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        width = 500
        height = 300
        name = "program"

        self.resize(width, height)
        self.setWindowTitle(name)
        # self.tab_widget = Tabs(self)
        self.__prepare_window()

    def __prepare_window(self):
        self.__buttons1 = Tabs(self)
        self.__buttons2 = Export_and_something_buttons()
        # self.__map = Map
        # self.__chart = Chart
        # self.__list = List

        main_layout = QGridLayout()
        main_layout.addWidget(self.__buttons1, 0, 0)
        main_layout.addWidget(self.__buttons2, 1, 0)
        # main_layout.addWidget(self.__list, 2, 2)

        self.setLayout(main_layout)
        self.show()

class Tabs(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(50, 50)
        self.tabs.addTab(self.tab1, "Wykres")
        self.tabs.addTab(self.tab2, "Mapa")
        self.tab1.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()

    sys.exit(app.exec_())
