#! /usr/bin/env python3

# Ahmed Alotaibi
# 4/19/2016
# A program that creates a car with its speed,
# providing its direction to take.
# It will points out at the cars' positions.
# Also, it prints the driver's name, including a deep copy for a second car
# from the first one with different speed
# and direction to take than the previous
# vehicle. And it shows the difference.
# Finaly, I added the Extra Credit, which asks the user for her/his age. 
import copy
import guarding
class Car:   
    def __init__(self, start_pos, speed, driver):
        self.st = start_pos
        self.sp = speed
        self.dr = driver

    def setDriver(self, driver):
        self.dr = driver
    def getDriver(self):
        return self.dr
    
    def drive(self, time, direction):
        self.t = time 
        self.d = direction
        self.st = self.sp // self.t

    def printPosition(self):
        print("The car is currently located at position",self.st)
class driver:
    def __init__(self, name, age, license_type):
        self.n = name
        self.ag = age
        self.lic = license_type
    def setName(self, name):
        self.n = name
    def setAge(self, age):
        self.ag = age
    def setLicenseType(self, ltype):
        self.lic = ltype
    def getName(self):
        return self.n
    def getAge(self):
        return self.ag
    def getLicenseType(self):
        return self.lic
    def printName(self):
        print ("The driver's name is :", self.getName())
        print("The driver's age is :", self.getAge())        
def main():
    myCar = Car(2,55,None)
    myCar.printPosition()
    myCar.drive(5, 'forward')
    myCar.printPosition()
    myCar.drive(11, 'backward')
    myCar.printPosition()

    age = guarding.getIntegerBetween("Please Enter your age : ", 16, 100)
    myDriver = driver("Ahmed", age, "Class D")
    myCar.setDriver(myDriver)
    myDriver = myCar.getDriver()
    myDriver.printName()
    
    secondCar = copy.deepcopy(myCar)
    secondCar.drive(20, 'forward')
    secondCar.drive(8, 'backward')
   
    print ('This is the first car.')
    myCar.printPosition()
    print ('This is the second car.')
    secondCar.printPosition()
    
if __name__ == "__main__":
    main()
