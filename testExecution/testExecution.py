import time


class TestExecution:
    testingTime = 30
    motorSpeed = 0
    motorDirection = ""

    def __init__(self):
        pass

    def setMotorSpeed(self, value):
        self.motorSpeed = value

    def setMotorDirection(self, value):
        self.motorDirection = value

    def startTest(self, server):
        server.sendMessage("S 1 6 100")
        counter = 0
        while counter < self.testingTime:
            # send to uC parameters
            # receive from uC values
            # send signals to windows
            print(server.receiveMessage())
            counter += 1
            time.sleep(1)

    def stopTest(self):
        pass
