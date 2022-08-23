import turtle

import colorgram as cs
from turtle import Turtle, Screen
from random import randint
import random

tim = Turtle()
tim.shape("arrow")
tim.width(2)
tim.speed(5)


def Getting_Color():
    color_list = cs.extract("image.jpg", 30)
    color_palette = []
    for color_list in color_list:
        r = color_list.rgb.r
        g = color_list.rgb.g
        b = color_list.rgb.b
        new_color = (r, g, b)
        color_palette.append(new_color)
        return random.choice(color_palette)


def change_color():
    turtle.colormode(255)
    colours = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
    tim.pencolor(random.choice(colours))


def Move():
    for i in range(1,8):
        for i in range(1, 16):
            tim.penup()
            tim.forward(60)
            change_color()
            tim.dot(22)
        tim.forward(5)
        tim.right(90)
        tim.forward(60)
        tim.right(90)
        for i in range(1, 16):
            tim.penup()
            tim.forward(60)
            change_color()
            tim.dot(22)
        tim.left(90)
        tim.forward(60)
        tim.left(90)


screen = Screen()
TURTLE_SIZE = 20
tim.penup()

tim.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
Move()
screen.exitonclick()