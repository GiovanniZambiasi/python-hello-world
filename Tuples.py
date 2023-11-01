myTuple = (10, "Hello")
print(f"Tuple is {myTuple[0]}, {myTuple[1]}")
#myTuple[0] = 10            # Error: Tuples are immutable in python

t = ('a', 'a', 'b')
print(t.count('a'))     # How many 'a's in tuple
print(t.index('b'))     # Returns index of 'b' in tuple

# In python, tuples are basically immutable lists. It's a convenient way to pass objects around without allowing them to be changed
