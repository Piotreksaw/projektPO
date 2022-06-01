from PyQt5.QtWidgets import QGroupBox, QGridLayout
from text_panel import TextPanel as TP
from glowne_pliki.pdf_packet.pdf_save_btn import PdfSaveButton


# klasa tworząca ukłąd przycisków do wczytania pliku i eksportowania wykresu do pdfa
class Export_and_something_buttons(QGroupBox):
    def __init__(self, chart, fileloader):
        super().__init__()
        self.__chart = chart
        self.__fileloader = fileloader
        # użycie metody tworzącaj układ
        self.__prepare_buttons()


    def __prepare_buttons(self):
        self.__create_button()
        # ustawienie przycisków jako grid
        layout = QGridLayout()
        # dodanie widgetów
        layout.addLayout(self.__file_loader_button, 0, 0, 1, 1)
        layout.addWidget(self.__pdf_save_btn, 0, 1, 1, 1)
        layout.addWidget(self.__text_panel, 0, 2, 1, 2)

        self.setLayout(layout)

    def __create_button(self):
        # stworzenie/wywołanie obiektów dodanych do widgetu
        self.__pdf_save_btn = PdfSaveButton("Save to PDF", self.__chart)
        self.__file_loader_button = self.__fileloader
        self.__text_panel = TP()
