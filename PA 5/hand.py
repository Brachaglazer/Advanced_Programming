from card import Card

class Hand:
    '''List of card objects, used to keep track of the cards belonging to a participant'''
    def __init__(self) -> None:
        '''Initiates an empty lists to be used as the participants hand of cards.'''
        self.cards = []

    def add_card(self, card:Card) -> None:
        '''Adds the participants most recent card hit to their hand'''
        self.cards.append(card)

    def get_total(self) -> int:
        '''Calculates the total value of all cards in a participants hand to determine busts etc.'''
        total = 0
        contains_ace = False
        for card in self.cards:
            total += card.value
            if card.rank == "Ace":
                contains_ace = True
        if contains_ace and total <= 11:
            total += 10
        return total

    def show_hand(self) -> str:
        '''Tells the participants the contents of a hand so that they can decide on their next move.'''
        written_hand = ""
        for card in self.cards:
            written_hand += f"{card.__str__()} | "
        return written_hand

    def __str__(self) -> str:
        '''Describes the important details of a participants house.'''
        return f"{len(self.cards)} cards totalling to {self.get_total()} points containing {self.show_hand()}"