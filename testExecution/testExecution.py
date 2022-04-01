import time

from PyQt5.QtCore import QObject, pyqtSignal


class TestExecution(QObject):
    counter_signal = pyqtSignal(int)
    testingTime = 30
    motorSpeed = 100
    motorDirection = 1
    counter = 1
    testCase = 1

    def __init__(self):
        super().__init__()

    def setMotorSpeed(self, value):
        self.motorSpeed = value

    def setMotorDirection(self, value):
        self.motorDirection = value


    def startTest(self, server):
        server.sendMessage("S {motorDirection} {testCase} {motorSpeed}".format(motorDirection=self.motorDirection,
                                                                               testCase=self.testCase,
                                                                               motorSpeed=self.motorSpeed))
        server.receiveMessage()
        self.counter = 1

        while self.counter <= self.testingTime:
            self.counter_signal.emit(int(self.counter * 100 / self.testingTime))
            # send to uC parameters
            # receive from uC values
            # send signals to windows
            self.processServerValues(server.receiveMessage())
            self.counter += 1
            time.sleep(1)

    def processServerValues(self, message):
        print(message)

    def stopTest(self, server):
        self.counter = 0
        server.sendMessage("X")
