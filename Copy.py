# Copying object in python is intrinsically connected to the concept of mutability/immutability
# In Python, strings are immutable:
strings_are_immutable = "José"
print(id(strings_are_immutable))
strings_are_immutable = "ésoJ"      # A New string object needs to be allocated
print(id(strings_are_immutable))    # Printed id is different from before!

lists_are_mutable = [0, 1]
print(id(lists_are_mutable))
lists_are_mutable.append(2)
print(id(lists_are_mutable))        # Printed id DOESN'T change!

# Since mutable objects are treated by-ref, you can modify them from other variables:
list_copy = lists_are_mutable    
list_copy[0] = 3
print(lists_are_mutable)            # Original list WAS modified!

# To *actually* copy a mutable ovject, you can use the 'copy' module:
import copy
list_copy = copy.copy(lists_are_mutable)
list_copy[0] = 99
print(lists_are_mutable)            # Original list keeps original value!

# But what if a mutable object has a nested object that's also mutable?
list_of_lists = [ ['a','b','c'], [1,2,3] ]

shallow_copy = copy.copy(list_of_lists)
shallow_copy[0][0] = 'z'
print(list_of_lists[0])             # Original's list WAS modified!

# That happens because copy.copy() performs a shallow copy. It also contains a 'deepcopy' method:
deep_copy = copy.deepcopy(list_of_lists)
deep_copy[0][0] = 'a'
print(list_of_lists[0])             # Original's list DOESN'T change!

# When sent as arguments, immutable objects are not copied. This makes sure we don't wastefull copy strings and other data types when sending them to functionsn
my_immutable_int = 10

def assign_value(var, value):
    print(id(var))  # my_immutable_int's addres is printed
    var = value
    print(id(var))  # A new object has been created and assigned to var, with a different addres (nothing happened to the original var)

assign_value(my_immutable_int, 99)  # my_immutable_int has kept its original value (and address)
