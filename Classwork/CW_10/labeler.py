# labeler.py
# Demonstrates using lebels.

from tkinter import *

# Creating a base (root) window.
root = Tk()
root.title("This is a label")
root.geometry("250x50")

# A frame is created inside the window to accommodate other elements.
app = Frame(root)
app.grid()

# Creating a label inside the frame.
lbl = Label(app, text="That is me!")
lbl.grid()

# Start of the event cycle.
root.mainloop()
