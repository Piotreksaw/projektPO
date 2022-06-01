import os
import sys

from PyQt5.QtWidgets import QPushButton, QFileDialog, QHBoxLayout


class FileLoader(QHBoxLayout):

    def __init__(self, btn_name):
        super().__init__()
        self.__selected_filepath = 'none'

        self.__create_all(btn_name)
        self.maybe_selected_file = self.__choose_and_read_file()

# Stworzenie przycisku do wybrania pliku w postaci przycisku który można nacisnąć
    def __create_all(self, btn_name):
        self.__file_loader_dialog_btn = self.__create_file_loader_dialog_btn(btn_name)

        self.addWidget(self.__file_loader_dialog_btn)

# Stworzenie przycisku oraz dodanie instrukcji która jest wykonywania po naciśnięciu
    def __create_file_loader_dialog_btn(self, btn_name):
        loader_btn = QPushButton(btn_name)
        loader_btn.clicked.connect(self.__choose_and_read_file)

        return loader_btn

# Metoda otwierająca okno wyboru pliku oraz zwracająca ścieżkę dostępu do pliku
    def __choose_and_read_file(self):
        parent = None
        current_dir = os.path.dirname(sys.argv[0])
        options = QFileDialog.DontUseNativeDialog
        self.maybe_selected_file, _ = QFileDialog.getOpenFileName(parent, "Choose csv file",
                                                                  current_dir, "CSV (*.csv)",
                                                                  options=options)

        if self.maybe_selected_file:
            return self.maybe_selected_file
        else:
            pass
