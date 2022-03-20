import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.listen()
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        scoreboard.level_up()
        car_manager.reset_cars()
        car_manager.increase_speed()

    # detect collision with cars

    for car in car_manager.cars:
        if (car.ycor() - 20 <= player.ycor() <= car.ycor() + 15) and car.distance(player) <= 30:
            player.reset_position()
            scoreboard.loose()
            car_manager.loose()

screen.exitonclick()
