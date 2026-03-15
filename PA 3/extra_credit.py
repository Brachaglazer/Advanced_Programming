from turtle import *
import random

screen = Screen()
screen.bgcolor("white")
class Flower(Turtle):
    def __init__(self,
                 name:str,
                 petals:int,
                 petal_color:str,
                 height:int,
                 x: int,
                 y: int,
                 size: int,
                 stamen_color: str,
                 stem_color: str = "green"
                 ):
        super().__init__()
        self.name = name
        self.petals = petals
        self.petal_color = petal_color
        self.height = height
        self.x = x
        self.y = y
        self.size = size
        self.stamen_color = stamen_color
        self.stem_color = stem_color

        self.hideturtle()
        self.speed(0)
        self.penup()

    def describe(self):
        print(f'{self.name} is {self.color}, has {self.petals} petals, and is {self.height} cm tall.')

    def grow(self):
        self.height += 2

    def _draw_one_petal(self, shape:int):
        self.begin_fill()
        self.color(self.petal_color)
        self.pensize(20)

        for _ in range(2):
            self.circle(self.size, shape)
            self.end_fill()

    def _draw_all_pedals(self, shape:int):
        for _ in range(self.petals):
            self.forward(self.size)
            self.pendown()
            self._draw_one_petal(shape)
            self.penup()
            self.goto(self.x, self.y)
            self.left(360 / self.petals)

    def _draw_stamen(self):
        self.color(self.stamen_color)
        self.goto(self.x, self.y-self.size//5)
        self.dot(self.size)

    def _draw_stem(self):
        self.penup()
        self.goto(self.x, self.y-self.size)
        self.color(self.stem_color)
        self.setheading(270)
        self.pensize(max(1, 15-self.petals))
        self.pendown()
        self.forward(150)
        self.penup()
        print("flower complete")

    def draw_one_flower(self, shape:int=60):
        self.goto(self.x, self.y)
        self.heading()
        self._draw_all_pedals(shape)
        self._draw_stamen()
        self._draw_stem()

    def draw_bud(self):
        old_x, old_y = self.x, self.y
        self.x += 100 * random.choice([-1,1])
        self.y += 100 * random.choice([1, -1])
        self._draw_stamen()
        self._draw_stem()
        self.x, self.y = old_x, old_y

flower_one = Flower("rose",
                    5,
                    "red",
                    10,
                    random.randint(-300, 300),
                    random.randint(-300, 300),
                    random.randint(5, 30),
                    "yellow")
flower_two = Flower("tulip",
                    7,
                    "blue",
                    15,
                    random.randint(-300, 300),
                    random.randint(-300, 300),
                    random.randint(5, 30),
                    "yellow")
flower_three = Flower("daizy",
                      3,
                      "yellow",
                      7,
                      random.randint(-300, 300),
                      random.randint(-300, 300),
                      random.randint(5, 30),
                      "pink")
flower_four = Flower("lily",
                     8,
                     "orange",
                     17,
                     random.randint(-300, 300),
                     random.randint(-300, 300),
                     random.randint(5, 30),
                     "blue")
garden = [flower_one, flower_two, flower_three, flower_four]

for flower in garden:
    flower.describe()
    flower.grow()
    print("growing...")
    flower.describe()
    flower.draw_one_flower(random.randint(30, 90))
    flower.draw_bud()

