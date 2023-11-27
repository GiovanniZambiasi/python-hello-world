class ClassName():

    def __init__(self, someArg, someOtherArg):
        self.someArg = someArg              # Member variables are implicitly declared via assignments in the constructor just like these
        self.someOtherArg = someOtherArg
        

instance = ClassName("Hello", 10)

class Animal():

    def __init__(self, name):
        self.name = name

    def who_am_i(self):
        print("I am an animal")

    def speak(self):
        raise NotImplementedError(f"Unimplemented speak called on type '{type(self)}'")

class Dog():

    # Class-object attributes are class-level constants
    species = "mammal"

    def __init__(self, breed, name, has_spots):
        Animal.__init__(self, name)       # Inheritance can be implicit by calling base constructor
        self.breed = breed
        self.has_spots = has_spots

    def speak(self):        
        print(f"{self.name}: Woof!")

    def who_am_i(self):     # Method can be overwritten
        print("I am a dog") 

my_dog = Dog("Caramel stray", "Douglas", True)
my_dog.speak()
my_dog.who_am_i()

class Cat(Animal):      # Inheritance can also be specified here

    # Constructor not always needed (since Cat doesn't have ctor, Animal's ctor will be used)

    def speak(self):        
        print(f"{self.name}: Meow!")

my_cat = Cat("Felix")
my_cat.speak()

for pet in [my_cat, my_dog]:
    print(type(pet))
    pet.speak()     # Polymorphic method 'speak' can be called for cats and dogs

def pet_speak(pet):
    pet.speak()

# The following method calls will be polymorphic: The dog will bark, and the cat will meow
pet_speak(my_dog)
pet_speak(my_cat)