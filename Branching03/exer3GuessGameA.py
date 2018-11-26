'''
Created on Nov 17, 2018

@author: domje
'''

import random


num = random.randint(1,100)
found = False
guesses = 0

print("I'm thinking of a number from 1 to 100.")
while not found and guesses < 7:
    guessNum = int(input("Guess a number: "))
    if guessNum < num:
        print("Too low.")
    elif guessNum > num:
        print("Too high.")
    else:
        found = True
    guesses += 1
    
if found:
    print("Congratulations! The number I guessed was indeed ", str(num))
else:
    print("Sorry, I guessed the number " + str(num) + ", and you should have found it within 7 tries.")
    
    
    