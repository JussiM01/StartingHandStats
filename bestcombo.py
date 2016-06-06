""" Functions for checking the best combination of pocket cards and
community cards."""

from playingcards import *
from pokerhands import *

##deck = Deck()
##pocket_cards = Hand()
##community_cards = PokerHand()
##
##deck.shuffle()
##
##deck.move_cards(pocket_cards, 2)
##deck.move_cards(community_cards, 5)
##
##print('pocket_cards:')
##print(pocket_cards)
##print('community_cards:')
##print(community_cards)


indecies = (0, 1, 2, 3, 4)
four_indecies = {indecies[:i] + indecies[i+1:] for i in range(5)}
three_indecies = {four_index[:i] + four_index[i+1:] for i in range(4)
                  for four_index in four_indecies}
##print(four_indecies)
##print(three_indecies)

def best_combo(pocket_cards, community_cards):
    test = PokerHand()
    test.cards = community_cards
    best_value = community_cards.evaluate()
    for card in pocket_cards.cards:
        test_value = best_combo_with_1(card, community_cards)
        if first_better(test_value, best_value): best_value = test_value
        #print('best_value:', best_value)
    test_value = best_combo_with_2(pocket_cards, community_cards)
    if first_better(test_value, best_value): best_value = test_value
    return best_value
    
def best_combo_with_1(card, community_cards):
    best_value = [0, [0] * 5]
    test_hand = PokerHand()
    for indecies in four_indecies:
        test_hand.cards = [card] + [community_cards.cards[i] for i in indecies]
        test_value = test_hand.evaluate()
        if first_better(test_value, best_value): best_value = test_value
    return best_value
        
def best_combo_with_2(pocket_cards, community_cards):
    best_value = [0, [0] * 5]
    test_hand = PokerHand()
    for indecies in three_indecies:
        test_hand.cards = pocket_cards.cards + [community_cards.cards[i]
                                                for i in indecies]
        test_value = test_hand.evaluate()
        if first_better(test_value, best_value): best_value = test_value
    return best_value

##print(best_combo(pocket_cards, community_cards))
