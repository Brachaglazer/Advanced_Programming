from participant import Participant
from deck import Deck

class Dealer(Participant):
    '''A child of the participant class. Plays the role of the House in the game.'''
    def __init__(self) -> None:
        super().__init__("Dealer")

    def show_first_card(self) -> str:
        '''Reveals the dealer's first card for all participants to see and base their decisions off of.'''
        return self.hand.cards[0]

    def take_turn(self, deck:Deck) -> None:
        '''Adds cards to the dealer's hand until the hand totals at least 17'''
        while self.get_total() < 17:
            new_card = deck.deal_card()
            print(f"Dealer draws: {new_card}")
            self.take_card(new_card)
            print(f"Dealer total: {self.get_total()}")