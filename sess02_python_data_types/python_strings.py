# Python script to demonstrate strings and string functions in Python

# Declare a string variable
string_var = "hello Nyanjui from Python programming"

# Display the string variable withe first letter in uppercase using % and an f-string
print("'string_var' with the first letter capitalised is: %s" % string_var.capitalize())
print(f"'string_var' with the first letter capitalised is: {string_var.capitalize()}")

# Display the type of 'string_var'
print(f"The type of 'string_var' is: {type(string_var)}")

# Display the contents of 'string_var' in uppercase
print(f"The content of 'string_var' in upper case is: {string_var.upper()}")

# Display the contents of 'string_var' in lowercase
print(f"The content of 'string_var' in lower case is: {string_var.lower()}")

string_2_center = "Programming"
# Center the above text with a specified width and given fill character
print(string_2_center.center(32,"="))

# Count & display the number of times a character appears in string ('o' in 'string_var')
print(f"The letter 'o' appears {string_var.count('o')} times in '{string_var}'")

# Display the highest and lowest alphabetical characters (using ASCII codes) in string_var
print(f"The highest and lowest alphabetical characters in '{string_var}' are:"
      f" '{max(string_var)}' & '{min(string_var)}' respectively. ")

# Replace the 'he' with 'He' and 'Python' with 'C#'
new_str = string_var.replace("he", "He")
new_str = new_str.replace("Python", "C#")

# Display the replaced/modified string
print(f"The modified contents of 'string_var' are: '{new_str}'")

# Declare nother string variable for more string operations
my_string = "  Hello, World 123   "

# get and display the number of characters using len()
print(f"Length of the string \n'{my_string}' is: {len(my_string)} characters")

# isalnum() - checks if all characters are alphanumeric (no spaces, symbols)
print(f"Is the string \n{my_string} alphanumeric? {my_string.isalnum()}")

# islower() - checks if all alphabetic characters are lowercase
print(f"Is the string \n{my_string} all lowercase? {my_string.islower()}")

# isupper() - checks if all alphabetic characters are uppercase
print(f"Is the string \n{my_string} all uppercase? {my_string.isupper()}")

# lstrip() - Removes any leading whitespace (from the left)
print(f"Remove the leading spaces from '{my_string}' to get: \n{my_string.lstrip()}")

# rstrip() - Removes any leading whitespace (from the right)
print(f"Remove the trailing spaces from '{my_string}' to get: \n{my_string.rstrip()}")

# strip() - Removes any leading and trailing whitespace (from the left and right)
print(f"Remove the leading and trailing spaces from '{my_string}' to get: \n{my_string.strip()}")

# endswith() - checks if the specified string ends with the specified substring (suffix)
print(f"Does the string '{my_string}' end with '123'? {my_string.strip().endswith('123')}")

# find() - locates the first occurence of the specified substring
print(f"The first occurence of the string 'World' in {my_string} is at index: "
      f"{my_string.find('World')}")

# index() - finds the first occurence of the substring, raises error when not found
print("Index of 'World' :", my_string.index('World'))

# count() - counts the number of occurences of the substring or character
print(f'The number of occurences of "or" in "{my_string}" is {my_string.count("or")}')

# rfind() - finds the last occurence of the specified substring
print(f"The last occurence of 'l' in '{my_string}' is : '{my_string.rfind('l')}'")

# rfind() - finds the last occurence of the specified substring, raises error when not found
print(f"The last index of 'l' in '{my_string}' is at index : '{my_string.rindex('l')}'")

# startswith() - checks if the string start with the given substring (prefix)
print(f'Does the string "{my_string}" start with "   Hello"? {my_string.startswith("  Hello")}')