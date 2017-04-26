#! /usr/bin/env python3

# Ahmed Alotaibi
# 3/8/2016
# A program that shows the
# students' names with their letter grades.

    
# This is Python 

def grade(studentchoice):
    if studentchoice == "yes" or studentchoice == "Yes":
        decision = 'Thank you for your willingness ..'
    else:
        if studentchoice == "No" or studentchoice == "no":
            decision = 'That is not a good decision ..'
    return decision   
def main():
    studentchoice = str(input("To pass the test, type 'Yes', to repeat type 'No': "))
    new = grade(studentchoice)
    print(new)
if __name__=="__main__":
    main()
