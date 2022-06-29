import os
import sys

import psutil
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from customWidgets.frames.consoleLogFrame import ConsoleLogFrame
from customWidgets.frames.motorControlFrame import MotorControlFrame
from customWidgets.frames.testCasesFrame import TestCasesFrame
from customWidgets.windows.graphWindow import GraphWindow
from testExecution.server import Server


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize main window of the application
        """
        super(MainWindow, self).__init__()
        self.server = Server('0.0.0.0', 50100)

        self.centralWidget = QtWidgets.QWidget(self)
        self.testCasesFrame = TestCasesFrame(self.centralWidget, self.server)
        self.motorControlFrame = MotorControlFrame(self.centralWidget)
        self.consoleLogFrame = ConsoleLogFrame(self.centralWidget)
        self.graphWindow = GraphWindow()

        self.setCentralWidget(self.centralWidget)
        self.setWindowIcon(QtGui.QIcon("resources" + os.path.sep + "Images" + os.path.sep + "icon.png"))
        self.setupUi()

    def setupUi(self):
        """
        Setup main window interface and connect all signals caught in this class.
        """
        self.setWindowTitle("Wifi Test")
        self.resize(1280, 768)
        self.setMinimumSize(1280, 768)
        self.setMaximumSize(1280, 768)
        self.graphWindow.hide()

        self.motorControlFrame.speed_data_signal.connect(self.testCasesFrame.onSliderChangedHandler)
        self.motorControlFrame.direction_data_signal.connect(self.testCasesFrame.onChangeDirectionHandler)
        self.testCasesFrame.testExecution.graph_signal.connect(self.graphWindow.onGraphHandler)
        self.testCasesFrame.testExecution.start_test_signal.connect(self.graphWindow.show)
        self.testCasesFrame.testExecution.print_message_signal.connect(self.consoleLogFrame.onPrintMessageHandler)


def kill_proc_tree(pid, including_parent=True):
    """
    Function to kill processes
    :param pid: The ID of process
    :type pid: int
    :param including_parent: True if you want to kill parents too
    :type including_parent: bool
    """
    parent = psutil.Process(pid)
    if including_parent:
        parent.kill()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wifiTest = MainWindow()
    wifiTest.show()
    returnValue = app.exec()
    if returnValue is not None:
        kill_proc_tree(os.getpid())
        sys.exit(returnValue)
