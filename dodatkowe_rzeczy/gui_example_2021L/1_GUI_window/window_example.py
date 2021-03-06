import sys

from PyQt5.QtWidgets import QApplication, QWidget


class EmptyView(QWidget):
    def __init__(self):
        super().__init__()
        width, height = 250, 150
        name = "nazwa"
        self.resize(width, height)
        self.setWindowTitle(name)
        self.show()


if __name__ == "__main__":
    app = QApplication([])

    empty_view = EmptyView()

    sys.exit(app.exec_())
