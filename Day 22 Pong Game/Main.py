from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()   # Create a screen object
screen.bgcolor("black") # Set the background color
screen.setup(width=800, height=600) # Set the screen size
screen.title("Pong")   # Set the title of the screen
# Paddle setup
r_paddle = Paddle((350, 0)) # Create a paddle object
l_paddle = Paddle((-350, 0)) # Create a paddle object
ball = Ball() # Create a ball object
scoreboard = Scoreboard() # Create a scoreboard object
# Movement setup
screen.listen()
screen.onkey(r_paddle.go_up, "Up")  # When the up arrow key is pressed, call the go_up method of the paddle object
screen.onkey(r_paddle.go_down, "Down") # When the down arrow key is pressed, call the go_down method of the paddle object
screen.onkey(l_paddle.go_up, "w") # When the w key is pressed, call the go_up method of the paddle object
screen.onkey(l_paddle.go_down, "s") # When the s key is pressed, call the go_down method of the paddle object
# Game setup
game_is_on = True # Set the game_is_on variable to True
while game_is_on: # While the game_is_on variable is True
    screen.update() # Update the screen
    ball.move() # Call the move method of the ball object

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280: # If the y coordinate of the ball is greater than 280 or less than -280
        ball.bounce_y() # Call the bounce_y method of the ball object

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320: # If the distance between the ball and the right paddle is less than 50 and the x coordinate of the ball is greater than 320 or the distance between the ball and the left paddle is less than 50 and the x coordinate of the ball is less than -320
        ball.bounce_x() # Call the bounce_x method of the ball object

    #Detect R paddle misses
    if ball.xcor() > 380: # If the x coordinate of the ball is greater than 380
        ball.reset_position() # Call the reset_position method of the ball object
        scoreboard.l_point() # Call the l_point method of the scoreboard object

    #Detect L paddle misses:
    if ball.xcor() < -380: # If the x coordinate of the ball is less than -380
        ball.reset_position() # Call the reset_position method of the ball object
        scoreboard.r_point() # Call the r_point method of the scoreboard object

screen.exitonclick() # When the screen is clicked, exit the screen