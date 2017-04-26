#! /usr/bin/env python3

# Ahmed Alotaibi
# 3/22/2016
# calculates grades and displays
# classes' names, including
# the average of the gpas.


def calculate_gpa(grades):

    total = 0 

    for p, points in enumerate(grades):

        total = (points / 20) -1

        total = round(total, 1)

    return total

def main():

    class_name = []
    
    class_grades = []


    number_classes = int(input("How many classes did you take? "))
    
    
    for name in range(number_classes):

        name = input("what is the name of class  ? ")

        class_name.append(name)

        continue

    for grade in range(number_classes):
        
        grade = int(input("What grade did you get ? "))
        
        class_grades.append(grade)

    print ()
    
    print("Report card:") 

    for class_number in range(number_classes):
        
        print (class_name[class_number], "-", class_grades[class_number])

    
    print()
    
    print("Term GPA:", calculate_gpa(class_grades))

if __name__ == '__main__':
    main()
