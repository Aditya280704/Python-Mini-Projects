# car = CarBlueprint()
#car is object and carblueprint is class
#class has caps in the first letter of word...

import turtle

timmy = turtle.Turtle()
#timmy is object and Turtle is class

#OTHER WAY:-

from turtle import Turtle ,Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")#here we inserted turtle as a string so earlier the shape of turtle was
#a cursor and know the shape of cursor changed to turtle and same way we can change the colour of the turtle...

my_screen = Screen()
print(my_screen.canvheight) 
my_screen.exitonclick()# this is a function attached to an object 
#and so this is calledas Method..