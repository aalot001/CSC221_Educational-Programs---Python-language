#! /usr/bin/env python3

# Ahmed Alotaibi
# 3/29/2016
# test many functions for lab09.



    
def OnlyInFirst(first, second):
   
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(first):
            return result

        if yi >= len(second):
            result.extend(first[xi:])
            return result

        if first[xi] == second[yi]:  
            xi += 1

        elif first[xi] < second[yi]: 
            result.append(first[xi])
            xi += 1

        else:                        
            yi += 1


def OnlyInSecond(first, second):

    result = []

    xi = 0
    yi = 0

    while True:

        if xi >= len(first):

            result.extend(second[yi:])

            return result

        if yi >= len(second):

            return result

        if first[xi] == second[yi]:

            yi += 1

        elif first[xi] < second[yi]:

            xi += 1

        else:

            result.append(second[yi])

            yi += 1


            
def inBoth(first, second):

    result = []

    xi = 0
    yi = 0

    while True:

        if xi >= len(first):

            result.extend(second[:yi])

            return result

        if yi >= len(second):

            result.extend(first[xi:])

            return result

        if first[xi] == second[yi]:

            yi += 1

        elif first[xi] < second[yi]:

            xi += 1

        else:
            
            result.append(second[yi])
            yi += 1


def inEitherNotBoth(first, second):


    result = []

    xi = 0
    yi = 0

    while True:

        if xi >= len(first):

            result.extend(second[yi:])

            return result

        if yi >= len(second):

            result.extend(first[xi:])

            return result

        if first[xi] == second[yi]:

            yi += 1

        elif first[xi] < second[yi]:

            result.append(second[yi])

            xi += 1

        else:

            result.append(first[xi])
            yi += 1


def bagDiff(first,second):

    result = []

    xi = 0
    yi = 0

    while True:
        if xi >= len(first):
            
            result.extend(second[:yi])
            return result

        if yi >= len(second):

            result.extend(first[xi:])
            return result

        if first[xi] == second[yi]:

            xi += 1

        elif first[xi] < second[yi]:

            result.append(first[xi])
            xi += 1
            return result

        else:

            yi += 1
            

def main():

    pass
            

if __name__== '__main__':

    
    main()
