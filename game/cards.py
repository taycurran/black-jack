from typing import Tuple

# An enumeration is a set of symbolic 
# names (members) bound to unique, constant values.
from enum import Enum

class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"

class Card:

    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()
    
    def _points(self) -> Tuple[int, int]:
        """return a two-tuple with the different ways to evaluate a card."""
        return int(self.rank), int(self.rank)

class AceCard(Card):

    def _points(self) -> Tuple[int, int]:
        return 1, 11

class FaceCard(Card):

    def _points(self) -> Tuple[int, int]:
        return 10, 10

# Factory Function Example A
def cardA(rank: int, suit: Suit) -> Card:
    if rank == 1:
        return AceCard("A", suit)
    elif 2 <= rank < 11:
        return Card(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: "J", 12: "Q", 13: "K"}[rank]
        return FaceCard(name, suit)
    raise Exception("Design Failure")

# Whoah... double list comprehension... trippy
deckA = [cardA(rank, suit) 
        for rank in range(1,14) 
        for suit in iter(Suit)] 

# The above comprehension is equivalent to the following loop.
def understand_cmp():
    deck = []
    for rank in range(1, 14):
        for suit in iter(Suit):
            dck.append(cardA(rank, suit))
    return deck

# Factory Function Example B

# We can map from the rank parameter to the class that must be constructed

# --- Understand Dict.get() to Understand how CardB works... ---
# Return Value from get()
# The get() method returns:

# the value for the specified key if key is in dictionary.
# None if the key is not found and value is not specified.
# -- value if the key is not found and value is specified. --

d = {1: 11, 2: 22, 3: 33}
assert d[2] == 22
assert d.get(2) == 22
assert d.get(4) == None
assert d.get(4, d[3]+11) == 44


def cardB(rank: int, suit: Suit) -> Card:
    # The Card value is specified in the get 
    # statement if the rank is not found.
    class_ = {1: AceCard, 11: FaceCard, 12: FaceCard,
                13: FaceCard}.get(rank, Card)
    return class_(str(rank), suit)

deckB = [cardB(rank, suit) 
        for rank in range(1,14) 
        for suit in iter(Suit)] 

# The cardB() function, however, has a serious deficiency. 
# It lacks the translation from 1 to A and 13 to K that we had in previous versions.