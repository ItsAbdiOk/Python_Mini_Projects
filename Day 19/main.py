from turtle import Turtle, Screen, width
import random

screen = Screen()
is_race_on = False
screen.setup(width = 500,height = 500)
User_bet = screen.textinput(title ="Make your bet", prompt = "Which turtle will win?")
colours = ['red','blue','green','yellow','orange','purple']
    

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colours[turtle_index])
    tim.penup()
    tim.goto(-230,(-50 + 30 * turtle_index))

while is_race_on is False:
    tim.forward(random.randint(0,10))
    if  tim.pos() == (450, ):
        break
screen.exitonclick()