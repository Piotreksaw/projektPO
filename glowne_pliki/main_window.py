import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QGroupBox, QLineEdit
# from PyQt5 import QtCore
from buttons import Map_and_Chart_buttons, Export_and_something_buttons


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        width = 500
        height = 300
        name = "program"

        self.resize(width, height)
        self.setWindowTitle(name)
        self.__prepare_window()

    def __prepare_window(self):
        self.__buttons1 = Map_and_Chart_buttons()
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


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    sys.exit(app.exec_())
