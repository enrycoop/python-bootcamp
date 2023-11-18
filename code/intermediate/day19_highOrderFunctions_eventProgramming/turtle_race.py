import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet",
                            prompt="Wich turtle will win the race? enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y = -100
for color in colors:
    t = Turtle(shape="turtle")
    t.penup()
    t.color(color)
    t.goto(x=-250, y=y)
    turtles.append(t)
    y += 50

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is winner!")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
