from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle") # Set the shape of the food to a circle
        self.penup() # Lift the pen so that the food doesn't draw
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # Set the size of the food
        self.color("blue") # Set the color of the food to blue
        self.speed("fastest") # Set the speed of the food to the fastest
        self.refresh() # Refresh the food

    def refresh(self):
        random_x = random.randint(-280, 280) # Get a random x coordinate
        random_y = random.randint(-280, 280) # Get a random y coordinate
        self.goto(random_x, random_y) # Move the food to the random coordinates
