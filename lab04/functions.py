#! /usr/bin/env python3

# Ahmed Alotaibi
# 2/15/2016
# functions



import testsuite

def absolute_value(x):
    if x < 0:
        return -x

    return x


def is_divisible(x, y):
    
    return x % y == 0


def sub_min_max(x, y):
    
    return max(x, y) - min(x, y)


def mymax(x, y):

    if (x > y):
        
        return x
    
    return y

def fibo(n):
    
    if n == 1 or n == 2:
        
        return 1
    
    return fibo(n-1) + fibo(n-2)

testsuite.run(absolute_value, is_divisible, sub_min_max, mymax, fibo)



