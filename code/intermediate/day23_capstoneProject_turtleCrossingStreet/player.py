from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.seth(90)
        self.goto(STARTING_POSITION)
        
    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)

