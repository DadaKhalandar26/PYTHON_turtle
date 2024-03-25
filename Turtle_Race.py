from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colours = ["red", "green", "blue", "black", "orange", "yellow"]
all_turtles = []

user_input = screen.textinput(title="Choose Your Colour", prompt="Which turtle will win the race? Enter the colour")

y = -100
for shade in colours:
    tim = Turtle()
    tim.shape("turtle")
    tim.color(shade)
    tim.penup()
    tim.goto(x=-230, y=y)
    y += 40
    all_turtles.append(tim)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
