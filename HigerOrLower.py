import random

SUIT_TUPLE = ('Spades','Hearts','Clubs','Diamonds')
RANK_TUPLE = ('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')

NCARDS = 8

def get_card(deckList):
    this_card = deckList.pop()
    return this_card

def shuffle_deck(deckList):
    deckListOut = deckList.copy()

    random.shuffle(deckListOut)
    return deckListOut


print("Welcome to the Higher or Lower Game!")

