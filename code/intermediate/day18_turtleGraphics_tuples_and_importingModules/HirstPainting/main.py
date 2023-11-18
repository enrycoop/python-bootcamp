import turtle
import colorgram
import random

from turtle import Turtle, Screen

color_extracted = colorgram.extract('code/intermediate/day18_turtleGraphics_tuples_and_importingModules/HirstPainting/flumequine.jpg',
                                    30)
colors = []
for color in color_extracted:
    r = int(color.rgb.r)
    g = int(color.rgb.g)
    b = int(color.rgb.b)
    colors.append((r, g, b))


screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.speed(100)
tim.penup()

for i in range(-250, 250, 50):
    for j in range(-250, 240, 50):
        tim.setpos((j, i))
        tim.pendown()
        tim.pencolor(random.choice(colors))
        tim.dot(20)
        tim.penup()

tim.hideturtle()
screen.exitonclick()


# Extract 6 colors from an image.
