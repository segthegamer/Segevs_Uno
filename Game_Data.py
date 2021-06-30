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
        self.card_dis = Deck_Maker()
        packet_tup = self.card_dis.make_deck()
        self.Player1 = Player(packet_tup[0], "1")
        self.Player2 = Player(packet_tup[1], "2")
        self.current = 1
        self.card_on_table = self.card_dis.random_card()

        self.listUsers = [self.Player1, self.Player2]

    def __str__(self) -> str:

        print(self.Player1.card_packet)
        print("############################################################################################")
        print(self.Player2.card_packet)
        print("############################################################################################")
        print(self.card_on_table)
        return "hey"


    def withdraw(self, player):

        if self.Player1.are_equals(player):
            self.Player1.card_packet.Add_card_to_deck(self.card_dis.random_card())

        if self.Player2.are_equals(player):
            self.Player2.card_packet.Add_card_to_deck(self.card_dis.random_card())
    


    def take_out_card(self , player , index):
        
        if self.Player1.are_equals(player):

            if(self.card_on_table.is_equal(self.Player1.card_packet.deck[index])):
                x = self.Player1.card_packet.Remove_card_from_deck(index)
                self.card_on_table = x 
            
        if self.Player2.are_equals(player):
                
                if(self.card_on_table.is_equal(self.Player2.card_packet.deck[index])):
                    x = self.Player2.card_packet.Remove_card_from_deck(index)
                    self.card_on_table = x 


