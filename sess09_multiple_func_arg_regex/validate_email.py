# Python GUI app to accept an email address from the user and validate it using regex

# import the required modules
import re
import tkinter as tk
from tkinter import messagebox, END

# Function to validate email address
def validate_email():

    email = entry_email.get().strip()
    if email == "": # same as not email
        tk.messagebox.showerror("Missing Email Address",
                                "Please enter the email address to be validated")
        return

    pattern = r"^[a-zA-Z\d.+_-]+@[a-zA-Z\d._]+\.[a-zA-Z]+$"

    if re.match(pattern, email):
        tk.messagebox.showinfo("Valid Email Address",
                               "The email address entered is valid")
    else:
        tk.messagebox.showerror("Invalid Email Address",
                                "The email address entered is not valid")

# Function to clear the email entry control/widget
def clear_text():
    entry_email.delete(0, END)
    entry_email.focus()

# Set up the GUI
root = tk.Tk()
root.title('Validate Email Address')

# Label(s)
label_email = tk.Label(root, text='Enter Email Address')
label_email.grid(row=0, column=0, padx=10, pady=5)

# Entry field(s)
entry_email = tk.Entry(root)
entry_email.grid(row=0, column=1, padx=10, pady=5)

# Button(s)
button_validate = tk.Button(root, text='Validate Email', command=validate_email)
button_validate.grid(row=1, column=0, padx=10, pady=5)

button_clear = tk.Button(root,text="Clear Email",command=clear_text)
button_clear.grid(row=1, column=1, padx=10, pady=5)

# Run the application
root.mainloop()