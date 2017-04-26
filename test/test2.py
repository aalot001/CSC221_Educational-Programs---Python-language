""" 1 -
Write a function that takes a list of numbers as a parameter
and modifies this list by doubling every number."""
"""def double(aList):
    for i in range(len(aList)):
        aList[i] = aList[i]*2
def main():
    aList = [1,2,3,4,5,6]
    double(aList)
    print(aList)
if __name__=="__main__":
    main()
#-------------------------------------------
2- 
Write a function that takes a list of numbers as a parameter
and returns a new list in which every number is twice the value
of the corresponding number in the parameter list.
def returnNewList(aList):
    result = []
    for n, items in enumerate(aList):
result.append(items * 2)
    return result
def main():
    aList = [1,2,5,6]
    newLList = returnNewList(li)
    print(newList)
if __name__=="__main__":
    main() 
#-----------------------------------------
3-
Write a function that takes a list of numbers as
a parameter and modifies this list reversing
it (without using built-in reverse method or slices).
def ListRevers(li):
    for i in range(len(li)//2):
        li [i], li[-i-1] = li[-i-1], li[i]
def main():
    li = [24,3,40,54,56,66,3,4,7,8]
    Revers(li)
    print(li)
if __name__=="__main__":
    main()
#--------------------------------------
4-
Write a function that takes a list of numbers as a parameter
and returns a new list with the same numbers but in the reverse order
(without using built-in reverse method or slices).
def Revers(aList):
    new_List = []
    for i in range(len(aList)):
        new_List.append(aList[-i-1])    
    return new_List
def main():
    aList = [4,23,5,6,22,90,100]
    new_Result = Revers(aList)
    print(new_Result)
if __name__=="__main__":
    main()
#---------------------------------------
6-
Write a function that takes a dictionary as a parameter,
containing entries such as "Tom":"555-5555" and modifies this
dictionary by pre-appending the area code "518-" to the values,
so that the entry becomes "Tom":"518-555-5555".

def preappendingAreaCode(phones):
    for i in phones.keys():
        phones[i] = "518-" + phones[i]
#---------------------------------------
7 -
Write a function that takes a dictionary as a parameter,
containing entries such as "Tom":"555-5555" and returns a new dictionary
in which the entries are similar but the area code "518-"
has been pre-appended to the values: "Tom":"518-555-5555".

def addAreaCode(phones):
    newNumber = {}
    for (k,v) in phones.items():
        newNumber[k] = "518-"+v
    return newNumber
def main():
    phones = {"Ahmed": "335-3196","Yazeed": "111-1212", "Harris": "555-1111"}
    preappendingAreaCode(phones)
    #addAreaCode(phones)
    print(phones)    
main()
#--------------------------------------
8 -
Write a fragment of code that repeatedly asks the user for a number or to
terminate the input by just pressing enter.
After all the input has been received,
the program prints the average of the numbers.
def while_average():
    count = 0
    total = 0
    while True:
        x = input("enter number or press Enter : ")
        if x =="":
            break
        total += eval(x)
        count += 1
    average = total/count
    print(" The average is",round(average,2))
while_average()
#-------------------------------------
9-
Write a function that takes as a parameter a non-empty dictionary
containing key-value pairs similar to "five":5, "eleven":11
and returns the maximum value from the pairs.
For instance, given {"five":5, "eleven":11}
the function should return 11.
def maximum(aDict):
    List = list(aDict.values())
    maxSoFar = List[0]
    for item in List:
        if maxSoFar < item:
            maxSoFar = item
        elif maxSoFar == item:
            maxSoFar = maxSoFar
    return maxSoFar
def main():
    aDict = {"five":5,"eleven":11}
    new = maximum(aDict)
    print(new)
if __name__=="__main__":
    main()
10 -
Write a program that takes numbers and return
a new List when even number divide by 2 and odd number
double by 2
def double1(myList):
    result = []
    for items in myList:
        if items % 2 == 0:
            result.append(items // 2)
        else:
            result.append(items * 2)
    return result
def main():
    myList = [1,2,5,6]
    newList = double1(myList)
    print(newList)
if __name__=="__main__":
    main()
11 -
Write a function that asks user for three values.
Create a list containing these values
and print the list with these values double..
def main():
    x,y,z = eval(input("Enter three values separetaed by common please: "))
    aList = [x,y,z]
    newList = [2 * x, 2 * y, 2 * z]
    print(newList)
if __name__=="__main__":
    main()
#---------------------------------
12-    
def kosequence(a,aList):
    n = 1
    aList.append(a)
    while a != 1:
        if a % 2 == 0:
            a = a // 2
            aList.append(a)
        else:
            a = (a*3) + 1
            aList.append(a)
        n += 1
    return n
def main():
    while True:
        values = input("Enter a number for a kolatz sequence or press enter to end: ")
        if values =="":
            break
        else:
            newList = []
            n = kosequence(eval(values),newList)
            print(newList)
            print(n)          
main()
if __name__=="__main__":
    main()
#13 --------
#Write a class fraction with multiplication method:   
class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom 
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def __mul__(self,other):
        newNu = self.num * other.num
        newDo = self.den * other.den
        return Fraction(newNu, newDo)
def main():
     x = Fraction(1,2)
     y = Fraction(1,3)
     a = x * y 
     print(a)
main()
#-----------------------------------------------------------------------------------------------------------------------
#Write a function that takes as promote aList of number and return the biggest number.
def largest(aList):
    if aList == [ ] :
        raise ValueError("An empty list does not have the largest item")
    largest_So_Far =  aList[0]
    for item in aList:
        if item > largest_So_Far:
            largest_So_Far = item 
    return largest_So_Far
def main():
    aList = [40,-40,35,-35,11,1000,9191,30,-40,40]
    print(largest(aList))
main()
