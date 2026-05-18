from hand import Hand
from card import Card
from deck import Deck

class Participant:
    '''Parent class to the player and dealer classes. Provides attributes and methods shared by both players.'''
    def __init__(self, name:str) -> None:
        self.name = name
        self.hand = Hand()

    def take_card(self, card:Card) -> None:
        '''Adds a card to a participants hand.'''
        self.hand.add_card(card)

    def show_hand(self) -> str:
        '''Reveals the cards of a participants hand.'''
        return self.hand.show_hand()

    def get_total(self) -> int:
        '''Retrieves the total points of the cards in a participants hand'''
        return self.hand.get_total()

    def is_busted(self) -> bool:
        '''Determines whether a participant is busted due to a total above 21 points.'''
        return self.get_total() > 21

    def take_turn(self, deck:Deck) -> None:
        '''Removes the top card from the deck and adds it to the participants hand.'''
        new_card = deck.deal_card()
        self.take_card(new_card)

#test
'''
deck = Deck()
deck.build_deck()
deck.shuffle()
part = Participant("test")
part.take_turn(deck)
part.take_turn(deck)
part.take_turn(deck)
print(part.get_total())
print(part.show_hand())
print(part.is_busted())
'''