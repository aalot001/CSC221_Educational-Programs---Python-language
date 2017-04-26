
#1-
#Write a function that takes a list of numbers as a parameter
#and modifies this list by doubling every number.
def double1(aList):
    for i in range(len(aList)):
        aList[i] = aList[i]*2
def main():
    aList = [1,2,3,4,5,6]
    double1(aList)
    print(aList)
if __name__=="__main__":
    main()
#OutPut = [2,4,6,8,10,12]
#-------------------------------------------
#2- 
#Write a function that takes a list of numbers as a parameter
#and returns a new list in which every number is twice the value
#of the corresponding number in the parameter list.
def double1(myList):
    result = []
    for n, items in enumerate(myList):
            result.append(items * 2)
    return result
def main():
    myList = [1,2,5,6]
    newList = double1(myList)
    print(newList)
if __name__=="__main__":
    main()
#OutPut = [2,4,10,12]
#-----------------------------------------
#3-
#Write a function that takes a list of numbers as
#a parameter and modifies this list reversing
#it (without using built-in reverse method or slices).
def listReversing(aList):
    for i in range(len(aList)//2):
        aList [i], aList[-i-1] = aList[-i-1], aList[i]
def main():
    aList = [24,3,40,54,56,66,3,4,7,8]
    listReversing(aList)
    print(aList)
if __name__=="__main__":
    main()
#OutPut = [8,7,4,3,66,56,54,40,3,24]
#--------------------------------------
#4-
#Write a function that takes a list of numbers as a parameter
#and returns a new list with the same numbers but in the reverse order
#(without using built-in reverse method or slices).
def listReversing2(aList):
    newList = []
    for i in range(len(aList)):
        newList.append(aList[-i-1])    
    return newList
def main():
    aList = [4,23,5,6,22,90,100]
    newResult = listReversing2(aList)
    print(newResult)
if __name__=="__main__":
    main()
#OutPut = [100,90,22,6,5,23,4]
#---------------------------------------
#5-
#Write a function that takes a dictionary as a parameter,
#containing entries such as "Tom":"555-5555" and modifies this
#dictionary by pre-appending the area code "518-" to the values,
#so that the entry becomes "Tom":"518-555-5555".
def preappendingAreaCode(phones):
    for i in phones.keys():
        phones[i] = "518-" + phones[i]
#---------------------------------------
#6 -
#Write a function that takes a dictionary as a parameter,
#containing entries such as "Tom":"555-5555" and returns a new dictionary
#in which the entries are similar but the area code "518-"
#has been pre-appended to the values: "Tom":"518-555-5555".
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
if __name__=="__main__":
    main()
#OutPut ={'Ahmed': '518-335-3196', 'Yazeed': '518-111-1212', 'Harris': '518-555-1111'}
#--------------------------------------
#7 -
#Write a fragment of code that repeatedly asks the user for a number or to
#terminate the input by just pressing enter.
#After all the the input has been received,
#the program prints the average of the numbers.
def whileaverage():
    count = 0
    total = 0
    while True:
        x = input("enter number or press Enter : ")
        if x =="":
            break
        total += eval(x)
        count += 1
    average = total/count
    print("The average is",round(average,2))
whileaverage()
#-------------------------------------
#8 -
#Write a function that takes as a parameter a non-empty dictionary
#containing key-value pairs similar to "five":5, "eleven":11
#and returns the maximum value from the pairs.
#For instance, given {"five":5, "eleven":11}
#the function should return 11.
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
#-----------------------------------------
#9-
#Write a program that takes numbers and return
#a new List when even number divide by 2 and odd number
#double by 2
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
#OutPut = [2, 1, 10, 3]
#-------------------------------------
#10-
#Write a function that asks user for three values.
#Create a list containing these values
#and print the list with these values double..
def main():
    x,y,z = eval(input("Enter three values separetaed by common please: "))
    aList = [x,y,z]
    newList = [2 * x, 2 * y, 2 * z]
    print(newList)
if __name__=="__main__":
    main()
#---------------------------------
#11-
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
if __name__=="__main__":
    main()
#-----------------------------------------------------------------
#12-
#Append numbers to the list, use the below code:
def main():
    a = [1,2,3,4,5]
    b = a [:]
    b.append(6)
    b.append(9)
    b.append(10)
    print(b) # OutPut = [1,2,3,4,5,6,9,10]
    print(a) # OutPut = [1,2,3,4,5]
if __name__=="__main__":
    main()
#----------------------------------------------------
#13-
# To change the value position use the below code:
def revers(aList):
    for i in range(len(aList)):
        aList[0], aList[4] = aList[4], aList[0]
def main():
    aList = [1,2,3,4,5]
    revers(aList)
    print(aList) # the Output is [5,2,3,4,1]
if __name__=="__main__":
    main()
#------------------------------------------------
#14-
#Write a program that asks and appends the number
#from the biggest to the lowest. No newList
def main():
    aList = []
    while True:
        x = input("Enter interger please" )
        if x == "":
            break
        else:
            aList.append(eval(x))
    for i in range(1,len(aList)+1):
        print(aList[-i])
if __name__=="__main__":
    main()
#--------------------------------------------------
#15-
#write a fraqment of code that opens file data.tx
#or catdes the FileNotFoundError Exception
"""try:
    myfile = open("data.txt", "r")
except FileNotFound:
    print(" ")"""
#------------------------------------------
#16-
#Write a code that checks if the file exits and return True or False.
#Also, the main function is for the user including excepation for no file.
def exists(filename):
    try:
        f = open(filename)
        f.close()
        return True
    except:
        return False
def main():
    filename = input("Enter a file name: ")
    try:
        f = open(filename, "r")
    except:
        print("There is no file named", filename)
        new = exists(filename)
        print(new)    
if __name__=="__main__":
    main()
#--------------------------------
#17-
#Write a program in which a turtle draws a square.
import turtle
win = turtle.Screen()
win.bgcolor("green")
ahmed = turtle.Turtle()
for i in range(4):
    ahmed.forward(100)
    ahmed.left(90)
win.exitonclick()
#---------------------------------------
#Write a program that asks user for integer n and print all squares
#18-
import turtle
win = turtle.Screen()
ahmed = turtle.Turtle()
n = eval(input("Please enter an integer to find the all squares: "))
for i in range(1,n+1):
    print(i*i)
win.exitonclick()
#-----------------------------------------
#Write a class fraction with multiplication method:
#19-
class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.doe = bottom
    def __str__(self):
        return str(self.num) +"/"+str(self.doe)
    def __mul__(self, other):
        newNum = self.num * other.num
        newDoe = self.doe * other.doe
        return Fraction(newNum, newDoe)
def main():
    x = Fraction(1,2)
    y = Fraction(1,3)
    a = x * y
    print(a)
if __name__=="__main__":
    main()
#OutPut = 1/6
#--------------------------------------------------
#Write a function that takes as promote aList of number and return the biggest number.
#20-
def highest(aList):
    if aList == [ ] :
        raise ValueError("An empty list does not have the largest item")
    largest_So_Far =  aList[0]
    for item in aList:
        if item > largest_So_Far:
            largest_So_Far = item 
    return largest_So_Far
def main():
    aList = [40,-40,35,-35,11,1000,9191,30,-40,40]
    print(highest(aList))

if __name__=="__main__":
    main()
#OutPut = 9191
#----------------------------------------------------
#21
   
def highest2(aList):
    high = aList[0]
    for n, item in enumerate(aList):
        if high < aList[n]:
            high = aList[n]
    return high
def main():
    aList = [12,8,35,19,11]
    newHigh = highest2(aList)
    print(newHigh)
if __name__=="__main__":
    main()
#------------------------------------
#22-
from random import randrange
def roll1():
    return randrange(1, 7)
def roll5():
    return roll1(), roll1(), roll1(), roll1(), roll1()
def allsame(dice):
    return dice[0] == dice[1] == dice[2] == dice [3] == dice[4]
def simulata1():
    count = 0
    while True:
        dice = roll5()
        count += 1
        if allsame(dice):
            break
    return count
def simulataN(n):
    total = 0
    for i in range(n):
        total += simulata1()
    return total/n
def printIntro():
    print("This program simulates tosses of 5 dices and ")
    print("and tells hom many are needed to obtain 5 of the kind. ")
def getInput():
    return eval(input("How many sulations to run ? "))
def printResults(avg):
    print("An average of",avg,"tosses were needed to obtain of the kind. ")
def main():
    printIntro()
    n = getInput()
    avg = simulataN(n)
    printResults(avg)
if __name__ == "__main__":
    main()
