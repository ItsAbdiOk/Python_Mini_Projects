from turtle import Turtle, Screen, color
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the raze? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
for i in range(0, 6):
    New_Turtle = Turtle(shape="turtle")
    New_Turtle.color(colors[i])
    New_Turtle.penup()
    New_Turtle.goto(x=-230, y=-100 + i * 40)
    all_turtles.append(New_Turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            Winning_Color = turtle.pencolor()
            if Winning_Color == user_bet:
                print(f"You've won! The {Winning_Color} turtle is the winner!")
            else:
                print(f"You've lost! The {Winning_Color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()