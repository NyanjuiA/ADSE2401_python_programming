# Python script/file to unpickle the person's details from the
# 'person_os.txt' file and display them

# import the required modules
import pickle,os

# Variable to hold the path to the 'person_os.txt' file
file_path = os.path.abspath(os.path.join(os.getcwd(), "..", "files",'person_os.txt'))

# List that will hole the Person objects from the 'person_os.txt' file
persons = []

# Open the 'person_os.txt' file and read its contents
with open(file_path,'rb') as f:
    while True:
        try:
            unpicked_person = pickle.load(f)
            persons.append(unpicked_person)
        except EOFError:
            break # End of file reached

# Access and display the unpickled person's details/attributes
if persons:
    print("Detail of the persons in the 'person_os.txt' file:")
    for index,person in enumerate(persons,start=1):
        print(f"Person {index}: Name: {person.name}, Age: {person.age}")
else:
    print("No person records in the 'person_os.txt' file.")