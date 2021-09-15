# Turtle Exercise - 100 Days of Code
from random import randint
from turtle import Turtle, Screen

t = Turtle()
t.shape('classic')
t.color('steel blue')
t.pensize(4)

for move in range(4):
    for dot in range(5):
        t.forward(10)
        t.color('yellow')
        t.forward(10)
        t.color('steel blue')
    t.left(90)

"""
# Test making patterns by varying the move distance.
dist = 5
angle = 80
for move in range(30):
    t.forward(dist)
    t.right(angle)
    dist += 2
"""


screen = Screen()
screen.exitonclick()
