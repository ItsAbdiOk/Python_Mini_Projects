from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()# Create a screen
screen.bgcolor("black") # Set the background color
screen.title("My Snake Game") # Set the title of the screen
screen.setup(width=600, height=600) # Set the size of the screen
screen.tracer(0) # IDK what this does, but it's important for the graphics 

snake = Snake() # Create a snake
food = Food() # Create food
scoreBoard = ScoreBoard() # Create a scoreboard

screen.listen() # Listen for key presses
screen.onkey(snake.up, "Up") # When the up arrow key is pressed, call the up method of the snake
screen.onkey(snake.down, "Down") # When the down arrow key is pressed, call the down method of the snake
screen.onkey(snake.left, "Left") # When the left arrow key is pressed, call the left method of the snake
screen.onkey(snake.right, "Right") # When the right arrow key is pressed, call the right method of the snake


game_is_on = True # Create a boolean to check if the game is on
while game_is_on: # While the game is on
    screen.update() # Update the screen
    time.sleep(0.1) # Delay the screen
    snake.move() # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15: # If the distance between the head of the snake and the food is less than 15
        food.refresh() # Refresh the food
        snake.extend() # Extend the snake
        scoreBoard.increase_score() # Increase the score
    
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280: # If the head of the snake is outside the screen
        game_is_on = False # Set the game_is_on variable to false
        scoreBoard.game_over() # Call the game_over method of the scoreboard

    # Detect collision with tail
    for segment in snake.segments[1:]: # Loop through the segments of the snake
        if snake.head.distance(segment) < 10: # If the distance between the head of the snake and a segment of the snake is less than 10
            game_is_on = False # Set the game_is_on variable to false
            scoreBoard.game_over() # Call the game_over method of the scoreboard
            










screen.exitonclick() # Exit the screen when clicked