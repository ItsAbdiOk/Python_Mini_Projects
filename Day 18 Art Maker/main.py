import turtle 
import colorgram as cs
from turtle import Turtle, Screen
from random import randint
import random

tim = Turtle()
tim.shape("arrow")
tim.width(2)
tim.speed(5)


def Getting_Color(): #Getting color from image
    color_list = cs.extract("image.jpg", 30) #30 is the number of colors
    color_palette = [] #Empty list
    for color_list in color_list: #Looping through the list
        r = color_list.rgb.r #Getting the red value
        g = color_list.rgb.g #Getting the green value
        b = color_list.rgb.b #Getting the blue value
        new_color = (r, g, b) #Creating a tuple
        color_palette.append(new_color) #Appending the tuple to the list
        return random.choice(color_palette) #Returning a random color from the list


def change_color(): #Changing the color
    turtle.colormode(255) #Setting the color mode to RGB
    colours = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
    tim.pencolor(random.choice(colours)) #Picking a random color from the list


def Move(): #Moving the turtle
    for i in range(1,8): #Looping through the range
        for i in range(1, 16): #Looping through the range
            tim.penup() #Lifting the pen
            tim.forward(60) #Moving the turtle forward
            change_color() #Changing the color
            tim.dot(22) #Drawing a dot
        tim.forward(5) #Moving the turtle forward
        tim.right(90) #Turning the turtle right
        tim.forward(60) #Moving the turtle forward
        tim.right(90) #Turning the turtle right
        for i in range(1, 16): #Looping through the range
            tim.penup() #Lifting the pen
            tim.forward(60) #Moving the turtle forward
            change_color() #Changing the color
            tim.dot(22) #Drawing a dot
        tim.left(90) #Turning the turtle left
        tim.forward(60) #Moving the turtle forward
        tim.left(90)    #Turning the turtle left


screen = Screen()
TURTLE_SIZE = 20
tim.penup()

tim.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
Move()
screen.exitonclick()