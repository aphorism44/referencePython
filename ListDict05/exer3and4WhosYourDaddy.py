'''
Created on Nov 17, 2018

@author: domje
'''

#male and father dict
gotDict = {
    "Steffon": "Ormund"
    , "Robert": "Steffon"
    , "Stannis": "Steffon"
    , "Renly": "Steffon"
    , "Gendry": "Robert"
    , "Joffrey": "Robert"
    , "Tommen": "Robert"
    }

name1 = "Gendry"
name2 = "Renly"
name3 = "Steffon"
name4 = "Tommen"
name5 = "Robert"
name6 = "Stannis"

print("Father of " + name1 + " is " + gotDict[name1])
print("Father of " + name2 + " is " + gotDict[name2])
print("Father of " + name3 + " is " + gotDict[name3])

#now find grandparents
father4 = gotDict[name4]
if father4 in gotDict:
    print("Grandfather of " + name4 + " is " + gotDict[father4])

father5 = gotDict[name5]
if father5 in gotDict:
    print("Grandfather of " + name5 + " is " + gotDict[father5])
    
father6 = gotDict[name6]
if father6 in gotDict:
    print("Grandfather of " + name6 + " is " + gotDict[father6])