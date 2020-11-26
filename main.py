import sys

import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.start_paint = False
        self.btn.clicked.connect(self.paint)

    def paint(self):
        self.start_paint = True
        self.repaint()
        self.start_paint = False

    def paintEvent(self, event):
        if self.start_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_figures(qp)
            qp.end()

    def draw_figures(self, qp):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = QColor('yellow')
        qp.setBrush(rgb)

        width = random.randint(10, 200)
        posx = random.randint(200, 600)
        posy = random.randint(200, 550)

        qp.drawEllipse(posx, posy, width, width)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())