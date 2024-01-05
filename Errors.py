def add(n1, n2):
    try:
        result = n1 + n2
    except:
        print(f"Failed to add '{n1}' with '{n2}'!")
    else:   # only runs if no exceptions are caught!
        print("No exceptions were thrown!")
        print(f"{n1} + {n2} = {result}")

def ask_for_int():
    
    while True:
        try:
            result = int(input("Please provide a number: "))    # Will return user input as string
        except ValueError:
            print("That was not a number!")
        else:
            return result

number1 = 10
number2 = ask_for_int()    

add(number1, number2) # Throws a TypeError: Can't add int + string


