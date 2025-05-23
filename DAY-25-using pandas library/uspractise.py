# 1 extract data from csv file
# make title box for screen
# guess country if correct then place it on map coordinates guess should be title case
# typing exit should end the program and make a new csv file for missed countries

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)} states correct",
                                    prompt="Make another guess").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("practise.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)


screen.exitonclick()