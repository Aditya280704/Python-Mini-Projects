from turtle import Turtle,Screen

tim = Turtle()

tim.shape("turtle") 
tim.color("red")
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)

#or

for _ in range(4):
    tim.forward(100)
    tim.right(90)
    
#drawing dashed line
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()





screen = Screen()
screen.exitonclick() 