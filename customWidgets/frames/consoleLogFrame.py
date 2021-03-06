import os

from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QFrame, QWidget
from datetime import datetime
from customWidgets.components.customTextEdit import CustomTextEdit


class ConsoleLogFrame(QFrame):

    def __init__(self, parent):
        """
        Initialize Console log frame
        :param parent: Reference of the component to which the window belongs
        :type parent: QWidget
        """
        super(ConsoleLogFrame, self).__init__(parent)

        self.consoleLog = CustomTextEdit(self)
        self.logFile = f"Log-{datetime.now().strftime('%d-%m-%Y')}.txt"
        self.outputFile = open(os.getcwd() + "\\Logs\\" + self.logFile, 'a')
        self.outputFile.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}: Log file created\n")
        self.outputFile.close()
        self.setupUi()

    def setupUi(self):
        """
        Set up frame size and components
        """
        self.setGeometry(QRect(-2, 498, 1284, 272))
        self.setMinimumSize(QSize(1284, 272))
        self.setMaximumSize(QSize(1284, 272))
        self.setStyleSheet("background-color: #30363F;"
                           "border-width: 2px;"
                           "border-style: solid;"
                           "border-color: #FF8A00")

        self.consoleLog.setGeometry(QRect(10, 10, 1265, 250))
        self.consoleLog.setTextStyle()

    def onPrintMessageHandler(self, text):
        """
        Add new text at the end of the text edit and file\n
        :param text: Text which will be printed
        :type text: str
        """
        self.outputFile = open(os.getcwd() + "\\Logs\\" + self.logFile, 'a')
        self.consoleLog.setPlainText(
            self.consoleLog.toPlainText() + f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}: {text}\n")
        self.outputFile.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}: {text}\n")
        self.outputFile.close()
