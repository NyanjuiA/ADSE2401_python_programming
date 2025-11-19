"""
Python Dictionaries
This is a built in data type that represents a collectio of key-value pairs, like a dictionary,
where each word has a corresponding definition.
Dictionaries are unordered, mutable and can store elements of different types.
Each element in a dictionary is accessed by its key rather than its index.
Dictionaries are created using {} curly brackets/braces.
Some dictionary operations are given below:
"""

# Student dictionary declaration
student = {"name":'Abigail', "age":25, "major":'Computer Science'}

# Display the length (number of key-value pairs) of the student dictionary
print(f"The number of key-value pairs in the 'student' dictionary is: {len(student)}")

# Fetch and display a view object (method to get the keys or values from a dictionary)
# of the keys in the 'student' dictionary
print(f'The keys from the "student" dictionary are:\n{student.keys()}')

# Fetch and display a view object of the values in the 'student' dictionary
print(f'The values from the "student" dictionary are:\n{student.values()}')

# Fetch and display a view object of the contents in the 'student' dictionary
print(f'The contents from the "student" dictionary are:\n{student.items()}')

# Get and display a value using its key from the 'student' dictionary
print(f'The key "name" in the "student" dictionary points to: {student["name"]}') # student.get("name")

# Remove and display the contents of a given key when it exists in a dictionary,
# else return/give back an optional default value
phone_no = student.pop("phone_no","Not Specified")
print(f"The value of 'phone_no' in the 'student' dictionary is {phone_no}.")

# Remove and display the contents of the last key-value pair in the 'student' dictionary
print(f"The last key-value pair in the 'student' dictionary is {student.popitem()}.")

# Update/modify and display the contents of the 'student' dictionary
student.update({"age":21, "grade":'A',"phone":"07123458"})
print(f"The updated contents fo the 'student' dictionary are:\n{student.items()}") # or {student}

# Create a copy of the "student" dictionary
copy_of_student = student.copy()
print(f"The contents of 'copy_of_student' dictionary are:\n{copy_of_student}")

# Fetch and return the value associated with a given key, and when not found assign it with a default value
major = student.setdefault("major",'Not defined')
print(f"The value of the key 'major' in the 'student' dictionary is: {major}.")

# Create and display a new dictionary for the keys of an existing dictionary
new_student = dict.fromkeys(student.keys()) # new_student = dict.fromkeys(["name","age","grade","phone"])
print(f"The key-value pairs in the 'new_student' dictionary are:\n{new_student}")

# Delete a specific key-value pair from the 'student' dictionary
# and display the remaining key-value pairs
del student['grade']
print(f"After removing/deleting the 'grade' key from the 'student' dictionary, the remaining key-value"
      f" pairs are:\n{student}")

# Find out and display whether a given key exists/is present in a dictionary
print(f'The key "age" is present in the "student" dictionary: {"age" in student}')
print(f'The key "grade" is present in the "student" dictionary: {"grade" in student}')

# Remove all the content from the student dictionary and display
student.clear()
print(f"After clearing the 'student' dictionary, we get:\n{student}")