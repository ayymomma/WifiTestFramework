from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QFrame


class ConsoleLogFrame(QFrame):

    def __init__(self, container):
        super(ConsoleLogFrame, self).__init__(container)

        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(-2, 498, 1284, 272))
        self.setMinimumSize(QSize(1284, 272))
        self.setMaximumSize(QSize(1284, 272))
        self.setStyleSheet("background-color: #30363F;"
                           "border-width: 2px;"
                           "border-style: solid;"
                           "border-color: #FF8A00")
