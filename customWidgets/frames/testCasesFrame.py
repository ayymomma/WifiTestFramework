from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QFrame


class TestCasesFrame(QFrame):

    def __init__(self, container):
        super(TestCasesFrame, self).__init__(container)

        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(640, -2, 642, 550))
        self.setMinimumSize(QSize(642, 550))
        self.setMaximumSize(QSize(642, 550))
        self.setStyleSheet("background-color: rgb(59, 67, 80);"
                           "border-width: 2px;"
                           "border-style: solid;"
                           "border-color: #FF8A00")
