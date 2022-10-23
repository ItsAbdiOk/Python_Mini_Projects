import turtle
import pandas as pd
import time

#This sets up the screen
screen = turtle.Screen() # Creates a playground for turtles
screen.title("U.S. States Game") # Gives the window a title
image = "blank_states_img.gif" # Sets the background image
screen.addshape(image) # Adds the background image to the screen
turtle.shape(image) # Sets the background image


#Formatting the States.csv file
data = pd.read_csv("50_states.csv") # Reads the csv file
all_states = data.state.to_list() # Creates a list of all the states
Guessed_States = []  # Creates an empty list to store the guessed states


while Guessed_States != all_states: # While you haven't guessed all the states
    Answer_State = screen.textinput(title="Guess the State", prompt="What's another state's name?").title() # Asks for the user's input
    t = turtle.Turtle() # Creates a turtle
    t.hideturtle() # Hides the turtle
    if Answer_State == "Exit": # If the user types exit
        Missing_States = [state for state in all_states if state not in Guessed_States] # Creates a list of the missing states
        new_data = pd.DataFrame(Missing_States) # Creates a new dataframe
        new_data.to_csv("States_to_Learn.csv") # Creates a csv file with the missing states
        break # Breaks the loop
    if Answer_State in all_states: # If the user's input is in the list of states
        t.penup() # Lifts the pen
        state_data = data[data.state == Answer_State] # Creates a new dataframe with the state's data
        t.goto(int(state_data.x), int(state_data.y)) # Moves the turtle to the state's coordinates
        t.write(Answer_State) # Writes the state's name
        Guessed_States.append(Answer_State) # Adds the state to the list of guessed states
        time.sleep(1) # Waits 1 second
    else: # If the user's input is not in the list of states
        print("That's not a state") # Prints that it's not a state
    
if Guessed_States == all_states: # If you guessed all the states
    t.penup() # Lifts the pen
    t.goto(0,0) # Moves the turtle to the center
    t.write("You Win!") # Writes "You Win!"
    time.sleep(5) # Waits 5 seconds
    
screen.exitonclick() # Closes the screen when you click on it

# Code by @ItsAbdiOk