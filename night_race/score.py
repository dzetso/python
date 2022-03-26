from turtle import Turtle
from block import BLOCKS_EACH_LEVEL
FONT = ("Courier", 12, "normal")

class Score():

    def __init__(self):
        self.levelboard = Turtle()
        self.levelboard.hideturtle()
        self.levelboard.goto(115, 230)
        self.levelboard.color("white")
        self.blockboard = Turtle()
        self.blockboard.hideturtle()
        self.blockboard.goto(115, 210)
        self.blockboard.color("white")
        self.level = 1
        self.blocks_passed = 0
        self.update_score()

    def reset_level(self):
        self.level = 1
        self.update_score()
    
    def level_up(self):
        self.level += 1
        self.update_score()
    
    def update_score(self):
        self.levelboard.clear()
        self.blockboard.clear()
        self.levelboard.write(f"Level: {self.level}", align="left", font=FONT)
        self.blockboard.write(f"{self.blocks_passed}/{BLOCKS_EACH_LEVEL}", align="left", font=FONT)


