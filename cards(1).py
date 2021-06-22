import random

class Card():
    def __init__(self, amount, color):
        #init card class
        self.amount = amount
        self.color = color

    def __str__(self):
        ##print for card class
        return f"{self.color} , {self.amount}"

    def is_equal(self, card):
        #checks to card for button eval
        if(self.amount == card.amount or self.color == card.color):
            return True
        return False
    


class CardPacket():
    def __init__(self, cards):
        ##init for CardPacket
        self.card_packet = cards
        self.length = len(self.card_packet)

    def __add_to_packet(self, card):
        ##adds card to pacekt
        self.card_packet.append(card)
        self.__update_length()

    def __update_length(self):
        #updates the length property (for win condtions)
        self.length = len(self.card_packet)

    def add_packet_to_packet(self, cards):
        #combines two packets
        for card in cards.card_packet:
            self.__add_to_packet(card)

    def withdraw_card(self , index):
        #get the last card from packet
        self.card_packet.pop(index)
        self.__update_length()
        return card

    def check_for_button(self ,card):
        #checks button, used only when packet is open
        index = 3 #TODO:change .
        for i in self.card_packet:
            if(i == index):
                if(self.card_packet[i].is_equal(card)):
                    self.withdraw_card(index)

class CardPacketDistirbuter():

    colors = ['R', 'y', 'G', 'C']
    amounts = [0 , 1, 2 , 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):

        self.cards_lst = []

        for shape in self.colors:
            for amount in self.amounts:
                card = Card(amount, shape)
                self.cards_lst.append(card)

        self.cards_lst = self.cards_lst*2

    def disterbute_packet(self):
        index = random.sample(range(0,  40), 40)
        cards1 = []
        cards2 = []
        for i in range(0, 40):
            if(i%2 == 0):
                cards1.append(self.cards_lst[index[i]])
            else:
                cards2.append(self.cards_lst[index[i]])
        player1_cards = CardPacket(cards1)
        player2_cards = CardPacket(cards2)
        return (player1_cards, player2_cards)

    def randCard(self):
        type_1 = random.randint(0, 10)
        color_1 = random.choice(self.colors)
        return Card(type_1, color_1)

        


x = CardPacketDistirbuter()
x.disterbute_packet()