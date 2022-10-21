from turtle import Turtle  # Import the Turtle class from the turtle module


class Ball(Turtle): # Create a Ball class that inherits from the Turtle class
 
    def __init__(self):
        super().__init__() # Call the __init__ method of the parent class
        self.shape("square") # Set the shape of the turtle to a square
        self.color("white") # Set the color of the turtle to white
        self.penup() # Lift the pen
        self.x_move = 10 # Set the x move to 10
        self.y_move = 10 # Set the y move to 10
        self.move_speed = 0.01 # Set the move speed to 0.01

    def move(self): # Create a move method
        new_x = self.xcor() + self.x_move # Set the new x coordinate to the current x coordinate plus the x move
        new_y = self.ycor() + self.y_move # Set the new y coordinate to the current y coordinate plus the y move
        self.goto(new_x, new_y) # Move the turtle to the new x and y coordinates

    def bounce_y(self): # Create a bounce_y method
        self.y_move *= -1 # Set the y move to the opposite of the current y move

    def bounce_x(self): # Create a bounce_x method
        self.x_move *= -1 # Set the x move to the opposite of the current x move
        self.move_speed *= 0.9 # Set the move speed to 90% of the current move speed

    def reset_position(self): # Create a reset_position method
        self.goto(0, 0) # Move the turtle to the center of the screen
        self.move_speed = 0.1 # Set the move speed to 0.1
        self.bounce_x() # Call the bounce_x method of the ball object