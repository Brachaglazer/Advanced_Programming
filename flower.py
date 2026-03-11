
import random
from turtle import *
import math
screen = Screen()
screen.bgcolor("white")
hot_palette = [
"hotpink","deeppink","pink",
"#ff69b4","#ff1493","#ff5c8a","#ff4d6d",
"#ff006e","#ff0a54","#ff477e","#ff7096",
"coral","tomato","orangered",
"#ff7b00","#ff8500","#ff9100","#ff9e00",
"#ff5400","#ff6d00","#ff3c38",
"red","crimson",
"#ff1744","#ff1744","#ff355e",
"magenta","fuchsia",
"#ff00ff","#ff00cc","#ff00aa","#ff0099",
"orchid","mediumorchid","darkorchid",
"#d000ff","#c77dff","#9d4edd","#8338ec",
"violet","blueviolet",
"gold","yellow",
"#ffbe0b","#ffd60a","#ffea00",
"#fb5607","#ff006e","#8338ec","#3a86ff"
]
green_palette = ["springgreen","mediumspringgreen","lime","limegreen",
"lawngreen","chartreuse","greenyellow","palegreen",
"lightgreen","mediumseagreen","seagreen","yellowgreen",
"darkseagreen","lightseagreen","#00ff7f","#39ff14",
"#7fff00","#66ff66","#99ff66","#66ff99","#33ff99","#00ff99"]

class Flower(Turtle):
    def __init__(self,
                 x:int,
                 y:int,
                 petals:int,
                 size:int,
                 petal_color:str,
                 stamen_color:str,
                 stem_color:str = "green"
                 ):

        super().__init__()
        self.x = x
        self.y = y
        self.petals = petals
        self.size = size
        self.petal_color = petal_color
        self.stamen_color = stamen_color
        self.stem_color = stem_color

        self.hideturtle()
        self.speed(0)
        self.penup()

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
        self._draw_all_petals(shape)
        self._draw_stamen()
        self._draw_stem()

    def draw_bud(self):
        old_x, old_y = self.x, self.y
        self.x += 100 * random.choice([-1,1])
        self.y += 100 * random.choice([1, -1])
        self._draw_stamen()
        self.draw_stem()
        self.x, self.y = old_x, old_y

for _ in range (20):
    # create one flower
    f = Flower(
        random.randint(-300, 300),
        random.randint(-300, 300),
        random.randint(6, 12),
        random.randint(5, 30),
        random.choice(hot_palette),
        random.choice(hot_palette),
        random.choice(green_palette)
        )
    f.draw_one_flower(random.randint(30, 90))
    f.draw_bud()