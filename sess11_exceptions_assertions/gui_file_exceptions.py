# Python file to demonstrate handling multiple exceptions in a GUI program
# to read and display file contents

# Import the required modules
import tkinter as tk
from tkinter import filedialog, messagebox
import sys


# Function to process the file and calculate the average
def process_file():
    file_name = entry.get()  # Get the file name from the text entry field
    result_label.config(text="")  # Clear previous results/answer

    try:
        # Main action: open the file, read the first line as an integer and perform division
        with open(file_name, 'r') as file:
            # divisor = int(file.readline().strip()) # could raise ValueError
            # total_score = 100 # Placeholder for total score
            # average = total_score / divisor # could raise ZeroDivisionError

            # Get the file content
            content = file.read().strip()

            if not content:  # When the file is empty
                raise ValueError("The file is empty")

            # Replace commas with spaces then split
            values = content.replace(",", " ").split()

            # Convert to floats (or int if you prefer)
            numbers = [float(value) for value in values]

            if len(numbers) == 0:  # When the file doesn't contain numbers
                raise ValueError("There no numbers in the file.")

            average = sum(numbers) / len(numbers)
    except FileNotFoundError:
        # Handle the case when the file doesn't exist
        result_label.config(text=f"Error: file '{file_name}' not found. Kindly check path")

    except (ValueError, ZeroDivisionError):
        # Handle invalid integer values or division by zero '0'
        result_label.config(text=f"Error: File must contain a non-zero integer(s)")

    except OSError as os_error:
        # Handle other file related issues (e.g., permission errors)
        result_label.config(text=f"Error: File access error:\n{os_error}")

    # Handle all other unexpected errors/exceptions
    except:
        result_label.config(text=f"Unexpected error occurred. Please try again.")
        # In a full-fledged application, you can log the errors here

    else:
        result_label.config(text=f"Success! The average score is {average:.2f}.")


# Function to open a file dialog and populate the entry field
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        entry.delete(0, tk.END)  # Cleare the current entry
        entry.insert(0, file_path)  # Set the entry to the selected file path


# Create the main TKinter window
root = tk.Tk()
root.title('File Reader - Average Score Calculator')
root.geometry('600x400')  # Set the window size

# Create and pack GUI elements
tk.Label(root, text="Enter path to score file or browse:").pack(padx=10, pady=10)

# Frame for entry and browse button
entry_frame = tk.Frame(root)
entry_frame.pack(pady=5)

# Text entry for file name
entry = tk.Entry(entry_frame, width=45)
entry.pack(side=tk.LEFT, padx=5, pady=5)

# Browse button
tk.Button(entry_frame, text="Browse", command=browse_file).pack(side=tk.LEFT)

# Process button to trigger file reading
tk.Button(root, text="Process File", command=process_file).pack(pady=10)

# Label to display the results of error messages
result_label = tk.Label(root, text="", wraplength=450)
result_label.pack(pady=10)

# Start the application
root.mainloop()
