# Classes for decks and differen type of hands.

from playingcards import *
from handstrengthfunctions import *

class Deck(object):

    def __init__(self):
        self.cards = []     # Refactor this as a list comprehension?
        for suit in range(4):
            for rank in range(2, 15):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []            # Refactor this as a list comprehension?
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self): return self.cards.pop()

    def add_card(self, card): self.cards.append(card)

    def shuffle(self): random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def sort_cards(self):
        self.cards.sort(key=lambda x: x.rank, reverse=True)

class Hand(Deck):
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label
    
class PokerHand(Hand):

    def wins(self, other):
        return first_better(self.evaluate(), other.evaluate())

##    def wins(self, other):
##        value_self, value_other = self.evaluate(), other.evaluate()
##        if value_self[0] > value_other[0]: return True
##        if value_self[0] < value_other[0]: return False
##        for i in range(len(value_self[1])):
##            if value_self[1][i] > value_other[1][i]: return True
##        return False
                
    def evaluate(self):
        self.sort_cards()
        for value in straight_or_flush(self.cards), duplicate_ranks(self.cards):
            if value: return value
        return [0, [card.rank for card in self.cards]]
