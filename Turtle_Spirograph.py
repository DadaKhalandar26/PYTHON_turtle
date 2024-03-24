import random
from turtle import Turtle, Screen


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


def random_colour():
    return random.choice(colors)


timmy = Turtle()
timmy.shape("turtle")

colors = ["#0000FF", "#00FFFF", "#EEE8AA", "#FFA500", "#BA55D3",
          "#4B0082", "#008000", "#FFFF00", "#DC143C", "#556B2F"]

timmy.speed("fastest")
timmy.penup()
timmy.setposition(x=100, y=100)
timmy.pendown()
sides = 3
for _ in range(10):
    timmy.color(random_colour())
    draw_shape(sides)
    sides += 1


screen = Screen()
screen.exitonclick()
