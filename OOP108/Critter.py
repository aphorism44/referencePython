'''
Created on Nov 18, 2018

@author: domje
'''

import sys


class Critter(object):
    '''A virtual pet'''
    total = 0
    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.__hunger = hunger
        self.__boredom = boredom
        Critter.total += 1
    def __str__(self):
        str = "\nCritter object\n"
        str += "Name: " + self.name + "\n"
        str += "Hunger: " + str(self.__hunger) + "\n"
        str += "Boredom: " + str(self.__boredom) + "\n"
        str += "Mood: " + self.mood + "\n"
        return str
    def talk(self):
        print("Hi! I'm ", self.name, ", and I'm feeling " + self.mood)
        self.__pass_time()
    def __pass_time(self):
        self.__hunger += 1
        self.__boredom += 1
    def eat(self, food = 4):
        print("Brrp. Thank you.")
        self.__hunger -= food
        if self.__hunger < 0:
            self.__hunger = 0
        self.__pass_time()
    def play(self, fun = 4):
        print("Wheee!")
        self.__boredom -= fun
        if self.__boredom < 0:
            self.__boredom = 0
        self.__pass_time()
    @property
    def mood(self):
        unhappiness = self.__hunger + self.__boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name = ""):
        if new_name == "":
            print("A Critter's name can't be an empty string.")
        else:
            self.__name = new_name
    @staticmethod
    def status():
        print("Total instantiated Critter objects: ", Critter.total)
        

def print_menu(crit):
    choice = None
    print \
    ("""
    Critter Caretaker
    
    0 - Quit
    1 - Listen to your critter
    2 = Feed your critter
    3 = Play with your critter
    """)
    
    choice = int(input("Choice: "))
    print()
    if choice == 0:
        print("Goodbye!")
        sys.exit()
    elif choice == 1:
        crit.talk()
    elif choice == 2:
        crit.eat()
    elif choice == 3:
        crit.play()
    elif choice == 999:
        print(crit)
    else:
        print("\nSorry, but ", choice, " isn't a valid option.")


def main():
    name = input("Name of your critter?: ")
    crit1 = Critter(name)
    while True:
        print_menu(crit1)
    
    
main()