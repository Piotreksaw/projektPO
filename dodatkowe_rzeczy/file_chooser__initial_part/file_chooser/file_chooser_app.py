from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout

from  projektPO.dodatkowe_rzeczy.file_chooser__initial_part.file_chooser.components.chart_panel import ChartPanel


class FileChooserApp(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__init_default_values()
        self.__init_view()

        self.show()



    def __init_view(self):
        self.setWindowTitle("FileChooserApp Example")
        self.setGeometry(self.__padding_x, self.__padding_y, self.__width, self.__height)

        main_layout = self.__config_main_layout()
        self.__add_widgets_to_main_layout(main_layout)

    def __config_main_layout(self):
        main_layout = QGridLayout()
        main_widget = QWidget(self)
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

        return main_layout

    def __add_widgets_to_main_layout(self, main_layout):
        file_loader_name = "Select file"
        self.__chart_panel = ChartPanel()
        self.__file_loader = FileLoader(file_loader_name)

        main_layout.addWidget(self.__chart_panel, 0, 0)
        main_layout.addLayout(self.__file_loader, 0, 1)
