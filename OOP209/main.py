'''
Created on Nov 25, 2018

@author: domje
'''

import blackjack, games

def main():
    print("\t\tWelcome to Blackjack!\n")
    names = []
    number = games.ask_integer("How many players (1-7)? ", 1, 8)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()
    game = blackjack.BJ_Game(names)
    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")
    
    
    
main()
input("\n\nPress enter key to exit.")