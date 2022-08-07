from turtle import Turtle


class Planet(Turtle):

    def __init__(self, dimension):
        super(Planet, self).__init__()
        self.shape("circle")
        self.shapesize(dimension * 1, dimension * 1)

    def position(self, x, y, heading):
        self.penup()
        self.goto(x, y)
        self.pendown()
        self.setheading(heading)

    def orbit(self, distance, momentum):
        self.circle(distance, 1 * momentum)




