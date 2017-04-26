#!/usr/bin/env python3

# Ahmed Alotaibi
# 2/24/2016
# modify the program so that it will draw a different shape.


import turtle

wn = turtle.Screen();
t = turtle.Turtle()


wn.setup(300, 200)
wn.screensize(300, 200)
wn.setworldcoordinates(0, 0, 300, 200)


t.penup()
t.setpos(100, 0) 
t.pendown()
t.setpos(100, 200)
t.penup()
t.setpos(200, 0) 
t.pendown()
t.setpos(200, 200)

def square(t):

    for i in range(4):
        t.forward(15)
        t.left(90)
        
    pass

def triangle(t):
    
    for i in range(3):
        t.forward(15)
        t.left(120)
        
    pass


def shapedrawer(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.begin_fill()
    if x <= 100:
         t.color("green")
         t.begin_fill()
         square(t)
         t.end_fill()
    elif 100 < x <= 200:
        t.color("red")
        t.begin_fill()
        t.circle(10)
        t.end_fill()
    else:
        t.color("blue")
        t.begin_fill()
        triangle(t)
        t.end_fill()
        
    #modify the statement here so if user clicked left
    #third to draw a red circle, like so   
    #continue with more statements to match the example
    #shown in the instructions

wn.onscreenclick(shapedrawer)
wn.mainloop()
