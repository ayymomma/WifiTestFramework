from PyQt5.QtCore import QRect, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel

from customWidgets.components.customButton import CustomButton
from customWidgets.components.customCheckBox import CustomCheckBox
from customWidgets.components.customLineEdit import CustomLineEdit
from customWidgets.components.customProgressBar import CustomProgressBar
from customWidgets.windows.temperatureWindow import TemperatureWindow


class TestCasesFrame(QFrame):

    def __init__(self, container):
        super(TestCasesFrame, self).__init__(container)

        self.frameName = QLabel(self)
        self.temperatureName = QLabel(self)
        self.testcasesName = QLabel(self)
        self.voltageName = QLabel(self)
        self.speedName = QLabel(self)
        self.maxTemperatureName = QLabel(self)
        self.maxTemperatureLineEdit = CustomLineEdit(self)
        self.progressBar = CustomProgressBar(self)
        self.startButton = CustomButton(self, "Start")
        self.stopButton = CustomButton(self, "Stop")
        self.temperatureCheckBox = CustomCheckBox(self)
        self.voltageCheckBox = CustomCheckBox(self)
        self.speedCheckBox = CustomCheckBox(self)

        self.temperatureWindow = TemperatureWindow(container)
        self.temperatureWindow.show()
        self.setupUi()

    def setupUi(self):
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setGeometry(QRect(640, -2, 642, 500))
        self.setMinimumSize(QSize(642, 500))
        self.setMaximumSize(QSize(642, 500))
        self.setStyleSheet("""
                            QFrame {
                            background-color: #30363F;
                            border-width: 2px;
                            border-style: solid;
                            border-color: #E47900;
                            }
                           """
                           )

        # frame name
        self.frameName.setGeometry(QRect(262, 30, 120, 30))
        self.frameName.setStyleSheet("text-align: center;"
                                     "border-style: none;"
                                     "color: rgb(181, 181, 181)")
        self.frameName.setFont(font)
        self.frameName.setText("Test control")

        # testcases name
        self.testcasesName.setGeometry(QRect(80, 120, 100, 30))
        self.testcasesName.setStyleSheet("text-align: center;"
                                         "border-style: none;"
                                         "color: rgb(181, 181, 181)")
        self.testcasesName.setFont(font)
        self.testcasesName.setText("Test cases")

        # temperature name
        self.temperatureName.setGeometry(QRect(110, 160, 180, 30))
        self.temperatureName.setStyleSheet("text-align: center;"
                                           "border-style: none;"
                                           "color: rgb(181, 181, 181)")
        self.temperatureName.setFont(font)
        self.temperatureName.setText("Temperature test case")

        # voltage name
        self.voltageName.setGeometry(QRect(110, 200, 180, 30))
        self.voltageName.setStyleSheet("text-align: center;"
                                       "border-style: none;"
                                       "color: rgb(181, 181, 181)")
        self.voltageName.setFont(font)
        self.voltageName.setText("Voltage test case")

        # speed name
        self.speedName.setGeometry(QRect(110, 240, 180, 30))
        self.speedName.setStyleSheet("text-align: center;"
                                     "border-style: none;"
                                     "color: rgb(181, 181, 181)")
        self.speedName.setFont(font)
        self.speedName.setText("Speed test case")

        # max temperature name
        self.maxTemperatureName.setGeometry(QRect(80, 280, 200, 30))
        self.maxTemperatureName.setStyleSheet("text-align: center;"
                                              "border-style: none;"
                                              "color: rgb(181, 181, 181)")
        self.maxTemperatureName.setFont(font)
        self.maxTemperatureName.setText("Maximum temperature")

        # horizontalLine edit max temperature
        font.setPointSize(10)
        self.maxTemperatureLineEdit.setGeometry(80, 320, 100, 35)
        self.maxTemperatureLineEdit.setLineEditStyle()
        self.maxTemperatureLineEdit.setFont(font)
        self.maxTemperatureLineEdit.setText("28.0")
        font.setPointSize(14)

        # progress bar
        self.progressBar.setGeometry(QRect(80, 380, 480, 30))
        self.progressBar.setProgressBarStyle()
        self.progressBar.setFont(font)
        self.progressBar.updateBar(1)

        # start button
        font.setPointSize(12)
        self.startButton.setGeometry(QRect(120, 420, 150, 35))
        self.startButton.setButtonStyle(bgColor="#01BF21", borderColor="#349E45", bgColorHover="#349E45",
                                        bgColorPressed="#01BF21")
        self.startButton.setFont(font)
        font.setPointSize(14)

        # stop button
        font.setPointSize(12)
        self.stopButton.setGeometry(QRect(370, 420, 150, 35))
        self.stopButton.setButtonStyle(bgColor="#E51616", borderColor="#903131", bgColorHover="#903131",
                                       bgColorPressed="#E51616")
        self.stopButton.setFont(font)
        font.setPointSize(14)

        # temperature check box
        self.temperatureCheckBox.setGeometry(QRect(80, 160, 32, 32))
        self.temperatureCheckBox.setCheckBoxStyle()

        # voltage check box
        self.voltageCheckBox.setGeometry(QRect(80, 200, 32, 32))
        self.voltageCheckBox.setCheckBoxStyle()

        # speed check box
        self.speedCheckBox.setGeometry(QRect(80, 240, 32, 32))
        self.speedCheckBox.setCheckBoxStyle()
