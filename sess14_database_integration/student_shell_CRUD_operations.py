# Python script to demonstrate MySQL database CRUD operations on the command line/shell
# NB: Ensure you've installed the mysql python connector => pip install mysql-connector-python

# Import the required modules
import mysql.connector
from db_conn import db_config
from student import Student

# Function to connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to python232401 MySQL database!") # remove in production code
            return connection
    except mysql.connector.Error as err:
        print(f"Error: Unable to connect to MySQL:\n{err}")
        return None

# Function to close the db connection
def close_connection(connection):
    if connection: # or connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

# Function to get/fetch student details from the python232401 database
def read_students(connection):
    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM student"
        cursor.execute(select_query)
        students = cursor.fetchall()
        for student in students:
            student = Student(*student)
            print(student)
    except mysql.connector.Error as err:
        print(f"Error: Unable to get student details from MySQL:\n{err}")

# Function to insert/add a student record into the student database
def insert_student(connection, student):
    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO student(StudentNO,Name,Birthdate,Gender,City)
        value(%s,%s,%s,%s,%s)
        """
        student_data = (student.student_no, student.name, student.birthdate, student.gender, student.city)
        cursor.execute(insert_query, student_data)
        connection.commit() # Save/store/persist/commit the changes to the python232401 database
        print(f"Student {student.name} inserted successfully") # remove in production code
    except mysql.connector.Error as err:
        print(f"Error: Unable to insert student details into MySQL:\n{err}")
    finally:
        cursor.close() # Close the cursor
        # close_connection(connection)  # Close the database connection

# Function to update/modify student details
def update_student(connection, student):
    try:
        cursor = connection.cursor()
        update_query = """
        UPDATE student
        SET Name=%s,Birthdate=%s,Gender=%s,City=%s
        WHERE StudentNo=%s
        """
        student_data = (student.name, student.birthdate, student.gender, student.city, student.student_no)
        cursor.execute(update_query, student_data)
        connection.commit()
        if cursor.rowcount > 0:
            print(f"Student {student.name}'s record updated successfully")
        else:
            print(f"Error: Student {student.name}'s record could not be updated or found!")
    except mysql.connector.Error as err:
        print(f"Error: Unable to update student details into MySQL:\n{err}")
    finally:
        cursor.close() # Close the cursor
        # close_connection(connection)  # Close the database connection

# Function to delete a student's record from the database
def delete_student(connection, student_no):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM student WHERE StudentNo=%s"
        cursor.execute(delete_query, (student_no,))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"Student {student_no} deleted successfully")
        else:
            print(f"Error: No record with the given student number was found!\nKindly"
                  f" check the student number and try again.")
    except mysql.connector.Error as err:
        print(f"Error: Unable to delete student details from the database:\n{err}")
    finally:
        cursor.close() # Close the cursor
        # close_connection(connection)  # Close the database connection

# Run the script to perform CRUD operations
if __name__ == '__main__':
    connection = connect_to_database()

    if connection:
        # Create some student objects
        new_student1 = Student('EICN_ADSE232401_S009','Peter Njuguna',
                               '1996-04-09','M','Githunguri')
        dummy_student = Student('EICN_ADSE232401_S010','Some Dummy Student',
                                '2010-08-11','M','Nyali')
        # Get all the students from the database
        read_students(connection)

        # Add/Insert the above student's details to the python232401 database
        # insert_student(connection, new_student1)
        # insert_student(connection, dummy_student)

        # update the dummy student's details
        dummy_student = Student('EICN_ADSE232401_S010', 'Updated Dummy Student',
                                '2001-08-11', 'M', 'Nyali')
        update_student(connection, dummy_student)

        read_students(connection)

        # Delete the dummy student's record
        delete_student(connection, dummy_student.student_no)


    close_connection(connection)