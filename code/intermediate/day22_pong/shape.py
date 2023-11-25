from turtle import Turtle


class Shape(Turtle):
    def __init__(self, x_pos, y_pos, shape, color="white"):
        super().__init__(shape=shape)
        self.speed("fastest")
        self.penup()
        self.color(color)
        self.goto(x_pos, y_pos)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def go_left(self):
        self.goto(self.xcor() - 20, self.ycor())

    def go_right(self):
        self.goto(self.xcor() + 20, self.ycor())

