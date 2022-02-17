# # from turtle import *
# # import turtle
# import turtle as t
# import heroes
# for x in range(10):
#     print(heroes.gen())
#
# tim = t.Turtle()
# tim.shape("turtle")
# tim.color("red")
# # tim.penup()
# # tim.forward(100)
# # tim.right(90)
# # tim.pendown()
# # tim.forward(100)
# # for x in range(0, 3):
# #     tim.right(90)
# #     tim.forward(200)
# # tim.right(90)
# # tim.forward(100)
#
# # screen = t.Screen()
# # screen.exitonclick()

import turtle as t
import random
tim = t.Turtle()
screen = t.Screen()

# directions = [0, 90, 180, 270]
# tim.pensize(10)
tim.speed(45)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def draw_spirograph(quantity):
    for x in range(quantity):
        # screen.bgcolor(random_color())
        tim.color(random_color())
        tim.circle(100)
        tim.left(360 / quantity)


draw_spirograph(90)

# for x in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

screen.exitonclick()

# tim.penup()
# tim.left(90)
# tim.forward(300)
# tim.right(90)
# tim.pendown()
#
#
# def draw_shape(shape_number):
#     for x in range(shape_number):
#         tim.forward(100)
#         tim.right(360 / shape_number)
#
#
# for _ in range(3, 10):
#     tim.color(random.choice(colors))
#     draw_shape(_)

# draw_shape(360)


