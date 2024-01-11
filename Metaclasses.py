from typing import *
import types

# Everything in python is an object, including classes:

class MyClass:
    pass

class_instance = MyClass()  # New object which is an instance of MyClass
class_obj= MyClass          # MyClass object (the class' instance)

# Python allows us to create classes at runtime, using the 'type' keyword

my_runtime_class = type("MyRuntimeClass", (), {"my_var":10})

# And we can create instances of this new class like we would any other class (using the 'call' operator)
my_runtime_class_instance = my_runtime_class()

# Note that writing 'class MyClass' in a python file is the same as calling type("MyClass", (), {}). This is important,
# because it tells us that all class objects are created by the 'type' class.
# For that reason, 'type' is a metaclass. It's the object that creates classes. Think of it as the class' class, or a class factory:

print(class_instance.__class__)  # <class '__main__.MyClass'>
print(class_instance.__class__.__class__)  # <class 'type'>

# You can create a custom metaclass, in case you want to override how a class gets created (not instances of the class, the class object itself!)
# For example, say you wanted to rename all methods in your class to uppercase, you could do that with a metaclass. Here's how:

class UppercaseMeta(type):  # Note that since 'type' can create classes, we must leverage its behaviour for our own metaclass

    def __new__(mcs, class_name:str, bases: tuple[type, ...], attributes: dict[str, Any]):

        uppercase_attrs : dict[str, Any] = { }

        for attr_name, attribute in attributes.items():
            if isinstance(attribute, types.FunctionType):
                uppercase_attrs[attr_name.upper()] = attribute
            else:
                uppercase_attrs[attr_name] = attribute

        return type(class_name, bases, uppercase_attrs)

class SomeClassWithMeta(metaclass = UppercaseMeta):

    def my_method(self):
        print("My method was called!")

    def my_other_method(self):
        print("My other was called!")


s = SomeClassWithMeta

print(s.__dict__)

instance = SomeClassWithMeta()
instance.MY_METHOD()    # Works!
instance.my_method()    # Throws an AttributeError: 'SomeClassWithMeta' object has no attribute 'my_method'
