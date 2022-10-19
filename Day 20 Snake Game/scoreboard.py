# This Code Handle the score of the game
from turtle import Turtle

class ScoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 # Create a variable to store the score, and set it to 0
        self.color("white") # Set the color of the scoreboard to white
        self.hideturtle() # Hide the turtle(arrow) that draws the scoreboard
        self.penup() # Lift the pen so that the scoreboard doesn't draw 
        self.goto(0, 260) # Move the scoreboard to the top of the screen
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal")) # Write the score to the screen
    def increase_score(self):
        self.score += 1 # Increase the score by 1
        self.clear() # Clear the old scoreboard
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal")) # Write the new score to the screen
    def game_over(self):
        self.goto(0, 0)
        self.clear() # Clear the old scoreboard
        self.write(f"GAME OVER, YOUR SCORE WAS: {self.score}", align="center", font=("Arial", 24, "normal"))






        