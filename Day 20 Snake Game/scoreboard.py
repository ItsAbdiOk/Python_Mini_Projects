# This Code Handle the score of the game
from turtle import Turtle

class ScoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 # Create a variable to store the score, and set it to 0
        with open("HighScoreStorage.txt") as file:
            self.high_score = int(file.read()) # Create a variable to store the high score, and set it to the high score in the file
        self.color("white") # Set the color of the scoreboard to white
        self.hideturtle() # Hide the turtle(arrow) that draws the scoreboard
        self.penup() # Lift the pen so that the scoreboard doesn't draw 
        self.goto(0, 260) # Move the scoreboard to the top of the screen
        self.write(f"Score: {self.score} High Score: {self.high_score}" , align="center", font=("Arial", 24, "normal") ) # Write the score to the screen
    def increase_score(self):
        self.score += 1 # Increase the score by 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , align="center", font=("Arial", 24, "normal") ) # Write the new score to the screen
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , align="center", font=("Arial", 24, "normal") ) # Write the new score to the screen
        with open("HighScoreStorage.txt", mode="w") as file:
            file.write(str(self.high_score))
    
    








        