def hello_world():  # 'def' keyword used to define a function
    '''
    Summary of function!
    '''
    print("Hello world!")

hello_world()

def print_hello_name(name='Default'): # Default ars are supported
    '''Prints "Hello + name"'''
    print(f"Hello {name}!")

print_hello_name("Jorge")

def add_args(lhs, rhs):
    return lhs+rhs
 
result = add_args(10, 20.5)
print(f"Result is {result}")

def is_even(num):
    return num % 2 == 0

def is_even_list(list):
    for element in list:
        if(is_even(element)):
            return True

    return False    

list = [79, 43, 25, 34]
print(is_even_list(list))

work_hours = [('Ezio', 115), ("Tiago", 54), ("Henrique", 125)]

def find_employee_of_the_month(worker_hours):
    max_hours = 0
    best_employee = 'N/A'

    for employee, hours in worker_hours:
        if(hours > max_hours):
            max_hours = hours
            best_employee = employee
    
    return (best_employee, max_hours)

name, hours = find_employee_of_the_month(work_hours)
print(f"Employee of the month is {name} ({hours}h worked)")