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

