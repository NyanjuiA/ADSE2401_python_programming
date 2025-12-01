# Python tkinter script/file with a label and button to display a message on the screen
# once the button is clicked.

# Import the tkinter module
import tkinter as tk

# Instantiate a tk object
root = tk.Tk()

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y positions to center the window/GUI
x = (screen_width - 640) // 2
y = (screen_height - 480) // 2

# Set the dimensions of the window
root.geometry('640x480+{}+{}'.format(x, y))

# Create a label with it's content/text and font size
label = tk.Label(root, text='Hello World!', font=('Arial', 25 ), fg='red')
label.pack()

# Function definition
def toggle_text():
    if label['text'] == 'Hello World!':
        label['text'] = 'Bye World!'
    else:
        label['text'] = 'Hello World!'

# Create a button with its content and font size
button = tk.Button(root, text='Toggle Text', command=toggle_text, # function invoked when button is clicked
font=('Arial', 25), fg='blue' )
button.pack()

# Run the application
root.mainloop()

