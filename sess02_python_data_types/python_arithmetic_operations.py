# Python script to demonstrate the various arithmetic operations on numeric values

# Declare and get two values for the user
num1 = int(input("Enter first number to be used in the calculation: \n"))
num2 = int(input("Enter second number to be used in the calculation: \n"))

# Addition
sum = num1 + num2

# Subtraction
difference = num1 - num2

# Multiplication
product = num1 * num2

# Division
floating_division = num1 / num2
integer_division = num1 // num2

# Modulus
modulus = num1 % num2

# Exponentiation
exponent = num1 ** num2

# Display the results
print(f"Addition: {num1} + {num2} = {sum}")
print(f"Subtraction: {num1} - {num2} = {difference}")
print(f"Multiplication: {num1} * {num2} = {product}")
print(f"Floating Division: {num1 / num2}")
print(f"Integer Division: {num1 // num2}")
print(f"Modulus or remainder: {num1 % num2}")
print(f"Exponent: {num1 ** num2}")