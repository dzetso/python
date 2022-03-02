from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=1400, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["silver", "orange", "yellow", "green", "blue", "black"]
y_coordinates = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="classic")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.speed("fastest")
    new_turtle.goto(x=-680, y=y_coordinates[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 680:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle is the winner")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner")

        if is_race_on and turtle.xcor() <= 680:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
