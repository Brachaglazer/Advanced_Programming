from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
from gamecontroller import GameController

screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor("white")
screen.title("Snake Eater")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Scoreboard()
snake_game = GameController(screen, snake, food, scoreboard)
snake_game.run_game_loop()
screen.exitonclick()