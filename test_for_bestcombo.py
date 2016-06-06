""" Test for bestcombo. This test checks that a 5 high straight flush is
detected correctly."""

from bestcombo import *

for i in range(10000):
    deck = Deck()
    pocket_cards = Hand()
    community_cards = PokerHand()

    deck.shuffle()

    deck.move_cards(pocket_cards, 2)
    deck.move_cards(community_cards, 5)

    bc = best_combo(pocket_cards, community_cards)

    if bc[0] == 8 and bc[1][0] == 5:
        print('pocket_cards:')
        print(pocket_cards)
        print('community_cards:')
        print(community_cards)
        print(bc)
        print('')
