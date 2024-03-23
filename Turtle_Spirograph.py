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
directions = [0, 90, 180, 270]

timmy.pensize(15)
timmy.speed("fastest")


for _ in range(200):
    timmy.color(random_colour())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()