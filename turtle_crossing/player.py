<<<<<<< HEAD
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -590)
        self.color("black")
    
    def move(self):
        self.forward(MOVE_DISTANCE)
||||||| a8d9c84
=======
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    pass
>>>>>>> 40d7cfb20de8d160d5606a09f7b00b56904f59ea
