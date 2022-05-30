from PyQt5.QtWidgets import QPushButton, QGroupBox, QGridLayout
from text_panel import TextPanel as TP
from file_loader import FileLoader
from pdf_save_btn import PdfSaveButton


class Export_and_something_buttons(QGroupBox):
    def __init__(self, chart, filepath):
        super().__init__()
        # self.__text_panel = text_panel
        self.__chart = chart
        self.__filepath = filepath
        self.__prepare_buttons()


    def __prepare_buttons(self):
        self.__create_text_button()
        layout = QGridLayout()
        layout.addLayout(self.__file_loader_button, 0, 0, 1, 1)
        layout.addWidget(self.__pdf_save_btn, 0, 1, 1, 1)
        layout.addWidget(self.__text_panel, 0, 2, 1, 2)

        self.setLayout(layout)

    def __create_text_button(self):

        self.__pdf_save_btn = PdfSaveButton("Save to PDF", self.__chart)
        # self.__file_loader_button = FileLoader("Select file")
        self.__file_loader_button = self.__filepath
        self.__text_panel = TP()



