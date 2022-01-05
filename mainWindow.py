import os
import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from customWidgets.frames.consoleLogFrame import ConsoleLogFrame
from customWidgets.frames.motorControlFrame import MotorControlFrame
from customWidgets.frames.testCasesFrame import TestCasesFrame


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()

        self.centralWidget = QtWidgets.QWidget(self)
        self.testCasesFrame = TestCasesFrame(self.centralWidget)
        self.motorControlFrame = MotorControlFrame(self.centralWidget)
        self.consoleLogFrame = ConsoleLogFrame(self.centralWidget)

        self.setCentralWidget(self.centralWidget)
        self.setWindowIcon(QtGui.QIcon("resources" + os.path.sep + "Images" + os.path.sep + "icon.png"))
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Wifi Test")
        self.resize(1280, 768)
        self.setMinimumSize(1280, 768)
        self.setMaximumSize(1280, 768)

        self.testCasesFrame.setObjectName("testCasesFrame")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wifiTest = mainWindow()
    wifiTest.show()
    sys.exit(app.exec())
