import os
import sys

from PyQt5.QtWidgets import QPushButton, QProgressBar, QFileDialog, QHBoxLayout

from  projektPO.dodatkowe_rzeczy.file_chooser__initial_part.file_chooser.components.io import FileReader


class FileLoader(QHBoxLayout):

    def __init__(self, btn_name):
        super().__init__()

        self.__create_all(btn_name)

    def __create_all(self, btn_name, parent=None):
        self.__file_loader_dialog_btn = self.__create_file_loader_dialog_btn(btn_name)
        self.__loader = QProgressBar(parent)

        self.addWidget(self.__file_loader_dialog_btn)
        self.addWidget(self.__loader)

    def __create_file_loader_dialog_btn(self, btn_name):
        loader_btn = QPushButton(btn_name)
        loader_btn.clicked.connect(self.__choose_and_read_file)

        return loader_btn

    def __choose_and_read_file(self):
        self.__loader.setValue(1)
        parent = None
        current_dir = os.path.dirname(sys.argv[0])
        self.__loader.setValue(10)
        options = QFileDialog.DontUseNativeDialog
        self.__loader.setValue(20)
        maybe_selected_file, _ = QFileDialog.getOpenFileName(parent, "Choose csv file",
                                                             current_dir, "CSV (*.csv);;All Files (*)",
                                                             options=options)
        self.__loader.setValue(40)
        print(maybe_selected_file)
        if maybe_selected_file:
            self.__loader.setValue(50)
            file_reader = FileReader(maybe_selected_file)
            # file_reader.read()
            self.__loader.setValue(100)
        else:
            print("sth wrong???")
            self.__loader.setValue(1)
