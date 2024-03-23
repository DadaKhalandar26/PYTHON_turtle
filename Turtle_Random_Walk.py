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
timmy.color("#FF00FF")

colors = ["#0000FF", "#00FFFF", "#EEE8AA", "#FFA500", "#BA55D3",
          "#4B0082", "#008000", "#FFFF00", "#DC143C", "#556B2F"]

walks = [timmy.fd(20), timmy.bk(20), timmy.rt(90), timmy.lt(90)]


timmy.pensize(10)
timmy.speed(5)

walk = True
while walk:
    random_number = random.randint(1, 4)
    timmy.color(random_colour())
    if random_number == 1:
        timmy.fd(20)
    elif random_number == 2:
        timmy.rt(90)
        timmy.fd(20)
    elif random_number == 3:
        timmy.bk(20)
    elif random_number == 4:
        timmy.lt(90)
        timmy.fd(20)


screen = Screen()
screen.exitonclick()