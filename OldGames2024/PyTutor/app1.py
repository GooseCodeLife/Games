# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define a function to show the popup message
def show_msg():
   messagebox.showinfo("Message","Hey There! I hope you are doing well.")

def foo():
   messagebox.showinfo("You foo!!")

def bar():
   messagebox.showinfo("You bar click!!")

# Add an optional Label widget
Label(win, text= "0", font= ('Aerial 17 bold italic')).pack(pady= 30)

# Create a Button to display the message
ttk.Button(win, text= "Click Here", command=show_msg).pack(pady= 20)

buttonsOperators = ['+','-','*','/']

buttonsNO=[ ]


ttk.Button(win, text= "Foo", command=foo).pack(pady= 20)

ttk.Button(win, text= "Bar", command=bar).pack(pady= 20)

win.mainloop()