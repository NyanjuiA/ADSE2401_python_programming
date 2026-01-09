# Python script to demonstrate how to handle multiple exceptions

try: # Code that may raise error(s)/exception(s)
    num_list = [3,5,8]
    # Try to display a number at an invalid index
    print(f"Value at index 7 is: {num_list[7]}")

    # Other possible exceptions
    num_list + 5 # Type error as you cannot sum an integer and a list
    num_list.remove(4) # Value error as the list doesn't contain number 4

    # Attempt integer division by zero
    quotient = 12 / 0

# Handle the above exceptions
except IndexError:
    print(f"Error: The index you tried to access is out of range")
except TypeError:
    print(f"Error: Sorry, you cannot add an integer and a list.")
except ValueError:
    print(f"Error: Sorry the list doesn't contain number 4.")
except ZeroDivisionError:
    print(f"Error: Attempted integer division by zero. Kindly change "
          f"the denominator to a non-zero number.")
