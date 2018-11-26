'''
Created on Nov 26, 2018

@author: domje

Demonstrate module creation
'''

class Player(object):
    """A player for a game."""
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep
    

def ask_yes_no(question):
    """Ask a yes/no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_integer(question, low, high):
    """Ask for an integer within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

if __name__ == "__main__":
    print("You ran this module directly and did not import it.")
    input("\n\nPlease press Enter to exit.")
