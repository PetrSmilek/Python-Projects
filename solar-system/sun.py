from turtle import Turtle


class Sun(Turtle):

    def __init__(self):
        super(Sun, self).__init__()
        self.shape("circle")
        self.shapesize(2.8, 2.8)
        self.color("yellow")
