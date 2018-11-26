'''
Created on Nov 15, 2018

@author: domje
'''

check = float(input("Please enter the amount of the restaurant bill: "))
tip15 = check * .15
tip20 = check * .20
print("\nWith a 15% tip, you should pay: ", check + tip15)
print("\nWith a 20% tip, you should pay: ", check + tip20)