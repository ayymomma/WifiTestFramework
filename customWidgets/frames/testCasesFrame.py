from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QFrame


class TestCasesFrame(QFrame):

    def __init__(self, container):
        super(TestCasesFrame, self).__init__(container)

        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(640, -2, 642, 500))
        self.setMinimumSize(QSize(642, 500))
        self.setMaximumSize(QSize(642, 500))
        self.setStyleSheet("background-color: #30363F;"
                           "border-width: 2px;"
                           "border-style: solid;"
                           "border-color: #E47900")
