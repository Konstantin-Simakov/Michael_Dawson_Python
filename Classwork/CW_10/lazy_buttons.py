# lazy_buttons.py
# Demonstrates creating buttons.

from tkinter import *

# Creating a base (root) window.
root = Tk()
root.title("Lazy buttons")
root.geometry("250x125")

# A frame is created inside the window to accommodate other elements.
app = Frame(root)
app.grid()

# Creating a button inside the frame.
bttn_1 = Button(app, text="I do nothing!")
bttn_1.grid()

# Creating a second button inside the frame.
bttn_2 = Button(app)
bttn_2.grid()
bttn_2.configure(text="And me too!")

# Creating a third button inside the frame.
bttn_3 = Button(app)
bttn_3.grid()
bttn_3["text"] = "And me!"

# Start of the event cycle.
root.mainloop()
