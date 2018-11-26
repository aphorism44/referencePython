'''
Created on Nov 17, 2018

@author: domje
'''
import random


WORDS = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "India"]

while WORDS:
    word = random.choice(WORDS)
    print(word)
    WORDS.remove(word)
    
