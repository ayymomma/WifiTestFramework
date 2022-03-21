from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel, QFrame

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


class TemperatureWindow(QDialog):
    def __init__(self, parent=None):
        super(TemperatureWindow, self).__init__(parent)
        self.windowName = QLabel(self)
        self.horizontalLine = QFrame(self)
        self.verticalLine = QFrame(self)
        self.bridgeTemperature = QLabel(self)
        self.motorTemperature = QLabel(self)
        self.lineEditBridgeTemp = CustomLineEdit(self)
        self.lineEditMotorTemp = CustomLineEdit(self)
        self.bridgeHumidity = QLabel(self)
        self.motorHumidity = QLabel(self)
        self.lineEditBridgeHum = CustomLineEdit(self)
        self.lineEditMotorHum = CustomLineEdit(self)

        self.setupUi()

    def setupUi(self):
        self.setObjectName("Temperature")
        self.setWindowTitle("Temperature and Humidity")
        self.resize(278, 193)
        self.setMinimumSize(278, 193)
        self.setMaximumSize(278, 193)
        self.setStyleSheet(windowStyle)

        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.windowName.setGeometry(QRect(30, 5, 220, 25))
        self.windowName.setObjectName("windowName")
        self.windowName.setFont(font)
        self.windowName.setText("Temperature and Humidity")

        font.setPointSize(10)
        self.horizontalLine.setGeometry(QRect(0, 30, 291, 16))
        self.horizontalLine.setFrameShape(QFrame.HLine)
        self.horizontalLine.setFrameShadow(QFrame.Sunken)
        self.horizontalLine.setObjectName("horizontalLine")

        self.verticalLine.setGeometry(QRect(125, 37, 20, 160))
        self.verticalLine.setFrameShape(QFrame.VLine)
        self.verticalLine.setFrameShadow(QFrame.Sunken)
        self.verticalLine.setObjectName("verticalLine")

        self.bridgeTemperature.setGeometry(QRect(10, 50, 120, 20))
        self.bridgeTemperature.setObjectName("bridgeTemperature")
        self.bridgeTemperature.setFont(font)
        self.bridgeTemperature.setText("HBridge Temperature")

        self.motorTemperature.setGeometry(QRect(155, 50, 110, 20))
        self.motorTemperature.setObjectName("motorTemperature")
        self.motorTemperature.setFont(font)
        self.motorTemperature.setText("Motor Temperature")

        self.lineEditBridgeTemp.setGeometry(QRect(30, 80, 80, 30))
        self.lineEditBridgeTemp.setObjectName("lineEditBridgeTemp")
        self.lineEditBridgeTemp.setReadOnly(True)
        self.lineEditBridgeTemp.setLineEditStyle()

        self.lineEditMotorTemp.setGeometry(QRect(170, 80, 80, 30))
        self.lineEditMotorTemp.setObjectName("lineEditMotorTemp")
        self.lineEditMotorTemp.setReadOnly(True)
        self.lineEditMotorTemp.setLineEditStyle()

        self.bridgeHumidity.setGeometry(QRect(20, 120, 110, 30))
        self.bridgeHumidity.setObjectName("bridgeHumidity")
        self.bridgeHumidity.setFont(font)
        self.bridgeHumidity.setText("HBridge Humidity")

        self.motorHumidity.setGeometry(QRect(165, 120, 110, 20))
        self.motorHumidity.setObjectName("motorHumidity")
        self.motorHumidity.setFont(font)
        self.motorHumidity.setText("Motor Humidity")

        self.lineEditBridgeHum.setGeometry(QRect(30, 150, 80, 30))
        self.lineEditBridgeHum.setObjectName("lineEditBridgeHum")
        self.lineEditBridgeHum.setReadOnly(True)
        self.lineEditBridgeHum.setLineEditStyle()

        self.lineEditMotorHum.setGeometry(QRect(170, 150, 80, 30))
        self.lineEditMotorHum.setObjectName("lineEditMotorHum")
        self.lineEditMotorHum.setReadOnly(True)
        self.lineEditMotorHum.setLineEditStyle()
