import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us_states_tutorial/blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

data = pandas.read_csv("us_states_tutorial/50_states.csv")
all_states = data.state.to_list()
guessed_states = []
guessed_states_indexes = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name: ").title()
    # if answer_state is one of the states in all the states of the 50_states.csv
    if answer_state == "Exit":
        not_guessed_states = data.drop(guessed_states_indexes)
        not_guessed_states.to_csv("us_states_tutorial/states_to_learn.csv")
        break
    if answer_state in all_states:
        all_states.remove(answer_state)
        guessed_states.append(answer_state)
        # if they got it right:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        
        # adding index of guessed states
        guessed_states_indexes.append(state_data.index.item())
