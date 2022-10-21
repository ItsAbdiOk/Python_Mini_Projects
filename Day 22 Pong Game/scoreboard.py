from turtle import Turtle   # Import the Turtle class from the turtle module


class Scoreboard(Turtle):  # Create a Scoreboard class that inherits from the Turtle class
 
    def __init__(self): 
        super().__init__() # Call the __init__ method of the parent class
        self.color("white") # Set the color of the turtle to white
        self.penup() # Lift the pen
        self.hideturtle() # Hide the turtle 
        self.l_score = 0 # Set the left score to 0
        self.r_score = 0 # Set the right score to 0
        self.update_scoreboard() # Call the update_scoreboard method of the scoreboard object

    def update_scoreboard(self): # Create an update_scoreboard method
        self.clear() # Clear the scoreboard
        self.goto(-100, 200) # Move the turtle to the left side of the screen
        self.write(self.l_score, align="center", font=("Courier", 80, "normal")) # Write the left score
        self.goto(100, 200) # Move the turtle to the right side of the screen
        self.write(self.r_score, align="center", font=("Courier", 80, "normal")) # Write the right score

    def l_point(self): # Create a l_point method
        self.l_score += 1  # Add 1 to the left score
        self.update_scoreboard() # Call the update_scoreboard method of the scoreboard object

    def r_point(self): # Create a r_point method
        self.r_score += 1 # Add 1 to the right score
        self.update_scoreboard() # Call the update_scoreboard method of the scoreboard object