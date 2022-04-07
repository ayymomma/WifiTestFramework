import time

from PyQt5.QtCore import QObject, pyqtSignal


class TestExecution(QObject):
    counter_signal = pyqtSignal(int)
    temperature_signal = pyqtSignal(list)
    voltage_signal = pyqtSignal(float)
    speed_signal = pyqtSignal(float)
    testingTime = 30
    motorSpeed = 100
    motorDirection = 1
    counter = 1
    testCase = 1
    minTemperature = 5
    maxTemperature = 28
    minVoltage = 8
    maxVoltage = 18

    def __init__(self):
        super().__init__()

    def setMotorSpeed(self, value):
        self.motorSpeed = value

    def setMotorDirection(self, value):
        self.motorDirection = value
        print(value)

    def setMinTemperature(self, value):
        try:
            self.minTemperature = int(value)
        except ValueError:
            self.minTemperature = 5
        print(self.minTemperature)

    def setMaxTemperature(self, value):
        try:
            self.maxTemperature = int(value)
        except ValueError:
            self.maxTemperature = 28
        print(self.maxTemperature)

    def setMinVoltage(self, value):
        try:
            self.minVoltage = int(value)
        except ValueError:
            self.minVoltage = 8
        print(self.minVoltage)

    def setMaxVoltage(self, value):
        try:
            self.maxVoltage = int(value)
        except ValueError:
            self.maxVoltage = 18
        print(self.maxVoltage)

    def startTest(self, server):
        server.sendMessage("S {motorDirection} {testCase} {motorSpeed}".format(motorDirection=self.motorDirection,
                                                                               testCase=self.testCase,
                                                                               motorSpeed=self.motorSpeed))
        server.receiveMessage()
        self.counter = 1

        while self.counter <= self.testingTime:
            self.counter_signal.emit(int(self.counter * 100 / self.testingTime))
            # send parameters to uC
            # receive from uC values
            # send signals to windows
            self.processServerValues(server.receiveMessage())
            self.counter += 1
            time.sleep(1)
        self.stopTest(server)

    def processServerValues(self, message):
        # if self.testCase == 1:
        #     temperatureHumidity = message.split(" ")
        #     self.temperature_signal.emit(temperatureHumidity)
        # elif self.testCase == 2:
        #     voltage = message.split(" ")
        #     self.voltage_signal.emit(float(voltage[0]))
        # elif self.testCase == 3:
        #     speed = message.split(" ")
        #     self.speed_signal.emit(float(speed[0]))
        # elif self.testCase == 4:
        #     temperatureHumidity = message.split(" ")[0:4]
        #     self.temperature_signal.emit(temperatureHumidity)
        #     voltage = message.split(" ")[4]
        #     self.voltage_signal.emit(float(voltage[0]))
        if self.testCase == 6:
            temperatureHumidity = message.split(" ")[0:4]
            self.temperature_signal.emit(temperatureHumidity)
            voltage = message.split(" ")[4]
            self.voltage_signal.emit(float(voltage))
            speed = message.split(" ")[5]
            self.speed_signal.emit(float(speed))


        print(message)

    def stopTest(self, server):
        self.counter = 0
        server.sendMessage("X")
