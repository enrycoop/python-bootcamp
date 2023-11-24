from shape import Shape


class Ball(Shape):
    def __init__(self):
        super().__init__(0, 0, "circle", "white")
        self.setheading(45)
    
    def go_forward(self):
        self.forward(1)

    def set_heading(self, angle):
        self.setheading(angle)

