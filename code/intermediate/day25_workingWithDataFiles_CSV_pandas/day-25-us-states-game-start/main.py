import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.iloc[0], state_data.y.iloc[0])
        t.write(state_data.state.item())
        guessed_states.append(state_data.state.item())
remaining_states = []
for state in all_states:
    if state not in guessed_states:
        remaining_states.append(state)

for state in remaining_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.speed("fastest")
    t.penup()
    t.color("red")
    state_data = data[data.state == state]
    t.goto(state_data.x.iloc[0], state_data.y.iloc[0])
    t.write(state_data.state.item())
    guessed_states.append(state_data.state.item())
data[data.state.isin(remaining_states)].to_csv("remaining_states.csv")

screen.exitonclick()

