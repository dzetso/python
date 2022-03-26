from turtle import Turtle
AMMO_COUNT = 3

class Gun:

    def __init__(self):
        self.current_position = ()
        self.ammos = []
        self.current_ammo = -1
        for n in range(AMMO_COUNT):
            new_ammo = Turtle("arrow")
            new_ammo.setheading(90)
            new_ammo.penup()
            new_ammo.color("green")
            new_ammo.shapesize(stretch_len=0.2, stretch_wid=0.4)
            self.ammos.append(new_ammo)
        self.reset_position()
    
    def reset_position(self):
        for ammo in self.ammos:
            ammo.showturtle()
            ammo.goto(-120, -200 - 20 * self.ammos.index(ammo))
        self.current_ammo = -1
    
    def shoot(self):
        if self.current_ammo <= 1:
            self.current_ammo += 1
            self.ammos[self.current_ammo].goto(self.current_position)

