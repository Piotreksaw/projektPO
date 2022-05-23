import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QGridLayout, QGroupBox
from PyQt5 import QtCore



class create_button(QPushButton):
    def __init__(self, word, text_panel: QLineEdit):
        super().__init__(word)
        self.__text_panel = text_panel
        self.__word = word

        self.clicked.connect(self.__printing_something)
        self.clicked.connect(self.__update_text_field)

    def __printing_something(self):
        print("hej tutaj jest jakiś komunikat ez")

    def __update_text_field(self):
        #org_text = self.__text_panel.text()
        #org_text = "" if org_text == "" else org_text
        new_text = f"{self.__word}"
        self.__text_panel.setText(new_text)


class ButtonsOrSmth(QGroupBox):
    def __init__(self, text_panel):
        super().__init__()
        self.__text_panel = text_panel
        self.__prepare_buttons()

    def __prepare_buttons(self):
        self.__create_text_button()
        layout = QGridLayout()

        layout.addWidget(self.__button1, 0, 0, 1, 2)
        layout.addWidget(self.__button2, 1, 0)
        layout.addWidget(self.__button3, 1, 1)

        self.setLayout(layout)

    def __create_text_button(self):
        self.__button1 = create_button("click me", self.__text_panel)
        self.__button2 = create_button("do it", self.__text_panel)
        self.__button3 = create_button("please", self.__text_panel)


class TextPanel(QLineEdit):
    def __init__(self):
        super(TextPanel, self).__init__()
        self.setAlignment(QtCore.Qt.AlignRight)
        self.setReadOnly(True)
        self.setText("")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        width = 500
        height = 350
        name = "nazwa"
        self.resize(width, height)
        self.setWindowTitle(name)
        self.__prepare_window()

    def __prepare_window(self):
        self.__textPanel = TextPanel()
        self.__buttons = ButtonsOrSmth(self.__textPanel)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.__textPanel, 0, 0)
        mainLayout.addWidget(self.__buttons, 1, 0)

        self.setLayout(mainLayout)
        self.show()


if __name__ == "__main__":
    app = QApplication([])

    main_window = MainWindow()

    sys.exit(app.exec_())
