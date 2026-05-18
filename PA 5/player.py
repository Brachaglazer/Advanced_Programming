from participant import Participant
from deck import Deck

class Player(Participant):
    '''Child of the participant class. Responsible for handling the participant other than the dealer.'''
    def __init__(self, name:str) -> None:
        super().__init__(name)

    def take_turn(self, deck:Deck) -> None:
        '''Responsible for carrying out the actions of the players turn'''
        while not self.is_busted():
            decision = input("\nWould you like to hit or stand? ")
            if decision.lower() == "hit":
                new_card = deck.deal_card()
                print(f"{self.name} draws: {new_card}")
                self.take_card(new_card)
                print(f"{self.name} total: {self.get_total()}")
            elif decision.lower() == "stand":
                break
            else:
                continue