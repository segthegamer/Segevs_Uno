from Cards import Card
from Cards import Deck
from Cards import Deck_Maker
from Player_Data import Player

import pickle
import threading


# import Player_Data
# import Cards

class Game:
    def __init__(self):

#        Temp_deck = Deck_Maker()
#        packet_tup = Temp_deck.make_deck()

        self.card_dis = Deck_Maker()
        packet_tup = self.card_dis.make_deck()
        self.Player1 = Player(packet_tup[0], "1")
        self.Player2 = Player(packet_tup[1], "2")
        self.card_on_table = self.card_dis.random_card()

        self.listUsers = [self.Player1, self.Player2]

    def withdraw(self, player):

        if self.Player1.are_equals(player):
            self.Player1.card_packet.add_packet_to_packet(self.card_dis.random_card())

        if self.Player2.are_equals(player):
            self.Player2.card_packet.add_packet_to_packet(self.card_dis.random_card())
