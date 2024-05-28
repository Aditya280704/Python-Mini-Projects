import turtle as t 
tim  = t.Turtle()
import random
colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue"]
directions = [0,90,180,270]
tim.pensize(15)#for making lines thicker 
tim.speed("fast")
for _ in range(200):
    tim.color(random.choice(colors) )
    tim.forward(30)
    tim.setheading(random.choice(directions))


