import threading

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QDialog

from customWidgets.components.customLineEdit import CustomLineEdit


class MyGraphicsView(QtWidgets.QGraphicsView):
    mouse_pos_signal = pyqtSignal(float)

    def __init__(self, parent):
        QtWidgets.QGraphicsView.__init__(self, parent)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        x_value_mouse_move = event.pos().x()
        self.mouse_pos_signal.emit(x_value_mouse_move)
        print(event.pos().x())


class FlagsWindow(QDialog):

    def __init__(self, parent=None):
        super(FlagsWindow, self).__init__(parent)
        self.x_value_mouse_move = 0
        self.thr = None
        self.scene = None
        self.line = QtWidgets.QFrame(self)
        self.line_2 = QtWidgets.QFrame(self)
        self.line_3 = QtWidgets.QFrame(self)
        self.varNameLineEdit = CustomLineEdit(self)
        self.valuesLineEdit = CustomLineEdit(self)
        self.temperatureLabel = QtWidgets.QLabel(self)
        self.voltageLabel = QtWidgets.QLabel(self)
        self.motorStateLabel = QtWidgets.QLabel(self)
        self.temperatureLineEdit = CustomLineEdit(self)
        self.voltageLineEdit = CustomLineEdit(self)
        self.motorStateLineEdit = CustomLineEdit(self)
        self.graphicsView = MyGraphicsView(self)

        self.x_vals = []
        self.y_temp = []
        self.y_volt = []
        self.y_dist = []
        self.fsf_vals = [1] * 30
        self.stop = False

        self.setupUi()
        self.graphicsView.mouse_pos_signal.connect(self.getXValue)

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(1100, 400)
        self.setStyleSheet("background-color: #30363F;")

        self.line.setGeometry(QtCore.QRect(0, 60, 1081, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_2.setGeometry(QtCore.QRect(470, 0, 20, 721))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_3.setGeometry(QtCore.QRect(250, 0, 20, 731))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.varNameLineEdit.setGeometry(QtCore.QRect(60, 11, 121, 41))
        self.varNameLineEdit.setLineEditStyle()
        self.varNameLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.varNameLineEdit.setReadOnly(True)

        self.valuesLineEdit.setGeometry(QtCore.QRect(300, 10, 121, 41))
        self.valuesLineEdit.setLineEditStyle()
        self.valuesLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.valuesLineEdit.setReadOnly(True)

        self.temperatureLabel.setGeometry(QtCore.QRect(20, 90, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.temperatureLabel.setFont(font)
        self.temperatureLabel.setStyleSheet("color: red;\n"
                                            "\n"
                                            "")

        self.voltageLabel.setGeometry(QtCore.QRect(20, 160, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.voltageLabel.setFont(font)
        self.voltageLabel.setStyleSheet("color: yellow;")

        self.motorStateLabel.setGeometry(QtCore.QRect(20, 280, 81, 16))
        self.motorStateLabel.setFont(font)
        self.motorStateLabel.setStyleSheet("color: green;")

        self.temperatureLineEdit.setGeometry(QtCore.QRect(300, 100, 113, 22))
        self.temperatureLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.temperatureLineEdit.setLineEditStyle()

        self.voltageLineEdit.setGeometry(QtCore.QRect(300, 160, 113, 22))
        self.voltageLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.voltageLineEdit.setLineEditStyle()


        self.motorStateLineEdit.setGeometry(QtCore.QRect(300, 280, 113, 22))
        self.motorStateLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.motorStateLineEdit.setLineEditStyle()

        self.graphicsView.setGeometry(QtCore.QRect(490, 80, 560, 270))
        self.graphicsView.setObjectName("graphicsView")

        self.setWindowTitle("Flags Window")
        self.varNameLineEdit.setText("VARIABLES NAME")
        self.valuesLineEdit.setText("VALUES")
        self.temperatureLabel.setText("H-Bridge & Motor Temperature")
        self.voltageLabel.setText("DC - Link")
        self.motorStateLabel.setText("Motor State")
        QtCore.QMetaObject.connectSlotsByName(self)

    def draw_flags(self, x_vals, y_temp_vals, y_voltage_vals):


        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.x_vals = [0] + x_vals
        self.y_temp = [0] + y_temp_vals
        self.y_volt = [0] + y_voltage_vals

        print(self.x_vals)
        print(self.y_temp)
        print(self.y_volt)

        self.fsf_vals = [1] * 30

        for i in range(1, len(x_vals)):
            red_pen = QtGui.QPen(QtCore.Qt.red)
            yellow_pen = QtGui.QPen(QtCore.Qt.yellow)
            green_pen = QtGui.QPen(QtCore.Qt.green)
            if y_temp_vals[i] == 1:
                self.fsf_vals[i] = 2
                for j in range(i + 1, len(self.fsf_vals)):
                    self.fsf_vals[j] = 0
                r = QtCore.QLineF(QtCore.QPoint((x_vals[i - 1] * 19) * 1, (y_temp_vals[i - 1] * 20) * (-1)),
                                  QtCore.QPoint((x_vals[i - 1] * 19) * 1, (y_temp_vals[i] * 20) * (-1)))
                self.scene.addLine(r, red_pen)
                r = QtCore.QLineF(QtCore.QPoint((x_vals[i - 1] * 19) * 1, (y_temp_vals[i] * 20) * (-1)),
                                  QtCore.QPoint((x_vals[i] * 19) * 1, (y_temp_vals[i] * 20) * (-1)))
                self.scene.addLine(r, red_pen)
                r = QtCore.QLineF(QtCore.QPoint((x_vals[i] * 19) * 1, (y_temp_vals[i - 1] * 20) * (-1)),
                                  QtCore.QPoint((x_vals[i] * 19) * 1, (y_temp_vals[i] * 20) * (-1)))
                self.scene.addLine(r, red_pen)
            else:
                if y_temp_vals[i - 1] == 1:
                    r = QtCore.QLineF(QtCore.QPoint((x_vals[i - 1] * 19) * 1, (y_temp_vals[i] * 20) * (-1)),
                                      QtCore.QPoint((x_vals[i] * 19) * 1, (y_temp_vals[i] * 20) * (-1)))
                    self.scene.addLine(r, red_pen)
                else:
                    r = QtCore.QLineF(QtCore.QPoint((x_vals[i - 1] * 19) * 1, (y_temp_vals[i] * 20) * (-1)),
                                      QtCore.QPoint((x_vals[i] * 19) * 1, (y_temp_vals[i - 1] * 20) * (-1)))
                    self.scene.addLine(r, red_pen)

            if y_voltage_vals[i] == 1:
                self.fsf_vals[i] = 3
                for j in range(i + 1, len(self.fsf_vals)):
                    self.fsf_vals[j] = 0
                r = QtCore.QLineF(QtCore.QPoint((x_vals[i - 1] * 19) * 1, (y_voltage_vals[i - 1] * 20 - 50) * (-1)),
                                  QtCore.QPoint((x_vals[i - 1] * 19) * 1, (y_voltage_vals[i] * 20 - 50) * (-1)))
                self.scene.addLine(r, yellow_pen)
                r = QtCore.QLineF(QtCore.QPoint((x_vals[i - 1] * 19) * 1, (y_voltage_vals[i] * 20 - 50) * (-1)),
                                  QtCore.QPoint((x_vals[i] * 19) * 1, (y_voltage_vals[i] * 20 - 50) * (-1)))
                self.scene.addLine(r, yellow_pen)
                r = QtCore.QLineF(QtCore.QPoint((x_vals[i] * 19) * 1, (y_voltage_vals[i] * 20 - 50) * (-1)),
                                  QtCore.QPoint((x_vals[i] * 19) * 1, (y_voltage_vals[i - 1] * 20 - 50) * (-1)))
                self.scene.addLine(r, yellow_pen)
            else:
                if y_voltage_vals[i - 1] == 1:
                    r = QtCore.QLineF(QtCore.QPoint((x_vals[i - 1] * 19) * 1, (y_voltage_vals[i] * 20 - 50) * (-1)),
                                      QtCore.QPoint((x_vals[i] * 19) * 1, (y_voltage_vals[i] * 20 - 50) * (-1)))
                    self.scene.addLine(r, yellow_pen)
                else:
                    r = QtCore.QLineF(QtCore.QPoint((x_vals[i - 1] * 19) * 1, (y_voltage_vals[i - 1] * 20 - 50) * (-1)),
                                      QtCore.QPoint((x_vals[i] * 19) * 1, (y_voltage_vals[i] * 20 - 50) * (-1)))
                    self.scene.addLine(r, yellow_pen)

            if self.fsf_vals[i] == 2 or self.fsf_vals[i] == 3 or self.fsf_vals[i] == 4:
                r = QtCore.QLineF(QtCore.QPoint((x_vals[i - 1] * 19) * 1, (self.fsf_vals[i - 1] * 20 - 200) * (-1)),
                                  QtCore.QPoint((x_vals[i - 1] * 19) * 1, (self.fsf_vals[i] * 20 - 200) * (-1)))
                self.scene.addLine(r, green_pen)
                r = QtCore.QLineF(QtCore.QPoint((x_vals[i - 1] * 19) * 1, (self.fsf_vals[i] * 20 - 200) * (-1)),
                                  QtCore.QPoint((x_vals[i] * 19) * 1, (self.fsf_vals[i] * 20 - 200) * (-1)))
                self.scene.addLine(r, green_pen)
                r = QtCore.QLineF(QtCore.QPoint((x_vals[i] * 19) * 1, (self.fsf_vals[i - 1] * 20 - 200) * (-1)),
                                  QtCore.QPoint((x_vals[i] * 19) * 1, (self.fsf_vals[i] * 20 - 200) * (-1)))
                self.scene.addLine(r, green_pen)
                r = QtCore.QLineF(QtCore.QPoint((x_vals[i] * 19) * 1, (20 - 200) * (-1)),
                                  QtCore.QPoint((x_vals[i] * 19) * 1, (- 200) * (-1)))
                self.scene.addLine(r, green_pen)
            else:
                if self.fsf_vals[i - 1] == 2 or self.fsf_vals[i - 1] == 3 or self.fsf_vals[i - 1] == 4:
                    r = QtCore.QLineF(
                        QtCore.QPoint((x_vals[i - 1] * 19) * 1, (self.fsf_vals[i] * 20 - 200) * (-1)),
                        QtCore.QPoint((x_vals[i] * 19) * 1, (self.fsf_vals[i] * 20 - 200) * (-1)))
                    self.scene.addLine(r, green_pen)
                else:
                    r = QtCore.QLineF(QtCore.QPoint((x_vals[i - 1] * 19) * 1, (self.fsf_vals[i - 1] * 20 - 200) * (-1)),
                                      QtCore.QPoint((x_vals[i] * 19) * 1, (self.fsf_vals[i] * 20 - 200) * (-1)))
                    self.scene.addLine(r, green_pen)

        self.stop = False
        self.thr = threading.Thread(target=self.change_values)
        self.thr.start()

    def change_values(self):
        while not self.stop:
            try:
                self.temperatureLineEdit.setText(str(self.y_temp[int(self.x_value_mouse_move / 20 + 1)]))
                self.voltageLineEdit.setText(str(self.y_volt[int(self.x_value_mouse_move / 20 + 1)]))
                self.motorStateLineEdit.setText(str(self.fsf_vals[int(self.x_value_mouse_move / 20 + 1)]))
            except IndexError:
                print("IndexError")

    def getXValue(self, value):
        self.x_value_mouse_move = value

    def closeEvent(self, event):
        self.stop = True
