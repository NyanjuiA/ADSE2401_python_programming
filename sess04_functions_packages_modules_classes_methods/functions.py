# This file/script demonstrates defining & calling/invoking user defined functions in Python

# Define a function to display a greeting message when called/invoked
def greeting():  # does not take any parameter(s)
    print("Hello from 'greeting()' funtion!")


# call/invoke the greeting() function
greeting()


# Define a function that accept's the user's name and then greet's them
def greet_user(username):  # accept's a single parameter
    print("Hello %s from Python functions!" % username)


# prompt the user for their name and invoke the above function with the name provided
name = input("Please enter your name:\n")
greet_user(name)


# create a function that accepts two numbers & an operator '+' (default) or 'x' to add
# or multiply them
def add_or_multiply(first_num, second_num, operator = '+'):
    """
    Add or multiply two numbers based on the specified operator.

    This function performs either addition or multiplication on two numeric inputs,
    depending on the value of the ``operator`` parameter. The default operation is addition.

    Parameters
    ----------
    first_num : int or float
        The first number (left operand) in the operation.
    second_num : int or float
        The second number (right operand) in the operation.
    operator : {'+', '*', 'x'}, default '+'
        The operation to perform:
            - '+' : addition (``first_num + second_num``)
            - '*' or 'x' : multiplication (``first_num * second_num``)

    Returns
    -------
    int or float
        The result of the addition or multiplication if a valid operator is provided.

    str
        An error message if an unsupported operator is given.

    Raises
    ------
    None
        The function does not raise exceptions; invalid operators return a descriptive string.

    Examples
    --------
    >>> add_or_multiply(5, 3)
    8
    >>> add_or_multiply(5, 3, '+')
    8
    >>> add_or_multiply(5, 3, 'x')
    15
    >>> add_or_multiply(5, 3, '*')
    15
    >>> add_or_multiply(5, 3, '-')
    "Invalid operator '-', given.\nPlease use '+' or 'x'"
    """
    if operator == '+':
        return first_num + second_num
    elif operator == '*' or operator == 'x':
        return first_num * second_num
    else:
        return f"Invalid operator '{operator}', given.\nPlease use '+' or 'x'"

# call/invoke the add_or_multiply function
print(f"The sum of 3 and 5 is: {add_or_multiply(3,5)}")
print(f"The product of 3 and 5 is: {add_or_multiply(3,5,operator = '*')}")

# Display the documentation string for the add_or_multiply function
print(f"\nThe documentation string for the add_or_multiply function is:\n{add_or_multiply.__doc__}")

# Anonymous function(s)
