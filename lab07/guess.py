#! /usr/bin/env python3

# Ahmed Alotaibi
# 3/8/2016
# A program that counts chars in texts.



def countLetters(text, letter):

   count = 0
   capital = "-"
   small = "_"
   for c, chars in enumerate(text):   
      for c in chars:
         if c == letter:
            capital == capital.upper() or small == small.lower()
            count = count + 1
   return count

def getIndexes(text, letter):
   
   List_Of_All_indexes = []
   index = 0
   index = text.find(letter, index)

   while index >= 0:   
      List_Of_All_indexes.append(index)
      index = text.find(letter, index + 1) 
   return List_Of_All_indexes 

def main():
    text = input("Enter a string of text: ")
    letter = input("Enter on letter to search for: ")
    times = countLetters(text, letter)
    print("The letter '" + letter + "' occured in the string", times, "times.")
    print("It was found at the indexes:", getIndexes(text, letter))


if __name__ == "__main__":
    main()
