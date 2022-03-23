import os
import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from customWidgets.frames.consoleLogFrame import ConsoleLogFrame
from customWidgets.frames.motorControlFrame import MotorControlFrame
from customWidgets.frames.testCasesFrame import TestCasesFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

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

        self.motorControlFrame.speed_data_signal.connect(self.testCasesFrame.onSliderChangedHandler)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wifiTest = MainWindow()
    wifiTest.show()
    sys.exit(app.exec())
