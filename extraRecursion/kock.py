#! /usr/bin/env python3


# Ahmed Alotaibi
# 3/13/2016
# Koch...Extra credit assignment.


import turtle 


def koch_Direction(order, depth):


    if depth == 0:

        ahmed.forward(order)
        

    else:
            
        koch_Direction(order/3, depth-1)
        ahmed.right(60) 
        koch_Direction(order/3, depth-1) 
        ahmed.left(120)
        koch_Direction(order/3, depth-1) 
        ahmed.right(60)  
        koch_Direction(order/3, depth-1)


def Draw_snowFlake(order, depth):


    for i in range(3):
        
        koch_Direction(order, depth)
        
        ahmed.left(120)


wn = turtle.Screen()
ahmed = turtle.Turtle()

wn.bgcolor("lightgreen")
ahmed.color("blue")

ahmed.penup()
ahmed.pendown()

ahmed.pensize(3)
ahmed.speed(50)


Draw_snowFlake(400,2)

wn.exitonclick()
