'''
Created on Nov 17, 2018

@author: domje
'''

num1 = int(input("Please enter the number to start counting at: "))
num2 = int(input("Please enter the number to stop counting at: "))
numGap = int(input("Please enter the amount each count increments or decrements: "))

if numGap > 0:
    num2 += 1
elif numGap < 1:
    num2 -= 1;

for i in range(num1, num2, numGap):
    print(i)