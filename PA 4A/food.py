from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color("#a84832")
        self.penup()
        self.goto(random.randint(-330, 330), random.randint(-240, 240))

    def refresh(self) -> tuple:
        self.penup()
        position = self.random_position()
        self.goto(position)
        return position

    def random_position(self) -> tuple:
        x = random.randint(-330, 330)
        y = random.randint(-240, 240)
        return (x, y)