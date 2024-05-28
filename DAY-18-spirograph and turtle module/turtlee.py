import turtle as t 
tim  = t.Turtle()
import random
colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue"]
# num_of_sides = 5 #for pentagon
def draw_Shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)
for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_Shape(shape_side_n)     