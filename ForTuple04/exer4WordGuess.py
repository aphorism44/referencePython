'''
Created on Nov 17, 2018

@author: domje
'''

import random


WORDS = ("apple", "banana", "cherry", "orange", "lemon", "raspberry", "pear", "mango")

word = random.choice(WORDS)
guess = ""
guesses = 0

print("You have 5 chances to guess the name of a fruit, which has " + str(len(word)) + " letters in it.")
print("You can get hints by checking if a letter is in it.")

while guesses < 5 and guess != word:
    letter = input("Guess a letter: ")
    if letter in word:
        print("That letter is in the fruit name.")
    else:
        print("That letter is not in the fruit name.")
    guess = input("Enter your guess: ")
    guesses += 1
    
if guess == word:
    print("Congratulations! The word was indeed " + guess)
else:
    print("Sorry, game over. The word was " + word)