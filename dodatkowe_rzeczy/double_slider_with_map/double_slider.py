import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QSlider, QGridLayout, QVBoxLayout
from PyQt5.Qt import Qt

class DoubleSlider(QWidget):

    def __init__(self, parent=None, min_val=0, max_val=100):
        super().__init__(parent)
        self.__validate_args(min_val, max_val)

        self.__min_val = min_val
        self.__max_val = max_val

        self.__create_view()

    def __validate_args(self, min_val, max_val):
        if min_val >= max_val:
            raise Exception("Wrong values! max_val cannot be lower than min_val.")

    def __create_view(self):
        self.__slider_from = self.__create_slider_from()
        self.__slider_to = self.__create_slider_to()

        layout = QVBoxLayout()
        layout.addWidget(self.__slider_from)
        layout.addWidget(self.__slider_to)

        self.setLayout(layout)


    def __create_slider_from(self):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(self.__min_val)
        slider.setMaximum(self.__max_val - 1)

        slider.setValue(self.__min_val)
        slider.valueChanged.connect(self.__handle_from_change)

        return slider

    def __create_slider_to(self):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(self.__min_val + 1)
        slider.setMaximum(self.__max_val)

        slider.setValue(self.__max_val)
        slider.valueChanged.connect(self.__handle_to_change)

        return slider

    def __handle_from_change(self):
        print(f"Value from: {self.__slider_from.value()}")
        value_from = self.__slider_from.value()
        value_to = self.__slider_to.value()

        if value_from >= value_to:
            self.__slider_to.setValue(value_from + 1)

    def __handle_to_change(self):
        print(f"Value to: {self.__slider_to.value()}")
        value_from = self.__slider_from.value()
        value_to = self.__slider_to.value()

        if value_to <= value_from:
            self.__slider_from.setValue(value_to - 1)

        
class SliderApp(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__init_default_value()
        self.__init_view()

        self.show()

    def __init_default_value(self):
        self.__padding_x = 100
        self.__padding_y = 100
        self.__width = 960
        self.__height = 600


    def __init_view(self):
        self.setWindowTitle("Slider example")
        self.setGeometry(self.__padding_x, self.__padding_y, self.__width, self.__height)

        main_layout = QGridLayout()
        main_widget = QWidget(self)
        main_widget.setLayout(main_layout)

        self.__add_widgets_to_main_layout(main_layout)

        self.setCentralWidget(main_widget)

    def __add_widgets_to_main_layout(self, main_layout):
        self.__double_slider_widget = DoubleSlider()

        main_layout.addWidget(self.__double_slider_widget, 0, 0)


def main():
    app = QApplication([])

    slider_app = SliderApp()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
