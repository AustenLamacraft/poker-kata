from itertools import product
from random import shuffle
from collections import Counter

VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'S', 'C')

HAND_TYPES = (
        'High Card',
        'Pair',
        'Two Pairs',
        'Three of a Kind',
        'Straight',
        'Flush',
        'Full House',
        'Four of a Kind',
        'Straight Flush'
)

class Card:
    def __init__(self, value, suit):
        value = str(value)
        suit = str(suit)
        if value not in VALUES:
            raise ValueError
        self.value = value
        if suit not in SUITS:
            raise ValueError
        self.suit = suit

    def __repr__(self):
        return '<Card object {}{}>'.format(self.value, self.suit)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value_index < other.value_index

    def __gt__(self, other):
        return self.value_index > other.value_index

    @property
    def value_index(self):
        return VALUES.index(self.value)


class PokerHand:
    def __init__(self, cards):
        if any(not isinstance(card, Card) for card in cards):
            raise ValueError
        if len(cards) != 5:
            raise ValueError
        card_set = {repr(card) for card in cards}
        duplicate_cards = len(card_set) < len(cards)
        if duplicate_cards:
            raise ValueError
        self.cards = sorted(cards)


    @property
    def hand_type(self):
        value_counts = Counter([card.value for card in self.cards]).most_common()
        value_spread = self.cards[4].value_index - self.cards[0].value_index
        suit_counts = Counter([card.suit for card in self.cards])


        if value_spread == 4 and len(suit_counts) == 1:
            return "Straight Flush", self.cards[-1].value
        elif value_counts[0][1] == 4:
            return "Four of a Kind", self.cards[-1].value
        elif value_counts[0][1] == 3 and value_counts[1][1] == 2:
            return "Full House", self.cards[-1].value
        elif len(suit_counts) == 1:
            return "Flush", self.cards[-1].value
        elif value_spread == 4 and len({card.value for card in self.cards}) == 5:
            return "Straight", self.cards[-1].value
        elif value_counts[0][1] == 3:
            return "Three of a Kind", value_counts[0][0]   # Value of the three
        elif value_counts[0][1] == 2 and value_counts[1][1] == 2:
            return "Two Pair", max(value_counts[0][0], value_counts[1][0]) #Value of higher pair, which may be second...

        elif value_counts[0][1] == 2:
            return "Pair", value_counts[0][0]
        else:
            return "High Card", self.cards[-1].value

    def __repr__(self):
        return '<PokerHand object {}>'.format(', '.join(str(card) for card in self))

    def __iter__(self):
        return iter(self.cards)

    def __gt__(self, other):
        if self.hand_type[0] != other.hand_type[0]:
            return HAND_TYPES.index(self.hand_type[0]) > HAND_TYPES.index(other.hand_type[0])
        else:
            return VALUES.index(self.hand_type[1]) > VALUES.index(other.hand_type[1])

    def __lt__(self, other):
        if self.hand_type[0] != other.hand_type[0]:
            return HAND_TYPES.index(self.hand_type[0]) < HAND_TYPES.index(other.hand_type[0])
        else:
            return VALUES.index(self.hand_type[1]) < VALUES.index(other.hand_type[1])

    def __eq__(self, other):
        return self.cards[-1] == other.cards[-1]

def create_deck():
    cards = [Card(value, suit) for value, suit in product(VALUES, SUITS)]
    shuffle(cards)
    return cards

def deal_hand(n, deck):
    return [deck.pop() for i in range(n)]
