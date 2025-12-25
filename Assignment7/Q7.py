
import random
def deal_cards():
    deck = list(range(52))
    random.shuffle(deck)
    hand = deck[:5]
    return hand

hand = deal_cards()
print("Dealt hand of 5 cards:", hand)
