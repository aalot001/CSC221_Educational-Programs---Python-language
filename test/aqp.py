#!/usr/bin/python3
'''
    CSC318
    Spring 2017
    2.9.11 Programming Exercise
    Write a program which asks the user for two natural numbers m, n and then
    displays all the ordered pairs in {i ∈ Z+ : i <= m} × {j ∈ Z+ : j <= n}.
    Run from the command line as:
        python3 2.9.11.py
    Or:
        chmod +x 2.9.11.py && ./2.9.11.py
'''
class OrderedPair():
    def __init__(self, m, n):
        self.m = m
        self.n = n
    def __str__(self):
        return str((self.m, self.n))
        
if __name__ == '__main__':
    try:
        m, n = input('Enter two numbers separated by a space:').split(' ')
        for i in range(1, int(m)+1):
            for j in range(1, int(n)+1):
                print(OrderedPair(i, j))
    except:
        raise ValueError
