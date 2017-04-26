#! /usr/bin/env python3

# Ahmed Alotaibi
# 3/22/2016
# Test for multiple functions. 

import testsuite
def sumOfEven(intList):
    result = 0
    item = (intList)
    for items in myList:
        if items % 2 == 0:
            result = item + item
        return result
def evenMembers(intList):
    result = []
    for item in intList:
        if item % 2 == 0:
            result.append(item)
    return result
def changeList(intList):
    result = []
    mylist = intList
    item = (intList)
    while True: 
        if item % 2 == 0:
            result.append(item * 3)
        else:
            result.append(item // 2)
    return result
"""def isReverse(intListOne, inListTwo):
    for items in intListOne and intListTwo:
        if intListOne == intListTwo:
            return True
        else:
            return False"""
def main():
    intList = testsuite
    print(sumOfEven, evenMembers,
          changeList(intList))
if __name__ == '__main__':
    main()
