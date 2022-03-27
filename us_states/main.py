from shutil import move
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "us_states/blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)

turtle.shape(image)

data = pandas.read_csv("us_states/50_states.csv")


game_is_on = True
correct = 0

states = data.state.to_list()

while game_is_on:
    answer_state = screen.textinput(title=f"{correct}/50 States Correct", prompt="What's the State? ").title()
    if answer_state in states:
        states.remove(answer_state)
        correct += 1
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(int(data[data["state"] == answer_state].x), int(data[data["state"] == answer_state].y))
        new_turtle.write(data[data["state"] == answer_state].state.item(), align="center", font=("Garamond", 7, "normal"))
    if correct == 50:
        game_is_on = False
        
turtle.mainloop()
