from io import BytesIO
from math import pi

import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class HardcodedSin(FigureCanvasQTAgg):
    __IMG_FORMAT = "png"

    def __init__(self, figsize=(4, 4), dpi=100):
        self.__fig = Figure(figsize=figsize, dpi=dpi)
        super().__init__(self.__fig)

        self.__init_fig()

    def get_img(self):
        img_data = BytesIO()
        self.__fig.savefig(img_data, format=self.__IMG_FORMAT)

        seek_offset = 0
        img_data.seek(seek_offset)

        return img_data

    def __init_fig(self):
        plot_config_id = 111
        self.__fig.add_subplot(plot_config_id)

        self.__fig.suptitle("Sin(x)")
        self.__plot_hardcoded_sin()
        self.__fig.tight_layout()

    def __plot_hardcoded_sin(self, start_x=0, end_x=2 * pi, n=100):
        x = np.linspace(start_x, end_x, n)
        sin_x = np.sin(x)

        ax = self.__fig.axes[0]

        ax.plot(x, sin_x, label="f. sin(x)")
        ax.set_xlim([start_x, end_x])
        self.__set_hardcoded_xtics(start_x, end_x, ax)

        ax.set_xlabel("func. arg [-]")
        ax.set_ylabel("func. value [-]")
        ax.grid()
        ax.legend()

    def __set_hardcoded_xtics(self, start, end, ax):
        pi_code = "\u03C0"
        x_ticks = [start, end / 4, end / 2, end * 3 / 4, end]
        x_ticks_labels_with_pi = list(map(lambda x: f"{x / pi}{pi_code}", x_ticks))

        ax.set_xticks(x_ticks)
        ax.set_xticklabels(x_ticks_labels_with_pi)
