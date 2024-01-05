# Modules are a fancy name for "some python script". Modules cann be aggregated into a package (as seen in GiosPackage/)

# We can import specific functions from modules:
from SomeModule import some_func

some_func()

# An alternative way to call this function is as follows:
import SomeModule
SomeModule.some_func()

# We can also import everything from a module using this syntax
from SomeModule import *

some_other_func()

# Importing modules from a package works like this:
from GiosPackage import GiosModuleMain

# Functions in modules are called using this syntax (as if the module was a class object)
GiosModuleMain.report_main()

# And if you have any sub-packages, you can import them like this:
from GiosPackage.GiosSubPackage import GiosSubModule

GiosSubModule.sub_report()

# __name__ is a built-in variable that stores the name of an object (in this case, the module itself). Usually, this holds the module name ('Modules', in this case)
# however, when a python module is run directly (such as when running 'python Modules.py' from the cmd), the __name__ variable for this specific module gets overwritten
# to "__main__". So, if we want to check if a particular module is being run directly (as opposted to being imported from some other module), we can perform the following check:
if __name__ == "__main__":
    print("I am being run directly!")
else:
    print("I am being imported from another module!")


# Other things (such as modules, functions, classes also have a __name__)
print(GiosModuleMain.__name__)