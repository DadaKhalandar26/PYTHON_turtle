import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


def random_colour():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    RGB_Colour = (red, green, blue)
    return RGB_Colour


timmy = Turtle()
timmy.shape("turtle")

directions = [0, 90, 180, 270]

timmy.pensize(15)
timmy.speed("fastest")


for _ in range(200):
    timmy.color(random_colour())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()

