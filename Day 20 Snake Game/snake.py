from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
Move_Distance = 20
class Snake :
    
    def __init__(self):
        self.segments = [] # Create a list to store the segments of the snake
        self.position = (0, 0) # Create a variable to store the position of the snake
        for position in STARTING_POSITIONS: # Loop through the starting positions
            self.create_snake(position) # Create a snake segment at each position
        self.head = self.segments[0] # Set the head of the snake to the first segment of the snake


    def create_snake(self , position):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)


    def extend(self):
        self.create_snake(self.segments[-1].position())





    def move(self):
        for i in range(len(self.segments)-1, 0, -1): # This loop makes the body of the snake follow the head
            new_x = self.segments[i-1].xcor() # Get the x coordinate of the segment in front of the current segment
            new_y = self.segments[i-1].ycor() # Get the y coordinate of the segment in front of the current segment
            self.segments[i].goto(new_x, new_y) # Move the current segment to the position of the segment in front of it
        self.head.forward(Move_Distance) # Move the head of the snake forward
    def up(self):
        if self.head.heading() != 270: # If the snake is not moving down
            self.head.setheading(90) # Set the heading of the snake to up
    def down(self):
        if self.head.heading() != 90: # If the snake is not moving up
            self.head.setheading(270) # Set the heading of the snake to down
    def left(self):
        if self.head.heading() != 0: # If the snake is not moving right
            self.head.setheading(180) # Set the heading of the snake to left
    def right(self):
        if self.head.heading() != 180: # If the snake is not moving left
            self.head.setheading(0) # Set the heading of the snake to right