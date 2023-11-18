from turtle import Turtle, Screen


screen = Screen()
screen.bgcolor("black")

tim = Turtle()
tim.shape("turtle")
tim.color("bisque4")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
for side, color in enumerate(colors, 4):
    angle = 360 / side
    tim.color(color)
    for _ in range(side):
        tim.forward(100)
        tim.right(angle)

screen.exitonclick()
