import socket
import pygame
import pickle
from Game_Data import Game
from Cards import Card
from Cards import Deck
from Cards import Deck_Maker

#Graphics
pygame.init()

#Title and icon
pygame.display.set_caption("Segev's Uno - Player 1")
icon = pygame.image.load('black_+4.png')
pygame.display.set_icon(icon)

# Game window
Screen_Width = 1200
Screen_Height = 600
screen = pygame.display.set_mode((Screen_Width, Screen_Height))

# Constants
Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 128)
Red = (256, 0, 0)
LeftMouse = 1
MiddleMouse = 2
RightMouse = 3


# Background image

def RedrawWindow():
    backround = pygame.image.load('background.png')
    screen.blit(backround, (0, 0))
    screen.fill(White)
    DrawBlank()
    pygame.display.update()

def DrawBlank():
    card_image = pygame.image.load('back.png')
    card_image.convert()
    rect = card_image.get_rect()
    rect.center = Screen_Width // 2, Screen_Height // 2
    screen.blit(card_image, rect)
    pygame.display.update()

def DrawCard(type, color):
    # make valid type and color check
    make_image = color + "_" + type + ".png"
    card_image = pygame.image.load(make_image)
    card_image.convert()

    rect = card_image.get_rect()
    rect.center = Screen_Width // 2, Screen_Height // 2

    screen.blit(card_image, rect)
    pygame.display.update()


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
#            msg = sock.recv(1024)
#            print('received message: %s' % msg.decode())
#            sock.sendall('This is client 1'.encode())
            # implement here your main logic
            while True:
                self.handle_client(sock)
        except socket.error as e:
            print(e)

    def handle_client(self, serverSocket):
#        Message = serverSocket.recv(1024).decode()
#        print(Message)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   run = False
            RedrawWindow()
            print("Your cards: ")
            print("Your card total: ")
            print("Opponent card total: ")
            print("deck card: ")
            action = input(
                "Select action: Pull, Place (Pull - Pulls new card from bank,"
                " Place + the card you wish to place)")
            action.lower()
            split_action = action.split()
            if split_action[0] == 'pull' or split_action[0] == 'place':
                serverSocket.send(action.encode())
            else:
                while action.lower() != 'pull' or action.lower() != 'place':
                    print("Invalid action, please select the following: ")
                    action = input(
                        "Select action: Pull, Place (Pull - Pulls new card from bank,"
                        " Place + the card you wish to place)")
                    action.lower()
                    split_action = action.split()
                    if split_action[0] == 'pull' or split_action[0] == 'place':
                        break
            #            if split_action[0] == 'place':
            #                sent_card = input("Enter the card you")

#            serverSocket.send(action.encode())
#            Running_Message = serverSocket.recv(1024).decode()
#            if Running_Message == 'Game has ended':
#                break
#            print(Running_Message)
            size = serverSocket.recv(16)
            data = serverSocket.recv(size)
            data = pickle.dumps(Game, 0)
            size = str(len(data)).ljust(16).encode('utf-8')
            self.ClientSocket.send(size)
            self.ClientSocket.send(data)



if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1731
    c = Client(ip, port)
    c.start()
