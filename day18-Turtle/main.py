# Turtle Exercise - 100 Days of Code
from random import randint
from turtle import Turtle
from turtle import Screen

t = Turtle()
t.shape('classic')
t.pensize(2)
t.speed(5)
t.penup()
t.goto(0, 140)
t.pendown()


# Creating a list of shapes with side count and angle between sides.
shapes = []
sides = [3, 4, 5, 6, 7, 8, 10]
for num in sides:
    shape_angle = [num, 360/num]
    shapes.append(shape_angle)

for num in shapes:
    t.color(float(randint(0, 1.0)), float(
        randint(0, 1.0)), float(randint(0, 1.0)))
    side_count = num[0]
    side_turn = num[1]
    for num in range(side_count):
        t.right(side_turn)
        t.forward(100)
    print(side_count, side_turn)

screen = Screen()
screen.exitonclick()
