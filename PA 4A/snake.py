from turtle import Turtle

MOVE_DISTANCE = 20
FINISH_LINE_Y = 260
STARTING_POSITION = (0, -260)

class Snake(Turtle):
    def __init__(self):
        self.segments = []
        self.head = (0, -260)
        super().__init__()
        self.shape("circle")
        self.color("black", "#8ba832")
        self.penup()
        self.goto(0, -220)
        self.setheading(90)

    def create_starting_snake(self):
        for s in range(3):
            self.grow()

    def move(self, temp):
        new_temp = (self.xcor(), self.ycor())
        for i, s in enumerate(self.segments):
            new_temp = (s.xcor(), s.ycor())
            s.goto(temp)
            temp = new_temp

    def grow(self):
        segment = Snake()
        segment.color("#829c75")
        if len(self.segments) > 0:
            segment.goto((self.segments[-1].xcor(), self.segments[-1].ycor() - 20))
        else:
            segment.goto(self.xcor(), self.ycor() - 20)
        self.segments.append(segment)

    def up(self):
        if self.segments and self.segments[0].ycor() == self.ycor() + 20:
            return
        self.goto(self.xcor(), self.ycor() + 20)
        self.head = (self.xcor(), self.ycor() + 20)
        self.move((self.xcor(), self.ycor() - 20))

    def down(self):
        if self.segments and self.segments[0].ycor() == self.ycor() - 20:
            return
        self.goto(self.xcor(), self.ycor() - 20)
        self.head = (self.xcor(), self.ycor() - 20)
        self.move((self.xcor(), self.ycor() + 20))

    def right(self):
        if self.segments and self.segments[0].xcor() == self.xcor() + 20:
            return
        self.goto(self.xcor() + 20, self.ycor())
        self.head = (self.xcor() + 20, self.ycor())
        self.move((self.xcor() - 20, self.ycor()))

    def left(self):
        if self.segments and self.segments[0].xcor() == self.xcor() - 20:
            return
        self.goto(self.xcor() - 20, self.ycor())
        self.head = (self.xcor() - 20, self.ycor())
        self.move((self.xcor() + 20, self.ycor()))

    def check_snake_collision(self):
        for s in self.segments:
            if (s.xcor() == self.xcor() and s.ycor() == self.ycor()):
                return True
            return False