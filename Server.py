import socket
import threading
import random
import itertools
import pygame
from queue import Queue
import Cards
from Game_Data import Game
import pickle

# Card Types
Card_Colors = ["red", "yellow", "green", "blue", "black"]
Normal_Card_Colors = ["red", "yellow", "green", "blue"]
Special_Cards_Type = ["skip", "reverse", "plus2"]
Black_Cards_Type = ["changeColor", "plus4"]
Normal_Cards_Type = list(range(0, 10)) + list(range(1, 10))
Total_Card_Types = Normal_Cards_Type + Special_Cards_Type + Black_Cards_Type

# Card Amounts
Normal_Cards_Amount = (Normal_Cards_Type + (Special_Cards_Type * 2))
Black_Cards_Amount = (4 * Black_Cards_Type)
Total_Card_Amount = ((len(Card_Colors) * Normal_Cards_Amount) + Black_Cards_Amount)


class Card:
    # color - "red", "yellow", "green", "blue", "black"
    # type - "skip", "reverse", "plus2", "changeColor", "plus4", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    def __init__(self, color, type):
        self.valid_card(color, type)
        self.color = color
        self.type = type
        self.temp_color = None

    def __repr__(self):
        return '{} {}'.format(self.color, self.type)

    def valid_card(self, color, type):
        if color not in Card_Colors:
            raise ValueError("Invalid Color")

    def get_color(self):
        return self.temp_color if self.temp_color else self.color

    def get_temp_color(self):
        return self.temp_color

    def set_temp_color(self, color):
        if color is not None:
            if color not in Card_Colors:
                raise ValueError('Invalid color')
        self.temp_color = color

    def playable_card(self, different):
        return different.color == 'black' or self.color == different.color or self.type == different.card_type


class Player:
    # cards = [Card('red', n) for n in range(7)]
    # player = Client(cards)

    def __init__(self, cards, player_id=None):
        if len(cards) != 7:
            raise ValueError("Players must start with 7 cards")
        if not all(isinstance(card, Card) for card in cards):
            raise ValueError('Invalid player: cards must all be Card objects')
        self.hand = cards
        self.player_id = player_id

    def __repr__(self):
        if self.player_id is not None:
            return '<Client object: player {}>'.format(self.player_id)
        else:
            return '<Client object>'

    def __str__(self):
        if self.player_id is not None:
            return str(self.player_id)
        else:
            return repr(self)

    def can_play(self, current_card):
        return any(current_card.playable(card) for card in self.hand)


def make_card():
    type_1 = random.randint(0, 10)
    color_1 = random.choice(Card_Colors)
    return Card(color_1, type_1)


def make_deck():
    temp_deck = []
    counter = 0
    while counter != 7:
        temp_deck.append(make_card())
        counter += 1
    return temp_deck


def valid_placement(deck_card, word):
    new_card_color = word[1]
    new_card_type = word[2]

    deck_card_color = deck_card[0]
    deck_card_type = deck_card[1]

    if new_card_color == 'black':
        return True
    elif new_card_color == deck_card_color:
        return True
    elif new_card_type == deck_card_type:
        return True
    else:
        return False


class Server(object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.dictSocketId = {}
        self.dictThreadsId = {}
        self.count = 0
        self.sumClient = 0
        self.q = Queue()

    def start(self):
        try:
            print('server starts up on ip %s port %s' % (self.ip, self.port))
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self.ip, self.port))
            sock.listen(2)

            while True:
                print('waiting for a new client')

                clientSocket, client_address = sock.accept()  # block
                self.dictSocketId[self.sumClient] = clientSocket
                self.dictThreadsId[self.sumClient] = threading.Thread(target=self.handle_client_connection,
                                                                      args=(self.count, clientSocket, self.count))
                self.dictThreadsId[self.sumClient].start()
                self.count += 1
                if (self.count == 2):
                    break

            while True:
                print(self.q.get())


        except socket.error as e:
            print(e)

    def sendAllClient(self, data):  # שולח מידע לכל הלקוחות בלולאה
        #        data = pickle.dumps(Game, 0)
        size = str(len(data)).ljust(16).encode('utf-8')
        for clientId in self.dictThreadsId:
            self.dictSocketId[clientId].send(size)
            self.dictSocketId[clientId].send(data)

    def handleClient(self, clientSock, current):
        print("hello")
        client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current, current))
        client_handler.start()

    def table(self, num):
        st = ""
        for i in range(1, num + 1):
            for j in range(1, num + 1):
                st += str(i * j) + " "
            st += "\n"
        return st

    #    def send_image(self , data_tup):
    #        header = data_tup[0]
    #        print(header)
    #        data = data_tup[1]
    #        self.ClientSocket.send(header)
    #        self.ClientSocket.send(data)

    #   def from_bytes(frame_data):

    #        frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    #        return frame

    def handle_client_connection(self, client_socket, current, id):
        print("start")
        while True:
            #            if self.count == 2:
            #                client_socket.sendall('Game is starting'.encode())
            #                deck_card = make_card()
            while True:
                size = client_socket.recv(16)
                data = client_socket.recv(size)
                x = pickle.loads(data)
                self.q.put((x, id))
                data = pickle.loads(Game, 0)
                size = str(len(data)).ljust(16).encode('utf-8')


#                    message = client_socket.recv(1024).decode()
#                    word = message.split()
#                    if word[0] == 'pull':
#                        pulled = make_card()
#                    elif word[0] == 'place':
#                        if
#                        deck_card_color = word[1]
#                        deck_card_type = word[2]
#                        deck_card = (deck_card_color + ' ' + deck_card_type)

#                    print('Message recived - ' + message)
#                    client_socket.sendall(('Message recived - ' + message).encode())


if __name__ == '__main__':
    ip = '0.0.0.0'
    port = 1731
    s = Server(ip, port)
    s.start()
