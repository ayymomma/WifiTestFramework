import time

from PyQt5.QtCore import QObject, pyqtSignal


class TestExecution(QObject):
    counter_signal = pyqtSignal(int)
    temperature_signal = pyqtSignal(list)
    voltage_signal = pyqtSignal(float)
    speed_signal = pyqtSignal(float)
    stop_test_signal = pyqtSignal()

    testingTime = 30
    motorSpeed = 100
    motorDirection = 1
    counter = 1
    testCase = 1
    minTemperature = 5
    maxTemperature = 28
    minVoltage = 8
    maxVoltage = 18
    temperatureTest = False
    voltageTest = False
    temperatureHumidity = []
    voltage = 0
    speed = 0

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
            self.processServerValues(server, server.receiveMessage())
            self.counter += 1
            time.sleep(1)
        self.stopTest(server, "Test finished")

    def checkVoltage(self, voltage):
        if self.voltageTest:
            if voltage < self.minVoltage or voltage > self.maxVoltage:
                return False, f'Voltage is out of range.'
            else:
                return True, ''
        else:
            return True, ''

    def checkTemperature(self, temperature, name):
        if self.temperatureTest:
            if temperature < self.minTemperature or temperature > self.maxTemperature:
                return False, f'{name} temperature is out of range.'
            else:
                return True, ''
        else:
            return True, ''

    def processServerValues(self, server, message):
        if self.testCase == 6:
            self.temperatureHumidity = message.split(" ")[0:4]
            self.temperature_signal.emit(self.temperatureHumidity)
            self.voltage = message.split(" ")[4]
            self.voltage_signal.emit(float(self.voltage))
            self.speed = message.split(" ")[5]
            self.speed_signal.emit(float(self.speed))

            flag, status = self.checkTemperature(float(self.temperatureHumidity[0].split("=")[1]), 'Motor')
            if not flag:
                self.stopTest(server, status)
            flag, status = self.checkTemperature(float(self.temperatureHumidity[2].split("=")[1]), 'H Bridge')
            if not flag:
                self.stopTest(server, status)
            flag, status = self.checkVoltage(float(self.voltage))
            if not flag:
                self.stopTest(server, status)
        print(message)

    def stopTest(self, server, status):
        self.counter = self.testingTime + 1
        server.sendMessage("X")
        print(status)
        self.stop_test_signal.emit()
