import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout, QGroupBox, QLineEdit
from PyQt5 import QtCore

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        width = 500
        height = 300
        name = "program"
        name2 = "hej"
        self.resize(width, height)
        self.setWindowTitle(name)
        self.__prepare_window()


    def __prepare_window(self):
        # self.__buttons = Buttons
        # self.__map = Map
        # self.__chart = Chart
        # self.__list = List

        main_layout = QGridLayout()
        main_layout.addWidget(self.__buttons, 1, 0)
        main_layout.addWidget(self.__map, 2, 1)
        main_layout.addWidget(self.__list, 2, 2)
        self.setLayout(main_layout)
        self.show()



if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    sys.exit(app.exec_())


