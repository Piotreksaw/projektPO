import os
import sys

from PyQt5.QtWidgets import QPushButton, QFileDialog
from reportlab.lib.utils import ImageReader
from pdf_generator import PdfReportGenerator


class PdfSaveButton(QPushButton):
    def __init__(self, name, chart):
        super().__init__(name)
        self.__chart = chart
        self.__pdf_generator = PdfReportGenerator()

        self.clicked.connect(self.__save_btn_action)

    def __save_btn_action(self):
        img_data = self.__chart.get_img()
        img = ImageReader(img_data)

        filename = self.__prepare_file_chooser()
        if filename:
            self.__pdf_generator.create_and_save_report(img, filename)
        else:
            print("nie wybrano lokalizacji")
            return


    def __prepare_file_chooser(self):
        options = QFileDialog.DontUseNativeDialog
        parent = None
        current_dir = os.path.dirname(sys.argv[0])
        filename, _ = QFileDialog.getSaveFileName(parent, "Save PDF report", current_dir, filter="PDF (*.pdf)")
        return filename