from blackJackGame import BlackJackGame

if __name__ == "__main__":
    print("Welcome to Blackjack!")
    name = input("Enter your name: ")
    game = BlackJackGame(name)
    game.play()