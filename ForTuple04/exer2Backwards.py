'''
Created on Nov 17, 2018

@author: domje
'''

inputStr = input("Please enter a message: ")

for i in range(len(inputStr) - 1, -1, -1):
   print(inputStr[i], end="")