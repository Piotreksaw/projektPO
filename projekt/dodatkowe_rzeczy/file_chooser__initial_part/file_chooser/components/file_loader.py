import os
import sys

from PyQt5.QtWidgets import QPushButton, QFileDialog, QHBoxLayout


class FileLoader(QHBoxLayout):

    def __init__(self, btn_name):
        super().__init__()
        self.__create_all(btn_name)
        self.__selected_filepath = 'none'

    def __create_all(self, btn_name, parent=None):
        self.__file_loader_dialog_btn = self.__create_file_loader_dialog_btn(btn_name)

        self.addWidget(self.__file_loader_dialog_btn)

    def __create_file_loader_dialog_btn(self, btn_name):
        loader_btn = QPushButton(btn_name)
        loader_btn.clicked.connect(self.__choose_and_read_file)

        return loader_btn

    def __choose_and_read_file(self):
        parent = None
        current_dir = os.path.dirname(sys.argv[0])
        options = QFileDialog.DontUseNativeDialog
        maybe_selected_file, _ = QFileDialog.getOpenFileName(parent, "Choose csv file",
                                                             current_dir, "CSV (*.csv)",
                                                             options=options)
        if maybe_selected_file:
            f = open("filepath.txt","w+")
            f.write(maybe_selected_file)
            f.close()
        else:
            print("does not work")
