from PyQt5.QtWidgets import QPushButton, QGroupBox, QGridLayout


class create_button(QPushButton):
    def __init__(self, word):
        super().__init__(word)
        self.__word = word


class Map_button(create_button):
    def __init__(self, word):
        super().__init__(word)


class Chart_button(create_button):
    def __init__(self, word):
        super().__init__(word)


class Map_and_Chart_buttons(QGroupBox):
    def __init__(self):
        super().__init__()
        # self.__text_panel = text_panel
        self.__prepare_buttons()

    def __prepare_buttons(self):
        self.__create_text_button()
        layout = QGridLayout()

        layout.addWidget(self.__button1, 0, 0)
        layout.addWidget(self.__button2, 0, 1)

        self.setLayout(layout)

    def __create_text_button(self):
        self.__button1 = Map_button("Mapa")
        self.__button2 = Chart_button("Wykres")
