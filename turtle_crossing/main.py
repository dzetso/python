<<<<<<< HEAD
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.move()
||||||| a8d9c84
=======
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
>>>>>>> 40d7cfb20de8d160d5606a09f7b00b56904f59ea
