import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# Add data to List:-
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states guess correct. ",
                                    prompt="Whats another state name?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
# If answer state is one of the 50states
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Name of state
        state_data = data[data.state == answer_state]
        # Once state is guessed tap into its x and y coordinate:-
        t.goto(int(state_data.x), int(state_data.y))
        guessed_state.append(answer_state)
        # Below line causes junk written on map alongside state name
        # t.write(state_data.state)
        # So we can simplify by
        t.write(answer_state)

# Print list of state not guessed by user when we exit the code

screen.exitonclick()
