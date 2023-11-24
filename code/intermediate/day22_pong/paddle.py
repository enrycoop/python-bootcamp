from shape import Shape


class Paddle(Shape):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos, "square", "white")
        self.shapesize(stretch_len=5)
        self.setheading(90)
