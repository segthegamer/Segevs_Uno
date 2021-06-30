import socket
import pygame
import pickle
from Game_Data import Game
from Cards import Card
from Cards import Deck
from Cards import Deck_Maker


class Client(object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.base_game = None

    def start(self):
        try:
            print('connecting to ip %s port %s' % (ip, port))
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            print('connected to server')

            while True:
                self.base_game = self.recv_from_server(sock)
                print(self.base_game.current)

                if(self.base_game.current == 2):
                    player = self.base_game.Player2
                    self.make_move(player , self.base_game)
                    self.base_game.current -= 1
                    print(self.base_game.current)
                    self.send_game_to_server(self.base_game , sock)
                
                print("heyyyy")

        except socket.error as e:
            print(e)

    def recv_from_server(self , clientSocket):

        size = clientSocket.recv(int(16))
        print(size)
        data = clientSocket.recv(int(size))
        x = pickle.loads(data)
        return x 


    def send_game_to_server(self, game , clientSocket):
        
        data = pickle.dumps(game, 0)
        size = str(len(data)).ljust(16).encode('utf-8')
        clientSocket.send(size)
        clientSocket.send(data)
            
    def make_move(self , player , game):
        print(game.card_on_table)
        print(game.Player1.card_packet)
        inp = int(input("enter withdraw index"))
        self.base_game.take_out_card(player , inp)



if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1760
    c = Client(ip, port)
    c.start()
