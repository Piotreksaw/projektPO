import random
import sys

from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtGui
from PyQt5.QtWidgets import *


class MosaicBtn(QLabel):

    def __init__(self, org_col, org_row, col, row, btn_size, full_img, main_window, current_matrix, empty_position,
                 btn_text=""):
        super().__init__(btn_text, main_window)

        self.__org_col = org_col
        self.__org_row = org_row
        self.__col = col
        self.__row = row
        self.__width = btn_size
        self.__height = btn_size

        self.__current_matrix = current_matrix
        self.__empty_position = empty_position

        self.__n_rows = len(current_matrix)
        self.__n_cols = len(current_matrix[0])

        self.__set_btn_background(full_img)
        self.__update_geometry()

    def mouseReleaseEvent(self, QMouseEvent):
        self.__move_if_possible()

    def __set_btn_background(self, full_img):
        img_part = self.__crop_img_part(full_img)
        img_part = img_part.convert("RGBA")
        qt_img_part = ImageQt(img_part)
        self.setPixmap(QtGui.QPixmap.fromImage(qt_img_part))

    def __crop_img_part(self, full_img):
        left = self.__org_col * self.__width
        right = left + self.__width - 1

        top = self.__org_row * self.__height
        bottom = top + self.__height - 1

        crop_box = (left, top, right, bottom)
        result_img = full_img.crop(crop_box)

        return result_img

    def __update_geometry(self):
        x = self.__col * self.__width
        y = self.__row * self.__height
        self.setGeometry(x, y, self.__width, self.__height)

    def __move_if_possible(self):
        x_step, y_step = self.__find_move_step()

        expect_any_move = x_step != 0 or y_step != 0

        if expect_any_move:
            new_row = self.__row + y_step
            new_col = self.__col + x_step

            self.__swap_to_empty_position_in_matrix(new_row, new_col)
            self.__update_geometry()

    def __find_move_step(self):
        x_step = 0
        y_step = 0

        if self.__is_empty_left():
            x_step -= 1

        elif self.__is_empty_right():
            x_step += 1

        elif self.__is_empty_top():
            y_step -= 1

        elif self.__is_empty_bottom():
            y_step += 1

        else:
            print(f"Cannot move (col: {self.__col}, row: {self.__row})!")

        return x_step, y_step

    def __is_empty_left(self):
        return self.__check_if_empty(self.__col - 1, self.__row)

    def __is_empty_right(self):
        return self.__check_if_empty(self.__col + 1, self.__row)

    def __is_empty_top(self):
        return self.__check_if_empty(self.__col, self.__row - 1)

    def __is_empty_bottom(self):
        return self.__check_if_empty(self.__col, self.__row + 1)

    def __check_if_empty(self, x, y):
        return 0 <= x < self.__n_cols \
               and 0 <= y < self.__n_rows \
               and self.__current_matrix[y][x] == self.__empty_position

    def __swap_to_empty_position_in_matrix(self, new_row, new_col):
        prev_position = self.__current_matrix[self.__row][self.__col]
        self.__current_matrix[new_row][new_col] = prev_position
        self.__current_matrix[self.__row][self.__col] = self.__empty_position

        self.__row = new_row
        self.__col = new_col


class MosaicMatrix:

    def __init__(self, main_window, n_cols, n_rows, btn_size, full_img):
        self.__main_window = main_window
        self.__n_cols = n_cols
        self.__n_rows = n_rows
        self.__btn_size = btn_size
        self.__full_img = full_img

        self.__init_matrices()
        self.__init_mosaic_buttons()

    def __init_matrices(self):
        matrix_data = self.__create_matrix_data()

        self.__final_matrix = self.__create_matrix_with_data(matrix_data)
        random.shuffle(matrix_data)
        self.__current_matrix = self.__create_matrix_with_data(matrix_data)

    def __create_matrix_data(self):
        matrix_data = [(c, r) for r in range(self.__n_rows) for c in range(self.__n_cols)]
        return matrix_data

    def __create_matrix_with_data(self, matrix_data):
        result_matrix = []
        row_matrix = []
        enum_start = 1

        for i, data in enumerate(matrix_data, enum_start):
            row_matrix.append(data)

            if i % self.__n_cols == 0:
                result_matrix.append(row_matrix)
                row_matrix = []

        return result_matrix

    def __init_mosaic_buttons(self):
        self.__buttons = []
        position_to_skip = (0, 0)

        for org_row, shuffled_row in zip(self.__final_matrix, self.__current_matrix):
            # Look below! Value from shuffled_row is org_position!!!
            for shuffled_position, org_position in zip(org_row, shuffled_row):

                if org_position == position_to_skip:
                    continue

                btn = MosaicBtn(*org_position, *shuffled_position,
                                self.__btn_size, self.__full_img, self.__main_window,
                                self.__current_matrix, position_to_skip)

                self.__buttons.append(btn)


class Mosaic(QMainWindow):

    def __init__(self, path_to_img, parent=None):
        super().__init__(parent)
        self.__init_default_value()

        self.setWindowTitle("Mosaic example")
        self.setGeometry(self.__padding_x, self.__padding_y, self.__width, self.__height)

        self.__init_view()
        img = self.__read_img_and_resize(path_to_img)
        self.__mosaic_matrix = MosaicMatrix(self, self.__cols, self.__rows, self.__btn_size, img)

        self.show()

    def __init_default_value(self):
        self.__btn_size = 150
        self.__rows = 3
        self.__cols = 3

        self.__padding_x = 200
        self.__padding_y = 200

        self.__width = self.__cols * self.__btn_size
        self.__height = self.__rows * self.__btn_size

    def __read_img_and_resize(self, path_to_img):
        with Image.open(path_to_img) as im:
            img = im.copy()

        img = img.resize((self.__width, self.__height))

        return img

    def __init_view(self):
        pass


if __name__ == "__main__":
    path_to_img = "imgs/gmach_elektrotechniki.png"

    app = QApplication([])
    mosaic = Mosaic(path_to_img)

    sys.exit(app.exec_())
