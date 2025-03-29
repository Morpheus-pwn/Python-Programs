# Write a program to draw a pentagon using turtle.

import turtle

t=turtle.Turtle()
t.speed(0)
t.pencolor("black")
t.pensize(5)
t.penup()
t.pendown()

for i in range(5):
    t.forward(100)
    t.right(72)

turtle.hideturtle()
turtle.done()