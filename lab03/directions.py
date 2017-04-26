#!/usr/bin/env python3

# Ahmed Alotaibi
# 02/09/2016
# Directions proof of concept


import turtle

win = turtle.Screen()
win.bgcolor("white")



alotaibi = turtle.Turtle()
alotaibi.color("red")
alotaibi.pensize(4)




direction = input("What direction would you like to go (left, right, up, down)? " )

if(direction == "left" ):

    alotaibi.forward(150)
    alotaibi.left(90)
    alotaibi.forward(75)
    alotaibi.left(90)
    alotaibi.forward(75)
    
 


elif(direction == "right" ):

    alotaibi.forward(75)
    


elif(direction == "up" ):

      alotaibi.forward(150)
      alotaibi.left(90)
      alotaibi.forward(75)


   

elif(direction == "down" ):

    alotaibi.forward(150)
    alotaibi.right(90)
    alotaibi.forward(75)
    


else:
    print("You've entered an invalid option." )



win.exitonclick()
