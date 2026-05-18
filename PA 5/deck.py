import random
from card import Card

SUITS = ["Spades", "Clubs", "Hearts", "Diamonds"]
RANKS = {
    "Ace": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}

class Deck:
    '''List of card objects, used to deal cards to the participants.'''
    def __init__(self) -> None:
        '''Initiates an empty list to be used as the deck of playing cards.'''
        self.cards = []

    def build_deck(self) -> None:
        '''Builds a virtual deck of cards to be used.'''
        self.cards = []
        for rank, value in RANKS.items():
            for suit in SUITS:
                new_card = Card(suit, rank, value)
                self.cards.append(new_card)

    def shuffle(self) -> None:
        '''Shuffles the deck of cards in order to deal a randomly rather than in the order the deck was created.'''
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        '''Deals the top card of the deck to the participant hitting.'''
        return self.cards.pop(0)

    def cards_remaining(self) -> int:
        return len(self.cards)