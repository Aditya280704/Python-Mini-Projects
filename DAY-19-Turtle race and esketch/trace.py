from turtle import Turtle,Screen
import random

is_race_on = False

screen = Screen()
screen.title("Turtle Race")
screen.setup(width = 500 , height = 400)

user_bet = screen.textinput(title="Make your bet " , prompt="Which turtle you think will win the race ?")
colors = ['red','blue','green','yellow','purple','pink']
y_pos = [-70,-40,-10,20,50,80]

all_turtles = []



for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(x = -230 , y= y_pos[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True
        
while is_race_on:    
    for turtle in all_turtles:
        rand_distance =  random.randint(0,10) 
        turtle.forward(rand_distance)
        if turtle.xcor()>230:
            winning_color = turtle.pencolor()
            is_race_on = False
            # this line below was showing error as i had not indented it inside above if loop..
            if winning_color == user_bet:
                print(f"You won!! The winning color turtle is {winning_color}")    
            else:
                print(f"You lost !! The winning color turtle was {winning_color} and you chose {user_bet}")    
            
        
    


screen.exitonclick()