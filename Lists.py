myList = [1,2,3]
myList = ["String", 100, 23.2]      # Python lists can hold different object types
print(len(myList))                  # To get length, use the len() method
print(myList[0])

myList = [1, 2, 3]
anotherList = [5,6,7]
myList = myList + anotherList       # Lists can be concatenated
print(myList)
myList[0] = 0       # Lists are not immutable
print(myList)

alphabet = ['a', 'e', 'x', 'b', 'c']
alphabet.sort()
print(alphabet)

## List comprehension

myString = "Hello!"
myList = [letter for letter in myString]    # Iterates through 'myString', and appends 'letter'
myList = [num**2 for num in range(0, 11)]   # From 0 to 10, appends 'num**2'
myList = [num for num in range(0, 11) if(num % 2 == 0)]   # From 0 to 10, appends elements that are even
myList = [num if num % 2 == 0 else 'ODD' for num in range(0, 11)]   # if/else in list comprehension go in the front

celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]    # Given a list of temperatures in celcius, convert each to f and append

