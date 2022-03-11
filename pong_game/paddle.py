from turtle import Turtle
SPEED = 20


class Paddle(Turtle):

    def __init__(self, coordinate):
        super().__init__()
        self.color("black")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(coordinate)
        self.color("white")

    def go_up(self):
        new_y = self.ycor() + SPEED
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - SPEED
        self.goto(self.xcor(), new_y)
