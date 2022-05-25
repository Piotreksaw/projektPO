from PyQt5.QtWidgets import QPushButton, QGroupBox, QGridLayout
from text_panel import TextPanel as TP


class create_button(QPushButton):
    def __init__(self,word):
        super().__init__(word)


class Export_to_pdf_button(create_button):
    def __init__(self):
        super().__init__("Export to PDF")


class Something_button(create_button):
    def __init__(self):
        super().__init__("insert file")

class Export_and_something_buttons(QGroupBox):
    def __init__(self):
        super().__init__()
        # self.__text_panel = text_panel
        self.__prepare_buttons()

    def __prepare_buttons(self):
        self.__create_text_button()
        layout = QGridLayout()

        layout.addWidget(self.__button2, 0, 0, 1, 1)
        layout.addWidget(self.__button1, 0, 1, 1, 1)
        layout.addWidget(self.__text_panel, 0, 2, 1, 2)

        self.setLayout(layout)

    def __create_text_button(self):
        self.__button1 = Export_to_pdf_button()
        self.__button2 = Something_button()
        self.__text_panel = TP()
