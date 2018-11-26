'''
Created on Nov 17, 2018

@author: domje
'''

#below line creates new file
text_file = open("write_it.txt", "w")
text_file.write("This is LINE 1\n")
text_file.write("And this is LINE 1\n")
text_file.write("So, this is LINE 3")

text_file.close()

#below will overwrite the whole file
text_file = open("write_it.txt", "w")
lines = [
    "This is the new line 1\n"
    , "And this is the new line 2\n"
    , "Finally, this is the new line 3"
    ]
text_file.writelines(lines)
text_file.close()