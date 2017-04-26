#!/usr/bin/env python3

# Ahmed Alotaibi
# 2/24/2016
# Rock, Paper, or Scissors game. 


import random


def randomDraw():
   draws = ["rock", "paper", "scissors"]
   return draws[random.randrange(0,3)]

wins = 1
losses = 1
ties = 0
while(1):

   x = input("Rock, Paper, or Scissors('exit to leave)?")

   y = randomDraw()

   if x == "exit":

      print("Game ended")

   
   if x =="paper" and y =="rock":
      print ("Computer chose rock. You win!")
      
   elif x =="rock" and y =="paper":
      print("Computer chose paper. You lose!")
      
   elif x == "rock" and y =="rock":
      print("Computer chose rock. Tie!")
     
   elif x =="scissors" and y =="paper":
      print("Computer chose paper. You win!")
      
   elif x =="scissors" and y =="scissors":
      print("Computer chose scissors. Tie!")
      
   elif y =="paper" and x =="rock":
      print("Computer chose paper. You lose!")
      
   elif y =="scissors" and x =="paper":
      print("Computer chose scissors. You lose!")
      
   elif x =="rock" and y =="scissors":
      print("Computer chose scissors. You win.")

