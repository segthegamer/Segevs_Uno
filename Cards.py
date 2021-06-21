import random


class Card:
    def __init__(self, color, type):
        self.color = color
        self.type = type

    def __str__(self):
        # print for card class
        return f"{self.color} , {self.type}"

    def is_equal(self, card):
        # checks to card for button eval
        if self.type == card.amount or self.color == card.color:
            return True
        return False


class Deck:
    def __init__(self, cards):
        # init for Deck
        self.deck = cards
        self.length = len(self.deck)

    def Add_card_to_deck(self, card):
        # adds card to deck
        self.deck.append(card)
        self.Deck_update()

    def Remove_card_from_deck(self, index):
        # get the last card from deck
        self.deck.pop(index)
        self.Deck_update()
        return card

    def Combine_deck(self, cards):
        # combines two packets
        for card in cards.card_packet:
            self.Add_card_to_deck(card)

    def Deck_update(self):
        # updates the length property (for win conditions)
        self.length = len(self.deck)


'''
    def check_for_button(self, card):
        # checks button, used only when packet is open
        index = 3  # TODO:change .
        for i in self.card_packet:
            if (i == index):
                if (self.card_packet[i].is_equal(card)):
                    self.withdraw_card(index)
'''


class Deck_Maker:

    Card_Colors = ["red", "yellow", "green", "blue"]
#    amounts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Normal_Cards_Type = list(range(0, 10)) + list(range(1, 10))

    def __init__(self):
        self.cards_lst = []

        for Color in self.Card_Colors:
            for Type in self.Normal_Cards_Type:
                card = Card(Type, Color)
                self.cards_lst.append(card)
        self.cards_lst = self.cards_lst * 2

    def random_card(self):
        rand_type = random.randint(0, 10)
        rand_color = random.choice(self.Card_Colors)
        return Card(rand_type, rand_color)

# what do i change
    def make_deck(self):
        index = random.sample(range(0, 40), 40)
        Deck_1 = []
        Deck_2 = []

        for i in range(0, 40):
            if i % 2 == 0:
                Deck_1.append(self.cards_lst[index[i]])
            else:
                Deck_2.append(self.cards_lst[index[i]])
        Client_1_Deck = Deck(Deck_1)
        Client_2_Deck = Deck(Deck_2)
        return Client_1_Deck, Client_2_Deck

