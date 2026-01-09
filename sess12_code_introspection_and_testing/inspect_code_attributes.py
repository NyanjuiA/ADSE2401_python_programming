# Python script to demonstate using introspection to display object attributes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello there, my name is {self.name}, and I'm {self.age} years old.")

# Create an instance of the Person class
p1 = Person("Abigail",age=25)
if isinstance(p1, Person):
    print(f"{p1.name} is an instance of the 'Person' class and is {p1.age} years old.")
else:
    print(f"The 'p1' variable is an instance of {type(p1)}")

# Use the dir() method to list the attributes and methods of the 'p1' object
print(f"Attributes and methods of the 'p1' object are:\n{dir(p1)}")