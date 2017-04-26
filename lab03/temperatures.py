#! /usr/bin/env python3




# Import the turtle library and the random library here

import turtle

import random


# Create a new screen and turtle here

win = turtle.Screen()

ahmed = turtle.Turtle()

# Set the initial temperature t here

t = 50


# Create a for loop using a range 0-25 here

for i in range(0,25):


# Create a random integer y inside of your for loop

    y = random.randint(10,100)

   

    if (y > t):
            ahmed.color("red")
            ahmed.left(90)
            ahmed.forward(y-t)
            ahmed.right(90)
            ahmed.forward(15)

    elif(y < t):
            ahmed.color("blue")
            ahmed.right(90)
            ahmed.forward(t-y)
            ahmed.left(90)
            ahmed.forward(15)
      

    t = y

   

win.exitonclick()






