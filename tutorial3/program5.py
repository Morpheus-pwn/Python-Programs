# Write a program to draw a radial pattern with 10 hexagons.

import turtle
t= turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_hexagon(size):
    for _ in range(6):
        t.forward(size)
        t.left(60)
    
hexagon_size=50

for i in range(10):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.left(36)
    draw_hexagon(hexagon_size)

turtle.done()