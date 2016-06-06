"""Functions for checking the strenght of a five card poker hand."""

from playingcards import *

def first_better(first_value, second_value):
    if first_value[0] > second_value[0]: return True
    if first_value[0] < second_value[0]: return False
    for i in range(len(second_value[1])):
        if first_value[1][i] > second_value[1][i]: return True
    return False 

def straight_or_flush(cards):
    for value in straight_flush(cards), flush(cards), straight(cards):
        if value: return value

def duplicate_ranks(cards):
    for value in trips_or_more(cards), two_pair(cards), pair(cards):
        if value: return value

def trips_or_more(cards):
    for value in quads(cards), full_house(cards), three_of_a_kind(cards):
        if value: return value
        
def straight_flush(cards):
    flush_value, straight_value = flush(cards), straight(cards)
    if flush_value and straight_value: return [8, straight_value[1]]

def flush(cards):
    for i in range(4):
        if cards[i].suit != cards[i+1].suit: return None
    return [5, [card.rank for card in cards]]

def straight(cards):
    if highest_A_lowest_2(cards):
        ace_lowest = Card(cards[0].suit, 1)
        new_representation = cards[1:] + [ace_lowest]
        return straight(new_representation)
    for i in range(4):
        if cards[i].rank != cards[i+1].rank + 1: return None
    return [4, [cards[0].rank]]

def highest_A_lowest_2(cards):
    return (cards[0].rank == 14 and cards[4].rank == 2)

def quads(cards):
    if sum([cards[i].rank for i in range(4)]) == 4 * cards[0].rank:
        return [7, [cards[0].rank, cards[-1].rank]]
    if sum([cards[i].rank for i in range(1,5)]) == 4 * cards[-1].rank:
        return [7, [cards[-1].rank, cards[0].rank]]
               
def full_house(cards):
    if (cards[0].rank == cards[1].rank == cards[2].rank and
        cards[3].rank == cards[4].rank):
        return [6, [cards[0].rank, cards[-1].rank]]
    if (cards[2].rank == cards[3].rank == cards[4].rank and
        cards[0].rank == cards[1].rank):
        return [6, [cards[-1].rank, cards[0].rank]]

def three_of_a_kind(cards):
    for i in range(3):
        if cards[i].rank == cards[i+1].rank == cards[i+2].rank:
            return [3, [cards[i].rank] +
                    [cards[k].rank for k in range(5)
                     if k not in range(i,i+3)]]

def two_pair(cards):
    if cards[0].rank == cards[1].rank:
        if cards[2].rank == cards[3].rank:
            return [2, [cards[0].rank, cards[2].rank, cards[4].rank]]
        if cards[3].rank == cards[4].rank:
            return [2, [cards[0].rank, cards[3].rank, cards[2].rank]]
    if cards[1].rank == cards[2].rank:
        if cards[3].rank == cards[4].rank:
            return [2, [cards[1].rank, cards[3].rank, cards[0].rank]]
                                                
def pair(cards):
    for i in range(4):
        if cards[i].rank == cards[i+1].rank:
            return [1, [cards[i].rank] + [cards[k].rank for k in range(5)
                    if k not in range(i,i+2)]]
