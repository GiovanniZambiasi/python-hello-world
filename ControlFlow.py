if True:                # Indentation defines scope in python statements. ':' marks the end of the 'if' statement
    print("True!")
else:
    print("Not true!")

## For loops

myIterable=[1,2,3,4,5,6,7,8,9]

for element in myIterable:
    print(element)

for element in myIterable:
    if element % 2 == 0:
        print(element)
    else:
        print(f"{element} (odd)")

for num in range(10):       # Iterates through all numbers from 0 to 9
    print(num)

for num in range(0, 10, 2): # 'range()' supports a custom step (2 in this example)
    print(num)

for letters in 'Hello World!':   # Strings are iterable
    print(letters)

for item in (10, "Hey!", 32.4): # Tuples are iterable
    print(item)

for index, letters in enumerate("Hello world!"):
    print(f"[{index}] {letters}")         # 'enumerate()' creates index/element tuples out of collections

tuples = [(1,2), (3,4), (5,6)]  

for (a, b) in tuples:       # Tuples can be unpacked in a for loop, to acces the individial members of the tuple
    print(a)
    print(b)

myDictionary = { "k1":1, "k2":2, "k3":3 }

for key in myDictionary:    # By default, dictionaries are iterated via keys
    print(key)

for key, value in myDictionary.items():    # Tuple unpacking can be used to iterate over key/value pairs
    print(f"{key} : {value}")

## While loops

x = 0

while x < 5:
    print(x)
    x += 1
else:                       # Python whiles support "else"
    pass

while False:
    pass        # "Pass" is mostly a placeholder keyword for control flow. 'continue' and 'break' are also valid keyword for control flow

## Misc

numbers = [1,2,3]
letters = ['a','b','c']

for num, letter in zip(numbers, letters):
    print(f"{num} ~ {letter}")  # 'zip()' function combines two separate lists into tuples


if 'x' in ["Hello world!"]:         # "in" keyword can be used to check if container contains element
    pass        
