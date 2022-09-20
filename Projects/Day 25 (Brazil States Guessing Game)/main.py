import turtle
import pandas as pd
ALIGNMENT = "center"
FONT = ("Courier", 8, "bold")

# creating screen
screen = turtle.Screen()
screen.title("Brazil's States Game")
screen.tracer(0)

# adding background
image = "Brazil_Blank_Map.gif"
screen.addshape(image)
turtle.shape(image)
screen.update()

# importing csv with states and their location
df = pd.read_csv("brazil_states.csv", sep=";", encoding="UTF-8")
df = df.set_index('state')
df.index = df.index.str.lower()

correct_states = []
game_is_on = True
while game_is_on:
    screen.update()
    # getting users input
    user_input = screen.textinput(title=f"{len(correct_states)}/27 States", prompt="Write a state's name below:\nWrite "
                                                                                   "'Exit' to exit").lower().strip()
    # checking if state exists and hasn't already been guessed
    if (user_input in df.index) and (user_input not in correct_states):
        # creating state name turtle
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        # selecting state location
        x = df.loc[user_input, "x"]
        y = df.loc[user_input, "y"]
        state_name.goto(x, y)
        # writing state name
        state_name.write(f"{user_input.title()}", align=ALIGNMENT, font=FONT)
        # adding to correct states list
        correct_states.append(user_input)
    # exit loop
    elif user_input == 'exit':
        game_is_on = False
