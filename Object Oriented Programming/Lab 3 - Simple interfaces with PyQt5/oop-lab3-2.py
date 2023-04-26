# Zadanie 2
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

        # Dodanie pola tekstowego do wpisania funkcji
        self.func_area_label = QLabel(self.main)
        self.func_area_label.setText('Funkcja:')
        side_layout.addWidget(self.func_area_label)

        self.func_area = QLineEdit(self.main)
        side_layout.addWidget(self.func_area)

        # Dodanie pola z wartością minimalną
        self.min_box_label = QLabel(self.main)
        self.min_box_label.setText('Min:')
        side_layout.addWidget(self.min_box_label)

        self.min_box = QDoubleSpinBox(self.main)
        self.min_box.setMinimum(-1e+9)
        self.min_box.setValue(0.00)
        side_layout.addWidget(self.min_box)

        # Dodanie pola z wartością maksymalną
        self.max_box_label = QLabel(self.main)
        self.max_box_label.setText('Max:')
        side_layout.addWidget(self.max_box_label)

        self.max_box = QDoubleSpinBox(self.main)
        self.max_box.setValue(0.00)
        side_layout.addWidget(self.max_box)

        # Dodanie pola określającego krok
        self.step_box_label = QLabel(self.main)
        self.step_box_label.setText('Krok:')
        side_layout.addWidget(self.step_box_label)

        self.step_box = QDoubleSpinBox(self.main)
        self.step_box.setValue(0.00)
        side_layout.addWidget(self.step_box)

        # Przycisk obsługujący rysowanie wykresu zadanej funkcji
        self.calculate_button = QPushButton('Rysuj')
        self.calculate_button.clicked.connect(self.draw_plot)
        side_layout.addWidget(self.calculate_button)

        side_layout.addStretch(1)

    def draw_plot(self):
        self.ax.clear()

        # Wygenerowanie funkcji na podstawie stringa pobranego z pola tekstowego
        fx_str = self.func_area.text()
        f = lambda x: eval(fx_str)

        # Pobranie wartości zakresu oraz kroku z pól
        min_val = self.min_box.value()
        max_val = self.max_box.value()
        step = self.step_box.value()

        # Wygenerowanie wykresu zadanej funkcji wraz z zakresem
        x = np.arange(min_val - 1, max_val + 1, step)
        y = f(x)

        self.ax.plot(x, y)
        self.ax.axvline(min_val, color='red', linestyle='--')
        self.ax.axvline(max_val, color='red', linestyle='--')
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

