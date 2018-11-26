'''
Created on Nov 17, 2018

@author: domje
'''

import pickle, shelve


#pickle = allows storage complex data in binary file (.dat)
gotDict = {
    "Steffon": "Ormund"
    , "Robert": "Steffon"
    , "Stannis": "Steffon"
    , "Renly": "Steffon"
    , "Gendry": "Robert"
    , "Joffrey": "Robert"
    , "Tommen": "Robert"
    }

variety = ["sweet", "hot", "dill"]
shape =["spear", "chip", "whole"]
brand =["Claussen", "Heinz", "Vlassic"]

datFile = open("pickles1.dat", "wb")
pickle.dump(gotDict, datFile)
pickle.dump(variety, datFile)
pickle.dump(shape, datFile)
pickle.dump(brand, datFile)
datFile.close()

#now unpickle it

datFileN = open("pickles1.dat", "rb")
gotDictN = pickle.load(datFileN)
varietyN = pickle.load(datFileN)
shapeN = pickle.load(datFileN)
brandN = pickle.load(datFileN)
datFileN.close()

print(gotDictN)
print(varietyN)
print(shapeN)
print(brandN)

#by using shelve, you can make things that act like a dictionary

sh = shelve.open("pickles2.dat")
sh["gotDict"] = gotDictN
sh["variety"] = varietyN
sh["shape"] = shapeN
sh["brand"] = brandN
sh.sync()
sh.close()

#now unshelve it
newSh = shelve.open("pickles2.dat")
print(newSh["gotDict"])
print(newSh["variety"])
print(newSh["shape"])
print(newSh["brand"])

newSh.close()
