from turtle import Turtle,Screen
import random
tim = Turtle()
colors = ['red','green','blue','purple','yellow']

def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(40)
        tim.right(angle)    

for num_of_sides in range(3,10):
    tim.color(random.choice(colors))
    draw_shape(num_of_sides)
    
screen =  Screen()
screen.exitonclick()    