import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QGridLayout, QGroupBox
from PyQt5 import QtCore


class TextPanel(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setAlignment(QtCore.Qt.AlignRight)
        self.setReadOnly(True)
        self.setText("hello")