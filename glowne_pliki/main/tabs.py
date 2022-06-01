from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget


# klasa służąca do stworzenia kart do przełączania się pomiędzy mapą a wykresem
class Tabs(QWidget):
    def __init__(self, chart, map):
        super().__init__()
        self.__chart = chart
        self.__map = map

        # ustawienie układu jako poziomy układ
        self.layout = QVBoxLayout(self)
        # stworzenie obiektów
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(100, 100)
        # stworzenie dwóch kart
        self.tabs.addTab(self.tab1, "Wykres")
        self.tabs.addTab(self.tab2, "Mapa")
        self.tab1.layout = QVBoxLayout()
        # ustawienie w pierwszej karcie wykeresu
        self.tab1.layout.addWidget(self.__chart)
        self.tab1.setLayout(self.tab1.layout)
        self.tab2.layout = QVBoxLayout()
        # ustawienie w drugiej karcie mapy
        self.tab2.layout.addWidget(self.__map)
        self.tab2.setLayout(self.tab2.layout)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
