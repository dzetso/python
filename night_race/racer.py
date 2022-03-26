from turtle import Turtle


class Racer(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("chartreuse")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=1.4)
        
    def reset_position(self):
        self.goto(0, -220)

    def left(self):
        self.backward(20)
    
    def right(self):
        self.forward(20)