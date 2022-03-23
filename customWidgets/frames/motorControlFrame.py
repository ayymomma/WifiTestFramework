import os

from PyQt5.QtCore import QRect, QSize, Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QFrame, QLabel

from customWidgets.components.customButton import CustomButton
from customWidgets.components.customLineEdit import CustomLineEdit
from customWidgets.components.customSlider import CustomSlider


class MotorControlFrame(QFrame):
    speed_data_signal = pyqtSignal(int)
    direction_data_signal = pyqtSignal(str)

    def __init__(self, container):
        super(MotorControlFrame, self).__init__(container)

        self.logoImage = QLabel(self)
        self.frameName = QLabel(self)
        self.sliderName = QLabel(self)
        self.motorDirection = QLabel(self)
        self.speedSlider = CustomSlider(self)
        self.clockwiseButton = CustomButton(self, "Clockwise")
        self.counterClockwiseButton = CustomButton(self, "Counter clockwise")
        self.speedLineEdit = CustomLineEdit(self)

        self.setupUi()

    def setupUi(self):
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        # frame settings
        self.setGeometry(QRect(-2, -2, 642, 500))
        self.setMinimumSize(QSize(642, 500))
        self.setMaximumSize(QSize(642, 500))
        self.setStyleSheet("background-color: #30363F;"
                           "border-width: 2px;"
                           "border-style: solid;"
                           "border-color: #E47900;")

        # continental logo
        self.logoImage.setGeometry(QRect(300, 320, 320, 120))
        self.logoImage.setStyleSheet("border-style: none")
        self.setLogoImage("conti.png")

        # frame name
        self.frameName.setGeometry(QRect(262, 30, 120, 30))
        self.frameName.setStyleSheet("text-align: center;"
                                     "border-style: none;"
                                     "color: rgb(181, 181, 181)")
        self.frameName.setFont(font)
        self.frameName.setText("Motor control")

        # slider name
        self.sliderName.setGeometry(QRect(50, 120, 120, 30))
        self.sliderName.setStyleSheet("text-align: center;"
                                      "border-style: none;"
                                      "color: rgb(181, 181, 181)")
        self.sliderName.setFont(font)
        self.sliderName.setText("Motor speed")

        # direction name
        self.motorDirection.setGeometry(QRect(50, 300, 150, 30))
        self.motorDirection.setStyleSheet("text-align: center;"
                                          "border-style: none;"
                                          "color: rgb(181, 181, 181)")
        self.motorDirection.setFont(font)
        self.motorDirection.setText("Motor direction")

        # slider
        self.speedSlider.setGeometry(QRect(50, 160, 540, 20))
        self.speedSlider.setSliderStyle()
        self.speedSlider.setMinimumWidth(400)
        self.speedSlider.setOrientation(Qt.Horizontal)
        self.speedSlider.sliderReleased.connect(lambda: self.sendSpeedData())

        # button clockwise
        font.setPointSize(12)
        self.clockwiseButton.setGeometry(QRect(50, 340, 150, 35))
        self.clockwiseButton.setButtonStyle()
        self.clockwiseButton.setFont(font)
        font.setPointSize(14)

        # button counterclockwise
        font.setPointSize(12)
        self.counterClockwiseButton.setGeometry(QRect(50, 390, 150, 35))
        self.counterClockwiseButton.setButtonStyle()
        self.counterClockwiseButton.setFont(font)
        font.setPointSize(14)

        # horizontalLine edit motor speed
        font.setPointSize(10)
        self.speedLineEdit.setGeometry(50, 220, 100, 35)
        self.speedLineEdit.setLineEditStyle()
        self.speedLineEdit.setFont(font)
        self.speedLineEdit.setText("0")
        self.speedLineEdit.setReadOnly(True)
        font.setPointSize(14)

    def setLogoImage(self, photoName):
        pixmap = QPixmap("resources" + os.path.sep + "images" + os.path.sep + photoName)
        self.logoImage.setPixmap(pixmap)

    def sendSpeedData(self):
        self.speed_data_signal.emit(self.speedSlider.getValue())
        self.speedLineEdit.setText(str(self.speedSlider.getValue()))
