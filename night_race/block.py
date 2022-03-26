from turtle import Turtle
BLOCKS_EACH_LEVEL = 40
X_POSITIONS_OF_BLOCKS = [100, 80, 60, 40, 20, 0, -20, -40, -60, -80, -100]
BLOCK_COLOR = ["red", "cyan", "blue", "yellow", "pink"]
import random


class Block():

    def __init__(self):
        self.blocks = []
        self.current_speed = 5
        self.create_blocks()

    def create_blocks(self):
        for n in range(BLOCKS_EACH_LEVEL):
            new_block = Turtle("square")
            new_block.penup()
            new_block.setheading(270)
            self.blocks.append(new_block)
        self.setting_positions()
    
    def setting_positions(self):
        for number in range(BLOCKS_EACH_LEVEL):
            block = self.blocks[number]
            x_position = random.choice(X_POSITIONS_OF_BLOCKS)
            y_position = 260 + 50 * number
            block.showturtle()
            block.color(random.choice(BLOCK_COLOR))
            block.goto(x_position, y_position)
    
    def move_blocks(self):
        for block in self.blocks:
            block.forward(self.current_speed)
    
    def increase_speed(self):
        self.current_speed += 5
    
    def reset_speed(self):
        self.current_speed = 5
