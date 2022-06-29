from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel, QFrame, QWidget

from customWidgets.components.customLineEdit import CustomLineEdit

windowStyle = """
QDialog {
    background-color: #30363F;
}
QLabel {
    text-align: center;
    border-style: none;
    color: rgb(181, 181, 181);
}
"""


class VoltageWindow(QDialog):
    def __init__(self, parent=None):
        """
        Initialize voltage window\n
        :param parent: Reference of the component to which the window belongs
        :type parent: QWidget
        """
        super(VoltageWindow, self).__init__(parent)
        self.windowName = QLabel(self)
        self.horizontalLine = QFrame(self)
        self.supplyVoltage = QLabel(self)
        self.lineEditVoltage = CustomLineEdit(self)

        self.setupUi()

    def setupUi(self):
        """
        Set up the window size and components
        """
        self.setObjectName("Voltage")
        self.setWindowTitle("Voltage")
        self.resize(278, 193)
        self.setMinimumSize(278, 193)
        self.setMaximumSize(278, 193)
        self.setStyleSheet(windowStyle)

        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.windowName.setGeometry(QRect(105, 5, 220, 25))
        self.windowName.setObjectName("windowName")
        self.windowName.setFont(font)
        self.windowName.setText("Voltage")

        font.setPointSize(10)
        self.horizontalLine.setGeometry(QRect(0, 30, 291, 16))
        self.horizontalLine.setFrameShape(QFrame.HLine)
        self.horizontalLine.setFrameShadow(QFrame.Sunken)
        self.horizontalLine.setObjectName("horizontalLine")

        self.lineEditVoltage.setGeometry(QRect(95, 100, 80, 30))
        self.lineEditVoltage.setObjectName("lineEditSpeed")
        self.lineEditVoltage.setReadOnly(True)
        self.lineEditVoltage.setLineEditStyle()

        self.supplyVoltage.setGeometry(QRect(95, 70, 110, 20))
        self.supplyVoltage.setObjectName("motorSpeed")
        self.supplyVoltage.setFont(font)
        self.supplyVoltage.setText("Supply Voltage")

        self.setValue(0)

    def setValue(self, value):
        """
        Set the value of the voltage line edit\n
        :param value: Voltage to be shown
        :type value: float
        """
        self.lineEditVoltage.setText(str(value) + "V")
