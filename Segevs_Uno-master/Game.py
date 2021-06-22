# Card Types
Card_Colors = ["red", "yellow", "green", "blue", "black"]
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

#not important

#    def __str__(self):
#       return '{}{}'.format(self.color_short, self.card_type_short)

#    def __eq__(self, other):
#       return self.color == other.color and self.type == other.card_type

#not important


    def valid_card(self, color, type):
        if color not in Card_Colors:
            raise ValueError("Invalid Color")
#        if color != 'black' and type not in Normal_Cards_Type and type not in Special_Cards_Type:
#            raise ValueError('Invalid card type')
#        if color == 'black' and type not in Black_Cards_Type:
#            raise ValueError('Invalid card type')

# not important

#    @property
#    def color_short(self):
#        return self.color[0].upper()

#    @property
#    def card_type_short(self):
#        if self.type in ('skip', 'reverse', 'wildcard'):
#            return self.type[0].upper()
#        else:
#            return self.type

# not important

# maybe important

    @property
    def _color(self):
        return self.temp_color if self.temp_color else self.color

# maybe important

    @property
    def temp_color(self):
        return self._temp_color

    @temp_color.setter
    def temp_color(self, color):
        if color is not None:
            if color not in Card_Colors:
                raise ValueError('Invalid color')
        self._temp_color = color

    def playable_card(self, different):
        return different.color == 'black' or self._color == different.color or self.type == different.card_type


class Player:
#   cards = [Card('red', n) for n in range(7)]
#  player = Client(cards)

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
