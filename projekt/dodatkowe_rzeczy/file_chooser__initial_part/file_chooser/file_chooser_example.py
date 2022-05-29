import sys

from PyQt5.QtWidgets import QApplication

from projektPO.dodatkowe_rzeczy.file_chooser__initial_part.file_chooser.file_chooser_app import FileChooserApp


def main():
    app = QApplication([])

    file_chooser_app = FileChooserApp()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
