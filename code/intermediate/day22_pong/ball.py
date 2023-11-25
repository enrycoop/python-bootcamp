from shape import Shape


class Ball(Shape):
    def __init__(self):
        super().__init__(0, 0, "circle", "white")
        self.x_move = 1
        self.y_move = 1
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

