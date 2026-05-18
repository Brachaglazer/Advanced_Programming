from deck import Deck
from player import Player
from dealer import Dealer

class BlackJackGame():
    '''
        Main Controller for game.
        Responsible for initially setting up the game, playing a round, and determining the winner.
    '''
    def __init__(self, player_name:str) -> None:
        self.deck = Deck()
        self.player = Player(player_name)
        self.dealer = Dealer()

    def initial_deal(self) -> None:
        '''Responsible for the initial setup of the game.
        Creates and shuffles the deck and deals two cards to both the player and dealer.
        Reveals both of the players cards, but only the first of the dealers cards.
        '''
        self.deck.build_deck()
        self.deck.shuffle()
        participants = [self.player, self.dealer]
        print("\n---DEALING CARDS---")
        for r in range(2):
            for p in participants:
                new_card = self.deck.deal_card()
                p.take_card(new_card)

        self.show_game_state()

    def show_game_state(self) -> None:
        '''Reveal all the users cards and only the first of the dealers cards.'''
        print("")
        print(f"{self.player.name}'s hand: {self.player.show_hand()}")
        print(f"Dealer's first card: {self.dealer.show_first_card()}")

    def determine_winner(self) -> str:
        '''Determine the winner based on the points in each the player and dealers hands.'''
        print("\n---FINAL HANDS---")
        participants = [self.dealer, self.player]
        for p in participants:
            print(f"\n{p.name}'s hand: {p.show_hand()}")
            print(f"{p.name}'s points: {p.get_total()}")
        print("\n---RESULT---")
        if self.player.is_busted():
            print(f"{self.player.name} is busted.")
            return "Dealer"
        if self.dealer.is_busted():
            print(f"Dealer is busted, {self.player.name} is not.")
            return self.player.name
        if (21 - self.dealer.get_total()) > (21 - self.player.get_total()):
            print(f"{self.player.name} got closer to 21 than the dealer did.")
            return self.player.name
        elif (21 - self.dealer.get_total()) == (21 - self.player.get_total()):
            return f"Dealer and {self.player.name}"
        else:
            print(f"Dealer got closer to 21 than {self.player.name} did.")
            return "Dealer"

    def play(self) -> None:
        '''Runs a round of the game.'''
        self.initial_deal()
        print("\n---YOUR TURN---")
        self.player.take_turn(self.deck)
        if not self.player.is_busted():
            print("\n---DEALER TURN---")
            print(f"Dealer reveals full hand: {self.dealer.show_hand()}")
            self.dealer.take_turn(self.deck)
        print(f"{self.determine_winner()} won!")