from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar


class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)


class GraphWindow(QWidget):

    def __init__(self, parent=None):
        super(GraphWindow, self).__init__(parent)

        self.timer = None
        _translate = QtCore.QCoreApplication.translate
        self.setObjectName("Temperature / Voltage Graphic")
        self.setWindowTitle(_translate("Form", "Temperature / Voltage Graphic"))
        self.canvas = MplCanvas()  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()  # Set box for plotting
        self.navi_toolbar = NavigationToolbar(self.canvas, self)

        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.navi_toolbar)
        self.setLayout(self.vbl)

        self.n_data = 30
        self.xdata = list(range(self.n_data))
        self.temperatureData = [1] * self.n_data
        self.voltageData = [1] * self.n_data
        self.update_plot()

        self.show()

    def start_timer(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self, temp=None, voltage=None):
        if temp is not None:
            self.temperatureData = self.temperatureData[1:] + [temp]
        if voltage is not None:
            self.voltageData = self.voltageData[1:] + [voltage]
        self.xdata = list(range(len(self.temperatureData)))
        self.canvas.axes.autoscale()
        self.canvas.axes.set_ylim(0, 50)
        self.canvas.axes.cla()  # Clear the canvas.
        if voltage is not None:
            self.canvas.axes.plot(self.xdata, self.voltageData, 'b', label='Voltage  (V)')
            self.canvas.axes.text(self.xdata[-1] - 2.5, self.voltageData[-1] + 0.2, f'{voltage} (V)')
        self.canvas.axes.twinx()
        if temp is not None:
            self.canvas.axes.plot(self.xdata, self.temperatureData, 'r', label='Temperature (C)')
            self.canvas.axes.text(self.xdata[-1] - 2.5, self.temperatureData[-1] + 0.2, f'{temp} (C)')
        self.canvas.axes.legend()
        # Trigger the canvas to update and redraw.
        self.canvas.draw()

    def stop_plot(self):
        self.timer.stop()

    def onGraphHandler(self, dataList):
        self.update_plot(dataList[0], dataList[1])
