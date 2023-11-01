myFile = open("my_file.txt")        # Opens file at location (or throws error if not found). Absolute path can be used
print(myFile.read())
print(myFile.read())    # Second read returns empty, because 'myFile's read location is already at the end of the file
myFile.seek(0)          # Resets 'myFile's read location to the start of the file

contents = myFile.read()
print(contents)

myFile.seek(0)
lines = myFile.readlines()  # Returns a list of lines in the file
print(lines)

myFile.close()      # Releases file to be accessible by the OS

with open("my_file.txt") as myFileTemp:     # Creates a temporary 'myFileTemp' variable, and automatically closes the file when it goes out of scope 
    contents = myFileTemp.read()

print(contents)
    
with open("my_new_file.txt", mode = 'w') as myFileTemp:     # Mode = 'w' opens the file for writing (and creates new file if needed)
    myFileTemp.write("Hey!\n\nThis is a new file\n\nBest regards\nGio")

import os
currentPath = os.getcwd()
print(currentPath)          # To get the current path, regardless of OS
