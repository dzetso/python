from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
with open("snake_game_day24/high_score.txt", mode="r") as file:
    content = file.read()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.get_high_score()
        self.update_scoreboard()

    def get_high_score(self):
        self.high_score = int(content)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.get_high_score()
        if self.score > self.high_score:
            with open("snake_game_day24/high_score.txt", mode="w") as file:
                file.write(str(self.score))
                self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
