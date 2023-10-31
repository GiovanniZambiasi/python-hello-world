myStr = "Hello World!"

print(myStr)
print(myStr[0])         # H
print(myStr[0:-1:1])    # Slicing: Copy every character from 0 to -1 (last index, exclusive) with a step of one
print(myStr[3:])        # Copy every char from 3 till the end of the string
print(myStr[0:5])       # Copy every char from 0 to 4
print(myStr[::2])       # Copy every 2 chars from 0 till the end