# Mutable vs Immutable is a very important concept in python

# Mutable objects are always treated by reference!

# Ints, strings, floats are IMMUTABLE objects
# Lists, Dictionaries, Sets are MUTABLE objects

# Custom types are treated as MUTABLE by default.
class Foo:

    def __init__(self, v:int) -> None:
        self.v = v

f = Foo(10)
f_copy = f
f_copy.v = 60
print(f.v)  # Value is modified!

# Implementing *true* immutability on custom types is very hard, and beyond my current python capabilities. However, there's a way
# to make a type artificially immutable: Making it a frozen dataclass
from dataclasses import dataclass

@dataclass(frozen=True)     # the 'frozen' property makes it impossible to write to this classe's fields
class ImmutableFoo:
    v : int                 # dataclass attributes makes sure this type contains an __init__ method which takes in an int argument for v

immutable = ImmutableFoo(10)
print(id(immutable))
#immutable.v = 10           # This line would throw a runtime error. Modifying this classe's variables is invalid
copy = immutable
print(id(copy))             # copy's address will be the same as the original though