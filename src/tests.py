from poker import Card, PokerHand, create_deck, deal_hand

# some useful card suit/value constants
T = 'T'
J = 'J'
Q = 'Q'
K = 'K'
A = 'A'
H = 'H'
D = 'D'
S = 'S'
C = 'C'
# you can use integers for the others (but not 10 - use T)

# test single card
card_1 = Card(A, S)
card_2 = Card(A, D)
assert card_1 == card_2
card_3 = Card(K, S)
assert card_1 != card_3
assert card_1 > card_3
assert not card_1 < card_3

# test identifying hands
cards_1 = [Card(v, s) for v, s in [(A, S), (2, D), (4, C), (7,  H), (K, S)]]
high_card = PokerHand(cards_1)
assert high_card.hand_type == ("High Card", "A")

cards_2 = [Card(v, s) for v, s in [(A, S), (Q, S), (J, S), (T,  S), (K, S)]]
straight_flush = PokerHand(cards_2)
assert straight_flush.hand_type == ("Straight Flush", "A")

cards_3 = [Card(v, s) for v, s in [(A, S), (A, D), (A, H), (A,  C), (K, S)]]
four = PokerHand(cards_3)
assert four.hand_type == ("Four of a Kind", "A")

cards_4 = [Card(v, s) for v, s in [(A, S), (A, D), (A, H), (K,  C), (K, S)]]
full_house = PokerHand(cards_4)
assert full_house.hand_type == ("Full House", "A")

cards_5 = [Card(v, s) for v, s in [(A, S), (J, S), (8, S), (4,  S), (2, S)]]
flush = PokerHand(cards_5)
assert flush.hand_type == ("Flush", "A")

cards_6 = [Card(v, s) for v, s in [(6, D), (5, S), (4, H), (3,  S), (2, S)]]
straight = PokerHand(cards_6)
assert straight.hand_type == ("Straight", "6")

cards_7 = [Card(v, s) for v, s in [(6, D), (6, S), (6, H), (3,  D), (2, S)]]
three = PokerHand(cards_7)
assert three.hand_type == ("Three of a Kind", "6")

cards_8 = [Card(v, s) for v, s in [(6, D), (6, S), (3, H), (3, D), (2, S)]]
two_pair = PokerHand(cards_8)
assert two_pair.hand_type == ("Two Pair", "6")

cards_9 = [Card(v, s) for v, s in [(6, D), (6, S), (5, H), (3, D), (2, S)]]
pair = PokerHand(cards_9)
assert pair.hand_type == ("Pair", "6")

# test comparing two poker hands
cards = [Card(v, s) for v, s in [(A, S), (2, D), (4, C), (7,  H), (K, S)]]
hand_1 = PokerHand(cards)
cards = [Card(v, s) for v, s in [(A, C), (3, D), (5, C), (8,  H), (T, S)]]
hand_2 = PokerHand(cards)
assert hand_1 == hand_2
assert hand_2 == hand_1

cards = [Card(v, s) for v, s in [(A, S), (2, D), (4, C), (7,  H), (K, S)]]
hand_1 = PokerHand(cards)
cards = [Card(v, s) for v, s in [(Q, S), (3, D), (5, C), (8,  H), (T, S)]]
hand_2 = PokerHand(cards)
assert hand_1 > hand_2
assert hand_2 < hand_1

# Compare two hands better than High Card
assert full_house > flush
assert flush < full_house

assert straight_flush > four
assert four < straight_flush

# Compare same hands
pair_1_cards = [Card(v, s) for v, s in [(6, D), (6, S), (5, H), (3, D), (2, S)]]
pair_1 = PokerHand(pair_1_cards)
pair_2_cards = [Card(v, s) for v, s in [(7, D), (7, S), (5, H), (3, D), (2, S)]]
pair_2 = PokerHand(pair_2_cards)
assert pair_2 > pair_1
assert pair_1 < pair_2

straight_flush_1_cards = [Card(v, s) for v, s in [(A, S), (Q, S), (J, S), (T,  S), (K, S)]]
straight_flush_2_cards = [Card(v, s) for v, s in [(K, S), (J, S), (T, S), (9,  S), (Q, S)]]
straight_flush_1 = PokerHand(straight_flush_1_cards)
straight_flush_2 = PokerHand(straight_flush_2_cards)
assert straight_flush_1 > straight_flush_2
assert straight_flush_2 < straight_flush_1


# test creating a deck
deck = create_deck()
assert len(deck) == 52
assert all(isinstance(card, Card) for card in deck)

# test creating a hand from the deck
cards = deal_hand(5, deck)
hand_1 = PokerHand(cards)
cards = deal_hand(5, deck)
hand_2 = PokerHand(cards)
