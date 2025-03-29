# draw a star using turtle methods

import turtle 
def draw_star(t, size,side_length):
    t.speed(0)
    t.pensize(size)
    for i in range(5):
        t.forward(side_length)
        t.right(144)

t=turtle.Turtle()
draw_star(t,5,50)
turtle.hideturtle()
turtle.done()
