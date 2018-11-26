'''
Created on Nov 17, 2018

@author: domje
'''

import random


cookieNum = random.randint(1,5)
fortune = ""

if cookieNum == 1:
    fortune = "You will have very good luck today!"
elif cookieNum == 2:
    fortune = "Your luck will be generally good."
elif cookieNum == 3:
    fortune = "Your luck is so-so."
elif cookieNum == 4:
    fortune = "You have bad luck coming today."
else:
    fortune = "You should make out your will before tonight."
    
print(fortune)

