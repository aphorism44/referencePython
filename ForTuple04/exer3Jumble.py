'''
Created on Nov 17, 2018

@author: domje
'''

import random


WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
HINTS = ("this programming language", "mixing things up", "not hard", "not easy", "3 for 1 + 2", "instrument you hit")

randIndex = random.randrange(len(WORDS))
word = WORDS[randIndex]
hint = HINTS[randIndex]
correct = word
jumble = ""
guess = ""
guessCount = 0;

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[position + 1:]
    
print("Guess the jumbled word below.")
print(jumble)

wantHint = ""
while wantHint != "Y" and wantHint != "N":
    wantHint = input("Do you want a hint(Y or N)? ")

if wantHint == "Y":
    print("Your hint is: " + hint)


while guess != correct:
    guessCount += 1;
    guess = input("Please enter a guess: ")

score = guessCount
if guess == correct:
    print("Congratulations! The word was indeed " + correct + ".")
    print("You used " + str(guessCount) + " guesses.")
    if wantHint == "N":
        score -= 5
        print("You get a bonus of 5 points since you didn't use a hint!")
    print("Your score is " + str(score) + ", of a best and lowest score of -4.")