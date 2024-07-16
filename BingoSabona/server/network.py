import socket
import time

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.102"  # Update this with your global server IP
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos

    def connect(self):
        connected = False
        while not connected:
            try:
                self.client.connect(self.addr)
                return self.client.recv(2048).decode()
                connected = True
            except Exception as e:
                print("Connection failed:", e)
                print("Retrying in 5 seconds...")
                time.sleep(5)

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print("Error sending data:", e)