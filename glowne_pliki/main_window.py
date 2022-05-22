import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QGroupBox, QLineEdit, QTabWidget
# from PyQt5 import QtCore
from buttons import Export_and_something_buttons
from PyQt5. QtCore import pyqtSlot
from tabs import Tabs
from list_of_countries import ButtonsPanel



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
        self.__tabs = Tabs()
        self.__buttons2 = Export_and_something_buttons()
        __button_panel = ButtonsPanel()

        main_layout = QGridLayout()
        main_layout.addWidget(self.__tabs, 0, 0)
        main_layout.addWidget(self.__buttons2, 1, 0)
        main_layout.addWidget(__button_panel, 0, 1, 2, 2)
        # main_layout.addWidget(self.__list, 2, 2)

        self.setLayout(main_layout)
        self.show()

def main():
    app = QApplication([])
    main_window = MainWindow()

    sys.exit(app.exec_())


if __name__ == "__main__":
   main()