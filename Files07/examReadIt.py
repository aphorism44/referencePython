'''
Created on Nov 17, 2018

@author: domje
'''

#open and close file
text_file = open("read_it.txt", "r")
text_file.close()

#read chars from file
text_file = open("read_it.txt", "r")
print(text_file.read(1)) #FIRST char
print(text_file.read(5)) #NEXT 5 chars
text_file.close()

#read whole file at once
text_file = open("read_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

#read chars from a line
text_file = open("read_it.txt", "r")
print(text_file.readline(1)) #FIRST char of Line 1
print(text_file.readline(5)) #NEXT 5 chars of Line 1
text_file.close()

#read one line at a time
text_file = open("read_it.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

#read entire file into a list
text_file = open("read_it.txt", "r")
lines = text_file.readlines()
print(lines) #a list []
print(len(lines)) #3
for line in lines:
    print(line)
text_file.close()


#loop through lines of a file
text_file = open("read_it.txt", "r")
for line in text_file:
    print(line)
text_file.close()