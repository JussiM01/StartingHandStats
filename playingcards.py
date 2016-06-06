# Class for playingcards.

import random

class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit=5, rank=0):
        self.suit = suit
        self.rank = rank
        
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades', None]
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                            Card.suit_names[self.suit])
