#! /usr/bin/env python3


# Ahmed Alotaibi
# 3/2/2016
# BinaryGuess. Game for testing.


def main():

    import random

    computer_tries = 0
    player_number = None
    computer_guess = random.randint(1, 100)
    question = None
    lower = 0 
    higher = 101
    
    while question != ("yes"):
        question = input("Did you pick a number? ")
        question = question.lower()
        
        if question == "yes":
            print("\nI will now guess your number!!!\n")

            
        while player_number == None:
            computer_tries += 1
            print(computer_guess, "\n")
            
            answer = input("Is this the correct number? ")
            answer = answer.lower()
            
            if answer == "yes":
                player_number = computer_guess
                if computer_tries < 2:
                    print("I did it! I guessed your number was", computer_guess,
                           "and it only \ntook me", computer_tries,
                           "try to get it right!")
                    
                else:
                    print("I did it! I guessed your number was", computer_guess,
                           "and it only \ntook me", computer_tries,
                           "tries to get it right!")
                    
            else:
                higher_lower = None
                while higher_lower not in ("higher", "lower"):
                    higher_lower = input("Is my guess higher or lower than your number? ")
                    
                    higher_lower = higher_lower.lower()
                    if higher_lower == "higher":
                        higher = computer_guess
                        computer_guess = random.randint(lower+1, higher-1)
                        
                    elif higher_lower == "lower":
                        lower = computer_guess
                        computer_guess = random.randint(lower+1, higher-1)
                        
                    else:
                        print("Please choose either higher or lower.")
                    print("Message: number must be " + str(lower) + " < x < " + str(higher))

if __name__=="__main__":
    main()  
