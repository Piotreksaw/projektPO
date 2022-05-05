import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGroupBox

from modules.buttons import PdfSaveButton
from modules.diagrams import HardcodedSin


class PdfApp(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.__init_view(width, height)
        self.__prepare_hardcoded_chart()
        self.__prepare_pdf_gen_button()

    def __init_view(self, width, height):
        self.setWindowTitle("Hardcoded chart of sin(x)")

        self.__layout = QVBoxLayout()
        elems = QGroupBox()
        elems.setLayout(self.__layout)

        self.setFixedSize(width, height)
        self.setCentralWidget(elems)
        self.show()

    def __prepare_hardcoded_chart(self):
        self.__chart = HardcodedSin()
        self.__layout.addWidget(self.__chart)

    def __prepare_pdf_gen_button(self):
        pdf_btn = PdfSaveButton("Save as PDF", self.__chart)
        self.__layout.addWidget(pdf_btn)


if __name__ == "__main__":
    app = QApplication([])

    window_width, window_height = 600, 400
    pdf_app = PdfApp(window_width, window_height)

    sys.exit(app.exec_())
