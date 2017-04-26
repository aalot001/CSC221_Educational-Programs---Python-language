#! /usr/bin/env python3

# Ahmed Alotaibi
# 2/13/2016
# triangles



import turtle

def draw_multicolor_triangle(t, sz):
    """Make turtle t draw a multi-colour triangle of sz."""
    
    for i in ['red','purple','blue']:
        t.color(i)
        t.forward(sz)
        t.left(120)

    def draw_triangle(tess, n, sz, inc):
        for i in range(15):
            t.forward(i)
            t.left(120)
            t.forward(sz)
            t.right(inc)

wn = turtle.Screen()            

wn.bgcolor("lightgreen")


tess = turtle.Turtle()
tess.pensize(3)


size = 10

for i in range(15):
    
    draw_multicolor_triangle(tess, size)
    size = size + 10
    tess.forward(15)
    tess.right(20)




wn.exitonclick()

