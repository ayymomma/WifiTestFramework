import os

from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QFrame, QLabel

from customWidgets.components.customSlider import CustomSlider


class MotorControlFrame(QFrame):

    def __init__(self, container):
        super(MotorControlFrame, self).__init__(container)

        self.logoImage = QLabel(self)
        self.frameName = QLabel(self)
        self.sliderName = QLabel(self)
        self.motorDirection = QLabel(self)
        self.speedSlider = CustomSlider(self)

        self.setupUi()

    def setupUi(self):
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        # frame settings
        self.setGeometry(QRect(-2, -2, 642, 550))
        self.setMinimumSize(QSize(642, 550))
        self.setMaximumSize(QSize(642, 550))
        self.setStyleSheet("background-color: rgb(59, 67, 80);"
                           "border-width: 2px;"
                           "border-style: solid;"
                           "border-color: #FF8A00;")

        # continental logo
        self.logoImage.setGeometry(QRect(185, 400, 320, 120))
        self.logoImage.setStyleSheet("border-style: none")
        self.setLogoImage("conti.png")

        # frame name
        self.frameName.setGeometry(QRect(262, 10, 120, 30))
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
        self.motorDirection.setGeometry(QRect(50, 280, 150, 30))
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

    def setLogoImage(self, photoName):
        pixmap = QPixmap("resources" + os.path.sep + "images" + os.path.sep + photoName)
        self.logoImage.setPixmap(pixmap)
