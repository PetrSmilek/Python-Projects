import time
import turtle
from turtle import Screen
from sun import Sun
from planets import Planet

screen = Screen()
screen.setup(width=800, height=800)
screen.title("Solar System")
screen.bgcolor("azure")

screen.tracer(0)

sun = Sun()

mercury = Planet(dimension=0.4)
venus = Planet(dimension=0.9)
earth = Planet(dimension=1)
mars = Planet(dimension=0.5)

mercury.position(x=80, y=0, heading=90)
venus.position(x=-150, y=0, heading=270)
earth.position(x=0, y=220, heading=180)
mars.position(x=0, y=-300, heading=0)

mercury.color("dimgrey")
venus.color("tan")
earth.color("deepskyblue")
mars.color("lightsalmon")

is_on = True

while is_on:
    time.sleep(0.75)

    mercury.orbit(distance=80, momentum=20)
    venus.orbit(distance=150, momentum=12)
    earth.orbit(distance=220, momentum=10)
    mars.orbit(distance=320, momentum=8)

    screen.update()


screen.exitonclick()
