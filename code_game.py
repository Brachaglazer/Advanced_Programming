import random


class Code:
    '''
    The code class handles creating and retrieving the code used for each game.
    '''
    def __init__(self, value: str):
        self.value = value  # the value of the 4 digit randomly generated code

    def generate_code(self):
        '''This method creates a randomly generated 4 digit code'''
        code = ""  # the randomly generated 4 digit string
        for r in range(4):
            code += str(random.randint(0, 9))
            self.value = code

    def get_code(self):
        '''This method returns the value of a given code object'''
        return self.value


class Evaluator:
    '''
    The evaluator class is responsible for comparing the users guess to the secret code.
    '''
    def evaluate(self, secret, guess):
        '''
        This method compares the secret code given to the guess given.
        The amount and details of the exact and partial matches are returned.
        '''
        partial = (0,0)  # the amount of partial matched per guess and their digits
        exact = self.count_exact(secret, guess)  # the amount of exact matched per guess and their digits
        if exact[0] < 4:
            partial = self.count_partial(secret, guess)
        return exact, partial


    def count_exact(self, secret, guess):
        '''
        Counts the amount of exact matches (same digit in same place) between the guess and secret code given.
        Returns the amount and the specific matched digits.
        '''
        num_exact = 0  # number of exact matches per guess
        exact_dig = []  # values of exact matched per guess
        for index, digit in enumerate(secret):
            if guess[index] == digit:
                num_exact += 1
                exact_dig.append(digit)
        return num_exact, exact_dig


    def count_partial(self, secret, guess):
        '''
        Counts the amount of partial matches (same digit, wrong place) between the guess and secret code given.
        Returns the amount and the specific matched digits.
        '''
        num_partial = 0  # number of partial matches per guess
        partial_dig = []  # values of partial matches per guess
        for index, digit in enumerate(secret):
            if digit in guess:
                if guess[index] != digit:
                    num_partial += 1
                    partial_dig.append(digit)
        return num_partial, partial_dig

class Player:
    '''
    The Player class is responsible for keeping track of the users guesses and attempts.
    '''
    def __init__(self, guesses: list, attempts_used: int):
        self.guesses = guesses  # all guesses of user per game
        self.attempts_used = attempts_used  # total amount of users attempts per game

    def store_guess(self, guess):
        '''Stores users guess and increases users attempts count each time the user guesses the code'''
        self.guesses.append(guess)
        self.make_guess()
    def make_guess(self):
        '''Increases a specific users amount of attempts'''
        self.attempts_used += 1
    def get_attempts_used(self):
        '''Returns the amount of attempts a user has attempted to guess the secret code'''
        return self.attempts_used

class Game:
    '''
    The Game class is responsible for carrying out the steps of the game.
    '''
    def __init__(self,
        secret_code: Code,
        player: Player,
        evaluator: Evaluator,
        max_attempts: int):

        self.secret_code = secret_code  # code object containing a 4 digit string value
        self.player = player  # player object containing users guesses and amount of attempts
        self.evaluator = evaluator  # evaluator object used to compare the users guess to the secret code
        self.max_attempts = max_attempts  # the number of attempts allowed per game

    def play(self):
        '''
        Prompts the user to guess the secret code as long as the user has not exhausted his attempts.
        '''
        won = False  # boolean expressing whether the user has guessed the secret code or not
        while self.player.attempts_used < self.max_attempts and won == False:
            print()
            print(f"{self.player.attempts_used} / {self.max_attempts} attempts used")
            guess = str(input("Guess the 4 digit code: "))  # the user input guess
            if (len(guess) != 4) or (guess.isdigit() == False):
                print("Guess must be exactly 4 digits.")
                continue
            won = self.process_turn(guess)
        if won == False:
            print("Attempts exhausted!")

    def process_turn(self, guess):
        '''Processes each turn by evaluating the guess of the user.
        Returns a boolean determining whether the user has won or not.
        '''
        self.player.store_guess(guess)
        check = self.evaluator.evaluate(self.secret_code.get_code(), guess)
        return self.check_win(check)

    def check_win(self, evaluator: Evaluator):
        '''Determines whether the user has won based on the amount of exact matches returned by the evaluator.'''
        if evaluator[0][0] == 4:
            print("You won!")
            return True
        else:
            self.check_loss(evaluator)
            return False

    def check_loss(self, evaluator: Evaluator):
        '''Prints the status of the users guess'''
        print(f"Exact matches: {evaluator[0][0]} {evaluator[0][1]}")
        if evaluator[1][0] > 0:
            print(f"Partial matches: {evaluator[1][0]} {evaluator[1][1]}")
        else:
            print(f"Partial matches: {0}")

if __name__ == "__main__":
    player = Player([], 0)

    code_obj = Code("")
    code_obj.generate_code()

    evaluator = Evaluator()

    game = Game(code_obj, player, evaluator, 8)

    game.play()
