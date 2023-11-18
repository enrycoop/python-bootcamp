from turtle import Turtle, Screen


screen = Screen()
screen.bgcolor("black")

tim = Turtle()
tim.shape("turtle")
tim.color("bisque4")
for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen.exitonclick()
