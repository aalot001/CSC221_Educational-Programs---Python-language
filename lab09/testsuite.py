#! /usr/bin/env python3

# Ahmed Alotaibi
# 03/21/2016
# Test suite for lab09


import sys
import alice 

def test(did_pass):
    
    linenum = sys._getframe(1).f_lineno   
    if did_pass:
        msg = ("Test at line {0} ok.".format(linenum))
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def main():



    test(alice.OnlyInFirst([1,2,2,3], [0,2,5,6,7]) == [1,3])
    test(alice.OnlyInFirst([0,1,3,6], [0,1,4,5,7]) == [3,6])
    test(alice.OnlyInFirst([0,1,2,4], [0,2,3,5,7]) == [1,4])
    test(alice.OnlyInFirst([0,1,4,5], [0,1,2,3,6]) == [4,5])
    test(alice.OnlyInFirst([0,2,4,5], [0,3,5,6,8]) == [2,4])


    test(alice.OnlyInSecond([1,2,2,3], [0,2,5,6,7]) == [0,5,6,7])
    test(alice.OnlyInSecond([0,1,2,3], [0,2,5,6,7]) == [5,6,7])
    test(alice.OnlyInSecond([0,2,4,5], [0,1,3,4,6]) == [1,3,6])
    test(alice.OnlyInSecond([0,1,3,4], [0,1,5,6,7]) == [5,6,7])
    test(alice.OnlyInSecond([0,2,2,4], [0,3,4,6,8]) == [3,6,8])


    test(alice.inBoth([0,1,2,3], [1,2,5,6,7]) == [1,2])
    test(alice.inBoth([0,1,2,4], [1,2,5,6,8]) == [1,2])
    test(alice.inBoth([0,1,3,4], [0,1,5,6,8]) == [0,1])
    test(alice.inBoth([0,2,3,4], [0,2,4,6,8]) == [0,2,4])
    test(alice.inBoth([0,1,2,4], [0,2,4,6,7]) == [0,2,4])
    
    test(alice.inEitherNotBoth([0,1,2,3], [1,2,5,6,7]) == [0,3,5,6,7])
    test(alice.inEitherNotBoth([1,3,4,6], [0,2,3,5,6]) == [0,1,2,4,5])   
    test(alice.inEitherNotBoth([2,3,5,7], [0,1,4,5,7]) == [0,1,2,3,4])
    test(alice.inEitherNotBoth([1,3,5,6], [0,1,4,5,7]) == [0,3,4,6,7])
    test(alice.inEitherNotBoth([1,3,6,9], [0,2,5,6,9]) == [0,1,2,3,5])

    test(alice.bagDiff([5,7,11,11,11,12,13], [7,8,11]) == [5,11,11,12,13])
    test(alice.bagDiff([5,7,8,9,10,11,11], [7,4,10]) == [5,7,8,9,11,11])
    test(alice.bagDiff([5,8,9,11,13,13,14], [8,10,13]) == [5,9,11,13,14])
    test(alice.bagDiff([5,6,7,9,11,14,14], [6,2,14]) == [5,7,9,11,14])
    test(alice.bagDiff([5,7,9,9,9,11,12], [7,8,9]) == [5,9,9,11,12])



if __name__ == '__main__':
    main()
