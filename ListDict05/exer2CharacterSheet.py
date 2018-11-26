'''
Created on Nov 17, 2018

@author: domje
'''

pool = 30
attributeDict = {
    "Strength": 0
    , "Health": 0
    , "Wisdom": 0
    , "Dexterity": 0
    }

while pool > 0:
    print("Here's your character's current stats: ")
    for att in attributeDict:
        print(att + ": " + str(attributeDict[att]))
    print("Points left: " + str(pool))
    attName = "XXX"
    while attName not in attributeDict:
        attName = input("Enter an attribute to update: ")
    pts = pool + 1
    while pts > pool:
        pts = int(input("Enter number of points to allocate: "))
    if attName in attributeDict:
        attributeDict[attName] += pts;
        pool -= pts
        
print("Final character sheet:")
for att in attributeDict:
    print(att + ": " + str(attributeDict[att]))