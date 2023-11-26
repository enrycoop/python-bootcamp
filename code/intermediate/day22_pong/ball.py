from shape import Shape
INITIAL_SPEED = 0.008


class Ball(Shape):
    def __init__(self):
        super().__init__(0, 0, "circle", "white")
        self.x_move = 1
        self.y_move = 1
        self.move_speed = INITIAL_SPEED
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.increase_speed()

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = INITIAL_SPEED

    def increase_speed(self):
        self.move_speed *= 0.9
