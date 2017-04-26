#! /usr/bin/env python3

# Ahmed Alotaibi
# 4/12/2016
# A program that creates a car with its speed, providing its dirction to take.
# It will points out at the car's position. Also, I created a second car.


class Car:
    def __init__(self, start_pos, speed):
        
        self.st = start_pos
        self.sp = speed
        
    def drive(self, time, direction):
        
        self.t = time 
        self.d = direction
        
        self.st = self.sp // self.t

    def printPosition(self):
        
        print("The car is currently located at position",self.st)
        
        
def main():

    myCar = Car(2,55)        
    myCar.printPosition()
    myCar.drive(5, 'forward')
    myCar.printPosition()
    myCar.drive(11, 'backward')
    myCar.printPosition()

    print("The below is the second car's position.")

    secondCar = Car(4, 20)
    secondCar.printPosition()
    secondCar.drive(6, 'backward')
    secondCar.printPosition()
    secondCar.drive(2, 'forward')
    secondCar.printPosition()
    
if __name__ == "__main__":

    main()
