#! /usr/bin/env python3

# Tyler Whitney
# 02/09/2016
# Test suite for lab04

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def run(absolute_value, is_divisible, sub_min_max, mymax, fibo):
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)
  
    test(is_divisible(6, 4) == False)
    test(is_divisible(6, 3) == True)

    test(sub_min_max(5, 10) == 5)
    test(sub_min_max(10, 5) == 5)
    test(sub_min_max(7, 3) == 4)
    test(sub_min_max(2, 5) == 3)
    test(sub_min_max(25, 100) == 75)
    test(sub_min_max(-5, 10) == 15)
    test(sub_min_max(-10, -25) == 15)

    test(mymax(10, 5) == 10)
    test(mymax(200, 1) == 200)
    test(mymax(1, 2) == 2)
    test(mymax(-10, 10) == 10)
    test(mymax(-25, -10) == -10)

    test(fibo(4) == 3)
    test(fibo(5) == 5)
    test(fibo(17) == 1597)
    test(fibo(13) == 233)
    test(fibo(23) == 28657)
    test(fibo(26) == 121393)
    test(fibo(75) == 2111485077978050)

#test_suite()        # Here is the call to run the tests
