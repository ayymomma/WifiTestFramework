import time

from PyQt5.QtCore import QObject, pyqtSignal


class TestExecution(QObject):
    counter_signal = pyqtSignal(int)
    testingTime = 30
    motorSpeed = 0
    motorDirection = ""

    def __init__(self):
        super().__init__()

    def setMotorSpeed(self, value):
        self.motorSpeed = value

    def setMotorDirection(self, value):
        self.motorDirection = value

    def startTest(self, server):
        server.sendMessage("S 1 6 100")
        counter = 1
        while counter <= self.testingTime:
            self.counter_signal.emit(int(counter * 100 / self.testingTime))
            # send to uC parameters
            # receive from uC values
            # send signals to windows
            print(server.receiveMessage())
            counter += 1
            time.sleep(1)

    def stopTest(self):
        pass
