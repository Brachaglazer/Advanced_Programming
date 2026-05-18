class Card:
    def __init__(self, suit:str, rank:str, value:int) -> None:
        '''Creates one card object containing the necessary information needed to use the card'''
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"