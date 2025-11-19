# Python script demonstrating how to import a module and use its code in the current script.

# Import (bring in) the code from the greetings module
from greetings import greet

# prompt the user for their name
username = input(f"Please enter your name:\n")

# Use the function from the greetings module to greet the user
print(greet(username))