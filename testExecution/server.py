import threading
import socket
import time


class Server:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = None
    port = None
    client = None
    clientAddress = None
    connected = False
    messageReceived = None
    data = "T=26.5 H=60 T=27.5 H=61 12 12100"

    def __init__(self, host, port):
        self.socket.bind((host, port))
        threading.Thread(target=self.startServer).start()
        threading.Thread(target=self.receiveMessage).start()

    def startServer(self):
        print("Waiting for client!")
        self.socket.listen()
        self.client, self.clientAddress = self.socket.accept()
        print("Connected by ", self.clientAddress)
        self.connected = True

    def receiveMessage(self):
        while True:
            if self.connected:
                self.data = self.client.recv(1024)
                self.data = self.data.decode()
                print("Am primit " + self.data + " de la client!")
                self.messageReceived = True
            time.sleep(0.5)

    def sendMessage(self, response):
        if self.connected:
            try:
                self.client.sendall(bytes(response.encode()))
                print("Am trimis " + response + " catre client!")
            except BrokenPipeError:
                print("Client deconectat")
                self.connected = False
