from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

ball_speed = 0.01
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

# MID DASHED LINE
place_y = 325
for _ in range(15):
    place_y -= 40
    place = (0, place_y)
    t = Turtle()
    t.shape("square")
    t.shapesize(stretch_wid=1, stretch_len=0.5)
    t.color("white")
    t.pu()
    t.goto(place)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    right_paddle = [int(r_paddle.ycor()) - 50, int(r_paddle.ycor()) + 50]
    left_paddle = [int(l_paddle.ycor()) - 50, int(l_paddle.ycor()) + 50]

    # Detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Detect collision with paddles
    # if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    #     if -350 < ball.xcor() < 350:
    #         ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # My version
    if ball.xcor() == 330:
        if ball.ycor() in range(right_paddle[0], right_paddle[1]):
            ball.bounce_x()
    elif ball.xcor() == -330:
        if ball.ycor() in range(left_paddle[0], left_paddle[1]):
            ball.bounce_x()
screen.exitonclick()
