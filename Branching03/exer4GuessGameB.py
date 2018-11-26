'''
Created on Nov 17, 2018

@author: domje

You guess a number.
The computer will guess a number, starting with 50, keeping track of the highest and lowest values.
Based on your response, the computer will adjust the ranges.
The next guess will be halfway between the high/low ranges.
Will use // to make sure all guesses are integers.
If the computer can't get it within 7 tries, it knows you're cheating and will tell you.

'''

low = 1
high = 100
found = False
computerGuess = 50
guesses = 0

print("I'll figure out the number you pick, and I'll always get it within 7 turns.")
print("Pick a number and keep it in your head.")

while not found and guesses < 7:
    computerGuess = (high + low) // 2
    print("My guess is " + str(computerGuess))
    response = ""
    while response != "H" and response != "L" and response != "Y":
        print("Please enter H if my number is too high, L if too low, and Y if I guessed the number.")
        response = input("Please enter your response: ")
    if response == "H":
        high = computerGuess - 1
    elif response == "L":
        low = computerGuess + 1
    else:
        found = True
    guesses += 1
        
if found:
    print("Of course you guessed " + str(computerGuess) + ". You can't beat a computer at this game.")
else:
    print("You have cheated - logically speaking, you can't pick any number between 1 and 100 that I can't guess within 7 tries.")
        
