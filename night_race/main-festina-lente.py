from turtle import Screen
from racer import Racer
from road import Road
from block import Block, BLOCKS_EACH_LEVEL
from score import Score
from gun import Gun
import time

screen = Screen()
screen.setup(width=300, height=500)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
road = Road()
block = Block()
racer = Racer()
score = Score()
gun = Gun()
racer.reset_position()
screen.onkeypress(racer.left, "Left")
screen.onkeypress(racer.right, "Right")
screen.onkey(gun.shoot, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.06)
    block.move_blocks()
    screen.update()
    score.update_score()
    if gun.current_ammo != -1:
        if gun.current_ammo == 0:
            gun.ammos[gun.current_ammo].forward(6)
        elif gun.current_ammo == 1:
            gun.ammos[gun.current_ammo].forward(6)
            gun.ammos[gun.current_ammo - 1].forward(6)
        else:
            gun.ammos[gun.current_ammo].forward(6)
            gun.ammos[gun.current_ammo - 1].forward(6)
            gun.ammos[gun.current_ammo - 2].forward(6)
    gun.current_position = (racer.xcor(), racer.ycor() + 13)
    # player out of the road

    if racer.xcor() > 100 or racer.xcor() < -100:
        game_is_on = False 

    # player hit the block
    for a_block in block.blocks:
        if a_block.distance(racer) < 15 and a_block.isvisible():
            racer.reset_position()
            block.reset_speed()
            block.setting_positions()
            score.reset_level()
            gun.reset_position()
        for ammo in gun.ammos:
            if a_block.distance(ammo) <= 10 and ammo.isvisible() and a_block.isvisible():
                a_block.hideturtle()
                ammo.hideturtle()

    # check how many blocks passed
    score.blocks_passed = 0
    for a_block in block.blocks:
        if a_block.ycor() < -240:
            score.blocks_passed += 1
    score.update_score()

    # player levels up
    if block.blocks[BLOCKS_EACH_LEVEL - 1].ycor() < -240:
        block.increase_speed()
        block.setting_positions()
        score.level_up()
        gun.reset_position()

screen.exitonclick()
