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
# An anonymous/lambda function is a way to write small compact functions quickly. They are often
# used when you need a simple function for a short period and don't want to write a full function
# using the def keyword
plus_five = lambda num: num + 5 # use a lambda to add 5 to a number
print(f"The sum of 7 and 5 using a lambda(anonymous function) is: {plus_five(7)}")

# Same functionality as the lambda above but using a full function
def add_five(num):
    return num + 5 # define a function to add 5 to the value passed in

# call/invoke the add_five() function
print(f"The sum of 2 and 5 using a normal function is: {add_five(2)}")

# Anonymous/lambda function to get the difference between 2 numbers
difference = lambda num1, num2: num1 - num2

# Sample usage of the above lambda
print(f"The difference between 3 and 5 using a lambda(anonymous function) is: {difference(3,5)}")

# Function with a varying number of parameters
# Define a function that accepts a varying number of parameters
def get_sum(*values):
    # sum = 0
    # for value in values:
    #     sum += value
    # return sum
    """
    This functions returns the sum of all the numbers/values passed in.

    Args:
        *values: Variable number of values to be totalled/summed.

    Returns:
        int or float: The sum of all the numbers/values passed in as an integer/float.

    Raises:
        TypeError:If any of the values/numbers passed in are not numeric.

    Examples:
        >>> get_sum(1, 2, 3)
        6
        >>> get_sum(3.5,2.1,1.4)
        7.0
        >>> get_sum(1, 2, "3")
        TypeError: All the values provided must be numbers/numeric.
    """
    try:
        return sum(values)
    except TypeError as e:
        raise TypeError("All the values provided must be numbers/numeric.") from e



# Create the entry point to our program
if __name__ == "__main__":
    # Create a list of numbers and sum them using the get_sum() function
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"The sum of the first ten numbers is: {get_sum(*num_list)}")
    nums_with_decimals = [4.5, 1.5, 2.0]
    print(f"The sum of 4.5, 1.5 and 2.0 is: {get_sum(*nums_with_decimals)}")
    mixed_nums = [2, 5, "7"]
    # print(f"The sum of 2, 5 and '7' is: {get_sum(*mixed_nums)}")
