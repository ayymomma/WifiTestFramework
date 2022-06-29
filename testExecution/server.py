import threading
import socket
import time


class Server:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = None
    connected = False
    messageReceived = None
    data = "T=26.5 H=60 T=27.5 H=61 12 12100"

    def __init__(self, host, port):
        """
        Initialize the server\n
        :param host: The IP of server
        :type host: str
        :param port: The PORT of server
        :type port: int
        """
        self.socket.bind((host, port))
        threading.Thread(target=self.startServer).start()
        threading.Thread(target=self.receiveMessage).start()

    def startServer(self):
        """
        Method used to start the server
        """
        print("Waiting for client!")
        self.socket.listen()
        self.client, clientAddress = self.socket.accept()
        print("Connected by ", clientAddress)
        self.connected = True

    def receiveMessage(self):
        """
        Receive a message from client and store it into a class variable\n
        """
        while True:
            if self.connected:
                self.data = self.client.recv(1024)
                self.data = self.data.decode()
                print("Am primit " + self.data + " de la client!")
                self.messageReceived = True
            time.sleep(0.5)

    def sendMessage(self, response):
        """
        Send a message to client\n
        :param response: The message that will be sent to client
        :type response: str
        """
        if self.connected:
            try:
                self.client.sendall(bytes(response.encode()))
                print("Am trimis " + response + " catre client!")
            except BrokenPipeError:
                print("Client deconectat")
                self.connected = False
