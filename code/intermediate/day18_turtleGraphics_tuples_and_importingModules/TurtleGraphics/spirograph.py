from math import pi
from turtle import Turtle, Screen


screen = Screen()
screen.bgcolor("black")

tim = Turtle()
tim.speed(1000)
tim.color("bisque4")


for _ in range(360):
    tim.circle(100)
    tim.setheading(tim.heading() + pi)
    # tim.right(pi)
    

screen.exitonclick()
