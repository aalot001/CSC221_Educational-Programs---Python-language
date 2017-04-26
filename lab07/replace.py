#! /usr/bin/env python3

# Ahmed Alotaibi
# 3/8/2016
# A program that removes chars or words
# and replaces a dash, "-".


def removeChar(char, sentence):

    chars = "-"    
    chars = sentence.replace(char, chars)
    Not_found = "Letter Not found"
    
    while char >= sentence:
        if char == "": 
            chars = sentence + char.replace("-")
        elif char != "":
            return Not_found
    else:
        return chars
    
def removeWord(word, sentence):
    
    words = "-"
    words = sentence.replace(word, words)
    
    for word in range(len(sentence)):
        if word == "":
            word = sentence + word.replace("-")
    return words

def main():
    sentence = input("Enter a word, sentence or phrase: ")
    print("What would you like to do?")
    print("1: Replace character(s) in your a word, sentence, or phrase")
    print("2: Replace a word in your sentence or phrase")
    choice = eval(input("Enter the number of your choice: "))
    if(choice == 1):
        ch = input("Enter one or more chars to clean them from the phrase: ")
        print("Your original phrase:", sentence)
        print("Your cleaned phrase:", removeChar(ch, sentence))
    elif(choice == 2):
        word = input("Enter a word to clean from the phrase: ")
        print("Your original phrase:", sentence)
        print("Your cleaned phrase:", removeWord(word, sentence))
    else:
        print("You entered an invalid choice.")

if __name__ == "__main__":
    main()
