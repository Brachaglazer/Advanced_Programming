from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.snake_score = 0
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Player Score: {self.snake_score}",
            align="center",
            font=("Arial", 16, "bold"))

    def increase_score(self):
        self.snake_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.write(
            f"Game over! Great job! Player Score: {self.snake_score}",
            align="center",
            font=("Arial", 16, "bold"))