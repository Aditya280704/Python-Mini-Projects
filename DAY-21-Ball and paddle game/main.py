# CREATE SCREEN
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800,height = 600)
screen.title("Pong Game")
# controls the animation
screen.tracer(0)

# Create the location as a tuple otherwise compiler takes it as 2 different values and shows error
# as paddle init takes 2 positional arguments but 3 were given
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with wall
    if ball.ycor()>270 or ball.ycor()<-270:
        # needs to bounce
        ball.bounce_y()
        
    # Detect collision with right paddle and left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # print("made contact")    
        ball.bounce_x()
        
    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset()  
        scoreboard.l_point() 
        
    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset()  
        scoreboard.r_point()  
    
    










screen.exitonclick()

