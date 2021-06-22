from Cards import Card
from Cards import Deck
from Cards import Deck_Maker

# import Cards


class Player:

    def __init__(self, card_packet, id):
        self.card_packet = card_packet
        self.id = id

    def are_equals(self, player2):
        if self.id == player2.id:
            return True
        return False

    def check_status(self):
        print(self.card_packet.length)
        if self.card_packet.length == 0:
            return True
        return False
