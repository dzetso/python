<<<<<<< HEAD
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level #{self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def loose(self):
        self.level = 1
        self.update_scoreboard()
||||||| a8d9c84
=======
FONT = ("Courier", 24, "normal")


class Scoreboard:
    pass
>>>>>>> 40d7cfb20de8d160d5606a09f7b00b56904f59ea
