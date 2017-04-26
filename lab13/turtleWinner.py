#! /usr/bin/env python3
# Ahmed Alotaibi
# 4/26/2016
# A competition of speed. Tess and Alex are excited,
# so they cannot wait to start the race. However, I think
# Tess will be the winner, because Alex has responsibilities
# to take care before the game starts.
# Alex will be tired. 
import turtle 
wn = turtle.Screen()
t = turtle.Turtle()
wn.setup(400, 500)
wn.screensize(400, 500)
wn.setworldcoordinates(0, 0, 400, 500)

alex = t 
def DrawLine():
    alex.color("black")
    alex.setpos(0,500)
    alex.forward(400)
    alex.setpos(400,0)
    alex.backward(400)
    alex.setpos(0,350)
    alex.forward(400)    
DrawLine()

wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("purple")
tess.penup()
tess.forward(100)
tess.pendown()
tess.left(90)
tess.forward(10)

alex = turtle.Turtle()
alex.color("blue")
alex.penup()
alex.forward(200)
alex.pendown()
alex.left(90)
alex.forward(10)

def handler_for_tess(x, y): 
     
    tess.forward(50)

def handler_for_alex(x, y):

    alex.forward(50)

def keyForTess():

    tess.forward(50)
    if tess.pos()[1] > t.pos()[1]:
        wn.bye()
        print("Tess clicked at ",tess.pos())
        
def keyForAlex():

    alex.forward(50)
    if alex.pos()[1] > t.pos()[1]:
        wn.bye()
        print("Alex clicked at ",alex.pos())
  
tess.onclick(handler_for_tess)
alex.onclick(handler_for_alex)

wn.onkey(keyForTess, "T")
wn.onkey(keyForAlex, "A")

wn.listen()
wn.mainloop()
