import socket
import Game

class Client(object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start(self):
        try:
            print('connecting to ip %s port %s' % (ip, port))
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            print('connected to server')
            # send receive example
            msg = sock.recv(1024)
            print('received message: %s' % msg.decode())
            sock.sendall('This is client 1'.encode())
            # implement here your main logic
            while True:
                self.handle_client(sock)
        except socket.error as e:
            print(e)

    def handle_client(self, serverSocket):
        Message = serverSocket.recv(1024).decode()
        print(Message)
        while True:
            print("Your cards: ")
            print("Your card total: ")
            print("Opponent card total: ")
            print("deck card: ")
            action = input(
                "Select action: Pull, Place (Pull - Pulls new card from bank,"
                " Place + the card you wish to place)")
            if action.lower() == 'pull' or action.lower() == 'place':
                serverSocket.send(action.encode())
            else:
                while action.lower() != 'pull' or action.lower() != 'place':
                    print("Invalid action, please select the following: ")
                    action = input(
                        "Select action: Pull, Place (Pull - Pulls new card from bank,"
                        " Place + the card you wish to place)")
                    if action.lower() == 'pull' or action.lower() == 'place':
                        break
            if action.lower() == 'place':
                sent_card = input("Enter the card you")

            serverSocket.send(action.encode())
            Running_Message = serverSocket.recv(1024).decode()
            if Running_Message == 'Game has ended':
                break
            print(Running_Message)


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1731
    c = Client(ip, port)
    c.start()
