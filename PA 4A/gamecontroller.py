from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Turtle, Screen

class GameController:
    def __init__(self, screen: Screen, snake: Snake, food: Food, scoreboard: Scoreboard, is_game_on: bool = True) -> None:
        self.screen = screen
        self.snake = snake
        self.food = food
        self.scoreboard = scoreboard
        self.is_game_on = is_game_on

    def setup_bindings(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")

    def run_game_loop(self):
        self.setup_bindings()
        self.snake.create_starting_snake()
        while self.is_game_on == True:
            self.screen.update()
            self.check_food_collision()
            self.check_wall_collision()
            lost = self.snake.check_snake_collision()
            if (lost):
                self.end_game()

    def check_food_collision(self) -> None:
        if self.snake.xcor() - self.food.xcor() in range(-20, 20) and self.snake.ycor() - self.food.ycor() in range(-20, 20):
            self.snake.grow()
            self.food.refresh()
            self.scoreboard.increase_score()
            self.scoreboard.update_scoreboard()

    def check_wall_collision(self) -> None:
        if self.snake.xcor() > 350 or self.snake.xcor() < -350 or self.snake.ycor() > 300 or self.snake.ycor() < -300:
            self.end_game()

    def end_game(self) -> None:
        self.scoreboard.game_over()
        self.is_game_on = False