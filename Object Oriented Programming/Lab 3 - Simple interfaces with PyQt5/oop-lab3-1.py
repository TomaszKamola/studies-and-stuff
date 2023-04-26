# Zadanie 1
import sys

import numpy as np

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib import pyplot as plt


class ApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = QWidget()
        self.setCentralWidget(self.main)

        layout = QHBoxLayout(self.main)

        # Zdefiniowanie canvasa, na którym będą rysowane wykresy
        self.figure = Figure(figsize=(6, 6))
        self.ax = self.figure.subplots()

        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        side_layout = QVBoxLayout(self.main)
        layout.addLayout(side_layout)

        # Zdefiniowanie przycisku i podłączenie funkcji do niego
        self.calculate_button = QPushButton('Rysuj')
        self.calculate_button.clicked.connect(self.calculate_slot)
        side_layout.addWidget(self.calculate_button)

        side_layout.addStretch(1)

    def calculate_slot(self):
        self.ax.clear()

        x = np.linspace(-np.pi, np.pi, 100)
        y = np.sin(x)

        self.ax.plot(x, y)
        self.ax.grid(linestyle='--', alpha=0.5)

        self.figure.canvas.draw()


if __name__ == "__main__":
    qapp = QApplication.instance()
    if not qapp:
        qapp = QApplication(sys.argv)

    app = ApplicationWindow()
    app.setWindowTitle('Aplikacja')
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec_()


# Zadanie 2

