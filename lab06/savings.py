#! /usr/bin/env python3

# Ahmed Alotaibi
# 3/1/2016
# A program shows how many years you will be waiting 
# for reaching the interest amount of your goal.
# Savings program, you may called it.




x =eval(input("How much would you like to start with?"))
    
y =eval(input("How is your interest rate?"))
    
z =eval(input("What is your amount goal?"))

year = 0


while x <= z :
    
    x = x * (1 + y)
    
    year = 1 + year

    print("Ater year ", year, " the amount is at ",round(x,2))

