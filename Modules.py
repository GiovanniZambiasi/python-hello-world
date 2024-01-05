# Modules are a fancy name for "some python script". Modules cann be aggregated into a package (as seen in GiosPackage/)

# We can import specific functions from modules:
from SomeModule import some_func

some_func()

# Importing modules from a package works like this:
from GiosPackage import GiosModuleMain

# Functions in modules are called using this syntax (as if the module was a class object)
GiosModuleMain.report_main()

# And if you have any sub-packages, you can import them like this:
from GiosPackage.GiosSubPackage import GiosSubModule

GiosSubModule.sub_report()
