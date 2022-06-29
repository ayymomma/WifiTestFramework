import time
import matplotlib.pyplot as plt

from PyQt5.QtCore import QObject, pyqtSignal
from server import Server


class TestExecution(QObject):
    counter_signal = pyqtSignal(int)
    temperature_signal = pyqtSignal(list)
    voltage_signal = pyqtSignal(float)
    speed_signal = pyqtSignal(float)
    stop_test_signal = pyqtSignal()
    start_test_signal = pyqtSignal()
    graph_signal = pyqtSignal(list)
    print_message_signal = pyqtSignal(str)

    testingTime = 30
    motorSpeed = 100
    newMotorSpeed = 100
    motorDirection = 1
    counter = 1
    testCase = 1
    minTemperature = 5
    maxTemperature = 28
    minVoltage = -1
    maxVoltage = 9999
    temperatureTest = False
    voltageTest = False
    temperatureHumidity = []
    voltage = 0
    speed = 0
    hBridgeTemperatureGraph = None
    motorTemperatureGraph = None
    voltageGraph = None
    failed = False

    xFlagValues = []
    yFlagTemperature = []
    yFlagVoltage = []

    def __init__(self):
        """
        Initialize the object
        """
        super().__init__()

    def setMotorSpeed(self, value):
        """
        Set the motor speed\n
        :param value: New motor speed
        :type value: int
        """
        self.newMotorSpeed = value

    def setMotorDirection(self, value):
        """
        Set the motor direction\n
        :param value: New motor direction
        :type value: int
        """
        self.motorDirection = value

    def setMinTemperature(self, value):
        """
        Set minimum temperature for tests\n
        :param value: New minimum temperature
        :type value: float
        """
        try:
            self.minTemperature = int(value)
        except ValueError:
            self.minTemperature = 5

    def setMaxTemperature(self, value):
        """
        Set maximum temperature for tests\n
        :param value: New maximum temperature
        :type value: float
        """
        try:
            self.maxTemperature = int(value)
        except ValueError:
            self.maxTemperature = 28

    def setMinVoltage(self, value):
        """
        Set minimum voltage for tests\n
        :param value: New minimum voltage
        :type value: float
        """
        try:
            self.minVoltage = int(value)
        except ValueError:
            self.minVoltage = 8

    def setMaxVoltage(self, value):
        """
        Set maximum voltage for tests\n
        :param value: New maximum voltage
        :type value: float
        """
        try:
            self.maxVoltage = int(value)
        except ValueError:
            self.maxVoltage = 18

    def startTest(self, server):
        """
        Start test execution\n
        :param server: Application server for sending and receiving messages
        :type server: Server
        """
        if self.newMotorSpeed != self.motorSpeed:
            self.motorSpeed = self.newMotorSpeed
        self.print_message_signal.emit('Test started.')
        self.start_test_signal.emit()
        server.sendMessage("S {motorDirection} {motorSpeed}".format(motorDirection=self.motorDirection,
                                                                    motorSpeed=self.motorSpeed))

        self.voltageGraph = None
        self.motorTemperatureGraph = None
        self.counter = 1
        self.failed = False
        self.xFlagValues = []
        self.yFlagTemperature = []
        self.yFlagVoltage = []

        while self.counter <= self.testingTime:
            if server.messageReceived:
                if self.newMotorSpeed != self.motorSpeed:
                    self.motorSpeed = self.newMotorSpeed
                    server.sendMessage(str(self.motorSpeed))
                self.xFlagValues.append(self.counter)
                self.counter_signal.emit(int(self.counter * 100 / self.testingTime))
                self.processServerValues(server, server.data)
                self.graph_signal.emit([self.motorTemperatureGraph, self.voltageGraph])
                self.counter += 1
            time.sleep(1)

        if not self.failed:
            self.stopTest(server, "Test finished with no errors!")

    def checkVoltage(self, voltage):
        """
        Check if voltage is in limits\n
        :param voltage: Voltage which will be tested
        :type voltage: float
        :return: False if voltage si out of range and the message 'Voltage is out of range' and True if voltage is in range
        :rtype: (bool, str)
        """
        if self.voltageTest:
            self.voltageGraph = voltage
            if voltage < self.minVoltage or voltage > self.maxVoltage:
                return False, f'Voltage is out of range.'
            else:
                return True, ''
        else:
            return True, ''

    def checkTemperature(self, temperature, name):
        """
        Check if temperature is in range\n
        :param temperature: Temperature which will be tested
        :type temperature: float
        :param name: Name of component which corresponds to temperature
        :type name: str
        :return: False if temperature si out of range and the message '{name} is out of range' and True if temperature is in range
        :rtype: (bool, str)
        """
        if self.temperatureTest:
            if name == 'Motor':
                self.motorTemperatureGraph = temperature
            if temperature < self.minTemperature or temperature > self.maxTemperature:
                return False, f'{name} temperature is out of range.'
            else:
                return True, ''
        else:
            return True, ''

    def processServerValues(self, server, message):
        """
        Split the message received from client and assign it to class variables\n
        :param server: Reference to application server
        :type server: Server
        :param message: Message received from client
        :type message: str
        :return: None
        :rtype: None
        """
        if self.testCase == 6:
            self.temperatureHumidity = message.split(" ")[0:4]
            self.temperature_signal.emit(self.temperatureHumidity)
            self.voltage = message.split(" ")[4]
            self.voltage = round((float(self.voltage) * 12.5) / 648, 2)
            self.voltage_signal.emit(float(self.voltage))
            try:
                self.speed = round((self.voltage * ((self.motorSpeed * 13000) / 250)) / 12, 2)
                self.speed_signal.emit(float(self.speed))
            except:
                pass

            flag, status = self.checkTemperature(float(self.temperatureHumidity[0].split("=")[1]), 'H Bridge')
            if not flag:
                self.yFlagTemperature.append(int(not flag))
                self.yFlagVoltage.append(0)
                self.failed = True
                self.stopTest(server, status)
                return

            flag, status = self.checkTemperature(float(self.temperatureHumidity[2].split("=")[1]), 'Motor')
            if not flag:
                self.yFlagTemperature.append(int(not flag))
                self.yFlagVoltage.append(0)
                self.failed = True
                self.stopTest(server, status)
                return

            self.yFlagTemperature.append(0)
            flag, status = self.checkVoltage(float(self.voltage))
            self.yFlagVoltage.append(int(not flag))
            if not flag:
                self.failed = True
                self.stopTest(server, status)
                return

    def stopTest(self, server, status):
        """
        Stop test execution\n
        :param server: Reference to application server
        :type server: Server
        :param status: Status of the test ( stopped by user, failed or finished )
        :type status: str
        """
        self.counter = self.testingTime + 5
        while len(self.xFlagValues) < 30:
            try:
                self.xFlagValues.append(self.xFlagValues[-1] + 1)
            except:
                self.xFlagValues.append(0)
            self.yFlagVoltage.append(0)
            self.yFlagTemperature.append(0)

        if len(self.xFlagValues) > 30:
            self.xFlagValues = self.xFlagValues[0:29]
            self.yFlagVoltage = self.yFlagVoltage[0:29]
            self.yFlagTemperature = self.yFlagTemperature[0:29]

        server.sendMessage("X")
        self.print_message_signal.emit(status)
        if self.failed:
            time.sleep(1)
            self.print_message_signal.emit('Test failed!')
        if status.find("Motor") != -1:
            time.sleep(1)
            self.print_message_signal.emit("Temperature:" + self.temperatureHumidity[0].split("=")[1])
        if status.find("H Bridge") != -1:
            time.sleep(1)
            self.print_message_signal.emit("Temperature:" + self.temperatureHumidity[2].split("=")[1])
        self.stop_test_signal.emit()
