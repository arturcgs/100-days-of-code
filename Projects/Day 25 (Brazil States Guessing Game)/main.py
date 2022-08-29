import turtle
import pandas as pd
ALIGNMENT = "center"
FONT = ("Courier", 8, "bold")

# creating screen
screen = turtle.Screen()
screen.title("Brazil's States Game")
screen.tracer(0)

# adding brackground
image = "Brazil_Blank_Map.gif"
screen.addshape(image)
turtle.shape(image)
screen.update()
def get_mouse_coord(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_coord)




# importing csv with states and their location
df = pd.read_csv("brazil_states.csv", sep=";", encoding="UTF-8")
df = df.set_index('state')
df.index = df.index.str.lower()


while True:
    screen.update()
    # getting users input
    user_input = screen.textinput(title="wow", prompt="Write a state's name below:").lower().strip()
    # checking if state exists and hasn't already been guessed
    if user_input in df.index:
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












turtle.mainloop()
