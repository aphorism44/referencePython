'''
Created on Nov 17, 2018

@author: domje
'''

import random


count = 0
heads = 0
tails = 0

while count < 100:
    toss = random.randrange(2)
    if toss == 1:
        heads += 1
    else:
        tails += 1
    count += 1
    
print("Heads: " + str(heads))
print("Tails: " + str(tails))
    
    