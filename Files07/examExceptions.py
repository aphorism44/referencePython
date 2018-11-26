'''
Created on Nov 17, 2018

@author: domje
'''

try:
    num = float(input("Enter a number:"))
    print(num)
except:
    print("Hit an error")

testTuple = (None, "Hi!", 42, "234")

for v in testTuple:
    try:
        print("Attempting to convert", v, "-->", end = " ")
        print(float(v))
    except (TypeError, ValueError):
        print("Hit an error during conversion")
        
for v in testTuple:
    try:
        print("Attempting to convert", v, "-->", end = " ")
        newV = float(v)
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)
    else:
        print(newV)