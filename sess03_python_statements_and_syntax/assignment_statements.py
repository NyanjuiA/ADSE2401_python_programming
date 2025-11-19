# Python script to demonstrate assignment statements

# Basic assignment
num1 = 5
spam = 'Yum'
print(f"The contents of 'num1' and 'spam' are {num1} and {spam}")

# Tuple assignment (positional)
spam, ham = 'Spam','YUM'
print(f"The contents of 'spam' and 'ham' variables after tuple assignment "
      f'are "{spam}" and "{ham}"')

# List assignment (positional)
[car, drink] = ["CX-5", "juice"]
print(f"The contents of 'car' and 'drink' variables after list assignment "
      f'are "{car}" and "{drink}"')

# Sequence assignment for numeric values (used on iterables & strings)
first_num, second_num, third_num, fourth_num = [5,8,4,7]
print(f"The contents of 'first_num', 'second_num', 'third_num' and 'fourth_num' variables \n"
      f"assigned using sequence assignment are: {first_num, second_num, third_num, fourth_num}")

# Sequence assignment for alphanumeric values
first_char, second_char, third_char, fourth_char = "Cx-5"
print(f"The contents of 'first_char', 'second_char', 'third_char' and 'fourth_char' variables \n"
      f"assigned using sequence assignment are: {first_char, second_char, third_char, fourth_char}")

# Extended sequence assignment for numeric values (used on iterables & strings)
first_num, second_num, *other_nums, eighth_num = [5,8,4,7,12,3,1,12]
print(f"The contents of 'first_num', 'second_num', 'other_nums' and 'eighth_num' variables \n"
      f"assigned using extended sequence assignment are: "
      f"{first_num}, {second_num}, {other_nums},  and {eighth_num}")

# Extended sequence assignment for alphanumeric values
first_char, second_char, *other_chars, eighth_char = "Meatball"
print(f"The contents of 'first_char', 'second_char', 'other_char' and 'eighth_char' variables \n"
      f"assigned using extended sequence assignment are: "
      f"{first_char, second_char, other_chars, eighth_char}")

# Multiple target assignment
print(f"The contents of 'first_num', 'second_num', and 'third_num' variables before multiple "
      f"target assignment are {first_num, second_num, third_num}")
first_num = second_num = third_num = 8
print(f"The contents of 'first_num', 'second_num', and 'third_num' variables after multiple "
      f"target assignment are {first_num, second_num, third_num}")

# Augmented assignment (shorthand assingment in C-based languages)
second_num += 2 # same as second_num = second_num + 2
print(f"After incrementing/adding 'second_num' using the augmented assignment (+=), we get:{second_num}")