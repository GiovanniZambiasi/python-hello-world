helloWorld = "Hello World!"

print(helloWorld)
print(helloWorld[0])         # H
print(helloWorld[0:-1:1])    # Slicing: Copy every character from 0 to -1 (last index, exclusive) with a step of one
print(helloWorld[3:])        # Copy every char from 3 till the end of the string
print(helloWorld[0:5])       # Copy every char from 0 to 4
print(helloWorld[::2])       # Copy every 2 chars from 0 till the end
print(helloWorld[::-1])      # Cleverly reverses a string

name = "Sam"
# name[0] = 'P'         # Won't work, strings are immutable in python
lastLetters = name[1:]
name = 'P' + lastLetters
print(name)             # Simple string concatenation using + operator

letter = 'z'
letter = letter * 10    # Multiplication works to concatenate N times
print(letter)

print(helloWorld.split())   # Splits string using whitespace as the divider
print(helloWorld.split('o')) # Splits string using o as the divider
