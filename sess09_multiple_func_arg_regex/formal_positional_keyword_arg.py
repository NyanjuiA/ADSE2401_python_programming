# Python script to demonstrate the use of formal, positional and keyword arguments in a function

# function definition
def profile(name, *args, **kwargs):
    print(f"Name : {name}") # formal argument
    if args:
        print(f"Hobbies: ") # positional variable argument(s)
        for hobby in args:
            print(f"- {hobby}")
    if kwargs:
        print(f"Other info: ") # Keyword variable argument(s)
        for key, value in kwargs.items():
            print(f"- {key}: {value}")

# Function call/invocation
profile("Nyanjui", "Cooking", "Reading", "Travelling", gender="Male", age=16,
        password="78ha;df;!", job="IT Lecturer", city="Mombasa", country="Kenya")

# Formal arguments are defined in the function signature(name)
# *args: collects positional arguments as a tuple
# **kwargs: collects extra keyword arguments as a dictionary