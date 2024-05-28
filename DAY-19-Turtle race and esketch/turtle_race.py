from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=400)  # all from screen in turtle module
user_bet = screen.textinput(title = "Make your Bet", prompt ="Which turtle will win the race? Enter a Colour : " )
colors = ['red','orange','yellow','green','blue','purple']

y_pos = [-70,-40,-10,20,50,80]
all_turtles = []




# tim.penup()
# tim.shape("turtle")
# tim.color(colors[1])
# tim.goto(x = -230,y = -100)

#ONE WAY IS TO CREATE DIFFERENT TURTLE OBJECT OTHER WAY IS TO USE FOR LOOP:-

# tom = Turtle()
# tom.penup()
# tom.shape("turtle")
# tom.color(colors[0])
# tom.goto(x = -230 , y = -60)

# tip = Turtle()
# tip.penup()
# tip.shape("turtle")
# tip.color(colors[2])
# tip.goto(x = -230 , y = -20)
# screen.exitonclick()


# USING FOR LOOP:-
for turtle_index in range(0,6):
    new_turtles = Turtle()
    new_turtles.shape("turtle")
    new_turtles.penup()
    new_turtles.color(colors[turtle_index])
    new_turtles.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtles)

if user_bet:
    is_race_on = True
    # CHECKS IF USER ENTERED A COLOUR AND THEN STARTS THE LOOP OTHERWISE
    #LOOP WILL BE STARTED BEFORE USER IS ENTERING THE COLOUR..


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False    
            if winning_color == user_bet:
                print(f"You have won ! The {winning_color} turtle is the winner..")
            else:
                print(f"You lost ! The winning turtle is {winning_color}")    
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)  

screen.exitonclick()    

