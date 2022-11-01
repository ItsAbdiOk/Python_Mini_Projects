from turtle import Turtle   # Import the Turtle class from the turtle module
 

class Paddle(Turtle): # Create a Paddle class that inherits from the Turtle class

    def __init__(self, position): # Create an __init__ method
        super().__init__() # Call the __init__ method of the parent class
        self.shape("square") # Set the shape of the turtle to a square
        self.color("white") # Set the color of the turtle to white
        self.shapesize(stretch_wid=5, stretch_len=1) # Set the width and length of the turtle to 5 and 1
        self.penup() # Lift the pen
        self.goto(position) # Move the turtle to the position
        
    def go_up(self): # Create a go_up method
        new_y = self.ycor() + 20 # Set the new y coordinate to the current y coordinate plus 20
        self.goto(self.xcor(), new_y) # Move the turtle to the current x coordinate and the new y coordinate
 
    def go_down(self): # Create a go_down method
        new_y = self.ycor() - 20 # Set the new y coordinate to the current y coordinate minus 20
        self.goto(self.xcor(), new_y) # Move the turtle to the current x coordinate and the new y coordinate