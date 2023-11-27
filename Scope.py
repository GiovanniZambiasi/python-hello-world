x = 50

def local_assignment():
    x = 100     # x is assigned locally (new x var with value 100 is created)
    print(f"X is {x}") 

local_assignment()
print(f"After calling '{local_assignment.__name__}' val is {x}")

def global_assignment():
    global x    # Marks variable x for global assignment (will use previously declared global x)
    x = 100     # x is assigned globally

global_assignment()
print(f"After calling '{global_assignment.__name__}' val is {x}")