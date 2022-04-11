import os
import threading
import socket

import psutil


class Server:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = None
    port = None
    client = None
    clientAddress = None

    def __init__(self, host, port):
        self.socket.bind((host, port))
        threading.Thread(target=self.startServer).start()

    def startServer(self):
        print("Waiting for client!")
        self.socket.listen()
        self.client, self.clientAddress = self.socket.accept()
        print("Connected by ", self.clientAddress)

    def receiveMessage(self):
        # edit when pcb is ready
        # data = self.client.recv(1024)
        # data = data.decode()
        data = "T=26.5 H=60 T=27.5 H=61 12 12100"
        return data

    def sendMessage(self, response):
        try:
            self.client.sendall(bytes(response.encode()))
            print("Am trimis " + response + " catre client!")
        except BrokenPipeError:
            print("Client has been disconnected!")

