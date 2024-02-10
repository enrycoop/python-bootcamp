"""
This is a simple script to create a turtle object.
See https://docs.python.org/3/library/turtle.html
"""


from turtle import Turtle, Screen


timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.fd(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

