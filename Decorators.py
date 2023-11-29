## Basics:

from typing import Any


def notifydecorator(func):  # Functions can be used as decorators
    def wrapper(*args, **kwargs):   # Wrapper takes in args and kwargs to enable parameters
        print(f"Function '{func.__name__}' will be called!")
        return func(*args, **kwargs)    # Wrapper must return a value to preserve the original function's return values
    return wrapper  # They must return a callable (in this case, a reference to the wrapper function). When called, the "bar" function below will actually invoke wrapper

@notifydecorator                
def decorated_method(value):
    print(f"Decorated method called with value '{value}'")

decorated_method("Foo")

class classbaseddecorator():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):    # Classes can also be decorators. The __call__ method will be invoked when the decorated method gets called
        print(f"{__name__} decorator executing!")
        return self.func(*args, **kwargs)

@classbaseddecorator    
def decorated_method_class():
    print("Decorated method being invoked!")

decorated_method_class()

## Built-in decorators

class Foo:

    class_var = "Class var!"
    
    def __init__(self) -> None:
        self.instance_var = "Instance var!"
        pass

    @classmethod        # classmethod built-in decorator ensures the "cls" argument received by the method is the original class instance, rather than some arbitrary instance of that class
    def foo(cls, num):
        print(num)

    @staticmethod       # staticmethod decorator ensures the method doesn't run in any instances of the class (and therefore doesn't need 'self' or 'cls' parameters)
    def foo_static(num):
        print(num)

f = Foo()
f.foo(10)
f.foo_static(10)